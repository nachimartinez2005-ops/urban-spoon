# Plan España — Lomito Bakery

Preparado la madrugada del 18/10 para la reunión del lunes.

## Por qué España y no otro mercado

Sale del método de la mentora, no de una corazonada:

- Orden de prioridad de destino: 1) inglés, 2) **Europa**, 3) LATAM, 4) Brasil.
  México es prioridad 3. España es prioridad 2.
- Barrido de la Ads Library con `countries: ["ES"]`: **12 anuncios en total**
  entre "repostería canina" y "galletas caseras para perros". **Cero players
  españoles.** Los que hay son páginas brasileñas (BRL) y colombianas (COP)
  alcanzando España con copy traducido.
- Algunos de esos llevan **40 y 90 días corriendo**. Señal Nivel 3 de
  longevidad: nadie banca 3 meses a pérdida.

Traducido: la oferta funciona ahí, la explotan desde afuera, y no hay nadie local.

## Precios — repreciados para España, NO convertidos

Convertir 229 MXN a euros daría ~11 €, que es regalar el producto en un mercado
con cuatro veces el poder adquisitivo. Estos precios están puestos para España:

| Concepto | México | España |
|---|---|---|
| **Producto principal** | 229 MXN ($12.37) | **19,90 €** (~$21.5) |
| Ancla (stack completo) | 1.084 MXN | 95 € |
| Descuento mostrado | 79% | 79% |

Desglose del stack: curso 44 € · calculadora 19 € · guía de ingredientes 9 € ·
plan de negocio 8 € · plantillas 6 € · porciones y soluciones 9 € = **95 €**

Precios de venta sugeridos que muestra la landing (mercado español):

| Producto | México | España |
|---|---|---|
| Bolsita de galletas x10 | 70 MXN | 7 € |
| Caja de pupcakes x4 | 120 MXN | 14 € |
| Pastel de cumpleaños | 350-380 MXN | 32-38 € |
| Snacks | 90 MXN | 8 € |
| Para gatos | 80 MXN | 8 € |
| Costo de ingredientes (ejemplo) | ~25 MXN | ~2,50 € |

**El ticket casi se duplica: de $12.37 a ~$21.5.** Con el mismo PDF, la misma
landing y los mismos creativos. Eso cambia qué CPA te podés permitir.

Upsells sugeridos: Pack Cumpleaños 7,90 € · Kit Vende en Redes 9,90 € ·
Pack Fechas que Venden 9,90 €.

## Localismos corregidos

- `camote` → **boniato**
- `refrigerador` → **nevera** (y el artículo, que se me rompió y lo arreglé)
- `precio de lanzamiento en pesos` → `precio de lanzamiento`
- Revisado: no queda voseo ni mexicanismos en el texto visible.
- `plátano` se deja: es correcto en España.

## Archivo listo

`landing-lomito-ES.html` — renderizado y revisado visualmente.

Los 4 enlaces de compra apuntan a `https://lomitobakery.impultienda.ar/`.
Nacho confirmó que Impultienda usa **el mismo link para todos los markets** y
detecta el país del visitante, así que no hace falta una URL distinta para
España. Ya no quedan placeholders: la landing está lista para subir.

## Precios a cargar en el market de España

Misma lógica de descuento que el market de México, para que no haya
incoherencias entre lo que dice la landing y lo que muestra el checkout.

| Producto | Tachado | Precio de venta |
|---|---|---|
| Pastelería Canina que Vende (principal) | 44,90 € | **19,90 €** |
| Pack Pasteles de Cumpleaños (upsell 1) | 14,90 € | **7,90 €** |
| Kit Vende en Redes (upsell 2) | 18,90 € | **9,90 €** |
| Pack Fechas que Venden (upsell 3) | 18,90 € | **9,90 €** |

El descuento post-compra del 20% se mantiene: el upsell de cumpleaños queda
en 6,32 € efectivos.

Salto de ticket respecto de México:

| | México | España |
|---|---|---|
| Principal | 229 MXN = $12.37 | 19,90 € = ~$21.50 |
| Con upsell de cumpleaños | 300 MXN = $16.22 | 26,22 € = ~$28.30 |

El punto de equilibrio sube de $12.20 a unos **$21**.

⚠️ **No usar la conversión automática de Impultienda.** Convertiría 229 MXN a
~11 € y se cae el motivo entero de ir a España. Los números se cargan a mano.

## Lo que falta y es de Nacho

1. **Cargar el market de España** con los precios de la tabla de arriba, a mano.
2. **Preguntar por el IVA digital de la UE** — vender infoproductos a
   consumidores europeos tiene obligaciones fiscales. Probablemente lo manejen
   ellos o esté bajo el umbral, pero hay que saberlo antes de facturar.

## Lo que falta y es mío

1. **Rehacer el texto quemado de los 2 videos**: hoy dicen "Te cuesta $25. La
   vendes a $70". En euros son 2,50 € y 7 €. Se rehace en el sandbox de
   Higgsfield con los archivos fuente.
2. **Adaptar el copy de los anuncios** al mercado español.
3. **Crear la campaña** apuntando a ES, con las ubicaciones abiertas desde el
   día cero y el píxel verificado antes de gastar un peso.

## Lo que NO voy a repetir de México

El cierre del método de la mentora: *"el whale valida la OFERTA, no te salva de
un test sucio"*. En México el test estuvo sucio. En España arranca así:

- Píxel instalado y verificado ANTES del primer peso
- Embudo de upsells probado con una compra real ANTES de abrir
- Un solo conjunto de anuncios, ubicaciones abiertas
- Presupuesto concentrado, no repartido
- Producto entregado alineado con lo que promete el anuncio
