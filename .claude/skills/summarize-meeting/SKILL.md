---
name: summarize-meeting
description: >-
  Convierte la transcripción bruta de una reunión en discusión, decisiones, acciones (con
  responsable y plazo, en tabla) y preguntas abiertas sin resolver. Úsala después de
  cualquier reunión de trabajo para que las decisiones queden registradas — lo que no se
  escribe tiende a desaparecer o a recordarse distinto por cada persona.
---

# Summarize Meeting — de transcripción a decisiones y acciones

> Fuente: [phuryn/pm-skills — pm-execution](https://github.com/phuryn/pm-skills)

Separa una transcripción bruta en categorías distintas, no un resumen genérico:

- **Discusión** — puntos generales que se hablaron.
- **Decisiones** — conclusiones concretas a las que se llegó.
- **Acciones** — tareas específicas, en tabla, con responsable y plazo.
- **Preguntas abiertas** — lo que quedó sin resolver, para que no se pierda.

El motivo real de usarla: una decisión que no se escribe en algún sitio tiende a
desaparecer o a recordarse de forma distinta por cada persona presente en la reunión.

## Cuándo se activa

Isabel tiene la transcripción o notas de una reunión de trabajo y quiere dejar registro
claro de qué se decidió, qué queda pendiente, y quién hace qué. También si pide
explícitamente `/summarize-meeting [transcripción]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Hay algo que ya se sepa que quedó sin resolver y convenga asegurarse de que no se
  pierda?

**2. Lee la transcripción completa**, no un resumen previo — separar decisión de discusión
requiere el texto real, no una versión ya condensada.

**3. Construye las cuatro secciones**: discusión (breve), decisiones (numeradas, concretas),
acciones (tabla con responsable y plazo), preguntas abiertas (marcadas explícitamente, no
omitidas por no tener respuesta clara).

**4. Si alguna "decisión" mencionada en la transcripción en realidad no se cerró del
todo, clasifícala como pregunta abierta, no como decisión** — no fuerces cierre donde no
lo hubo.

**5. Termina señalando qué pregunta abierta conviene cerrar antes de la siguiente
reunión, y por qué bloquea algo concreto.**

## Ejemplo

**Isabel escribe:**
> `/summarize-meeting` reunión de hoy sobre el lanzamiento de comparación de campañas —
> aquí la transcripción: [pega texto]

**Preguntas antes de construir:**
> Antes de resumir, ¿hay algo que ya sepas que quedó sin resolver y quieras asegurarte de
> que no se pierda?

**Isabel responde:**
> Sí, no llegamos a decidir si normalizamos periodos distintos en la primera versión o lo
> dejamos para después.

**Output final:**

> **Resumen:** se discutió el estado del PRD, el riesgo de formato de datos detectado en
> el pre-mortem, y el alcance de la primera versión.
>
> **Decisiones:**
> 1. La primera versión no incluirá normalización de periodos distintos — se confirma
>    como fase 2, tal como estaba en el PRD.
> 2. Se confirma la fecha de lanzamiento para el próximo trimestre.
>
> **Acciones:**
> | Tarea | Responsable | Plazo |
> |---|---|---|
> | Confirmar formato de datos con ingeniería | Isabel | Esta semana |
> | Documentar la exclusión de normalización en el PRD | PM | Antes del viernes |
>
> **Preguntas abiertas:**
> - ⚠️ No quedó claro si el checklist de QA (`handoff`) lo revisa Isabel o un QA dedicado
>   — mencionado pero no decidido.

**Recomendación final:**
> Cerrar la pregunta abierta del QA antes de la próxima reunión — es una decisión pequeña
> pero que bloquea saber quién ejecuta el checklist que ya tenéis diseñado.
