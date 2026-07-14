---
title: Dónde va realmente tu contexto de diseño en Claude
url: https://yummy-design-sprint.notion.site/Where-your-design-context-actually-belongs-in-Claude-35962791470980be91fac4fc3c977fa1
section: ia-claude
subsection: Claude para diseñadores
date_added: 2026-07-12
---

## De qué va
Una guía práctica sobre dónde meter el contexto de diseño en Claude, basada en la documentación oficial de Anthropic. Antes de responder a nada, Claude ya está leyendo tres cosas: tus Custom Instructions, los archivos que has subido al proyecto, y qué Skills podrían ser relevantes. Cada una carga de forma distinta, y entender esa diferencia es lo que separa una configuración que funciona de una que malgasta tu ventana de contexto.

## Las tres capas, en corto
- **Custom Instructions** se cargan en cada mensaje, siempre. Siempre activas, siempre consumiendo tokens.
- **Project Knowledge** (archivos subidos) se carga entero en proyectos pequeños, o se busca por RAG en proyectos grandes.
- **Skills** solo cargan su nombre y descripción al arrancar (30-50 tokens cada una). El contenido completo se carga solo cuando Claude decide que hace falta.

## Custom Instructions
Es el texto que Claude lee al principio de cada conversación de un Proyecto, antes incluso de ver tu mensaje. Aquí va lo que Claude nunca debería olvidar, sin importar qué le pidas — cada palabra aquí cuesta tokens en cada turno.

Ejemplos buenos: "Soy product designer de nivel medio construyendo un dashboard B2B para iOS y web", "Usa siempre una grid de 8px, zona táctil mínima 44x44px", "Cuando pida un componente, incluye estados hover, focus y disabled", "Nunca sugieras Inter, Roboto ni fuentes de sistema".

Lo que NO va aquí: tu lista completa de tokens (eso es Project Knowledge), documentación larga de procesos (eso es una Skill), instrucciones específicas de una tarea puntual (eso va en el propio chat). Regla general: si lo dirías en cualquier reunión sin importar el tema, va aquí. Si solo aplica a ciertas tareas, no. Extensión recomendada: 200-400 palabras, algunos incluso dicen que no pases de 500.

## Project Knowledge
Son los archivos que subes a la base de conocimiento de un Proyecto (PDFs, imágenes, JSON, markdown, código), disponibles en todas las conversaciones de ese Proyecto.

Aquí está la parte que más gente entiende mal: en proyectos pequeños (pocos archivos, muy por debajo del límite de contexto), Claude carga tus archivos directamente en cada mensaje, todo el rato. En proyectos grandes (cerca del límite), Claude cambia automáticamente a modo RAG: en vez de cargarlo todo, busca y trae solo las piezas relevantes para cada pregunta.

Qué subir aquí: un `design-tokens.json` con los valores reales de ESTE proyecto (no uno genérico), el brand guide del cliente en PDF, 3-5 capturas de la dirección visual que buscas, y sobre todo un `corrections.md` — cada vez que corriges a Claude ("las cards son de 16px de radio, no 12px"), lo apuntas ahí y Claude deja de repetir el mismo error en la siguiente sesión. Es, según la guía, de lo más rentable que puedes hacer.

Qué NO subir: archivos de proyectos ya terminados, un PDF de 40 páginas de documentación completa del design system (mejor un resumen enfocado), cosas que usas en TODOS tus proyectos (eso es una Skill, no hace falta copiarlo en cada Proyecto), o archivos enormes "por si acaso".

## Skills
Son conjuntos de instrucciones portátiles que te acompañan a todos los sitios: en todos tus Proyectos, en chats normales, en Claude Code. Es tu criterio empaquetado para que Claude lo use donde haga falta.

La parte clave de cómo cargan se llama *progressive disclosure*: al arrancar, Claude solo lee el nombre y una descripción corta de cada Skill (unos 30-50 tokens). Cuando le pides algo relevante, compara tu petición contra esas descripciones y carga el contenido completo solo de las Skills que aplican. Las que no hacen falta se quedan sin usar, con coste cero. Es justo lo contrario de Project Knowledge en proyectos pequeños, donde todo se carga siempre.

Ejemplos: una Skill de "UI Designer" con tu filosofía de spacing y tus mínimos de contraste; una Skill de "UX Copywriter" con tus reglas de microcopy; una Skill de marca por cliente (nómbrala por el cliente, no "brand.md", para que Claude active la correcta); una Skill de accesibilidad con tus estándares WCAG.

Qué NO poner en una Skill: valores de tokens específicos de un proyecto (eso es Project Knowledge), una única Skill gigante que lo cubra todo (Anthropic recomienda varias Skills enfocadas en vez de una mega-Skill), material de referencia de un solo uso, o contenido que cambia en cada proyecto. La pregunta que resuelve la duda: ¿usarías esta regla también en tu próximo proyecto? Si sí, es una Skill. Si no, es Project Knowledge.

## ¿Y los archivos .md tipo DESIGN.md?
Un .md es simplemente texto plano con formato sencillo (# para títulos, - para listas). No es código, no es una base de datos, no es una herramienta de diseño. Claude lo procesa más barato y más rápido que un PDF con la misma información, y además está más estructurado, así que encuentra secciones concretas de forma más fiable.

Dónde ayuda: un `corrections.md` (probablemente el archivo más rentable que puedes crear), un `design-rules.md` con tu escala de spacing y el razonamiento de cuándo usar cada valor (no solo el número, también el porqué), o un `brand-brief.md` con la versión condensada de una marca para un proyecto concreto.

Dónde NO ayuda: si intentas que sustituya tu design system real (que vive en Figma, en código, en tu librería de componentes) — si mantienes el .md Y tus variables de Figma Y tus tokens de código, has creado tres fuentes de verdad que van a desincronizarse. Tampoco ayuda si el archivo se vuelve gigante (si tu DESIGN.md tiene 500+ líneas, probablemente está haciendo demasiado — lo ideal son 100-200 líneas), ni si el contenido cambia constantemente (mejor conectar Claude a Figma vía MCP para acceso en vivo: el .md es una foto fija, MCP es una conexión viva). El error más habitual: tratar un DESIGN.md como si FUERA el design system, cuando en realidad es solo el briefing que le das a Claude.

## Coste real en tokens
La ventana de contexto de Claude en los planes de pago es de 200.000 tokens. Unas Custom Instructions de 300 palabras cuestan ~400 tokens (0,2%), un `design-tokens.json` unos 1.000-3.000 tokens, un `corrections.md` unos 500-1.000, y una Skill sin activar prácticamente nada (30-50 tokens). Una configuración bien organizada suele usar solo un 3-8% del contexto, dejando el resto libre para el trabajo real.

## Ideas clave
- Custom Instructions carga en cada mensaje, siempre — solo lo verdaderamente universal, bajo 400 palabras.
- Project Knowledge se carga entero en proyectos pequeños o se busca por RAG en proyectos grandes; limpia lo que no uses.
- Skills solo cargan nombre + descripción hasta que son relevantes; mejor varias Skills enfocadas que una mega-Skill.
- La pregunta test: ¿lo usarías en tu próximo proyecto? Skill. ¿Es de este proyecto? Project Knowledge.
- Un .md es un documento de briefing para Claude, no un reemplazo de tu design system real.

## Para aprender
- **Ventana de contexto (context window)**: La cantidad total de texto que Claude puede "tener en la cabeza" a la vez en una conversación, medida en tokens (200.000 en los planes de pago). Todo lo que subes, escribes o Claude carga automáticamente compite por ese mismo espacio limitado — por eso importa tanto qué metes ahí y cómo carga cada cosa.
- **RAG (Retrieval-Augmented Generation)**: Una técnica en la que, en vez de cargar todos tus archivos en cada mensaje, el sistema busca solo las partes relevantes para tu pregunta concreta y las trae al contexto. Es lo que activa Claude automáticamente cuando un Proyecto tiene demasiados archivos para caber todos a la vez.
- **Custom Instructions**: El bloque de texto que Claude lee al principio de cada conversación dentro de un Proyecto, antes de ver tu mensaje. Es tu contexto "siempre activo": quién eres, qué construyes, tus reglas que nunca cambian — pensado para ser corto porque se paga en tokens en cada turno.
- **Progressive disclosure (de una Skill)**: La forma en que carga una Skill: al principio Claude solo ve su nombre y una frase descriptiva (casi gratis en tokens); solo si tu petición encaja con esa descripción, Claude carga el contenido completo de la Skill. Es lo que permite tener muchas Skills guardadas sin que cuesten nada hasta que realmente se usan.

---
Artículo original: https://yummy-design-sprint.notion.site/Where-your-design-context-actually-belongs-in-Claude-35962791470980be91fac4fc3c977fa1
