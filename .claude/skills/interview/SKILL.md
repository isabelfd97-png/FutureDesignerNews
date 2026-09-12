---
name: interview
description: >-
  Dos modos para entrevistas de usuario reales: Prep genera un guion con preguntas de
  sondeo JTBD antes de la entrevista; Summarize convierte la transcripción ya grabada en el
  job real que la persona intentaba resolver, señales de satisfacción/frustración, y
  acciones concretas para el equipo. Úsala antes de una entrevista (prep) y después de
  tenerla grabada (summarize) — la misma skill cubre ambos extremos del proceso.
---

# Interview — preparar y resumir entrevistas JTBD

> Fuente: [phuryn/pm-skills — pm-product-discovery](https://github.com/phuryn/pm-skills)

Dos modos que se usan en secuencia, antes y después de una entrevista real con un usuario.

## Diferencia con `layers-observed-behaviour`

Ambas extraen información de transcripciones, pero el output es distinto:
`layers-observed-behaviour` da job stories con confianza marcada (🟢🟡🔴), pensadas para
alimentar decisiones de producto. Esta da un resumen más orientado a PM — el job real,
señales de satisfacción/frustración, y una lista de acciones concretas para el equipo. Se
pueden usar ambas sobre la misma transcripción si hace falta un formato u otro según para
quién sea el resumen.

## Modo Prep

Genera el guion de la entrevista antes de tenerla, con preguntas de sondeo estilo JTBD:
enfocadas en descubrir qué intenta lograr la persona, qué situación disparó la necesidad, y
qué resultado busca. Prioriza preguntas de comportamiento pasado ("cuéntame la última vez
que...") sobre preguntas hipotéticas ("¿usarías...?") — la gente predice mal su propio
comportamiento futuro, pero recuerda razonablemente bien lo que hizo.

## Modo Summarize

Convierte la transcripción ya grabada en:
- **Job** — qué intentaba lograr realmente la persona.
- **Señales de satisfacción** — qué funciona bien en su proceso actual, si algo.
- **Señales de frustración** — dónde se atasca, qué le frustra, citado literalmente cuando
  sea posible.
- **Acciones** — qué debería priorizar el equipo a partir de esto.

## Cuándo se activa

**Prep:** Isabel va a hacer una entrevista real y necesita el guion antes.
**Summarize:** Isabel ya tiene una transcripción o notas de una entrevista hecha y quiere
extraer lo accionable.

También si pide explícitamente `/interview prep [contexto]` o
`/interview summarize [transcripción]`.

## Cómo trabajar — mecánica exacta

**Modo Prep:**
1. Pregunta qué se sabe ya de la persona a entrevistar (rol, experiencia) para ajustar el
   nivel de las preguntas.
2. Genera preguntas de comportamiento pasado, nunca hipotéticas, orientadas a descubrir el
   job real detrás de la tarea que se quiere entender.

**Modo Summarize:**
1. Lee la transcripción completa, no un resumen previo.
2. Extrae el job, las señales de satisfacción/frustración (citando literalmente cuando se
   pueda), y las acciones concretas.
3. No inventes señales que no estén en el texto — si no hay ninguna señal positiva
   mencionada, dilo explícitamente en vez de inventar una neutra.

## Ejemplo — Modo Prep

**Isabel escribe:**
> `/interview prep` voy a entrevistar a alguien de marketing sobre cómo decide qué
> campaña repetir

**Pregunta antes de construir:**
> ¿Ya sabes algo de esta persona (rol exacto, cuánto lleva en el puesto), o entra a
> ciegas?

**Isabel responde:**
> Lleva 2 años en marketing, gestiona 5-6 campañas al mes.

**Output final:**
> - "Cuéntame la última vez que decidiste repetir o no una campaña — ¿qué pasó, paso a
>   paso?"
> - "¿Qué tenías que mirar o comparar para tomar esa decisión?"
> - "¿Qué hiciste cuando la información que necesitabas no estaba fácil de encontrar?"
> - "Si pudieras eliminar un paso de ese proceso mañana, ¿cuál sería?"

## Ejemplo — Modo Summarize

**Isabel escribe:**
> `/interview summarize` aquí está la transcripción: [pega texto]

**Output final:**
> **Job:** decidir rápido qué campaña repetir sin perder tiempo comparando manualmente.
> **Señales de satisfacción:** ninguna positiva mencionada sobre el proceso actual.
> **Señales de frustración:** "siempre acabo con la calculadora abierta a la vez que
> Excel" — frustración explícita con el proceso manual.
> **Acciones para el equipo:** priorizar la vista de comparación automática antes que
> cualquier otra mejora visual del dashboard.
