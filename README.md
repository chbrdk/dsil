# DSIL - Design System Interface Layer

> A domain-specific language for describing design systems, optimized for LLM consumption.

**Version**: 1.0.0  
**License**: MIT  
**Authors**: Chris Bordeck (MSQ DX / United Digital Group)

---

## What is DSIL?

DSIL (Design System Interface Layer) is a structured format for describing design systems in a way that Large Language Models can reliably understand and use. It bridges the gap between human-readable documentation and machine-interpretable specifications.

### The Problem

When developers ask LLMs to generate UI code with a design system, common errors occur:

| Problem | Example | Impact |
|---------|---------|--------|
| Invented props | `<Button color="blue">` | Prop doesn't exist |
| Invalid combinations | `loading` + `disabled` manually | Redundant code |
| Missing handlers | `<Modal open={true}>` without `onClose` | Runtime error |
| Wrong component | `<Dropdown>` instead of `<Select>` | Component doesn't exist |

### The Solution

DSIL provides:

- **Explicit Constraints** - Rules like "loading implies disabled" are codified
- **Semantic Mappings** - "When to use Select vs. Radio?" is defined
- **Token Efficiency** - Compact format saves 80% of tokens
- **Single Source of Truth** - Everything in one structured place

---

## Project Structure

```
dsil-repo/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── specs/
│   └── DSIL-SPEC-v1.0.md       # Technical Specification
├── docs/
│   ├── DSIL-GUIDE.md           # Practical Guide
│   └── DSIL-REFERENCE.md       # Complete Reference
└── examples/
    ├── minimal.dsil            # Minimal example (3 components)
    ├── porsche-ds.dsil.md      # Enterprise example (40+ components)
    └── starter-template.md     # Blank template
```

---

## Quick Start

### 1. Read the Documentation

- **[Specification](specs/DSIL-SPEC-v1.0.md)** – Complete technical specification
- **[Guide](docs/DSIL-GUIDE.md)** – Practical hands-on guide
- **[Reference](docs/DSIL-REFERENCE.md)** – Complete reference documentation

### 2. Create Your DSIL File

Start with the [starter template](examples/starter-template.md) or see the examples:
- [Minimal example](examples/minimal.dsil) – Simple 3-component system
- [Material Design example](examples/material-design.dsil.md) – Based on Google's Material Design 3

```dsil
@meta {
  name: "my-design-system"
  version: "1.0.0"
  dsil-version: "1.0.0"
  prefix: { html: "my-", react: "My" }
}

@component my-button {
  @doc "Interactive button component"
  @controlled false
  
  variants: {
    variant: { primary: {}, secondary: {} }
  }
  
  props: {
    variant: { type: "primary" | "secondary", default: "primary" }
    disabled: { type: boolean, default: false }
    loading: { type: boolean, default: false }
  }
  
  slots: {
    default: { required: true, type: text }
  }
  
  events: {
    click: { native: true }
  }
  
  constraints: {
    @rule "loading implies disabled"
  }
}
```

### 3. Use in LLM Prompts

Convert to Compact format for token-efficient LLM usage:

```
#DSIL:1.0 my-design-system v1.0.0

C.my-button:
  v[primary*|secondary]
  p[variant?:str=primary, disabled?:bool=false, loading?:bool=false]
  s[default!:text]
  e[click]
  !loading implies disabled
```

See the [Guide](docs/DSIL-GUIDE.md#using-dsil-with-ai-tools) for detailed instructions on using DSIL with AI tools like Cursor, ChatGPT, and Claude.

---

## Core Concepts

### Dual Format

| Format | Use Case | Token Efficiency |
|--------|----------|------------------|
| Full | Writing, reviewing, documentation | Baseline |
| Compact | LLM system prompts, chat context | 80% reduction |

### Sections

| Section | Purpose |
|---------|---------|
| `@meta` | System identity and configuration |
| `@tokens` | Design tokens (spacing, colors, etc.) |
| `@icons` | Available icon names |
| `@types` | Reusable type definitions |
| `@component` | Component definitions |
| `@pattern` | Composition patterns |
| `@semantics` | Intent-to-component mapping |
| `@i18n` | Internationalization |
| `@rtl` | Right-to-left support |
| `@animation` | Motion specifications |
| `@a11y` | Accessibility requirements |

### Controlled Components

Components requiring external state management are marked with `@controlled true`:

```dsil
@component my-modal {
  @controlled true
  
  props: {
    open: { type: boolean, required: true }
  }
  
  events: {
    dismiss: { payload: {} }
  }
  
  constraints: {
    @rule "dismiss must be handled" { critical: true }
  }
}
```

---

## Documentation

This repository contains comprehensive documentation for DSIL:

### Specification
- **[DSIL-SPEC-v1.0.md](specs/DSIL-SPEC-v1.0.md)** – Complete technical specification with all syntax rules, sections, and formal definitions

### Guides
- **[DSIL-GUIDE.md](docs/DSIL-GUIDE.md)** – Practical guide with quick start, examples, best practices, troubleshooting, and AI tool integration
- **[DSIL-REFERENCE.md](docs/DSIL-REFERENCE.md)** – Complete reference documentation with full syntax, all features, examples, and token budgets

### Examples
- **[minimal.dsil](examples/minimal.dsil)** – Minimal example demonstrating core features
- **[material-design.dsil.md](examples/material-design.dsil.md)** – Material Design 3 example based on Google's publicly available design system
- **[porsche-ds.dsil.md](examples/porsche-ds.dsil.md)** – Enterprise-level example with 40+ components
- **[starter-template.md](examples/starter-template.md)** – Blank template to get started quickly
- **[rag-implementation-example.py](examples/rag-implementation-example.py)** – Complete RAG implementation in Python
- **[rag-implementation-example.ts](examples/rag-implementation-example.ts)** – Complete RAG implementation in TypeScript
- **[code-validation-example.ts](examples/code-validation-example.ts)** – TypeScript code validation and transformation
- **[code-validation-example.py](examples/code-validation-example.py)** – Python code validation and transformation

---

## Token Budget Guidelines

| System Size | Components | Full Format | Compact Format |
|-------------|------------|-------------|----------------|
| Minimal | 5-10 | 2,000-4,000 | 400-800 |
| Standard | 15-25 | 5,000-10,000 | 1,000-2,000 |
| Enterprise | 40+ | 15,000-30,000 | 3,000-6,000 |

---

## Getting Started

1. **Read the Guide** – Start with [DSIL-GUIDE.md](docs/DSIL-GUIDE.md) for a practical introduction
2. **Review Examples** – Check [minimal.dsil](examples/minimal.dsil) and [porsche-ds.dsil.md](examples/porsche-ds.dsil.md)
3. **Use the Template** – Start with [starter-template.md](examples/starter-template.md)
4. **Reference** – Use [DSIL-REFERENCE.md](docs/DSIL-REFERENCE.md) when you need detailed syntax
5. **Validate Code** – Use [code-validation-example.ts](examples/code-validation-example.ts) or [code-validation-example.py](examples/code-validation-example.py) to validate LLM-generated code

## Use Cases

DSIL is perfect for:

- **AI-Powered Code Generation** – Provide DSIL to LLMs for accurate component usage
- **Design System Documentation** – Single source of truth for your design system
- **Onboarding** – Help new developers understand your design system quickly
- **Code Validation** – Validate and transform LLM-generated code to ensure it conforms to your design system (see [code-validation-example.ts](examples/code-validation-example.ts) and [code-validation-example.py](examples/code-validation-example.py))
- **Token Efficiency** – Compact format saves 80% of tokens vs. traditional docs

## Contributing

Contributions are welcome! Please read the [specification](specs/DSIL-SPEC-v1.0.md) before submitting changes.

---

## License

MIT License - see LICENSE file for details.

---

## Authors

- **Chris Bordeck** - MSQ DX / United Digital Group

---

*DSIL v1.0 - Design System Interface Layer*
