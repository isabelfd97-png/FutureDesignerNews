---
name: identify-assumptions-existing
description: >-
  Audita una decisión o feature YA existente o ya decidida (no una idea nueva en
  exploración) contra las cuatro categorías de riesgo de Marty Cagan — Valor, Usabilidad,
  Viabilidad, Factibilidad — para detectar la suposición no verificada que podría hacer
  fracasar algo en lo que ya se va a invertir trabajo. Úsala cuando Isabel (o su equipo) ya
  ha decidido construir algo concreto y quiere una última comprobación de riesgo antes de
  comprometer el trabajo, sin necesidad de pasar por un ciclo de discovery completo
  (`discover`).
---

# Identify Assumptions (Existing) — auditar algo ya decidido

> Fuente: [phuryn/pm-skills — pm-product-discovery](https://github.com/phuryn/pm-skills)

Mismo marco de las 4 categorías de riesgo de Marty Cagan que usa el Paso 2 de `discover`,
pero pensado como comprobación independiente y rápida sobre algo que **ya está decidido o
en marcha** — no una idea nueva en fase de exploración. Sirve para el momento en que alguien
(Isabel, o un compañero de equipo) llega con "vamos a construir X" ya cerrado, y hace falta
una última pasada de riesgo antes de comprometer el trabajo.

## Cuándo se activa

Isabel tiene una feature, decisión o pieza de trabajo ya decidida (propia o de alguien del
equipo) y quiere comprobar qué suposiciones no verificadas está dando por hechas antes de
construirla. No hace falta pasar por ideación ni por generar alternativas — eso es
`discover` completo; esta skill entra directo a auditar lo ya decidido.

## Las cuatro categorías

- **Valor** — ¿le importa esto de verdad a alguien? ¿resuelve un dolor real y verificado?
- **Usabilidad** — ¿sabrán usarlo sin que se lo expliquen?
- **Viabilidad** — ¿tiene sentido de negocio o de recursos sostenerlo? (en un proyecto sin
  presión de negocio real, puede marcarse n/a en vez de forzarla)
- **Factibilidad** — ¿se puede construir con lo que se tiene ahora mismo?

## Cómo hacer la auditoría

Por cada categoría, marca el riesgo (✅ bajo riesgo / ⚠️ riesgo real y sin verificar / n/a)
y, si es ⚠️, describe exactamente qué comportamiento tendría que darse para que la
suposición fuera cierta — no te quedes en "es arriesgado", di qué es lo que no se sabe.

Termina señalando explícitamente **cuál de las suposiciones marcadas ⚠️ es la que más
peligro tiene de "hundir" el trabajo** si resulta falsa — no dejes las cuatro categorías con
el mismo peso si una es claramente la más crítica.

## Ejemplo — creando algo nuevo desde cero

Isabel: *"Ya he decidido crear una gráfica nueva de métricas de uso de campañas para los
usuarios — de entrada quiero auditarla antes de ponerme a construirla."*

- **Valor** ⚠️ — asume que los usuarios quieren ver esta métrica concreta (uso por
  campaña) y no otra (por ejemplo, comparativa entre campañas, o tendencia en el tiempo).
  No verificado con ningún usuario todavía.
- **Usabilidad** ✅ — es un tipo de gráfica estándar (barras/líneas), bajo riesgo de que no
  se entienda.
- **Viabilidad** — n/a o a valorar según el contexto de negocio del proyecto.
- **Factibilidad** ✅ — los datos ya existen en el sistema, bajo riesgo técnico.

**La que puede hundir el trabajo:** Valor. Si construyes la gráfica y en realidad el
usuario quería ver otra cosa, has invertido el esfuerzo en la métrica equivocada.

## Ejemplo — iterando algo que ya existe

Isabel: *"Voy a iterar el estilo visual de una gráfica de métricas que ya existe, hacerla
más atractiva."*

- **Valor** ⚠️ — asume que el problema real es el estilo visual, no la elección de qué
  datos mostrar o cómo se organizan. Si nadie se ha quejado del estilo pero sí de que "no
  entienden la gráfica", el rediseño visual no ataca el problema real.
- **Usabilidad** ⚠️ — un rediseño puede mejorar el atractivo pero empeorar la legibilidad
  si no se prueba con los mismos usuarios que ya la leen hoy.
- **Viabilidad** — n/a normalmente para una iteración de estilo.
- **Factibilidad** ✅ — es una iteración, no una construcción desde cero; bajo riesgo.

**La que puede hundir el trabajo:** Valor — comprobar primero si el problema reportado es
de verdad estético antes de invertir en el rediseño.
