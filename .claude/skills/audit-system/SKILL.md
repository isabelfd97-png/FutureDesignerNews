---
name: audit-system
description: >-
  Audita un sistema de diseño real (componentes, tokens, documentación) en tres ejes —
  consistencia, completitud (coverage) y accesibilidad — y devuelve los hallazgos
  priorizados por severidad, listos para usarse como agenda de una reunión de migración o
  version bump. Úsala cuando Isabel vaya a hacer un cambio grande a un sistema de
  componentes existente (migración de versión, unificación) y necesite saber qué está roto
  o incompleto antes de decidir el alcance del cambio.
---

# Audit System — auditoría de consistencia, coverage y accesibilidad

> Fuente: [Owl-Listener/designer-skills — design-systems](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)

Igual que `tokenize`, trabaja sobre código o documentación real de un sistema de diseño ya
existente, no sobre una idea nueva. Audita tres ejes:

- **Consistencia** — si los componentes siguen los mismos patrones entre sí, o cada uno
  reinventa su propia lógica (nombres de prop, estructura, comportamiento).
- **Completitud (coverage)** — si faltan estados, variantes o casos que deberían estar
  documentados (ej. un componente sin estado "disabled" o sin "empty state" definido).
- **Accesibilidad** — contraste, tamaños de target táctil, y otros criterios del estándar
  que se esté siguiendo (WCAG u otro).

El output está pensado para convertirse directamente en la **agenda de una reunión** de
migración o version bump, no como informe para archivar — por eso los hallazgos van
priorizados por severidad.

## Cuándo se activa

Isabel va a hacer un cambio grande a un sistema de componentes existente (migración de
versión, unificación de componentes duplicados) y necesita saber qué está roto o incompleto
antes de decidir el alcance del cambio. También si pide explícitamente
`/audit-system [componentes o sistema a auditar]`.

No la actives sin código o documentación real que auditar — no inventa un sistema desde
cero, evalúa uno que ya existe.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿El objetivo es preparar una migración concreta, o es una revisión de salud general sin
  cambio inminente?
- ¿Hay un estándar de accesibilidad concreto a cumplir (WCAG AA, una normativa del sector),
  o se audita contra el estándar general?

**2. Audita los tres ejes** sobre el código/documentación aportado, siendo específica: no
"falta consistencia", sino qué componentes exactos usan convenciones distintas para lo
mismo, y en qué.

**3. Prioriza cada hallazgo por severidad:**
- 🔴 Bloqueante — debe resolverse antes de la migración/cambio, o se lanza con una
  regresión real.
- 🟡 Importante — conviene resolverlo, pero no bloquea el lanzamiento.
- ⚪ Mejora menor — cosmético, sin urgencia.

**4. Cierra recomendando qué bloque llevar como punto obligatorio a la próxima reunión.**

## Ejemplo

**Isabel escribe:**
> `/audit-system` antes de la v2 de nuestro sistema de componentes de gráficas, quiero
> auditarlo — aquí está el código de los 4 componentes de gráfica que tenemos: [pega
> código/enlaces]

**Preguntas antes de construir:**
> Antes de auditar, dos cosas:
> - ¿El objetivo es preparar la migración a v2, o es una revisión de salud general sin
>   cambio inminente?
> - ¿Hay algún estándar de accesibilidad concreto que debáis cumplir (WCAG AA, alguna
>   normativa de vuestro sector), o auditamos contra el estándar general?

**Isabel responde:**
> Es para la migración a v2. Cumplimos WCAG AA como estándar general de la empresa.

**Output final:**

> **🔴 Bloqueante para v2:**
> - El componente `LineChart` no tiene versión con contraste suficiente para modo oscuro
>   (ratio 2.1:1, WCAG AA pide 3:1 mínimo para elementos gráficos) — hay que resolver
>   antes de migrar, no después.
>
> **🟡 Importante, no bloqueante:**
> - `BarChart` y `LineChart` usan nombres de prop distintos para lo mismo
>   (`highlightColor` vs `accentColor`) — inconsistencia que confundirá a quien use ambos.
> - Ningún componente de gráfica tiene documentado qué pasa con datos vacíos (empty
>   state) — falta de coverage.
>
> **⚪ Mejora menor:**
> - Los tooltips de `PieChart` no siguen el mismo espaciado que el resto — cosmético, no
>   urgente.

**Recomendación final:**
> Llevar el bloque 🔴 como punto obligatorio de la reunión de migración — sin resolverlo,
> la v2 saldría con una regresión de accesibilidad. Los 🟡 pueden discutirse pero no
> bloquean el lanzamiento.
