---
name: audit-interaction
description: >-
  Evalúa una interacción de IA ya existente contra las taxonomías de las 8 skills base del
  plugin (turn-taking, iniciativa, revelación progresiva, multimodalidad, memoria,
  UI generativa, feedback, frustración). Úsala cuando Isabel tenga una función de IA ya
  construida (propia o de un competidor) y quiera auditarla con criterio estructurado, en
  vez de una impresión general de "se siente rara".
---

# Audit Interaction — auditoría de una interacción de IA ya existente

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Evalúa una interacción de IA real (propia o de un competidor, como en `benchmark`) contra
las 8 dimensiones del plugin, para pasar de "esto se siente raro" a un diagnóstico
concreto de qué dimensión falla y por qué.

## Cuándo se activa

Isabel tiene una interacción de IA ya construida y quiere auditarla con criterio
estructurado. También si pide explícitamente `/audit-interaction [interacción a evaluar]`.
Necesita material real (capturas, transcripción de uso, o acceso a probarlo) — igual que
`benchmark` y `evaluate`, no evalúa una idea abstracta.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Es una interacción propia o de un competidor?
- ¿Hay algo que ya sospeches que falla (se siente lenta, repite errores, abruma con
  información)?

**2. Revisa el material contra las 8 dimensiones**, marcando cada una con ✅ / ⚠️ / 🔴 y
describiendo el problema concreto detectado, no una impresión vaga.

**3. Termina priorizando qué dimensión resolver primero**, explicando el impacto real si
no se corrige.

## Ejemplo

**Isabel escribe:**
> `/audit-interaction` el asistente de campañas que ya está en producción, aquí tienes una
> grabación de uso: [pega/describe]

**Preguntas antes de construir:**
> Antes de auditar, dime:
> - ¿Hay algo que ya sospeches que falla?

**Isabel responde:**
> Cuando el usuario corrige algo, siento que el asistente no reconoce el error, solo
> vuelve a intentarlo.

**Output final:**

> - **conversation-patterns** 🔴 — confirmado: ante una corrección, el asistente reintenta
>   sin reconocer el malentemdido explícitamente. Rompe la confianza del usuario en que fue
>   entendido.
> - **mixed-initiative-flow** ✅ — el asistente cede el control de forma clara tras cada
>   propuesta.
> - **progressive-disclosure** ⚠️ — en la primera interacción, lista 5 capacidades de
>   golpe en vez de revelar solo la relevante al momento.
> - **frustration-detection** 🔴 — no hay ninguna señal implementada; si el usuario repite
>   la misma corrección 2-3 veces, el sistema no lo detecta ni ofrece alternativa.

**Recomendación final:**
> Priorizar `conversation-patterns` (reconocer el error explícitamente) — es lo que más
> directamente rompe la confianza y es relativamente barato de arreglar frente a construir
> detección de frustración desde cero.
