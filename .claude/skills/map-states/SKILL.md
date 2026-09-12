---
name: map-states
description: >-
  Modela los estados de un componente concreto como una máquina de estados formal —
  estados, eventos que disparan cada transición, guards (condiciones que la bloquean) y
  edge cases — con foco especial en los estados que se suelen olvidar (loading, empty,
  error, partial, offline). Úsala cuando un componente tenga varios estados que interactúan
  entre sí de forma no trivial y la sección de "Estados" de `create-component` se quede
  corta, o cuando Isabel quiera formalizar el comportamiento antes de que esos estados se
  descubran en QA en vez de en diseño.
---

# Map States — máquina de estados de un componente

> Fuente: [Owl-Listener/designer-skills — interaction-design](https://github.com/Owl-Listener/designer-skills/tree/main/interaction-design)

## Cómo encaja con lo que ya existe

Tres skills tocan "estados" de formas distintas:
- `layers-interaction-flow` mapea **pantallas/lugares** por los que se mueve el usuario
  (navegación entre pantallas).
- `create-component` incluye una sección de "Estados" dentro de la spec completa del
  componente, de forma ligera.
- `map-states` (esta) se mete solo en los estados de **un componente concreto**, como
  máquina de estados formal: no solo qué estados hay, sino qué evento dispara cada
  transición y qué condiciones (guards) pueden bloquearla.

Útil cuando un componente tiene varios estados que interactúan entre sí de forma no
trivial — ahí una sección de "Estados" dentro de una spec general se queda corta.

## Qué modela

- **Estados** — todas las condiciones posibles del componente (incluyendo las que se
  suelen olvidar: loading, empty, error, partial, offline).
- **Eventos** — qué dispara cada transición de un estado a otro.
- **Guards** — condiciones que pueden bloquear una transición aunque el evento ocurra.
- **Edge cases** — combinaciones inusuales o límite que no encajan en el flujo principal.

## Cuándo se activa

Isabel tiene un componente con varios estados que interactúan de forma compleja
(carga parcial, reintentos, dependencias entre estados) y quiere formalizarlos antes de que
se descubran como bugs en QA. También si pide explícitamente `/map-states [componente]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Los datos llegan de golpe, o pueden llegar de forma parcial/escalonada?
- ¿Qué pasa si se pierde la conexión o falla una petición a mitad de proceso? Si Isabel no
  lo ha pensado, dilo explícitamente en vez de asumir un comportamiento.

**2. Construye la máquina de estados**: lista de estados, y para cada transición, el
evento que la dispara y cualquier guard que la condicione.

**3. Revisa explícitamente los estados que se suelen olvidar** — loading, empty, error,
partial, offline — y marca con ⚠️ cualquiera que no esté definido.

**4. Termina recomendando qué ⚠️ resolver primero**, explicando qué pasaría por defecto
(normalmente el peor comportamiento posible) si ingeniería lo decide por su cuenta sin
spec.

## Ejemplo

**Isabel escribe:**
> `/map-states` la gráfica de comparación de campañas — quiero los estados formalizados

**Preguntas antes de construir:**
> Antes de la máquina de estados, dime:
> - ¿Los datos se cargan de golpe, o pueden llegar parcialmente (una campaña carga antes
>   que la otra)?
> - ¿Qué pasa si se pierde la conexión a mitad de carga?

**Isabel responde:**
> Pueden llegar parcialmente, cada campaña se pide por separado. No había pensado en
> pérdida de conexión.

**Output final:**

> **Estados:** `idle` → `loading` → `partial` (una campaña cargada, otra no) → `loaded`
> (ambas) / `error`
>
> **Transiciones:**
> - `idle` --(evento: usuario selecciona 2 campañas)--> `loading`
> - `loading` --(evento: llega respuesta de 1 campaña)--> `partial`
> - `partial` --(evento: llega la segunda respuesta)--> `loaded`
> - `partial` --(evento: falla la segunda petición)--> `error` con guard: *solo si ya
>   pasaron X segundos sin respuesta, no al primer fallo de red*
>
> ⚠️ **Estado sin definir:** no hay ningún estado `offline` — si se pierde la conexión en
> `partial`, ¿se queda esperando indefinidamente, muestra un aviso, o reintenta
> automáticamente?

**Recomendación final:**
> Definir el estado `offline` antes de construir — sin él, ingeniería decidirá su propio
> comportamiento (probablemente "se queda esperando para siempre", la peor experiencia
> posible).
