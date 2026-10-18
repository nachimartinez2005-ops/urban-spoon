# Método de búsqueda de ofertas — acordado 16/10/2026

Nacho quiere copiar el método de @felipe.culacciati. Decisión final: sábado 17/10.

## Qué estamos copiando y qué no

| | Felipe | Nosotros hasta ahora |
|---|---|---|
| Qué testea | **ofertas** (producto + precio + promesa + landing) | **creativos** sobre una sola oferta |
| Ritmo | 3-4 por día | 1 oferta, ~12 creativos, en 14 días |

El gap no es de presupuesto, es de nivel de experimento. Cambiar el creativo
mueve el CTR; cambiar la oferta mueve la tasa de conversión, que es un
multiplicador mucho mayor.

NO copiamos su contenido orgánico de TikTok: Nacho tiene acento argentino y
vende a México. Queda descartado por ahora (decisión suya).

## Dato de Nacho, no verificado por mí

Dice que en el perfil de Felipe hay días de 80-100 ventas. No pude entrar a
TikTok (bloqueado por el proxy), así que lo tomo de su observación. En el
video que me pasó, Felipe reporta 7 ventas y "quedó profit, pero muy poquito":
los días flojos son el costo de los días buenos. Consistente con el método.

Corrección a mí mismo: dije "ese tipo está casi donde estás vos" basándome
solo en ese video. Con el dato del perfil, esa conclusión estaba mal.

## Las 3 reglas, fijadas ANTES de que haya plata en juego

1. **El dinero de búsqueda es dinero que puede perderse entero.** No es
   "inversión que vuelve". El número es el que no cambia el mes si desaparece.
2. **Regla de muerte: $25 gastados y 0 ventas → se mata la oferta.** Sin
   excepciones, sin "un día más". Ese "un día más" costó $79 en 7 v prob. y 14 A.
3. **Las cajas no se mezclan.** Lomito y búsqueda tienen presupuestos
   independientes. Ninguno alimenta al otro.

Acordado: las hago cumplir aunque Nacho pida lo contrario en caliente.

## Expectativa que hay que sostener

**Más presupuesto compra más intentos, NO mejor puntería.** La tasa de acierto
no sube con el dinero; sube la cantidad de tiros por semana. Si se entra
esperando que la plata traiga el ganador, la tercera oferta muerta frustra.

## Economía del test

Base: CPM ~$11.39, CPA de equilibrio $12.20. Un test necesita gastar hasta
tener una venta o poder declararlo muerto → ~$25 por oferta.

| Tests/día | Presupuesto |
|---|---|
| 3 (lo de Felipe) | $75/día |
| 2 | $50/día |
| 1 | $25/día |
| 1 cada 2 días | $14/día (lo actual de Lomito) |

Orden que importa: Felipe financia sus tests con sus ganadores. Nacho todavía
no tiene uno. Primero sale un ganador, después el volumen.

## Ventaja nuestra: velocidad de producción

El cuello de botella de Felipe es el dinero. El de Nacho era el tiempo —
Lomito llevó 2 semanas de armado. Eso ya no es cierto: con el pipeline
montado el 16/10 (sandbox de Higgsfield + subida por URL a Meta) una oferta
completa (ebook, bonos, landing, creativos, anuncios) se produce en un día.

## Pendiente para el sábado

- Lista de 10 ofertas candidatas vía skill `cazar` sobre la biblioteca de
  anuncios de Meta, ordenadas por velocidad de producción
- Escenarios de $50, $100 y $200 por semana
- Calendario concreto de producción

## Selección de mercado (planteado por Nacho, 16/10 noche)

Nacho observa que hay países que gastan más en producto digital y quiere que
se tenga en cuenta al buscar ofertas. Correcto, pero con dos matices:

**1. No es poder adquisitivo, es ticket ÷ CPM.** Un mercado con el doble de
ingreso suele tener también más CPM, porque hay más anunciantes compitiendo.
Si el ticket sube 2x y el CPM 2.5x, el mercado es peor. La referencia a
superar es la de México hoy: CPM $11.39 con ticket de $12.37.

**2. Límite duro antes de cualquier análisis: el cobro.** Impultienda es
argentina y hoy cobra en MXN. PENDIENTE DE NACHO: preguntarle a Impultienda a
qué países puede cobrar y en qué monedas. Si no puede cobrar ahí, el poder
adquisitivo del mercado es irrelevante.

**Pendiente mío para el sábado:** usar `ads_insights_industry_benchmark` para
traer CPM y CTR reales por mercado y armar la tabla de ticket ÷ CPM ordenada
por dato, no por intuición. Nada de estimar poder adquisitivo de memoria.

NO cambiar el mercado de Lomito ahora: el corte del sábado se decide con los
datos de México.

### Actualización 16/10 noche — el cobro NO es la restricción

Nacho confirma que Impultienda cobra a muchísimos países: Europa, África,
América. El límite duro que yo había planteado no existe.

**La restricción pasa a ser el idioma.** El ebook está en español, así que el
universo real para Lomito es:
- Europa: España (el de mayor poder adquisitivo del idioma)
- América: México, Colombia, Chile, Perú, Argentina, Uruguay, Costa Rica,
  Panamá, Ecuador, y el hispano de EE.UU. (mayor ingreso y mayor CPM)
- África: descartado. Solo Guinea Ecuatorial habla español y es minúscula.

Poder cobrar en 100 países sí es ventaja real para las OFERTAS FUTURAS, donde
se puede elegir idioma desde el día cero. Para Lomito son ~10 mercados.

### Oportunidad más barata detectada: mismo producto, mercado más rico

| | México | España |
|---|---|---|
| Precio actual | 229 MXN = $12.37 | — |
| Equivalente razonable | — | €19–24 = $21–26 |

Mismo PDF, misma landing, mismos creativos (adaptando "colonia" → "barrio" y
los precios de ejemplo). El ticket casi se duplica con costo de producción
cero. No es una oferta nueva: es la actual en otro mercado. Se testea con $25.

Riesgo: el CPM de España es bastante mayor que el de México. NO afirmarlo
hasta tener los benchmarks reales de Meta. Si el ratio ticket ÷ CPM no supera
al de México, no sirve.

### Pendiente de Nacho (junto con lo anterior)

Preguntarle a Impultienda por el **IVA digital de la UE**. Vender
infoproductos a consumidores europeos tiene obligaciones fiscales.
Probablemente lo manejen ellos o esté debajo del umbral, pero hay que
confirmarlo antes de facturar en Europa, no después.

## Presupuesto real — corregido 17/10 noche

Yo venía manejando los $250 como TOPE DE GASTO. Nacho aclaró que son
**TOPE DE PÉRDIDA, Y POR MES**. No es lo mismo: lo facturado descuenta.

| | |
|---|---|
| Gastado en Lomito | $219.09 |
| Facturado | $133.69 |
| **Perdido en octubre** | **$85.40** |
| Disponible hasta el 31 | **$164.60** |
| Días restantes de octubre | 14 |
| **Pérdida permitida por día** | **$11.76** |

Ritmo actual desde que el presupuesto bajó a $14/día: **−$4.51 por día**
(viernes +$5.28, sábado −$14.30). Va holgado.

Runway real: entre 12 días (peor caso, cero ventas, −$14/día) y 36 días
(ritmo actual). NO los 2 días que yo había calculado con el marco equivocado.

Nacho cuenta los $128.44 de Noches en Calma como mes anterior. Observación
hecha una vez y no se insiste: ese gasto ocurrió del 2 al 6 de octubre, o sea
que es caja de este mes. Es su contabilidad y su decisión.

### Reparto de los $164.60

| Destino | Asignado |
|---|---|
| Lomito México | $70 |
| Test de España | $50 |
| Reserva | $44.60 |

Entran los dos frentes sin pedir plata nueva.

### Regla de freno

Si la pérdida acumulada del mes llega a **$200**, se para todo y los $50
finales se reservan para noviembre. No se espera a tocar los $250 exactos:
el último tramo es el que deja sin capacidad de reacción.

## Cierre del sábado 17/10

| | Viernes | Sábado |
|---|---|---|
| Invertido | $10.94 | $14.30 |
| LPV | 8 | 30 |
| CTR | 2.78% | 5.38% |
| Ventas | 1 | 0 |

15 B viernes+sábado: $15.59 gastados, 1 venta → **CPA $15.59 → rama amarilla**.

La entrega quedó arreglada: el sábado CJ1 gastó $14.30 de $14 contra $4.27 el
viernes. Fue el primer día de toda la campaña con entrega funcionando.

Decisión: **no tocar nada el domingo.** Un solo día de entrega sana no alcanza
para juzgar, y cada cambio reinicia el aprendizaje. El lunes se lee sábado +
domingo, los dos primeros días limpios.

Tampoco se recorta el video in-stream de Facebook (CPM $37.77, clics
probablemente accidentales, $1.17/día): el costo de reiniciar el aprendizaje
supera el ahorro.

### Corrección a un número que di mal

El viernes le dije a Nacho "11 ventas, $149.91 facturados". Estaba mal, conté
dos veces la venta del 16. El número correcto desde el 10/10 es **10 ventas y
$133.69**, que es lo que ya decía el PDF del informe.
