---
name: evaluate
description: >-
  Evaluación heurística clásica de Jakob Nielsen — revisión experta de un diseño contra
  los 10 principios de usabilidad (visibilidad del estado, consistencia, prevención de
  errores, reconocer antes que recordar...), con hallazgos puntuados en la escala de
  severidad de Nielsen (0 = no es problema, 4 = catástrofe de usabilidad). Úsala sobre
  capturas o un diseño real cuando Isabel quiera detectar problemas de usabilidad sin
  reclutar usuarios ni montar un test — más barato que un test de usabilidad real, aunque
  no lo sustituye del todo.
---

# Evaluate — evaluación heurística de Nielsen

> Fuente: [Owl-Listener/designer-skills — prototyping-testing](https://github.com/Owl-Listener/designer-skills/tree/main/prototyping-testing)

Evaluación heurística clásica (Jakob Nielsen, años 90, sigue siendo estándar). En vez de
traer usuarios reales a testear, se revisa el diseño contra 10 principios fijos de
usabilidad. Detecta gran parte de lo que detectaría un test de usabilidad real, por una
fracción del coste — útil como primera pasada antes de gastar presupuesto de research en un
test con usuarios de verdad, pero no lo sustituye del todo.

## Las 10 heurísticas de Nielsen

1. Visibilidad del estado del sistema
2. Correspondencia entre el sistema y el mundo real
3. Control y libertad del usuario
4. Consistencia y estándares
5. Prevención de errores
6. Reconocer antes que recordar
7. Flexibilidad y eficiencia de uso
8. Diseño estético y minimalista
9. Ayudar a reconocer, diagnosticar y recuperarse de errores
10. Ayuda y documentación

## Escala de severidad

- **0** — no es un problema real
- **1** — problema cosmético, arreglar si sobra tiempo
- **2** — problema menor, baja prioridad
- **3** — problema mayor, prioridad alta de arreglar
- **4** — catástrofe de usabilidad, bloqueante antes de lanzar

## Cuándo se activa

Isabel tiene capturas o un diseño real (no una idea abstracta) y quiere detectar problemas
de usabilidad sin reclutar usuarios ni montar un test. También si pide explícitamente
`/evaluate [pantalla o flujo]`.

Necesita material real que evaluar (capturas, código navegable) — igual que `benchmark`, no
inventa el diseño, lo evalúa.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Se evalúan las 10 heurísticas completas, o hay alguna que preocupe más en concreto?
- ¿Hay algún estándar propio del producto, más allá de Nielsen, que también deba
  respetarse?

**2. Revisa el material contra cada heurística relevante**, describiendo el hallazgo
concreto (no "falta consistencia", sino qué elemento exacto rompe qué patrón).

**3. Puntúa cada hallazgo con la escala de severidad** (0-4).

**4. Si algún hallazgo coincide con algo ya detectado por otra skill** (`cognitive-load-assessment`, `error-flow`), señálalo como tal en vez de tratarlo como un hallazgo nuevo aislado.

**5. Termina priorizando qué severidad 3-4 resolver antes del lanzamiento.**

## Ejemplo

**Isabel escribe:**
> `/evaluate` la pantalla de comparación de campañas, aquí tienes las capturas:
> [pega/adjunta]

**Preguntas antes de construir:**
> Antes de la evaluación, dime:
> - ¿Quieres las 10 heurísticas completas, o alguna te preocupa más en concreto?
> - ¿Hay algún estándar propio de vuestro producto (más allá de Nielsen) que también deba
>   respetar?

**Isabel responde:**
> Las 10 completas está bien. No hay estándar propio más allá de lo general.

**Output final:**

> | Heurística | Hallazgo | Severidad |
> |---|---|---|
> | Visibilidad del estado | No hay indicador de "cargando" mientras llega la segunda
> campaña | 3 — problema mayor, confunde si está cargando o roto |
> | Reconocer antes que recordar | El usuario debe recordar el resultado de la campaña
> anterior (mismo hallazgo que `cognitive-load-assessment`) | 3 |
> | Consistencia | El botón "Comparar" usa el color naranja de marca, pero "Cerrar" usa el
> mismo naranja en otra pantalla del sistema | 2 — inconsistencia menor pero confunde
> jerarquía |
> | Prevención de errores | No hay aviso antes de comparar rangos de fechas muy distintos | 3 |

**Recomendación final:**
> Los dos hallazgos con severidad 3 (indicador de carga, prevención de rangos distintos)
> son los que priorizaría antes del lanzamiento — severidad 4 sería bloqueante total, y no
> hay ninguno de ese nivel aquí.
