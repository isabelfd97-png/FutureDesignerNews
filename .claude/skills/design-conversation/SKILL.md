---
name: design-conversation
description: >-
  Diseña un flujo de conversación humano-IA completo, combinando turn-taking, iniciativa
  mixta, revelación progresiva de capacidad y manejo de errores. Úsala cuando Isabel vaya a
  diseñar una función de IA conversacional (un asistente, un chat) de principio a fin, en
  vez de diseñar cada parte suelta sin conexión entre sí.
---

# Design Conversation — flujo de conversación humano-IA completo

> Parte del plugin [`model-interaction-design`](../../plugins/model-interaction-design.md) — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)

Comando principal del plugin: combina `conversation-patterns`, `mixed-initiative-flow` y
`progressive-disclosure` para diseñar una interacción de IA completa, de principio a fin,
en vez de decidir cada pieza por separado sin conexión.

## Cuándo se activa

Isabel va a diseñar una función de IA conversacional nueva (un asistente, un chat, una
función que responde en lenguaje natural) y quiere el flujo completo — quién inicia, cómo
se revela la capacidad, qué pasa ante un malentendido. También si pide explícitamente
`/design-conversation [función a diseñar]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿La IA debería ser reactiva (espera a que el usuario pida algo) o proactiva (propone sin
  que se lo pidan)?
- ¿Qué tan familiarizado está el usuario típico con este tipo de función de IA?

**2. Diseña el arranque de la conversación** (iniciativa: quién habla primero y con qué
tono).

**3. Diseña cuánta capacidad se revela al principio** vs. lo que se descubre con el uso.

**4. Diseña qué pasa ante un malentendido** — la secuencia de reparación explícita, no un
reintento silencioso.

**5. Marca con ⚠️ cualquier decisión de diseño que dependa de tecnología o restricciones
que Isabel no haya confirmado** (ej. si el sistema puede de verdad detectar que hubo un
malentendido, o si eso requiere trabajo de ingeniería adicional).

## Ejemplo

**Isabel escribe:**
> `/design-conversation` un asistente dentro del dashboard que ayuda a decidir qué
> campaña repetir

**Preguntas antes de construir:**
> Antes del diseño completo, dime:
> - ¿Debería el asistente proponer proactivamente cuando detecta que una campaña acaba de
>   cerrar, o esperar a que el usuario le pregunte?
> - ¿El usuario típico ya ha usado asistentes de IA en otras herramientas, o sería su
>   primera vez?

**Isabel responde:**
> Debería proponer proactivamente cuando cierra una campaña. Es su primera vez con un
> asistente así en herramientas de trabajo, en general.

**Output final:**

> **Iniciativa (arranque):** el asistente inicia proactivamente ("veo que la Campaña X
> terminó ayer, ¿quieres que la compare con la anterior?") en vez de esperar pasivo.
>
> **Revelación progresiva:** en el primer uso, mencionar solo la capacidad concreta que
> disparó la propuesta ("puedo comparar campañas"), no listar todo lo que el asistente
> sabe hacer de golpe — dado que es la primera vez del usuario con este tipo de función,
> abrumar con capacidades reduce la confianza en vez de aumentarla.
>
> **Manejo de malentendido:** si el usuario dice "no, me refería a otra campaña", el
> asistente reconoce explícitamente ("ah, perdona, ¿te refieres a la Campaña Y?") antes de
> reintentar — nunca vuelve a proponer sin reconocer el error.
>
> ⚠️ **Sin confirmar:** si el sistema puede detectar automáticamente que una campaña
> "acaba de cerrar" para disparar la propuesta proactiva, o si eso requiere una
> integración que aún no existe.

**Recomendación final:**
> Confirmar con ingeniería la viabilidad de la detección automática (el ⚠️) antes de
> comprometer el diseño proactivo — si no es viable a corto plazo, el diseño debería
> arrancar en modo reactivo como primera versión.
