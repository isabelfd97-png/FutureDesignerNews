# The Future Designer — How the paper thinks

*A field guide for designers (not developers). It explains all the logic and the decisions behind the home page and the reading experience, in plain language.*

---

## 1. The one big idea

The home page is a **simple, predictable newspaper**: the newest article leads, and everything follows in the order it arrived.

There is no algorithm, no account, and no scoring to learn. Articles are shown newest-first, at three sizes, so the page always has a clear front-page hierarchy without asking the reader to do anything. On top of that, you can mark what you've **read**, so it's easy to see at a glance what's still waiting for you.

**Why it's built this way:** an earlier version rearranged the whole front page around a 0–5 star rating you had to give every article. It was powerful but overcomplicated — the page's shape depended on a mental model the reader had to hold ("this story is here because I gave it this many stars"). We removed ratings entirely in favour of plain chronology plus a lightweight read/unread marker.

---

## 2. The front page ("Portada") — three sizes, newest first

The home page (called *Portada* in the app) sorts every visible article by date (`date_added`, newest first) and lays them out in three tiers:

| Tier | What fills it | Size |
|------|---------------|------|
| **Lead** (*front-lead-single*) | The single newest article. | Large hero — image + big headline + summary |
| **Secondary** (*front-secondary*) | The next **2** articles. | Medium cards, side by side |
| **More articles** (*Más artículos*) | Everything else. | Standard card grid, below a divider |

That's the whole rule: **relevance = recency.** The most recent thing is the headline; the layout gets smaller as articles get older. If there are three or fewer articles, the lower tiers simply don't render.

**The reasoning:** a newspaper front page has a natural hierarchy — one headline, a couple of secondary stories, then the rest. Mapping that to pure recency keeps it predictable: a reader always knows *why* a story is where it is (it's newer or older), with no hidden state to manage.

---

## 3. Read / unread — the one personal marker

Ratings are gone. The only thing the reader marks now is whether they've **read** an article, and it's entirely manual.

- **Inside an article** there's a button: **"Marcar como leído"**. Pressing it flips to **"Leído · marcar como no leído"** (with a check), and pressing again undoes it. Nothing is automatic — opening an article does *not* mark it read.
- **On the front page**, a read article shows a black **"Leído ✓"** badge in the top-right corner and is **dimmed** (it returns to full strength on hover), so unread articles stand out. This appears at all three sizes.
- The state is saved instantly to your device and reflected on the front page whenever you return to it.

**Why manual-only:** the whole point of this pass was to reduce complexity and keep the reader in control. A manual toggle is unambiguous — the paper never guesses that you "read" something just because you clicked in.

---

## 4. The six desks (sections)

Content is organised into six fixed desks. These power the top navigation and the tags on every card. Each has a one-line remit that sets what belongs there.

- **Design 2.0** (`design-2-0`) — How the craft of design is changing in the AI era: new workflows, new skills, and the principles that still hold.
- **Claude** (`claude`) — Guides, features and ways of working specific to Claude: agents, context, usage limits, Claude Code.
- **Figma** (`figma`) — Updates, plugins and features in Figma, including everything AI touches inside the tool itself.
- **Engineering** (`engineering`) — Collaborating better with developers: process, culture, expectations and a shared language.
- **AI** (`ai`) — Concepts and AI in general, beyond Claude: fundamentals, models, reference terminology.
- **Materials** (`materials`) — Skills, templates, repos and other downloadables bundled with an article, ready to use.

Articles can also carry a free-form **subsection** label (shown after the desk name, like *Claude · Agents*). Subsections aren't a fixed list — they emerge from the content and are used to sharpen the tag and to find related reading.

---

## 5. The living masthead — small signs that the paper is awake

The top of the page carries several details whose only job is to make a static site feel current and personal. None of them change what you can read — they set tone.

- **Animated nameplate (on load):** the title "The Future Designer" rises in word by word on each visit, with alternate words in the accent orange.
- **Live kicker (updates every 30s):** a pulsing radar dot with *"En directo"* and the current date and time. Reinforces that this is today's paper.
- **Time-aware greeting:** the subtitle greets the reader by name and changes with the clock — morning, afternoon, night each get their own line.
- **Reading streak:** a flame icon counts consecutive days that have new articles, with an encouraging phrase on hover (*"Racha en llamas — sigue así"*). Gentle motivation to keep the habit.

---

## 6. The ticker — the newest headlines

Below the masthead, a horizontal ticker scrolls the **most recent headlines**, each stamped with its desk and linking straight to its article. Hovering pauses the scroll; a hand-drawn "¡Nuevo!" starburst sits on top as a "latest" flag.

*(Previously the ticker showed only unrated articles and opened a quick-rating modal. With ratings removed, it's now simply a live index of the newest stories.)*

---

## 7. Inside an article — the reading view, and what it remembers

Opening an article slides over a full reading view. Beyond the summary and body, several elements turn passive reading into something you keep.

- **Key points & summary:** every article leads with an AI-written summary and a short list of key points, so the value is legible before you commit to the full read.
- **Read toggle:** the "Marcar como leído" button described in section 3.
- **Glossary terms (heart to keep):** new or tricky terms appear with a definition and a heart. Hearting a term adds it to your personal Encyclopedia (section 8).
- **Related articles (scored, not random):** up to three suggestions, ranked by relevance — sharing a subsection scores highest, then the same desk, then any shared glossary term. Only genuine matches show.
- **Annotations:** highlighted quotes with your doubts, comments, and expansions — see section 8.

---

## 8. Annotations — margin notes on the article itself

While reading, you can debate an article with Claude (the *anotar-articulo* skill) and turn the outcome into an annotation anchored to the exact phrase it's about — not just a note appended at the end.

- **Two types, two colours:** **ampliación** (yellow) is the explanation itself; **ejemplo** (blue) is a concrete, real-world case. When both apply to the same phrase, both highlights show at once.
- **Highlighted, not hidden:** the phrase gets a hand-drawn marker-style highlight in the article body. Tap it and a post-it note pins itself just below, in the matching colour — no dark overlay, nothing else on the page is blocked.
- **Real post-its, not tooltips:** the note is a rectangular sticky note that scrolls with the article. If two notes land on the same phrase, they overlap like real sticky notes — tap either one to bring it to the front.
- **The badge:** the moment an article has any annotation, its card shows a **"¡Con anotaciones!"** flag next to the tag, on every size (lead, secondary, grid).

---

## 9. Encyclopedia & flashcards — the terms you kept become a study deck

Every term you heart inside an article collects into the **Encyclopedia** — an A–Z of definitions, each linked back to the article it came from, with a live letter index down the side and a search box. (Some articles are marked as full "dictionary" pieces and contribute all their terms automatically.)

From there, **Repasar** (Review) opens a flashcard session built on the **Leitner spaced-repetition system**. A term you recall correctly moves up a box and won't reappear for longer; a term you miss drops back to box 1 and returns tomorrow. The five boxes schedule reviews like this:

| Box 1 | Box 2 | Box 3 | Box 4 | Box 5 |
|-------|-------|-------|-------|-------|
| 1 day | 3 days | 7 days | 14 days | 30 days |

The Review button shows how many terms are *due* today, so the paper doubles as a lightweight way to actually retain the vocabulary of the field, not just skim it.

---

## 10. The rest of the toolkit — search, streak & keeping it tidy

- **Spotlight search:** a quick search that matches across titles, summaries, key points and subsections. With no query it simply shows the six most recent articles as a starting point.
- **Two kinds of delete:** articles can be *hidden* (a soft trash you can restore from) or *permanently deleted* via the history view. Hidden and deleted items drop out of every tier, count and search.
- **History & footer count:** a history view lists what's been removed, and the footer always states how many articles are saved and when the paper was last updated.

---

## 11. The visual language — why it looks like a brutalist newspaper

The look is deliberate: part broadsheet authority, part independent zine. It says "this is a real publication" while staying playful enough to feel personal.

**Palette:** Ink `#0A0A0A` · Signal orange `#FF5A1F` · Paper `#FFFFFF` · Muted grey `#7A7A7A`.

- **One accent, used sparingly:** a single signal orange marks what's live, new, or interactive. Because it's the only colour, it always means "pay attention here."
- **Heavy grotesque + mono:** Archivo Black for headlines gives print weight; Space Mono for kickers, dates and labels reads like a wire service; Space Grotesk carries the body.
- **Hard offset shadows:** cards lift with a solid black shadow on hover instead of a soft blur — a tactile, screen-printed feel rather than a glossy web one.
- **Grayscale photos + pixel icons:** images are desaturated so no single thumbnail shouts over the orange, and each article gets a hand-drawn pixel-art icon chosen from its content when it has no image.
- **Dotted paper ground:** a faint dot grid behind everything reads as newsprint texture and ties the pages together.

**The throughline:** signal over noise. Every visual choice exists to make the *content* the loudest thing on the page.

---

## 12. Where everything lives — it's all on your device

Important for anyone redesigning the experience: **nothing a reader does leaves their browser.** The read markers, hearted terms and the trash are all stored locally. There is no server, no login, and no syncing between devices. Open the paper on a different machine and it starts fresh. Annotations are the one exception — they're written into `data/articles.json` itself (via the *anotar-articulo* skill), so they travel with the article for every reader, not just you.

| Stored value | What it holds |
|--------------|---------------|
| `readArticles` | Which articles you've marked as read (drives the badge + dimming). |
| `likedTerms` | Glossary terms you hearted into the Encyclopedia. |
| `termSRS` | Flashcard progress — which Leitner box each term is in and when it's due. |
| `hiddenArticles` / `deletedArticles` | Soft-trashed and permanently removed items. |

**Consequence for design:** because state is per-device and per-person, the paper is genuinely one reader's newspaper. Features can be as personal as you like — but they can't assume anything carries over to another device, and the first-visit state (nothing read yet) is a real, common experience worth designing for.
