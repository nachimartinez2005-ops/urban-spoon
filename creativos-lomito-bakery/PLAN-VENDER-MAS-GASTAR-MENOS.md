# Lomito Bakery — Auditoría + plan para vender más y gastar menos

Campaña: **Test ABO | Pastelería Canina | MX 10/10** (`52532697130726`)
Cuenta: Ebooks Argentina (`1560224662043860`) · Píxel: Lomito Bakery (`1712126017302327`)
Fecha: 2026-10-12 · Ventana: últimos 30 días

---

# PARTE 1 — AUDITORÍA

## 1.1 Corrección al diagnóstico anterior ⚠️

En mi análisis anterior te dije que **el cuello de botella era la landing page**. Con el
desglose por placement a la vista, **eso era incorrecto** y el dato cambia qué hay que hacer primero.

Lo que pasó: el 1.18% de conversión que calculé estaba contaminado por tráfico basura.
Separado por placement, la landing convierte **bien**.

## 1.2 El hallazgo: 57% del presupuesto fue a placements que vendieron $0

| Placement | Gasto | Clics | CTR | Compras | CPA |
|---|---|---|---|---|---|
| **Facebook Feed** | $16.96 | 83 | 5.87% | **2** | **$8.48** |
| **Instagram Reels** | $12.37 | 35 | 3.47% | **2** | **$6.19** |
| Instagram Feed | $12.67 | 27 | 2.73% | 0 | — |
| Facebook Reels | $11.24 | 72 | 5.65% | 0 | — |
| Instagram Stories | $8.31 | 31 | 3.74% | 0 | — |
| Facebook Stories | $2.25 | 7 | 7.29% | 0 | — |
| Audience Network classic | $1.51 | 32 | 6.44% | 0 | — |
| **AN rewarded_video** | $0.49 | 40 | **36.70%** 🚨 | 0 | — |
| FB instream video | $1.43 | 8 | 7.14% | 0 | — |
| Resto (marketplace, search, WhatsApp…) | ~$0.25 | 3 | — | 0 | — |

**Lectura:**

- **$29.33 → 4 ventas** (FB Feed + IG Reels) = **CPA $7.33, ROAS ~1.38** ✅
- **$38.15 → 0 ventas** (todo lo demás) ❌
- `AN rewarded_video`: **36.70% de CTR** con 40 clics y 0 ventas. Eso no es interés:
  son personas tocando el anuncio para cobrar una recompensa dentro de un juego.
  Es el clic más basura que existe en Meta.

**Conversión real por tipo de tráfico:**

| Tráfico | Clics | Ventas | CVR |
|---|---|---|---|
| Placements buenos (FB Feed + IG Reels) | 118 | 4 | **3.39%** ← normal/sano para infoproducto |
| Placements basura | 220 | 0 | **0%** |
| Mezclado (lo que yo medí antes) | 338 | 4 | 1.18% ← el número engañoso |

**La landing no está rota. El tráfico estaba sucio.** Con 3.39% de CVR en tráfico limpio,
tu funnel funciona.

## 1.3 Economía unitaria real (precios confirmados)

**Precios:** ebook **$8.90** · upsells disponibles: **$5.90, $5.90, $4.90**

### Reconstrucción exacta de lo que reportó Meta

Meta reportó ROAS `0.600178` sobre $67.48 → **$40.50** de ingreso. Eso calza al centavo con:

```
4 ebooks ($35.60) + 1 upsell de $4.90 = $40.50 ✅
```

**Conclusión importante: el upsell SÍ está siendo trackeado.** El `Purchase` dispara en el
upsell. Lo que falta no es el upsell, son **2 ventas de ebook** que no se atribuyeron
(el problema de `fbp` al 35.5%).

### El número real

| | Ventas | Ingreso | ROAS |
|---|---|---|---|
| Lo que ve Meta | 4 + 1 upsell | $40.50 | **0.60** |
| Lo que pasó de verdad | 6 + 1 upsell | **$58.30** | **0.86** |
| Invisible para Meta | 2 ebooks | $17.80 (**31% del ingreso**) | — |

### 🚨 El problema estructural: el ticket no paga el tráfico

| Métrica | Valor |
|---|---|
| CPA real (mezclado, 6 ventas) | **$11.25** |
| Ticket | **$8.90** |
| AOV actual (take rate upsell 17%) | **$9.72** |
| **Pérdida por venta** | **−$2.35** |

**Pagás $11.25 para ganar $9.72.** No es un problema de creativos ni de hooks:
con este ticket y este CPA la cuenta no cierra ni con los mejores anuncios del mundo.

La buena noticia: en placements limpios tu CPA es **$7.33**, y ahí sí cierra
($8.90 de ticket contra $7.33 de costo = ROAS 1.21, delgado pero positivo).

### CPA de equilibrio según lo que hagas

| Configuración | AOV | CPA de equilibrio |
|---|---|---|
| Hoy (ticket $8.90, upsell 17%) | $9.72 | $9.72 |
| + escalera de upsells al 35% | $10.85 | $10.85 |
| + escalera al 50% | $11.69 | $11.69 |
| Precio $11.90 + upsell 35% | $13.85 | $13.85 |
| **Precio $14.90 + upsell 35%** | **$16.85** | **$16.85** |

> Cada dólar que le sumás al AOV es un dólar más que podés pagar por cliente.
> **Subir el AOV es más barato y más rápido que bajar el CPA.**

### El upsell está desaprovechado

Tenés **$16.70 en upsells disponibles** ($5.90 + $5.90 + $4.90) y solo **1 de 6
compradores** tomó uno — el más barato ($4.90). Eso es un take rate del 17% y la elección
del más chico. Dos hipótesis a verificar:

1. **¿Se les muestra el upsell a todos?** Si el flujo se rompe o no aparece, no es take rate bajo: es que no se ofrece.
2. **¿En qué orden se presentan?** Se tomó el de $4.90 y ninguno de $5.90 → probablemente se muestra primero el más barato. Hay que invertirlo.

## 1.4 El problema de atribución (más grave de lo que parece)

Revisé la calidad del píxel. El dato clave:

| Evento | Calidad de coincidencia (EMQ) | Cobertura `fbp` |
|---|---|---|
| **Purchase** | **9.3 / 10** 🟢 excelente | 100% |
| AddToCart | 6.1 / 10 🟡 | 100% |
| InitiateCheckout | 5.8 / 10 🟡 | 80.8% |
| **PageView** | **5.3 / 10** 🔴 | **35.5%** 🚨 |

Tu evento `Purchase` está impecable: manda email, teléfono, external_id, nombre, ciudad y
estado al 100%. Cuando dispara, Meta lo matchea perfecto.

**Entonces, ¿por qué faltan 2 ventas?** Las causas probables, en orden:

1. **El upsell no dispara `Purchase`.** Es una transacción aparte. Para Meta ese ingreso
   simplemente **no existe**. Es casi seguro el caso de la venta con upsell.
2. **`fbp` solo en 35.5% de los PageView.** El `_fbp` es la cookie que une el clic con la
   compra. En 2 de cada 3 visitas no se está sembrando → si alguien entra sin `fbp` y
   compra, Meta no puede conectar el clic con la venta.
3. **Ventana de atribución.** Default 7 días clic / 1 día visualización. Un comprador que
   tardó 8 días no se cuenta.

**Por qué importa más allá del reporte:** el algoritmo optimiza con lo que ve. Si ve 4 de 6
conversiones, está aprendiendo con **33% menos señal**. Sale a buscar gente parecida a 4
compradores en vez de 6. Eso te encarece cada venta siguiente. **Arreglar la medición no es
cosmético: es performance.**

## 1.5 Estructura de cuenta

**Opportunity Score: 99/100.** La estructura está bien, no es el problema.
Única recomendación de Meta: video vertical 9:16 a pantalla completa con audio en Reels
(estima -8% en costo por resultado). Relevante: **IG Reels es uno de tus 2 placements que vende.**

## 1.6 Tu error operativo

| Vos | Gaston Aguirre (competidor) |
|---|---|
| 7 creativos distintos | **29 anuncios activos** |
| $5-13 de gasto cada uno | Todos con **el mismo titular** |
| Ninguno con datos suficientes | Una ganadora escalada 29 veces |

Repartiste $67 entre 7 creativos. Ninguno juntó datos suficientes para que Meta aprenda.
El competidor encontró **una** ganadora y la clonó 29 veces. Esa es la diferencia operativa.

---

# PARTE 2 — LA COMPETENCIA

Barrido mundial en Ads Library. **9-10 anunciantes activos** sobre el mismo ángulo en español.

## 2.1 Los que importan

### 🐋 Cluster "Power Pet" (Brasil → LATAM) — valida la OFERTA
Fanpages: `Manual Powe Pet`, `Manual Power Pet`, `Power Pet`, `Nexusebook`,
`Manual Pet Prime`, `Pedro Oliveira`, `Ultranegócios Bruna`

- **El anuncio más viejo activo: 145 días.** Nadie banca gasto perdedor 5 meses.
- **La misma oferta en 6-7 fanpages distintas** = se esconde de los cloners. Señal de que convierte.
- Cuentas en BRL con creativos en español = atacan LATAM desde Brasil.
- Ángulo: *"Gana dinero creando snacks para mascotas"*, *"¿Quieres ganar dinero en dólares
  desde casa con un negocio que no para de crecer?"*
- **Veredicto: la oferta está validada. La longevidad de 145 días es la prueba más dura que da la Library.**

### 📈 Gaston Aguirre Entrenador Canino — el que está escalando ahora
`facebook.com/ads/library/?id=1103945928902593` · page `1293185060555800`

- **29 anuncios activos**, todos con el titular idéntico: *"Aprendé pastelería canina desde cero 👉"*
- Más viejo activo: **~10 días**. Cuenta en USD, voseo (AR/LATAM).
- Duplicación 29× del mismo creativo = ya ganó su test interno.
- Posicionamiento: marca personal de **entrenador canino** → autoridad.
- **Es el que hay que modelar primero.**

### 💵 CloudPets — la mejor estructura de hook que vi
page `485693804637447` · "Herramientas con IA para pastelería canina y felina"

- 10 anuncios, **precio en TODOS los titulares: `· US$17`**
- 3 hooks rotando, todos de curiosidad:
  - *"12 kg: 1 de maní y avena al día · US$17"* (dosis según peso)
  - *"Ninguna receta lleva estos 5 · US$17"* (negación/curiosidad)
  - *"¿Cuántas le doy? Según su peso · US$17"* (pregunta)
- Muy fresco (<1 día) = está testeando. Pero **la estructura del hook es oro.**

### 🇲🇽 Infinity Cursos — tu competidor directo en México
page `602697532923268`

- *"🧁 Curso + App + 50 Recetas por $199 MXN"*
- *"🧁 ¡Aprende a Hornear Snacks para tu Mascota por Solo $100!"*
- *"🐶🐱 Repostería para Lomitos y Michis"*
- ~13 días corriendo. **Mismo precio que vos (~$199 MXN ≈ $10 USD).**
- Vende **"Curso + App"**, no "ebook". Mayor valor percibido por el mismo precio.

### ⏳ Barkery en casa — señal de longevidad
page `155619625248201` — solo 3 anuncios pero **25 días activos sin pausa**.
*"Empieza a hornear desde casa este fin de semana 🦴"*

### Otros
| Anunciante | Señal | Ángulo |
|---|---|---|
| Mariana Rojas | 7 ads, 3 días | *"Hornea en casa en un fin de semana"* |
| Pcs cuisine | 8 ads, 11 días | *"✅TALLER REPOSTERIA CANINA"* |
| Dogtor Patitas | 14 días | *"+70 recetas para empezar desde casa"* |
| Entre Huellitas (PE) | 5 días | *"+50 lecciones"*, *"¡Aprende desde cero!"* |
| Emprende con Pastelería Canina | 2 días | *"¡¡¡75% DE DESCUENTO!!!"* |

## 2.2 Veredicto de mercado: **SUBNICHO — validado pero poblándose**

Demanda probada (145 días de longevidad en el cluster BR). Pero 9-10 anunciantes en el
mismo ángulo y **nadie domina México**. Hay espacio, pero ya no alcanza con "aprende
pastelería canina": hay que diferenciarse en **oferta y precalificación**, no en hook.

## 2.3 Lo que hay que copiar (en orden de impacto)

| # | Qué copiar | De quién | Por qué a vos te sirve específicamente |
|---|---|---|---|
| 1 | **Precio en el titular** (`· $199 MXN`) | CloudPets (10 ads), Infinity | **Arregla tu problema de clic basura.** Quien toca ya sabe que se paga. |
| 2 | **Ancla de cantidad alta** | Dogtor (+70 recetas), Entre Huellitas (+50 lecciones), Infinity (50 recetas) | Vos ofrecés **15 recetas**. En el estante sos el más flaco al mismo precio. |
| 3 | **"desde cero"** en vez de "desde casa" | Gaston (29 ads) | Habla al principiante sin experiencia. Es su única variable y la clonó 29 veces. |
| 4 | **Inmediatez de fin de semana** | Barkery (25 días), Mariana Rojas | *"Empezá este fin de semana"* vence la objeción "no tengo tiempo". |
| 5 | **Hook de curiosidad-negación + precio** | CloudPets | *"Ninguna receta lleva estos 5 · $199"* — curiosidad que igual precalifica. |
| 6 | **"Curso + App"** en vez de "ebook" | Infinity Cursos | Mismo precio, más valor percibido. Tus 5 bonos ya son eso, vendelos así. |
| 7 | **Escalar UNA ganadora a 10-20 copias** | Gaston (29×) | Tu error operativo exacto. |
| 8 | **Varias fanpages para la misma oferta** | Cluster Power Pet | Para cuando escales. No ahora. |

---

# PARTE 3 — PASO A PASO

## 🔴 FASE 0 — HOY. 30 minutos, $0, el de mayor impacto

### Paso 1 — Cortar los placements que no venden
En el ad set, pasar de Advantage+ placements a **placements manuales** y dejar solo:
- ✅ Facebook → Feed
- ✅ Instagram → Reels

Apagar todo lo demás (IG Feed, FB Reels, Stories, **Audience Network**, instream,
marketplace, search, WhatsApp).

> **Impacto:** recuperás los $38.15 de cada $67 que hoy se van a cero ventas.
> A tu CPA real de $7.33 en placements buenos, ese presupuesto son **~5 ventas más**
> con el mismo gasto. Es el cambio más rentable de toda esta lista.
>
> ⚠️ Nota: con poco presupuesto los placements manuales pueden subir el CPM. Si el CPM
> se te va más de 40% arriba, volvé a agregar IG Feed solamente.

### Paso 2 — Apagar los creativos muertos
`3 notas` ($13.01, **0 ventas**) y `4 carrusel` ($8.33, **0 ventas**).
$21 gastados, $0 vendidos. Ese ángulo ("recetas lindas") está probado y perdió.

### Paso 3 — Reactivar `2 video neg`
ROAS **1.39**, está pausado. Es tu segundo mejor anuncio.

---

## 🟠 FASE 1 — ESTA SEMANA. Arreglar la medición

### Paso 4 — Verificar que los TRES upsells disparen `Purchase`
El de **$4.90 ya dispara** (se reconstruyó desde el ROAS reportado). Confirmar que los
dos de **$5.90** también lo hagan, cada uno con su valor real.

> Corrección respecto de la versión anterior de este documento: el upsell **no** era la
> causa de las ventas faltantes. Las 2 ventas que faltan son de ebook y la causa es `fbp`.

### Paso 5 — Mandar el valor real en cada Purchase
Verificar que el evento envíe `value` y `currency` con el monto cobrado de verdad
(no un valor fijo). Sin eso no podés usar optimización por valor más adelante.

### Paso 6 — Arreglar la cobertura de `fbp` (35.5% → >90%)
Es lo que hace que se pierdan ventas atribuidas. Revisar:
- Que el código base del píxel cargue en **todas** las páginas, antes del contenido
- Que el banner de cookies no bloquee el píxel hasta aceptar
- Que checkout y landing estén en el **mismo dominio** (si el checkout es externo, hay que
  pasar `fbclid`/`_fbp` en la URL)
- Que esté activo el *first-party cookie* (ya lo tenés ✅)

### Paso 7 — Ampliar la ventana de atribución
Pasar a **7 días clic + 1 día visualización** si no está. Un infoproducto de $10 se
compra rápido, pero no siempre el mismo día.

### Paso 8 — Verificar deduplicación
Tu `Purchase` manda email + teléfono + external_id (EMQ 9.3 🟢), o sea que ya tenés API de
Conversiones corriendo. Confirmar que navegador y servidor usan el **mismo `event_id`**
para no contar doble.

---

## 🟡 FASE 2 — ESTA SEMANA. La oferta (lo que más mueve el ROAS)

> Un infoproducto no se arregla con creativos. Se arregla con oferta.
> Acá está tu mayor palanca y no cuesta un peso de pauta.

### Paso 9 — Repackagear: de 15 recetas a 50+
Tu competencia vende "+70 recetas", "+50 lecciones", "50 recetas". Vos "15 recetas"
**al mismo precio**. No hace falta escribir 35 recetas nuevas: contá lo que ya tenés
como unidades (variantes, tamaños, rellenos, versiones sin horno, para gato).

### Paso 10 — Dejar de venderlo como "ebook"
"Ebook + 5 bonos" → **"Curso + App + 50 recetas"** o **"Kit completo"**.
Infinity Cursos cobra lo mismo que vos y suena a tres veces más.

### Paso 11 — Poner el precio en el titular
`Pastelería canina desde cero · $199 MXN`
Precalifica el clic (tu problema #1) y es exactamente lo que hacen los 2 competidores
que mejor estructura tienen.

### Paso 12 — Sistematizar el upsell
Ya vendiste uno. Convertilo en parte del flujo para **todos**:
- **Order bump** en el checkout ($5-8: pack de etiquetas imprimibles, 20 recetas premium)
- **Upsell post-compra** ($15-25: plantillas de precios, mini curso de ventas por WhatsApp)

> Con 30% de take rate a $15, cada 6 ventas te suma ~$27. Sobre $67 de gasto eso solo
> ya te mueve el ROAS de ~1.1 a ~1.5. **Es la vía más rápida y barata a la rentabilidad:
> no depende de la pauta.**

---

## 🟢 FASE 3 — PRÓXIMOS 7 DÍAS. Creativos

### Paso 13 — Subir los 5 creativos nuevos
Los que ya están hechos (ver `README.md`), **al mismo ad set** que `1 v prob.`,
para que compitan con la ganadora bajo el mismo aprendizaje.

### Paso 14 — Agregar 3 creativos con los ángulos robados
1. *"Pastelería canina desde cero · $199"* — el ángulo de Gaston + precio
2. *"Ninguna receta lleva estos 5 ingredientes · $199"* — negación de CloudPets
3. *"Empezá a hornear este fin de semana · 50 recetas"* — inmediatez de Barkery

### Paso 15 — Reels verticales 9:16 con audio
Lo pide Meta explícitamente (estima -8% en costo por resultado) y **IG Reels es uno de tus
2 placements que vende**. Los videos actuales no están optimizados para ese formato.

### Paso 16 — Regla de corte, sin excepciones
Mirar **CPA**, nunca CTR (ya sabés que el CTR te mintió):

| CPA | Acción |
|---|---|
| < $8 | Escalar |
| $8 - 12 | Dejar correr |
| > $15 o 0 ventas con $10 gastados | **Apagar** |

### Paso 17 — Cuando aparezca la ganadora, clonarla 10-20 veces
Como Gaston. No buscar la ganadora #2: multiplicar la #1.

---

## 🔵 FASE 4 — SEMANA 2-3. Escalar

### Paso 18 — Consolidar en una campaña CBO
Una campaña, **1-2 ad sets**, 6-10 creativos adentro. Dejar de fragmentar presupuesto.

### Paso 19 — Advantage+ Audience, público amplio
Con ~$10 de ticket no se puede pagar segmentación fina. Geo México + 25-55 + amplio.
Que el píxel (ya bien medido tras la Fase 1) encuentre al comprador.

### Paso 20 — Retargeting barato
Público de `InitiateCheckout` sin `Purchase` (últimos 14 días). Esa gente ya puso la
tarjeta. Es el CPA más bajo que vas a conseguir.

### Paso 21 — Subir presupuesto de a 20%, cada 3 días
Con ROAS >1.5 sostenido 3 días. Saltos más grandes reinician el aprendizaje.

### Paso 22 — Recién entonces, más fanpages
Cuando tengas una ganadora rentable, replicar la oferta en 2-3 fanpages como el cluster
Power Pet. Esto es para escalar algo que ya funciona, **no para arreglar algo que no**.

---

# PARTE 4 — LA MATEMÁTICA

Mismo presupuesto de **$67.48**, usando tu CPA real de **$7.33** en placements limpios
y los precios confirmados.

| Escenario | Ventas | Ingreso | ROAS |
|---|---|---|---|
| Hoy (lo que ve Meta) | 4 | $40.50 | **0.60** |
| Hoy (real) | 6 | $58.30 | **0.86** ← perdés $2.35 por venta |
| **+ Fase 0** (cortar placements) | 9.2 | $89.42 | **1.33** ✅ |
| **+ Fase 2** (escalera de upsells al 35%) | 9.2 | $99.85 | **1.48** |
| **+ precio a $14.90** (asumiendo CVR −20%) | 7.4 | $124.05 | **1.84** |

> El salto de 0.86 → 1.33 es **solo apagar placements**. No cuesta un peso.
> El salto de 1.33 → 1.84 es **oferta y precio**. Tampoco cuesta pauta.
> **Ni un solo tramo de esta tabla depende de hacer mejores creativos.**

## Las 3 cosas que importan si solo hacés tres

1. **Cortar Audience Network y los placements de $0 ventas** → de ROAS 0.86 a ~1.33
2. **Arreglar `fbp` (35.5% → 90%)** → Meta deja de volar ciego con 31% del ingreso invisible
3. **Arreglar la escalera de upsells y subir el precio a $11.90-14.90** → te sube el CPA que podés pagar de $9.72 a ~$16.85

## Por qué el precio es la palanca decisiva

A $8.90 estás comprando tráfico en México con el ticket más bajo del nicho:

| Competidor | Precio |
|---|---|
| **Vos** | **$8.90** |
| Infinity Cursos (MX) | $199 MXN ≈ $10.80 |
| CloudPets | **US$17** |

CloudPets tiene **casi el doble de margen por venta** para pagar el mismo clic. Puede
sobrevivir a un CPA de $17 donde vos morís a $10. En una subasta donde todos compran la
misma atención, **el que tiene más AOV gana** — no el que tiene mejor creativo.

## Datos confirmados por el anunciante
- Ebook: **$8.90 USD**
- Upsells disponibles: **$5.90, $5.90, $4.90**
- Ventas reales: **6 ebooks + 1 upsell de $4.90** = $58.30
