# Cómo queda organizado todo · Repostería que Vende

1 producto principal · 5 bonos · 3 upsells. Misma arquitectura que Lomito.

---

## La regla que manda sobre todo

**Un bono no puede pisar a un upsell.** En Lomito los upsells no se vendían
porque los bonos ya regalaban lo mismo. Acá la línea está trazada desde el
principio:

| | Producción | Venta |
|---|---|---|
| **Curso y bonos (gratis)** | las 30 recetas, costos, insumos, rescates, conservación | **persona a persona**: tus contactos, tu colonia, la oficina de alguien |
| **Upsells (pago)** | pastelería de evento, que no está en el curso | **en redes** y **por fecha del calendario** |

Si al revisar un bono ves que repite algo de un upsell, el bono se recorta.
Nunca al revés.

---

## 1 · PRODUCTO PRINCIPAL — $229 MXN

Mismo precio que Lomito a propósito: el break-even queda igual y los dos
tests se comparan sin una variable de más.

| Archivo | Qué es | Estado |
|---|---|---|
| `00-LEEME-PRIMERO.pdf` | Bienvenida y qué abrir primero · 2 págs | **listo** |
| `01-Reposteria-que-Vende.pdf` | **El curso** · 102 págs, 30 recetas | **listo** |
| `02-Bono-Calculadora-de-precios.xlsx` | Bono 1 | **listo** |
| `03-Bono-Sustituciones-y-rescates.pdf` | Bono 2 · 5 págs | **listo** |
| `04-Bono-Etiquetas-y-empaque.pdf` | Bono 3 · 5 págs | **listo** |
| `05-Bono-Conservacion-y-traslado.pdf` | Bono 4 · 3 págs | **listo** |
| `06-Bono-Donde-comprar-mas-barato.pdf` | Bono 5 · 4 págs | **listo** |

### Por qué estos cinco

Ninguno es relleno. Cada uno resuelve algo que frena a quien recién arranca:

1. **Calculadora** — el ebook trae los costos sugeridos; la calculadora deja
   meter los precios reales de *su* súper y recalcula precio y margen solos.
   Es el bono con más valor percibido y el más barato de producir.
2. **Sustituciones y rescates** — el bono que **baja reembolsos**. Casi toda
   devolución en cursos de recetas viene de una primera tanda arruinada.
3. **Etiquetas y empaque** — para que el producto se vea de tienda y no
   casero. Es lo que sostiene el precio que el curso enseña a cobrar.
4. **Conservación y traslado** — cuánto aguanta cada postre y cómo llevarlo
   sin que llegue destruido. Problema real del primer pedido grande.
5. **Dónde comprar más barato** — central de abastos contra súper, qué
   conviene por mayoreo. Sube el margen de las 30 recetas de una.

---

## 2 · LOS 3 UPSELLS

No van en la carpeta del principal. Cada uno con su carpeta y su link.
**No se nombran en la landing**: se ofrecen en el order bump del checkout y
en el mail post-compra.

| # | Producto | Precio | Páginas | Qué trae |
|---|---|---|---|---|
| 1 | Pastelería de Fiesta | $119 MXN | 10 | Cinco pasteles de evento que **no están** en el curso (dos pisos, de número, naked cake, smash cake, temático con fondant), cómo cotizar un evento y cómo cobrar la mesa de postres como paquete |
| 2 | Vende en Redes | $139 MXN | 7 | Cómo fotografiar con luz de ventana, 15 publicaciones escritas, la semana en historias y qué contestar cuando preguntan el precio |
| 3 | Fechas que Venden | $139 MXN | 6 | El calendario mexicano mes por mes, las 5 fechas grandes con qué producir y cuándo abrir pedidos, y cómo armar una preventa |

Los tres están **hechos**: 23 páginas en total, todas en 1696×2528.

### Las dos verificaciones que no se pueden saltear

**El Pack de Fiesta no pisa al curso — verificado el 23/10.** Los 7 pasteles
del curso (tres leches, pay de queso, pay de limón, elote, zanahoria, tarta
de fresas e imposible) son todos caseros. Ninguno de los cinco del Pack
aparece ahí.

**Pero hay un roce con la categoría 5**, que se llama "Mesa de postres e
individuales" y ya trae cakepops, fresas con chocolate y mini cheesecakes.
Por eso el Pack **no vende esas recetas**: vende el pastel de evento y el
armado y cotización de la mesa como paquete. La página 10 del Pack lo dice
con todas las letras — "las piezas salen de las recetas que ya tienes en el
curso" — para que nadie sienta que le cobraron dos veces lo mismo.

**El Kit de Redes roza al curso — resuelto.** La página 101 del ebook enseña
a conseguir los primeros diez clientes y una de las cinco vías es el teléfono
propio. La página 2 del Kit declara la línea: el curso te enseña a venderle a
quien ya te conoce, el Kit a que te encuentre quien no. Ninguna de las 15
publicaciones del Kit repite "mandá foto y precio a tus veinte contactos".

---

## 3 · LA LANDING

`landing-reposteria-que-vende.html`, **lista para pegar**.

El ancla no es inventada: es la suma de los 6 precios tachados.

| Archivo | Precio tachado |
|---|---|
| Curso, 102 págs | $499 |
| Bono 1 · Calculadora | $209 |
| Bono 2 · Sustituciones y rescates | $149 |
| Bono 3 · Etiquetas y empaque | $129 |
| Bono 4 · Conservación y traslado | $99 |
| Bono 5 · Dónde comprar más barato | $119 |
| **Suma** | **$1.204** |

$229 sobre $1.204 da **81% de descuento**. Los dos números cierran.

**Checkout real y verificado el 23/10:**
`https://reposteria-que-vende.impultienda.ar/checkout` — ya está puesto en
la landing.

⚠️ **Cuidado con el subdominio sin guiones.** `reposteriaquevende` (todo
junto) también existe, devuelve 200 y carga **la tienda de Lomito**. No da
404: carga bien y muestra el producto equivocado, así que el error no se
nota hasta el cierre. El bueno lleva guiones.

Los 3 upsells **no se nombran** en la landing: van en el order bump del
checkout y en el mail post-compra.

---

## Orden para hacerlo

1. Nacho: crear la tienda en Impultienda con el nombre *Repostería que Vende*
2. Compartir el pixel `1712126017302327` (el mismo de Lomito, Impultienda
   deja usarlo en varias tiendas)
3. Pegar la landing y subir los archivos
4. Crear los 3 productos de upsell con su link
5. **Compra de prueba real de punta a punta**, mirando que la pantalla final
   muestre los 7 archivos
