# Break-even · Repostería que Vende

Calculado el 2026-10-23, con la comisión del 2% que reportó Nacho.

---

## El número para decidir

**CPA de break-even: $12.20 USD.**

Es el conservador, el mismo de Lomito. Abajo está por qué no uso $12.64.

| Escenario | Precio | Retención | Neto por venta |
|---|---|---|---|
| Solo 2% (lo reportado) | $12.90 | $0.26 | **$12.64** |
| 5,4% (el real de Lomito) | $12.90 | $0.70 | **$12.20** |

La diferencia entre los dos es de $0.44 por venta. Sobre 20 ventas son $8.80:
no cambia una decisión de apagar o escalar, pero sí la diferencia entre creer
que estás en break-even y estar perdiendo.

## La discrepancia que hay que resolver

Lomito vende al mismo precio, $12.90, y su break-even verificado es **$12.20**.
Eso implica una retención total del **5,4%**, no del 2%.

Son 3,4 puntos que faltan. La explicación más probable es que haya **dos
cobros distintos**:

- **Impultienda** (la plataforma): el 2% que reportó Nacho
- **Impul Pay** (la pasarela): su propia comisión, que en México suele andar
  en 3,5% más IVA

Mientras no esté confirmado, **se usa $12.20**. Equivocarse para el lado
pesimista cuesta dejar pasar alguna venta marginal; equivocarse para el otro
lado es gastar pensando que estás empatando cuando estás perdiendo.

### Cómo se resuelve en dos minutos
Nacho ya tiene ventas reales de Lomito. En la liquidación de Impultienda,
mirar **cuánto se depositó por una venta de $12.90**. Ese número, dividido
por 12.90, da la retención real. No hay que estimarlo: está en la cuenta.

## Con upsell

| | Ticket | Neto al 5,4% |
|---|---|---|
| Solo el curso | $12.90 | $12.20 |
| Curso + Pastelería de Fiesta | $19.60 | $18.54 |
| Curso + los tres upsells | $35.40 | $33.49 |

**El break-even con upsell NO se usa para decidir todavía.** En Lomito el
ticket promedio real es $16.65, pero eso se supo después de varias ventas.
Acá no hay ninguna: suponer que la gente va a comprar el upsell antes de
tener una sola venta es exactamente cómo se justifica un CPA que no cierra.

Se arranca con **$12.20** y se recalcula cuando haya 5 o más ventas y se
sepa el ticket promedio real.

## Cómo se lee en el cierre diario

| CPA | Qué significa |
|---|---|
| menos de $8 | escalar |
| $8 a $12.20 | rentable, dejar correr |
| $12.20 a $15 | pierde poco; aguanta solo si el ticket promedio sube con upsells |
| más de $15 | apagar |

Y el freno duro que no cambia: **$100 de test, y a los $100 con 0-1 ventas se
mata.** Sin "un día más".
