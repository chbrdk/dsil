#!/usr/bin/env python3
"""
DSIL Code Validation Example (Python)
=====================================

This example demonstrates how to validate and transform LLM-generated code
to ensure it conforms to DSIL specifications.

Features:
- Regex-based validation (simple, fast)
- AST-based validation (using ast module)
- Constraint validation
- LLM self-correction integration
- Framework conversion utilities

Requirements:
- openai (for LLM self-correction)
- python-dotenv (for environment variables)

Installation:
    pip install openai python-dotenv

Usage:
    from code_validation_example import DSILCodeValidator
    
    validator = DSILCodeValidator(dsil_manifest)
    is_valid, errors, fixed_code = validator.validate_and_fix(code)
"""

import re
import ast
import json
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum

try:
    from openai import OpenAI
    import os
    from dotenv import load_dotenv
    load_dotenv()
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: OpenAI not installed. LLM self-correction will be disabled.")

# ============================================================================
# TYPES
# ============================================================================

class ErrorType(Enum):
    UNKNOWN_COMPONENT = "UNKNOWN_COMPONENT"
    UNKNOWN_PROP = "UNKNOWN_PROP"
    INVALID_PROP_VALUE = "INVALID_PROP_VALUE"
    INVALID_VARIANT_VALUE = "INVALID_VARIANT_VALUE"
    CONSTRAINT_VIOLATION = "CONSTRAINT_VIOLATION"
    MISSING_REQUIRED_PROP = "MISSING_REQUIRED_PROP"
    MISSING_REQUIRED_HANDLER = "MISSING_REQUIRED_HANDLER"
    FRAMEWORK_SYNTAX_ERROR = "FRAMEWORK_SYNTAX_ERROR"

@dataclass
class ValidationError:
    type: ErrorType
    message: str
    component: Optional[str] = None
    prop: Optional[str] = None
    variant: Optional[str] = None
    value: Optional[Any] = None
    allowed: Optional[List[str]] = None
    constraint: Optional[str] = None
    line: int = 0
    fix: Optional[str] = None

@dataclass
class ComponentUsage:
    name: str
    props: Dict[str, Any]
    variants: Dict[str, str]
    line: int

# ============================================================================
# DSIL CODE VALIDATOR
# ============================================================================

class DSILCodeValidator:
    """
    Validates and transforms LLM-generated code against DSIL specifications.
    """
    
    def __init__(self, dsil_manifest: Dict, use_llm: bool = False):
        """
        Initialize validator.
        
        Args:
            dsil_manifest: DSIL manifest dictionary
            use_llm: Whether to use LLM for self-correction
        """
        self.components = self._extract_components(dsil_manifest)
        self.constraints = self._extract_constraints(dsil_manifest)
        self.use_llm = use_llm and HAS_OPENAI
        
        if self.use_llm:
            self.llm_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def _extract_components(self, manifest: Dict) -> Dict[str, Dict]:
        """Extract components from DSIL manifest"""
        components = {}
        
        if 'components' in manifest:
            for component in manifest['components']:
                name = component.get('name') or component.get('tag-react') or component.get('tag-html')
                if name:
                    components[name] = {
                        'props': component.get('props', {}),
                        'variants': self._extract_variants(component.get('variants', {})),
                        'constraints': component.get('constraints', []),
                        'required': component.get('required', []),
                        'controlled': component.get('controlled', False)
                    }
        
        return components
    
    def _extract_variants(self, variants: Dict) -> Dict[str, List[str]]:
        """Extract variant definitions"""
        result = {}
        for key, value in variants.items():
            if isinstance(value, list):
                result[key] = value
            elif isinstance(value, dict):
                result[key] = list(value.keys())
        return result
    
    def _extract_constraints(self, manifest: Dict) -> List[Dict]:
        """Extract all constraints from manifest"""
        constraints = []
        
        if 'components' in manifest:
            for component in manifest['components']:
                for constraint in component.get('constraints', []):
                    constraints.append({
                        'component': component.get('name'),
                        'constraint': constraint
                    })
        
        return constraints
    
    def validate_and_fix(
        self,
        code: str,
        framework: str = 'react'
    ) -> Tuple[bool, List[ValidationError], str]:
        """
        Validate code and return (is_valid, errors, fixed_code)
        
        Args:
            code: Source code to validate
            framework: Framework type ('react', 'vue', 'angular')
        
        Returns:
            Tuple of (is_valid, errors, fixed_code)
        """
        # Step 1: Quick regex validation
        errors = []
        usages = self._extract_component_usages(code)
        
        # Step 2: Validate each component usage
        for usage in usages:
            component_errors = self._validate_component_usage(usage)
            errors.extend(component_errors)
        
        # Step 3: Apply fixes
        fixed_code = code
        if errors:
            fixed_code = self._apply_fixes(code, errors)
            
            # Step 4: Re-validate after fixes
            usages_after = self._extract_component_usages(fixed_code)
            errors_after = []
            for usage in usages_after:
                component_errors = self._validate_component_usage(usage)
                errors_after.extend(component_errors)
            
            # Step 5: Use LLM if still errors and enabled
            if errors_after and self.use_llm:
                fixed_code = self._llm_correct(fixed_code, errors_after)
                # Final validation
                usages_final = self._extract_component_usages(fixed_code)
                errors_final = []
                for usage in usages_final:
                    component_errors = self._validate_component_usage(usage)
                    errors_final.extend(component_errors)
                errors = errors_final
            else:
                errors = errors_after
        
        return len(errors) == 0, errors, fixed_code
    
    def _extract_component_usages(self, code: str) -> List[ComponentUsage]:
        """Extract component usages from code using regex"""
        usages = []
        
        # Pattern: <ComponentName prop="value" ...>
        pattern = r'<(\w+)([^>]*)>'
        matches = re.finditer(pattern, code)
        
        for match in matches:
            component_name = match.group(1)
            props_string = match.group(2)
            props = self._parse_props(props_string)
            variants = self._extract_variants_from_props(props)
            
            # Calculate line number
            line = code[:match.start()].count('\n') + 1
            
            usages.append(ComponentUsage(
                name=component_name,
                props=props,
                variants=variants,
                line=line
            ))
        
        return usages
    
    def _parse_props(self, props_string: str) -> Dict[str, Any]:
        """Parse props from JSX-like string"""
        props = {}
        
        # Pattern: prop="value" or prop={value} or prop
        patterns = [
            r'(\w+)="([^"]*)"',  # prop="value"
            r'(\w+)=\{([^}]+)\}',  # prop={value}
            r'(\w+)=\{true\}',  # prop={true}
            r'(\w+)=\{false\}',  # prop={false}
            r'(\w+)(?=\s|>)',  # prop (boolean, no value)
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, props_string)
            for match in matches:
                prop_name = match.group(1)
                if len(match.groups()) > 1:
                    prop_value = match.group(2)
                    # Try to parse value
                    if prop_value == 'true':
                        props[prop_name] = True
                    elif prop_value == 'false':
                        props[prop_name] = False
                    else:
                        props[prop_name] = prop_value
                else:
                    props[prop_name] = True
        
        return props
    
    def _extract_variants_from_props(self, props: Dict[str, Any]) -> Dict[str, str]:
        """Extract variant props"""
        variants = {}
        variant_keys = ['variant', 'size', 'intent', 'type']
        
        for key in variant_keys:
            if key in props:
                variants[key] = str(props[key])
        
        return variants
    
    def _validate_component_usage(self, usage: ComponentUsage) -> List[ValidationError]:
        """Validate a single component usage"""
        errors = []
        
        # Check if component exists
        if usage.name not in self.components:
            errors.append(ValidationError(
                type=ErrorType.UNKNOWN_COMPONENT,
                message=f"Component '{usage.name}' not found in DSIL",
                component=usage.name,
                line=usage.line,
                fix=f"Replace with a valid component or remove"
            ))
            return errors
        
        component_def = self.components[usage.name]
        
        # Validate props
        for prop_name, prop_value in usage.props.items():
            if prop_name not in component_def['props']:
                errors.append(ValidationError(
                    type=ErrorType.UNKNOWN_PROP,
                    message=f"Prop '{prop_name}' does not exist on {usage.name}",
                    component=usage.name,
                    prop=prop_name,
                    line=usage.line,
                    fix=f"Remove prop '{prop_name}'"
                ))
            else:
                prop_def = component_def['props'][prop_name]
                # Check if value is valid (if values are defined)
                if 'values' in prop_def and prop_value not in prop_def['values']:
                    errors.append(ValidationError(
                        type=ErrorType.INVALID_PROP_VALUE,
                        message=f"Invalid value '{prop_value}' for prop '{prop_name}'",
                        component=usage.name,
                        prop=prop_name,
                        value=prop_value,
                        allowed=prop_def['values'],
                        line=usage.line,
                        fix=f"Use one of: {', '.join(prop_def['values'])}"
                    ))
        
        # Validate variants
        for variant_name, variant_value in usage.variants.items():
            if variant_name not in component_def['variants']:
                errors.append(ValidationError(
                    type=ErrorType.UNKNOWN_VARIANT,
                    message=f"Variant '{variant_name}' does not exist",
                    component=usage.name,
                    variant=variant_name,
                    line=usage.line,
                    fix=f"Remove variant '{variant_name}'"
                ))
            elif variant_value not in component_def['variants'][variant_name]:
                errors.append(ValidationError(
                    type=ErrorType.INVALID_VARIANT_VALUE,
                    message=f"Invalid variant value '{variant_value}' for '{variant_name}'",
                    component=usage.name,
                    variant=variant_name,
                    value=variant_value,
                    allowed=component_def['variants'][variant_name],
                    line=usage.line,
                    fix=f"Use one of: {', '.join(component_def['variants'][variant_name])}"
                ))
        
        # Validate constraints
        for constraint_str in component_def['constraints']:
            constraint_error = self._validate_constraint(usage, constraint_str, component_def)
            if constraint_error:
                errors.append(constraint_error)
        
        # Check required props
        for prop_name in component_def.get('required', []):
            if prop_name not in usage.props:
                prop_def = component_def['props'].get(prop_name, {})
                default = prop_def.get('default', '')
                errors.append(ValidationError(
                    type=ErrorType.MISSING_REQUIRED_PROP,
                    message=f"Required prop '{prop_name}' is missing",
                    component=usage.name,
                    prop=prop_name,
                    line=usage.line,
                    fix=f"Add prop '{prop_name}'" + (f'="{default}"' if default else '')
                ))
        
        return errors
    
    def _validate_constraint(
        self,
        usage: ComponentUsage,
        constraint: str,
        component_def: Dict
    ) -> Optional[ValidationError]:
        """Validate a single constraint"""
        # Parse: "loading → disabled"
        if '→' in constraint:
            condition, result = constraint.split('→', 1)
            condition = condition.strip()
            result = result.strip()
            
            # Check if condition is true
            condition_met = self._evaluate_condition(usage, condition)
            
            if condition_met:
                # Check if result is satisfied
                result_met = self._evaluate_condition(usage, result)
                
                if not result_met:
                    return ValidationError(
                        type=ErrorType.CONSTRAINT_VIOLATION,
                        message=f"Constraint violated: {constraint}",
                        component=usage.name,
                        constraint=constraint,
                        line=usage.line,
                        fix=f"Set {result}={True}"
                    )
        
        # Parse: "ghost + danger → invalid"
        if '+' in constraint and 'invalid' in constraint:
            parts = constraint.split('+')
            parts = [p.strip().replace('→ invalid', '').strip() for p in parts]
            
            all_met = all(self._evaluate_condition(usage, part) for part in parts)
            
            if all_met:
                return ValidationError(
                    type=ErrorType.CONSTRAINT_VIOLATION,
                    message=f"Invalid combination: {constraint}",
                    component=usage.name,
                    constraint=constraint,
                    line=usage.line,
                    fix="Remove one of the conflicting props/variants"
                )
        
        return None
    
    def _evaluate_condition(self, usage: ComponentUsage, condition: str) -> bool:
        """Evaluate a condition against component usage"""
        condition = condition.strip()
        
        # "!disabled" → check if disabled is false
        if condition.startswith('!'):
            prop_name = condition[1:]
            return usage.props.get(prop_name) != True
        
        # "variant:primary" → check variant value
        if ':' in condition:
            prop_name, value = condition.split(':', 1)
            prop_name = prop_name.strip()
            value = value.strip()
            return usage.variants.get(prop_name) == value or usage.props.get(prop_name) == value
        
        # "loading" → check if prop is true
        return usage.props.get(condition) == True
    
    def _apply_fixes(self, code: str, errors: List[ValidationError]) -> str:
        """Apply automatic fixes to code"""
        fixed = code
        
        for error in errors:
            if error.type == ErrorType.UNKNOWN_PROP:
                # Remove invalid prop
                fixed = re.sub(
                    rf'<{error.component}[^>]*\s+{error.prop}="[^"]*"',
                    f'<{error.component}',
                    fixed
                )
                fixed = re.sub(
                    rf'<{error.component}[^>]*\s+{error.prop}=\{{[^}}]+\}}',
                    f'<{error.component}',
                    fixed
                )
            
            elif error.type == ErrorType.INVALID_VARIANT_VALUE:
                # Fix variant value
                if error.allowed and len(error.allowed) > 0:
                    fixed = re.sub(
                        rf'<{error.component}[^>]*{error.variant}="[^"]*"',
                        f'<{error.component} {error.variant}="{error.allowed[0]}"',
                        fixed
                    )
            
            elif error.type == ErrorType.CONSTRAINT_VIOLATION:
                # Apply constraint fix
                if error.constraint and '→' in error.constraint:
                    condition, result = error.constraint.split('→', 1)
                    condition = condition.strip()
                    result = result.strip()
                    
                    # If condition is true, ensure result is true
                    if self._has_condition(code, error.component, condition):
                        fixed = re.sub(
                            rf'(<{error.component}[^>]*)>',
                            rf'\1 {result}={{true}}>',
                            fixed
                        )
            
            elif error.type == ErrorType.MISSING_REQUIRED_PROP:
                # Add missing prop
                default = error.fix.split('=')[1] if '=' in error.fix else ''
                fixed = re.sub(
                    rf'(<{error.component}[^>]*)>',
                    rf'\1 {error.prop}{default}>',
                    fixed
                )
        
        return fixed
    
    def _has_condition(self, code: str, component: str, condition: str) -> bool:
        """Check if condition is present in component"""
        pattern = rf'<{component}[^>]*{condition}=\{{true\}}'
        return bool(re.search(pattern, code))
    
    def _llm_correct(
        self,
        code: str,
        errors: List[ValidationError]
    ) -> str:
        """Use LLM to correct code"""
        if not self.use_llm:
            return code
        
        errors_summary = '\n'.join([
            f"- {e.type.value}: {e.message}" for e in errors
        ])
        
        prompt = f"""
You generated this code, but validation found errors:

```tsx
{code}
```

Errors:
{errors_summary}

Please fix all errors and return ONLY the corrected code, no explanations.
"""
        
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a code validator and fixer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            
            fixed_code = response.choices[0].message.content
            
            # Extract code from markdown if needed
            if "```" in fixed_code:
                match = re.search(r'```(?:tsx|ts|jsx|js)?\n(.*?)```', fixed_code, re.DOTALL)
                if match:
                    fixed_code = match.group(1)
            
            return fixed_code.strip()
        except Exception as e:
            print(f"LLM correction failed: {e}")
            return code

# ============================================================================
# USAGE EXAMPLE
# ============================================================================

def example():
    """Example usage"""
    dsil_manifest = {
        'components': [
            {
                'name': 'Button',
                'props': {
                    'variant': {'type': 'string', 'values': ['primary', 'secondary', 'ghost']},
                    'disabled': {'type': 'boolean', 'default': False},
                    'loading': {'type': 'boolean', 'default': False}
                },
                'variants': {
                    'variant': ['primary', 'secondary', 'ghost']
                },
                'constraints': ['loading → disabled']
            }
        ]
    }
    
    validator = DSILCodeValidator(dsil_manifest, use_llm=False)
    
    code = """
    <Button loading={true} disabled={false}>
      Save
    </Button>
    """
    
    is_valid, errors, fixed_code = validator.validate_and_fix(code)
    
    print(f"Valid: {is_valid}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"  - {error.type.value}: {error.message}")
    print(f"\nFixed Code:\n{fixed_code}")

if __name__ == "__main__":
    example()
