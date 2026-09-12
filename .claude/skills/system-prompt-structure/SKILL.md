---
name: system-prompt-structure
description: >-
  Anatomía de un system prompt efectivo — rol, contexto, restricciones, formato. Úsala
  cuando Isabel necesite entender o revisar las partes básicas que debería tener cualquier
  system prompt bien estructurado, antes de escribir uno desde cero o antes de auditar uno
  existente.
---

# System Prompt Structure

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Define las partes que debería tener un system prompt bien construido: **rol** (quién es la
IA en este contexto), **contexto** (qué información de fondo necesita), **restricciones**
(qué no debe hacer, qué límites respetar) y **formato** (cómo debe estructurar su
respuesta). Un prompt que mezcla estas partes sin orden claro suele producir resultados
inconsistentes.

## Cuándo se activa

Isabel necesita revisar o construir un system prompt desde sus fundamentos, o quiere
entender por qué un prompt existente produce resultados irregulares. Es la base que usa
`design-prompt` para construir uno completo.
