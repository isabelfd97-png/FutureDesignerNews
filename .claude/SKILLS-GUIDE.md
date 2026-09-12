# Guía de skills de diseño/producto — de la idea al cierre

Todas las skills revisadas y aprobadas en la sesión de revisión de septiembre 2026,
ordenadas por en qué punto del trabajo se usan. Cada una vive en `.claude/skills/<nombre>/SKILL.md`
con su explicación y ejemplo completo — esta guía es solo el mapa para localizarlas rápido.

---

## 0. Diagnóstico inicial — "no sé por dónde empezar"

**layers-orient** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Audita un proyecto en 7 capas (estrategia → superficie visual) y señala en cuál está el
verdadero cuello de botella, antes de tocar nada visual.
*Ejemplo:* "quiero iterar el estilo de esta gráfica" → el diagnóstico revela que el problema
real es que no se decidió si la gráfica muestra tendencia o comparación (capa 3, no capa 7).

---

## 1. Descubrimiento e investigación — entender el problema y a quién afecta

**layers-user-needs** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Convierte una idea vaga en job stories priorizadas ("Cuando..., quiero..., para poder...").
*Ejemplo:* "quiero crear una gráfica nueva" → sale con 2-3 job stories y una lista de
oportunidades priorizadas por accionabilidad.

**layers-observed-behaviour** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Igual que la anterior pero desde notas/comentarios reales, marcando confianza
(🟢 Observado / 🟡 Inferido / 🔴 Asumido).

**layers-domain** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Cosecha el vocabulario real de conversaciones de equipo y detecta dónde PM/diseño/
ingeniería usan la misma palabra para cosas distintas.

**synthetic-persona** — traída del segundo cerebro de Isabel (no es de las 4 colecciones)
Construye una persona sintética fundamentada en investigación real (o marcada como
suposición si no la hay), con entrevista guiada de 9 áreas y una fase para "hablar" con ella.

**journey-map** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-research)
Mapa de recorrido con etapas/emociones/dolores + fila de oportunidades accionables (lo que
la mayoría de journey maps se saltan).

**discover** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Ciclo completo: ideación → suposiciones (Valor/Usabilidad/Viabilidad/Factibilidad) →
priorización → experimento más barato.

**interview** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Dos modos: Prep (guion de entrevista JTBD) y Summarize (transcripción → job real, señales
de satisfacción/frustración, acciones).

**test-plan** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-research)
Plan de test de usabilidad completo: reclutamiento, tareas orientadas a objetivo (no
dirigidas), criterio de éxito definido antes, guía de facilitación.

---

## 2. Estrategia y priorización — decidir qué construir y por qué

**frame-problem** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/ux-strategy)
Convierte un encargo ambiguo ("rediseñar X") en un problem statement con quién, qué, por
qué importa, y criterio de éxito.

**opportunity-solution-tree** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Árbol outcome → oportunidades → soluciones → experimentos (Teresa Torres). Incluye un
Paso 0 para encontrar el outcome de negocio cuando no hay experiencia previa en estrategia.

**north-star-metric** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Define la métrica única que mejor captura el valor real entregado, clasificando el negocio
en "juego" (atención / transacción / productividad) antes de elegir la métrica.

**value-proposition** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Propuesta de valor en 6 partes JTBD (Who/Why/What before/How/What after/Alternatives), con
énfasis en el contraste antes/después.

**identify-assumptions-existing** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Audita algo YA decidido contra las 4 categorías de riesgo de Marty Cagan, sin pasar por un
discovery completo.

**strategy** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Product Strategy Canvas completo de 9 secciones (visión → defensibilidad). Uso poco
frecuente, para decisiones de negocio grandes.

**market-scan** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
SWOT + PESTLE + Porter's Five Forces + Ansoff Matrix combinados. Para momentos de alto
impacto: defender una inversión, entrar en una reunión de planificación, o una entrevista
de trabajo.

---

## 3. Modelo conceptual — decidir qué es cada cosa antes de diseñar pantallas

**layers-conceptual-model** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Define objetos, relaciones, estados y vocabulario por escrito, sin ninguna interfaz
todavía — evita que un equipo discuta "qué es esto" mirando la misma pantalla.

---

## 4. Flujo e interacción — cómo se mueve el usuario, antes de diseñar visualmente

**layers-interaction-flow** — [jamiemill/layers-skills](https://github.com/jamiemill/layers-skills)
Breadboarding (Shape Up): lugares, affordances y conexiones, sin ningún diseño visual, con
caminos de fallo y decisiones abiertas marcadas.

**map-states** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/interaction-design)
Máquina de estados formal de un componente: estados, eventos, guards — con foco en los que
se olvidan (loading, empty, error, partial, offline).

**error-flow** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/interaction-design)
Diseña qué le pasa al usuario cuando algo falla: prevención, detección, mensaje,
recuperación — no solo detecta que puede fallar.

---

## 5. Especificación para construir — el puente hacia ingeniería

**create-component** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)
Spec completa y reutilizable de un componente (props, variantes, estados, accesibilidad,
edge cases) para que viva en una librería. Distinta de `design-handoff`: esta es el
componente en abstracto, no una pantalla concreta.

**tokenize** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)
Extrae colores/espaciados/tipografías escritos "a pelo" en código real y los organiza en
design tokens con nombre y estructura.

**write-prd** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
PRD completo de 8 secciones (resumen → release) a partir de una idea o problem statement,
con suposiciones siempre marcadas explícitamente.

**handoff** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-ops)
Spec de handoff + checklist de QA para verificar DESPUÉS de la implementación. La parte de
checklist es lo nuevo frente a `design-handoff`.

---

## 6. Validación — comprobar antes de lanzar

**evaluate** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/prototyping-testing)
Evaluación heurística de Nielsen (10 principios), con severidad 0-4. Más barato que un
test de usabilidad real, no lo sustituye del todo.

**cognitive-load-assessment** — [owl-listener/inclusive-design-skills](https://github.com/owl-listener/inclusive-design-skills/tree/main/cognitive-accessibility)
Evalúa memoria/atención/complejidad de decisión de un flujo, distinguiendo carga
intrínseca (inevitable) de extrínseca (evitable por diseño).

**cognitive-accessibility-review** — [owl-listener/inclusive-design-skills](https://github.com/owl-listener/inclusive-design-skills/tree/main/cognitive-accessibility)
Revisión completa en 6 dimensiones (incluye carga cognitiva + lenguaje + wayfinding +
errores + foco + memoria). El listón: ¿puede alguien cansado y sin familiaridad completar
la tarea sin ayuda?

**responsive-audit** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/ui-design)
Audita layout/touch targets/reflow en cada breakpoint — abre y redimensiona de verdad si
hay una página real que probar.

**benchmark** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/ux-strategy)
Compara cómo resuelven competidores un patrón concreto, con tabla y gap analysis. Necesita
capturas reales — no inventa cómo se ve una app que no se ha visto.

**audit-system** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/design-systems)
Audita un sistema de diseño en consistencia/coverage/accesibilidad, priorizado por
severidad — output listo como agenda de reunión de migración.

**experiment** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/main/prototyping-testing)
Diseña un A/B test (hipótesis/variantes/métrica/tamaño de muestra), avisando si no hay
tráfico suficiente para un resultado fiable.

**pre-mortem** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Estresa un plan/PRD ya escrito, clasificando riesgos en Tigers (reales y urgentes), Paper
Tigers (parecen graves y no lo son), Elephants (grandes, lentos, todos lo saben y nadie lo
aborda).

---

## 7. Lanzamiento y medición

**analyze-test** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Analiza resultados de un A/B ya corriendo: significancia, tamaño de muestra alcanzado, y
recomendación Ship / Extend / Stop.

---

## 8. Proceso de equipo y cierre

**retro** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Retrospectiva estructurada (Start/Stop/Continue, 4Ls, o Sailboat) que siempre cierra con
2-3 acciones con responsable y plazo.

**summarize-meeting** — [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
Transcripción de reunión → discusión / decisiones / acciones (tabla) / preguntas abiertas.

**write-rationale** — [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills)
Escribe por qué se tomó una decisión, conectada a necesidad de usuario + objetivo de
negocio + principio de diseño — para que el criterio sobreviva más allá de la conversación.

---

## 9. Diseñar con IA — dos plugins completos

Documentados en `.claude/plugins/`, con sus skills asociadas en `.claude/skills/`.

### Plugin `model-interaction-design` — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)
Cómo se comportan las interacciones humano-IA: quién lidera, cómo se revela capacidad, qué
pasa ante un malentendido.
- 8 skills base (versión breve): `conversation-patterns`, `mixed-initiative-flow`,
  `progressive-disclosure`, `multimodal-orchestration`, `context-window-design`,
  `generative-ui`, `feedback-loops`, `frustration-detection`
- 3 comandos (ejemplo completo): `design-conversation`, `audit-interaction`,
  `map-initiative`

### Plugin `prompt-architecture` — [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)
Los prompts como superficie de producto: estructura, plantillas, restricciones, versionado.
- 7 skills base (versión breve): `system-prompt-structure`, `template-design`,
  `chain-of-thought-design`, `few-shot-patterns`, `constraint-specification`,
  `prompt-versioning`, `context-engineering`
- 3 comandos (ejemplo completo): `design-prompt`, `build-chain`, `audit-prompt`

---

## Descartadas en la revisión (no añadidas)

- `layers-observed-behaviour`-style duplicado: **empathy-map** — redundante con
  `layers-observed-behaviour`.
- **user-persona** (Owl-Listener) — ya cubierta, mejor, por `synthetic-persona`.
- **layers-product-strategy** — redundante con `opportunity-solution-tree`; se reforzó
  esta última con un Paso 0 en su lugar.
- **error-personality** — descartada sin motivo específico registrado.
