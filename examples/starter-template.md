# DSIL Starter Template

> Copy this file and adapt it to your design system.

---

## Instructions

1. **Adapt Meta**: Name and version of your system
2. **Define Tokens**: Only those that actually exist
3. **Add Components**: Start with 5-10 core components
4. **Add Patterns**: The most common combinations
5. **Write Semantics**: Intent mapping for better LLM decisions

**Tip**: Less is more! A focused DSIL with 10 well-defined components beats an overloaded one with 50.

---

## Template (Full Format)

```dsil
# ============================================================================
# [YOUR SYSTEM NAME] – DSIL Manifest
# ============================================================================

@meta {
  name: "[system-name]"
  version: "[x.y.z]"
  dsil-version: "1.0.0"
  description: "Description of your design system"
  
  prefix: {
    html: "[prefix]-"     # e.g., "my-"
    react: "[Prefix]"      # e.g., "My"
  }
  
  imports: {
    react: "@package/components-react"
    # Add other frameworks as needed
  }
  
  config: {
    strict: true          # Only defined values allowed
    controlled: true      # Mark controlled components
    theme: "light"        # Default theme
    allowCustom: false    # Disallow custom props
  }
}

# ----------------------------------------------------------------------------
# TOKENS
# Define only tokens that actually exist in your system!
# ----------------------------------------------------------------------------

@tokens {
  
  # Theme
  theme: {
    values: [light, dark, auto]
    default: "light"
  }
  
  # Spacing – adapt values to your system
  spacing: {
    @group static {
      xs: { value: "[value]", css: "$spacing-xs" }  # e.g., "4px"
      sm: { value: "[value]", css: "$spacing-sm" }  # e.g., "8px"
      md: { value: "[value]", css: "$spacing-md" }  # e.g., "16px"
      lg: { value: "[value]", css: "$spacing-lg" }  # e.g., "24px"
      xl: { value: "[value]", css: "$spacing-xl" }  # e.g., "32px"
      # ... more as needed
    }
  }
  
  # Colors – group by usage
  color: {
    @group brand {
      primary: { value: "[hex]", css: "$color-primary" }      # e.g., "#0066CC"
      secondary: { value: "[hex]", css: "$color-secondary" }  # e.g., "#000000"
      # ...
    }
    
    @group semantic {
      success: { value: "[hex]", css: "$color-success" }      # e.g., "#00AA00"
      warning: { value: "[hex]", css: "$color-warning" }      # e.g., "#FF9B00"
      error: { value: "[hex]", css: "$color-error" }          # e.g., "#FF0000"
      info: { value: "[hex]", css: "$color-info" }            # e.g., "#0061BD"
    }
    
    @group neutral {
      # Your grayscale values
      # 50, 100, 200, ..., 900
    }
  }
  
  # Typography
  typography: {
    family: {
      sans: { value: "[font-stack]" }  # e.g., "'Inter', Arial, sans-serif"
      # mono: { value: "[font-stack]" }  # if available
    }
    
    scale: {
      # Your size scale
      # xs, sm, base, lg, xl, 2xl, etc.
    }
    
    weight: {
      # Used weights
      # normal, medium, semibold, bold, etc.
    }
  }
  
  # Breakpoints
  breakpoint: {
    base: { value: "0px" }
    s: { value: "[value]" }    # e.g., "768px"
    m: { value: "[value]" }    # e.g., "1024px"
    l: { value: "[value]" }    # e.g., "1280px"
  }
  
  # Additional token categories as needed:
  # border: { radius: { ... }, width: { ... } }
  # shadow: { ... }
  # motion: { duration: { ... }, easing: { ... } }
}

# ----------------------------------------------------------------------------
# ICONS
# Define available icon names, grouped by usage
# ----------------------------------------------------------------------------

@icons {
  @group navigation {
    # arrow-left, arrow-right, chevron-down, menu, close, etc.
  }
  
  @group action {
    # add, edit, delete, save, search, filter, etc.
  }
  
  @group status {
    # success, error, warning, info, spinner, etc.
  }
  
  special: {
    none: { @doc "No icon" }
  }
}

# ----------------------------------------------------------------------------
# TYPES (Optional but recommended)
# Reusable type definitions
# ----------------------------------------------------------------------------

@types {
  @type Theme {
    values: [light, dark, auto]
    default: light
  }
  
  @type Size {
    values: [small, medium, large]
    default: medium
  }
  
  @type IconName {
    @doc "All available icon names"
    definition: "@ref(icons.*)"
    special: none
  }
}

# ----------------------------------------------------------------------------
# COMPONENTS
# Add your components – start with the most important ones!
# ----------------------------------------------------------------------------

@component button {
  @doc "Interactive button for user actions"
  @controlled false
  @tag-react Button
  
  variants: {
    # Define your variants
    variant: {
      primary: { @doc "Main action" }
      secondary: { @doc "Secondary action" }
      # Add more variants
    }
    size: {
      small: { @doc "Compact" }
      medium: { @doc "Standard", default: true }
      large: { @doc "Prominent" }
    }
  }
  
  props: {
    variant: {
      type: "primary" | "secondary"
      default: "primary"
    }
    size: {
      type: "small" | "medium" | "large"
      default: "medium"
    }
    disabled: {
      type: boolean
      default: false
    }
    loading: {
      type: boolean
      default: false
      @doc "Shows loading spinner"
    }
  }
  
  slots: {
    default: {
      required: true
      type: text
      @doc "Button label"
    }
  }
  
  events: {
    click: { native: true }
  }
  
  constraints: {
    # Rules the LLM should follow
    @rule "loading implies disabled" {
      error: "Button with loading=true is automatically disabled"
    }
  }
  
  usage: {
    do: ["Use primary for main actions", "Use action-oriented labels"]
    dont: ["Don't use multiple primary buttons per viewport"]
  }
  
  examples: {
    basic: |
      <Button>Save</Button>
      <Button variant="secondary">Cancel</Button>
      <Button loading>Saving...</Button>
  }
}

# Add more components following this pattern:
# @component input { ... }
# @component card { ... }
# @component modal { ... }
# ...

# ----------------------------------------------------------------------------
# PATTERNS
# Define frequent combinations
# ----------------------------------------------------------------------------

@patterns {
  @pattern form-field {
    @doc "Standard form field structure"
    
    structure: [label?, field!, helper?, error?]
    
    components: {
      label: "text component"
      field: "input | select | textarea"
      helper: "text component"
      error: "text component"
    }
    
    constraints: {
      @rule "error present → helper hidden"
      @rule "error state requires error message"
    }
  }
  
  # Add more patterns:
  # @pattern button-actions { ... }
  # @pattern page-header { ... }
}

# ----------------------------------------------------------------------------
# SEMANTICS
# Intent-to-Component Mapping – very valuable for LLMs!
# ----------------------------------------------------------------------------

@semantics {
  
  @intent "user selects one from options" {
    @alias "single select", "choose one"
    
    conditions: {
      "≤ 5 options": {
        component: "radio-group"
        reason: "All options immediately visible"
      }
      "> 5 options": {
        component: "select"
        reason: "Saves space"
      }
    }
  }
  
  @intent "user toggles setting" {
    conditions: {
      "immediate effect": {
        component: "switch"
        reason: "Toggle without form submit"
      }
      "form submit required": {
        component: "checkbox"
        reason: "Part of form submission"
      }
    }
  }
  
  # Add more intents as needed
}
```

---

## Template (Compact Format)

For token-optimized LLM contexts:

```dsil
#DSIL:1.0 [system-name] v[x.y.z]

## Meta
prefix[html:[prefix]-|react:[Prefix]]
config[strict|controlled|theme:light]

## Tokens
T.theme[light*|dark|auto]
T.spacing[xs|sm|md|lg|xl]
T.color.brand[primary|secondary]
T.color.semantic[success|warning|error|info]
T.breakpoint[base:0|s:768|m:1024|l:1280]px

## Icons
I.navigation: arrow-*, chevron-*, menu, close
I.action: add, edit, delete, save, search
I.status: success, error, warning, info

## Components
C.button:
  v.variant[primary*|secondary]
  v.size[small|medium*|large]
  p[disabled?:bool=false, loading?:bool=false]
  s[default!:text]
  e[click]
  !loading→disabled

C.input:
  v.size[small|medium*|large]
  p[type?:str=text, disabled?:bool=false, required?:bool=false]
  s[prefix?, suffix?]
  e[input, focus, blur]

# ... more components

## Patterns
P.form-field: [label?,field!,helper?,error?] !error→-helper

## Semantics
S."select one": ≤5→radio-group | >5→select
S."toggle": immediate→switch | form-submit→checkbox
```

---

## Checklist

Before using, verify:

- [ ] All token values are correct
- [ ] Variant names match the real system
- [ ] Constraints reflect real limitations
- [ ] No invented components/props
- [ ] Compact version is synchronized with full version
- [ ] Tested with real prompts

---

## Next Steps After Template Creation

1. **Validate**: Have an LLM generate code and check against your real system
2. **Iterate**: Adjust constraints based on LLM errors
3. **Expand**: Add components as needed
4. **Document**: Add usage hints from real experience

---

## Resources

- **Specification**: See [`../specs/DSIL-SPEC-v1.0.md`](../specs/DSIL-SPEC-v1.0.md) for complete technical specification
- **Guide**: See [`../docs/DSIL-GUIDE.md`](../docs/DSIL-GUIDE.md) for practical usage guide
- **Reference**: See [`../docs/DSIL-REFERENCE.md`](../docs/DSIL-REFERENCE.md) for complete reference documentation
- **Examples**: See [`minimal.dsil`](minimal.dsil) for a minimal example and [`porsche-ds.dsil.md`](porsche-ds.dsil.md) for an enterprise example
