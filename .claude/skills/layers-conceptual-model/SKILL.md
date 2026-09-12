---
name: layers-conceptual-model
description: >-
  Define por escrito, independientemente de cualquier interfaz, los objetos, relaciones,
  estados y vocabulario de un producto o feature — la Capa 3 de `layers-orient`, pero
  construida en detalle en vez de solo diagnosticada. Úsala antes de diseñar una pantalla
  nueva, cuando Isabel vaya a crear algo desde cero, o cuando un equipo mire la misma
  pantalla y no esté de acuerdo en qué es exactamente lo que representa (el síntoma clásico
  de un modelo conceptual que nunca se puso por escrito).
---

# Layers Conceptual Model — el objeto, antes que la pantalla

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

Cuando `layers-orient` diagnostica que el problema está en la Capa 3 (modelo conceptual),
esta skill es la que se sienta a construirlo de verdad, en texto, antes de dibujar nada.
Jamie Mill la llama "la capa que más carga soporta": si dos personas de un equipo miran la
misma pantalla y no coinciden en qué es lo que representa, no hay un problema de diseño
visual — hay un modelo conceptual que nunca se escribió, y cada quien lo ha rellenado a su
manera en su cabeza.

## Qué define

- **Objetos** — qué "cosas" existen (una Campaña, una Métrica, un Segmento...).
- **Relaciones** — cómo se conectan entre sí (una Campaña *tiene* muchas Métricas).
- **Estados** — qué fases puede tener cada objeto (Borrador → Activa → Cerrada).
- **Vocabulario** — el nombre exacto y consistente de cada cosa, detectando cuando distintas
  personas del equipo usan palabras distintas para lo mismo.

## Cuándo se activa

Isabel va a diseñar una pantalla o feature nueva desde cero y quiere el modelo conceptual
resuelto antes de dibujar nada. También cuando ya hay una pantalla construida y surge
desacuerdo sobre qué representa exactamente (entre ella y su equipo, o incluso ella
consigo misma). También si pide explícitamente "hazme un `/layers-conceptual-model`".

## Cómo trabajar — mecánica exacta

No entregues el modelo directamente a partir del primer mensaje, aunque parezca sencillo.
Sigue siempre esta secuencia:

**1. Preguntas antes de construir.** Con lo mínimo que Isabel ha dado, pregunta:
   - Qué objetos hay en juego (no asumas que solo hay uno).
   - Cuáles de esos objetos tienen estados distintos y cuáles no.
   - Si hay alguna palabra que ella o su equipo usan de forma distinta para lo mismo.

**2. Recoge la respuesta tal cual venga**, aunque sea incompleta o insegura ("no sé",
   "supongo que") — no hace falta que Isabel tenga el modelo claro de antemano, para eso
   está la skill.

**3. Devuelve el modelo construido**, en un documento corto (objetos / relaciones / estados
   / vocabulario), y **marca explícitamente con ⚠️** cualquier hueco, contradicción, o
   decisión que Isabel no haya cerrado — no la rellenes tú por tu cuenta ni la dejes
   implícita.

**4. Termina con una recomendación concreta** de qué ⚠️ conviene cerrar con su equipo antes
   de diseñar, explicando brevemente por qué (qué se rompería o habría que rehacer si se
   diseña sin resolverlo primero).

## Ejemplo

**Isabel escribe:**
> `/layers-conceptual-model` voy a montar una pantalla nueva de campañas

**Preguntas antes de construir:**
> Antes de pantallas, vamos a dejar claro el modelo por escrito. Unas preguntas rápidas:
> 1. ¿Qué "cosas" (objetos) hay en esta pantalla? Por ejemplo: ¿solo "Campaña", o también
>    "Métrica", "Segmento de usuarios", "Canal"?
> 2. De esas cosas, ¿cuáles pueden tener distintos estados (borrador, activa, cerrada...) y
>    cuáles no?
> 3. ¿Hay alguna palabra que uses tú, o tu equipo, de forma distinta para lo mismo? (ej:
>    "campaña" vs "iniciativa")

**Isabel responde:**
> Objetos: campaña y métricas de uso. Estados no sé, supongo que activa/cerrada.
> Vocabulario no sé si hay lío, pero marketing a veces dice "iniciativa"

**Output final:**

> **Modelo conceptual — Campañas**
>
> **Objetos**
> - Campaña — acción de marketing con fecha inicio/fin
> - Métrica — valor medido (uso) asociado a una Campaña en un momento dado
>
> **Relaciones**
> - Una Campaña *tiene* muchas Métricas (una por día)
>
> **Estados de Campaña**
> - Activa → Cerrada
> - ⚠️ Pregunta abierta: ¿existe un estado "Archivada" o "Pausada"? No se mencionó, pero si
>   existe, hay que decidir ahora si es comparable con otras campañas o no.
>
> **Vocabulario**
> - ⚠️ Conflicto detectado: marketing a veces usa "iniciativa" para lo mismo que
>   "campaña". Decisión pendiente: ¿se unifica en un solo término para este dashboard, o
>   debe soportar que la gente busque por ambos nombres?

**Recomendación final:**
> Antes de diseñar la pantalla, conviene cerrar esas dos ⚠️ con el equipo (aunque sea una
> pregunta rápida) — si se diseña ya y la respuesta cambia el modelo después, hay que
> rehacer parte de la pantalla.

El output nunca es una pantalla ni un mockup — es siempre este documento corto de texto,
con las dudas marcadas explícitamente, para resolverlas antes de que se diseñe nada visual.
