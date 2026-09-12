---
name: write-prd
description: >-
  Genera un PRD (Product Requirements Document) completo de 8 secciones — resumen,
  contactos, contexto, objetivo, segmento de mercado, propuesta de valor, solución (con
  suposiciones marcadas explícitamente) y release — a partir de una idea de feature o un
  problem statement. Úsala cuando Isabel necesite formalizar una feature para que un equipo
  (o un agente de IA) la construya, especialmente porque un PRD ambiguo hoy se traduce
  directamente en código con la ambigüedad ya resuelta, y no siempre bien.
---

# Write PRD — documento de requisitos de producto de 8 secciones

> Fuente: [phuryn/pm-skills — pm-execution](https://github.com/phuryn/pm-skills)

Genera un PRD completo a partir de una idea de feature o un problem statement (puede venir
directamente de `frame-problem`). El argumento central: cuando el código se construye cada
vez más con agentes de IA a partir de una spec, la calidad del PRD determina directamente
la calidad de lo construido — un PRD ambiguo ya no solo confunde a un ingeniero que puede
preguntar, se traduce en código con la ambigüedad resuelta (mal) por el agente sin que
nadie lo note hasta después. Mismo principio que `frame-problem` y
`layers-conceptual-model`, llevado al documento formal completo.

## Las 8 secciones

1. **Resumen** — 2-3 frases de qué trata el documento.
2. **Contactos** — stakeholders clave, rol y comentarios relevantes.
3. **Contexto** — por qué importa esto ahora, qué cambió para que sea posible.
4. **Objetivo** — propósito, beneficio de negocio, métricas de éxito en formato SMART/OKR.
5. **Segmento de mercado** — a quién va dirigido, definido por problema/job, no por
   demografía.
6. **Propuesta de valor** — jobs que resuelve, ganancias, dolores evitados,
   diferenciación (puede conectar con `value-proposition`).
7. **Solución** — enfoque técnico: UX/prototipos, descripción de features, y
   **suposiciones marcadas explícitamente**, nunca coladas como hechos.
8. **Release** — cronograma relativo, qué va en la primera versión vs. futuras
   iteraciones.

## Cuándo se activa

Isabel necesita formalizar una feature para que un equipo (o un agente de IA) la
construya, con las 8 secciones completas. También si pide explícitamente `/write-prd
[idea o problem statement]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Quiénes son los stakeholders clave (nombres/roles)?
- ¿Hay una fecha o urgencia real, o el timeline es flexible?

**2. Construye las 8 secciones**, reutilizando lo que ya exista de otras skills
(`frame-problem` para contexto/objetivo, `value-proposition` para la sección 6,
`north-star-metric` para conectar el objetivo a una métrica real) en vez de reescribirlo
desde cero.

**3. En la Sección 7 (Solución), marca con ⚠️ cada suposición técnica o de producto que no
esté confirmada** — nunca presentarlas con el mismo peso que un hecho verificado.

**4. Termina recomendando qué ⚠️ confirmar antes de considerar el PRD final**, priorizando
la que más cambiaría el alcance si resultara falsa.

## Ejemplo

**Isabel escribe:**
> `/write-prd` la feature de comparación automática de campañas — partiendo del problem
> statement que hicimos con frame-problem

**Preguntas antes de construir:**
> Antes del PRD completo, dime:
> - ¿Quiénes son los stakeholders clave de esto (nombres/roles)?
> - ¿Hay ya una fecha o urgencia real, o el timeline es flexible?

**Isabel responde:**
> Stakeholders: yo (diseño), un PM, dos ingenieros. No hay fecha fija, pero se quiere para
> el próximo trimestre.

**Output final** (resumido):

> 1. Resumen — [2-3 frases]
> 2. Contactos — Isabel (diseño), [PM], [ingenieros]
> 3. Contexto — [de frame-problem: dolor del proceso manual en Excel]
> 4. Objetivo — [conectado a North Star si existe]
> 5. Segmento — equipo de marketing que gestiona campañas activamente
> 6. Propuesta de valor — [de value-proposition si existe, o construida aquí]
> 7. Solución — ⚠️ **Suposición marcada:** se asume que los datos de ambas campañas están
>    siempre en el mismo formato; no confirmado con ingeniería.
> 8. Release — próximo trimestre, primera versión sin normalización de periodos
>    distintos (fase 2)

**Recomendación final:**
> Confirmar con ingeniería la suposición ⚠️ de la Sección 7 antes de que el PRD se
> considere final — es la que más cambiaría el alcance de la primera versión si resulta
> falsa.
