# -*- coding: utf-8 -*-
"""Genera el HTML del ebook. Luego se convierte a PDF con Chromium headless."""
import io, html, subprocess, sys, os
from recetas import R, CATEGORIAS, ORDEN

ESC = html.escape
OUT_HTML = "ebook.html"
OUT_PDF = "Pasteleria-Canina-que-Vende-2026-30-recetas.pdf"

CSS = """
@page { size: 140mm 210mm; margin: 0; }
*{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{height:100%}
:root{--cream:#FDF3E3;--cream2:#FBE9D2;--terra:#B5533C;--terra2:#9A4330;--mint:#9FD5BA;
      --mintl:#CDEADC;--brown:#3B2B20;--muted:#7A6354;--line:#E3D2BC;--red:#C8372A}
body{font-family:'Inter',sans-serif;color:var(--brown);font-size:9pt;line-height:1.5}
.serif{font-family:'Bitstream Charter','DejaVu Serif',serif}
.p{width:140mm;height:209.8mm;background:var(--cream);position:relative;overflow:hidden;
   page-break-after:always;display:flex;flex-direction:column}
.p:last-child{page-break-after:auto}
.pad{padding:10mm 11mm}
.grow{flex:1}
.hdbar{background:var(--terra);color:#fff;padding:4.5mm 11mm;font-size:7pt;font-weight:800;letter-spacing:.14em}
.ttl{font-size:21pt;font-weight:800;line-height:1.1}
.ttl2{font-size:16pt;font-weight:800;line-height:1.12}
.kick{font-size:7.5pt;font-weight:800;letter-spacing:.16em;color:var(--terra);text-transform:uppercase}
.lede{font-size:9.5pt;color:var(--muted);line-height:1.5}
.pill{display:inline-block;background:var(--mint);color:var(--brown);font-size:6.5pt;
      font-weight:800;padding:1.2mm 3.2mm;border-radius:99px;letter-spacing:.12em}
.pill.new{background:var(--terra);color:#fff}
.note{background:var(--brown);color:#fff;border-radius:2.5mm;padding:3mm 4mm;font-size:8pt}
.note b{color:var(--mint)}
.warn{background:var(--red);color:#fff;border-radius:2.5mm;padding:3mm 4mm;font-size:8pt;font-weight:700}
.card{border:1.1pt solid var(--line);border-radius:3mm;overflow:hidden;background:#fffdf8}
.row{display:flex;justify-content:space-between;padding:2.6mm 4mm;font-size:8.8pt;border-bottom:1pt solid var(--line)}
.row:last-child{border-bottom:0}
.row b{font-weight:700}
.price{background:var(--terra);color:#fff;border-radius:3mm;padding:4mm;text-align:center}
.price .big{font-size:12pt;font-weight:800}
.price .sm{font-size:7.5pt;opacity:.9;margin-top:.8mm}
.cols{display:flex;gap:5mm}
.lbl{font-size:7.5pt;font-weight:800;color:var(--terra);letter-spacing:.12em;margin-bottom:2.5mm}
.ing{display:flex;gap:2.2mm;align-items:flex-start;margin-bottom:2.4mm;font-size:8.2pt;line-height:1.28}
.ing i{width:4.6mm;height:4.6mm;flex:0 0 4.6mm;border-radius:50%;background:var(--terra);color:#fff;
       font-style:normal;font-size:6pt;font-weight:800;display:flex;align-items:center;justify-content:center;margin-top:.3mm}
.ing:nth-child(even) i{background:var(--mint);color:var(--brown)}
.stp{display:flex;gap:2.2mm;align-items:center;border-radius:2.2mm;padding:2mm 2.6mm;margin-bottom:1.8mm;
     font-size:8.2pt;line-height:1.25;background:var(--terra);color:#fff}
.stp:nth-child(even){background:var(--mintl);color:var(--brown)}
.stp i{font-style:normal;font-weight:800;font-size:9pt;min-width:3.6mm}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.box{background:var(--cream2);border-radius:2.6mm;padding:3mm;font-size:8pt}
.box b{display:block;font-size:8.5pt;margin-bottom:.8mm}
.tbl{width:100%;border-collapse:collapse;font-size:8pt}
.tbl td{border:1pt solid var(--line);padding:2.2mm 3mm}
.tbl td:first-child{font-weight:700;width:34%}
.divider{align-items:center;justify-content:center;text-align:center;background:var(--mint);padding:0 14mm}
.divider .let{font-size:60pt;font-weight:800;color:var(--terra);line-height:.9}
.divider .nm{font-size:22pt;font-weight:800;margin-top:3mm;letter-spacing:-.01em}
.divider .sb{font-size:10pt;color:var(--brown);opacity:.75;margin-top:1.5mm}
.divider ol{list-style:none;margin-top:7mm;text-align:left;width:100%}
.divider ol li{display:flex;gap:3mm;font-size:9pt;margin-bottom:2.2mm;align-items:center}
.divider ol li span{background:var(--terra);color:#fff;font-size:6.5pt;font-weight:800;
                    border-radius:99px;padding:.9mm 2.4mm;min-width:7mm;text-align:center}
.toc li{display:flex;align-items:baseline;gap:2mm;font-size:10pt;margin-bottom:3.4mm}
.toc li b{min-width:7mm;color:var(--terra);font-weight:800}
.toc li i{flex:1;border-bottom:1.2pt dotted var(--line);font-style:normal}
.fnote{font-size:7pt;color:var(--muted);text-align:center}
.cvr{text-align:center;padding:14mm 12mm}
.cvr h1{font-size:33pt;line-height:.97;font-weight:800;margin-top:5mm}
.cvr h1 .q{color:var(--terra);display:block;font-size:24pt;margin-top:1.5mm}
.cvr .badge{position:absolute;right:11mm;top:31mm;width:19mm;height:19mm;border-radius:50%;
            background:var(--mint);display:flex;flex-direction:column;align-items:center;
            justify-content:center;font-size:5.5pt;font-weight:800}
.cvr .badge b{font-size:11pt}
.cvr .hero{flex:1;margin:6mm 0 5mm;border-radius:4mm;
           background:linear-gradient(160deg,#F3DFC4,#E8CBA6);display:flex;
           align-items:center;justify-content:center;font-size:42pt}
.chips{display:flex;gap:3mm}
.chips .c{flex:1;background:var(--cream2);border:1.2pt solid var(--terra);border-radius:3mm;padding:3mm 1mm;text-align:center}
.chips .c b{display:block;font-size:15pt;font-weight:800;line-height:1}
.chips .c span{font-size:6.5pt;color:var(--muted)}
"""

P = []
def page(cls, inner): P.append(f'<div class="p {cls}">{inner}</div>')

def recipe_head(r):
    tag = '<span class="pill new">NUEVA · RECETA %02d</span>' % r["n"] if r["nuevo"] \
          else '<span class="pill">RECETA %02d</span>' % r["n"]
    return f'<div class="hdbar" style="padding-bottom:5.5mm">{tag}' \
           f'<div class="ttl serif" style="margin-top:3mm;letter-spacing:0">{ESC(r["titulo"]).upper()}</div></div>'

def page_ficha(r):
    rows = "".join(f'<div class="row"><span>{k}</span><b>{ESC(v)}</b></div>'
                   for k, v in [("Nivel", r["nivel"]), ("Rinde", r["rinde"]),
                                ("Tiempo", r["tiempo"]), ("Duración", r["duracion"]),
                                ("Costo aprox.", r["costo"])])
    tam = "".join(f'<tr><td>{ESC(a)}</td><td>{ESC(b)}</td></tr>' for a, b in r["tam"])
    cons = "".join(f'<tr><td>{ESC(a)}</td><td>{ESC(b)}</td></tr>' for a, b in r["cons"])
    page("", recipe_head(r) + f"""
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="lede" style="margin-bottom:5mm">{ESC(r["lede"])}</div>
        <div class="card" style="margin-bottom:5mm">{rows}</div>
        <div class="lbl">TAMAÑOS Y RENDIMIENTO</div>
        <table class="tbl" style="margin-bottom:5mm">{tam}</table>
        <div class="lbl">CONSERVACIÓN</div>
        <table class="tbl">{cons}</table>
        <div class="grow"></div>
        <div class="price"><div class="big">{ESC(r["venta"])}</div>
          <div class="sm">Margen aproximado {ESC(r["margen"])} · costo {ESC(r["costo"])}</div></div>
      </div>""")

def page_pasos(r):
    ing = "".join(f'<div class="ing"><i>{i}</i><div>{ESC(x)}</div></div>'
                  for i, x in enumerate(r["ing"], 1))
    pas = "".join(f'<div class="stp"><i>{i}</i><div>{ESC(x)}</div></div>'
                  for i, x in enumerate(r["pasos"], 1))
    formas = "".join(f'<div class="box">{ESC(f)}</div>' for f in r["formas"])
    page("", f"""
      <div class="hdbar">PASO A PASO · RECETA {r["n"]:02d}
        <div class="ttl2 serif" style="letter-spacing:0;margin-top:1.5mm">{ESC(r["titulo"]).upper()}</div></div>
      <div class="pad grow" style="display:flex;flex-direction:column">
        <div class="cols grow">
          <div style="width:41%"><div class="lbl">INGREDIENTES</div>{ing}</div>
          <div style="flex:1"><div class="lbl">PREPARACIÓN</div>{pas}</div>
        </div>
        <div class="warn" style="margin-top:3mm">⚠ {ESC(r["alerta"])}</div>
        <div class="lbl" style="margin-top:4mm">4 FORMAS DE VENDER</div>
        <div class="grid2">{formas}</div>
        <div class="note" style="margin-top:3.5mm"><b>CONSEJO:</b> {ESC(r["consejo"])}</div>
      </div>""")

# ───────────────────────── PORTADA ─────────────────────────
page("cvr", """
  <div class="kick">LOMITO BAKERY PRESENTA</div>
  <h1 class="serif">PASTELERÍA<br>CANINA<span class="q">QUE VENDE</span></h1>
  <div class="badge"><span>EDICIÓN</span><b>2026</b></div>
  <div class="lede" style="margin-top:4mm">Recetas para lomitos y cómo convertirlas<br>en tu negocio desde casa</div>
  <div class="hero">🦴 🧁 🎂</div>
  <div class="chips">
    <div class="c"><b>30</b><span>recetas</span></div>
    <div class="c"><b>5</b><span>categorías</span></div>
    <div class="c"><b style="font-size:8.5pt;line-height:1.25;margin-top:2mm">Plan de<br>negocio</b><span></span></div>
  </div>
  <div class="fnote" style="margin-top:5mm;font-weight:700">Lomito Bakery · 2026</div>""")

# ───────────────────────── BIENVENIDA ─────────────────────────
page("", """
  <div class="hdbar">BIENVENIDA</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">¡Te damos la bienvenida!</div>
    <div class="lede" style="margin-top:4mm">En esta guía aprenderás a preparar galletas, pupcakes,
      pasteles, snacks y premios saludables para perros y gatos, y a venderlos desde tu cocina.</div>
    <div class="lede" style="margin-top:3mm">Cada receta incluye <b style="color:#3B2B20">cuánto te cuesta
      producirla, a cuánto venderla y qué margen deja</b>. No es solo un recetario: es un negocio
      con los números hechos.</div>
    <div class="grid2" style="margin-top:6mm">
      <div class="box"><b>📘 Recetas fáciles</b>Paso a paso, desde cero, aunque nunca hayas horneado.</div>
      <div class="box"><b>🥕 Ingredientes seguros</b>Todo de súper y económico.</div>
      <div class="box"><b>💰 Precios calculados</b>Costo, precio de venta y margen en cada receta.</div>
      <div class="box"><b>📦 Plan para vender</b>Empaque, formatos y primeros pedidos.</div>
    </div>
    <div class="grow"></div>
    <div class="warn">Importante: estas recetas son premios y no sustituyen el alimento diario de tu mascota.
      Consulta al veterinario ante alergias o condiciones de salud.</div>
  </div>""")

# ───────────────────────── ÍNDICE ─────────────────────────
items = [("1", "Fundamentos")] + \
        [(chr(65 + i), CATEGORIAS[c][0].title()) for i, c in enumerate(ORDEN)] + \
        [("6", "Tu negocio")]
toc = "".join(f'<li><b>{a}</b><i></i><span>{ESC(b)}</span></li>' for a, b in items)
page("", f"""
  <div class="hdbar">ÍNDICE</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif" style="margin-bottom:7mm">ÍNDICE</div>
    <ul class="toc" style="list-style:none">{toc}</ul>
    <div class="grow"></div>
    <div class="price"><div class="big">30 recetas probadas</div>
      <div class="sm">+ plan para vender desde casa</div></div>
  </div>""")

# ───────────────────────── FUNDAMENTOS ─────────────────────────
page("divider", """
  <div class="kick" style="color:#3B2B20">PARTE 1</div>
  <div class="let serif">1</div>
  <div class="nm serif">FUNDAMENTOS</div>
  <ol><li><span>1</span>Equipo básico</li><li><span>2</span>Ingredientes seguros</li>
      <li><span>3</span>Ingredientes prohibidos</li><li><span>4</span>Higiene y conservación</li></ol>""")

equipo = ["Horno", "Charola para hornear", "Papel para hornear", "Tazón grande",
          "Rodillo", "Cortadores de galletas", "Molde para muffins", "Frascos herméticos"]
page("", f"""
  <div class="hdbar">FUNDAMENTOS · EQUIPO BÁSICO</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">Todo lo que necesitas ya está en tu cocina</div>
    <div class="grid2" style="margin-top:6mm">{"".join(f'<div class="box"><b>{ESC(e)}</b></div>' for e in equipo)}</div>
    <div class="grow"></div>
    <div class="note"><b>EXTRA RECOMENDADO:</b> cortadores en forma de hueso y de huellita.
      Son los que más venden.</div>
  </div>""")

seguros = ["Avena", "Harina de arroz", "Plátano", "Calabaza", "Camote", "Zanahoria",
           "Manzana sin semillas", "Huevo", "Pollo cocido", "Yogur natural sin azúcar",
           "Crema de cacahuate sin xilitol", "Aceite de coco"]
page("", f"""
  <div class="hdbar" style="background:#4E8D6E">FUNDAMENTOS · INGREDIENTES SEGUROS</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">Tu despensa canina</div>
    <div class="grid2" style="margin-top:6mm">
      {"".join(f'<div class="box" style="background:#DFF0E6"><b>✓ {ESC(s)}</b></div>' for s in seguros)}</div>
    <div class="grow"></div>
    <div class="price" style="background:#4E8D6E"><div class="big">Siempre sin sal, sin azúcar y sin condimentos</div></div>
  </div>""")

prohibidos = ["Chocolate y cacao", "Xilitol", "Uvas y pasas", "Cebolla", "Ajo",
              "Nueces de macadamia", "Aguacate", "Café y alcohol", "Exceso de sal"]
page("", f"""
  <div class="hdbar" style="background:#C8372A">FUNDAMENTOS · INGREDIENTES PROHIBIDOS</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif" style="color:#C8372A">Nunca los uses</div>
    <div class="grid2" style="margin-top:6mm">
      {"".join(f'<div class="box" style="background:#FBE0DC"><b>✕ {ESC(s)}</b></div>' for s in prohibidos)}</div>
    <div class="grow"></div>
    <div class="warn">Si tu mascota come alguno, llama de inmediato al veterinario.</div>
  </div>""")

dur = [("Galletas secas", "Frasco hermético: 7 días", "Congelador: 3 meses"),
       ("Con pollo o hígado", "Refrigerador: 5 días", "Congelador: 2 meses"),
       ("Pasteles con betún", "Refrigerador: 3 días", "No congelar"),
       ("Paletas heladas", "Congelador: 1 mes", "No recongelar"),
       ("Deshidratados", "Frasco hermético: 2 semanas", "Congelador: 3 meses")]
filas = "".join(f'<tr><td>{ESC(a)}</td><td>{ESC(b)}</td><td>{ESC(c)}</td></tr>' for a, b, c in dur)
page("", f"""
  <div class="hdbar">FUNDAMENTOS · HIGIENE Y CONSERVACIÓN</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl2 serif">HIGIENE</div>
    <div style="margin-top:3mm">
      <div class="ing"><i>✓</i><div>Lávate las manos y los utensilios</div></div>
      <div class="ing"><i>✓</i><div>Trabaja en superficies limpias</div></div>
      <div class="ing"><i>✓</i><div>Etiqueta cada producto con la fecha</div></div>
    </div>
    <div class="ttl2 serif" style="margin-top:6mm">¿CUÁNTO DURAN?</div>
    <table class="tbl" style="margin-top:3mm">{filas}</table>
    <div class="grow"></div>
    <div class="note">Los premios no deben superar el <b>10 % de la alimentación diaria</b>.
      Ante alergias, consulta al veterinario.</div>
  </div>""")

# ───────────────────────── CATEGORÍAS Y RECETAS ─────────────────────────
for i, c in enumerate(ORDEN):
    nom, sub = CATEGORIAS[c]
    rs = [r for r in R if r["cat"] == c]
    lis = "".join(f'<li><span>{r["n"]:02d}</span>{ESC(r["titulo"])}</li>' for r in rs)
    page("divider", f"""
      <div class="kick" style="color:#3B2B20">CATEGORÍA {c}</div>
      <div class="let serif">{c}</div>
      <div class="nm serif">{ESC(nom)}</div>
      <div class="sb">{len(rs)} recetas · {ESC(sub)}</div>
      <ol>{lis}</ol>""")
    for r in rs:
        page_ficha(r); page_pasos(r)

# ───────────────────────── TU NEGOCIO ─────────────────────────
page("divider", """
  <div class="kick" style="color:#3B2B20">PARTE 6</div>
  <div class="let serif">6</div>
  <div class="nm serif">TU NEGOCIO</div>
  <ol><li><span>1</span>Cómo calcular tu precio</li><li><span>2</span>Empaque que vende</li>
      <li><span>3</span>Tus primeros 10 pedidos</li><li><span>4</span>Qué escribir para vender</li></ol>""")

page("", """
  <div class="hdbar">TU NEGOCIO · CÓMO CALCULAR TU PRECIO</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">La fórmula</div>
    <div class="price" style="margin-top:5mm"><div class="big">(Ingredientes + Empaque) × 3.5 = Tu precio</div>
      <div class="sm">Multiplica por 4 si entregas a domicilio</div></div>
    <div class="lbl" style="margin-top:6mm">EJEMPLO REAL · RECETA 01</div>
    <table class="tbl">
      <tr><td>Ingredientes</td><td>$25 MXN</td></tr>
      <tr><td>Empaque (bolsita + etiqueta)</td><td>$6 MXN</td></tr>
      <tr><td>Costo total</td><td>$31 MXN</td></tr>
      <tr><td>Precio de venta</td><td>$70 MXN</td></tr>
      <tr><td>Tu ganancia</td><td>$39 MXN por bolsita</td></tr>
    </table>
    <div class="grow"></div>
    <div class="note"><b>NUNCA</b> cobres solo los ingredientes. Tu tiempo, el gas del horno
      y el empaque también cuestan.</div>
  </div>""")

page("", """
  <div class="hdbar">TU NEGOCIO · EMPAQUE QUE VENDE</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">El empaque vale tanto como la receta</div>
    <div class="grid2" style="margin-top:6mm">
      <div class="box"><b>🛍️ Bolsita kraft</b>La más barata. Con una etiqueta y un moño ya se ve de tienda.</div>
      <div class="box"><b>🫙 Frasco de vidrio</b>Para regalo. Permite cobrar casi el doble.</div>
      <div class="box"><b>🎁 Caja de cumpleaños</b>Pastel + galletas + paletas. El ticket más alto.</div>
      <div class="box"><b>📦 Mayoreo</b>Bolsas grandes para veterinarias y estéticas.</div>
    </div>
    <div class="lbl" style="margin-top:6mm">TU ETIQUETA SIEMPRE LLEVA</div>
    <table class="tbl">
      <tr><td>Nombre</td><td>Del producto y de tu marca</td></tr>
      <tr><td>Ingredientes</td><td>Lista completa</td></tr>
      <tr><td>Fecha</td><td>De elaboración y de caducidad</td></tr>
      <tr><td>Conservación</td><td>Frasco, refrigerador o congelador</td></tr>
      <tr><td>Contacto</td><td>Tu WhatsApp o Instagram</td></tr>
    </table>
    <div class="grow"></div>
    <div class="note"><b>CONSEJO:</b> una etiqueta impresa en casa cuesta menos de $1 y sube
      tu precio percibido muchísimo más que eso.</div>
  </div>""")

page("", """
  <div class="hdbar">TU NEGOCIO · TUS PRIMEROS 10 PEDIDOS</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">De dónde salen los primeros clientes</div>
    <div style="margin-top:5mm">
      <div class="stp"><i>1</i><div>Tus vecinos con perro. Regala 3 bolsitas de prueba.</div></div>
      <div class="stp"><i>2</i><div>El grupo de WhatsApp de tu colonia o edificio</div></div>
      <div class="stp"><i>3</i><div>La veterinaria del barrio: ofrécele comisión</div></div>
      <div class="stp"><i>4</i><div>La estética canina: ahí esperan los dueños</div></div>
      <div class="stp"><i>5</i><div>Grupos de Facebook de mascotas de tu ciudad</div></div>
      <div class="stp"><i>6</i><div>El parque de perros un sábado por la mañana</div></div>
      <div class="stp"><i>7</i><div>Publica el cumpleaños de TU perro con su pastel</div></div>
      <div class="stp"><i>8</i><div>Pide a cada cliente que te etiquete en una foto</div></div>
    </div>
    <div class="grow"></div>
    <div class="note"><b>LA REGLA:</b> las primeras 3 bolsitas se regalan. La cuarta se cobra.
      Nadie compra comida para su perro sin verla antes.</div>
  </div>""")

page("", """
  <div class="hdbar">TU NEGOCIO · QUÉ ESCRIBIR PARA VENDER</div>
  <div class="pad grow" style="display:flex;flex-direction:column">
    <div class="ttl serif">Mensajes que puedes copiar</div>
    <div class="lbl" style="margin-top:5mm">PARA TU VECINA</div>
    <div class="box">«Hola 🐾 Empecé a hacer galletas caseras para perros, sin azúcar ni
      conservadores. Te dejo una bolsita de regalo para que las pruebe tu lomito. Si le gustan,
      la bolsita de 10 queda en $70.»</div>
    <div class="lbl" style="margin-top:4mm">PARA LA VETERINARIA</div>
    <div class="box">«Hola, hago premios naturales para perros con ingredientes seguros.
      ¿Les interesaría venderlos en el mostrador? Les dejo una muestra y les doy el 30 % de comisión.»</div>
    <div class="lbl" style="margin-top:4mm">PARA TUS REDES</div>
    <div class="box">«El cumpleaños de Toby 🎂🐶 Pastel de zanahoria sin azúcar, 100 % apto para perros.
      ¿Quieres uno para el tuyo? Escríbeme por DM.»</div>
    <div class="grow"></div>
    <div class="note"><b>CONSEJO:</b> siempre pon el precio. Quien pregunta «¿cuánto?»
      y tiene que esperar la respuesta, casi nunca compra.</div>
  </div>""")

page("", """
  <div class="hdbar">PARA CERRAR</div>
  <div class="pad grow" style="display:flex;flex-direction:column;text-align:center;align-items:center">
    <div style="font-size:40pt;margin-top:12mm">🐾</div>
    <div class="ttl serif" style="margin-top:5mm">Ahora te toca a ti</div>
    <div class="lede" style="margin-top:4mm">Tienes 30 recetas, los costos, los precios y el plan.
      Lo único que falta es encender el horno.</div>
    <div class="lede" style="margin-top:3mm">Empieza por la receta 01. Es la más fácil, la más barata
      y la que más se vende.</div>
    <div class="grow"></div>
    <div class="price"><div class="big">Lomito Bakery · Edición 2026</div>
      <div class="sm">Pastelería Canina que Vende</div></div>
    <div class="fnote" style="margin-top:4mm">Las recetas de este libro son premios y no sustituyen
      el alimento diario. Consulta siempre al veterinario ante dudas, alergias o condiciones de salud.</div>
  </div>""")

doc = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Pastelería Canina que Vende</title><style>{CSS}</style></head><body>{"".join(P)}</body></html>'
io.open(OUT_HTML, "w", encoding="utf-8").write(doc)
print(f"HTML generado · {len(P)} páginas")

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
if os.path.exists(CHROME):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    f"--print-to-pdf={OUT_PDF}", "--no-pdf-header-footer",
                    "file://" + os.path.abspath(OUT_HTML)],
                   capture_output=True)
    if os.path.exists(OUT_PDF):
        print(f"PDF generado · {os.path.getsize(OUT_PDF)//1024} KB · {OUT_PDF}")
