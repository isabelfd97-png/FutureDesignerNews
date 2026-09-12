---
name: create-component
description: >-
  Especifica la API completa y reutilizable de un componente de sistema de diseño —
  props, variantes, estados, accesibilidad, edge cases — pensado para vivir en una librería
  y usarse en muchas pantallas distintas, no para documentar una pantalla concreta. Úsala
  cuando Isabel vaya a formalizar un componente nuevo o ya existente pero sin documentar,
  para que ingeniería tenga una spec completa desde la primera pasada.
---

# Create Component — spec completa de un componente reutilizable

> Fuente: [Owl-Listener/designer-skills — design-systems](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)

## ⚠️ Diferencia con `design-handoff`

Esta skill se parece a `design:design-handoff` (ya disponible por defecto), pero no es lo
mismo:

- **`design-handoff`** parte de **un diseño concreto ya hecho** (una pantalla, un mockup) y
  documenta cómo construir *esa pantalla específica* — layout, tokens usados, qué props
  necesita un componente en ese contexto puntual.
- **`create-component`** parte de cero (o de un componente ya construido pero sin
  documentar) y define la **API completa y reutilizable** del componente en abstracto —
  cada prop posible, cada variante, cada estado, pensado para cualquier pantalla que lo use,
  no solo la que originó la necesidad.

Es la diferencia entre "así se ve este botón en esta pantalla" (`design-handoff`) y "así
funciona el componente Botón en todo el sistema" (`create-component`). Si Isabel pide specs
de handoff para una pantalla concreta ya diseñada, usa `design-handoff`; si pide formalizar
un componente para que viva en la librería y se reutilice, usa esta.

## Qué incluye la spec

- **Props** — parámetros de entrada y opciones de configuración.
- **Variantes** — versiones o combinaciones de estilo distintas.
- **Estados** — condiciones visuales/interactivas por las que puede pasar (cargando, vacío,
  error, hover, disabled...).
- **Accesibilidad** — cumplimiento WCAG, marcado semántico, soporte de tecnología asistiva.
- **Edge cases** — combinaciones de props/estados que no están resueltas y que alguien
  decidirá por su cuenta si no se especifican.

## Cuándo se activa

Isabel va a formalizar un componente nuevo, o uno ya construido pero nunca documentado
formalmente, para que viva en un sistema/librería reutilizable. También si pide
explícitamente `/create-component [componente]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Es un componente nuevo, o ya existe una versión sin documentar que hay que formalizar?
- ¿Cuántas variantes necesita (por tipo de dato, tamaño, contexto de uso)?

**2. Construye la spec completa** (props, variantes, estados, accesibilidad) con lo
aportado, usando criterio razonable para completar lo que falte.

**3. Detecta y marca con ⚠️ los edge cases sin resolver** — combinaciones de props o
estados que no estaban decididas en la versión actual (si existe) o que Isabel no
mencionó, y que si no se especifican, cada desarrollador que las implemente decidirá algo
distinto por su cuenta.

**4. Termina señalando cuál de los ⚠️ es más urgente resolver antes de pasar la spec a
ingeniería.**

## Ejemplo

**Isabel escribe:**
> `/create-component` quiero especificar el componente de gráfica de comparación de
> campañas para nuestra librería

**Preguntas antes de construir:**
> Antes de la spec completa, dime:
> - ¿Es un componente nuevo, o ya existe una versión que hay que formalizar en spec?
> - ¿Cuántas variantes visuales necesita (por tipo de dato, por tamaño), o de momento solo
>   una?

**Isabel responde:**
> Existe una versión ya construida pero sin documentar. Necesita variante compacta (para
> tarjetas pequeñas) y variante completa (para la pantalla de detalle).

**Output final:**

> **Props:** `data`, `variant` (`compact` | `full`), `comparisonMode` (boolean),
> `onDataPointClick`...
> **Variantes:** `compact` (sin ejes etiquetados, solo tendencia visual) / `full` (ejes,
> leyenda, tooltip)
> **Estados:** cargando / con datos / vacío / error de carga
> ⚠️ **Edge case sin definir:** ¿qué pasa si `comparisonMode` está activo pero solo hay
> una campaña seleccionada? No estaba resuelto en la versión actual.
> **Accesibilidad:** roles ARIA para gráfica, texto alternativo describiendo la tendencia
> para lectores de pantalla

**Recomendación final:**
> El edge case de `comparisonMode` con una sola campaña es lo primero a resolver — sin
> spec, cada desarrollador que lo toque decidirá algo distinto por su cuenta.
