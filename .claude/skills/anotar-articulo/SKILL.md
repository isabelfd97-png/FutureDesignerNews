---
name: anotar-articulo
description: "Debatir un artículo de The Future Designer con Isabel mientras lo lee y capturar ampliaciones y ejemplos como subrayados sobre el propio texto."
argument-hint: "<id o título del artículo>"
allowed-tools:
  - Read
  - Bash
---

<objective>
Isabel está leyendo un artículo del sitio y quiere debatirlo en voz alta: le surgen dudas,
quiere comentar algo, o quiere que se amplíe con más información. El resultado de esa
conversación no se queda solo en el chat — se convierte en anotaciones subrayadas sobre la
frase exacta del artículo a la que se refieren, visibles la próxima vez que lo abra.

Esto NO es la reflexión de cierre de `scripts/add_reflection.py` (un bloque de texto libre al
final del artículo). Es más fino: cada anotación cuelga de una frase concreta del cuerpo.
</objective>

<process>
1. **Identifica el artículo.** Búscalo en `data/articles.json` por id o por título (fuzzy está
   bien). Si hay ambigüedad, pregunta.

2. **Ten la conversación normal.** Lee `content_md` del artículo si hace falta contexto.
   Debate con Isabel como harías en cualquier chat: responde dudas, da tu opinión, amplía
   con lo que sepas. No hace falta ningún formato especial para esta parte — es una
   conversación de verdad, no un formulario.

3. **Cuando algo de lo hablado merezca quedar anotado en el artículo**, prepara una o dos
   anotaciones:
   - `quote`: la frase EXACTA (verbatim, misma puntuación) de `content_md` a la que se
     refiere. Cópiala tal cual del JSON, no la parafrasees. Si lo que comentó Isabel no
     corresponde a una frase concreta sino al artículo en general, no es una anotación —
     sugiere `scripts/add_reflection.py` en su lugar.
   - `type`: uno de
     - `ampliacion` (amarillo) — la explicación en sí: qué significa, cómo funciona, cómo
       encaja con el resto del artículo
     - `ejemplo` (azul) — un caso concreto, con nombres y pasos reales, no en abstracto
   - `text`: redactado con claridad, 1–3 frases (más si el ejemplo lo pide). Puede incluir
     un enlace real a otro artículo del sitio con `<a href="#/articulo/OTRO-ID">texto</a>`
     si aporta.

   **Por defecto, cuando Isabel pregunta algo que no entiende, prepara las DOS anotaciones**
   — una `ampliacion` con la explicación y un `ejemplo` con un caso concreto — casi siempre
   ancladas a la MISMA cita (es lo normal, no una excepción: el front-end las agrupa y
   muestra los dos subrayados a la vez sobre esa frase). Si el ejemplo encaja mejor en una
   frase distinta cercana, usa esa cita en su lugar.

4. **Enséñaselo antes de guardar.** Muestra la cita elegida, el/los tipo(s) y el/los texto(s)
   tal cual se guardarían. Espera su confirmación — puede pedir que cambies la cita, el tipo
   o la redacción.

5. **Guarda solo tras su aprobación**, una llamada por anotación, con `scripts/add_annotation.py`:
   ```
   echo '{
     "project_dir": "/Users/isabelferrer-dalmau/Desktop/10 Articles and news",
     "article_id": "...",
     "quote": "...",
     "type": "ampliacion|ejemplo",
     "text": "...",
     "date": "YYYY-MM-DD"
   }' | python3 scripts/add_annotation.py
   ```
   Si el script falla porque no encuentra la cita, no la inventes ni la aproximes —
   vuelve a copiarla literal desde `data/articles.json` y reinténtalo.

6. **Repite** el paso 3–5 tantas veces como surjan anotaciones durante la sesión de lectura.

7. **Nunca hagas commit ni push por tu cuenta.** El artículo queda actualizado localmente y
   reconstruido (`add_annotation.py` ya corre `build_repo.py`); Isabel decide cuándo subirlo,
   igual que con cualquier otro cambio del sitio.
</process>

<notes>
- La primera vez que una anotación se resalta en el artículo, la tarjeta de ese artículo en
  portada y en la sección muestra automáticamente la insignia "¡Con anotaciones!" junto al
  tag — no hace falta tocar nada más para eso.
- Que una `ampliacion` y un `ejemplo` compartan la misma cita a propósito está bien y es lo
  esperado — el front-end las agrupa y pinta los dos rayados (amarillo + azul) uno encima
  del otro sobre esa frase, y al tocarla salen los dos post-it apilados.
- La nota aparece como un post-it fijado justo debajo de la frase (se cierra con su X, o con
  Esc) — no bloquea el resto del artículo ni hay que hacer clic fuera para cerrarla.
</notes>
