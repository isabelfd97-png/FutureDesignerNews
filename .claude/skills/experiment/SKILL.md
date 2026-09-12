---
name: experiment
description: >-
  Diseña un experimento A/B de principio a fin — hipótesis (Si hacemos X, entonces Y,
  porque Z), variantes, métrica principal, y guía de tamaño de muestra necesario para
  significancia estadística. Úsala cuando un cambio se pueda medir cuantitativamente a
  escala y haya tráfico/usuarios suficientes para un test válido. Avisa explícitamente
  cuando el volumen disponible no da para una conclusión fiable, en vez de dejar correr un
  test cuyo resultado sería ruido, no señal.
---

# Experiment — diseño de A/B test con rigor estadístico

> Fuente: [Owl-Listener/designer-skills — prototyping-testing](https://github.com/Owl-Listener/designer-skills/tree/main/prototyping-testing)

Diseña un experimento A/B real, no solo "probemos dos versiones a ver cuál gusta más". El
error más común sin formación en experimentación es correr un test con poco tráfico y sacar
conclusiones de ahí — prácticamente tirar una moneda. Esta skill avisa explícitamente
cuando el volumen disponible no alcanza para un resultado fiable.

## Qué define

- **Hipótesis** — en formato "Si hacemos X, entonces Y cambiará, porque Z" — nunca "vamos a
  probar esto a ver qué pasa".
- **Variantes** — qué cambia exactamente entre A y B. Una sola variable a la vez; si
  cambian varias cosas de golpe, no se sabrá cuál causó el efecto.
- **Métrica principal** — la que decide qué variante gana. Idealmente conectada a la North
  Star o a un input metric ya definido (`north-star-metric`), no una métrica inventada
  para la ocasión.
- **Tamaño de muestra** — cuánto tráfico/usuarios y cuánto tiempo hace falta para que el
  resultado sea estadísticamente válido, no ruido.

## Cuándo se activa

Isabel quiere probar un cambio que se puede medir cuantitativamente a escala (no una
opinión subjetiva de "gusta más"), y hay volumen de usuarios real para plantearse un A/B.
También si pide explícitamente `/experiment [cambio a probar]`.

Si el cambio es más cualitativo o de bajo volumen de usuarios, esta skill debe señalar que
un A/B no es la herramienta adecuada y sugerir una alternativa (test de usabilidad
pequeño, prueba cualitativa) en vez de forzar el formato.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Cuántos usuarios usan esta parte del producto aproximadamente por semana?
- ¿Qué métrica se usaría para decidir qué variante ganó?

**2. Construye la hipótesis en el formato Si/Entonces/Porque**, las variantes (solo una
variable cambiada), y la métrica principal.

**3. Calcula o estima la guía de tamaño de muestra** con el volumen de tráfico aportado —
si el tráfico es bajo, dilo explícitamente con un ⚠️ y da una estimación realista de cuánto
tiempo haría falta correr el test.

**4. Si el volumen no alcanza para un resultado fiable en un plazo razonable, recomienda
una alternativa cualitativa** en vez de sugerir correr el A/B de todos modos.

## Ejemplo

**Isabel escribe:**
> `/experiment` quiero probar si mover la leyenda debajo de la gráfica (en vez de al lado)
> mejora la comparación de campañas

**Preguntas antes de construir:**
> Antes de diseñar el experimento, dime:
> - ¿Cuántos usuarios usan esta pantalla de comparación aproximadamente por semana?
> - ¿Qué métrica usarías para decidir quién ganó — tiempo hasta decisión, tasa de
>   abandono, otra?

**Isabel responde:**
> Unos 200 usuarios activos por semana la usan. Usaría el tiempo hasta que toman la
> decisión de repetir/no repetir.

**Output final:**

> **Hipótesis:** Si movemos la leyenda debajo de la gráfica (en vez de al lado), entonces
> el tiempo hasta decisión bajará, porque libera espacio horizontal para leer mejor la
> tendencia en pantallas pequeñas.
>
> **Variantes:** A (leyenda lateral, actual) / B (leyenda debajo)
>
> **Métrica principal:** tiempo medio hasta decisión (ya identificado como input metric en
> `north-star-metric`)
>
> ⚠️ **Aviso de tamaño de muestra:** con ~200 usuarios/semana y un efecto esperado
> moderado, necesitarías aproximadamente 3-4 semanas corriendo el test para tener
> significancia estadística razonable. Con menos tiempo, el resultado no sería fiable —
> cualquier diferencia podría ser ruido, no un efecto real.

**Recomendación final:**
> Si no se puede esperar 3-4 semanas, considerar un test cualitativo más pequeño
> (`test-scenario` o una prueba de usabilidad con 5 personas) en vez de un A/B — con este
> volumen de tráfico, un A/B rápido no daría un resultado en el que confiar.
