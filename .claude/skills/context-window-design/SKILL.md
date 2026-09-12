---
name: context-window-design
description: >-
  Diseña cómo se comporta una interacción con IA en torno a los límites de memoria y
  contexto — qué se recuerda de una sesión a otra, qué se olvida, y cómo se comunica al
  usuario cuando algo se ha perdido. Úsala cuando Isabel diseñe una función de IA con
  memoria persistente o conversaciones largas, y necesite decidir qué pasa cuando se supera
  el límite.
---

# Context Window Design

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Diseña el comportamiento de una IA en torno a los límites de token/memoria: qué información
persiste entre sesiones, qué se pierde, y sobre todo, **cómo se comunica al usuario** que
algo se ha olvidado — en vez de que la IA finja recordar algo que ya no tiene, o el usuario
descubra la pérdida de memoria de forma confusa a mitad de conversación.

## Cuándo se activa

Isabel diseña una función de IA con conversaciones largas o memoria entre sesiones, y
necesita decidir qué pasa cuando se supera el límite de contexto — silencio, aviso
explícito, o resumen de lo que se mantiene.
