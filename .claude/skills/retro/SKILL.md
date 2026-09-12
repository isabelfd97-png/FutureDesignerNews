---
name: retro
description: >-
  Facilita una retrospectiva de sprint estructurada, con tres formatos a elegir
  (Start/Stop/Continue, 4Ls, Sailboat), preguntas concretas sobre cumplimiento del
  objetivo y bloqueos, y siempre cierra con 2-3 acciones con responsable, plazo y forma de
  medir el cumplimiento — además de hacer seguimiento de si las acciones de la retro
  anterior se cumplieron. Úsala al final de un sprint o ciclo de trabajo para evitar que la
  retrospectiva se quede en opiniones sueltas sin ninguna acción real después.
---

# Retro — retrospectiva de sprint estructurada

> Fuente: [phuryn/pm-skills — pm-execution](https://github.com/phuryn/pm-skills)

Facilita una retrospectiva evitando el problema más común: que se disuelva en opiniones
sueltas ("fue un sprint duro", "en general bien") sin ninguna acción concreta después.
Siempre cierra con acciones asignadas, con plazo y forma de medir el cumplimiento.

## Los tres formatos

- **Start/Stop/Continue** — qué empezar a hacer, qué dejar de hacer, qué mantener.
- **4Ls** — Liked/Learned/Lacked/Longed for (qué gustó, qué se aprendió, qué faltó, qué se
  echó en falta).
- **Sailboat** — metáfora náutica: Viento (lo que empuja), Ancla (lo que frena), Rocas
  (riesgos), Isla (el objetivo).

## Preguntas que estructura la sesión

- ¿Se cumplió el objetivo del sprint?
- ¿Velocidad vs. compromiso — se hizo lo que se planeó?
- ¿Qué bloqueos aparecieron y cómo se resolvieron?
- ¿Cómo fue la colaboración del equipo?

## Cuándo se activa

Isabel (o su equipo) termina un sprint o ciclo de trabajo y quiere una retrospectiva
estructurada, no una conversación abierta sin rumbo. También si pide explícitamente
`/retro [sprint, formato opcional]`.

Se empareja con un resumidor de reuniones para transcribir la sesión en vivo si hace falta
(otra skill, no cubierta aquí todavía).

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Se cumplió el objetivo del sprint?
- ¿Hay alguna acción pendiente de la retro anterior que revisar primero, o es la primera
  retrospectiva?

**2. Si hay retro anterior, revisa primero el estado de sus acciones** — cumplidas, a
medias, o abandonadas — antes de generar contenido nuevo.

**3. Estructura el contenido en el formato elegido** (Start/Stop/Continue por defecto si
no se especifica otro), usando lo que Isabel aporte y, si existen, hallazgos de
`pre-mortem` u otras skills relacionadas con el sprint.

**4. Cierra siempre con 2-3 acciones concretas**, cada una con responsable, plazo, y cómo
se sabrá si se cumplió — nunca una lista de buenas intenciones sin dueño ni fecha.

## Ejemplo

**Isabel escribe:**
> `/retro` sprint de la feature de comparación de campañas, formato Start/Stop/Continue

**Preguntas antes de construir:**
> Antes de la retro, dime:
> - ¿Se cumplió el objetivo del sprint (lanzar la comparación)?
> - ¿Hay alguna acción pendiente de la retro anterior que debamos revisar primero?

**Isabel responde:**
> Se cumplió, aunque con un retraso de 2 días por la suposición de formato de datos que
> salió mal en el pre-mortem. No hay retro anterior, es la primera.

**Output final:**

> **Start:** confirmar suposiciones técnicas críticas (como la de formato de datos) con
> ingeniería antes de escribir el PRD final, no después.
> **Stop:** dejar suposiciones marcadas con ⚠️ sin resolver hasta que ya se está
> construyendo.
> **Continue:** el uso de `pre-mortem` antes del sprint — ayudó a detectar el riesgo,
> aunque no a tiempo de evitarlo del todo esta vez.
>
> **Acciones concretas:**
> 1. Confirmar suposiciones técnicas marcadas con ⚠️ en el PRD dentro de las primeras 48h
>    del sprint, no al final — responsable: Isabel + ingeniería, antes del próximo sprint.
> 2. Añadir un paso de "check técnico rápido" al proceso de `write-prd` para este tipo de
>    suposición — responsable: Isabel, revisar en la siguiente retro.
