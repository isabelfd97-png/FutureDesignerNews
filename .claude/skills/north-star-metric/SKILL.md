---
name: north-star-metric
description: >-
  Define la North Star Metric de un producto o feature — la métrica única que mejor
  captura el valor real entregado al cliente — junto a sus métricas de apoyo (input
  metrics, indicadores tempranos que la predicen). Clasifica primero el negocio en uno de
  tres "juegos" (atención, transacción, productividad) para elegir el tipo de métrica
  correcto. Úsala cuando Isabel necesite proponer una métrica de éxito para una feature o
  producto con el mismo rigor que un PM o alguien de datos, en vez de una métrica intuitiva
  de diseño (tipo "engagement" o "tiempo en página") que no encaja con el tipo de negocio.
---

# North Star Metric — la métrica única y sus predictores tempranos

> Fuente: [phuryn/pm-skills — pm-marketing-growth](https://github.com/phuryn/pm-skills)

Concepto de growth popularizado por Sean Ellis y Amplitude: un producto debería tener una
sola métrica principal que capture mejor el valor real entregado a sus clientes, y que
prediga el éxito a largo plazo mejor que cualquier otra. Es fácil, sin este marco, proponer
una métrica de diseño intuitiva (engagement, tiempo en página) que no encaja con el tipo de
negocio real — y que por eso mismo un PM o alguien de datos tumbe con razón.

## Paso previo — clasificar el "juego" de negocio

Antes de elegir la métrica, clasifica el negocio en uno de tres tipos, porque la métrica
correcta depende de esto:

- **Juego de atención** (modelos con publicidad) — la métrica gira en torno a
  tiempo/impresiones/atención capturada.
- **Juego de transacción** (e-commerce, marketplaces) — gira en torno a conversión, volumen
  de transacciones.
- **Juego de productividad** (SaaS, herramientas) — gira en torno a uso recurrente,
  adopción, retención.

Nunca elijas una métrica sin haber identificado antes el tipo de juego — una métrica de
"atención" (vistas, tiempo en pantalla) en un negocio de productividad puede parecer
positiva y no significar nada de valor real entregado.

## Cuándo se activa

Isabel necesita proponer una métrica de éxito para una feature o producto y quiere que
resista el escrutinio de un PM o de alguien de datos, en lugar de una intuición de diseño
sin conectar al modelo de negocio real. También si pide explícitamente
`/north-star-metric [feature o producto]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cómo gana dinero la empresa — suscripción/SaaS, comisión por transacción, publicidad?
- ¿Ya existe una North Star Metric a nivel de producto, o sería la primera vez que se
  define (aunque sea solo para una feature)?

**2. Clasifica el juego de negocio** con la respuesta, explicando brevemente por qué.

**3. Propón la North Star Metric** — debe medir valor real entregado, no una proxy fácil de
medir pero vacía (vistas, clics) si el juego de negocio no encaja con eso.

**4. Propón 1-2 input metrics** — indicadores tempranos que predicen si la North Star va a
subir o bajar, no solo el resultado final.

**5. Marca con ⚠️ cualquier métrica "tentadora" que Isabel mencione o que sea obvia elegir,
pero que no encaje con el juego de negocio identificado** — explica por qué no predice lo
que parece predecir.

## Ejemplo

**Isabel escribe:**
> `/north-star-metric` la feature de comparación de campañas que estamos lanzando

**Preguntas antes de construir:**
> Antes de definir la métrica, necesito saber:
> - ¿Cómo gana dinero vuestra empresa — suscripción/SaaS, comisión por transacción,
>   publicidad?
> - ¿Ya tenéis una North Star Metric para el producto general, o sería la primera vez que
>   se define?

**Isabel responde:**
> Es SaaS, cobramos suscripción mensual. No tenemos North Star definida todavía a nivel de
> producto, solo para esta feature.

**Output final:**

> **Clasificación:** juego de productividad (SaaS) — la métrica debe girar en torno a uso
> recurrente y retención, no en torno a impresiones o transacciones.
>
> **North Star Metric propuesta:** número de decisiones de "repetir/no repetir campaña"
> tomadas usando la comparación (no solo "vistas de la gráfica" — eso mide atención, no
> valor real entregado).
>
> **Input metrics (predictores tempranos):**
> - % de comparaciones que terminan en una decisión tomada (vs. abandonadas a medias)
> - Tiempo medio hasta la decisión (si baja, la feature está funcionando)
>
> ⚠️ **Aviso:** "vistas de la gráfica" es una métrica tentadora por ser fácil de medir,
> pero en un negocio de productividad no predice retención — alguien puede mirarla y
> seguir sin decidir nada.

**Recomendación final:**
> Presentar la North Star (decisiones tomadas) como la métrica de éxito de la feature ante
> el equipo, no las vistas — es la que resistiría el escrutinio de alguien de datos o PM.
