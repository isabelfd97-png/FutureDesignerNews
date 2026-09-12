---
name: cognitive-accessibility-review
description: >-
  Revisión completa de accesibilidad cognitiva combinando seis análisis: carga cognitiva,
  lenguaje claro, wayfinding/navegación, prevención y recuperación de errores, foco y
  atención, y carga de memoria. Evalúa si una persona cansada, con estrés y sin
  familiaridad previa puede completar la tarea sin ayuda — un listón más exigente que WCAG
  técnico. Úsala para una revisión completa de un flujo, combinando o ampliando lo que ya
  cubre `cognitive-load-assessment` en solitario.
---

# Cognitive Accessibility Review — el paraguas de las seis dimensiones

> Fuente: [owl-listener/inclusive-design-skills — cognitive-accessibility](https://github.com/owl-listener/inclusive-design-skills/tree/main/cognitive-accessibility)

Combina `cognitive-load-assessment` (que ya se tiene como skill independiente) con otros
cinco análisis, en una sola revisión completa:

1. **Carga cognitiva** — decisiones, memoria, conceptos nuevos, pasos, complejidad de
   lectura y visual.
2. **Lenguaje claro** — jerga, ambigüedad, claridad de las acciones.
3. **Wayfinding/navegación** — si el usuario entiende dónde está, qué opciones tiene, cómo
   volver atrás.
4. **Prevención y recuperación de errores** — se solapa con `error-flow`, pero aquí se
   evalúa si ya está bien resuelto, no se diseña desde cero.
5. **Foco y atención** — distracciones, elementos que compiten por la atención.
6. **Carga de memoria** — qué debe recordar el usuario entre pantallas o sesiones.

El listón real que evalúa: si una persona cansada, con estrés, y que nunca ha usado esto
antes, puede completar la tarea sin ayuda. Es más exigente que cumplir WCAG técnico
(contraste, lectores de pantalla) — aquí se trata de si el diseño funciona para un cerebro
que no está en su mejor momento.

## Cuándo se activa

Isabel quiere una revisión completa de un flujo en las seis dimensiones, no solo carga
cognitiva aislada. Si ya existe un `cognitive-load-assessment` hecho, se reutiliza en vez
de repetirlo desde cero. También si pide explícitamente
`/cognitive-accessibility:review [flujo]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cubre el flujo entero, o hay una pantalla concreta que preocupe más?
- ¿Ya existe un `cognitive-load-assessment` de esto, o se parte de cero en las 6
  dimensiones?

**2. Recorre las seis dimensiones por pantalla**, marcando severidad:
- 🔴 Critical — bloquea la tarea.
- 🟡 Major — fricción significativa, no bloquea del todo.
- ⚪ Minor — fricción menor.

**3. Construye:**
- Un **resumen ejecutivo** con valoración general y los 3 problemas principales.
- Una **tabla pantalla por pantalla** con severidad por dimensión.
- **Recomendaciones priorizadas** por impacto y esfuerzo de implementación.

**4. Si alguna dimensión ya está cubierta por otra skill** (ej. errores por `error-flow`,
carga cognitiva por `cognitive-load-assessment`), reutiliza esos hallazgos en vez de
reevaluar desde cero, y márcalo como tal en la tabla.

## Ejemplo

**Isabel escribe:**
> `/cognitive-accessibility:review` el flujo completo de comparación de campañas, de
> principio a fin

**Preguntas antes de construir:**
> Antes de la revisión completa, dime:
> - ¿Quieres que cubra todo el flujo entero, o alguna pantalla en concreto te preocupa
>   más?
> - ¿Hay ya un `cognitive-load-assessment` hecho de esto, o partimos de cero en las 6
>   dimensiones?

**Isabel responde:**
> Todo el flujo entero. Sí, ya tenemos el cognitive-load-assessment de antes.

**Output final:**

> **Resumen ejecutivo:** Valoración general — Media. 3 problemas principales: (1) demanda
> de memoria en Vista de comparación [ya detectado], (2) uso de jerga técnica sin explicar
> ("ROI ajustado", "CTR normalizado") en los tooltips, (3) sin indicación clara de "dónde
> estoy" al entrar desde un link externo directo a la comparación.
>
> | Pantalla | Carga cognitiva | Lenguaje | Wayfinding | Errores | Foco | Memoria |
> |---|---|---|---|---|---|---|
> | Vista de comparación | 🟡 Major (ya detectado) | 🔴 Critical — jerga sin explicar | 🟡 Major | ✅ (ya cubierto por error-flow) | ✅ | 🟡 Major |

**Recomendaciones priorizadas:**
> 1. 🔴 Critical: explicar o simplificar "ROI ajustado"/"CTR normalizado" — bloquea
>    comprensión para cualquiera que no maneje esos términos de memoria.
> 2. 🟡 Major: añadir indicador de ubicación cuando se llega por link directo, sin pasar
>    por Lista de campañas.
