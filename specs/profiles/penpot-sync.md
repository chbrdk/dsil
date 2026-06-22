# DSIL Profile: `penpot-sync`

**Extends:** [DSIL-SPEC-v1.2.md](../DSIL-SPEC-v1.2.md) instance-sync  
**Example manifest:** `examples/penpot-webdesign-layouts/`

This profile is **one adapter** for Penpot → runtime IR. It is not DSIL core.

## Shorthand

```dsil
@meta {
  config: { syncProfile: "penpot-storybook" }
}
```

Equivalent to `profiles: ["instance-sync", "penpot-sync"]`.

## Binding

Use generic `@binding` with `source.tool: penpot` and `layerMap`.

Penpot layer names map via `layerMap`. Child order from Penpot `shapes[]` / `layout-item-index` → instance `slotOrder`.

## Instance tool metadata

```json
{
  "toolMeta": {
    "penpot": {
      "penpotName": "Card Alfa",
      "fileId": "cc47af74-88dd-801a-8008-3250a5bf46e1"
    }
  },
  "syncStatus": "synced",
  "unmappedLayers": []
}
```

## Pull / push matrix (reference deployment: CREATION)

| Layer | Pull Penpot | Push runtime |
|-------|-------------|--------------|
| Tokens | Yes | CSS variables |
| Page layout | Yes | JSON sidecar |
| Instances | Yes | JSON sidecar |

## Unknown layers

Unmapped Penpot layers → `syncStatus: scaffold`, `unmappedLayers[]` — never silent drop.
