---
name: error-flow
description: >-
  Diseña el manejo de errores de una feature de principio a fin — prevención, detección,
  mensaje y recuperación — no solo detecta que un error puede ocurrir, sino qué le pasa al
  usuario cuando ocurre: qué ve, si puede seguir usando el resto de la pantalla, cómo se
  recupera, y si se podía haber evitado antes. Úsala cuando `map-states` haya marcado un
  hueco de error/offline sin resolver, o cuando Isabel quiera diseñar la experiencia
  completa de qué pasa cuando algo falla, en vez de dejarlo en un genérico "ha ocurrido un
  error".
---

# Error Flow — diseñar qué pasa cuando algo falla

> Fuente: [Owl-Listener/designer-skills — interaction-design](https://github.com/Owl-Listener/designer-skills/tree/main/interaction-design)

`map-states` marca **que existe** un estado de error (o que falta uno), pero no diseña qué
le pasa al usuario ahí. `error-flow` coge ese hueco y lo diseña de principio a fin, para
una feature completa. No es una herramienta de detección de bugs — es diseño de la
experiencia de cuando algo falla.

## Las cuatro partes

- **Prevención** — qué se puede hacer para que el error no ocurra (validar antes de
  enviar, avisar de límites antes de que se rompan).
- **Detección** — cómo se sabe que algo falló (timeout, respuesta de error, validación).
- **Mensaje** — qué le dice al usuario, dónde aparece, con qué tono. Nunca un genérico "ha
  ocurrido un error" si se puede ser específico.
- **Recuperación** — qué puede hacer el usuario para salir del error (reintentar, deshacer,
  seguir usando lo que sí funcionó).

## Cuándo se activa

`map-states` ha marcado un hueco de error/offline sin resolver y hace falta diseñarlo de
verdad, o Isabel quiere directamente diseñar el manejo de errores de una feature completa.
También si pide explícitamente `/error-flow [feature]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- Cuando falla algo, ¿el usuario queda bloqueado del todo, o puede seguir usando el resto
  de la pantalla/feature?
- ¿Hay algo que se pueda prevenir antes de que ocurra el error (avisos previos, límites
  visibles)?

**2. Diseña las cuatro partes** (prevención, detección, mensaje, recuperación) con lo
aportado. El mensaje debe ser específico al fallo concreto, no genérico, y localizado al
área afectada si el resto de la pantalla sigue funcionando — nunca bloquear todo por un
fallo parcial si se puede evitar.

**3. Marca con ⚠️ cualquier decisión sin resolver** (número de reintentos automáticos,
tiempo de espera antes de mostrar el error, qué pasa si falla también el reintento).

**4. Termina con una recomendación clara** sobre el patrón de mensaje/recuperación más
adecuado — priorizando mantener usable lo que sí funcionó, en vez de castigar al usuario
entero por un fallo parcial.

## Ejemplo

**Isabel escribe:**
> `/error-flow` la gráfica de comparación de campañas — el hueco de `offline`/error que
> detectamos antes con map-states

**Preguntas antes de construir:**
> Antes de diseñar el flujo de error, dime:
> - Cuando falla la carga de una campaña, ¿el usuario puede seguir usando el resto de la
>   pantalla, o queda bloqueado?
> - ¿Hay algo que se pueda prevenir antes de que ocurra el error (ej. avisar si el rango
>   de fechas es demasiado grande y probablemente tarde/falle)?

**Isabel responde:**
> Puede seguir viendo la campaña que sí cargó. No habíamos pensado en prevención.

**Output final:**

> **Prevención:** si el rango de fechas seleccionado supera 90 días, mostrar un aviso
> antes de cargar ("rangos largos pueden tardar más") en vez de dejar que falle
> silenciosamente por timeout.
>
> **Detección:** timeout a los 10s sin respuesta de la API de la campaña que falla.
>
> **Mensaje:** en el hueco donde debería estar la campaña que falló — no un modal
> bloqueante, ya que la otra campaña sí cargó: *"No se pudo cargar esta campaña.
> [Reintentar]"* — específico a esa campaña, no un error genérico de toda la pantalla.
>
> **Recuperación:** botón de reintentar solo para la campaña fallida, sin recargar la que
> ya funcionaba.
>
> ⚠️ **Sin definir:** ¿cuántos reintentos automáticos, si alguno, antes de mostrar el
> botón manual? No especificado.

**Recomendación final:**
> Usar mensaje de error localizado (solo en el hueco de la campaña fallida) en vez de
> bloquear toda la pantalla — mantiene usable lo que sí funcionó, en vez de castigar al
> usuario por un fallo parcial.
