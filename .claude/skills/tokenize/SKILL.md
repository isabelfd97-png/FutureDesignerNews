---
name: tokenize
description: >-
  Extrae colores, espaciados, tipografías y elevaciones escritos "a pelo" en código real
  (CSS, hojas de estilo, componentes) y los organiza en design tokens con nombre, estructura
  jerárquica y theme mapping. Úsala cuando Isabel tenga código de un componente o pantalla
  con valores repetidos sin sistematizar (hex codes sueltos, paddings inconsistentes) y
  quiera limpiarlo en tokens reutilizables. A diferencia del resto de skills de esta
  colección, trabaja directamente sobre código real, no sobre ideas o estrategia.
---

# Tokenize — de valores sueltos a design tokens

> Fuente: [Owl-Listener/designer-skills — design-systems](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)

A diferencia del resto de skills de investigación/estrategia, esta trabaja directamente
sobre código real (CSS, hojas de estilo, un archivo de componente). Busca valores escritos
"a pelo" y repetidos sin sistematizar — colores hexadecimales sueltos, paddings que varían
sin motivo aparente, tipografías inconsistentes — y los organiza en **design tokens**:
variables con nombre y significado, en vez de valores sueltos copiados y pegados por todo
el código.

## Qué decide, además de poner nombre

- **Naming** — cómo se llama cada token (`color-brand-primary`, no `naranja1`).
- **Estructura** — jerarquía: si es un token base, o uno semántico que apunta a uno base.
- **Theme mapping** — si el mismo token cambia de valor en modo claro/oscuro u otras
  variantes.

## Cuándo se activa

Isabel tiene código real (CSS, un componente, una hoja de estilos) con valores repetidos
sin sistematizar y quiere organizarlos en tokens reutilizables. También si pide
explícitamente `/tokenize [código o archivo]`.

No la actives sin código real que analizar — esta skill no inventa una paleta desde cero,
limpia y organiza lo que ya existe escrito.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Ya existe algún sistema de tokens en el resto del producto que deba respetarse, o es la
  primera vez que se sistematiza?
- ¿Hay modo oscuro u otras variantes de tema, o solo un tema por ahora?

**2. Extrae los valores repetidos** del código aportado, contando cuántas veces aparece
cada uno y detectando variaciones que podrían ser el mismo valor escrito de forma
inconsistente (`#1A1A1A` vs `#1a1a1a`, `15px` vs `16px` vs `17px`).

**3. Propón el nombre y la estructura de cada token**, agrupando lo que es claramente el
mismo valor con pequeñas inconsistencias de escritura.

**4. Marca con ⚠️ cualquier inconsistencia que podría ser un error accidental (copiar/pegar)
en vez de una decisión de diseño deliberada** — no la unifiques silenciosamente sin
señalarlo, porque cambiar el valor "canónico" puede alterar visualmente algo que nadie
decidió cambiar a propósito.

**5. Termina recomendando qué ⚠️ confirmar antes de aplicar los cambios al código real.**

## Ejemplo

**Isabel escribe:**
> `/tokenize` aquí está el CSS de la gráfica de campañas, tiene colores repetidos por
> todos lados: [pega el CSS]

**Preguntas antes de construir:**
> Antes de organizar los tokens, dos cosas:
> - ¿Ya existe algún sistema de tokens en el resto del producto que debería respetar (o es
>   la primera vez)?
> - ¿Hay modo oscuro, o solo un tema por ahora?

**Isabel responde:**
> No hay sistema de tokens todavía en ningún sitio. Solo modo claro por ahora.

**Output final:**

> **Tokens extraídos:**
> - `#FF6B00` (aparece 6 veces) → `color-chart-highlight`
> - `#1A1A1A` (aparece 12 veces, a veces como `#1a1a1a`, inconsistente) →
>   `color-text-primary`
> - `#F5F5F5` (aparece 4 veces) → `color-background-subtle`
> - `16px` de padding (aparece 8 veces con ligeras variaciones: 15px, 16px, 17px) →
>   `space-md` (unificado a 16px)
>
> ⚠️ **Detectado:** `#1A1A1A` y `#1a1a1a` son el mismo color escrito de forma
> inconsistente — al unificar en un token, se corrige automáticamente esta inconsistencia
> oculta.
>
> ⚠️ **Detectado:** el padding varía entre 15px/16px/17px sin razón aparente —
> probablemente error de copiar/pegar, no una decisión de diseño. Se propone unificar a
> 16px, pero confirmar antes de aplicar el cambio.

**Recomendación final:**
> Antes de reemplazar los valores en el CSS, confirmar los dos ⚠️ — sobre todo el del
> padding, porque unificarlo podría cambiar visualmente algo que nadie decidió cambiar a
> propósito.
