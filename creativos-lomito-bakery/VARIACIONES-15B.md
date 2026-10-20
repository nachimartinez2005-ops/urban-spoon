# Variaciones de copy del anuncio ganador (15 B)

Escritas el 2026-10-20. Para lanzar el miércoles 21, después de evaluar el
salto de presupuesto de $14 a $17/día.

---

## El original

**Anuncio:** `15 B | negacion + 30 recetas` · ad id `52533183939926`
**Creative id:** `1803041127501843`
**Video id:** `2497533197399959`
**Conjunto:** CJ1 | V1 Problema | MX 25-60 (`52532697234526`)
**CTA:** BUY_NOW

Rendimiento acumulado 16-19/10: $49.33 gastados / $66.61 facturados /
4 ventas / **CPA $12.33** / CTR 3.86% / 92 LPV / 14 checkouts.
Break-even: $12.20 sin upsell, $16.94 con bump. **Rentable solo.**
Las 4 ventas de esos días salieron todas de este anuncio.

### Copy original
```
Chocolate, uvas, cebolla, xilitol y aguacate. ⚠️

Ninguna de las 30 recetas de Pastelería Canina que Vende lleva estos
ingredientes, porque son tóxicos para los perros.

Lo que sí llevan: avena, plátano, calabaza, camote, zanahoria y pollo.

Y además de hornearlas, aprendes a venderlas 👇

Una bolsita de galletas te cuesta unos $21 de ingredientes y empaque. Se
vende en $70. Y casi nadie en tu colonia las hace.

💰 Cada receta trae su costo y su precio de venta
📦 Cómo empacar
📲 Cómo conseguir tus primeros pedidos

📘 Curso digital de $12.90 USD · 30 recetas + 5 bonos
🛡️ Garantía de 7 días
👉 Pícale a «Comprar».

*Precios sugeridos. Tus ganancias dependen de tus costos y tus ventas.
```
**Titular:** `Ninguna de las 30 lleva estos 5 · $12.90`
**Descripción:** `30 recetas seguras + calculadora de precios`

---

## Por qué gana (hipótesis a validar con estas variaciones)

1. **No abre vendiendo. Abre con peligro para el perro.** La primera línea
   activa el instinto protector, no el interés comercial.
2. **No pide nada en los primeros 3 segundos.** No hay oferta hasta el
   cuarto párrafo.
3. **La negación es contable y específica:** "ninguna de las 30 lleva
   estos 5". Un número verificable, no un adjetivo.
4. **El dinero llega después de la confianza**, no antes.
5. **El precio está a la vista y es bajo.** Nada de "descúbrelo adentro".

**Lo que se conserva en las 4 variaciones: la negación específica al
principio y el dinero en segundo lugar. Lo que cambia es QUÉ se niega.**

---

## Nota técnica

Los ad creatives de Meta son **inmutables**: no se puede editar el copy de
un anuncio existente. Cada variación es un creative nuevo apuntando al
**mismo `video_id` 2497533197399959**, con body/title/description distintos.

Ventajas: aísla la variable (si una gana, fue el texto) y **no gasta un solo
crédito de Higgsfield**.

Pasos: `ads_create_creative` con el video_id → `ads_create_ad` en CJ1 →
`ads_activate_entity`.

---

## A · Negación del producto que ya compra
*La más cercana al ganador: misma palanca de seguridad, otro objetivo.
Ataca el premio de supermercado en vez del ingrediente tóxico.*

```
Dale vuelta a la bolsa de premios que le compras a tu perro y lee. ⚠️

Harina refinada, glicerina, colorante y conservadores. Eso es lo que trae.

Ninguna de las 30 recetas de Pastelería Canina que Vende lleva nada de eso.
Llevan avena, plátano, calabaza, camote, zanahoria y pollo.

Y además de hornearlas, aprendes a venderlas 👇

Una bolsita te cuesta unos $21 de ingredientes y empaque. Se vende en $70.
Y casi nadie en tu colonia las hace.

💰 Cada receta trae su costo y su precio de venta
📦 Cómo empacar
📲 Cómo conseguir tus primeros pedidos

📘 Curso digital de $12.90 USD · 30 recetas + 5 bonos
🛡️ Garantía de 7 días
👉 Pícale a «Comprar».

*Precios sugeridos. Tus ganancias dependen de tus costos y tus ventas.
```
**Titular:** `Leé la bolsa que le das · $12.90`
**Descripción:** `30 recetas sin conservadores + calculadora`
**Nombre sugerido:** `19 A | negacion bolsa supermercado`

---

## B · Negación de la capacidad
*Quita la objeción "yo no sé cocinar", que es la que más gente frena.*

```
No necesitas saber cocinar. ⚠️

Las 30 recetas de Pastelería Canina que Vende se hacen con un bowl, una
cuchara y el horno que ya tienes. Ninguna lleva más de 6 ingredientes y
todos están en el súper.

La más difícil tarda 25 minutos.

Y además de hornearlas, aprendes a venderlas 👇

Una bolsita te cuesta unos $21 de ingredientes y empaque. Se vende en $70.
Y casi nadie en tu colonia las hace.

💰 Cada receta trae su costo y su precio de venta
📦 Cómo empacar
📲 Cómo conseguir tus primeros pedidos

📘 Curso digital de $12.90 USD · 30 recetas + 5 bonos
🛡️ Garantía de 7 días
👉 Pícale a «Comprar».

*Precios sugeridos. Tus ganancias dependen de tus costos y tus ventas.
```
**Titular:** `Un bowl, una cuchara, 25 minutos · $12.90`
**Descripción:** `30 recetas fáciles + calculadora de precios`
**Nombre sugerido:** `20 B | negacion no se cocinar`

---

## C · Negación de la inversión — RESERVA
*Quita la objeción "para vender necesito montar un negocio".*

```
No necesitas horno industrial. ⚠️

Ni permiso de salubridad, ni local, ni invertir miles para empezar a vender
pastelería para perros.

Necesitas el horno de tu casa y $21 de ingredientes. Esa es toda la
inversión de la primera bolsita, y se vende en $70.

Las 30 recetas de Pastelería Canina que Vende están pensadas para hacerse
en una cocina normal 👇

💰 Cada receta trae su costo y su precio de venta
📦 Cómo empacar
📲 Cómo conseguir tus primeros pedidos

📘 Curso digital de $12.90 USD · 30 recetas + 5 bonos
🛡️ Garantía de 7 días
👉 Pícale a «Comprar».

*Precios sugeridos. Tus ganancias dependen de tus costos y tus ventas.
```
**Titular:** `Sin local, sin permisos, sin miles · $12.90`
**Descripción:** `Empieza con el horno que ya tienes`
**Nombre sugerido:** `21 C | negacion inversion`

---

## D · Negación del tiempo — RESERVA
*La más lejana al ganador. La última en entrar.*

```
No te quita las tardes. ⚠️

Una tanda de galletas para perro son 25 minutos, y salen entre 15 y 20
bolsitas. Las haces un domingo y las vendes toda la semana.

Las 30 recetas de Pastelería Canina que Vende vienen con los tiempos
reales, no con los optimistas 👇

Una bolsita te cuesta unos $21 de ingredientes y empaque. Se vende en $70.
Y casi nadie en tu colonia las hace.

💰 Cada receta trae su costo y su precio de venta
📦 Cómo empacar
📲 Cómo conseguir tus primeros pedidos

📘 Curso digital de $12.90 USD · 30 recetas + 5 bonos
🛡️ Garantía de 7 días
👉 Pícale a «Comprar».

*Precios sugeridos. Tus ganancias dependen de tus costos y tus ventas.
```
**Titular:** `25 minutos, 20 bolsitas, un domingo · $12.90`
**Descripción:** `30 recetas con tiempos reales`
**Nombre sugerido:** `22 D | negacion tiempo`

---

## Plan de lanzamiento

**Lanzar A y B el miércoles 21. C y D quedan en reserva.**

Dos razones para no lanzar las cuatro:

1. **A $17/día, cuatro anuncios nuevos en aprendizaje al mismo tiempo le
   roban entrega a 15 B** justo cuando está rindiendo. Es el error de
   fragmentar el presupuesto, otra vez.
2. **A es la hermana del ganador y B ataca la objeción más común.** Son las
   dos apuestas con mejor relación entre probabilidad y aprendizaje.

C y D entran cuando el presupuesto aguante más anuncios — orientativamente
a partir de $30/día.

### Criterio de corte
Mismo que para cualquier creativo: **~500 impresiones sin venta y se pausa.**
No se evalúa por CTR solo; 15 B tiene 3.86% y las que no venden andaban en
1.4-1.7%, pero esa diferencia hay que verla con muestra, no con 120
impresiones.

### Qué NO hacer
- No tocar 15 B. Es el control del experimento.
- No lanzar A y B el mismo día que se cambia el presupuesto: no se podría
  atribuir el resultado a ninguno de los dos.
- No hacer variaciones de VIDEO todavía. El video es el activo probado;
  cambiarlo es cambiar la variable cara. Primero agotar el copy, que es
  gratis.
