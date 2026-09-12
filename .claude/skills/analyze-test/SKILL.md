---
name: analyze-test
description: >-
  Analiza resultados reales de un experimento A/B — significancia estadística, validación
  de que se alcanzó el tamaño de muestra necesario, y una recomendación Ship / Extend /
  Stop. Úsala cuando ya haya datos de un test corriendo (diseñado idealmente con
  `experiment`) y haga falta decidir si lanzar, seguir corriendo, o parar — especialmente
  cuando el resultado "parece positivo" a mitad de camino y hay riesgo de decidir antes de
  tiempo sobre ruido, no sobre un efecto real.
---

# Analyze Test — de resultados a decisión Ship/Extend/Stop

> Fuente: [phuryn/pm-skills — pm-data-analytics](https://github.com/phuryn/pm-skills)

Cierra el círculo con `experiment` — esa skill diseña el A/B test, esta analiza los
resultados una vez corrido. El error más común que previene: mirar el resultado a mitad de
camino, ver que "parece que gana B", y lanzar sin comprobar si eso es un efecto real o solo
ruido de los primeros días (espiar el test antes de tiempo).

## Las tres comprobaciones

- **Significancia estadística** — si la diferencia observada entre variantes es un efecto
  real o ruido aleatorio, con su intervalo de confianza.
- **Validación de tamaño de muestra** — si se alcanzó de verdad el volumen de datos
  necesario para el efecto mínimo detectable (MDE) planteado al diseñar el test, con el
  tráfico real observado (no el estimado de antemano).
- **Recomendación:**
  - **Ship** — resultado significativo, ganador claro, se puede lanzar.
  - **Extend** — tendencia positiva pero aún sin suficientes datos, seguir corriendo.
  - **Stop** — sin diferencia real, o la variante nueva perjudica.

## Cuándo se activa

Hay datos reales de un experimento corriendo (idealmente diseñado con `experiment`) y hace
falta decidir si lanzar, extender o parar. También si pide explícitamente
`/analyze-test [datos del experimento]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cuánto tiempo se planeó correr el test originalmente, y cuánto lleva corriendo ya?

**2. Calcula significancia e intervalo de confianza** con los datos reales aportados —
nunca declares un ganador solo por el porcentaje de mejora bruto sin mirar el intervalo.

**3. Compara el tamaño de muestra alcanzado contra el necesario** (del diseño original si
existe, o estimado con el tráfico real).

**4. Da la recomendación Ship/Extend/Stop**, y si el resultado "parece positivo" pero el
intervalo de confianza todavía es ancho, márcalo explícitamente con ⚠️ como señal
prematura, no como resultado concluyente.

## Ejemplo

**Isabel escribe:**
> `/analyze-test` los resultados del experimento de la leyenda debajo de la gráfica,
> llevamos 2 semanas corriendo — aquí los datos: [pega/adjunta CSV]

**Preguntas antes de construir:**
> Antes de analizar, dime: ¿cuántas semanas se planeó correr el test originalmente (según
> `experiment`), y ya se cumplieron?

**Isabel responde:**
> Se planeó para 3-4 semanas, llevamos solo 2.

**Output final:**

> **Significancia:** la variante B (leyenda debajo) muestra un 12% de mejora en tiempo
> hasta decisión, pero con un intervalo de confianza que todavía cruza el cero — no es
> concluyente todavía.
>
> **Validación de tamaño de muestra:** con el tráfico real observado (no el estimado), se
> necesitan ~1-2 semanas más para alcanzar el tamaño de muestra planeado.
>
> ⚠️ **Aviso:** el resultado "parece positivo" pero es exactamente el tipo de señal
> prematura que lleva a lanzar demasiado pronto — el intervalo de confianza aún es
> demasiado ancho.

**Recomendación: Extend.** Seguir corriendo el test 1-2 semanas más antes de decidir, en
vez de lanzar B ya solo porque la tendencia se ve bien.
