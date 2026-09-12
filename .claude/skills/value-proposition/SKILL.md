---
name: value-proposition
description: >-
  Construye una propuesta de valor en el formato JTBD (Jobs to be Done) de 6 partes: Who,
  Why, What before, How, What after, Alternatives — con énfasis especial en "What before" /
  "What after", que es donde la mayoría de propuestas de valor se rompen. Úsala cuando
  Isabel necesite articular por qué algo importa (una feature, un producto) sin construir el
  Product Strategy Canvas completo (`strategy`) — es la versión ligera de su Sección 2, para
  cuando solo hace falta la propuesta de valor.
---

# Value Proposition — el framework JTBD de 6 partes

> Fuente: [phuryn/pm-skills — pm-product-strategy](https://github.com/phuryn/pm-skills)

Es la misma Sección 2 del canvas de `strategy`, pero como skill independiente y ligera —
para cuando solo hace falta la propuesta de valor, sin construir el documento de estrategia
completo. La propuesta de valor se revisa con mucha más frecuencia que la estrategia
entera, así que tiene sentido poder generarla sola.

## Las 6 partes

1. **Who** — quién se beneficia (un perfil concreto, nunca "todo el mundo").
2. **Why** — por qué lo necesita (el "job" que está intentando hacer).
3. **What before** — cómo resuelve esto *hoy*, sin la solución propuesta.
4. **How** — cómo se resuelve con la solución propuesta.
5. **What after** — cómo cambia su situación una vez la tiene.
6. **Alternatives** — qué otras opciones consideraría en su lugar.

**Punto crítico:** "What before" / "What after" es donde la mayoría de propuestas de valor
se rompen — es habitual describir el "How" (la feature) con mucho detalle y saltarse el
contraste real de antes/después, que es lo que de verdad convence a alguien de que vale la
pena. No dejes que el "How" ocupe más espacio o atención que el contraste before/after.

## Cuándo se activa

Isabel necesita articular por qué algo importa (una feature, un producto, una propuesta) y
no hace falta el canvas de estrategia completo (`strategy`) — solo la propuesta de valor.
También si pide explícitamente `/value-proposition [idea]`.

## Cómo trabajar — mecánica exacta

**1. Preguntas antes de construir:**
- ¿Quién la usaría en la práctica — un rol concreto, no "los usuarios" en general?
- Hoy, sin esta solución, ¿cómo resuelve esa persona el mismo problema?

**2. Construye las 6 partes.** Dedica especial cuidado al "What before" — describe el
proceso actual con detalle real (qué hace, cuánto tarda, dónde falla), no una frase vaga
tipo "lo hace manualmente".

**3. Termina señalando cuál de las seis partes es el argumento más fuerte** para liderar al
presentar esto — normalmente el contraste before/after, no la feature en sí.

## Ejemplo

**Isabel escribe:**
> `/value-proposition` la feature de comparación automática de campañas

**Preguntas antes de construir:**
> Antes de escribir la propuesta, dime:
> - ¿Quién la usaría en la práctica — un rol concreto, no "los usuarios"?
> - Hoy, sin esta feature, ¿cómo resuelve esa persona el mismo problema?

**Isabel responde:**
> La usaría alguien de marketing que gestiona campañas. Hoy lo hace copiando números a
> Excel y comparando a mano.

**Output final:**
> - **Who:** persona de marketing que gestiona varias campañas activas
> - **Why:** necesita decidir qué campaña repetir sin perder media hora copiando números
> - **What before** ⚠️ (la parte clave): hoy exporta datos a Excel, los alinea
>   manualmente por fecha, y compara a ojo — proceso lento y propenso a error si compara
>   periodos distintos
> - **How:** vista de comparación automática dentro del dashboard, alineando periodos
>   automáticamente
> - **What after:** decide en minutos en vez de media hora, con menos riesgo de comparar
>   mal por accidente
> - **Alternatives:** seguir con Excel manual, o pedirle el dato a alguien de analítica
>   cada vez

**Recomendación final:**
> El "What before" es lo más fuerte de esta propuesta — el dolor real es el tiempo perdido
> y el riesgo de error manual, no la falta de una gráfica bonita. Vale la pena liderar con
> eso al presentarlo, no con la feature en sí.
