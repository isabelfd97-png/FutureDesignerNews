---
name: constraint-specification
description: >-
  Define formato de salida, longitud, tono y límites de contenido dentro de un prompt, para
  que la IA no se salga de lo esperado. Úsala cuando una función de IA produzca respuestas
  demasiado largas, con un tono inconsistente, o que a veces incluyen contenido que no
  debería, y haga falta fijar límites explícitos en vez de confiar en que "se comporte
  bien" por defecto.
---

# Constraint Specification

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Define los límites explícitos que un prompt debe imponer: formato de salida esperado,
longitud máxima/mínima, tono, y qué tipo de contenido queda fuera de los límites. Sin
restricciones explícitas, la IA puede comportarse de forma razonable la mayoría de las
veces y salirse del patrón esperado en casos concretos — las restricciones reducen esa
variabilidad.

## Cuándo se activa

Una función de IA produce respuestas inconsistentes en formato, longitud o tono, y hace
falta fijar límites explícitos en el prompt en vez de depender del comportamiento por
defecto.
