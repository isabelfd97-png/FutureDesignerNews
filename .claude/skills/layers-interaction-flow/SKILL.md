---
name: layers-interaction-flow
description: >-
  Mapea la estructura de interacción de un flujo en notación breadboard (Shape Up, Ryan
  Singer / Basecamp) — lugares, affordances (acciones posibles) y líneas de conexión entre
  ellos — sin ningún diseño visual, marcando edge cases, caminos de fallo y decisiones
  abiertas. Úsala después de tener el modelo conceptual (`layers-conceptual-model`) y antes
  de diseñar ninguna pantalla, cuando Isabel necesite decidir cómo se mueve el usuario entre
  estados/pantallas antes de decidir cómo se ven.
---

# Layers Interaction Flow — breadboarding antes del diseño visual

> Fuente: [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)

El **breadboarding** viene de la metodología Shape Up de Basecamp (Ryan Singer). El nombre
es una metáfora de las placas de pruebas de electrónica: antes de meter un circuito en una
carcasa bonita, se prueba "al aire", con cables sueltos, para ver si la lógica funciona.
Aplicado a producto: se mapea el flujo completo en texto o cajas simples, **sin ningún
diseño visual**, para forzar las decisiones estructurales antes de las decisiones de
estilo.

## Los tres elementos de la notación

- **Places (lugares)** — pantallas o estados por los que pasa el usuario.
- **Affordances (acciones)** — cosas concretas que el usuario puede hacer en cada lugar (un
  botón, un link, un campo).
- **Connection lines** — a qué lugar lleva cada affordance.

**Regla de oro:** nunca maquetas. Si en algún momento se empieza a discutir color, tamaño o
estilo mientras se construye el breadboard, se ha saltado un paso — esto es solo esqueleto
y cableado.

## Diferencia con `layers-conceptual-model`

`layers-conceptual-model` define **qué es cada cosa** (objetos, relaciones, estados).
`layers-interaction-flow` define **cómo se mueve el usuario entre esas cosas** — el camino,
no el vocabulario. Van en secuencia: primero el modelo conceptual, luego el flujo de
interacción construido sobre ese modelo ya resuelto.

## Cuándo se activa

Isabel tiene un modelo conceptual razonablemente claro (propio o de
`layers-conceptual-model`) y necesita decidir cómo se mueve el usuario entre estados o
pantallas, antes de diseñar nada visual. También si pide explícitamente
`/layers-interaction-flow [flujo a mapear]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Desde dónde arranca el flujo — hay un punto de entrada claro, o varios posibles?
- ¿Qué pasa si algo falla en el camino (datos no disponibles, una selección incompleta)? Si
  Isabel no lo ha pensado, dilo explícitamente en vez de asumir un comportamiento.

**2. Construye el breadboard** en notación de lugares/affordances/conexiones, sin usar
ningún término visual (color, tamaño, posición).

**3. Marca con ⚠️ cada camino de fallo sin definir y cada decisión estructural abierta** —
no rellenes tú el hueco con la opción que te parezca más razonable sin decirlo
explícitamente.

**4. Termina recomendando qué ⚠️ resolver antes de pasar a diseño visual**, explicando por
qué es una decisión estructural (cambia cuántos lugares/estados existen) y no una decisión
de estilo.

## Ejemplo

**Isabel escribe:**
> `/layers-interaction-flow` mapea el flujo de comparar dos campañas en el dashboard

**Preguntas antes de construir:**
> Antes del breadboard, dime:
> - ¿Desde dónde arranca esto — el usuario ya está viendo una campaña y decide comparar, o
>   hay un punto de entrada distinto?
> - ¿Qué pasa si intenta comparar y algo falla (datos no disponibles, solo una campaña
>   seleccionada)?

**Isabel responde:**
> Arranca desde la lista de campañas, selecciona dos con checkbox. No había pensado en qué
> pasa si falla algo.

**Output final:**

> **Lugar: Lista de campañas**
> → affordance "seleccionar checkbox de Campaña A" → permanece en Lista de campañas
> (estado: 1 seleccionada)
> → affordance "seleccionar checkbox de Campaña B" → Lugar: Vista de comparación
>
> **Lugar: Vista de comparación**
> → affordance "cerrar comparación" → vuelve a Lista de campañas
> → affordance "cambiar Campaña B por otra" → permanece en Vista de comparación, actualiza
> datos
>
> ⚠️ **Camino de fallo sin definir:** ¿qué Lugar existe si una de las dos campañas no
> tiene datos suficientes para comparar? No hay ningún lugar/estado definido para eso
> todavía.
> ⚠️ **Decisión abierta:** si el usuario deselecciona una campaña estando en la Vista de
> comparación, ¿vuelve automáticamente a Lista, o se queda esperando una segunda
> selección?

**Recomendación final:**
> Resolver los dos ⚠️ antes de pasar a diseño visual — son decisiones estructurales, no de
> estilo, y cambian cuántas pantallas/estados hay que diseñar realmente.
