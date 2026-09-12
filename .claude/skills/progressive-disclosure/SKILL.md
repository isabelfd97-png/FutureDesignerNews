---
name: progressive-disclosure
description: >-
  Diseña cómo se revela gradualmente la capacidad de una IA, para que coincida con lo que
  el usuario espera que sepa hacer en cada momento, en vez de explicar todo de golpe la
  primera vez. Úsala cuando Isabel introduzca una función de IA nueva y quiera decidir
  cuánto mostrar al principio y cuánto dejar que se descubra con el uso.
---

# Progressive Disclosure (IA)

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Aplica el principio clásico de "revelación progresiva" al contexto específico de
capacidades de IA: no listar todo lo que la IA sabe hacer en el primer mensaje, sino
revelarlo gradualmente, en el momento en que sea relevante — evita abrumar y evita también
que el usuario subestime lo que la IA puede hacer si nunca se lo cuenta.

## Cuándo se activa

Isabel introduce una función de IA nueva y necesita decidir qué mostrar en el primer
contacto y qué dejar para más adelante. Se combina con `mixed-initiative-flow` para decidir
si esa revelación la inicia la IA o se descubre solo cuando el usuario pregunta.
