---
name: design-prompt
description: >-
  Crea un system prompt estructurado para una función de IA, combinando rol, contexto,
  restricciones y formato (`system-prompt-structure`). Úsala cuando Isabel vaya a
  especificar el prompt detrás de una función de IA nueva, de principio a fin, en vez de
  escribirlo de forma improvisada.
---

# Design Prompt — crear un system prompt estructurado

> Parte del plugin [`prompt-architecture`](../../plugins/prompt-architecture.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Comando principal del plugin para construir un system prompt desde cero, combinando las
partes de `system-prompt-structure` con restricciones (`constraint-specification`) y
ejemplos (`few-shot-patterns`) cuando hagan falta.

## Cuándo se activa

Isabel va a especificar el prompt detrás de una función de IA nueva y quiere construirlo
con estructura, no de forma improvisada. También si pide explícitamente
`/design-prompt [función de IA]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Qué debe hacer exactamente esta función de IA, y qué NO debe hacer bajo ningún
  concepto?
- ¿Hay un formato de salida específico que deba respetar siempre (JSON, un tono concreto,
  una longitud máxima)?

**2. Construye el prompt en las cuatro partes**: rol, contexto, restricciones, formato.

**3. Si el resultado esperado es difícil de describir solo con instrucciones, añade 1-2
ejemplos concretos (few-shot)** en vez de alargar las instrucciones en prosa.

**4. Marca con ⚠️ cualquier restricción crítica que dependa de que el modelo la respete
siempre** (ej. "nunca inventar un dato que no esté en el contexto") — estas merecen
verificarse con pruebas reales, no solo confiar en que el prompt lo garantiza.

## Ejemplo

**Isabel escribe:**
> `/design-prompt` un asistente que resume por qué una campaña de marketing tuvo el
> rendimiento que tuvo, a partir de los datos de la campaña

**Preguntas antes de construir:**
> Antes del prompt, dime:
> - ¿Qué NO debe hacer bajo ningún concepto? (ej. ¿puede especular sobre causas que no
>   están en los datos?)
> - ¿Hay un formato de salida fijo (longitud, estructura)?

**Isabel responde:**
> No debe inventar causas que no estén respaldadas por los datos. Máximo 3 frases, sin
> jerga técnica.

**Output final:**

> **Rol:** Eres un asistente que resume el rendimiento de campañas de marketing para
> personas sin formación técnica en analítica.
>
> **Contexto:** Recibirás los datos de la campaña (métricas, fechas, canal) como entrada.
>
> **Restricciones:**
> - Nunca menciones una causa que no esté respaldada explícitamente por los datos
>   recibidos. Si no hay datos suficientes para explicar el resultado, dilo directamente
>   en vez de especular.
> - Sin jerga técnica (nada de "CTR", "ROI ajustado" sin explicar).
> - Máximo 3 frases.
>
> **Formato:** texto plano, sin listas ni markdown.
>
> ⚠️ **Verificar con pruebas reales:** la restricción de "no inventar causas" es crítica —
> conviene probarla con casos límite (datos ambiguos o incompletos) antes de confiar en
> que el modelo la respeta siempre.

**Recomendación final:**
> Probar el prompt con al menos un caso de datos ambiguos antes de lanzarlo — es el
> escenario donde más fácilmente un modelo "rellena" con una causa inventada si no está
> bien restringido.
