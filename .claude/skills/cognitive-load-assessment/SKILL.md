---
name: cognitive-load-assessment
description: >-
  Evalúa un flujo desde el punto de vista de carga cognitiva — demandas de memoria,
  atención/decisiones, complejidad de decisión — distinguiendo la complejidad inevitable
  de la tarea (carga intrínseca) de la fricción añadida por el propio diseño (carga
  extrínseca). Úsala sobre un flujo ya mapeado (`layers-interaction-flow`) cuando Isabel
  quiera detectar esfuerzo mental innecesario, especialmente si lo usan personas con prisa,
  estrés o cansancio — el tipo de complejidad que no aparece en un heatmap pero mata la
  finalización de la tarea.
---

# Cognitive Load Assessment — carga mental, no solo visual

> Fuente: [owl-listener/inclusive-design-skills — cognitive-accessibility](https://github.com/owl-listener/inclusive-design-skills/tree/main/cognitive-accessibility)

Evalúa cuánto esfuerzo mental pide un flujo, no si es visualmente atractivo o
técnicamente correcto. Distingue:

- **Carga intrínseca** — complejidad inevitable dada la propia tarea (comparar dos series
  de datos siempre exige procesar dos cosas a la vez; eso no desaparece).
- **Carga extrínseca** — fricción añadida por el diseño, no por la tarea (nombres
  confusos, pasos innecesarios, tener que recordar algo de una pantalla anterior).

El objetivo es minimizar la extrínseca sin fingir que la intrínseca desaparece.

## Las tres dimensiones

1. **Memoria** — cuántas cosas debe recordar el usuario de un paso a otro (óptimo: ninguna
   o 1-2).
2. **Atención** — cuántas decisiones toma y cuántos conceptos nuevos aprende (óptimo: 0-3
   decisiones, 0-1 concepto nuevo).
3. **Complejidad de decisión** — pasos, densidad visual, claridad del lenguaje.

Cualquier dimensión marcada 🔴 Alta es señal de que hace falta rediseñar esa parte.

## Cuándo se activa

Isabel tiene un flujo ya mapeado (idealmente con `layers-interaction-flow`) y quiere
detectar esfuerzo mental innecesario, especialmente si lo usa gente con prisa, estrés o
cansancio (un contexto de uso real muy común y fácil de olvidar al diseñar con calma).
También si pide explícitamente `/cognitive-load-assessment [flujo]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿En qué estado suele estar quien usa este flujo — con prisa, tranquilo, bajo estrés?
- ¿Hay algo del flujo que ya se sospeche que pide demasiado esfuerzo mental?

**2. Recorre el flujo pantalla por pantalla** como si fueras un usuario cansado y poco
familiarizado (no el usuario experto que lo diseñó), contando demandas cognitivas en cada
paso.

**3. Construye una tabla pantalla por pantalla** con las tres dimensiones puntuadas
(✅ bajo / ⚠️ límite / 🔴 alto), y para cada 🔴 o ⚠️, indica si la carga es intrínseca
(inevitable) o extrínseca (evitable con mejor diseño).

**4. Termina con recomendaciones priorizadas por impacto**, dando preferencia a técnicas
concretas: divulgación progresiva, valores por defecto inteligentes, agrupar información
(chunking) — nunca solo "simplificar" sin decir cómo.

## Ejemplo

**Isabel escribe:**
> `/cognitive-load-assessment` el flujo de comparar dos campañas que ya mapeamos con
> layers-interaction-flow

**Preguntas antes de construir:**
> Antes de evaluar, dime:
> - ¿Este flujo lo usa gente con prisa/estresada habitualmente (ej. antes de una
>   reunión), o con tiempo tranquilo?
> - ¿Hay algo del flujo que ya sospeches que pide demasiado esfuerzo mental?

**Isabel responde:**
> Normalmente se usa con prisa, antes de reuniones de resultados. No he pensado en
> esfuerzo mental específicamente.

**Output final** (recorriendo el flujo como alguien cansado/con prisa):

| Pantalla | Memoria | Atención | Decisión |
|---|---|---|---|
| Lista de campañas | Ninguna ✅ | 1 decisión (elegir 2) ✅ | Bajo ✅ |
| Vista de comparación | 🔴 Alta — debe recordar qué campaña era "la buena" de la semana pasada para decidir si repetir | 3 decisiones (repetir, descartar, comparar otra) ⚠️ Límite | Medio ⚠️ |

**Recomendación priorizada:**
> 1. 🔴 Prioridad alta: la demanda de memoria en Vista de comparación es carga
>    *extrínseca* evitable — mostrar directamente el resultado de la campaña anterior al
>    lado, en vez de exigir que el usuario lo recuerde de memoria.
> 2. ⚠️ Menor: las 3 decisiones en Vista de comparación están en el límite aceptable — no
>    urgente, pero vigilar si se añaden más opciones en el futuro.
