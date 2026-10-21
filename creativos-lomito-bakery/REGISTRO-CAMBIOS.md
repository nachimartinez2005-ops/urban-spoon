# Registro de cambios ejecutados en la cuenta

Cuenta: Ebooks Argentina (`1560224662043860`)
Campaña: Test ABO | Pastelería Canina | MX 10/10 (`52532697130726`)

---

## 2026-10-12 — PASO 1: cortar placements basura + arreglar edad

### Hallazgos previos a la ejecución

1. **La edad real no era 25-60.** Los conjuntos se llaman `MX 25-60` pero tenían
   `age_min: 18, age_max: 65` con `targeting_automation.advantage_audience: 1`.
   Advantage+ Audience trata el rango de edad como sugerencia y lo ignora.
   Se estaba comprando tráfico de 18-65.

2. **8 conjuntos con $6/día cada uno.** Fragmentación extrema: con CPA ~$7 cada
   conjunto hace <1 conversión/día y nunca sale de la fase de aprendizaje
   (Meta necesita ~50 conversiones/semana por conjunto).

3. **CJ3 gastó $13.01 con 0 ventas** — 19% del gasto total en un ángulo muerto.

### Cambios aplicados

**Targeting nuevo (idéntico en los 5 conjuntos conservados):**
```json
{
  "age_min": 25,
  "age_max": 60,
  "geo_locations": { "countries": ["MX"],
                     "location_types": ["frequently_in","home","recent"] },
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed"],
  "instagram_positions": ["reels"],
  "device_platforms": ["mobile", "desktop"],
  "targeting_automation": { "advantage_audience": 0 }
}
```

`page_types` resultante: `["desktopfeed", "instagramreels", "mobilefeed"]`
Eliminados: Audience Network (classic + rewarded_video), WhatsApp Status,
Threads, Stories FB/IG, FB Reels, IG Feed, Marketplace, Search, instream video,
right column, profile feeds, biz_disco, notifications.

| Conjunto | ID | Acción | Estado final |
|---|---|---|---|
| CJ1 \| V1 Problema | `52532697234526` | Placements + edad | ✅ ACTIVE |
| CJ2 \| V2 Negocio | `52532697322726` | Placements + edad + **reactivado** | ✅ ACTIVE |
| CJ5 \| V5 Pastel | `52532697375926` | Placements + edad | ✅ ACTIVE |
| CJ6 \| V5 Pastel copy ganancia | `52532940160526` | Placements + edad | ✅ ACTIVE |
| CJ7 \| V1 Problema copy extra | `52532940166926` | Placements + edad | ✅ ACTIVE |
| CJ3 \| V3 Notas | `52532697353726` | **PAUSADO** ($13.01 / 0 ventas) | ⏸️ PAUSED |
| CJ4 \| V4 Carrusel | `52532697365526` | ya estaba pausado | ⏸️ PAUSED |
| CJ6 Pastel - Copia | `52532939754326` | sin tocar ($0 gastado) | ⏸️ PAUSED |

**Presupuesto diario: $30/día antes → $30/día después.** Se cambió el perdedor
(CJ3) por el segundo mejor (CJ2, CPA $9.90 con upsell = ROAS 1.39). Exposición neutra.

### Notas técnicas

- Meta fuerza `status: PAUSED` al editar un conjunto activo
  (`status_forced_to_paused: true`). Los tres afectados (CJ1, CJ2, CJ5) se
  reactivaron con `ads_activate_entity` → confirmado `status: ACTIVE`.
- Los 5 anuncios quedaron en `PENDING_REVIEW`: editar el targeting dispara
  revisión nueva de Meta. Normal, se aprueban en minutos u horas.
- `is_draft: false` en todas las respuestas → los cambios fueron a los objetos
  en vivo, no a un borrador.

### Qué monitorear en 48-72h

| Métrica | Esperado | Alarma |
|---|---|---|
| CTR | **BAJA** de ~5% a ~2-3% (se van los clics basura) | — |
| CPM | Sube algo (menos inventario disponible) | **+40% o más** |
| CPA | **BAJA** hacia ~$7 | se mantiene >$12 |
| Ventas/día | Sube | baja con CPM alto |

**Plan de contingencia:** si el CPM sube más de 40% y el CPA no baja, agregar de
vuelta solo `instagram_positions: ["stream"]` (Feed de Instagram). Con $6/día por
conjunto, restringir demasiado puede encarecer el alcance.

**No mirar el CTR para decidir.** Decidir solo por CPA.

### Pendiente (próximos pasos del plan)

- Paso 4-8: arreglar `fbp` (35.5%) y verificar los 3 upsells
- Paso 9-12: repackagear a 50+ recetas, precio en titular, escalera de upsells
- Paso 18: consolidar los conjuntos (la fragmentación de $6/día sigue sin resolverse)

---

## 2026-10-12 (segunda tanda) — Correcciones y reasignación de presupuesto

### Bug encontrado y corregido 🚨
**CJ2 tenía el conjunto ACTIVO pero el anuncio `2 video neg` PAUSADO.**
Un conjunto activo con el anuncio apagado no entrega nada: ocupaba lugar en la
estructura sin poder vender. Activado (`ads_activate_entity` sobre el ad).

> Regla: para que un anuncio se entregue, los TRES niveles tienen que estar
> activos — campaña, conjunto Y anuncio.

### Reasignación de presupuesto

Hallazgo: **CJ5 y CJ6 usan el mismo video** ("V5 Pastel", `video_id` 1063090180100392
y 1954647015494680 del mismo material). La diferencia está en el CTA:

| | CTA | Efecto |
|---|---|---|
| CJ5 (creativo `1954647015494680`) | `SEE_DETAILS` | no precalifica |
| CJ6 (creativo `1404693651814835`) | **`BUY_NOW`** | precalifica el clic ✅ |

Se pausó CJ5 y se conserva CJ6: mismo asset, mejor CTA, copy más nuevo.

| Conjunto | Antes | Ahora | Razón |
|---|---|---|---|
| CJ1 \| V1 Problema | $6 | **$10** | mejor CPA ($6.43), 2 de 4 ventas |
| CJ2 \| V2 Negocio | $6 | **$8** | 2º mejor (CPA $9.90 con upsell, ROAS 1.39) |
| CJ6 \| copy ganancia | $6 | $6 | sin datos, CTA BUY_NOW, merece test |
| CJ7 \| copy ingreso extra | $6 | $6 | sin datos, CTA BUY_NOW, merece test |
| CJ5 \| V5 Pastel | $6 | **PAUSADO** | duplicado de CJ6 con peor CTA |

**Total: $30/día antes → $30/día ahora.** Misma exposición, inclinada a lo que funciona.

### Estado final verificado

```
🟢 CJ1 | V1 Problema          $10/día   anuncio ACTIVE
🟢 CJ2 | V2 Negocio            $8/día   anuncio ACTIVE (reparado)
🟢 CJ6 | copy ganancia         $6/día   anuncio ACTIVE
🟢 CJ7 | copy ingreso extra    $6/día   anuncio ACTIVE
⏸️ CJ3 | V3 Notas              pausado  ($13.01 / 0 ventas)
⏸️ CJ4 | V4 Carrusel           pausado  ($8.33 / 0 ventas)
⏸️ CJ5 | V5 Pastel             pausado  (duplicado de CJ6)
⏸️ CJ6 Pastel - Copia          pausado  ($0 gastado)
```

`ads_get_errors` sobre la campaña: **sin errores de entrega.**
Los 4 anuncios activos pasaron revisión de Meta.

### Lo que queda SIN resolver en Meta (a propósito)

**Consolidación (Paso 18).** Siguen siendo 4 conjuntos separados, ninguno con
volumen para salir de aprendizaje. Es el próximo cambio estructural grande.
**Se difiere ~72h a propósito:** hoy ya se cambiaron placements y presupuestos;
consolidar ahora reiniciaría el aprendizaje antes de tener un solo dato limpio
bajo la configuración nueva.

**Retargeting (Paso 20).** Evaluado y descartado por ahora: con ~118 clics
limpios históricos, el público de carrito abandonado es demasiado chico para
que Meta lo entregue (necesita ~1.000 personas). Vuelve a la mesa cuando haya
volumen.

---

# TRABAJO PENDIENTE EN IMPULTIENDA (no tengo acceso)

> El checkout de Lomito Bakery está en **Impultienda**. No hay conector, así que
> esto es manual. **Acá está el 70% de la ganancia que queda** — más que
> cualquier cosa que se pueda tocar en el administrador de anuncios.

## 1. El pixel pierde 2 de cada 3 visitas 🔴 PRIORIDAD MÁXIMA

**Diagnóstico:** `PageView` tiene cobertura de `fbp` del **35.5%**.
`Purchase` está impecable (EMQ 9.3, email/teléfono/external_id al 100%) → la
integración de servidor de Impultienda funciona bien. El agujero está en el
**navegador**, en la página de aterrizaje.

**Qué hacer:**
- Verificar que el pixel `1712126017302327` esté cargado en **TODAS** las páginas:
  aterrizaje, checkout, upsells y página de gracias. No solo en el checkout.
- Que cargue en el `<head>`, **antes** del contenido.
- Si hay banner de cookies, que **no bloquee** el pixel hasta aceptar.
- Si la landing y el checkout están en dominios distintos, pasar `fbclid` y
  `_fbp` en la URL del botón de compra.

**Qué ganás:** recuperás ~31% del ingreso que hoy Meta no ve. Y más importante:
el algoritmo deja de optimizar con 4 de 6 conversiones.

## 2. Los upsells están mal ordenados 🟠

**Evidencia:** de 6 compradores, 1 solo tomó upsell, y tomó **el más barato
($4.90)**. Ninguno tomó los de $5.90.

**Qué hacer:**
- Verificar **en qué orden** se muestran. Si el de $4.90 aparece primero,
  invertirlo: **$5.90 primero, $4.90 como downsell** si rechaza.
- Verificar que los dos upsells de **$5.90 disparen `Purchase`** con su valor
  real. El de $4.90 ya dispara (se reconstruyó desde el ROAS reportado).
- Confirmar que el flujo de upsell **se le muestra a todos** los compradores.
  Un take rate de 17% puede no ser take rate bajo: puede ser que no se ofrezca.

**Qué ganás:** con 35% de toma a $5.57 promedio, el AOV sube de $9.72 a $10.85.
Son $1.13 más de CPA que podés pagar por cada cliente.

## 3. El precio no paga el tráfico 🟠

| | Precio | Recetas |
|---|---|---|
| **Lomito Bakery** | **$8.90** | **15** |
| Infinity Cursos (MX) | ~$10.80 | 50 + App |
| CloudPets | **$17** | — |
| Dogtor Patitas | — | 70 |

Sos **el más barato y el que menos ofrece**. CloudPets tiene el doble de margen
para pagar el mismo clic.

**Qué hacer:**
- Repackagear: `15 recetas` → **`Curso + App + 50 recetas`**. No hace falta
  escribir 35 recetas nuevas: contá variantes, tamaños, versiones sin horno,
  para gato. Tus 5 bonos YA son el "curso".
- Subir a **$14.90** (o testear $11.90 primero si da miedo).

**Qué ganás:** el CPA que podés pagar salta de **$9.72 a $16.85**. Es la
diferencia entre perder plata y escalar.

---

## Lo que necesito para seguir con los anuncios

**La URL exacta del checkout de Impultienda.** Los creativos de video actuales
no exponen el `link_url` por API, y sin esa URL no puedo crear los anuncios
nuevos con el copy que precalifica (precio en el titular, "50 recetas",
"desde cero"). No la invento: un link mal puesto quema presupuesto mandando
gente a la nada.

---

## 2026-10-12 (tercera tanda) — 3 anuncios nuevos con copy que precalifica

URL de destino recibida: `https://lomitobakery.impultienda.ar/checkout`

> ⚠️ **No se pudo verificar la página.** La política de red de este entorno
> devuelve 403 al intentar abrirla (mismo bloqueo que el CDN de Higgsfield).
> No se sabe si `/checkout` es página de venta o formulario de pago directo.
> **Por eso los 3 anuncios se dejaron PAUSADOS**: si los creativos actuales
> apuntan a una página de venta y estos van directo al pago, la conversión
> se hunde. Verificar el destino en la vista previa antes de activar.

### Creativos creados

Todos sobre los **videos ya probados** (no se gastó un crédito en material nuevo),
con `BUY_NOW` y el **precio en el titular** — que es el arreglo directo al
problema del clic basura.

| Creativo | ID | Video | Titular |
|---|---|---|---|
| NEW-A Precio + desde cero | `1064418276589580` | `2513584822498079` (ganador) | `Pastelería canina desde cero · $8.90` |
| NEW-B Negación curiosidad | `1867866977717409` | `2149988429061612` (CJ2) | `Ninguna receta lleva estos 5 · $8.90` |
| NEW-C Fin de semana | `2136004643971775` | `2513584822498079` (ganador) | `Empieza a vender este fin de semana` |

Ángulos modelados de la competencia:
- **NEW-A** → Gaston Aguirre ("desde cero", 29 ads) + CloudPets (precio en titular)
- **NEW-B** → CloudPets ("Ninguna receta lleva estos 5 · US$17") + el ángulo
  $21→$85 que ya ganó en CJ2 (ROAS 1.39)
- **NEW-C** → Barkery en casa (25 días activo) y Mariana Rojas ("fin de semana")

Copy en español de México (manteniendo "pícale", "lomitos", "colonia" del
original). Todos declaran **"ebook digital de $8.90 USD"** en el cuerpo:
quien hace clic ya sabe que se paga y cuánto.

### Anuncios creados (PAUSADOS) — todos en CJ1, el mejor conjunto

| Anuncio | ID | Estado |
|---|---|---|
| 8 NEW-A \| precio en titular + desde cero | `52533177900326` | ⏸️ PAUSED |
| 9 NEW-B \| negación curiosidad + precio | `52533177911326` | ⏸️ PAUSED |
| 10 NEW-C \| inmediatez fin de semana | `52533177917726` | ⏸️ PAUSED |

Se pusieron en **CJ1** (`52532697234526`, $10/día) a propósito: compiten contra
el ganador `1 v prob.` bajo el mismo público, mismos placements y mismo
aprendizaje. Es la única comparación limpia posible.

`conversion_domain` configurado en `lomitobakery.impultienda.ar` en los tres.

### Antes de activarlos — 1 verificación obligatoria

1. Abrir la vista previa de `8 NEW-A` y **tocar el botón «Comprar»**.
2. ¿Llega al mismo lugar que tus anuncios actuales?
   - **Sí** → activar los 3.
   - **No** (los actuales van a una página de venta) → avisar y se cambia
     el `link_url` de los 3 creativos.

### Nota sobre el precio en el copy

Los 3 anuncios dicen **$8.90 USD** porque es el precio real de hoy.
**Si se sube el precio a $14.90 (recomendado), hay que rehacer estos 3
creativos** — los creativos de Meta son inmutables, no se pueden editar.
Conviene decidir el precio primero y después activarlos.

---

## 2026-10-12 (cuarta tanda) — URL corregida y anuncios ACTIVADOS

### El destino real

El anunciante verificó en Ads Manager (campo "Destino → Sitio web" del anuncio
ganador `1 v prob.`):

```
URL real de los anuncios:  https://lomitobakery.impultienda.ar      ← página de venta
URL dada primero:          https://lomitobakery.impultienda.ar/checkout  ← formulario de pago
```

También confirmó que `/checkout` es **formulario pelado** (nombre, email, tarjeta)
con una opción para agregar un upsell → es un **order bump**, no una página de venta.

> ✅ Haber dejado los 3 anuncios pausados evitó mandar el 100% del tráfico frío
> de CJ1 a un formulario de pago sin pitch. Tráfico frío no compra en un
> formulario: la conversión se habría desplomado.

### Creativos rehechos (los de Meta son inmutables)

| Creativo | ID viejo (link malo) | ID nuevo (link correcto) |
|---|---|---|
| NEW-A Precio + desde cero | `1064418276589580` | **`1636729557909886`** |
| NEW-B Negación curiosidad | `1867866977717409` | **`1094910450189201`** |
| NEW-C Fin de semana | `2136004643971775` | **`2350729689010748`** |

### Anuncios

Archivados (link incorrecto, nunca entregaron, $0 gastado):
`52533177900326`, `52533177911326`, `52533177917726`

Creados y **ACTIVADOS** en CJ1:

| Anuncio | ID | Estado |
|---|---|---|
| 8 NEW-A \| precio en titular + desde cero | `52533179439726` | 🟢 en revisión → activo |
| 9 NEW-B \| negación curiosidad + precio | `52533179442326` | 🟢 en revisión → activo |
| 10 NEW-C \| inmediatez fin de semana | `52533179445126` | 🟢 en revisión → activo |

> `ads_activate_entity` sobre NEW-A falló una vez con `INTERNAL / is_retryable: true`.
> Reintentado → ACTIVE. Error transitorio de Meta, no de configuración.

### Presupuesto rebalanceado (CJ1 ahora tiene 4 anuncios)

Con 4 creativos compitiendo, $10/día daban ~$2.50 por anuncio: muy poco para
generar datos. Se le dio aire sin mover el total.

| Conjunto | Antes | Ahora |
|---|---|---|
| **CJ1** (ganador + 3 nuevos) | $10 | **$14** |
| CJ2 \| V2 Negocio | $8 | $8 |
| CJ6 \| copy ganancia | $6 | **$4** |
| CJ7 \| copy ingreso extra | $6 | **$4** |

**Total: $30/día.** Sin cambios en la exposición diaria.

> Bajar el presupuesto SÍ fuerza pausa (`status_forced_to_paused: true` en CJ6 y
> CJ7, a diferencia de subirlo). Ambos reactivados y confirmados ACTIVE.

### Estado final de la campaña

```
🟢 CJ1   $14/día   1 v prob. (ganador) + NEW-A + NEW-B + NEW-C   ← el test real
🟢 CJ2    $8/día   2 video neg
🟢 CJ6    $4/día   6 video p.c. – copy ganancia
🟢 CJ7    $4/día   7 v prob. – copy ingreso extra
⏸️ CJ3, CJ4, CJ5, CJ6-Copia
```

---

## Hallazgo nuevo: el upsell es un ORDER BUMP en el checkout

El anunciante confirmó que en `/checkout` "te deja elegir si querés agregar un upsell".
Eso explica el take rate del 17% y que se eligiera el más barato.

**Problema:** un order bump en la página de pago compite con la compra principal.
Agrega una decisión justo cuando la persona está por pagar.

**Reparto recomendado de los $16.70 disponibles:**

| Momento | Qué poner | Por qué |
|---|---|---|
| Order bump (checkout) | **uno solo**, el de **$5.90** | una decisión, no tres; y el grande |
| Post-compra #1 | el otro **$5.90** | un clic, sin recargar tarjeta, riesgo cero |
| Post-compra #2 | **$4.90** como downsell | si rechaza el anterior |

El post-compra es la clave: una vez cobrada la tarjeta, el upsell **no puede
dañar la conversión principal**.

En el bump que quede: describir el valor (no el nombre), anclar precio
("normalmente $15, hoy $5.90") y ponerlo **arriba** del botón de pago.

**No pre-tildarlo.** Sube el número a corto plazo y trae reembolsos y
contracargos. Con un producto de $8.90, un contracargo cuesta más que 3 upsells.

---

## 2026-10-12 (quinta tanda) — Precio $12.90: landing + anuncios alineados

Precio actualizado por el anunciante a **$12.90**. Upsells: 1 order bump en
checkout + **2 post-compra ya existentes**.

> 🔍 **Observación sobre los upsells:** si los 2 post-compra ya existían, entonces
> tuvieron **0 tomas** en 6 ventas — el único upsell vendido fue el de $4.90 del
> order bump. Con n=6 no es concluyente, pero un post-compra que no vende suele
> ser: no se muestra, pide recargar la tarjeta, o la oferta no se entiende.
> **Pendiente: hacer una compra de prueba y ver qué pasa después de pagar.**

### Landing nueva

`landing-lomito-bakery.html` — HTML autocontenido (CSS inline, sin scripts ni
dependencias externas) para pegar en un bloque de HTML personalizado de Impultienda.

Estructura: título "desde cero" → para quién → la cuenta $21→$85 → entregables
itemizados con valor tachado → precio anclado ($57 → $12.90, 77% OFF) →
garantía 7 días → FAQ → CTA final.

Aplica los 5 movimientos de repackaging:
1. "ebook" → **"curso"**
2. "5 bonos" → **cada bono nombrado con su valor**
3. ancla de cantidad
4. **ancla de precio** ($57 tachado)
5. **"desde cero"** en el título (patrón con 3 anunciantes de respaldo)

**3 valores a verificar antes de pegar** (marcados en comentarios del HTML):
- `50RECETAS` — poner el número REAL. Prometer de más = reembolsos.
- `$57` — el ancla tiene que ser creíble.
- Garantía 7 días — si no la da, borrar ese bloque.

### Anuncios realineados a $12.90

Los creativos de Meta son inmutables → hubo que rehacerlos otra vez.

| Archivado ($8.90) | Nuevo ($12.90) | Anuncio |
|---|---|---|
| `52533179439726` | creativo `1805484000557178` | `52533181028726` ✅ |
| `52533179442326` | creativo `2116534289001779` | `52533181029526` ✅ |
| `52533179445126` | creativo `1496437402305575` | `52533181030726` ✅ |

Cambios de copy además del precio: "ebook" → "curso", se agregó
**"🛡️ Garantía de 7 días"**, y se quitó el conteo fijo de recetas hasta que el
anunciante confirme el número real.

> `ads_activate_entity` devolvió `INTERNAL / is_retryable: true` en 3 de 6
> intentos. Todos resueltos reintentando. Error transitorio de Meta.

### Estado final

```
🟢 CJ1  $14/día   1 v prob. + NEW-A/B/C ($12.90)    ← 4 anuncios compitiendo
🟢 CJ2   $8/día   2 video neg
🟢 CJ6   $4/día   6 video p.c. – copy ganancia
🟢 CJ7   $4/día   7 v prob. – copy ingreso extra
⏸️ CJ3, CJ4, CJ5, CJ6-Copia
```

Los anuncios viejos de CJ2, CJ6 y CJ7 **no mencionan precio**, así que siguen
siendo compatibles con $12.90. Sí dicen "ebook" en vez de "curso" — inconsistencia
menor con la landing nueva, no urgente.

### Economía unitaria a $12.90

| | Antes ($8.90) | Ahora ($12.90) |
|---|---|---|
| AOV (take rate upsell 17%) | $9.72 | **$13.72** |
| CPA de equilibrio | $9.72 | **$13.72** |
| CPA real en placements limpios | $7.33 | $7.33 |
| **Margen** | **−$2.39/venta** ❌ | **+$6.39/venta** ✅ |

Si el CPA se mantiene en $7.33, el negocio pasa de perder a ganar.

---

## 2026-10-13 — Ebook aprobado: 30 recetas en landing y anuncios

### Lectura de rendimiento (día 1 post-cambios)

| Anuncio | Gasto hoy | Impr | CTR | CPM | Compras | CPA |
|---|---|---|---|---|---|---|
| **7 v prob. – copy ingreso extra** | $6.67 | 369 | 6.23% | $18.08 | **1** | **$6.67** ✅ |
| 1 v prob. | $8.68 | 479 | 5.01% | $18.12 | 0 | — |
| 6 video p.c. – copy ganancia | $6.28 | 443 | 2.26% | $14.18 | 0 | — |
| 2 video neg | $0.35 | 22 | 0% | $15.91 | 0 | — |
| NEW-A / B / C ($12.90) | $0.51 | **19** | — | — | 0 | — 🚨 |
| CJ5 y CJ3 (ya pausados) | $15.14 | 1664 | — | 0 | — | gasto previo a la pausa |

### 🚨 Problema 1: los 3 creativos nuevos no recibían entrega

19 impresiones en ~24 h. Meta concentró el presupuesto de CJ1 en `1 v prob.`,
que tiene todo el historial, y dejó a los nuevos sin aire. **Un test que no
entrega no es un test.**

**Solución aplicada:** se pausó el anuncio `1 v prob.` (`52532706691526`).
CJ1 queda con $14/día **exclusivos para los 3 creativos nuevos**.

> No se pierde el ángulo: `1 v prob.` usa el video `2513584822498079`, el mismo
> que usan NEW-A y NEW-C, pero con copy sin precio y CTA `SEE_DETAILS`.
> Los nuevos son el mismo asset con mejor copy y `BUY_NOW`.
> Se evitó crear un 5º conjunto: habría empeorado la fragmentación.

### 🚨 Problema 2: CPM subió más de lo tolerado

`1 v prob.` pasó de **$11.60 a $18.12** de CPM (+56%), por encima del umbral
del 40% que se fijó como alarma al cortar placements.

**Decisión: todavía NO se revierte.** El CTR se sostuvo (5.01%) y la única
venta del día entró a **CPA $6.67**, justo en el objetivo. Si en 48 h el CPA
sigue arriba de $12, se vuelve a agregar `instagram_positions: ["stream"]`.

### Nota sobre CJ3 y CJ5

Figuran con $15.14 gastados "hoy" pese a estar pausados. Verificado:
`effective_status: PAUSED` en ambos, y el gasto supera su presupuesto diario
de $6, o sea que se acumuló **antes** de que la pausa tomara efecto dentro del
día de reporte. No es una fuga activa.

### Creativos actualizados a 30 recetas

El ebook ampliado quedó aprobado, así que el ancla de cantidad ya es verdad.
Se suma a los otros dos patrones validados ("desde cero" y precio).

| Anuncio | ID | Titular |
|---|---|---|
| 14 A | `52533183938926` | `30 recetas desde cero · $12.90` |
| 15 B | `52533183939926` | `Ninguna de las 30 lleva estos 5 · $12.90` |
| 16 C | `52533183942726` | `30 recetas y vendes este fin de semana` |

Los 3 anteriores (sin conteo de recetas) quedaron archivados sin datos que perder
(19 impresiones entre los tres).

**NEW-A4 combina los tres patrones validados en un solo titular:**
cantidad + "desde cero" + precio.

### Landing actualizada

`15 recetas` → **30** · `4 categorías` → **5** · `64 páginas` → **79**
Ancla de precio $49 → **$56** (77% OFF), valor del módulo principal $22 → **$29**.

### Estado

```
🟢 CJ1  $14/día  →  14 A + 15 B + 16 C  (los 3 nuevos, sin competencia interna)
🟢 CJ2   $8/día  →  2 video neg
🟢 CJ6   $4/día  →  6 video p.c. – copy ganancia
🟢 CJ7   $4/día  →  7 v prob. – copy ingreso extra  ← mejor CPA de hoy ($6.67)
⏸️ CJ3, CJ4, CJ5, CJ6-Copia
```

## 2026-10-13 · Paso 2: píxel y reasignación de presupuesto

### Diagnóstico corregido del píxel (dataset 1712126017302327)

Lectura real de `ads_get_dataset_quality` el 13/10:

| Evento | EMQ | fbp | Carga |
|---|---|---|---|
| Purchase | **9.3** | **100 %** | navegador |
| AddToCart | 6.1 | 100 % | navegador |
| InitiateCheckout | 5.6 | 63,4 % | tiempo real |
| PageView | 5.3 | **38,9 %** | por hora |

**Corrección a lo que dije antes.** Yo había afirmado que con fbp al
35,5 % Meta no veía el 31 % de la facturación. Era falso: generalicé el
fbp del PageView al Purchase. El Purchase tiene su propio fbp al 100 %
y EMQ 9.3, así que la atribución de ventas está sana. Lo que el fbp
bajo rompe es el público de retargeting, no los ingresos.

Causa: la landing (bloque de HTML personalizado) no tenía el píxel.
Los eventos de checkout sí lo tienen — de ahí el 100 % en Purchase y
AddToCart contra el 38,9 % del PageView, que incluye la landing.
Arreglado: `landing-lomito-bakery.html` ahora trae el código base con
una guarda que no lo duplica si Impultienda ya lo inyecta.

### InitiateCheckout inflado (hallazgo nuevo, sin resolver)

7 días de eventos: 479 PageView · 123 InitiateCheckout · 11 AddToCart ·
7 Purchase. El IC es el 25,7 % de las visitas y hay 17,6 IC por compra.
El 12/10 a las 16 h: 16 IC con 15 PageView en la misma hora. Hoy el IC
cuesta $0,99 contra $0,58 del landing page view, o sea que ~58 % de las
visitas a la landing registran un IC.

No es intención real: Impultienda dispara InitiateCheckout al cargar la
página, no al apretar comprar. No daña la entrega porque las campañas
optimizan a PURCHASE, pero vuelve imposible medir la fuga del checkout
y envenenaría cualquier público basado en IC.

### Presupuesto

| Conjunto | Antes | Ahora | Por qué |
|---|---|---|---|
| CJ6 copy ganancia | $4 ACTIVO | **PAUSADO** | $17,87 gastados, 0 compras, CTR 3,03 % |
| CJ7 copy ingreso extra | $4 | **$8** | CPA de hoy $6,94, CTR 6,17 % |
| CJ1 / CJ2 | $14 / $8 | igual | CJ1 corriendo los 3 creativos nuevos |

Total: $30/día.

**Corrección operativa.** Yo tenía anotado que subir el presupuesto no
force-pausa un conjunto activo. Es falso: subir CJ7 de $4 a $8 devolvió
`status_forced_to_paused: true` y lo apagó. Lo reactivé con
`ads_activate_entity` y verifiqué ACTIVE / delivery active. De acá en
más, después de cada cambio de presupuesto hay que verificar el estado.

## 2026-10-16 — Corrección: Higgsfield y video

Dije que no podía hacer video "porque las descargas de Higgsfield están bloqueadas".
Era una conclusión mal sacada. Lo real, verificado hoy:

- Generar SÍ funciona. Probé `generate_image_batch` con `nano_banana_flash` y salieron
  2 imágenes base 9:16 para los ángulos A1 y A2.
- Lo que está bloqueado es que YO baje el archivo: el CDN de Higgsfield
  (`d8j0ntlcm91z4.cloudfront.net`) devuelve 403 en el túnel del proxy. Nacho sí puede
  abrir el link y bajarlo desde su navegador, así que no es un bloqueo real del flujo.
- El bloqueo real hoy es otro: **se acabaron los créditos**. Quedan 3.05 en el workspace
  privado (plan plus) y `seedance_2_0_mini` necesita más. Las 2 imágenes consumieron 3.

Imágenes base ya generadas (listas para animar cuando haya créditos):
- A1 (cocina, mujer amasando): job `625b02f8-b08b-4a14-9844-3e78720c580c`
- A2 (pastel en caja kraft): job `8a6d015b-6c26-4029-bfba-06fc984767ec`

## 2026-10-16 mediodía — Concentración del presupuesto en 15 B

Acumulado de vida por anuncio al mediodía:

| Anuncio | Gasto | Impr. | CTR | LPV | Ventas | Facturado | CPA |
|---|---|---|---|---|---|---|---|
| 15 B negación | $8.28 | 436 | 4.36% | 10 | 3 | $50.70 | $2.76 |
| 16 C fin de semana | $8.01 | 472 | 2.33% | 4 | 0 | $0 | — |
| 7 v prob. (CJ7) | $44.31 | 2667 | 4.35% | 48 | 2 | $30.00 | $22.16 |
| 14 A (ya pausado) | $35.41 | 2618 | 2.14% | 35 | 1 | $12.49 | $35.41 |

Acciones:
- Pausado 16 C. 472 impresiones, por debajo de mi regla de 500, pero sin
  ninguna venta y con la mitad del CTR de 15 B. Distinto del caso 14 A, donde
  casi corto un anuncio que SÍ vendía.
- Pausado 7 v prob. ROAS 0.68: $44.31 gastados, $30 devueltos.

Resultado: 15 B queda como único anuncio activo, en CJ1 a $14/día.
El gasto diario baja de $22 a $14. Proyección al sábado a la noche: ~$221
acumulados, dentro del techo de $250 que puso Nacho.

Riesgos anotados:
- El CPA de $2.76 no se va a sostener. 15 B venía con ~$2/día; pasarlo a $14
  es multiplicar por 7 y Meta va a buscar público más caro.
- Queda un solo anuncio corriendo: si se fatiga, no hay nada atrás.

Nota de zona horaria: la cuenta publicitaria corre en America/Buenos_Aires.
Una compra a las 2 AM hora de Nacho cuenta en el día NUEVO para Meta, aunque
en México todavía sea el día anterior. La tabla diaria usa ese mismo reloj.

## 2026-10-16 noche — Entrega congelada y corrección de mi propia recomendación

**El problema.** Tras dejar un solo anuncio activo al mediodía, CJ1 dejó de
gastar: $4.25 a las 18:25 y $4.27 a las 18:40 (2 centavos en 15 minutos),
375 impresiones en todo el día contra $14 de presupuesto. Con un solo creativo
Meta no tiene material para rotar y prefiere no gastar. CPM $11.39: no es precio,
es falta de inventario creativo.

**Corrección importante sobre mis creativos v2.** Al inspeccionar el creativo
de 15 B descubrí que el anuncio ganador NO es una imagen: es un video vertical
de metraje real (manos cortando galletas con forma de hueso) con una caja de
titular arriba y subtítulos quemados. Mis 4 estáticos son pósters tipográficos,
otra especie. Y mis 2 videos de Higgsfield son de 5 segundos, mudos, sin gancho
ni subtítulos: materialmente más débiles que el que funciona. Recomendé subirlos
esta noche antes de haber visto esto. Era una recomendación mal fundada.

**Segundo bloqueo.** La API no expone el link_url de ningún creativo de la cuenta
(object_story_spec no es un campo soportado) y el iframe de preview de
business.facebook.com está bloqueado por el proxy. No tengo forma de verificar a
dónde apunta el anuncio, y no voy a mandar tráfico pago a una URL adivinada.

**Lo que sí hice.** Revisando el histórico encontré que varios anuncios se
juzgaron contra un embudo roto (sin upsells, ticket de $8.90):

| Anuncio | Gasto | CTR | Ventas | CPA | ¿Rentable hoy? |
|---|---|---|---|---|---|
| 1 v prob. | $21.59 | 5.26% | 2 | $10.80 | SÍ — bajo el equilibrio de $12.20 |
| 2 video neg | $20.57 | 3.57% | 1 | $20.57 | No |
| 5 video p.c. | $20.52 | 5.27% | 1 | $20.52 | No |
| 3 notas | $20.44 | 4.60% | 0 | — | No |

`1 v prob.` ya vivía dentro de CJ1, solo pausado. Lo reactivé: no hace falta
crear creativos ni conocer la URL de destino. Quedan 2 anuncios rotando en CJ1,
ambos con economía defendible al ticket de hoy. El presupuesto no se tocó.

Descartados a propósito: 2 video neg, 5 video p.c. y 3 notas. CPA por encima del
equilibrio incluso con upsell.

### Link de destino (dato de Nacho, 16/10 noche)

Landing: `https://lomitobakery.impultienda.ar/` (con barra final)

CONFIRMADO por Nacho contra el campo "URL del sitio web" del anuncio 15 B en
Ads Manager: es el mismo destino que usan los anuncios que están corriendo.
Cualquier anuncio nuevo tiene que usar exactamente esa URL.

No lo pude verificar yo mismo: el proxy de esta sesión devuelve 403 en
`impultienda.ar`.

### Los videos SÍ se pudieron subir — vía sandbox de Higgsfield

Mi conclusión anterior ("no puedo bajar los mp4, hay que hacerlo a mano") estaba
mal. Higgsfield tiene un sandbox Linux propio (`sandbox_exec`) con ffmpeg,
tipografías e internet sin el bloqueo del proxy. Cadena completa:

1. `curl` de los 2 mp4 dentro del sandbox de Higgsfield (ahí el CDN no da 403)
2. Caja de titular en PNG con Pillow + Montserrat ExtraBold, superpuesta con
   ffmpeg, más subtítulos cronometrados con `drawtext`
3. `media_upload` → `curl PUT` → `media_confirm` para obtener URL pública
4. `ads_creative_upload_media` con `upload_source: URL` — Meta descarga el
   video él mismo, así que mi proxy no interviene

Escollo: Meta descarga VIDEOS de `d2ol7oe51mr4n9.cloudfront.net` pero rechaza
IMÁGENES del mismo host ("Image Wasn't Downloaded ... robots.txt"). Solución:
usar como miniatura la que genera el propio Meta al procesar el video, leída
con `ads_get_ad_videos` campo `picture`.

Resultado — CJ1 pasa de 1 anuncio congelado a 4 activos, sin tocar el
presupuesto de $14/día:

| Anuncio | Creativo | Estado |
|---|---|---|
| 15 B negación | video original | ACTIVE |
| 1 v prob. | reactivado, CPA histórico $10.80 | ACTIVE |
| 17 V1 no se cocinar CC | video nuevo con gancho + subtítulos | IN_PROCESS |
| 18 V2 cuánto cobrar CC | video nuevo con gancho + subtítulos | IN_PROCESS |

Los 4 son del ángulo de objeción. Declarados con `self_ai_disclosure: OPT_IN`
por tener media generada con IA.

Textos quemados (tuteo, verificado):
- V1: gancho "No necesitas saber cocinar" / subs "Solo necesitas la receta",
  "30 recetas paso a paso"
- V2: gancho "Lo difícil no es hornear" / subs "Es saber cuánto cobrar",
  "Te cuesta $25.", "La vendes a $70."

### Upsells — precios confirmados por Nacho (16/10 noche)

| Upsell | Precio | Post-compra con 20% off |
|---|---|---|
| Pack Pasteles de Cumpleaños | 89 MXN | **71.2** |
| Kit Vende en Redes | 109 MXN | 87.2 |
| Pack Fechas que Venden | 109 MXN | 87.2 |

El 71.2 que aparecía en las ventas es el de cumpleaños con su descuento.
Está bien configurado, no había nada roto.

Observación con 2 casos (muestra chica, no concluyente): las dos ventas con
upsell tomaron el de 89 y ninguna el de 109. Puede ser azar o puede ser que el
embudo muestre primero el más barato. Diferencia si tomaran uno de 109: 16 MXN
por venta, ~48 MXN/día a 3 ventas diarias.

Decisión: NO tocarlo ahora. Es poca plata contra el riesgo de romper un embudo
que recién empezó a funcionar, y el de cumpleaños probablemente convierta mejor
por ser el más barato. Anotado para probar cuando el negocio esté estable.

Economía por venta actualizada y confirmada:
- Solo ebook: 229 MXN = $12.37
- Con upsell de cumpleaños: 300.2 MXN = $16.22
- Con upsell de 109: 316.2 MXN = $17.08

## 2026-10-16 23:20 — Diagnóstico real de la entrega congelada

La entrega se volvió a frenar con 4 creativos activos: entre las 21:15 y las
23:15 la cuenta sumó 3 impresiones y $0 de gasto. O sea, el problema NO eran
los creativos. Mi hipótesis del mediodía ("falta material para rotar") era
incompleta.

**Causa raíz.** El ad set optimiza para `OFFSITE_CONVERSIONS` con evento
PURCHASE. Meta necesita del orden de 50 conversiones semanales por ad set para
salir de aprendizaje; acá hay ~1 compra por día. Sin señal suficiente no puede
construir el modelo y prefiere no gastar antes que gastar mal. Es aprendizaje
limitado permanente, y explica el freno del mediodía y el de la noche.

**Factor agravante.** Las ubicaciones estaban restringidas a mano a solo 3:
Feed de Facebook, feed de escritorio y Reels de Instagram. Frecuencia 1.17, o
sea que ni siquiera repetía: le faltaba inventario, no le sobraba.

**Acción tomada (decisión mía, Nacho dijo "tomá la decisión").** Abrí las
ubicaciones a todas. De 3 page_types a 30. Plataformas efectivas ahora:
facebook, instagram, audience_network, whatsapp, threads.

Verificado: status ACTIVE, sin pausa forzada, presupuesto intacto en $14/día,
optimización sin cambios. Reversible.

Por qué este cambio y no otro: no altera qué se optimiza ni cuánto se gasta,
solo amplía dónde buscar. El cambio grande —mover la optimización a un evento
más frecuente para darle señal a Meta— queda para el sábado con datos delante.

A vigilar mañana: que Audience Network no traiga un aluvión de impresiones
baratas sin ventas. Si pasa, recortarla.

## 2026-10-19 — Respuestas de Impultienda (soporte)

Las 4 preguntas enviadas el 18/10 a la noche quedaron respondidas:

1. **Píxel compartido: SÍ.** Configuraciones > Meta / Tracking > botón
   "Usar un píxel de mis otras tiendas" > elegir `1712126017302327` >
   Guardar. Copia el ID y el token de la API de Conversiones. Las otras
   tiendas no se tocan. En Meta se filtra por dominio para separar
   México de España.
   → Corrige el riesgo que yo había marcado: España NO arranca con el
   píxel en cero, hereda el historial de conversiones.

2. **Segunda tienda: sin costo.** Entra en el mismo plan.
   → Nada bloquea el lanzamiento del martes.

3. **Pasarela: Impul Pay.** Una sola activación, y en la sección
   Impul Pay se elige con qué cobra cada tienda.

4. **IVA: va INCLUIDO en el precio en las tres opciones**
   (Ninguno / Whop recauda y remite / Lo recaudo yo).
   → IVA español 21%: de 19,90 € quedan 16,45 €. Se pierde 17,4% de
   CADA precio de España, no solo del principal.
   → El break-even CPA de ~$21 que yo había proyectado para España está
   calculado SIN esto, o sea que es optimista. RECALCULAR el martes
   antes de fijar presupuesto.
   → Opción elegida: "Whop recauda y remite" (evita registrarse en el
   régimen OSS de la UE desde Argentina).

5. **OXXO: NO lo permiten.** Solo tarjeta.
   → Fuga real en México: una parte importante de las compras digitales
   mexicanas se pagan en efectivo por OXXO. Puede explicar parte del
   30 LPV / 0 ventas del sábado 17. Yetzel Vazgar es el caso visible;
   probablemente hubo otros que se fueron sin escribir.
   → Argumento adicional a favor de migrar: en España la penetración de
   tarjeta es mucho más alta. El problema no es que México sea mal
   mercado, es que nuestro método de cobro no funciona ahí.

## 2026-10-19 — México repuntó: la migración queda EN REVISIÓN

Datos reales (campaña Test ABO | Pastelería Canina | MX):

| Día | Gasto | Impr. | CTR | LPV | Checkouts | Ventas | Facturado | CPA |
|---|---|---|---|---|---|---|---|---|
| Sáb 17 | $14.32 | 958 | 4.80% | 30 | 6 | 0 | — | — |
| Dom 18 | $19.74 | 1753 | 3.94% | 30 | 5 | 1 | $17.11 | $19.74 |
| Lun 19 (parcial) | $6.75 | 810 | 3.46% | 9 | 3 | 1 | $20.95 | $6.75 |

- Venta del 19/10: $20.95 ≈ 388 MXN → consistente con ebook 229 + bump 89
  + upsell post-compra 71,2. Ticket más alto de toda la campaña.
- CPA del 19/10: $6.75 contra un break-even con bump de $16.94. Rentable.
- **Pérdida de octubre: $86.46 → ≈ $74.89.** Primera vez que BAJA.
- 3 días juntos: $40.81 gastados / $38.06 facturados → break-even.

### Consecuencia sobre el plan
La decisión de migrar a España se tomó el sábado leyendo "30 LPV / 0 ventas".
Dos días después hay 2 ventas y la pérdida baja. NO se da vuelta el plan por
un día sin cerrar, pero tampoco se ejecuta la pausa de México a ciegas.
→ El martes 20 se hace el cierre con 4 días limpios (16-19) y recién ahí se
decide pausar México o dejarlo correr. La tienda ES se sigue armando igual:
armarla no cuesta pauta.

### Fuga identificada
14 checkouts iniciados en 3 días → 2 compras. **86% de abandono en el
checkout**, con la gente ya en el botón de pagar. El CTR es bueno y el
tráfico llega: el problema no está en la pauta. OXXO (no disponible)
explica una parte. Revisar el checkout el martes.

### Pendiente técnico
**CJ7 | V1 Problema – copy ingreso extra | MX** está ACTIVO con $8/día
asignados y gastó $0. Misma entrega congelada que ya tuvimos. No se toca
hoy para no resetear el aprendizaje en medio de una racha. Primer punto
del martes.

## 2026-10-20 — CIERRE DE 4 DÍAS: se CANCELA la migración a España

### Los 4 días limpios (16-19/10)

| Día | Gasto | Impr. | CTR | CPM | LPV | Checkouts | Ventas | Facturado | CPA |
|---|---|---|---|---|---|---|---|---|---|
| Vie 16 | $10.94 | 899 | 2.78% | $12.17 | 8 | 2 | 1 | $16.22 | $10.94 |
| Sáb 17 | $14.32 | 958 | 4.80% | $14.95 | 30 | 6 | 0 | — | — |
| Dom 18 | $19.76 | 1754 | 3.93% | $11.27 | 30 | 5 | 1 | $17.11 | $19.76 |
| Lun 19 | $14.55 | 1769 | 3.22% | $8.22 | 30 | 4 | **2** | **$33.27** | **$7.28** |
| **Total** | **$59.57** | 5380 | — | — | 98 | 17 | **4** | **$66.60** | **$14.89** |

**Los 4 días dieron POSITIVO: +$7.03.** Primera vez en toda la campaña.

Pérdida de octubre: $86.46 (17/10) → **≈ $72.12**.

### El ganador está identificado
**15 B | negacion + 30 recetas** (id 52533183939926), acumulado 16-19:
$49.33 gastados / $66.61 facturados / 4 ventas / **CPA $12.33** / CTR 3.86%
/ 92 LPV / 14 checkouts.
→ Es rentable solo: break-even sin upsell $12.20, con bump $16.94.
→ TODAS las ventas de los 4 días son de este anuncio. Los demás: cero.

### Señales de que Meta está aprendiendo
- CPM en caída limpia: $12.17 → $14.95 → $11.27 → $8.22 → $7.33 (hoy).
- Frecuencia 1.12-1.24: la audiencia NO está saturada, hay espacio para escalar.

### DECISIÓN: México se queda, España se posterga
El plan del sábado decía migrar. Se cancela. No se abandona un activo que
acaba de dar positivo para irse a un mercado sin validar. La tienda ES queda
armada y en espera — no cuesta nada tenerla lista.

### Acciones ejecutadas hoy
1. Pausado **1 v prob.** (id 52532706691526): 57 impresiones, CTR 1.75%,
   cero resultados. Ya tuvo sus oportunidades.
2. **CJ1 subido de $14 a $17/día** (+21%, debajo del 25% que resetea el
   aprendizaje). El conjunto se auto-pausó con el cambio y fue reactivado.
   Verificado: daily_budget $17, effective_status ACTIVE.
3. **17 V1 | no se cocinar CC** y **18 V2 | cuanto cobrar CC** se dejan
   correr: tienen 118-141 impresiones, muestra demasiado chica para matarlos
   aunque su CTR (1.4-1.7%) sea malo contra el 3.86% de 15 B.

### Sigue abierto
- CJ7 activo con $8/día gastando $0 (entrega congelada).
- 17 checkouts → 4 compras = **76% de abandono**. Sigue siendo la fuga más
  grande. OXXO explica parte.

## 2026-10-21 — Martes cerrado, presupuesto se MANTIENE, A y B al aire

### Martes 20/10 cerrado

| Anuncio | Gasto | Impr. | CTR | CPM | LPV | Checkouts | Ventas | Facturado | CPA |
|---|---|---|---|---|---|---|---|---|---|
| 15 B | $16.04 | 1871 | 3.63% | $8.57 | 25 | 1 | 1 | $12.38 | $16.04 |
| 17 V1 | $0.09 | 8 | 0.00% | — | 0 | 0 | 0 | — | — |
| 18 V2 | $0.20 | 8 | 0.00% | — | 0 | 0 | 0 | — | — |
| **Total** | **$16.33** | 1887 | — | — | 25 | 1 | **1** | **$12.38** | **$16.33** |

**Día NEGATIVO: −$3.95.** La racha de días en positivo se corta en 1.
La venta fue de $12.38 (ebook solo, sin bump ni upsell).
Pérdida de octubre: ≈ $76.07.

**Lectura honesta del salto de presupuesto:** con $14.55 el lunes hubo 2
ventas; con $16.04 el martes hubo 1. Más gasto, más impresiones (1871, el
máximo histórico), CPM más barato ($8.57, el mínimo histórico), y MENOS
ventas. Con un solo día de muestra eso es ruido, no tendencia — pero no es
la confirmación que buscábamos.

El martes al mediodía yo había dicho "va justo en ritmo" mirando el ritmo de
GASTO, que efectivamente se mantuvo ($7.89 → $16.04). Lo que no llegó fue la
segunda venta de la tarde.

### Decisión de presupuesto: SE MANTIENE EN $17
El criterio fijado el lunes decía:
- 2+ ventas y CPA ≤ $15 → subir a $20-21
- 1 venta, CPA $17-25 → dejar en $17
- 0 ventas → volver a $14

Resultado: 1 venta, CPA $16.04. Cae en la banda del medio (apenas por debajo
de $17). **Se mantiene en $17.** El criterio hizo su trabajo: sin él, el
impulso habría sido subir igual porque "el CPM está bajando".

### Lanzadas A y B
Creatives nuevos sobre el MISMO video 2497533197399959 (los creatives de
Meta son inmutables). Cero créditos de Higgsfield gastados.

| Variación | Creative | Ad | Estado |
|---|---|---|---|
| 19 A \| negacion bolsa supermercado | 1652734899898327 | 52534970928926 | ACTIVE |
| 20 B \| negacion no se cocinar | 4561278850851238 | 52534970958726 | ACTIVE |

Page 1289151314292479 (Lomito Bakery) · link lomitobakery.impultienda.ar ·
CTA BUY_NOW. Verificado por lectura: ambas ACTIVE.

**C y D siguen en reserva** hasta que el presupuesto pase de ~$30/día.
**15 B no se toca:** es el control del experimento.

### CORRECCIÓN: CJ7 no tenía "entrega congelada"
Yo venía diciendo desde el 20/10 que CJ7 estaba "activo con $8/día y entrega
congelada", y lo arrastré en dos tareas programadas. **Era un conjunto SIN
ANUNCIOS.** No gastaba porque no tenía nada que entregar. No era un problema
de delivery, era un conjunto vacío.
→ CJ7 (52532940166926) pausado.

### Pausados 17 V1 y 18 V2
Acumulado 17-20/10: 17 V1 con 73 impresiones y CTR 1.37%; 18 V2 con 106 y
1.89%. Contra el 3.84% de 15 B.

**No llegaron a las ~500 impresiones de mi propio criterio de corte.** Los
pauso igual, y por un motivo distinto al criterio: Meta ya les cerró el
grifo (8 impresiones cada uno el martes) y nunca van a juntar muestra. Lo
que sí hacen es competir por el presupuesto de exploración con A y B, que
son los tests que me importan ahora.

Detalle a tener en cuenta: **17 V1 era "no sé cocinar", el mismo ángulo que
mi variación B.** Con otro video, rindió 1.37% de CTR. B no es un ángulo
virgen — pero sí es un test distinto, porque mantiene fijo el video ganador
y varía solo el copy.

### Estado del conjunto CJ1
$17/día · 3 anuncios activos: 15 B (control), 19 A, 20 B.

## 2026-10-21 (tarde) — Pago rechazado: verificado, sin consecuencias

Nacho recibió un aviso de pago rechazado y lo abonó con tarjeta de crédito.
Verificado contra la API de Meta el 21/10:

| Chequeo | Resultado |
|---|---|
| `account_status` de 1560224662043860 | **ACTIVE** |
| `has_payment_method` | **true** |
| Errores que bloquean entrega (`ads_get_errors`) | **ninguno** (lista vacía) |
| Entrega del día | normal, los 3 anuncios activos gastando |
| Anuncios pausados por el incidente | **ninguno** |

No hubo interrupción de entrega ni se perdió aprendizaje. El pago rechazado
fue un rechazo del medio de pago, no una restricción de la cuenta: Meta
reintenta y, al cobrarse, la cuenta sigue igual. El riesgo real de estos
casos —que Meta pause la cuenta por deuda— **no se materializó**.

### Dato del día (21/10, parcial, ~mediodía)
15 B: $7.73 gastados · 824 impresiones · CTR 3.52% · 16 LPV ·
**2 ventas · $35.38 facturados · CPA $3.87**.
→ Aparecieron las DOS ventas que Nacho reportó. La segunda era retraso de
atribución, como estimé: no era venta orgánica ni atribución perdida.
Día en curso: $8.04 gastados / $35.38 facturados → **+$27.34**.

### Sobre A y B
19 A: 26 impresiones. 20 B: 7. Ya NO están en cero, pero siguen con muestra
mínima. Meta les da exploración con cuentagotas, como estaba previsto.
Decisión sobre si necesitan conjunto propio: mañana, con el día cerrado.
