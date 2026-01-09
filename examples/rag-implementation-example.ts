/**
 * DSIL RAG Implementation Example (TypeScript)
 * ==============================================
 * 
 * This example demonstrates how to implement RAG (Retrieval-Augmented Generation)
 * for DSIL manifests using TypeScript/Node.js.
 * 
 * Requirements:
 * - openai (for embeddings)
 * - chromadb (or other vector database)
 * - dotenv (for environment variables)
 * 
 * Installation:
 *   npm install openai chromadb dotenv
 * 
 * Usage:
 *   npx ts-node rag-implementation-example.ts
 */

import { OpenAI } from 'openai';
import { ChromaClient } from 'chromadb';
import * as fs from 'fs/promises';
import * as path from 'path';
import * as dotenv from 'dotenv';

dotenv.config();

// ============================================================================
// CONFIGURATION
// ============================================================================

const CORE_DSIL_PATH = 'dsil/core.dsil';
const COMPONENTS_DIR = 'dsil/components';
const EMBEDDING_MODEL = 'text-embedding-3-small';
const VECTOR_DB_PATH = './chroma_db';

// ============================================================================
// TYPES
// ============================================================================

interface DSILComponent {
  name: string;
  content: string;
  embedding: number[];
  metadata: {
    component: string;
    type: 'component' | 'pattern';
    category?: string;
    doc?: string;
    props?: string;
    keywords?: string;
    tokens?: number;
  };
}

interface RetrievalResult {
  components: string[];
  content: string;
  mentioned: string[];
  semanticMatches: string[];
}

interface CoreDSIL {
  content: string;
  compact: string;
  meta: {
    name: string;
    version: string;
  };
  tokens: number;
}

// ============================================================================
// DSIL RAG CLASS
// ============================================================================

class DSILRAG {
  private client: OpenAI;
  private chroma: ChromaClient;
  private collection: any;
  private coreDSIL: CoreDSIL;

  constructor(coreDSILPath: string, componentsDir: string) {
    this.client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
    this.chroma = new ChromaClient({ path: VECTOR_DB_PATH });
    this.coreDSIL = this.loadCoreDSIL(coreDSILPath);
    this.initializeCollection(componentsDir);
  }

  private loadCoreDSIL(filePath: string): CoreDSIL {
    const content = fs.readFileSync(filePath, 'utf-8');
    
    return {
      content,
      compact: this.toCompact(content),
      meta: this.parseMeta(content),
      tokens: this.countTokens(content)
    };
  }

  private async initializeCollection(componentsDir: string) {
    this.collection = await this.chroma.getOrCreateCollection({
      name: 'dsil_components',
      metadata: { description: 'DSIL component definitions' }
    });

    // Index components if collection is empty
    const count = await this.collection.count();
    if (count === 0) {
      console.log('Indexing components...');
      await this.indexComponents(componentsDir);
      const newCount = await this.collection.count();
      console.log(`Indexed ${newCount} components`);
    }
  }

  private async indexComponents(componentsDir: string) {
    const files = await fs.readdir(componentsDir);
    const dsilFiles = files.filter(f => f.endsWith('.dsil'));

    if (dsilFiles.length === 0) {
      console.log(`No component files found in ${componentsDir}`);
      return;
    }

    const ids: string[] = [];
    const embeddings: number[][] = [];
    const documents: string[] = [];
    const metadatas: any[] = [];

    for (const file of dsilFiles) {
      const filePath = path.join(componentsDir, file);
      const content = await fs.readFile(filePath, 'utf-8');
      
      const componentName = this.extractComponentName(content);
      if (!componentName) continue;

      const embedding = await this.createEmbedding(content);
      const metadata = this.extractMetadata(content, componentName);

      ids.push(componentName);
      embeddings.push(embedding);
      documents.push(content);
      metadatas.push(metadata);
    }

    if (ids.length > 0) {
      await this.collection.add({
        ids,
        embeddings,
        documents,
        metadatas
      });
    }
  }

  async retrieve(userQuery: string, topK: number = 5): Promise<RetrievalResult> {
    // 1. Extract mentioned components
    const mentioned = this.extractComponents(userQuery);

    // 2. Semantic search
    const queryEmbedding = await this.createEmbedding(userQuery);
    const semanticResults = await this.collection.query({
      queryEmbeddings: [queryEmbedding],
      nResults: topK,
      include: ['documents', 'metadatas']
    });

    // 3. Combine mentioned + semantic matches
    const componentNames = new Set([
      ...mentioned,
      ...(semanticResults.ids[0] || [])
    ]);

    // 4. Retrieve full component definitions
    let retrievedContent = '';
    if (componentNames.size > 0) {
      const retrieved = await this.collection.get({
        ids: Array.from(componentNames),
        include: ['documents']
      });

      if (retrieved.documents && retrieved.documents.length > 0) {
        retrievedContent = retrieved.documents.join('\n\n');
      }
    }

    return {
      components: Array.from(componentNames),
      content: retrievedContent,
      mentioned,
      semanticMatches: semanticResults.ids[0] || []
    };
  }

  async buildSystemPrompt(userQuery: string): Promise<string> {
    const retrieved = await this.retrieve(userQuery);
    const systemName = this.coreDSIL.meta.name;

    let prompt = `You are a frontend developer using the ${systemName} design system.

═══════════════════════════════════════════════════════════════
CORE SYSTEM (Always Available)
═══════════════════════════════════════════════════════════════
${this.coreDSIL.compact}

`;

    if (retrieved.content) {
      prompt += `═══════════════════════════════════════════════════════════════
RETRIEVED COMPONENTS (For This Request)
═══════════════════════════════════════════════════════════════
${this.toCompact(retrieved.content)}

`;
    }

    prompt += `═══════════════════════════════════════════════════════════════
RULES
═══════════════════════════════════════════════════════════════
1. ONLY use components from CORE SYSTEM or RETRIEVED COMPONENTS above
2. If a component is NOT listed above, it does NOT exist - do not use it
3. ALWAYS check @semantics section for component selection decisions
4. Use tokens from @tokens section (e.g., T.spacing.md, T.color.primary)
5. Respect ALL constraints (marked with !)
6. Controlled components (@controlled true) require state management
7. When uncertain which component to use, check @semantics section

═══════════════════════════════════════════════════════════════
COMPONENT SELECTION GUIDE
═══════════════════════════════════════════════════════════════
- Check @semantics section for intent-based component selection
- Use patterns from @patterns when appropriate
- Follow constraints strictly
- Use tokens, not hardcoded values
`;

    return prompt;
  }

  private extractComponents(query: string): string[] {
    const keywordMap: Record<string, string> = {
      'button': 'button',
      'input': 'input',
      'text field': 'text-field',
      'textfield': 'text-field',
      'form': 'form',
      'card': 'card',
      'dialog': 'dialog',
      'modal': 'dialog',
      'select': 'select',
      'dropdown': 'select',
      'checkbox': 'checkbox',
      'radio': 'radio',
      'switch': 'switch',
      'toggle': 'switch',
      'chip': 'chip',
      'snackbar': 'snackbar',
      'toast': 'snackbar',
      'list': 'list',
      'table': 'table',
      'tabs': 'tabs',
      'accordion': 'accordion',
      'menu': 'menu',
      'drawer': 'drawer',
      'bottom sheet': 'bottom-sheet',
      'textarea': 'textarea',
    };

    const found: string[] = [];
    const queryLower = query.toLowerCase();

    for (const [keyword, component] of Object.entries(keywordMap)) {
      if (queryLower.includes(keyword)) {
        found.push(component);
      }
    }

    return [...new Set(found)]; // Remove duplicates
  }

  private async createEmbedding(text: string): Promise<number[]> {
    try {
      const response = await this.client.embeddings.create({
        model: EMBEDDING_MODEL,
        input: text
      });
      return response.data[0].embedding;
    } catch (error) {
      console.error('Error creating embedding:', error);
      // Return zero vector as fallback
      return new Array(1536).fill(0.0);
    }
  }

  private extractComponentName(content: string): string | null {
    const match = content.match(/@component\s+([\w-]+)/);
    return match ? match[1] : null;
  }

  private extractMetadata(content: string, componentName: string): any {
    // Extract @doc
    const docMatch = content.match(/@doc\s+"([^"]+)"/);
    const doc = docMatch ? docMatch[1] : '';

    // Extract props (simplified)
    const propsMatch = content.match(/props:\s*\{([^}]+)\}/s);
    const props: string[] = [];
    if (propsMatch) {
      const propMatches = propsMatch[1].matchAll(/(\w+):\s*\{/g);
      for (const match of propMatches) {
        props.push(match[1]);
      }
    }

    // Determine category
    let category = 'other';
    if (componentName.includes('button') || componentName.includes('link') || componentName.includes('chip')) {
      category = 'action';
    } else if (componentName.includes('input') || componentName.includes('select') || componentName.includes('textarea') || componentName.includes('checkbox') || componentName.includes('radio')) {
      category = 'input';
    } else if (componentName.includes('card') || componentName.includes('container') || componentName.includes('box')) {
      category = 'layout';
    } else if (componentName.includes('dialog') || componentName.includes('modal') || componentName.includes('snackbar') || componentName.includes('toast')) {
      category = 'feedback';
    }

    // Extract keywords
    const keywords = [componentName];
    if (doc) {
      keywords.push(...doc.toLowerCase().split(/\s+/).filter(w => w.length > 4));
    }

    return {
      component: componentName,
      type: 'component',
      category,
      doc: doc.substring(0, 100),
      props: props.slice(0, 5).join(','),
      keywords: keywords.slice(0, 10).join(','),
      tokens: this.countTokens(content)
    };
  }

  private parseMeta(content: string): { name: string; version: string } {
    const nameMatch = content.match(/name:\s*"([^"]+)"/);
    const versionMatch = content.match(/version:\s*"([^"]+)"/);

    return {
      name: nameMatch ? nameMatch[1] : 'unknown',
      version: versionMatch ? versionMatch[1] : '1.0.0'
    };
  }

  private toCompact(content: string): string {
    // Simplified - in production, use proper DSIL converter
    return content;
  }

  private countTokens(text: string): number {
    // Rough estimate: 1 token ≈ 4 characters
    return Math.floor(text.length / 4);
  }
}

// ============================================================================
// USAGE EXAMPLE
// ============================================================================

async function main() {
  console.log('DSIL RAG Implementation Example');
  console.log('='.repeat(60));
  console.log();

  try {
    const rag = new DSILRAG(CORE_DSIL_PATH, COMPONENTS_DIR);
    console.log(`✓ Loaded core DSIL: ${rag['coreDSIL'].meta.name}`);
    
    const count = await rag['collection'].count();
    console.log(`✓ Indexed components: ${count}`);
    console.log();

    // Example query
    const query = 'Create a login form with email and password fields';
    console.log(`Query: ${query}`);
    
    const retrieved = await rag.retrieve(query);
    console.log(`Mentioned: ${retrieved.mentioned.join(', ')}`);
    console.log(`Semantic matches: ${retrieved.semanticMatches.join(', ')}`);
    console.log(`Total retrieved: ${retrieved.components.length} components`);

    const prompt = await rag.buildSystemPrompt(query);
    console.log(`\nSystem prompt length: ${prompt.length} characters`);
    console.log(`Estimated tokens: ~${Math.floor(prompt.length / 4)}`);

  } catch (error) {
    console.error('Error:', error);
    console.log('\nTo use this example:');
    console.log('1. Create a core.dsil file');
    console.log('2. Create a components/ directory with .dsil files');
    console.log('3. Set OPENAI_API_KEY environment variable');
  }
}

if (require.main === module) {
  main();
}

export { DSILRAG };
