---
title: Diccionario de IA para diseñadores
url: https://yummy-design-sprint.notion.site/AI-Design-Dictionary-326627914709808eb562c22421ba2088
section: terminologia-tecnica
subsection: Diccionario de referencia
date_added: 2026-07-12
---

## De qué va
Un diccionario de términos de IA pensado específicamente para diseñadoras, escrito por una diseñadora. No es para memorizar: cada término explica cuándo te lo vas a encontrar y por qué importa para tu forma de trabajar con IA.

## Cómo está organizado
- **Empieza aquí** — los términos que te vas a encontrar en tu primera semana trabajando con herramientas de IA: CLI, Terminal, API, MCP, prompt engineering, ventana de contexto, alucinaciones, LLM, GPT, Markdown, JSON, Artifacts, system prompt.
- **Nivel 2** — lo que va apareciendo según profundizas: entorno de desarrollo, npm, Git, GitHub, frameworks, frontend vs backend, despliegue, variables de entorno, tokens, agéntico, modelo, multimodal, SVG, debug, y más.
- **Términos avanzados** — infraestructura y conceptos con los que puedes llegar lejos sin conocerlos, pero que acabas encontrando si sigues profundizando: fork, branch, RAG, fine-tuning, embeddings, servidor, dominio, DNS, SSL, Skills y Proyectos de Claude.

## Por qué le importa a un product designer
Cada entrada trae la 'traducción a lenguaje de diseño': por ejemplo, un repositorio de GitHub se explica como 'el historial de versiones de Figma, pero rastreando también la carpeta de assets y las notas de desarrollo'. Esa capa de traducción es lo que hace que términos que suenan intimidantes dejen de serlo, y es justo el tipo de vocabulario que ayuda a hablar con ingeniería sin sentir que falta contexto.

Todos los términos de este diccionario se han incorporado directamente a la sección Enciclopedia del sitio (no hace falta darles like uno a uno, como con el resto de artículos) — piénsalo como el diccionario de cabecera al que puedes volver en cualquier momento.

## Ideas clave
- El diccionario cubre 63 términos en tres niveles de profundidad, de lo esencial a lo avanzado.
- Cada término incluye cuándo lo verás, su traducción a lenguaje de diseño, y por qué importa para tu flujo de trabajo con IA.
- No hace falta memorizarlo: es una referencia para volver cuando te encuentres una palabra nueva.
- Todos sus términos ya están en la Enciclopedia del sitio de forma automática.

## Para aprender
- **CLI (Command Line Interface)**: Una forma de controlar el ordenador escribiendo comandos en vez de haciendo clic. Es donde viven Claude Code y los servidores MCP — no hace falta dominarla, pero conocer lo básico abre puertas.
- **Terminal**: La aplicación donde escribes comandos de CLI (Terminal en Mac, PowerShell en Windows). Es como abrir un archivo de Figma en blanco: no pasa nada hasta que tú haces algo.
- **API (Application Programming Interface)**: La forma en que dos programas se hablan entre sí: uno pide algo, el otro lo devuelve. Un servidor MCP es, en el fondo, Claude hablando con tus otras apps a través de sus APIs.
- **MCP (Model Context Protocol)**: La conexión que deja a Claude ver e interactuar directamente con herramientas como Figma o Notion, en vez de que tengas que describírselas con palabras. Es lo que hace que un flujo de diseño-a-código funcione de verdad.
- **Prompt engineering**: La habilidad de escribir instrucciones claras y específicas para que Claude haga justo lo que quieres — como escribir un buen brief de diseño: uno vago da resultados vagos.
- **Context window (ventana de contexto)**: Cuánta información puede 'ver' Claude a la vez: la conversación, los archivos, las instrucciones. Si Claude empieza a 'olvidar' cosas de antes, has llenado la ventana de contexto.
- **Hallucination (alucinación)**: Cuando la IA afirma algo completamente falso con total seguridad. Conviene verificar siempre los datos que de verdad importan, sobre todo en documentación o afirmaciones técnicas.
- **LLM (Large Language Model)**: La familia de IA que hace funcionar a Claude, ChatGPT y similares, entrenada con muchísimo texto para entender y generar lenguaje. Se les da bien el lenguaje, no tanto las matemáticas o los datos en tiempo real.
- **GPT (Generative Pre-trained Transformer)**: Un modelo concreto creado por OpenAI, no un término genérico para toda la IA (aunque se use así coloquialmente). Claude NO es un GPT: es un modelo distinto, de Anthropic.
- **Markdown**: Una forma sencilla de dar formato a texto con símbolos (# para títulos, ** para negrita, - para listas). Claude lo domina de forma nativa, y es también el formato de los archivos SKILL.md.
- **JSON (JavaScript Object Notation)**: Un formato de datos estructurado, con etiquetas y valores entre llaves. Los design tokens, las respuestas de una API o los archivos de configuración suelen venir en este formato.
- **Artifacts**: Los resultados interactivos que Claude puede crear —webs, código, documentos— que aparecen en un panel aparte y se pueden probar en vivo. Es la diferencia entre que Claude te describa algo y que te lo enseñe funcionando.
- **System prompt**: Instrucciones ocultas que definen cómo se comporta Claude antes incluso de que empieces a escribir. Es como un brief de diseño que está siempre activo — en Proyectos y en las Skills, básicamente defines el tuyo.
- **IDE (Integrated Development Environment)**: Un editor de texto sofisticado para escribir código (VS Code, Cursor). Es el Figma de los desarrolladores: no es solo un lienzo, tiene capas, extensiones y propiedades.
- **npm (Node Package Manager)**: Una herramienta que descarga e instala paquetes de código ya escritos por otros, para no construir todo desde cero — como instalar un plugin de Figma, pero para proyectos de código.
- **Node.js**: Una forma de ejecutar JavaScript fuera del navegador. Muchos servidores MCP y herramientas de IA están construidos con él, así que tenerlo instalado suele ser un requisito previo.
- **Git**: Un sistema que registra cada cambio hecho en el código, para poder volver atrás, colaborar sin pisarse el trabajo y ver quién cambió qué. Es como el historial de versiones de Figma, pero mucho más potente.
- **GitHub**: Una web donde se guardan y comparten repositorios de Git — como Google Drive para código, con funciones de colaboración. La mayoría de servidores MCP y herramientas de IA viven ahí.
- **Repository / Repo**: La carpeta de un proyecto con todo su historial de cambios, normalmente alojada en GitHub. 'Clonar el repo' significa simplemente descargarlo a tu ordenador.
- **Clone**: Descargar una copia de un repositorio de GitHub a tu ordenador — como duplicar un archivo de la Comunidad de Figma a tu propia cuenta.
- **Localhost**: Tu propio ordenador actuando como servidor temporal y privado. Cuando pruebas algo que Claude ha construido, primero corre en local, antes de publicarse en ningún sitio.
- **Framework (React, Next.js, Vue...)**: Una base de código ya construida que los desarrolladores usan para no empezar de cero — como una plantilla de design system con patrones comunes ya montados. Claude suele generar código en React.
- **Frontend vs Backend**: Frontend es lo que ve e interactúa el usuario (la interfaz); backend es lo invisible: servidores, bases de datos, lógica. Como diseñadora con IA trabajas sobre todo en frontend, pero entender la diferencia ayuda a hablar con ingeniería.
- **Deployment (despliegue)**: El proceso de sacar código de tu ordenador y ponerlo en internet para que otros lo vean — el equivalente a publicar un prototipo de Figma en vez de dejarlo en borradores.
- **Vercel / Netlify**: Plataformas que facilitan el despliegue: conectas tu código y ellas se encargan de ponerlo online. Es el botón de 'publicar' de Framer o Webflow, pero para sitios hechos a medida en código.
- **Environment variables (variables de entorno)**: Ajustes secretos guardados fuera del código, como claves de API o contraseñas, para que no queden visibles en los archivos.
- **.env file**: El archivo especial, normalmente oculto, donde se guardan las variables de entorno. Nunca se sube a GitHub ni se comparte públicamente.
- **Tokens (contexto de IA)**: Las unidades con las que Claude mide el texto (aprox. 1 token = 0,75 palabras). Las conversaciones más largas gastan más tokens — importa sobre todo si usas la API o tienes límites de uso ajustados.
- **Agentic (agéntico)**: Cuando la IA puede actuar por su cuenta, no solo responder: navegar, hacer clic, ejecutar código, completar tareas de varios pasos. Es la diferencia entre que alguien te describa un cambio y que lo haga por ti.
- **Dependencies (dependencias)**: Otros paquetes de código que necesita tu proyecto para funcionar — como los componentes vinculados a una librería de Figma: si la quitas, algo se rompe.
- **Build**: Convertir el código fuente en algo que realmente se pueda ejecutar, como paso previo al despliegue — el equivalente a exportar un diseño de Figma en el formato correcto para desarrollo.
- **Claude Code vs Claude Desktop**: Dos formas distintas de usar Claude. Claude Desktop es la app de chat normal; Claude Code vive en la terminal y puede ejecutar comandos, editar archivos y construir proyectos de forma más autónoma.
- **Computer use**: Una capacidad de Claude para ver y controlar tu pantalla —hacer clic, rellenar formularios, navegar por apps— como un asistente remoto. Abre la puerta a automatizar tareas repetitivas en cualquier aplicación, no solo en las que tienen API.
- **Model (modelo de IA)**: El sistema de IA entrenado que da las respuestas. Claude es un modelo; sus distintas versiones (Opus, Sonnet) tienen capacidades y velocidad distintas, como productos dentro de la misma familia.
- **Multimodal**: IA que entiende varios tipos de entrada —texto, imágenes, audio— no solo texto. Para una diseñadora es enorme: puedes compartir capturas y mockups directamente en vez de describirlo todo con palabras.
- **SVG (Scalable Vector Graphics)**: Un formato de imagen vectorial escrito en código en vez de píxeles, que escala perfectamente a cualquier tamaño. Claude puede generar SVGs —iconos, ilustraciones— directamente.
- **CSS variables**: Valores reutilizables definidos una vez y usados en todo el CSS — el equivalente exacto en código a los design tokens o las variables de Figma.
- **Debug (depurar)**: Encontrar y arreglar errores en el código. Cuando el código que genera Claude no funciona, tendrás que depurarlo — y Claude también puede ayudarte a hacerlo si le pegas el error.
- **Syntax (sintaxis)**: Las reglas gramaticales de un lenguaje de programación. Si Claude genera código y no funciona, puede deberse a un error de sintaxis.
- **Boilerplate**: Código de arranque estándar que hace falta en todo proyecto de cierto tipo — como una plantilla de Figma con tu design system ya montado, para no partir de un archivo en blanco cada vez.
- **Stack**: La combinación de tecnologías usada para construir algo (lenguajes, frameworks, herramientas). Decirle a Claude tu stack ('React con Tailwind') ayuda a que genere el código adecuado.
- **Temperature (temperatura)**: Un ajuste que controla lo creativa o predecible que es una respuesta de IA: baja temperatura, más predecible; alta, más variada. Es como el nivel de libertad creativa que le das a un brief.
- **Fork**: Crear tu propia copia de un repositorio ajeno que sigue conectada al original, para modificarla sin afectar al original — como duplicar un archivo de la Comunidad de Figma manteniendo el enlace de origen.
- **Branch (rama)**: Una versión paralela del código donde puedes hacer cambios sin tocar la versión principal, y fusionarla después — como una rama de Figma para explorar una idea sin tocar el archivo principal.
- **Commit**: Guardar una instantánea de los cambios de código con un mensaje que describe qué hiciste — como dejar una nota de versión en el historial de Figma.
- **Push / Pull**: Push es enviar tus cambios guardados a GitHub; pull es descargar los cambios más recientes de GitHub a tu ordenador.
- **Config / Configuration file (archivo de configuración)**: Un archivo con los ajustes de cómo debe comportarse una herramienta o proyecto, normalmente en JSON o YAML — el panel de ajustes de Figma, pero guardado en un archivo.
- **YAML**: Un formato de archivos de configuración parecido al JSON pero basado en sangrado en vez de llaves, a menudo más fácil de leer.
- **RAG (Retrieval Augmented Generation)**: Una técnica en la que la IA busca información relevante en una base de datos antes de responder, en vez de fiarse solo de lo que aprendió en el entrenamiento — como una biblioteca de referencia que la IA puede consultar antes de contestar.
- **Fine-tuning (ajuste fino)**: Entrenar un modelo ya existente con datos adicionales para especializarlo en una tarea concreta, como una formación extra después del entrenamiento base. Es caro y avanzado; para la mayoría, un buen prompting basta.
- **Embeddings**: Una forma de convertir texto (o imágenes) en números que capturan su significado, para que cosas parecidas tengan números parecidos y se puedan buscar por significado, no solo por coincidencia exacta.
- **Vector database (base de datos vectorial)**: Una base de datos optimizada para guardar y buscar embeddings, encontrando los resultados 'más parecidos' en vez de coincidencias exactas — la infraestructura detrás de la búsqueda semántica.
- **Inference (inferencia)**: El momento en que un modelo de IA realmente genera una respuesta, usando lo que aprendió durante el entrenamiento. Cuando le mandas un mensaje a Claude y responde, eso es inferencia.
- **Server (servidor)**: Un ordenador que da servicio a otros ordenadores: ejecuta software, guarda datos y responde peticiones. Cuando visitas una web, tu navegador le pide la página a un servidor.
- **Cloud (la nube)**: Ordenadores y servicios que corren en internet en vez de en tu máquina — 'en la nube' significa 'en los servidores de otro', como guardar archivos en Google Drive en vez de en tu disco duro.
- **Docker / Container**: Una forma de empaquetar una aplicación con todo lo que necesita para funcionar igual en cualquier ordenador. Algunos servidores MCP corren dentro de un contenedor Docker.
- **Hosting (alojamiento)**: El servicio que mantiene tu web o aplicación funcionando en un servidor para que la gente pueda acceder a ella — como preguntarte dónde vive tu portfolio (¿Framer? ¿Webflow?).
- **Domain (dominio)**: La dirección legible de una web, como yummy-labs.com, en vez de una serie de números. Se compra a un registrador de dominios.
- **DNS (Domain Name System)**: El sistema que traduce nombres de dominio en las direcciones numéricas que entienden los ordenadores — la guía telefónica de internet.
- **SSL / HTTPS**: La capa de seguridad que cifra los datos entre tu navegador y una web. El candado y el 'https://' en la URL significan que está activa.
- **Skills (Claude)**: Instrucciones personalizadas que le das a Claude en un archivo SKILL.md estructurado, para que se comporte de una forma concreta en tareas específicas — un brief creativo detallado que está siempre activo.
- **Projects (Claude)**: Espacios de trabajo en Claude donde puedes fijar instrucciones personalizadas, subir archivos de referencia y mantener contexto a través de conversaciones — como la estructura de equipos de Figma, pero para contexto de IA.
- **Compile (compilar)**: Convertir el código fuente en un formato que el ordenador pueda ejecutar, un paso previo necesario en algunos lenguajes — como exportar un diseño de Figma a los assets finales de producción.

---
Artículo original: https://yummy-design-sprint.notion.site/AI-Design-Dictionary-326627914709808eb562c22421ba2088
