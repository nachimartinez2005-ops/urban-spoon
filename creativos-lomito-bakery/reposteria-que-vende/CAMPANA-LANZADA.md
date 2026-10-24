# Campaña de lanzamiento · Repostería que Vende

Lanzada el 2026-10-23 a las 18:00 BA. **Está corriendo.**

## Los IDs

| | ID |
|---|---|
| Campaña · `Test ABO \| Repostería que Vende \| MX 23/10` | `52535600821126` |
| Conjunto · `CJ1 \| R1 negacion recetario \| MX 25+` | `52535600841126` |
| Anuncio · `R1 v2 \| negacion recetario \| con IG` | `52535619088726` |
| ~~Anuncio v1, pausado~~ | ~~`52535601279726`~~ |
| Creative | `29471724449079022` |
| Video | `1932490898160979` |
| Portada | hash `d6986f1ef70fce9de993fbaab9699506` |

## Cómo quedó configurada

| | |
|---|---|
| Objetivo | OUTCOME_SALES |
| Optimización | OFFSITE_CONVERSIONS por **PURCHASE** |
| Pixel | `1712126017302327` (el mismo de Lomito) |
| Presupuesto | **$20/día**, ABO · 5 días son los $100 del test |
| Público | México, 25+, Advantage+ Audience con sugerencia hasta 60 |
| Ubicaciones | Advantage+ (automáticas) |
| Destino | `https://reposteriaquevende.impultienda.ar` |
| CTA | COMPRAR |
| Página de Facebook | **Dulce comienzo** |
| Instagram | **@reposteriarentablemx** (`17841425937424204`) |

### Las identidades: resuelta la de Instagram, pendiente la de Facebook

La v1 del anuncio salió sin cuenta de Instagram vinculada, así que en
Instagram se mostraba con la identidad de la página de Facebook. Se rehizo
el 23/10 a las 21:00 con **@reposteriarentablemx** vinculada. La v1 quedó
pausada con $1.91 gastados y 162 impresiones, que es despreciable.

**Queda pendiente la página de Facebook.** Sigue siendo *Dulce comienzo*,
que es del negocio anterior de sueño infantil y tiene contenido de bebés. En
Instagram ya no importa, pero quien vea el anuncio en Facebook y entre al
perfil se encuentra con eso. El nombre "Repostería que Vende" no estaba
disponible para una página nueva; el de Instagram quedó como Repostería
Rentable MX.

### Por qué ABO y no CBO
Para que el cierre diario siga funcionando igual que con Lomito: el
protocolo lee `daily_budget` del conjunto. Con una sola oferta y un solo
anuncio, CBO no aporta nada.

## Break-even: $12.20 USD

Mientras no se confirme la retención real de Impultienda (ver
`BREAK-EVEN.md`), se usa el conservador de Lomito.

| CPA | Qué se hace |
|---|---|
| menos de $8 | escalar |
| $8 a $12.20 | rentable, dejar correr |
| $12.20 a $15 | pierde poco, solo aguanta si suben los upsells |
| más de $15 | apagar |

## Los frenos, que no se negocian

- **$100 fijos.** A los $100 con 0-1 ventas se mata. Sin "un día más".
- **R2 y R3 no se lanzan todavía.** Entran cuando R1 tenga ~500 impresiones,
  gane o pierda. Varios anuncios nuevos a la vez se roban la entrega y
  ninguno junta muestra.
- **No se juzga por CTR.** En Lomito hubo anuncios con CTR 5% y cero ventas.
- **No se mata nada con menos de ~150 impresiones.**

## Lo que quedó sin verificar

**No hubo compra de prueba.** Nacho probó los links desde el celular y
funcionan, así que la landing, el checkout y la descarga de los PDFs están
vistos. Lo que nadie probó es el tramo de después del pago: que la entrega
salga sola, que el mail llegue a bandeja principal y que el link de la
carpeta sea el correcto.

Si eso falla, el síntoma es alguien que pagó y no recibió nada. **En la
primera venta hay que escribirle al comprador y confirmar que recibió los 7
archivos.**

## Pendientes

1. Confirmar la retención real de Impultienda y recalcular el break-even.
2. El checkout está **en inglés** ("Personal info", "First name"). Para un
   comprador mexicano eso baja la confianza justo en el paso del pago, y en
   Lomito ya cargamos 76% de abandono sin explicar.
3. Arriba de la landing aparece **"lomitobakery"**, que es el nombre de la
   cuenta. Quien llega de un anuncio de repostería lee eso primero.
