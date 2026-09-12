---
name: write-rationale
description: >-
  Escribe el razonamiento por escrito detrás de una decisión ya tomada, conectándola
  explícitamente a necesidades de usuario, objetivos de negocio y principios de diseño.
  Úsala al cerrar una decisión importante (de cualquier skill anterior: un ⚠️ resuelto, una
  prioridad elegida, un trade-off aceptado) para que quede registrada y recuperable
  después, en vez de vivir solo en la memoria de quien participó en la conversación.
---

# Write Rationale — el criterio que sobrevive después de la conversación

> Fuente: [Owl-Listener/designer-skills — designer-toolkit](https://github.com/Owl-Listener/designer-skills)

Escribe por qué se tomó una decisión, conectándola a tres cosas: **necesidad de usuario**,
**objetivo de negocio**, y **principio de diseño aplicado**. Es para defender una decisión
por escrito — si hace falta una conversación en vivo defendiendo una postura, esa es otra
skill (`design-negotiation`, no cubierta aquí).

Es la pieza que cierra el círculo de todo el resto de skills: cada vez que una skill
anterior generó un ⚠️, una prioridad, o un trade-off aceptado, esa decisión vivía solo en
la conversación del momento. `write-rationale` la convierte en algo recuperable después —
dentro de meses, cuando alguien pregunte "¿por qué está hecho así?", la respuesta está
escrita, no depende de la memoria de nadie.

## Cuándo se activa

Isabel cierra una decisión importante y quiere dejar constancia escrita de por qué se
tomó, especialmente si viene de un ⚠️ resuelto en otra skill, una priorización, o un
trade-off aceptado conscientemente. También si pide explícitamente `/write-rationale
[decisión]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Qué motivó la decisión — una limitación técnica, una priorización, algo que salió en
  otra skill (pre-mortem, una reunión resumida)?

**2. Construye el rationale conectando la decisión a:**
- **Necesidad de usuario** — de dónde sale, si existe un job story o hallazgo previo
  relacionado.
- **Objetivo de negocio** — qué se prioriza con esta decisión y por qué.
- **Principio aplicado** — la regla general que justifica la elección, no solo el caso
  puntual.
- **Trade-off aceptado** — qué se sacrifica conscientemente al decidir esto.

**3. Enlaza, si existen, los artefactos previos de otras skills** (PRD, pre-mortem,
resumen de reunión) en vez de repetir su contenido — el rationale conecta, no duplica.

## Ejemplo

**Isabel escribe:**
> `/write-rationale` por qué decidimos no incluir normalización de periodos en la primera
> versión de comparación de campañas

**Preguntas antes de construir:**
> Antes de redactar el rationale, dime: ¿qué te hizo decidir eso — fue una limitación
> técnica, una decisión de priorización, o algo que salió en el pre-mortem?

**Isabel responde:**
> Fue priorización — salió en la reunión que resumimos, para no retrasar el lanzamiento
> del trimestre.

**Output final:**

> **Decisión:** la primera versión de comparación de campañas no normaliza periodos de
> fechas distintos.
>
> **Necesidad de usuario:** el equipo de marketing necesita decidir rápido qué campaña
> repetir (job story de `layers-user-needs`) — la normalización mejora precisión pero no
> es lo que más frena la decisión hoy.
>
> **Objetivo de negocio:** lanzar dentro del trimestre (decisión registrada en
> `summarize-meeting`) pesaba más que cubrir un caso de uso menos frecuente.
>
> **Principio aplicado:** "shippear lo que resuelve el 80% del caso real antes que
> bloquear por el 20% restante".
>
> **Trade-off aceptado:** quien compare campañas de duración muy distinta verá un aviso,
> no un resultado normalizado, hasta la fase 2.

**Recomendación final:**
> Guardar este rationale junto al PRD y al pre-mortem de esta feature — si alguien
> pregunta en 6 meses por qué no hay normalización, esta es la respuesta, sin depender de
> que alguien recuerde la reunión.
