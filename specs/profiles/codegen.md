# DSIL Profile: `codegen`

**Extends:** [DSIL-SPEC-v1.0.md](../DSIL-SPEC-v1.0.md)  
**Examples:** `examples/porsche-ds.dsil.md`, `examples/material-design.dsil.md`

## Purpose

Optimize DSIL catalogs for **LLM consumption** and **code validation** against a component vocabulary. No design-tool pull/push.

## Features

- Full + compact dual format (`#DSIL:1.0`, `C.`, `T.`, `S.`)
- `@patterns`, `@semantics`, constraint language
- Framework `imports` (React, Vue, …) in examples — not required by core

## Not in scope

- `@instance`, `@binding`, `slotOrder`, reconcile patches
- Storybook sidecars or orchestrator SSOT

Porsche PDS in CREATION uses this profile via `vendor/porsche-dsil/` + `pds-registry.v3.json` — separate from Penpot instance sync.
