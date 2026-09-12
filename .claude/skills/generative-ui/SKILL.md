---
name: generative-ui
description: >-
  Diseña interfaces donde la IA genera componentes de UI dinámicamente (una gráfica, una
  tarjeta, un formulario) en vez de responder solo con texto. Úsala cuando Isabel diseñe
  una función donde la respuesta de la IA deba tomar forma de componente visual generado en
  el momento, y necesite decidir los límites de esa generación (qué puede variar, qué debe
  mantenerse consistente con el sistema de diseño).
---

# Generative UI

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Diseña interfaces donde la IA no solo responde con texto, sino que genera un componente
visual en el momento (una gráfica ajustada a la pregunta, una tarjeta resumen, un
formulario). El reto central: decidir qué puede variar libremente y qué debe respetar
siempre el sistema de diseño existente (`create-component`, `tokenize`), para que lo
generado no rompa la consistencia visual del producto.

## Cuándo se activa

Isabel diseña una función donde la IA construye un componente visual dinámicamente en vez
de solo texto, y necesita definir los límites de esa generación antes de que se implemente.
