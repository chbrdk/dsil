#!/usr/bin/env python3
"""
DSIL RAG Implementation Example
================================

This example demonstrates how to implement RAG (Retrieval-Augmented Generation)
for DSIL manifests, allowing efficient use of large design systems with LLMs.

Requirements:
- openai (for embeddings)
- chromadb (or other vector database)
- python-dotenv (for environment variables)

Installation:
    pip install openai chromadb python-dotenv

Usage:
    python rag-implementation-example.py
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Optional
from dotenv import load_dotenv

try:
    from openai import OpenAI
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("Please install required packages:")
    print("  pip install openai chromadb python-dotenv")
    exit(1)

# Load environment variables
load_dotenv()

# ============================================================================
# CONFIGURATION
# ============================================================================

CORE_DSIL_PATH = "dsil/core.dsil"
COMPONENTS_DIR = "dsil/components"
EMBEDDING_MODEL = "text-embedding-3-small"
VECTOR_DB_PATH = "./chroma_db"

# ============================================================================
# DSIL RAG CLASS
# ============================================================================

class DSILRAG:
    """
    Retrieval-Augmented Generation implementation for DSIL manifests.
    
    Splits DSIL into:
    - Core: Always included (meta, tokens, semantics, patterns, core components)
    - Extended: Retrieved on demand (other components, rare patterns)
    """
    
    def __init__(self, core_dsil_path: str, components_dir: str):
        """Initialize DSIL RAG system"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.core_dsil = self._load_core_dsil(core_dsil_path)
        self.components_dir = Path(components_dir)
        
        # Initialize vector database
        self.chroma_client = chromadb.PersistentClient(
            path=VECTOR_DB_PATH,
            settings=Settings(anonymized_telemetry=False)
        )
        self.collection = self._get_or_create_collection()
        
        # Index components if not already indexed
        if self.collection.count() == 0:
            print("Indexing components...")
            self._index_components(components_dir)
            print(f"Indexed {self.collection.count()} components")
    
    def _load_core_dsil(self, path: str) -> Dict:
        """Load core DSIL file"""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Core DSIL not found: {path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'content': content,
            'compact': self._to_compact(content),
            'meta': self._parse_meta(content),
            'tokens': self._estimate_tokens(content)
        }
    
    def _get_or_create_collection(self):
        """Get or create ChromaDB collection"""
        try:
            return self.chroma_client.get_collection("dsil_components")
        except:
            return self.chroma_client.create_collection(
                name="dsil_components",
                metadata={"description": "DSIL component definitions"}
            )
    
    def _index_components(self, components_dir: str):
        """Index all component files"""
        components_path = Path(components_dir)
        
        if not components_path.exists():
            print(f"Components directory not found: {components_dir}")
            return
        
        component_files = list(components_path.glob("*.dsil"))
        
        if not component_files:
            print(f"No component files found in {components_dir}")
            return
        
        ids = []
        embeddings = []
        documents = []
        metadatas = []
        
        for file_path in component_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            component_name = self._extract_component_name(content)
            if not component_name:
                continue
            
            # Create embedding
            embedding = self._create_embedding(content)
            
            # Extract metadata
            metadata = self._extract_metadata(content, component_name)
            
            ids.append(component_name)
            embeddings.append(embedding)
            documents.append(content)
            metadatas.append(metadata)
        
        # Batch add to vector DB
        if ids:
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )
    
    def retrieve(self, user_query: str, top_k: int = 5) -> Dict:
        """
        Retrieve relevant DSIL components for user query.
        
        Returns:
            Dict with 'components' (list of component names) and 
            'content' (retrieved DSIL content)
        """
        # 1. Extract mentioned components from query
        mentioned = self._extract_components(user_query)
        
        # 2. Semantic search
        query_embedding = self._create_embedding(user_query)
        semantic_results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=['documents', 'metadatas']
        )
        
        # 3. Combine mentioned + semantic matches
        component_names = set(mentioned)
        if semantic_results['ids'] and len(semantic_results['ids'][0]) > 0:
            for component_id in semantic_results['ids'][0]:
                component_names.add(component_id)
        
        # 4. Retrieve full component definitions
        retrieved_content = []
        if component_names:
            retrieved = self.collection.get(
                ids=list(component_names),
                include=['documents', 'metadatas']
            )
            if retrieved['documents']:
                retrieved_content = retrieved['documents']
        
        return {
            'components': list(component_names),
            'content': '\n\n'.join(retrieved_content) if retrieved_content else '',
            'mentioned': mentioned,
            'semantic_matches': semantic_results['ids'][0] if semantic_results['ids'] else []
        }
    
    def build_system_prompt(self, user_query: str) -> str:
        """
        Build complete system prompt with core + retrieved components.
        
        Returns:
            Complete system prompt string
        """
        # Retrieve relevant components
        retrieved = self.retrieve(user_query)
        
        # Build prompt
        system_name = self.core_dsil['meta'].get('name', 'design-system')
        
        prompt = f"""You are a frontend developer using the {system_name} design system.

═══════════════════════════════════════════════════════════════
CORE SYSTEM (Always Available)
═══════════════════════════════════════════════════════════════
{self.core_dsil['compact']}

"""
        
        if retrieved['content']:
            prompt += f"""═══════════════════════════════════════════════════════════════
RETRIEVED COMPONENTS (For This Request)
═══════════════════════════════════════════════════════════════
{self._to_compact(retrieved['content'])}

"""
        
        prompt += """═══════════════════════════════════════════════════════════════
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
"""
        
        return prompt
    
    def _extract_components(self, query: str) -> List[str]:
        """Extract component names from user query using keyword matching"""
        keyword_map = {
            # Explicit component mentions
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
            'bottom-sheet': 'bottom-sheet',
            'text area': 'textarea',
            'textarea': 'textarea',
        }
        
        found = []
        query_lower = query.lower()
        
        for keyword, component in keyword_map.items():
            if keyword in query_lower:
                found.append(component)
        
        return list(set(found))  # Remove duplicates
    
    def _create_embedding(self, text: str) -> List[float]:
        """Create embedding for text using OpenAI"""
        try:
            response = self.client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error creating embedding: {e}")
            # Return zero vector as fallback
            return [0.0] * 1536  # text-embedding-3-small dimension
    
    def _extract_component_name(self, content: str) -> Optional[str]:
        """Extract component name from @component definition"""
        match = re.search(r'@component\s+([\w-]+)', content)
        return match.group(1) if match else None
    
    def _extract_metadata(self, content: str, component_name: str) -> Dict:
        """Extract metadata from component definition"""
        # Extract @doc
        doc_match = re.search(r'@doc\s+"([^"]+)"', content)
        doc = doc_match.group(1) if doc_match else ""
        
        # Extract props
        props_match = re.search(r'props:\s*\{([^}]+)\}', content, re.DOTALL)
        props = []
        if props_match:
            prop_names = re.findall(r'(\w+):\s*\{', props_match.group(1))
            props = prop_names
        
        # Determine category (simple heuristic)
        category = "other"
        if any(word in component_name for word in ['button', 'link', 'chip']):
            category = "action"
        elif any(word in component_name for word in ['input', 'select', 'textarea', 'checkbox', 'radio']):
            category = "input"
        elif any(word in component_name for word in ['card', 'container', 'box']):
            category = "layout"
        elif any(word in component_name for word in ['dialog', 'modal', 'snackbar', 'toast']):
            category = "feedback"
        
        # Extract keywords
        keywords = [component_name]
        if doc:
            # Extract important words from doc
            keywords.extend([w for w in doc.lower().split() if len(w) > 4])
        
        return {
            'component': component_name,
            'type': 'component',
            'category': category,
            'doc': doc[:100] if doc else "",  # Truncate for metadata
            'props': ','.join(props[:5]),  # First 5 props
            'keywords': ','.join(keywords[:10]),  # First 10 keywords
            'tokens': self._estimate_tokens(content)
        }
    
    def _parse_meta(self, content: str) -> Dict:
        """Parse @meta section to extract system name"""
        name_match = re.search(r'name:\s*"([^"]+)"', content)
        version_match = re.search(r'version:\s*"([^"]+)"', content)
        
        return {
            'name': name_match.group(1) if name_match else 'unknown',
            'version': version_match.group(1) if version_match else '1.0.0'
        }
    
    def _to_compact(self, content: str) -> str:
        """
        Convert DSIL to compact format.
        
        Note: This is a simplified version. In production, use a proper
        DSIL converter that handles all syntax correctly.
        """
        # For now, return content as-is
        # In production, implement full compact conversion
        return content
    
    def _estimate_tokens(self, text: str) -> int:
        """Estimate token count (rough approximation)"""
        # Rough estimate: 1 token ≈ 4 characters
        return len(text) // 4


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

def main():
    """Example usage of DSIL RAG"""
    
    print("DSIL RAG Implementation Example")
    print("=" * 60)
    print()
    
    # Check if core DSIL exists
    if not os.path.exists(CORE_DSIL_PATH):
        print(f"Error: Core DSIL not found at {CORE_DSIL_PATH}")
        print("\nTo use this example:")
        print("1. Create a core.dsil file with @meta, @tokens, @semantics, @patterns")
        print("2. Create a components/ directory with individual component .dsil files")
        print("3. Set OPENAI_API_KEY environment variable")
        return
    
    # Initialize RAG system
    try:
        rag = DSILRAG(CORE_DSIL_PATH, COMPONENTS_DIR)
        print(f"✓ Loaded core DSIL: {rag.core_dsil['meta']['name']}")
        print(f"✓ Indexed components: {rag.collection.count()}")
        print()
    except Exception as e:
        print(f"Error initializing RAG: {e}")
        return
    
    # Example queries
    example_queries = [
        "Create a login form with email and password fields",
        "Build a card with image and action buttons",
        "Show me how to create a modal dialog",
        "Create a form with validation and error messages"
    ]
    
    print("Example Queries:")
    print("-" * 60)
    
    for i, query in enumerate(example_queries, 1):
        print(f"\n{i}. Query: {query}")
        retrieved = rag.retrieve(query)
        
        print(f"   Mentioned components: {retrieved['mentioned']}")
        print(f"   Semantic matches: {retrieved['semantic_matches']}")
        print(f"   Total retrieved: {len(retrieved['components'])} components")
        
        if retrieved['content']:
            tokens = rag._estimate_tokens(retrieved['content'])
            print(f"   Retrieved content: ~{tokens} tokens")
    
    print("\n" + "=" * 60)
    print("\nTo build a complete system prompt:")
    print()
    print("  prompt = rag.build_system_prompt(user_query)")
    print("  # Use 'prompt' as system message with LLM API")
    print()


if __name__ == "__main__":
    main()
