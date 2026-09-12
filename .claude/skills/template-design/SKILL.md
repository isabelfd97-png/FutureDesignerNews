---
name: template-design
description: >-
  Diseña plantillas de prompt reutilizables y parametrizadas para producir salidas
  consistentes cada vez que se usan, en vez de reescribir el prompt desde cero para cada
  caso similar. Úsala cuando Isabel tenga una función de IA que se repite con variaciones
  pequeñas (mismo tipo de tarea, distintos datos de entrada) y quiera un prompt reutilizable
  en vez de uno hecho a medida cada vez.
---

# Template Design (prompts)

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Diseña plantillas de prompt con parámetros claros (lo que cambia de un uso a otro) separados
de la estructura fija (lo que siempre debe estar), para que la salida sea consistente cada
vez sin tener que reescribir el prompt entero para cada caso parecido.

## Cuándo se activa

Isabel tiene una función de IA que se repite con variaciones pequeñas (ej. generar un
resumen de campaña distinto cada vez, pero con la misma estructura) y quiere una plantilla
reutilizable. Se combina con `prompt-versioning` cuando la plantilla necesita iterarse con
el tiempo.
