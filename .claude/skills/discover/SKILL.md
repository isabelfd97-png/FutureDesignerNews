---
name: discover
description: >-
  Ciclo completo de discovery de producto encadenando cuatro pasos: ideación multi-punto de
  vista, mapeo de suposiciones (Valor / Usabilidad / Viabilidad / Factibilidad), priorización
  por matriz Impacto × Riesgo, y diseño del experimento más barato para validar la suposición
  más arriesgada. Úsala cuando Isabel tenga una oportunidad concreta (de un `journey-map`,
  `layers-user-needs`, o simplemente una idea de feature) y quiera decidir con criterio qué
  construir primero, en vez de saltar directo a construir la primera idea que se le ocurrió.
  Especialmente útil como vocabulario y proceso de trabajo en equipo (PM, ingeniería,
  diseño), no solo para proyectos personales.
---

# Discover — ciclo completo de discovery de producto

> Fuente: [phuryn/pm-skills — pm-product-discovery](https://github.com/phuryn/pm-skills)

Basado en el ciclo de discovery continuo de Teresa Torres (*Continuous Discovery Habits*):
en vez de comprometerse a construir la primera idea que suena bien, se generan varias
opciones, se identifica qué tendría que ser verdad para que cada una funcione, se prioriza
qué suposición es más arriesgada y menos conocida, y se diseña la forma más barata de
comprobarla antes de construir nada grande.

## Cuándo se activa

Isabel tiene una oportunidad concreta ya identificada (puede venir de un `journey-map`, de
`layers-user-needs`, o simplemente de una idea suya de feature) y quiere decidir con
criterio qué construir primero, en vez de comprometerse directamente a la primera idea. Es
especialmente valiosa cuando el contexto es de equipo (PM, ingeniería, diseño juntos
decidiendo qué priorizar), aunque también se puede correr en solitario en un proyecto
personal.

También si pide explícitamente "hazme un `/discover`" o "corre un ciclo de discovery
sobre...".

## Paso 1 — Brainstorm Ideas (ideación multi-perspectiva)

Genera varias soluciones posibles para la oportunidad — nunca una sola. Fuerza variedad
pensando desde perspectivas distintas, no solo la más obvia: ¿cómo lo resolvería alguien
priorizando velocidad? ¿Alguien priorizando confianza/credibilidad? ¿Alguien priorizando el
mínimo esfuerzo de construcción? No conviertas esto en una sola idea "evidente" disfrazada
de brainstorm.

## Paso 2 — Identify Assumptions (mapeo de suposiciones)

Para cada idea generada, lista qué tendría que ser verdad para que funcione, clasificado en
las cuatro categorías de Marty Cagan:

- **Valor** — ¿le importa esto de verdad a alguien? ¿resuelve un dolor real?
- **Usabilidad** — ¿sabrán usarlo sin que se lo expliquen?
- **Viabilidad** — ¿tiene sentido de negocio/recursos sostenerlo? (en proyecto personal sin
  presión de negocio, esta categoría puede quedar en n/a — no la inventes si no aplica)
- **Factibilidad** — ¿se puede construir con lo que se tiene?

Sé concreta en cada suposición — no "asume que gusta", sino qué comportamiento exacto
tendría que darse para que la idea funcione.

## Paso 3 — Prioritize Assumptions (matriz Impacto × Riesgo)

De todas las suposiciones listadas (de todas las ideas, no solo una), identifica cuáles son
más **arriesgadas** (menos se sabe si son ciertas) y de mayor **impacto** (si fallan, la
idea entera se cae). Esas son las que hay que validar primero — no las más fáciles de
comprobar, sino las que más determinan si vale la pena seguir.

## Paso 4 — Brainstorm Experiments (diseño del experimento)

Para la suposición prioritaria, diseña la forma más barata posible de comprobarla — nunca
construir la solución completa como primer paso. Piensa en el experimento más pequeño que
daría una señal real: un prototipo de papel, una versión falsa/manual, observar un
comportamiento existente, una pregunta directa a 2-3 personas.

## Ejemplo completo

Oportunidad: *"el equipo de marketing no está seguro de qué campaña repetir porque la
gráfica actual no permite comparar directamente dos campañas."*

**1. Ideación:**
- Vista de comparación lado a lado de dos campañas
- Overlay de dos líneas superpuestas en la misma gráfica
- Tabla resumen con el % de cambio entre campañas

**2. Suposiciones (para la idea del overlay de líneas):**
- Valor: asume que comparar visualmente ayuda más a decidir que una tabla de números.
- Usabilidad: asume que no se confunden dos líneas superpuestas de distinto color.
- Viabilidad: n/a o a valorar según el contexto de negocio del proyecto.
- Factibilidad: asume que los datos de ambas campañas están en el mismo formato y periodo.

**3. Priorización:** la de Usabilidad es la más arriesgada — es fácil confundir dos líneas
superpuestas — y además es barata de comprobar antes de construir nada.

**4. Experimento:** en vez de construir la interacción completa, hacer un mockup estático
con dos líneas superpuestas y enseñarlo a 2-3 personas del equipo, preguntando qué campaña
creen que va mejor — antes de invertir en construirlo de verdad.
