---
title: El loop de 2 niveles para que Claude deje de autopuntuarse su propio diseño
url: https://www.linkedin.com/posts/carmenerincon_hey-designers-todays-is-a-slightly-share-7483122441939058688-KocS
section: claude
subsection: Evaluación de diseño con Claude Code
date_added: 2026-07-15
---

## De qué va
Carmen Rincon (co-fundadora de Yummy Labs, la misma fuente de los artículos que ya tienes sobre dónde va tu contexto en Claude y por qué los diseñadores gastan su límite de uso más rápido) explica un problema muy concreto: pedirle a Claude que revise el propio diseño que acaba de generar no funciona, porque cuando evalúa su propio trabajo lo defiende. Lee lo que *quiso* construir, no lo que realmente hay en pantalla — es el mismo motivo por el que no puedes corregir bien tu propio texto recién escrito. Tiene nombre: sesgo de autopreferencia (self-preferential bias).

La diferencia de puntuación que midió en un proyecto real de cliente es la prueba: Claude se puntuó a sí mismo un 75 sobre 100 en una pantalla; un panel ciego que no había construido esa pantalla puntuó exactamente el mismo trabajo un 52. 23 puntos de diferencia sobre lo mismo.

## El loop de dos niveles en Claude Code
**Nivel 1 — el panel de críticos.** En vez de que el mismo Claude que construyó la pantalla la revise, se lanzan varios agentes críticos separados, cada uno en su propio contexto (así ninguno ha visto el proceso de construcción y no puede defenderlo). Cada agente es dueño de una única lente:
- craft + marca + fidelidad
- UX + accesibilidad + motion
- tokens + código + contenido
- oportunidad / mejora

Puntúan a ciegas contra una rúbrica — y aquí está el truco que casi nadie hace: la rúbrica se pondera hacia lo que Claude hace *peor*, no hacia lo que ya hace bien. Layout y viabilidad técnica ya se le dan razonablemente bien, así que pesan menos; gusto, coherencia y craft son sus puntos débiles, así que pesan más. Eso es lo que convierte la revisión en algo útil de verdad, en vez de un halago disfrazado de evaluación.

**Nivel 2 — la memoria.** Los fallos detectados en el panel se guardan y se recargan cada sesión nueva, así Claude deja de repetirlos: los mismos fallos de contraste, los mismos colores fuera del sistema, el mismo error de spacing no vuelven a aparecer. La siguiente pantalla arranca más alto, y la puntuación sube de loop en loop en vez de resetear cada vez que empiezas una sesión nueva.

## Por qué le importa a un product designer
Este panel de críticos es, en el fondo, el mismo patrón de subagentes que ya viste en el artículo de 'Claude Agents': un trabajo con un objetivo claro, herramientas acotadas (aquí, de solo lectura — mirar y puntuar, nunca tocar) y límites bien definidos, aplicado en concreto a resolver el problema de que nadie se marca bien sus propios deberes. La idea de que la rúbrica debe pesar más hacia los puntos débiles del modelo, no hacia los fuertes, es aplicable más allá de este caso: cualquier sistema de revisión (humano o IA) es más útil cuando se diseña para encontrar lo que de verdad se le escapa a quien construyó, no para confirmar lo que ya sabía hacer bien.

## Ideas clave
- No dejes que Claude revise su propio trabajo: lo defiende por sesgo de autopreferencia, igual que tú no puedes corregir bien tu propio texto recién escrito.
- Diferencia medida en un proyecto real: 75/100 autopuntuado vs. 52/100 por un panel ciego — 23 puntos de distancia sobre el mismo trabajo.
- Nivel 1: agentes críticos separados, cada uno en su propio contexto y con una sola lente, puntuando a ciegas contra una rúbrica ponderada hacia los puntos débiles del modelo.
- Nivel 2: los fallos se guardan y se recargan cada sesión, así la puntuación mejora acumulativamente en vez de resetear.
- Es el mismo patrón de subagentes de 'Claude Agents', aplicado a que nadie se corrija bien sus propios deberes.

## Para aprender
- **Sesgo de autopreferencia (self-preferential bias)**: La tendencia a valorar mejor algo que tú mismo has hecho, porque cuando lo revisas recuerdas la intención con la que lo construiste, no solo lo que realmente quedó. Es la razón por la que revisar tu propio trabajo (de texto, de código, o de diseño) da resultados más generosos que cuando lo revisa alguien que no lo construyó.
- **Evaluación ciega (blind review)**: Un proceso de revisión donde quien evalúa no sabe (o no ha visto) quién o cómo se construyó lo que está puntuando, para que no pueda inclinarse a favor de ello. En este caso, los agentes críticos evalúan la pantalla sin haber participado en construirla, así puntúan desde cero en vez de simplemente confirmar el trabajo.

---
Artículo original: https://www.linkedin.com/posts/carmenerincon_hey-designers-todays-is-a-slightly-share-7483122441939058688-KocS
