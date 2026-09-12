---
name: opportunity-solution-tree
description: >-
  Construye un Opportunity Solution Tree (Teresa Torres) de 4 niveles — outcome →
  oportunidades → soluciones → experimentos — para que cada feature o idea se pueda trazar
  hacia arriba hasta un resultado medible real, en vez de existir sola sin justificación.
  Úsala cuando Isabel tenga varias oportunidades sueltas (de `journey-map`,
  `layers-user-needs`, `layers-observed-behaviour`) y quiera organizarlas contra un objetivo
  común, o cuando parta de una solución/idea concreta (un rediseño visual, una feature) y
  quiera comprobar honestamente si responde a una oportunidad real o es solo gusto/intuición
  sin validar.
---

# Opportunity Solution Tree — de una idea suelta a un árbol trazable

> Fuente: [phuryn/pm-skills — pm-product-discovery](https://github.com/phuryn/pm-skills)

Herramienta central de Teresa Torres (*Continuous Discovery Habits*). La idea: cada feature
que se construye debería poder trazarse, rama por rama, hasta un outcome medible. Si no se
puede dibujar esa línea, probablemente se está construyendo algo porque "suena bien", no
porque de verdad mueva ningún resultado.

Se empareja bien con `layers-user-needs` (que genera las oportunidades sueltas que aquí se
organizan) y con `journey-map` / `layers-observed-behaviour` (otras fuentes de
oportunidades).

## Los 4 niveles

1. **Outcome** — el objetivo real, una métrica o resultado medible (no una feature). Ej:
   "el equipo de marketing decide más rápido qué campañas repetir".
2. **Opportunities** — necesidades, dolores o deseos del usuario que, si se resuelven,
   mueven ese outcome. Pueden ramificarse en sub-oportunidades.
3. **Solutions** — ideas concretas para atacar cada oportunidad. Varias por oportunidad,
   nunca una sola.
4. **Experiments** — la forma más barata de validar cada solución antes de construirla
   entera.

## Cuándo se activa

Isabel tiene varias oportunidades sueltas (de `journey-map`, `layers-user-needs`,
`layers-observed-behaviour`) y quiere organizarlas contra un mismo outcome para decidir qué
atacar primero. También cuando parte de una **solución** ya pensada (un rediseño visual,
una feature concreta) y quiere comprobar honestamente si responde a una oportunidad real o
es una corazonada de diseño sin validar — este es el uso "hacia atrás" del árbol.

## Paso 0 — Encontrar el outcome cuando no está claro

No des por hecho que Isabel ya tiene un business outcome definido — si no tiene experiencia
en estrategia de producto, ayúdala a llegar a uno en vez de pedírselo como requisito
previo. Pregunta, en este orden:

- "¿Qué número, si subiera, haría que alguien dijera 'esto va bien'? (usuarios que vuelven,
  tiempo hasta decisión, campañas repetidas con éxito, tickets resueltos sin escalar...)"
- "Si tu manager o stakeholder solo pudiera mirar una métrica dentro de 3 meses, ¿cuál
  sería?"

Si aun así no sale nada claro, ofrece 2-3 outcomes candidatos típicos según el tipo de
producto o feature del que se trate, para que ella elija en vez de partir de cero — no la
dejes bloqueada sin un punto de partida.

Un outcome siempre es una **métrica o resultado medible**, nunca una feature ("decide más
rápido qué campaña repetir" vale; "tener un dashboard de campañas" no vale — eso es una
solución, no un outcome).

## Cómo construirlo

**Caso 1 — Empezando por el outcome (hacia abajo):**
Con el outcome ya identificado (Paso 0), cuelga las oportunidades ya
identificadas debajo, y para cada una genera varias soluciones (nunca una sola), y para la
solución prioritaria, un experimento barato.

**Caso 2 — Empezando por una solución ya pensada (hacia atrás):**
Cuando Isabel trae una idea concreta (ej. "quiero iterar el estilo de esta gráfica para que
sea más atractiva"), no la descartes ni la aceptes sin más — hazla subir por el árbol:

1. Pregunta a qué oportunidad responde. Si no hay ninguna verbalizada o evidenciada, dilo
   explícitamente — es una señal real, no un bloqueo.
2. Si no hay oportunidad clara, ofrece colgarla como **hipótesis sin validar** (marcada
   como tal, nunca como si fuera una oportunidad confirmada) en vez de descartar la idea.
3. Diseña el experimento más barato para comprobar esa hipótesis antes de invertir en
   construir la solución completa — no le digas a Isabel "no lo hagas por gusto", ayúdala a
   ser honesta sobre si es corazonada o evidencia, y a validarlo barato si es corazonada.

No fuerces cada rama a tener exactamente el mismo número de niveles rellenos — una
oportunidad puede quedarse sin solución todavía, o una solución sin experimento diseñado
si Isabel solo quiere ver el mapa general primero.

## Ejemplo — construyendo hacia abajo con oportunidades ya identificadas

**Outcome:** *"El equipo de marketing decide más rápido qué campañas repetir"*

```
Outcome: el equipo decide más rápido qué campañas repetir
│
├── Opportunity: "no está claro qué eje es cuál" (de layers-observed-behaviour)
│   ├── Solution: etiquetar ejes con claridad
│   └── Solution: tooltip con el valor exacto al pasar el cursor
│
├── Opportunity: "no hay forma fácil de comparar dos campañas" (del journey-map)
│   ├── Solution: vista de comparación lado a lado
│   │   └── Experiment: mockup estático de comparación, enseñado a 2-3 personas del equipo
│
└── Opportunity (hipótesis, inferida): "prefieren barras a líneas para comparar"
    └── Solution: opción de cambiar entre barras y líneas
```

## Ejemplo — trabajando hacia atrás desde una solución

Isabel: *"quiero iterar el estilo visual de la gráfica de campañas, hacerla más
atractiva."*

```
Outcome: el equipo decide más rápido qué campañas repetir
│
└── Opportunity (hipótesis, sin validar): "la gráfica actual no transmite suficiente
    claridad/confianza como para decidir rápido, y por eso tarda más de lo necesario"
    ├── Solution: rediseño visual de estilo
    └── Experiment: enseñar la versión actual vs. un mockup nuevo a 2-3 personas del
        equipo y preguntar cuál les ayuda a decidir más rápido, antes de invertir en
        el rediseño completo
```

La utilidad aquí no es bloquear la idea — es que Isabel decida con los ojos abiertos si
invierte en el rediseño directamente o valida primero la hipótesis que lo sostiene.
