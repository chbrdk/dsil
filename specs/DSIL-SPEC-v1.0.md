# DSIL – Design System Interface Layer

## Specification v1.0

> **Status**: Official Release  
> **Version**: 1.0.0  
> **Date**: 2026-01-07  
> **Authors**: Chris Bordeck (MSQ DX / United Digital Group)  
> **License**: MIT

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Design Principles](#2-design-principles)
3. [Syntax Overview](#3-syntax-overview)
4. [Core Sections](#4-core-sections)
5. [Extension Sections](#5-extension-sections)
6. [Compact Format](#6-compact-format)
7. [Validation Rules](#7-validation-rules)
8. [Implementation Guide](#8-implementation-guide)

---

## 1. Introduction

### 1.1 What is DSIL?

**DSIL (Design System Interface Layer)** is a domain-specific language designed to describe design systems in a format optimized for Large Language Model (LLM) consumption. It bridges the gap between human-readable design system documentation and machine-interpretable specifications.

### 1.2 Problem Statement

| Problem | Impact |
|---------|--------|
| **Verbose Documentation** | Consumes excessive context tokens |
| **Ambiguous Specifications** | LLMs generate invalid component combinations |
| **Missing Constraints** | No explicit rules for valid/invalid states |
| **Scattered Information** | Props, variants, examples in different places |
| **No Semantic Intent** | LLMs can't infer "when to use what" |

### 1.3 Solution

DSIL provides:

- **Token-Efficient Encoding**: Compact syntax preserving semantic meaning
- **Explicit Constraints**: Rules preventing invalid combinations
- **Semantic Mappings**: Intent-to-component decision trees
- **Dual Formats**: Full (human-readable) and Compact (LLM-optimized)
- **Validation-Ready**: Output validatable against schema

### 1.4 Token Budget Guidelines

| System Size | Components | Full Format | Compact Format |
|-------------|------------|-------------|----------------|
| Minimal | 5-10 | 2,000-4,000 | 400-800 |
| Standard | 15-25 | 5,000-10,000 | 1,000-2,000 |
| Enterprise | 40+ | 15,000-30,000 | 3,000-6,000 |

---

## 2. Design Principles

| Principle | Description |
|-----------|-------------|
| **Token Economy** | Minimize tokens while maximizing semantic density |
| **Unambiguity** | Every construct has exactly one interpretation |
| **Composability** | Small primitives combine into complex structures |
| **Validation-Ready** | Output validatable against schema |
| **Human Readable** | Developers can read/write DSIL without tools |
| **Framework Agnostic** | Works with React, Vue, Angular, Web Components |

---

## 3. Syntax Overview

### 3.1 Basic Structure

```dsil
# Comment (single line)

@section-name {
  property: value
  
  nested-block: {
    key: value
  }
  
  @subsection {
    ...
  }
}
```

### 3.2 Data Types

| Type | Syntax | Example |
|------|--------|---------|
| String | `"value"` or `value` | `name: "Acme DS"` |
| Number | `123` | `columns: 12` |
| Boolean | `true` / `false` | `required: true` |
| Array | `[a, b, c]` | `values: [sm, md, lg]` |
| Enum | `a \| b \| c` | `type: primary \| secondary` |
| Object | `{ key: value }` | `{ min: 0, max: 100 }` |
| Reference | `@ref(path)` | `@ref(tokens.color.primary)` |
| Type | `@type(TypeName)` | `@type(IconName)` |

### 3.3 Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `!` | Required | `label!: string` |
| `?` | Optional | `icon?: IconName` |
| `*` | Default | `size: sm \| md* \| lg` |
| `→` | Maps to | `options ≤ 5 → radio` |
| `+` | Extends | `@extends base +newProp` |
| `@` | Decorator | `@component`, `@doc` |
| `#` | Comment | `# This is a comment` |

### 3.4 Decorators

| Decorator | Purpose |
|-----------|---------|
| `@doc` | Documentation string |
| `@deprecated` | Marks as deprecated |
| `@since` | Version introduced |
| `@see` | External reference URL |
| `@controlled` | Requires external state |
| `@tag-*` | Framework-specific names |
| `@alias` | Alternative names |

---

## 4. Core Sections

### 4.1 @meta

```dsil
@meta {
  name: "design-system-name"
  version: "1.0.0"
  dsil-version: "1.0.0"
  
  prefix: {
    html: "p-"
    react: "P"
  }
  
  imports: {
    react: "@package/components-react"
  }
  
  config: {
    strict: true
    controlled: true
    theme: "light"
  }
}
```

### 4.2 @tokens

```dsil
@tokens {
  theme: {
    values: [light, dark, auto]
    default: "light"
  }
  
  spacing: {
    @group static {
      4: { value: "4px", css: "$spacing-4" }
      8: { value: "8px", css: "$spacing-8" }
      16: { value: "16px", css: "$spacing-16" }
    }
    
    @group fluid {
      sm: { css: "$spacing-fluid-sm" }
      md: { css: "$spacing-fluid-md" }
      lg: { css: "$spacing-fluid-lg" }
    }
  }
  
  color: {
    @group brand {
      primary: { value: "#000000", css: "$color-primary" }
    }
    
    @group notification {
      success: { value: "#018A16" }
      warning: { value: "#FF9B00" }
      error: { value: "#E00000" }
      info: { value: "#2762D9" }
    }
  }
  
  typography: {
    @group heading {
      large: { css: "@include heading-large" }
      medium: { css: "@include heading-medium" }
      small: { css: "@include heading-small" }
    }
    
    @group text {
      large: { css: "@include text-large" }
      medium: { css: "@include text-medium" }
      small: { css: "@include text-small", default: true }
    }
  }
  
  breakpoint: {
    base: { value: "0px" }
    s: { value: "760px" }
    m: { value: "1000px" }
    l: { value: "1300px" }
  }
  
  motion: {
    duration: {
      short: { value: "150ms", css: "$motion-short" }
      moderate: { value: "250ms", css: "$motion-moderate" }
      long: { value: "400ms", css: "$motion-long" }
    }
    
    easing: {
      base: { value: "cubic-bezier(0.25, 0.1, 0.25, 1)" }
    }
  }
}
```

### 4.3 @icons

```dsil
@icons {
  @group navigation {
    arrow-up, arrow-down, arrow-left, arrow-right
    external, return, logout
  }
  
  @group action {
    add, close, check, edit, delete
    search, filter, download, upload, save
  }
  
  @group status {
    information, information-filled
    success, success-filled
    warning, warning-filled
    error, error-filled
  }
  
  @group user {
    user, user-filled
    heart, heart-filled
    star, star-filled
  }
  
  special: {
    none: { @doc "No icon" }
  }
}
```

### 4.4 @types

```dsil
@types {
  @type BreakpointCustomizable<T> {
    @doc "Responsive values per breakpoint"
    
    definition: T | {
      base?: T
      s?: T
      m?: T
      l?: T
    }
    
    example: |
      // Simple
      compact={true}
      
      // Responsive
      compact={{ base: true, m: false }}
  }
  
  @type FormState {
    values: [none, success, error]
    default: none
  }
  
  @type Theme {
    values: [light, dark, auto]
    default: light
  }
  
  @type IconName {
    @ref(@icons)
    special: none
  }
}
```

### 4.5 @components

#### Structure

```dsil
@component component-name {
  @doc "Description"
  @controlled true|false
  @tag-react ReactName
  
  variants: {
    variant-name: {
      option1: { @doc "Description" }
      option2: { @doc "Description" }
    }
  }
  
  props: {
    propName: {
      type: Type
      default: "value"
      required: true|false
      @doc "Description"
    }
  }
  
  slots: {
    slotName: {
      required: true|false
      type: node|text
      @doc "Description"
    }
  }
  
  events: {
    eventName: {
      payload: { key: type }
      @doc "Description"
      handling: |
        // Code example
    }
  }
  
  constraints: {
    @rule "condition → result" {
      error: "Error message"
      critical: true|false
    }
  }
  
  a11y: {
    role: "aria-role"
    @rule "requirement"
  }
  
  examples: {
    name: |
      // Code
  }
}
```

#### Example: Button

```dsil
@component p-button {
  @doc "Interactive element for user actions"
  @controlled false
  @tag-react PButton
  
  variants: {
    variant: {
      primary: { @doc "Main CTA" }
      secondary: { @doc "Secondary action" }
      ghost: { @doc "Minimal appearance" }
    }
  }
  
  props: {
    variant: { type: "primary" | "secondary" | "ghost", default: "primary" }
    compact: { type: boolean | BreakpointCustomizable<boolean>, default: false }
    disabled: { type: boolean, default: false }
    loading: { type: boolean, default: false }
    icon: { type: IconName, default: "none" }
    type: { type: "button" | "submit" | "reset", default: "submit" }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    default: { required: true, type: text, @doc "Button label" }
  }
  
  events: {
    click: { native: true }
  }
  
  constraints: {
    @rule "loading:true → disabled implicit"
    @rule "hideLabel:true && icon:'none' → invalid"
  }
  
  examples: {
    basic: |
      <PButton>Save</PButton>
      <PButton variant="secondary">Cancel</PButton>
      <PButton loading>Saving...</PButton>
  }
}
```

#### Example: Controlled Accordion

```dsil
@component p-accordion {
  @doc "Collapsible content. CONTROLLED COMPONENT."
  @controlled true
  @tag-react PAccordion
  
  props: {
    heading: { type: string, required: true }
    headingTag: { type: "h1"|"h2"|"h3"|"h4"|"h5"|"h6", default: "h2" }
    open: { type: boolean, default: false, @doc "CONTROLLED: Must manage via state" }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    default: { required: true, type: node }
  }
  
  events: {
    update: {
      payload: { open: boolean }
      @doc "Fired when user clicks header"
      handling: |
        const [isOpen, setIsOpen] = useState(false);
        <PAccordion 
          open={isOpen} 
          onUpdate={(e) => setIsOpen(e.detail.open)}
        />
    }
  }
  
  constraints: {
    @rule "MUST handle update event" {
      error: "Accordion won't toggle without handler"
      critical: true
    }
  }
}
```

### 4.6 @patterns

```dsil
@patterns {
  
  @pattern form-field {
    @doc "Standard form field structure"
    
    structure: [label?, field!, description?, message?]
    
    components: {
      label: "p-text or slot='label'"
      field: "p-input-* | p-select | p-textarea"
      description: "p-text[size:x-small]"
      message: "p-text[size:x-small]"
    }
    
    constraints: {
      @rule "state:'error' → message required"
      @rule "required:true → label shows *"
    }
  }
  
  @pattern button-actions {
    @doc "Button group for forms/dialogs"
    
    structure: |
      Mobile: [Primary] [Secondary] (stacked)
      Desktop: [Ghost] [Secondary] [Primary] (row)
    
    implementation: |
      <PButtonGroup direction={{ base: 'column', s: 'row' }}>
        <PButton variant="ghost">Cancel</PButton>
        <PButton variant="primary">Save</PButton>
      </PButtonGroup>
    
    constraints: {
      @rule "Primary at end"
      @rule "Max 1 primary"
      @rule "Max 3 buttons"
    }
  }
  
  @pattern modal-confirmation {
    @doc "Confirmation dialog"
    
    structure: [heading, warning-notification, footer-buttons]
    
    implementation: |
      <PModal heading="Confirm" onDismiss={close}>
        <PInlineNotification state="warning" description="..." />
        <template slot="footer">
          <PButtonGroup>
            <PButton variant="ghost">Cancel</PButton>
            <PButton variant="primary">Confirm</PButton>
          </PButtonGroup>
        </template>
      </PModal>
  }
}
```

### 4.7 @semantics

```dsil
@semantics {
  
  @intent "select one from options" {
    conditions: {
      "≤5, horizontal space": → p-segmented-control
      "≤7": → p-radio-group
      ">7": → p-select
      ">7, searchable": → p-select[filter:true]
    }
  }
  
  @intent "select multiple from options" {
    conditions: {
      "≤5": → multiple p-checkbox
      ">5": → p-multi-select
    }
  }
  
  @intent "toggle binary setting" {
    conditions: {
      "immediate effect": → p-switch
      "form submit required": → p-checkbox
    }
  }
  
  @intent "text input" {
    conditions: {
      "email": → p-input-email
      "phone": → p-input-tel
      "search": → p-input-search
      "password": → p-input-password
      "multiline": → p-textarea
      "default": → p-input-text
    }
  }
  
  @intent "show feedback" {
    conditions: {
      "page-level": → p-banner
      "inline": → p-inline-notification
      "temporary": → p-toast
      "on-demand": → p-popover
    }
  }
  
  @intent "loading state" {
    conditions: {
      "button action": → p-button[loading:true]
      "content area": → p-spinner
    }
  }
}
```

---

## 5. Extension Sections

### 5.1 @i18n

```dsil
@i18n {
  config: {
    defaultLocale: "en"
    supportedLocales: ["de", "en", "fr", "es"]
    rtlLocales: ["ar", "he"]
  }
  
  components: {
    p-pagination: {
      intl-keys: {
        prev: { default: "Previous", de: "Zurück" }
        next: { default: "Next", de: "Weiter" }
        page: { default: "Page", de: "Seite" }
      }
      
      example: |
        <PPagination intl={{ prev: 'Zurück', next: 'Weiter' }} />
    }
    
    p-select: {
      intl-keys: {
        noResults: { default: "No results", de: "Keine Ergebnisse" }
        clear: { default: "Clear", de: "Löschen" }
      }
    }
    
    p-modal: {
      intl-keys: {
        close: { default: "Close", de: "Schließen" }
      }
    }
  }
  
  constraints: {
    @rule "intl prop overrides defaults"
    @rule "Missing keys → fallback to default locale"
    @rule "Placeholders like {count} must be preserved"
  }
}
```

### 5.2 @rtl

```dsil
@rtl {
  activation: '<html dir="rtl" lang="ar">'
  
  directional-icons: {
    mirrored: [arrow-left, arrow-right, external, return]
    preserved: [arrow-up, arrow-down, check, close, heart]
  }
  
  components: {
    p-button: "Icon position mirrored"
    p-tabs: "Direction reversed, keyboard inverted"
    p-carousel: "Slides RTL, buttons swapped"
    p-flyout: "position:end → opens left"
    p-modal: "Close button on left"
    p-input-*: "Label right, text RTL"
  }
  
  css: {
    @rule "Use start/end not left/right"
    @rule "Tailwind: ms-* not ml-*"
  }
}
```

### 5.3 @animation

```dsil
@animation {
  tokens: {
    duration: {
      short: "150ms"
      moderate: "250ms"
      long: "400ms"
    }
    
    easing: {
      base: "cubic-bezier(0.25, 0.1, 0.25, 1)"
      ease-out: "cubic-bezier(0, 0, 0.2, 1)"
      ease-in: "cubic-bezier(0.4, 0, 1, 1)"
    }
  }
  
  reduced-motion: {
    @doc "Respects prefers-reduced-motion"
    behavior: "Important animations shortened, decorative removed"
  }
  
  components: {
    p-accordion: {
      expand: { property: "height, opacity", duration: "moderate" }
      chevron: { property: "transform", duration: "short" }
    }
    
    p-modal: {
      backdrop: { property: "opacity", duration: "moderate" }
      content: { property: "opacity, scale", duration: "moderate" }
    }
    
    p-flyout: {
      slide: { property: "transform", duration: "moderate" }
    }
    
    p-toast: {
      enter: { property: "opacity, translateY", duration: "short" }
      exit: { property: "opacity, translateX", duration: "short" }
    }
    
    p-button: {
      hover: { property: "background", duration: "short" }
      active: { property: "scale", duration: "instant" }
      loading: { property: "rotate", duration: "1000ms", iteration: "infinite" }
    }
    
    p-spinner: {
      rotate: { duration: "1000ms", easing: "linear", iteration: "infinite" }
    }
  }
  
  patterns: {
    skeleton: "shimmer @1500ms infinite"
    page-transition: "opacity, x @250ms"
    staggered-list: "staggerChildren: 100ms"
  }
}
```

### 5.4 @a11y

```dsil
@a11y {
  live-regions: {
    polite: "Waits for screen reader"
    assertive: "Interrupts immediately"
    off: "No announcement"
  }
  
  components: {
    p-toast: {
      aria-live: "polite"
      role: "status"
      announce: "{state}: {message}"
    }
    
    p-inline-notification: {
      aria-live: {
        "state:info|success|warning": "polite"
        "state:error": "assertive"
      }
      role: {
        "state:error|warning": "alert"
        default: "status"
      }
    }
    
    p-modal: {
      announce: { open: "Dialog: {heading}", close: "Dialog closed" }
      focus: { open: "first interactive", close: "return to trigger" }
      requirements: ["focus-trap", "ESC closes", "aria-modal"]
    }
    
    p-accordion: {
      aria-expanded: "dynamic"
      announce: { expand: "{heading} expanded", collapse: "{heading} collapsed" }
      keyboard: ["Enter/Space: toggle"]
    }
    
    p-tabs: {
      aria-selected: "dynamic"
      announce: "{label} selected, {index}/{total}"
      keyboard: ["Arrow: navigate", "Home: first", "End: last"]
    }
    
    p-select: {
      aria-expanded: "dynamic"
      announce: {
        open: "{count} options"
        select: "{label} selected"
        filter: "{count} results"
      }
      keyboard: ["Arrow: navigate", "Enter: select", "ESC: close"]
    }
  }
  
  requirements: {
    focus: ["visible", "logical order", "trap in modals", "return after close"]
    contrast: ["4.5:1 normal text", "3:1 large text", "no color-only"]
    keyboard: ["all interactive accessible", "visible focus", "ESC closes overlays"]
  }
}
```

---

## 6. Compact Format

### 6.1 Prefix Reference

| Prefix | Section |
|--------|---------|
| `#DSIL:` | Header |
| `T.` | Tokens |
| `I.` | Icons |
| `C.` | Components |
| `P.` | Patterns |
| `S.` | Semantics |
| `A.` | Animation |
| `L.` | Live/A11y |

### 6.2 Notation Reference

| Notation | Meaning |
|----------|---------|
| `*` | Default |
| `!` | Required |
| `?` | Optional |
| `=` | Default value |
| `:` | Type |
| `[]` | Options |
| `{}` | Payload |
| `→` | Maps to |
| `+` | Extension |
| `@` | Decorator |

### 6.3 Type Abbreviations

| Short | Full |
|-------|------|
| `BC<T>` | `BreakpointCustomizable<T>` |
| `bool` | `boolean` |
| `str` | `string` |
| `num` | `number` |
| `Icon` | `IconName` |

### 6.4 Complete Template

```dsil
#DSIL:1.0 {name} v{version}

## Meta
prefix[html:{p-}|react:{P}]
import.react: "{package}"
config[strict|controlled|theme:light]

## Tokens
T.theme[light*|dark|auto]
T.spacing[4|8|16|24|32|48]px
T.color.notification[success|warning|error|info]
T.typography.heading[large|medium|small]
T.typography.text[large|medium|small*|x-small]
T.breakpoint[base:0|s:760|m:1000|l:1300]px
T.motion.duration[short:150|moderate:250|long:400]ms

## Icons
I.nav: arrow-*, external, return
I.action: add, close, check, edit, delete, search
I.status: information, success, warning, error
I.special: none

## Components
C.{name} [@controlled]:
  v[variant1*|variant2]
  p[prop:type=default, prop2?, prop3!]
  s[slot!, slot2?]
  e[event({payload})]
  !constraint

## Patterns
P.{name}: [slot1, slot2!, slot3?]

## Semantics
S."{intent}": condition → component

## i18n
C.{name} +intl{key1, key2, key3:{placeholder}}

## RTL
@rtl.icons.mirrored: [list]
@rtl.icons.preserved: [list]

## Animation
A.{component}: animation[properties] @duration

## A11y
L.{component}: aria-live:polite, role:status, announce:"template"
```

---

## 7. Validation Rules

### 7.1 Structural Rules

| Rule | Description |
|------|-------------|
| `V001` | Every `@component` must have `@doc` |
| `V002` | Every prop must have `type` |
| `V003` | Required slots must be marked with `!` |
| `V004` | Controlled components must document event handling |
| `V005` | Constraints must have `error` messages |

### 7.2 Semantic Rules

| Rule | Description |
|------|-------------|
| `S001` | `loading:true` implies `disabled` |
| `S002` | `hideLabel:true` requires `icon` or `aria-label` |
| `S003` | `state:'error'` requires `message` |
| `S004` | Controlled components require event handlers |
| `S005` | Primary button max 1 per visible area |

### 7.3 Constraint Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `→` | Implies | `loading → disabled` |
| `&&` | And | `hideLabel && !icon` |
| `\|\|` | Or | `icon \|\| aria-label` |
| `!` | Not | `!valid` |
| `≤` / `≥` | Comparison | `options ≤ 5` |

---

## 8. Implementation Guide

### 8.1 For LLM System Prompts

#### Direct Prompt (Small to Medium Systems)

For systems with 5-30 components, include the complete DSIL Compact Format directly in the system prompt:

```
You are an assistant that generates UI code using the {name} design system.

{DSIL Compact Format here}

Rules:
1. Only use components defined in the DSIL
2. Respect all constraints (marked with !)
3. Use semantics to choose appropriate components
4. Handle controlled components with proper state
5. Include intl props for i18n support
```

#### RAG-Based Prompt (Enterprise Systems)

For systems with 40+ components, use Retrieval-Augmented Generation (RAG) to include only relevant components:

**Core (Always in Prompt):**
- `@meta` - System identity
- `@tokens` - All design tokens
- `@semantics` - All intent mappings (critical)
- `@patterns` - Common patterns
- Core components (5-10 most used)

**Retrieved (Via RAG):**
- Extended components (retrieved based on query)
- Rare patterns (retrieved when relevant)
- Extension sections (i18n, rtl, animation, a11y - when needed)

See [DSIL-GUIDE.md](../docs/DSIL-GUIDE.md#using-rag-retrieval-augmented-generation-with-dsil) and [DSIL-REFERENCE.md](../docs/DSIL-REFERENCE.md#10-rag-retrieval-augmented-generation-integration) for complete RAG implementation details.

**Decision Matrix:**

| System Size | Components | Compact Tokens | Recommendation |
|-------------|------------|----------------|----------------|
| Small | 5-15 | 400-1,500 | Direct prompt (full DSIL) |
| Medium | 15-30 | 1,500-3,000 | Direct prompt or RAG (context dependent) |
| Enterprise | 40+ | 3,000-6,000+ | RAG recommended |

### 8.2 For Code Generation

When implementing DSIL parsers or code generators:

1. Parse DSIL source into an abstract syntax tree (AST)
2. Validate component usage against defined constraints
3. Generate framework-specific code (React, Vue, Angular, Web Components, etc.)
4. Apply patterns for component composition
5. Include accessibility attributes as specified in `@a11y` sections

**Validation During Generation:**
- Check all component names exist in DSIL manifest
- Verify all props match component definitions
- Ensure variant values are in allowed set
- Validate constraints are satisfied
- Include required props and handlers
- Use correct framework-specific syntax

### 8.3 For Design Tooling Integration

DSIL can be used with design tools and systems:

1. Import DSIL as a component library definition format
2. Validate designs against defined constraints and rules
3. Generate documentation from `@doc` annotations
4. Export tokens to CSS variables, SCSS maps, JSON, or other formats
5. Validate component prop combinations in design tools

### 8.4 For RAG Implementation

When implementing RAG for DSIL:

1. **Split DSIL** into core (always in prompt) and extended (retrieved on demand)
2. **Create embeddings** for component definitions using text embedding models
3. **Index components** in a vector database (ChromaDB, Pinecone, Weaviate, etc.)
4. **Implement retrieval** combining keyword matching and semantic search
5. **Assemble context** with core DSIL + retrieved components
6. **Convert to Compact Format** for token efficiency

See [DSIL-REFERENCE.md](../docs/DSIL-REFERENCE.md#10-rag-retrieval-augmented-generation-integration) for detailed implementation guide.

### 8.5 For Code Validation

When validating LLM-generated code against DSIL specifications:

1. **Parse Generated Code**
   - Convert to Abstract Syntax Tree (AST)
   - Extract component usages, props, variants, event handlers
   - Identify framework (React, Vue, Angular, Web Components)

2. **Validate Against DSIL**
   - Component existence: Verify all component names exist in DSIL
   - Prop validation: Check props match component definitions
   - Variant validation: Ensure variant values are in allowed set
   - Constraint checking: Validate all DSIL constraints are satisfied
   - Required props: Check required props and handlers are present
   - Framework syntax: Verify framework-specific syntax is correct

3. **Transform and Fix**
   - Remove invalid props
   - Fix invalid variant values (use default or first valid option)
   - Apply constraint fixes automatically (e.g., `loading → disabled`)
   - Add missing required props with default values
   - Convert component names for framework-specific usage
   - Fix syntax errors

4. **Error Reporting**
   - Report validation errors with component name, prop, line number
   - Provide fix suggestions
   - Log validation results for DSIL improvement

5. **Auto-Fix Strategies**
   - Safe fixes: Remove invalid props, fix variant values
   - Constraint fixes: Apply constraint rules automatically
   - Complex fixes: Use LLM self-correction for cases AST/regex can't handle

**Validation Approaches:**

| Approach | Precision | Speed | Use Case |
|----------|-----------|-------|----------|
| **AST-based** | High | Medium | Production systems, complex code |
| **Regex-based** | Medium | Fast | Quick validation, simple code |
| **LLM self-correction** | High | Slow | Complex errors, fallback option |
| **Hybrid** | High | Variable | Best practice (combines all) |

See [DSIL-GUIDE.md](../docs/DSIL-GUIDE.md#validating-and-transforming-llm-generated-code) and [DSIL-REFERENCE.md](../docs/DSIL-REFERENCE.md#11-code-validation--transformation) for detailed implementation guides and examples.

---

## 9. Appendix

### 9.1 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-07 | Initial release |

### 9.2 Contributors

- 
- Chris (MSQ DX / UDG) - Requirements, testing

### 9.3 References

- Porsche Design System: https://designsystem.porsche.com
- Web Components: https://www.webcomponents.org
- ARIA Practices: https://www.w3.org/WAI/ARIA/apg/

---

**End of DSIL Specification v1.0**
