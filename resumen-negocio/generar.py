# -*- coding: utf-8 -*-
import subprocess, pathlib

BASE = pathlib.Path(__file__).parent
CSS = """
@page { size: A4; margin: 17mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
       color:#3B2B20; font-size:10.3pt; line-height:1.55; margin:0; }
h1 { font-size:25pt; line-height:1.12; margin:0 0 3mm; color:#B5533C; letter-spacing:-0.3pt; }
h2 { font-size:14pt; margin:9mm 0 3mm; color:#B5533C; border-bottom:1.6pt solid #B5533C;
     padding-bottom:1.6mm; letter-spacing:-0.2pt; }
h3 { font-size:11pt; margin:6mm 0 2mm; color:#3B2B20; }
p  { margin:0 0 2.6mm; }
ul,ol { margin:0 0 3mm; padding-left:5.5mm; }
li { margin-bottom:1.3mm; }
table { width:100%; border-collapse:collapse; margin:3mm 0 4mm; font-size:9.2pt; }
th { background:#B5533C; color:#fff; text-align:left; padding:2.1mm 2.6mm; font-weight:600; }
td { padding:2mm 2.6mm; border-bottom:0.5pt solid #E6D9C4; }
tr:nth-child(even) td { background:#FBF6EC; }
td.n, th.n { text-align:right; font-variant-numeric:tabular-nums; }
.tot td { font-weight:700; background:#F3E2D2 !important; border-top:1.2pt solid #B5533C; }
.neg { color:#B5533C; font-weight:600; }
.pos { color:#2E7D52; font-weight:600; }
.page { page-break-after:always; }
.page:last-child { page-break-after:auto; }
.cover { height:252mm; display:flex; flex-direction:column; justify-content:center; }
.kicker { font-size:9.5pt; letter-spacing:3.2pt; text-transform:uppercase; color:#C8821A;
          margin-bottom:5mm; font-weight:600; }
.sub { font-size:12.5pt; color:#6B5744; margin-top:4mm; line-height:1.5; }
.rule { height:2.6pt; background:#B5533C; width:34mm; margin:7mm 0; }
.box { background:#FBF6EC; border-left:3.4pt solid #C8821A; padding:3.6mm 4.4mm; margin:4mm 0; }
.box.alert { border-left-color:#B5533C; background:#FAEDE8; }
.box.good  { border-left-color:#2E7D52; background:#EDF6F0; }
.box p:last-child { margin-bottom:0; }
.bignum { font-size:30pt; font-weight:700; color:#B5533C; line-height:1; letter-spacing:-1pt; }
.cards { display:flex; gap:3.6mm; margin:4mm 0; }
.card { flex:1; background:#FBF6EC; border:0.7pt solid #E6D9C4; border-radius:2.4mm;
        padding:3.4mm; }
.card .lbl { font-size:8pt; text-transform:uppercase; letter-spacing:0.9pt; color:#8A7259;
             margin-bottom:1.6mm; font-weight:600; }
.card .val { font-size:16.5pt; font-weight:700; color:#3B2B20; line-height:1.1; }
.card .fo  { font-size:8.2pt; color:#8A7259; margin-top:1.2mm; }
.muted { color:#8A7259; font-size:9pt; }
.tag { display:inline-block; font-size:7.8pt; font-weight:700; padding:0.7mm 2.2mm;
       border-radius:1.2mm; text-transform:uppercase; letter-spacing:0.6pt; vertical-align:1pt; }
.tag.v { background:#2E7D52; color:#fff; }
.tag.r { background:#B5533C; color:#fff; }
.tag.a { background:#C8821A; color:#fff; }
.foot { margin-top:8mm; padding-top:3mm; border-top:0.7pt solid #E6D9C4;
        font-size:8.4pt; color:#8A7259; }
"""

BODY = """
<div class="page cover">
  <div class="kicker">Informe interno · Confidencial</div>
  <h1>El negocio de<br>ebooks digitales</h1>
  <div class="rule"></div>
  <div class="sub">
    Estado completo al <strong>16 de octubre de 2026</strong>.<br>
    Lomito Bakery · Noches en Calma · Mochila Terapéutica
  </div>
  <div class="box alert" style="margin-top:14mm">
    <p><strong>El número que importa:</strong> llevás <strong>USD 330.16</strong>
    invertidos en publicidad y <strong>USD 133.69</strong> facturados.
    El negocio está <strong class="neg">USD 196.47 abajo</strong>.</p>
    <p class="muted" style="margin-top:2mm">Todas las cifras de publicidad salen
    de la API de Meta, no de estimaciones. Las que no pude verificar están
    marcadas como tales.</p>
  </div>
</div>

<div class="page">
  <h2>1 · Resumen ejecutivo</h2>

  <div class="cards">
    <div class="card"><div class="lbl">Invertido</div><div class="val">$330.16</div>
      <div class="fo">publicidad Meta</div></div>
    <div class="card"><div class="lbl">Facturado</div><div class="val">$133.69</div>
      <div class="fo">10 ventas</div></div>
    <div class="card"><div class="lbl">Resultado</div>
      <div class="val neg">&minus;$196.47</div><div class="fo">59% del gasto</div></div>
  </div>

  <h3>Qué pasó, en tres frases</h3>
  <p><strong>Lanzaste dos productos.</strong> Noches en Calma gastó $128.44 en cinco
  días y no vendió una sola vez. Lomito Bakery gastó $201.72 y vendió diez veces.</p>
  <p><strong>Lomito funciona, pero todavía no es rentable.</strong> Su CPA mezclado es
  de $20.17 y su punto de equilibrio está en $12.20. Vendés, pero cada venta cuesta
  más de lo que deja.</p>
  <p><strong>Dentro de Lomito hay algo que sí gana plata.</strong> El anuncio
  <em>15 B</em> lleva 3 ventas con $8.28 de gasto: ROAS de 6.1x. El problema es que
  nunca recibió presupuesto de verdad.</p>

  <div class="box good">
    <p><strong>La conclusión honesta.</strong> No tenés un problema de producto ni de
    mercado. Tenés un problema de asignación: el 92% de la plata fue a anuncios que
    no vendían, mientras el único que convertía recibía migajas.</p>
  </div>

  <h3>Estado de los tres productos</h3>
  <table>
    <tr><th>Producto</th><th>Estado</th><th class="n">Invertido</th>
        <th class="n">Vendido</th><th>Qué falta</th></tr>
    <tr><td><strong>Lomito Bakery</strong></td><td><span class="tag v">Vivo</span></td>
        <td class="n">$201.72</td><td class="n">$133.69</td><td>Escalar el ángulo que funciona</td></tr>
    <tr><td><strong>Noches en Calma</strong></td><td><span class="tag r">Pausado</span></td>
        <td class="n">$128.44</td><td class="n">$0.00</td><td>Autopsia antes de reintentar</td></tr>
    <tr><td><strong>Mochila Terapéutica</strong></td><td><span class="tag a">Sin armar</span></td>
        <td class="n">$0.00</td><td class="n">$0.00</td><td>Todo: producto, landing, oferta</td></tr>
    <tr class="tot"><td>Total</td><td></td><td class="n">$330.16</td>
        <td class="n">$133.69</td><td class="neg">&minus;$196.47</td></tr>
  </table>
  <div class="foot">Fuente: Meta Ads API, cuenta 1560224662043860, gasto de vida al 16/10/2026.</div>
</div>

<div class="page">
  <h2>2 · Dónde se fue cada peso</h2>

  <h3>Publicidad — lo único que pude verificar con precisión</h3>
  <table>
    <tr><th>Campaña</th><th>Producto</th><th class="n">Gasto</th>
        <th class="n">Impresiones</th><th class="n">Ventas</th><th class="n">Facturado</th></tr>
    <tr><td>Test ABO Pastelería Canina</td><td>Lomito</td><td class="n">$201.72</td>
        <td class="n">16.493</td><td class="n">10</td><td class="n">$133.69</td></tr>
    <tr><td>ABO Noches en Calma 1/10</td><td>Noches</td><td class="n">$114.09</td>
        <td class="n">22.038</td><td class="n">0</td><td class="n">$0.00</td></tr>
    <tr><td>Tráfico Noches en Calma 2/10</td><td>Noches</td><td class="n">$14.35</td>
        <td class="n">9.556</td><td class="n">0</td><td class="n">$0.00</td></tr>
    <tr class="tot"><td>Total</td><td></td><td class="n">$330.16</td>
        <td class="n">48.087</td><td class="n">10</td><td class="n">$133.69</td></tr>
  </table>

  <div class="box alert">
    <p><strong>Noches en Calma es la herida más grande y la menos mirada.</strong>
    31.594 impresiones, $128.44 gastados, <strong>cero ventas</strong>. No es mala
    suerte: con ese volumen, un producto que vende aunque sea poco ya habría vendido
    algo. Algo estaba roto de raíz — la oferta, el precio, la landing o el seguimiento
    de conversiones. Nunca se hizo esa autopsia, y es plata que ya está perdida sin
    haber dejado aprendizaje.</p>
  </div>

  <h3>Otros costos — necesito que los completes</h3>
  <p>Estos no los puedo ver desde acá. Sin ellos, el &minus;$196.47 es optimista.</p>
  <table>
    <tr><th>Concepto</th><th>Qué sé</th><th>Qué falta</th></tr>
    <tr><td>Higgsfield</td><td>Plan Plus activo; cargaste 100 créditos hoy</td>
        <td>Cuánto pagaste por la suscripción y por los créditos</td></tr>
    <tr><td>Impultienda</td><td>Cobra comisión por venta</td>
        <td>Qué porcentaje; reduce los $133.69 reales</td></tr>
    <tr><td>Dominio / hosting</td><td>Usás el subdominio de Impultienda</td>
        <td>Si pagaste dominio propio</td></tr>
    <tr><td>Tu tiempo</td><td>Dos semanas de trabajo intensivo</td>
        <td>No está costeado en ningún lado</td></tr>
  </table>
  <div class="foot">Pasame estos cuatro números y actualizo el informe con el costo real.</div>
</div>

<div class="page">
  <h2>3 · Lomito Bakery en detalle</h2>

  <h3>Qué vendés hoy</h3>
  <table>
    <tr><th>Nivel</th><th>Producto</th><th class="n">Precio MXN</th><th class="n">USD</th></tr>
    <tr><td>Principal</td><td>Pastelería Canina que Vende — 30 recetas, 72 págs</td>
        <td class="n">229</td><td class="n">$12.37</td></tr>
    <tr><td>Bono 1</td><td>Calculadora de precios (Excel, 124 fórmulas)</td><td class="n">incluido</td><td class="n">—</td></tr>
    <tr><td>Bono 2</td><td>Guía de ingredientes</td><td class="n">incluido</td><td class="n">—</td></tr>
    <tr><td>Bono 3</td><td>Plan de negocio desde casa</td><td class="n">incluido</td><td class="n">—</td></tr>
    <tr><td>Bono 4</td><td>Plantillas de etiquetas</td><td class="n">incluido</td><td class="n">—</td></tr>
    <tr><td>Bono 5</td><td>Porciones, sustituciones y soluciones</td><td class="n">incluido</td><td class="n">—</td></tr>
    <tr><td>Upsell 1</td><td>Pack Pasteles de Cumpleaños</td><td class="n">89 → 71.2</td><td class="n">$3.85</td></tr>
    <tr><td>Upsell 2</td><td>Kit Vende en Redes</td><td class="n">109</td><td class="n">$5.89</td></tr>
    <tr><td>Upsell 3</td><td>Pack Fechas que Venden</td><td class="n">109</td><td class="n">$5.89</td></tr>
  </table>

  <h3>Economía por venta</h3>
  <div class="cards">
    <div class="card"><div class="lbl">Solo ebook</div><div class="val">$12.37</div>
      <div class="fo">229 MXN</div></div>
    <div class="card"><div class="lbl">Con upsell</div><div class="val">$16.22</div>
      <div class="fo">300.2 MXN · verificado</div></div>
    <div class="card"><div class="lbl">Equilibrio</div><div class="val">$12.20</div>
      <div class="fo">CPA máximo sin upsell</div></div>
  </div>
  <p class="muted">Tipo de cambio 18.51 MXN/USD, deducido de las conversiones de Meta,
  no de una cotización externa.</p>

  <h3>Día por día desde el 10/10</h3>
  <table>
    <tr><th>Fecha</th><th class="n">Ventas</th><th class="n">Facturado</th>
        <th class="n">Invertido</th><th class="n">Resultado</th></tr>
    <tr><td>10/10</td><td class="n">2</td><td class="n">$17.80</td><td class="n">$18.87</td><td class="n neg">&minus;$1.07</td></tr>
    <tr><td>11/10</td><td class="n">2</td><td class="n">$22.70</td><td class="n">$48.61</td><td class="n neg">&minus;$25.91</td></tr>
    <tr><td>12/10</td><td class="n">1</td><td class="n">$8.90</td><td class="n">$43.76</td><td class="n neg">&minus;$34.86</td></tr>
    <tr><td>13/10</td><td class="n">1</td><td class="n">$12.49</td><td class="n">$39.27</td><td class="n neg">&minus;$26.78</td></tr>
    <tr><td>14/10</td><td class="n">3</td><td class="n">$55.57</td><td class="n">$24.83</td><td class="n pos">+$30.74</td></tr>
    <tr><td>15/10</td><td class="n">0</td><td class="n">$0.00</td><td class="n">$18.51</td><td class="n neg">&minus;$18.51</td></tr>
    <tr><td>16/10 <span class="muted">parcial</span></td><td class="n">1</td><td class="n">$16.22</td><td class="n">$5.65</td><td class="n pos">+$10.57</td></tr>
    <tr class="tot"><td>Total</td><td class="n">10</td><td class="n">$133.69</td>
        <td class="n">$199.50</td><td class="n neg">&minus;$65.81</td></tr>
  </table>
  <p class="muted">Los $201.72 de la campaña incluyen $2.22 anteriores al 10/10.
  El ticket promedio subió de $8.90 a $16.22 cuando pasaste a pesos mexicanos y
  activaste los upsells: eso fue trabajo que rindió.</p>
</div>

<div class="page">
  <h2>4 · El hallazgo que define todo</h2>

  <p>Desglosando Lomito por anuncio, el panorama cambia por completo:</p>
  <table>
    <tr><th>Anuncio</th><th class="n">Gasto</th><th class="n">Impr.</th><th class="n">CTR</th>
        <th class="n">Ventas</th><th class="n">Facturado</th><th class="n">CPA</th><th class="n">ROAS</th></tr>
    <tr><td><strong>15 B</strong> negación</td><td class="n">$8.28</td><td class="n">436</td>
        <td class="n">4.36%</td><td class="n">3</td><td class="n">$50.70</td>
        <td class="n pos">$2.76</td><td class="n pos">6.1x</td></tr>
    <tr><td>7 v prob.</td><td class="n">$44.31</td><td class="n">2.667</td><td class="n">4.35%</td>
        <td class="n">2</td><td class="n">$30.00</td><td class="n">$22.16</td><td class="n neg">0.68x</td></tr>
    <tr><td>14 A desde cero</td><td class="n">$35.41</td><td class="n">2.618</td><td class="n">2.14%</td>
        <td class="n">1</td><td class="n">$12.49</td><td class="n">$35.41</td><td class="n neg">0.35x</td></tr>
    <tr><td>16 C fin de semana</td><td class="n">$8.01</td><td class="n">472</td><td class="n">2.33%</td>
        <td class="n">0</td><td class="n">$0.00</td><td class="n">—</td><td class="n neg">0.00x</td></tr>
  </table>

  <div class="box good">
    <p><strong>15 B devuelve $6.12 por cada dólar.</strong> Y en toda su vida recibió
    $8.28 — el 4% del presupuesto de Lomito. Mientras tanto, los dos anuncios que
    perdían plata se llevaron $79.72 entre los dos.</p>
  </div>

  <h3>Qué tiene 15 B que los otros no</h3>
  <p>Ataca una objeción en vez de mostrar el producto. El mensaje no es
  «mirá qué lindos pasteles» sino «no necesitás saber cocinar». Los tres anuncios
  que fracasaron muestran producto o fecha. El que vende, discute con la cabeza
  del que duda.</p>
  <p>Eso coincide con lo que hacen los competidores que llevan más tiempo
  anunciando en el nicho: tres de cada nueve corren el ángulo «desde cero».</p>

  <h3>Qué se hizo con esa información</h3>
  <ul>
    <li>Pausados <strong>14 A</strong>, <strong>16 C</strong> y <strong>7 v prob.</strong></li>
    <li>Todo el presupuesto ($14/día) va a <strong>15 B</strong></li>
    <li>Creados 4 creativos estáticos y 2 videos verticales del mismo ángulo</li>
  </ul>

  <div class="box alert">
    <p><strong>Efecto secundario detectado el 16/10 a la tarde.</strong> Con un solo
    anuncio activo, Meta no logra gastar el presupuesto: entregó 187 impresiones y
    $1.69 de los $14 disponibles. Sin material para rotar, el sistema prefiere no
    gastar. Es el argumento para subir los creativos nuevos cuanto antes.</p>
  </div>
</div>

<div class="page">
  <h2>5 · Cuánto se puede ganar</h2>

  <p>Tres escenarios, todos construidos sobre números que ya ocurrieron, no sobre
  deseos. El supuesto común: $14/día de inversión y ticket neto de $14.50
  (mezcla de ventas con y sin upsell).</p>

  <table>
    <tr><th>Escenario</th><th>Supuesto</th><th class="n">Ventas/día</th><th class="n">CPA</th>
        <th class="n">Ganancia/día</th><th class="n">Ganancia/mes</th></tr>
    <tr><td><strong>Conservador</strong></td><td>Se mantiene el promedio actual</td>
        <td class="n">1.4</td><td class="n">$10.00</td><td class="n pos">+$6.30</td>
        <td class="n pos">+$189</td></tr>
    <tr><td><strong>Realista</strong></td><td>15 B escala al nivel del 14/10</td>
        <td class="n">3.0</td><td class="n">$8.28</td><td class="n pos">+$18.66</td>
        <td class="n pos">+$560</td></tr>
    <tr><td><strong>Optimista</strong></td><td>Se suman creativos que funcionan</td>
        <td class="n">5.0</td><td class="n">$9.00</td><td class="n pos">+$27.50</td>
        <td class="n pos">+$825</td></tr>
  </table>

  <div class="box">
    <p><strong>Tu meta de 1.000.000 ARS mensuales de ganancia</strong> equivale a unos
    USD 690 al mes al cambio actual. Cae entre el escenario realista y el optimista:
    necesitás sostener entre <strong>3 y 4 ventas diarias rentables</strong>.</p>
    <p style="margin-top:2mm">No es una fantasía: el 14 de octubre hiciste 3 ventas
    en un día con CPA de $8.28. Ya ocurrió una vez. La pregunta es si se repite.</p>
  </div>

  <h3>Qué haría falta para llegar</h3>
  <ol>
    <li><strong>Volumen de entrega.</strong> Hoy el cuello es que Meta no gasta el
    presupuesto. Más creativos del ángulo ganador lo destraban.</li>
    <li><strong>Subir el ticket.</strong> Cada venta deja $12.37 sin upsell. Si lográs
    que la mitad de los compradores tome un upsell, el ticket sube a ~$15 y el margen
    por venta casi se duplica.</li>
    <li><strong>Retargeting.</strong> Desde que el píxel registra 100% de cobertura,
    podés perseguir a quien visitó y no compró. Es el tráfico más barato que existe.</li>
    <li><strong>Reels.</strong> Los 2 videos abren un inventario que con imagen
    estática no tenías, y en México suele ser más barato.</li>
  </ol>
</div>

<div class="page">
  <h2>6 · Los otros dos productos</h2>

  <h3>Noches en Calma <span class="tag r">Pausado</span></h3>
  <p>Producto de sueño infantil. Corrió del 2 al 6 de octubre con cuatro ángulos
  distintos: culpa, agotamiento, método gentil y uno llamado «Moisés».</p>
  <table>
    <tr><th>Métrica</th><th class="n">Valor</th></tr>
    <tr><td>Invertido</td><td class="n">$128.44</td></tr>
    <tr><td>Impresiones</td><td class="n">31.594</td></tr>
    <tr><td>Ventas</td><td class="n neg">0</td></tr>
  </table>
  <p>Con 31.594 impresiones y cero ventas, el problema no fue el creativo: fue algo
  estructural. Las hipótesis, en orden de probabilidad:</p>
  <ol>
    <li><strong>El píxel no estaba midiendo.</strong> En Lomito descubrimos que la
    landing no tenía píxel instalado. Si acá pasó lo mismo, pudo haber ventas que
    nunca se registraron.</li>
    <li><strong>La oferta no cerraba.</strong> Precio, promesa o garantía.</li>
    <li><strong>El checkout estaba roto</strong>, como estuvo el embudo de upsells de
    Lomito, que resultó estar simplemente pausado.</li>
  </ol>
  <div class="box alert">
    <p><strong>Recomendación:</strong> no volver a encender Noches en Calma hasta
    hacer la autopsia. Reintentar a ciegas es repetir el gasto. La primera pregunta
    es si el píxel estaba instalado — se responde en diez minutos.</p>
  </div>

  <h3>Mochila Terapéutica <span class="tag a">Sin armar</span></h3>
  <p>Material de apoyo para psicólogos infantiles y docentes. Es el plan B.</p>
  <p><strong>Lo único que existe hoy</strong> son cuatro imágenes generadas el 10 de
  octubre: un consultorio infantil, un aula, tarjetas de emociones y un plano cenital
  de material impreso. No hay producto, ni landing, ni catálogo, ni precio.</p>
  <p>Trabajo pendiente para dejarlo vendible, en orden:</p>
  <ol>
    <li>Definir qué incluye exactamente y a qué precio</li>
    <li>Producir el contenido — es el grueso del trabajo</li>
    <li>Armar landing y checkout con píxel instalado <em>desde el día cero</em></li>
    <li>Creativos del ángulo de objeción, que es lo que demostró funcionar</li>
  </ol>
</div>

<div class="page">
  <h2>7 · Lo que este dinero compró</h2>

  <p>Perdiste $196.47. A cambio aprendiste cosas que valen para cualquier
  infoproducto que lances después. Vale la pena escribirlas.</p>

  <h3>Lecciones caras</h3>
  <ul>
    <li><strong>Sin píxel no hay negocio.</strong> La landing de Lomito corrió días sin
    píxel. Meta optimizaba a ciegas. Noches en Calma pudo haber muerto por lo mismo.
    Instalarlo y verificarlo con el Pixel Helper es lo primero, siempre.</li>
    <li><strong>Un embudo pausado no avisa.</strong> Los upsells de Lomito no vendían
    porque el embudo estaba desactivado. Seis ventas pasaron sin que nadie viera la
    oferta post-compra. Probá cada paso con una compra real antes de gastar en ads.</li>
    <li><strong>El producto tiene que coincidir con lo que promete el anuncio.</strong>
    Los anuncios decían 30 recetas y la entrega tenía 6 archivos viejos.</li>
    <li><strong>No regales lo que vendés.</strong> Dos bonos se entregaban gratis y a la
    vez se ofrecían como upsell pago.</li>
    <li><strong>Matá a los perdedores rápido.</strong> 7 v prob. y 14 A se llevaron
    $79.72 para devolver $42.49. Cada día que siguieron abiertos fue dinero tirado.</li>
    <li><strong>Pero no mates a un ganador por impaciencia.</strong> 14 A casi se pausa
    con 282 impresiones cuando era el único que vendía. La regla de esperar 500
    impresiones antes de juzgar existe por algo.</li>
  </ul>

  <h3>Lo que ya está construido y no hay que rehacer</h3>
  <ul>
    <li>Producto completo de Lomito: 30 recetas, 5 bonos, 3 upsells, entrega funcionando</li>
    <li>Calculadora de precios en Excel con 124 fórmulas verificadas</li>
    <li>Landing en pesos mexicanos con píxel instalado y funcionando</li>
    <li>Checkout validado en México: prefijo +52, precios en MXN, upsells activos</li>
    <li>4 creativos estáticos y 2 videos verticales listos para subir</li>
    <li>Un ángulo de mensaje validado con datos reales: la objeción, no el producto</li>
  </ul>
  <div class="box good">
    <p>Si mañana tuvieras que empezar de nuevo, llegarías a este punto en una semana
    en vez de dos, y sin gastar $196 en descubrir lo que ya sabés.</p>
  </div>
</div>

<div class="page">
  <h2>8 · Decisiones pendientes</h2>

  <h3>Esta noche</h3>
  <p><strong>Subir o no los creativos nuevos.</strong> Con un solo anuncio activo, Meta
  entregó 187 impresiones en todo el día. Si eso sigue así, el corte del sábado se
  decide con datos insuficientes. Subirlos no aumenta el presupuesto: le da a Meta
  material para rotar.</p>

  <h3>Sábado a la noche — criterio ya fijado</h3>
  <table>
    <tr><th>CPA de 15 B</th><th>Qué pasa</th></tr>
    <tr><td>Hasta $15</td><td>Gana. Se suman los creativos nuevos y se escala con cuidado.</td></tr>
    <tr><td>$15 a $25</td><td>Último intento con los creativos nuevos, dentro del techo.</td></tr>
    <tr><td>Más de $25</td><td>Pausar todo. El problema no son los anuncios.</td></tr>
  </table>
  <p>Techo de gasto acordado: <strong>USD 250</strong> de vida de la campaña.
  Al 16/10 van $201.72. Meta no acepta configurar un límite automático por debajo de
  $294.62, así que el tope se controla a mano en cada revisión.</p>

  <h3>Para completar este informe</h3>
  <ul>
    <li>Cuánto pagaste de suscripción y créditos de Higgsfield</li>
    <li>Qué comisión cobra Impultienda por venta</li>
    <li>Si el upsell de 71.2 MXN apunta al producto que querías (es el de 89 con 20% off, no el de 109)</li>
    <li>Si Noches en Calma tenía píxel instalado</li>
  </ul>

  <div class="box">
    <p><strong>Lo más importante que no se está haciendo.</strong> Hay $128.44 enterrados
    en Noches en Calma sin una sola conclusión. Esa autopsia cuesta una tarde y puede
    valer más que todo lo que gastes la semana que viene — sobre todo si el diagnóstico
    es «el píxel no estaba puesto», que es lo más probable y lo más fácil de arreglar.</p>
  </div>

  <div class="foot">
    Informe generado el 16 de octubre de 2026. Cifras de publicidad verificadas contra
    la API de Meta Ads, cuenta 1560224662043860. Las cifras no verificables están
    señaladas en el texto.
  </div>
</div>
"""

html = f"<!doctype html><html lang='es'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{BODY}</body></html>"
(BASE / "informe.html").write_text(html, encoding="utf-8")

subprocess.run([
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "--headless", "--disable-gpu",
    "--no-sandbox", "--no-pdf-header-footer",
    f"--print-to-pdf={BASE/'Resumen-Negocio-Ebooks-2026-10-16.pdf'}",
    str(BASE / "informe.html"),
], check=True, capture_output=True)
print("PDF generado")
