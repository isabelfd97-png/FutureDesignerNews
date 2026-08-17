---
name: anotar-articulo
description: "Debatir un artículo de The Future Designer con Isabel mientras lo lee y capturar dudas, comentarios y ampliaciones como subrayados sobre el propio texto."
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

3. **Cuando algo de lo hablado merezca quedar anotado en el artículo**, prepara:
   - `quote`: la frase EXACTA (verbatim, misma puntuación) de `content_md` a la que se
     refiere. Cópiala tal cual del JSON, no la parafrasees. Si lo que comentó Isabel no
     corresponde a una frase concreta sino al artículo en general, no es una anotación —
     sugiere `scripts/add_reflection.py` en su lugar.
   - `type`: uno de
     - `duda` — algo que ha preguntado o que queda sin resolver
     - `comentario` — una opinión, reacción o nota personal suya
     - `ampliacion` — información extra que tú (Claude) aportas para completar el tema
   - `text`: la anotación redactada con claridad, 1–3 frases. Su voz si es un comentario
     suyo; la tuya si es una ampliación.

4. **Enséñaselo antes de guardar.** Muestra la cita elegida, el tipo y el texto tal cual se
   guardarían. Espera su confirmación — puede pedir que cambies la cita, el tipo o la
   redacción.

5. **Guarda solo tras su aprobación**, con `scripts/add_annotation.py`:
   ```
   echo '{
     "project_dir": "/Users/isabelferrer-dalmau/Desktop/10 Articles and news",
     "article_id": "...",
     "quote": "...",
     "type": "duda|comentario|ampliacion",
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
- Cada anotación se subraya como mucho una vez en el artículo aunque la frase se repita.
- Si la misma cita se usa sin querer en dos anotaciones distintas, la segunda simplemente no
  encontrará dónde resaltarse (el guion ya marcó esa cita como usada) — evita citas duplicadas
  entre anotaciones del mismo artículo.
</notes>
