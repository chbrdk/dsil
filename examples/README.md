# DSIL Examples

Each folder/file demonstrates a **profile**, not a separate DSL.

| Example | Profile | Format |
|---------|---------|--------|
| [minimal.dsil](./minimal.dsil) | codegen | Compact `.dsil` |
| [porsche-ds.dsil.md](./porsche-ds.dsil.md) | codegen | Markdown + `@component` blocks |
| [material-design.dsil.md](./material-design.dsil.md) | codegen | Material Design 3 reference |
| [penpot-webdesign-layouts/](./penpot-webdesign-layouts/) | instance-sync + penpot-sync | `catalog.json` + `.dsil.md` sidecars |

## Penpot example (`penpot-webdesign-layouts`)

Bundled from CREATION via `npm run sync:dsil-example` in the CREATION repo.

Key v1.2 artifacts:

- `catalog.json` — SSOT with `layoutRecipe`, instances, generic bindings
- `bindings.json` — `source.tool: penpot` layer maps
- `instances/*.dsil` — human-readable instance sidecars

Validation reference implementation: `@creation/dsil-core` in the CREATION monorepo.
