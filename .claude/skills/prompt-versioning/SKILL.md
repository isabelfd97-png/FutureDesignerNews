---
name: prompt-versioning
description: >-
  Gestiona iteraciones de un prompt en el tiempo — qué cambió entre versiones, qué se probó,
  qué funcionó y qué no. Úsala cuando un prompt lleve varias iteraciones sin registro claro
  de qué se cambió y por qué, o cuando Isabel quiera comparar formalmente una versión nueva
  contra la anterior antes de reemplazarla.
---

# Prompt Versioning

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Registra las iteraciones de un prompt — qué cambió de una versión a otra, qué hipótesis
motivó el cambio, y qué resultado dio — para no perder el rastro de "por qué está escrito
así" ni repetir cambios que ya se probaron y no funcionaron.

## Cuándo se activa

Un prompt lleva varias iteraciones sin ningún registro de qué cambió y por qué, o Isabel
quiere comparar formalmente una versión nueva contra la anterior antes de reemplazarla en
producción.
