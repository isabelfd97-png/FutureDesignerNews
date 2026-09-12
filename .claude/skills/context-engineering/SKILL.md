---
name: context-engineering
description: >-
  Decide qué información entra en la ventana de contexto de un prompt y en qué orden, para
  que la IA priorice lo relevante y no se pierda entre información irrelevante o mal
  ordenada. Úsala cuando una función de IA tenga acceso a mucha información de fondo y no
  esté claro qué incluir, qué omitir, o en qué orden colocarla dentro del prompt.
---

# Context Engineering

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Decide qué información se incluye en el contexto de un prompt y en qué orden — no toda la
información disponible ayuda, y el orden en que se presenta puede cambiar qué prioriza la
IA. Distinto de `context-window-design` (que decide qué se recuerda entre sesiones); esta
skill decide qué entra en un prompt concreto, en el momento de construirlo.

## Cuándo se activa

Una función de IA tiene acceso a mucha información de fondo (historial, datos de la
cuenta, documentos) y no está claro qué incluir en el prompt, qué omitir, o en qué orden
presentarlo para que la IA priorice bien.
