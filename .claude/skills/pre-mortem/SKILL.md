---
name: pre-mortem
description: >-
  Estresa un plan o PRD ya escrito buscando qué suposiciones lo sostienen y qué haría que
  cada una fallara, clasificando cada riesgo como Tiger (real, probable, urgente), Paper
  Tiger (parece grave pero no lo es) o Elephant (grande y lento, todo el mundo lo sabe pero
  nadie lo aborda). Úsala sobre un PRD (`write-prd`) o plan de lanzamiento ya escrito, antes
  de comprometer el trabajo, para evitar tratar todos los riesgos con la misma urgencia.
---

# Pre-Mortem — Tigers / Paper Tigers / Elephants

> Fuente: [phuryn/pm-skills — pm-execution](https://github.com/phuryn/pm-skills)

Estresa un plan o PRD ya escrito, buscando las suposiciones que lo sostienen ("load-bearing
assumptions") y qué haría que cada una fallara — pero, a diferencia de un análisis de
riesgo genérico, clasifica cada hallazgo en tres tipos para evitar el error más común: tratar
todos los riesgos con la misma urgencia.

## La clasificación

- **🐅 Tiger** — riesgo real, probable y urgente. Si no se atiende, puede tumbar el plan
  pronto.
- **📄 Paper Tiger** — da miedo pero no es realmente una amenaza; la gente le dedica
  energía desproporcionada a algo que probablemente no va a pasar o que ya está mitigado.
- **🐘 Elephant** — el "elefante en la habitación": algo grande y lento que todo el mundo
  sabe que existe pero nadie aborda directamente, porque no es urgente hoy pero acabará
  siendo enorme si se ignora indefinidamente.

Cada riesgo termina con el **test más barato** para comprobar si es real, no solo con la
preocupación anotada sin acción.

## Cuándo se activa

Isabel tiene un PRD (`write-prd`) o plan de lanzamiento ya escrito y quiere estresarlo
antes de comprometer trabajo sobre él. También si pide explícitamente `/pre-mortem
[plan o PRD]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Hay algo del plan que ya genere inquietud, aunque no esté claro si es real o exagerado?

**2. Identifica las suposiciones que sostienen el plan** — especialmente las ya marcadas
con ⚠️ en un PRD existente, si lo hay.

**3. Clasifica cada una** en Tiger / Paper Tiger / Elephant, explicando por qué encaja en
esa categoría y no en otra — no asumas que todo lo que preocupa a Isabel es
automáticamente un Tiger.

**4. Para cada Tiger, propone el test más barato posible** para confirmar o descartar el
riesgo cuanto antes.

**5. Termina priorizando qué Tiger atacar primero** — los Paper Tigers y Elephants se
mencionan mencionan pero no compiten por atención inmediata con los Tigers.

## Ejemplo

**Isabel escribe:**
> `/pre-mortem` el PRD de comparación de campañas que ya escribimos con write-prd

**Preguntas antes de construir:**
> Antes del análisis, dime: ¿hay algo del plan que ya te genere inquietud, aunque no
> sepas si es real o exagerado?

**Isabel responde:**
> Me preocupa que ingeniería tarde más de lo esperado por la suposición de formato de
> datos que dejamos marcada con ⚠️ en el PRD.

**Output final:**

> **🐅 Tiger:** la suposición de formato de datos (⚠️ del PRD) sin confirmar con
> ingeniería — si es falsa, retrasa el proyecto entero. Real, probable, urgente.
>
> **📄 Paper Tiger:** "la gente no va a entender la comparación" — suena a riesgo serio,
> pero ya se validó indirectamente en `evaluate` y `test-plan` con severidad baja; no
> merece más atención de la que ya tiene.
>
> **🐘 Elephant:** el sistema de tokens de diseño (`tokenize`) aún no está aplicado a los
> componentes de gráfica — nadie lo ha priorizado, no bloquea este lanzamiento, pero cada
> feature nueva de gráficas seguirá acumulando deuda visual hasta que se aborde.

**Recomendación (test más barato por riesgo):**
> 🐅 Confirmar el formato de datos con ingeniería esta semana (coste: una pregunta en
> Slack) — es el único de los tres que puede tumbar el plan a corto plazo.
