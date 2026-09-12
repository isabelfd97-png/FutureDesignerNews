---
name: multimodal-orchestration
description: >-
  Coordina texto, imagen, voz y uso de herramientas dentro de una misma interacción con IA,
  decidiendo qué modalidad usar en cada momento y cómo se combinan sin confundir al
  usuario. Úsala cuando una función de IA combine más de un tipo de entrada/salida (texto +
  imagen, texto + acción sobre una herramienta) y haga falta decidir el orden y la
  transición entre ellas.
---

# Multimodal Orchestration

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Decide cómo se coordinan distintas modalidades (texto, imagen, voz, ejecución de una
herramienta) dentro de una misma interacción — por ejemplo, cuándo la IA debería mostrar
una gráfica generada en vez de describirla en texto, o cuándo debería confirmar en texto
antes de ejecutar una acción real.

## Cuándo se activa

Isabel diseña una función de IA que combina más de un tipo de entrada o salida y necesita
decidir el orden, la transición entre modalidades, y quién elige qué modalidad usar en cada
momento (la IA por defecto, o el usuario explícitamente).
