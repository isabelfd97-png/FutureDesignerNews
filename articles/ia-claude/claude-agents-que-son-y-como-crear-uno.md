---
title: Claude Agents: qué son y cómo crear uno
url: https://yummy-design-sprint.notion.site/Claude-Agents-What-are-they-how-to-create-one-38e6279147098049a74ae0de250a51a1
section: ia-claude
subsection: Agentes de IA
date_added: 2026-07-12
---

## De qué va
Una guía de Yummy Labs pensada específicamente para diseñadores, sin dar por hecho ningún conocimiento técnico. La idea que explica todo el tema: un agente no es necesariamente algo técnico, es un trabajo que tú diseñas. Le das a Claude un objetivo, las herramientas para alcanzarlo y los límites para no salirse de madre, y él decide los pasos.

## La diferencia entre task, workflow y agente
La línea honesta que separa los tres es quién decide los pasos:

- **Task** — tú piensas los pasos, Claude hace uno. Ejemplo: "reescribe este texto de estado vacío".
- **Workflow** — tú programas la secuencia de pasos, Claude rellena cada uno. Ejemplo: "agrupa estas notas, luego mapéalas, luego resume".
- **Agente** — tú das el objetivo, Claude decide los pasos. Ejemplo: "revisa esta pantalla contra nuestro design system y señala qué se desvía".

¿Chatear con Claude es "usar un agente"? Normalmente no, eso es una task. Se convierte en agente en el momento en que entra en bucle: usa herramientas, lee sus propios resultados y decide qué hacer a continuación hacia el objetivo que le diste.

## Qué son realmente las 'herramientas' (tools)
Las herramientas son las manos y ojos del agente: lo que puede mirar y hacer.

- **Integradas en Claude Code**: leer un archivo, buscar dentro de archivos, encontrar archivos por patrón, modificar un archivo, ejecutar un comando (por ejemplo, hacer una captura de pantalla o correr tests).
- **Conectadas por MCP**: leer un frame de Figma o sus variables, leer y actualizar una página de Notion, redactar un email, consultar una base de datos.
- **Personalizadas**: cualquier función que definas tú, como crear un ticket o publicar en un CMS.

Qué herramientas le das a un agente es una decisión de diseño: un agente revisor recibe herramientas de solo lectura y nunca la de escribir, así puede mirar pero nunca tocar.

## Cómo diseñar un buen agente
Trátalo como el onboarding de un rol, no como escribir un prompt:

- **Un solo trabajo por agente.** Objetivo y límites claros; objetivo vago, agente vago.
- **Pocas herramientas, bien elegidas y bien descritas.** Más herramientas no es mejor.
- **Dale acceso a su propia verdad de campo**: que pueda leer su propio resultado (una captura, un test, un diff) para autocorregirse.
- **Acótalo y dale un límite de parada**, por ejemplo un número máximo de intentos.
- **Que sea transparente**: que muestre su plan, para que se entienda por qué hizo lo que hizo.

## Cuándo compensa un agente (y cuándo no)
Usa un agente cuando los pasos no se pueden mapear de antemano Y el resultado es verificable, y cuando merece la pena el coste extra de tiempo y tokens. Usa algo más simple —una task o un workflow— cuando ya sabes los pasos o cuando la velocidad y la predictibilidad importan más. La regla de Anthropic: busca lo más simple que funcione, y añade autonomía solo cuando mejora claramente el resultado.

## Las desventajas reales
Los agentes son más lentos y caros (exploran, y explorar gasta tokens), menos predecibles (el mismo input puede dar resultados distintos en cada ejecución) y los errores se acumulan en cada paso del bucle. Mitigaciones: mantenerlos de solo lectura cuando se pueda, poner a una persona en los puntos de control, probar en un entorno seguro y añadir límites de parada.

## Ocho agentes que puede construir un diseñador
Cada uno funciona porque la tarea necesita criterio, pero el resultado es verificable:

1. **Revisor de diseño** — compara una pantalla construida contra el design system y la referencia.
2. **Auditor de accesibilidad** — revisa contraste, tamaño de zonas táctiles, orden de foco, texto alternativo.
3. **Sintetizador de research** — convierte notas de entrevistas en temas y patrones.
4. **Revisor de copy y voz** — detecta microcopy que se sale de la guía de voz.
5. **Auditor de uso de componentes** — encuentra valores sueltos que deberían usar el sistema.
6. **Análisis competitivo** — dado un flujo, recopila cómo lo resuelven otros y resume patrones.
7. **Agente que construye pantallas** — construye una pantalla desde una spec y la va comparando y corrigiendo hasta que encaja (con una persona supervisando, porque edita archivos).
8. **Auditor de flujo** — recorre un prototipo contra una spec escrita y señala estados que faltan: vacío, cargando, error, éxito.

## Ejemplo completo: el revisor de diseño, cableado de principio a fin
Hay dos tipos de herramientas que le das a este agente. El primer cajón es su núcleo, integrado en Claude Code y sin tocar internet: leer archivos, buscar en el código, encontrar archivos, ejecutar comandos (capturas, diffs, tests de accesibilidad). El segundo cajón son los conectores (MCP), la parte que suele resultar confusa: Figma le deja comparar contra el frame real; Notion le deja leer una spec o escribir sus hallazgos; Linear/Jira le deja crear un ticket por cada problema; Slack le deja avisar al canal del equipo. Un conector se convierte en herramienta disponible en el momento en que lo activas en Ajustes.

El flujo típico: le describes el trabajo a Claude como si hicieras un brief a alguien nuevo en el equipo (qué herramientas tiene, cuál no —normalmente 'escribir'—, y qué cuenta como 'bien'), Claude guarda ese agente como un archivo dentro del proyecto, y luego lo invocas por su nombre cada vez que quieras que revise una pantalla. La misma base se puede reescribir para distintos trabajos con una frase extra y el conector correspondiente: comparar contra Figma, registrar en una base de Notion, crear tickets en Linear, avisar por Slack, o sumar una auditoría de accesibilidad.

## Por qué le importa a un product designer
Cuando un agente vive en el proyecto compartido del equipo, y no en el historial de chat de una persona, los criterios de revisión dejan de vivir solo en la cabeza del diseñador senior: quedan escritos, versionados y se aplican igual a todo el mundo. Escala el criterio de una persona en vez de depender de que esté en la sala, conecta diseño, producto e ingeniería (que viven en apps distintas) y elimina el cuello de botella de esperar a que la única persona que conoce el sistema tenga hueco. El aviso honesto: un agente conecta el trabajo, no sustituye la conversación — usado mal, cada uno se aísla con su propia IA en vez de hablar más.

## Para aprender
- **Subagente**: Un agente con un único trabajo, guardado como un pequeño archivo dentro de la carpeta oculta `.claude/agents/` de tu proyecto. No hace falta crearlo a mano: le describes el trabajo a Claude (qué herramientas tiene, qué no, qué cuenta como 'bien hecho') y él escribe el archivo. Una vez creado, lo invocas por su nombre cada vez que lo necesites, como llamar a un compañero especializado.
- **Conector MCP**: La forma en que un agente se conecta a una herramienta real que ya usas — Figma, Notion, Linear, Slack — en vez de quedarse solo con lo que hay en el proyecto. Solo se convierte en algo que el agente puede usar cuando tú lo activas explícitamente en Ajustes; a partir de ahí se le entrega igual que cualquier otra herramienta.
- **Guardrails (límites del agente)**: Las reglas que acotan lo que un agente puede hacer mientras trabaja solo — por ejemplo, darle acceso de solo lectura para que pueda revisar pero nunca modificar archivos, o ponerle un número máximo de intentos para que no se quede dando vueltas indefinidamente.
- **Claude Agent SDK**: La vía para desarrolladores: el mismo concepto de agente, pero convertido en código para que funcione de forma fiable dentro de un producto y para otras personas, no solo para ti en una conversación. Es la ruta que tomaría tu equipo de ingeniería si quisiera llevar uno de estos agentes más allá de tu propio uso.

---
Artículo original: https://yummy-design-sprint.notion.site/Claude-Agents-What-are-they-how-to-create-one-38e6279147098049a74ae0de250a51a1
