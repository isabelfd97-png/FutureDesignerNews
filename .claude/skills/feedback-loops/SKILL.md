---
name: feedback-loops
description: >-
  Diseña cómo el usuario corrige o valora una respuesta de IA — pulgar arriba/abajo,
  edición inline, señales de refuerzo — y qué hace el sistema con esa señal. Úsala cuando
  Isabel diseñe un mecanismo de corrección o valoración de una respuesta de IA y necesite
  decidir tanto la interacción visible como qué pasa con esa señal después.
---

# Feedback Loops (IA)

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Diseña los mecanismos por los que un usuario corrige o valora lo que hace una IA —
pulgar arriba/abajo, editar directamente una respuesta generada, aceptar o rechazar una
sugerencia — y qué pasa con esa señal después (¿se usa para mejorar futuras respuestas,
o desaparece sin más?). Una señal de feedback sin ningún efecto visible entrena al usuario
a dejar de darla.

## Cuándo se activa

Isabel diseña un mecanismo de corrección o valoración de respuestas de IA y necesita
decidir tanto la interacción (cómo se ve/usa) como el efecto real de esa señal, para que no
sea un gesto vacío.
