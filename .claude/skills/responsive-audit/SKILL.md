---
name: responsive-audit
description: >-
  Audita un diseño en varios breakpoints (móvil, tablet, desktop) revisando layout, touch
  targets y content reflow, para detectar pensamiento "desktop-first" antes de que salga a
  producción. Úsala cuando Isabel tenga un diseño ya construido (idealmente una página o
  componente real que se pueda abrir y redimensionar) y quiera comprobar que se comporta
  bien en todos los tamaños de pantalla, no solo en el que se diseñó primero.
---

# Responsive Audit — comprobar cada breakpoint, no asumirlo

> Fuente: [Owl-Listener/designer-skills — ui-design](https://github.com/Owl-Listener/designer-skills/tree/main/ui-design)

Es habitual diseñar pensando primero en desktop y asumir que "ya se adaptará" a móvil sin
comprobarlo de verdad. Esta skill audita breakpoint por breakpoint:

- **Layout** — cómo se reorganiza el contenido en cada tamaño.
- **Touch targets** — que los elementos interactivos sean lo bastante grandes en móvil
  (mínimo recomendado ~44px de área táctil).
- **Content reflow** — que texto y componentes se adapten sin desbordar ni cortarse.

## Cómo comprobarlo de verdad, no solo describirlo

Si el diseño vive en una página o componente real (aunque sea en desarrollo local),
ábrelo en el navegador y **redimensiona la ventana de verdad** en cada breakpoint para
comprobarlo, en vez de asumir el comportamiento solo por lo que Isabel describa. Si es un
diseño en Figma sin código todavía, pide capturas de cada breakpoint (mismo criterio que
`benchmark`) en vez de inventar cómo se vería.

## Cuándo se activa

Isabel tiene un diseño ya construido y quiere comprobar que se comporta bien en todos los
tamaños de pantalla, no solo en el que diseñó primero. También si pide explícitamente
`/responsive-audit [página o componente]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Qué breakpoints importan realmente? (los estándar de móvil/tablet/desktop, o unos
  concretos definidos por el proyecto)
- ¿Hay algo que ya se sospeche que falla, o se parte de cero?

**2. Revisa cada breakpoint por separado**, marcando el estado con:
- ✅ correcto
- ⚠️ funciona pero con problema menor (compresión, legibilidad reducida)
- 🔴 roto — desbordamiento, contenido inaccesible, touch target insuficiente

**3. Termina con una recomendación priorizada** de qué arreglar primero — normalmente lo
🔴 en el breakpoint más pequeño, porque suele ser el más restrictivo y el que más usuarios
afecta si el producto es mobile-heavy.

## Ejemplo

**Isabel escribe:**
> `/responsive-audit` audita la gráfica de comparación de campañas que ya está montada,
> tengo el servidor corriendo en local

**Preguntas antes de construir:**
> Antes de auditar, dos cosas:
> - ¿Qué breakpoints os importan realmente? (móvil/tablet/desktop estándar, o tenéis unos
>   concretos definidos)
> - ¿Hay algo que ya sospeches que falla, o partimos de cero?

**Isabel responde:**
> Los estándar están bien. Sospecho que en móvil la leyenda de la gráfica se sale de la
> pantalla.

**Output final** (tras abrir y redimensionar de verdad):

> **Desktop (1440px):** ✅ layout correcto, leyenda a la derecha de la gráfica.
> **Tablet (768px):** ⚠️ la leyenda se mantiene a la derecha pero deja la gráfica
> comprimida a menos de 300px de ancho — apenas se lee la tendencia.
> **Móvil (375px):** 🔴 confirmado — la leyenda se sale del viewport horizontalmente,
> genera scroll lateral no intencional. Además, los puntos de datos táctiles miden ~18px,
> por debajo del mínimo recomendado de 44px.

**Recomendación final:**
> Prioridad 🔴 en móvil: mover la leyenda debajo de la gráfica en vez de al lado, y
> aumentar el área táctil de los puntos de datos (puede ser mayor que el punto visual, con
> padding invisible). El problema de tablet es secundario y se resuelve solo si se arregla
> el patrón de leyenda responsive.
