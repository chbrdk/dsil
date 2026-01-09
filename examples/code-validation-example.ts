/**
 * DSIL Code Validation Example (TypeScript)
 * ==========================================
 * 
 * This example demonstrates how to validate and transform LLM-generated code
 * to ensure it conforms to DSIL specifications.
 * 
 * Features:
 * - AST-based parsing (using TypeScript compiler API)
 * - Component validation
 * - Prop and variant validation
 * - Constraint checking
 * - Automatic code fixes
 * - Framework conversion utilities
 * 
 * Requirements:
 * - typescript
 * - @babel/parser
 * - @babel/traverse
 * - @babel/types
 * 
 * Installation:
 *   npm install typescript @babel/parser @babel/traverse @babel/types
 * 
 * Usage:
 *   import { DSILCodeValidator } from './code-validation-example';
 *   
 *   const validator = new DSILCodeValidator(dsilManifest);
 *   const result = validator.validateAndTransform(code, 'react');
 */

import * as ts from 'typescript';
import { parse } from '@babel/parser';
import traverse from '@babel/traverse';
import * as t from '@babel/types';

// ============================================================================
// TYPES
// ============================================================================

interface DSILComponent {
  name: string;
  props: Record<string, PropDefinition>;
  variants: Record<string, string[]>;
  constraints: string[];
  required?: string[];
  controlled?: boolean;
}

interface PropDefinition {
  type: string;
  required?: boolean;
  default?: any;
  values?: string[];
}

interface ComponentUsage {
  name: string;
  props: Record<string, any>;
  variants: Record<string, string>;
  line: number;
  column: number;
  node: any;
}

interface ValidationError {
  type: string;
  message: string;
  component?: string;
  prop?: string;
  variant?: string;
  value?: any;
  allowed?: string[];
  constraint?: string;
  line: number;
  column: number;
  fix?: string;
}

interface ValidationWarning {
  type: string;
  message: string;
  component?: string;
  line: number;
}

interface ValidationResult {
  valid: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
  transformedCode?: string;
  fixesApplied?: number;
}

interface ConstraintAST {
  type: 'IMPLICATION' | 'EXCLUSION' | 'COMPARISON' | 'REQUIREMENT';
  original: string;
  condition?: any;
  result?: any;
  conditions?: any[];
  property?: string;
  operator?: string;
  value?: number;
}

// ============================================================================
// DSIL CODE VALIDATOR
// ============================================================================

export class DSILCodeValidator {
  private dsilComponents: Map<string, DSILComponent>;
  private constraintParser: ConstraintParser;
  private constraintValidator: ConstraintValidator;
  private codeTransformer: CodeTransformer;

  constructor(dsilManifest: any) {
    this.dsilComponents = this.parseDSIL(dsilManifest);
    this.constraintParser = new ConstraintParser();
    this.constraintValidator = new ConstraintValidator();
    this.codeTransformer = new CodeTransformer();
  }

  /**
   * Parse DSIL manifest into component map
   */
  private parseDSIL(manifest: any): Map<string, DSILComponent> {
    const components = new Map<string, DSILComponent>();

    if (manifest.components) {
      for (const component of manifest.components) {
        const name = component.name || component['tag-react'] || component['tag-html'];
        if (name) {
          components.set(name, {
            name,
            props: this.parseProps(component.props || {}),
            variants: this.parseVariants(component.variants || {}),
            constraints: component.constraints || [],
            required: component.required || [],
            controlled: component.controlled || false
          });
        }
      }
    }

    return components;
  }

  private parseProps(props: any): Record<string, PropDefinition> {
    const result: Record<string, PropDefinition> = {};

    for (const [key, value] of Object.entries(props)) {
      if (typeof value === 'object' && value !== null) {
        result[key] = {
          type: (value as any).type || 'string',
          required: (value as any).required || false,
          default: (value as any).default,
          values: (value as any).values
        };
      } else {
        result[key] = { type: 'string' };
      }
    }

    return result;
  }

  private parseVariants(variants: any): Record<string, string[]> {
    const result: Record<string, string[]> = {};

    for (const [key, value] of Object.entries(variants)) {
      if (Array.isArray(value)) {
        result[key] = value;
      } else if (typeof value === 'object' && value !== null) {
        result[key] = Object.keys(value);
      }
    }

    return result;
  }

  /**
   * Validate and transform code
   */
  validateAndTransform(code: string, framework: 'react' | 'vue' | 'angular'): ValidationResult {
    const errors: ValidationError[] = [];
    const warnings: ValidationWarning[] = [];

    // 1. Parse code to AST
    const ast = this.parseCode(code, framework);
    if (!ast) {
      return {
        valid: false,
        errors: [{
          type: 'PARSE_ERROR',
          message: 'Failed to parse code',
          line: 0,
          column: 0
        }],
        warnings: []
      };
    }

    // 2. Extract component usages
    const componentUsages = this.extractComponents(ast, framework);

    // 3. Validate each usage
    for (const usage of componentUsages) {
      const validation = this.validateComponentUsage(usage);
      errors.push(...validation.errors);
      warnings.push(...validation.warnings);
    }

    // 4. Transform code if errors found
    let transformedCode = code;
    let fixesApplied = 0;
    if (errors.length > 0) {
      const transformResult = this.codeTransformer.transform(code, errors, framework);
      transformedCode = transformResult.code;
      fixesApplied = transformResult.fixesApplied;
    }

    return {
      valid: errors.length === 0,
      errors,
      warnings,
      transformedCode: errors.length > 0 ? transformedCode : undefined,
      fixesApplied
    };
  }

  /**
   * Parse code to AST
   */
  private parseCode(code: string, framework: string): any {
    try {
      if (framework === 'react') {
        return parse(code, {
          sourceType: 'module',
          plugins: ['jsx', 'typescript']
        });
      }
      // Add other framework parsers as needed
      return null;
    } catch (error) {
      console.error('Parse error:', error);
      return null;
    }
  }

  /**
   * Extract component usages from AST
   */
  private extractComponents(ast: any, framework: string): ComponentUsage[] {
    const usages: ComponentUsage[] = [];

    if (framework === 'react') {
      traverse(ast, {
        JSXOpeningElement(path: any) {
          const name = path.node.name;
          let componentName: string;

          if (t.isJSXIdentifier(name)) {
            componentName = name.name;
          } else if (t.isJSXMemberExpression(name)) {
            componentName = `${name.object.name}.${name.property.name}`;
          } else {
            return;
          }

          const props: Record<string, any> = {};
          const variants: Record<string, string> = {};

          for (const attr of path.node.attributes) {
            if (t.isJSXAttribute(attr)) {
              const propName = attr.name.name as string;
              let propValue: any;

              if (attr.value) {
                if (t.isStringLiteral(attr.value)) {
                  propValue = attr.value.value;
                } else if (t.isJSXExpressionContainer(attr.value)) {
                  if (t.isBooleanLiteral(attr.value.expression)) {
                    propValue = attr.value.expression.value;
                  } else if (t.isStringLiteral(attr.value.expression)) {
                    propValue = attr.value.expression.value;
                  } else if (t.isNumericLiteral(attr.value.expression)) {
                    propValue = attr.value.expression.value;
                  } else {
                    propValue = true; // Expression like {handler}
                  }
                } else {
                  propValue = true;
                }
              } else {
                propValue = true;
              }

              props[propName] = propValue;

              // Check if it's a variant
              if (propName === 'variant' || propName === 'size' || propName === 'intent') {
                variants[propName] = String(propValue);
              }
            }
          }

          usages.push({
            name: componentName,
            props,
            variants,
            line: path.node.loc?.start.line || 0,
            column: path.node.loc?.start.column || 0,
            node: path.node
          });
        }
      });
    }

    return usages;
  }

  /**
   * Validate a single component usage
   */
  private validateComponentUsage(usage: ComponentUsage): {
    errors: ValidationError[];
    warnings: ValidationWarning[];
  } {
    const errors: ValidationError[] = [];
    const warnings: ValidationWarning[] = [];
    const component = this.dsilComponents.get(usage.name);

    if (!component) {
      errors.push({
        type: 'UNKNOWN_COMPONENT',
        message: `Component "${usage.name}" not found in DSIL`,
        component: usage.name,
        line: usage.line,
        column: usage.column,
        fix: `Replace with a valid component or remove`
      });
      return { errors, warnings };
    }

    // Validate props
    for (const [propName, propValue] of Object.entries(usage.props)) {
      if (!component.props[propName]) {
        errors.push({
          type: 'UNKNOWN_PROP',
          message: `Prop "${propName}" does not exist on ${usage.name}`,
          component: usage.name,
          prop: propName,
          line: usage.line,
          column: usage.column,
          fix: `Remove prop "${propName}"`
        });
      } else {
        const propDef = component.props[propName];
        if (!this.validatePropValue(propValue, propDef)) {
          errors.push({
            type: 'INVALID_PROP_VALUE',
            message: `Invalid value for prop "${propName}"`,
            component: usage.name,
            prop: propName,
            value: propValue,
            allowed: propDef.values,
            line: usage.line,
            column: usage.column,
            fix: propDef.values ? `Use one of: ${propDef.values.join(', ')}` : 'Use valid value'
          });
        }
      }
    }

    // Validate variants
    for (const [variantName, variantValue] of Object.entries(usage.variants)) {
      if (!component.variants[variantName]) {
        errors.push({
          type: 'UNKNOWN_VARIANT',
          message: `Variant "${variantName}" does not exist`,
          component: usage.name,
          variant: variantName,
          line: usage.line,
          column: usage.column,
          fix: `Remove variant "${variantName}"`
        });
      } else if (!component.variants[variantName].includes(variantValue)) {
        errors.push({
          type: 'INVALID_VARIANT_VALUE',
          message: `Invalid variant value "${variantValue}" for "${variantName}"`,
          component: usage.name,
          variant: variantName,
          value: variantValue,
          allowed: component.variants[variantName],
          line: usage.line,
          column: usage.column,
          fix: `Use one of: ${component.variants[variantName].join(', ')}`
        });
      }
    }

    // Validate constraints
    for (const constraint of component.constraints) {
      const constraintAST = this.constraintParser.parse(constraint);
      const constraintError = this.constraintValidator.validateConstraint(usage, constraintAST, component);
      if (constraintError) {
        errors.push(constraintError);
      }
    }

    // Check required props
    for (const [propName, propDef] of Object.entries(component.props)) {
      if (propDef.required && !usage.props[propName]) {
        errors.push({
          type: 'MISSING_REQUIRED_PROP',
          message: `Required prop "${propName}" is missing`,
          component: usage.name,
          prop: propName,
          line: usage.line,
          column: usage.column,
          fix: `Add prop "${propName}"${propDef.default ? `="${propDef.default}"` : ''}`
        });
      }
    }

    return { errors, warnings };
  }

  private validatePropValue(value: any, propDef: PropDefinition): boolean {
    if (propDef.values && !propDef.values.includes(String(value))) {
      return false;
    }
    // Add more type checking as needed
    return true;
  }
}

// ============================================================================
// CONSTRAINT PARSER
// ============================================================================

class ConstraintParser {
  parse(constraint: string): ConstraintAST {
    const original = constraint.trim();

    // Parse: "loading → disabled"
    if (constraint.includes('→')) {
      const [condition, result] = constraint.split('→').map(s => s.trim());
      return {
        type: 'IMPLICATION',
        original,
        condition: this.parseCondition(condition),
        result: this.parseCondition(result)
      };
    }

    // Parse: "ghost + danger → invalid"
    if (constraint.includes('+') && constraint.includes('invalid')) {
      const parts = constraint.split('+').map(s => s.trim().replace('→ invalid', '').trim());
      return {
        type: 'EXCLUSION',
        original,
        conditions: parts.map(p => this.parseCondition(p))
      };
    }

    // Parse: "count ≤ 3"
    const comparisonMatch = constraint.match(/(\w+)\s*(≤|≥|=)\s*(\d+)/);
    if (comparisonMatch) {
      return {
        type: 'COMPARISON',
        original,
        property: comparisonMatch[1],
        operator: comparisonMatch[2],
        value: parseInt(comparisonMatch[3])
      };
    }

    throw new Error(`Unknown constraint format: ${constraint}`);
  }

  private parseCondition(condition: string): any {
    condition = condition.trim();

    // "!disabled" → { type: 'prop', name: 'disabled', value: false }
    if (condition.startsWith('!')) {
      return {
        type: 'prop',
        name: condition.substring(1),
        value: false
      };
    }

    // "variant:primary" → { type: 'variant', name: 'variant', value: 'primary' }
    if (condition.includes(':')) {
      const [name, value] = condition.split(':').map(s => s.trim());
      return {
        type: 'variant',
        name,
        value
      };
    }

    // "loading" → { type: 'prop', name: 'loading', value: true }
    return {
      type: 'prop',
      name: condition,
      value: true
    };
  }
}

// ============================================================================
// CONSTRAINT VALIDATOR
// ============================================================================

class ConstraintValidator {
  validateConstraint(
    usage: ComponentUsage,
    constraint: ConstraintAST,
    component: DSILComponent
  ): ValidationError | null {
    switch (constraint.type) {
      case 'IMPLICATION':
        if (this.evaluateCondition(usage, constraint.condition)) {
          if (!this.evaluateCondition(usage, constraint.result)) {
            return {
              type: 'CONSTRAINT_VIOLATION',
              message: `Constraint violated: ${constraint.original}`,
              component: usage.name,
              constraint: constraint.original,
              line: usage.line,
              column: usage.column,
              fix: this.generateImplicationFix(constraint)
            };
          }
        }
        break;

      case 'EXCLUSION':
        const allTrue = constraint.conditions!.every(
          cond => this.evaluateCondition(usage, cond)
        );
        if (allTrue) {
          return {
            type: 'CONSTRAINT_VIOLATION',
            message: `Invalid combination: ${constraint.original}`,
            component: usage.name,
            constraint: constraint.original,
            line: usage.line,
            column: usage.column,
            fix: 'Remove one of the conflicting props/variants'
          };
        }
        break;

      case 'COMPARISON':
        // Implementation for comparison constraints
        break;
    }

    return null;
  }

  private evaluateCondition(usage: ComponentUsage, condition: any): boolean {
    if (condition.type === 'prop') {
      const propValue = usage.props[condition.name];
      if (condition.value === true) {
        return propValue === true;
      } else {
        return propValue !== true;
      }
    } else if (condition.type === 'variant') {
      return usage.variants[condition.name] === condition.value;
    }
    return false;
  }

  private generateImplicationFix(constraint: ConstraintAST): string {
    if (constraint.result && constraint.result.type === 'prop') {
      return `Set ${constraint.result.name}={true}`;
    }
    return `Apply constraint: ${constraint.original}`;
  }
}

// ============================================================================
// CODE TRANSFORMER
// ============================================================================

class CodeTransformer {
  transform(
    code: string,
    errors: ValidationError[],
    framework: string
  ): { code: string; fixesApplied: number } {
    let transformed = code;
    let fixesApplied = 0;

    for (const error of errors) {
      switch (error.type) {
        case 'UNKNOWN_PROP':
          transformed = this.removeProp(transformed, error.component!, error.prop!);
          fixesApplied++;
          break;

        case 'INVALID_VARIANT_VALUE':
          if (error.allowed && error.allowed.length > 0) {
            transformed = this.fixVariant(
              transformed,
              error.component!,
              error.variant!,
              error.value,
              error.allowed[0]
            );
            fixesApplied++;
          }
          break;

        case 'CONSTRAINT_VIOLATION':
          transformed = this.applyConstraintFix(transformed, error);
          fixesApplied++;
          break;

        case 'MISSING_REQUIRED_PROP':
          transformed = this.addProp(transformed, error.component!, error.prop!);
          fixesApplied++;
          break;
      }
    }

    return { code: transformed, fixesApplied };
  }

  private removeProp(code: string, component: string, prop: string): string {
    const regex = new RegExp(`(<${component}[^>]*)\\s+${prop}="[^"]*"`, 'g');
    return code.replace(regex, '$1');
  }

  private fixVariant(
    code: string,
    component: string,
    variant: string,
    oldValue: any,
    newValue: string
  ): string {
    const regex = new RegExp(
      `(<${component}[^>]*${variant}=\\{)"${oldValue}"`,
      'g'
    );
    return code.replace(regex, `$1"${newValue}"`);
  }

  private applyConstraintFix(code: string, error: ValidationError): string {
    if (error.constraint?.includes('→')) {
      const [condition, result] = error.constraint.split('→').map(s => s.trim());
      const component = error.component!;

      // If condition is true, ensure result is true
      const conditionRegex = new RegExp(
        `(<${component}[^>]*${condition}=\\{true\\}[^>]*)>`,
        'g'
      );

      code = code.replace(conditionRegex, (match) => {
        if (!match.includes(`${result}={true}`) && !match.includes(`${result}={false}`)) {
          return match.replace('>', ` ${result}={true}>`);
        }
        return match;
      });
    }

    return code;
  }

  private addProp(code: string, component: string, prop: string): string {
    const regex = new RegExp(`(<${component}[^>]*)>`, 'g');
    return code.replace(regex, `$1 ${prop}>`);
  }
}

// ============================================================================
// USAGE EXAMPLE
// ============================================================================

export function example() {
  const dsilManifest = {
    components: [
      {
        name: 'Button',
        props: {
          variant: { type: 'string', values: ['primary', 'secondary', 'ghost'] },
          disabled: { type: 'boolean', default: false },
          loading: { type: 'boolean', default: false }
        },
        variants: {
          variant: ['primary', 'secondary', 'ghost']
        },
        constraints: ['loading → disabled']
      }
    ]
  };

  const validator = new DSILCodeValidator(dsilManifest);

  const code = `
    <Button loading={true} disabled={false}>
      Save
    </Button>
  `;

  const result = validator.validateAndTransform(code, 'react');

  console.log('Valid:', result.valid);
  console.log('Errors:', result.errors);
  console.log('Fixed Code:', result.transformedCode);
}
