---
name: test-plan
description: >-
  Diseña un plan de test de usabilidad completo — preguntas de investigación, criterios de
  reclutamiento, tareas orientadas a objetivo (no dirigidas), criterio de éxito definido de
  antemano, y guía de facilitación. Úsala como alternativa cualitativa cuando `experiment`
  detecta que no hay tráfico suficiente para un A/B, o siempre que Isabel quiera testear
  con usuarios reales sin caer en los dos errores más comunes: tareas que regalan la
  respuesta, y criterio de éxito vago decidido a posteriori.
---

# Test Plan — plan de test de usabilidad completo

> Fuente: [Owl-Listener/designer-skills — design-research](https://github.com/Owl-Listener/designer-skills/tree/main/design-research)
> (invocada originalmente como `/design-research:test-plan`)

La mayoría de tests de usabilidad fallan en el **plan**, no en la ejecución — sobre todo por
dos errores clásicos:

1. **Tareas dirigidas** ("haz clic aquí para comparar") en vez de orientadas a objetivo
   ("decide si repetirías esta campaña") — la primera no dice si la persona habría
   encontrado el camino sola.
2. **Criterio de éxito vago** ("si lo completó bien"), decidido a ojo después de ver la
   sesión, en vez de definido antes de empezar.

Esta skill construye el plan completo evitando ambos.

## Qué incluye

- **Preguntas de investigación** — qué se quiere aprender, específico, no "a ver qué
  opinan".
- **Criterios de reclutamiento** — quién debe participar, y explícitamente quién NO (para
  no sesgar con gente que no representa al usuario real, o que ya conoce la feature).
- **Tareas** — siempre orientadas a objetivo, nunca dirigidas paso a paso.
- **Criterio de éxito** — definido antes de la sesión, en niveles (éxito / éxito con
  fricción / fallo), no decidido después viendo qué pasó.
- **Guía de facilitación** — qué decir y qué no decir mientras se observa (nunca rescatar a
  quien se atasca, eso es el dato).

## Cuándo se activa

Es la alternativa natural cuando `experiment` (A/B) detecta que no hay tráfico suficiente
para un resultado fiable. También cuando Isabel quiere testear algo con usuarios reales de
forma cualitativa, independientemente de si antes se descartó un A/B. También si pide
explícitamente `/test-plan [qué testear]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cuántas personas se pueden reclutar realistamente, y de qué perfil (ya usan el
  producto, o vale gente nueva)?
- ¿Qué preocupa más — que no encuentren cómo hacer algo, o que lo hagan pero interpreten
  mal el resultado?

**2. Construye la pregunta de investigación** específica a esa preocupación.

**3. Define los criterios de reclutamiento**, marcando con ⚠️ a quién excluir si podría
sesgar el resultado (quien ya vio la feature en una demo, por ejemplo).

**4. Redacta la tarea en formato orientado a objetivo**, nunca dando pistas de dónde
hacer clic o qué botón usar.

**5. Define el criterio de éxito en niveles, antes de la sesión**, no después.

**6. Añade la guía de facilitación**, dejando claro que no se rescata a quien se atasca —
el atasco es el dato.

**7. Si el número de participantes es bajo (menos de ~8), recuerda que no se buscan
porcentajes, se buscan patrones cualitativos repetidos.**

## Ejemplo

**Isabel escribe:**
> `/test-plan` quiero testear si la gente entiende cómo comparar dos campañas, ya que no
> tenemos tráfico suficiente para el A/B que planteamos

**Preguntas antes de construir:**
> Antes del plan, dime:
> - ¿Cuántas personas puedes reclutar realistamente, y de qué perfil (deben ya usar el
>   dashboard, o vale gente nueva)?
> - ¿Qué te preocupa más — que no encuentren cómo comparar, o que comparen pero
>   interpreten mal el resultado?

**Isabel responde:**
> Puedo conseguir 5 personas del equipo de marketing que ya usan el dashboard. Me
> preocupa sobre todo que no encuentren cómo comparar.

**Output final:**

> **Pregunta de investigación:** ¿pueden los usuarios encontrar y completar la
> comparación de dos campañas sin ayuda?
>
> **Criterios de reclutamiento:** 5 personas de marketing que ya usen el dashboard
> semanalmente. ⚠️ Excluir a quien ya haya visto la nueva feature en una demo — sesgaría
> el resultado de "encontrarlo sin ayuda".
>
> **Tarea (orientada a objetivo, no dirigida):** "Tienes dos campañas del mes pasado.
> Decide cuál repetirías el mes que viene." — nunca "haz clic en Comparar".
>
> **Criterio de éxito:**
> - ✅ Éxito: encuentra y usa la comparación sin pistas, en menos de 2 minutos
> - 🟡 Éxito con fricción: la encuentra pero tarda más de 2 minutos o duda visiblemente
> - 🔴 Fallo: no la encuentra, o la usa pero malinterpreta el resultado
>
> **Guía de facilitación:** no sugerir dónde hacer clic aunque la persona esté atascada
> más de 30 segundos — anotar el atasco como dato, no rescatarla.

**Recomendación final:**
> Con solo 5 personas, no buscar cifras (% de éxito) — buscar patrones cualitativos: si 3
> de 5 se atascan en el mismo punto, eso ya es señal suficiente para actuar, aunque no sea
> estadísticamente significativo.
