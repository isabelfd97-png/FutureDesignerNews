---
name: mixed-initiative-flow
description: >-
  Decide cuándo lidera la IA y cuándo lidera el usuario en una interacción, y cómo se cede
  el control de uno a otro. Úsala cuando Isabel diseñe una función de IA y no esté claro si
  debe esperar pasiva a que el usuario pida algo, o proponer proactivamente — y qué pasa en
  el momento exacto de ceder el control.
---

# Mixed-Initiative Flow

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Define quién tiene la iniciativa en cada momento de una interacción con IA: si la IA
espera pasiva a que el usuario pida algo, o propone proactivamente (ej. "veo que esta
campaña terminó ayer, ¿la comparo con la anterior?"), y cómo se cede el control de una
parte a otra sin que se sienta abrupto.

## Cuándo se activa

Isabel diseña una función de IA y no está claro si debe ser reactiva o proactiva, o en qué
punto exacto del flujo debería la IA "ceder la palabra" de vuelta al usuario. Es la base
que usa `map-initiative` para mapear un flujo completo etapa por etapa.
