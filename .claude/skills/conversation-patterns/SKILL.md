---
name: conversation-patterns
description: >-
  Fundamentos de turn-taking, secuencias de reparación (cuando hay un malentendido y hay
  que corregirlo) y estructura de diálogo entre humano e IA. Úsala cuando Isabel diseñe
  cualquier interacción conversacional con IA y quiera que los malentendidos se manejen con
  una secuencia explícita de reconocimiento y corrección, en vez de que la IA reintente sin
  reconocer el error.
---

# Conversation Patterns

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Cubre los fundamentos de cómo se estructura un diálogo entre humano e IA: quién habla
cuándo (turn-taking), y sobre todo, qué pasa cuando algo se malinterpreta —
las **secuencias de reparación**: reconocer explícitamente el malentendido antes de
reintentar, en vez de ignorarlo y responder como si nada.

## Cuándo se activa

Isabel diseña una interacción conversacional (chat, asistente) y quiere definir cómo se
manejan los malentendidos, o revisar si el turn-taking actual tiene sentido. Suele
combinarse con `mixed-initiative-flow` (quién lidera) y alimenta a `design-conversation`
cuando se construye el flujo completo.
