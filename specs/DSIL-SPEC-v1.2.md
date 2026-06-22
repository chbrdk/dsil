# DSIL Specification v1.2 — Core + Profiles

**Status:** Normative extension (supersedes v1.1 for instance/sync semantics)  
**Base:** [DSIL-SPEC-v1.0.md](./DSIL-SPEC-v1.0.md) (catalog language)  
**Backward compatible:** v1.0/v1.1 catalogs remain valid; profiles are opt-in.

## 1. Versioning policy

DSIL uses **three independent version axes**:

| Axis | Field | Meaning |
|------|--------|---------|
| **Core** | `dsil-core-version` | Language + instance IR rules (this document) |
| **Profile** | `syncProfile` / `profiles[]` | Optional adapter (Penpot, Figma, codegen-only, …) |
| **Manifest** | `version` in `@meta` | Your design system release (PDS 3.2, Webdesign v2.1, …) |

**Examples (Porsche, Penpot Webdesign, Material) are reference manifests**, not part of the core spec.

```
DSIL Core v1.2
├── Profile: codegen        → LLM / code validation (v1.0 focus)
├── Profile: instance-sync  → @instance, bindings, reconcile IR
└── Profile: *-adapter      → penpot-sync, figma-sync (examples)
```

## 2. Instance IR (core)

An **instance** is a filled composition tree — tool-agnostic intermediate representation.

### 2.1 `@instance` (source syntax)

```dsil
@instance card-alfa-default {
  component: penpot-card
  variant: { Button: "No" }
  slotOrder: [media, meta, body, title]
  tree: {
    slot: title { type: text, value: "Heading", typography: "H3 Heading" }
    slot: body { type: text, value: "Excerpt…", typography: "Body text" }
    slot: media { type: image, src: "/media.svg", alt: "" }
    slot: meta { type: text, value: "2023-11-14" }
  }
  layout: {
    padding: token("card.padding")
    radius: token("card.radius")
  }
}
```

### 2.2 JSON export (normative)

See `schemas/dsil-instance-ir-1.2.json`.

| Field | Required | Description |
|-------|----------|-------------|
| `instanceId` | yes | Stable id |
| `component` | yes | `@component` id |
| `variant` | no | Axis → value map from design tool |
| `slotOrder` | no | Visual order; defaults from `layoutRecipe.defaultSlotOrder` |
| `tree` | yes | Slot name → node |
| `layout` | no | Token-bound shell properties |
| `toolMeta` | no | Profile-specific metadata (never required by core) |

### 2.3 Slot node types

| type | Fields | Purpose |
|------|--------|---------|
| `text` | `value`, `typography?` | Copy + optional typography style id |
| `image` | `src`, `alt` | Media |
| `ref` | `ref`, `props`, `slots` | Nested component |
| `token` | `tokenRef` | Layout/token binding |

### 2.4 `layoutRecipe` (component-level)

Describes **how slots compose** without pixel CSS from any design tool.

```dsil
@component penpot-card {
  slots: { title: { required: true, type: text, typography: "H3 Heading" }, … }
  layoutRecipe: {
    mode: column
    gap: token("card.gap")
    defaultSlotOrder: [media, meta, body, title, action]
    regions: {
      main: { slots: [media, meta, body, title] }
      footer: { slots: [action], justify: end }
    }
    slotPresentation: {
      media: { as: media, aspect: "495/173" }
      meta: { as: inline-row, icon: calendar }
      title: { as: heading, level: 3, color: token("color.icon-star") }
    }
  }
}
```

JSON: `schemas/dsil-catalog-1.2.json` → `components.*.layoutRecipe`.

## 3. Design-tool bindings (generic)

### 3.1 `@binding` (replaces tool-specific decorators in core)

```dsil
@binding card-alfa-default {
  instanceId: card-alfa-default
  source: {
    tool: penpot
    fileId: "cc47af74-88dd-801a-8008-3250a5bf46e1"
    componentName: "Card Alfa"
  }
  layerMap: {
    "Blog post title": title
    Excerpt: body
    "Placeholders / Image2": media
    Date: meta
  }
}
```

| `source.tool` | Profile doc |
|---------------|-------------|
| `penpot` | [profiles/penpot-sync.md](./profiles/penpot-sync.md) |
| `figma` | (reserved) |
| `manual` | No pull adapter |

**Legacy:** `@penpot-binding` remains valid shorthand when `syncProfile: penpot-storybook`.

## 4. Reconcile vocabulary

`@patch` operations apply to instance IR (profile: instance-sync):

| patch | Args | Effect |
|-------|------|--------|
| `set-text` | target, value | Update text node |
| `set-slot-order` | order[] | Replace `slotOrder` |
| `bind-token` | target, tokenRef | Layout token |
| `move-child` | from, to, slot | Reparent slot (advanced) |

## 5. Validation rules (unified)

| ID | Severity | Rule |
|----|----------|------|
| V101 | error | Instance references defined `@component` |
| V102 | error | Binding references defined instance; unique source key |
| V103 | error | `ref` targets exist in catalog or primitives registry |
| V104 | error | Required slots present in `tree` |
| V105 | error | `slotOrder` entries must name slots in `tree` or `layoutRecipe` |
| V106 | warning | `tree` slots not listed in `slotOrder` (order undefined) |
| V107 | error | `layoutRecipe.defaultSlotOrder` must list declared slots |
| V108 | scaffold | Unknown source layers (binding `layerMap` miss) — profile policy |

Structural rules V001–V005 and semantic S001–S005 from v1.0 apply to catalog sections unchanged.

## 6. Runtime packages (reference)

| Package | Role |
|---------|------|
| `@creation/dsil-core` | Validate catalog + instances, compact export |
| `@creation/dsil-render` | Generic instance → DOM preview (vanilla) |
| Tool adapters | e.g. CREATION `instance_map.py` (Penpot **example** profile) |

**Penpot HTML export is not normative IR** — use only for visual diff, not production render.

## 7. Examples (non-normative)

| Path | Role |
|------|------|
| `examples/minimal.dsil` | Smallest valid catalog |
| `examples/porsche-ds.dsil.md` | Deep **codegen** catalog example |
| `examples/penpot-webdesign-layouts/` | **instance-sync** + Penpot profile example |
| `examples/material-design.dsil.md` | Public DS mapped to v1.0 |

## 8. Migration from v1.1

1. Set `meta.dsilCoreVersion: "1.2.0"` (keep `dsilVersion` for manifest if needed).
2. Add `layoutRecipe` to components that need ordered composition.
3. Rename `@penpot-binding` → `@binding` with `source.tool: penpot` (shorthand still accepted).
4. Move `penpotBinding` on instances → `toolMeta.penpot` in new exports (old field deprecated).
