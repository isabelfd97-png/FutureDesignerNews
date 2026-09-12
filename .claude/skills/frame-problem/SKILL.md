---
name: frame-problem
description: >-
  Convierte un encargo ambiguo ("tenemos que rediseñar X") en un problem statement
  estructurado — quién se ve afectado, qué está pasando exactamente, por qué importa ahora,
  y cómo se sabría que está resuelto. Úsala cuando Isabel reciba (o proponga) un encargo
  vago que en realidad es una solución disfrazada de problema, antes de pasar a diseñar
  nada. Detecta si la petición original ya asume la solución sin haber confirmado cuál es
  el problema real.
---

# Frame Problem — de encargo ambiguo a problem statement

> Fuente: [Owl-Listener/designer-skills — ux-strategy](https://github.com/Owl-Listener/designer-skills)

"Tenemos que rediseñar el onboarding" no es un problema — es una tarea disfrazada de
problema. No dice para quién, qué está fallando exactamente, por qué importa ahora, ni cómo
se sabría que quedó resuelto. Esta skill fuerza a estructurar eso antes de que nadie se
ponga a diseñar.

## Qué cubre un problem statement bien formado

- **Quién** se ve afectado — un segmento concreto, no "los usuarios" en general.
- **Qué** está pasando exactamente — el síntoma observable, nunca la solución.
- **Por qué importa ahora** — impacto de negocio o de usuario, no solo "estaría mejor".
- **Cómo se sabría que está resuelto** — un criterio de éxito medible, no "que quede más
  bonito" o "que se sienta mejor".

## Cuándo se activa

Isabel recibe (o propone ella misma) un encargo vago tipo "rediseñar X", "mejorar Y", sin
que quede claro cuál es el problema real detrás. También si pide explícitamente
`/frame-problem [encargo]`.

Presta especial atención cuando el propio encargo **ya contiene una solución** ("rediseñar
el onboarding" ya asume que rediseñar es lo que hace falta) — esa es la señal más clara de
que hay que parar y reformular antes de aceptar el encargo tal cual viene.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Qué hace pensar que hay un problema — un dato concreto, una queja, o una intuición?
- ¿Para quién específicamente? (un segmento, no "todos")
- Si se arregla, ¿qué número o comportamiento debería cambiar para saber que funcionó?

**2. Construye el problem statement** con lo aportado, describiendo el síntoma observable
sin colar la solución dentro de la descripción del problema.

**3. Marca con ⚠️ si la petición original ya venía con una solución implícita** ("rediseñar"
en vez de "el 40% abandona") y explica qué información falta para saber si esa solución es
la correcta.

**4. Propón un criterio de éxito** — si Isabel no lo tiene claro, no lo inventes con un
número concreto; ofrece el tipo de métrica adecuada y márcala como pendiente de definir con
el equipo.

**5. Termina con una recomendación** de qué información conviene reunir antes de pasar a
diseño, si el problema todavía no está lo bastante acotado.

## Ejemplo

**Isabel escribe:**
> `/frame-problem` tenemos que rediseñar el onboarding

**Preguntas antes de construir:**
> Antes de reformularlo, necesito algo de contexto:
> - ¿Qué te hace pensar que el onboarding necesita cambiar — un dato (caída de usuarios),
>   una queja concreta, o una intuición?
> - ¿Para quién específicamente? ¿Todos los usuarios nuevos, o un segmento?
> - Si lo arregláis, ¿qué número o comportamiento debería cambiar para saber que
>   funcionó?

**Isabel responde:**
> Vimos que el 40% abandona antes de terminar el onboarding. No sabemos bien por qué. Es
> para todos los usuarios nuevos.

**Output final:**

> **Problem statement:**
> El 40% de los usuarios nuevos abandona el onboarding antes de completarlo, y no se
> conoce la causa. Esto importa porque cada abandono es un usuario que ya se registró y no
> llega a activarse, perdiendo la inversión de adquisición ya hecha.
>
> ⚠️ **Hueco detectado:** "rediseñar" es una solución, no está justificada todavía — no se
> sabe si el problema es de UI (confuso), de fricción (demasiados pasos) o de relevancia
> (no ven el valor). Antes de rediseñar, conviene saber *dónde exactamente* dentro del
> flujo ocurre el abandono.
>
> **Criterio de éxito propuesto:** reducir el abandono del 40% a un número concreto (a
> definir con el equipo) dentro de un plazo.

**Recomendación final:**
> Antes de pasar a diseño, valdría la pena mirar analytics para saber en qué paso concreto
> ocurre el abandono — "rediseñar el onboarding entero" y "arreglar el paso 3 donde se
> atasca todo el mundo" son proyectos muy distintos en esfuerzo.
