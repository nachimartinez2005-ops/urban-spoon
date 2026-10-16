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
