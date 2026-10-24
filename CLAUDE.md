# Contexto del negocio — leer antes de responder cualquier cosa

Este repo es la memoria del negocio. **No es un proyecto de software.** Es la
bitácora de un negocio de infoproductos (ebooks) que corre pauta en Meta Ads.

Si Nacho pregunta algo del negocio, la respuesta sale de estos archivos, no de
lo que vos supongas. Si no está escrito acá, no está verificado: decilo en vez
de completar el hueco.

---

## Regla cero: los números no se inventan

- Los datos de Meta salen de la **API de Meta Ads** (herramientas `mcp__meta_ads__*`),
  nunca de memoria ni de una estimación.
- Lo ya verificado está en `resumen-negocio/datos.md` con fecha y fuente.
- Si das un número, decí de dónde salió y de qué fecha es.
- Si un dato está viejo, traelo de nuevo de la API antes de decidir sobre él.

Esto ya falló antes: en octubre se manejó un presupuesto de "$250 de gasto"
cuando era "$250 de pérdida", y eso inventó una urgencia que no existía.

---

## Dónde está cada cosa

| Ruta | Qué es |
|---|---|
| `creativos-lomito-bakery/REGISTRO-CAMBIOS.md` | **La bitácora. El archivo más importante.** Todo cierre, decisión y dato diario va acá, al final, con fecha. |
| `creativos-lomito-bakery/README.md` | Diagnóstico de la campaña y los creativos |
| `creativos-lomito-bakery/PLAN-NOV-DIC.md` | Plan y presupuesto vigente (nov-dic 2026) |
| `creativos-lomito-bakery/PLAN-SEMANA-19-25-OCT.md` | Plan de la semana en curso |
| `creativos-lomito-bakery/VARIACIONES-15B.md` | Las 4 variaciones de copy del anuncio ganador |
| `creativos-lomito-bakery/ORGANIZACION-PRODUCTOS.md` | Catálogo: 1 principal + 5 bonos + 3 upsells, con precios y links de pago |
| `creativos-lomito-bakery/ANALISIS-PRECIOS.md` | Precios de competencia |
| `creativos-lomito-bakery/METODO-BUSQUEDA-OFERTAS.md` | El método de caza de ofertas nuevas |
| `creativos-lomito-bakery/PLAN-ESPANA.md` | Plan de España — **postergado**, armado y en espera |
| `creativos-lomito-bakery/ebook/` | El producto: PDFs, entregables, scripts que los generan |
| `creativos-lomito-bakery/landing-lomito-bakery.html` | Landing de México (viva) |
| `creativos-lomito-bakery/landing-lomito-ES.html` | Landing de España (en espera) |
| `resumen-negocio/` | Informe general del negocio + `datos.md` |

---

## Estado al 2026-10-20

**Oferta activa:** Lomito Bakery — ebook de pastelería canina, mercado México.

- Cuenta Meta: `1560224662043860` (Ebooks Argentina). La cuenta ARS
  `238377004117040` es otro negocio de 2020, gasto 0: **excluida siempre**.
- Campaña: `Test ABO | Pastelería Canina | MX 10/10` (`52532697130726`).
- Tienda: Impultienda. Pasarela Impul Pay. **OXXO SÍ está disponible** (lo
  agregaron hace poco; Nacho lo verificó el 24/10 entrando al checkout como
  comprador mexicano). El dato viejo "solo tarjeta" quedó obsoleto.

**El cierre de 4 días (16-19/10) dio positivo: +$7.03.** Primera vez en toda la
campaña. Pérdida acumulada de octubre: ≈ $72.12 (venía de $86.46).

**Ganador identificado:** anuncio `15 B | negación + 30 recetas` (`52533183939926`).
CPA $12.33, CTR 3.86%. **Todas** las ventas de los 4 días son de este anuncio.
Break-even: $12.20 sin upsell, $16.94 con bump.

**Decisión vigente:** México se queda, España se posterga. No se abandona un
activo que acaba de dar positivo para irse a un mercado sin validar.

**Conjunto CJ1:** $17/día (subido desde $14 el 20/10, +21%, debajo del 25% que
resetea el aprendizaje).

### La fuga más grande (sin resolver)
**76% de abandono en el checkout** — 17 checkouts iniciados → 4 compras, con la
gente ya en el botón de pagar. El CTR es bueno y el tráfico llega: el problema
no está en la pauta. **Ya no se explica con OXXO**: OXXO está habilitado.

Antes de volver a llamar a esto "fuga", hay que verificar qué mide el evento:
nuestra landing solo dispara `PageView`, así que `InitiateCheckout` lo tira
Impultienda, y lo más probable es que salte **al cargar la página de pago**,
no al apretar pagar. Si es así, "124 checkouts → 17 ventas" es en realidad
"124 llegaron a la página de pago → 17 compraron" = 14%, que para tráfico
frío de Meta a $12.90 es flojo pero no una catástrofe. **Sin verificar esto,
el número no se usa para decidir.**

### Otros pendientes
- `CJ7 | V1 Problema – copy ingreso extra | MX`: ACTIVO con $8/día, gastó $0.
  Entrega congelada.
- España: si se retoma, **recalcular el break-even con IVA 21% incluido en el
  precio** (de 19,90 € quedan 16,45 €; se pierde 17,4% de cada precio). El CPA
  de break-even de ~$21 que se proyectó NO tiene esto contemplado.

---

## Presupuesto (manda sobre todo)

- **$300 USD de pérdida tolerada por mes. $600 en total para nov + dic.**
- Es **tope de pérdida, no de gasto.** Si una oferta factura $900 gastando
  $1.000, perdiste $100, no $1.000.
- **Un activo en break-even es gratis.** Lomito, mientras no pierda plata, no
  consume nada de los $600.
- **$100 fijo por test de oferta nueva.** No $150 porque al tercer día pintaba bien.
- **Se mata a los $100 con 0-1 ventas.** Sin "un día más".
- Noviembre testea ($240 test / $60 reserva). Diciembre escala ($100 / $200).
  **La reserva no se toca para testear.**
- El cuello de botella no es la plata, es la velocidad de construcción: ~1 oferta
  cada 10 días. Poner más plata no mete más ofertas.

---

## Cómo juzgar un creativo

No mires CTR, acá engaña: hubo anuncios con CTR 5% y cero ventas. **Mirá CPA.**

- CPA < $8 → escalar
- CPA $8-12 → dejar correr
- CPA > $15, o 0 ventas con $10 gastados → apagar

Dejá correr 3-4 días o ~$10 USD por creativo antes de juzgar. No mates un
anuncio con menos de ~150 impresiones: la muestra es demasiado chica.

El ángulo que gana es **negocio con número concreto** (costo vs precio de venta,
ingreso extra). El ángulo "recetas lindas" probó dar $0 con $21 gastados.

---

## Cómo trabajar acá

1. **Leé antes de opinar.** Como mínimo `REGISTRO-CAMBIOS.md` (el final) y
   `datos.md`. Si el tema toca presupuesto, también `PLAN-NOV-DIC.md`.
2. **Escribí lo que se decide.** Toda sesión que produzca un dato, un cierre o
   una decisión termina agregando una entrada fechada al final de
   `REGISTRO-CAMBIOS.md`.
3. **Commiteá siempre.** El container se borra al cerrar la sesión: lo que no
   está commiteado se perdió. Mensajes en español, descriptivos, contando qué
   pasó y no qué archivo se tocó (mirá el historial como ejemplo).
4. **No des vuelta un plan por el dato de un día.** Pasó con España: se decidió
   migrar un sábado leyendo "30 LPV / 0 ventas" y dos días después había 2
   ventas. Las decisiones se toman sobre cierres de 3-4 días limpios.
5. **Separá lo verificado de lo proyectado.** Decir "esto lo confirmé en la API"
   y "esto es una estimación mía" no es lo mismo, y acá importa la diferencia.
6. Escribí en español rioplatense (voseo), como el resto del repo. El material
   dirigido al comprador mexicano va en neutro/mexicano.
