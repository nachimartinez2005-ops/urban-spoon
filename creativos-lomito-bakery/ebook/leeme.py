# -*- coding: utf-8 -*-
"""Genera 00-LEEME-PRIMERO.pdf: la hoja de bienvenida del paquete.

Estructura: 1 producto principal + 5 bonos. Los 3 upsells (Pack Pasteles
de Cumpleaños, Kit Vende en Redes, Pack Fechas que Venden) se venden
aparte y NO se nombran acá como si vinieran incluidos.
"""
import generar as G

PRINCIPAL = ("01", "Curso Pastelería Canina · 30 recetas", "PDF · 72 págs",
             "Las 30 recetas paso a paso, en 5 categorías. Cada una con su costo, "
             "su precio de venta, su margen, tamaños, conservación y 4 formas de venderla.")

BONOS = [("02", "Calculadora de precios", "Excel / Google Sheets",
          "Metés tus costos y te dice exactamente qué cobrar. Trae una segunda "
          "hoja con las 30 recetas y sus números."),
         ("03", "Guía de ingredientes seguros y prohibidos", "PDF · 4 págs",
          "Los 12 que sí y los 9 que nunca. Imprimible."),
         ("04", "Plan de negocio desde casa", "PDF · 5 págs",
          "La fórmula de precios, el empaque, de dónde salen tus primeros 10 "
          "pedidos y los mensajes para vender."),
         ("05", "Plantillas de etiquetas", "PDF · 5 págs",
          "Para imprimir, recortar y pegar en tus bolsitas."),
         ("06", "Porciones, sustituciones y soluciones", "PDF · 5 págs",
          "Cuánto darle según su peso, qué usar si falta un ingrediente y cómo "
          "salvar una tanda que salió mal.")]

PASOS = [("1", "Abre el archivo <b>01</b> y ve directo a la Receta 01. Es la más "
               "fácil, la más barata y la que más se vende."),
         ("2", "Imprime el archivo <b>03</b> y pégalo en tu refrigerador."),
         ("3", "Cuando quieras poner precios, abre el <b>02</b> en Excel o Google "
               "Sheets y llena solo las celdas amarillas.")]

def ficha(n, t, f_, d, destacado=False):
    borde = "border:1.4pt solid #B5533C;" if destacado else ""
    return f'''<div style="padding:2.8mm 4mm;border-bottom:1pt solid var(--line);{borde}">
         <div style="display:flex;justify-content:space-between;align-items:baseline">
           <span style="font-size:9pt;font-weight:800"><span style="color:#B5533C">{n}</span> &nbsp;{t}</span>
           <span style="font-size:6.5pt;color:#7A6354;white-space:nowrap">{f_}</span></div>
         <div style="font-size:7.6pt;color:#7A6354;line-height:1.35;margin-top:.8mm">{d}</div>
       </div>'''

p1 = G.pg("", f"""
  <div class="hdbar">EMPEZÁ POR ACÁ</div>
  <div class="pad grow">
    <div class="kick">Lomito Bakery · Edición 2026</div>
    <div class="ttl2 serif" style="margin-top:2.5mm">Pastelería Canina que Vende</div>
    <div class="lede" style="margin-top:2.5mm">
      ¡Gracias por tu compra! Tu paquete son <b>6 archivos</b>: el curso y 5 bonos.
    </div>

    <div class="lbl" style="margin-top:6mm">TUS PRIMEROS 3 PASOS</div>
    {"".join(f'<div class="stp"><i>{n}</i><span>{t}</span></div>' for n, t in PASOS)}

    <div class="lbl" style="margin-top:5.5mm">EL CURSO</div>
    <div class="card">{ficha(*PRINCIPAL, destacado=True)}</div>

    <div class="lbl" style="margin-top:5mm">TUS 5 BONOS</div>
    <div class="card">{"".join(ficha(*b) for b in BONOS[:3])}</div>
  </div>
  <div class="pad fnote" style="padding-top:0">lomitobakery.impultienda.ar</div>""")

p2 = G.pg("", f"""
  <div class="hdbar">TUS 5 BONOS · CONTINUACIÓN</div>
  <div class="pad grow">
    <div class="card">{"".join(ficha(*b) for b in BONOS[3:])}</div>

    <div class="box" style="margin-top:6mm">
      <b>Un consejo para la primera semana</b>
      No intentes las 30 recetas. Elige 3: una galleta, un pastel y un premio
      deshidratado. Con esas tres armas una bolsita, una caja de cumpleaños y
      un premio de entrenamiento, que es todo lo que te van a pedir al principio.
    </div>

    <div class="note" style="margin-top:5mm">
      <b>¿ALGO NO ABRE?</b> Responde el correo con el que recibiste este paquete
      y te lo mandamos por otro medio. No te quedes sin tus archivos.
    </div>
  </div>
  <div class="pad" style="padding-top:0">
    <div class="warn">
      Estas recetas son premios y no sustituyen el alimento diario de tu mascota:
      no deben superar el 10 % de su alimentación. Consulta siempre al veterinario
      ante dudas, alergias o condiciones de salud.
    </div>
    <div class="fnote" style="margin-top:3.5mm">
      Precios sugeridos en pesos mexicanos. Tus ganancias dependen de tus costos,
      tu zona y tus ventas. &nbsp;·&nbsp; lomitobakery.impultienda.ar
    </div>
  </div>""")


OFERTAS = [
    ("🎂", "Pack Pasteles de Cumpleaños", "4.90",
     "5 pasteles de fiesta paso a paso: smash cake, pastel salado de pollo, "
     "pastel de calabaza de dos pisos, pastel con forma de hueso y donas glaseadas. "
     "Con betunes seguros.",
     "Un smash cake se vende entre $350 y $380. Con uno solo lo recuperas 70 veces.",
     "https://lomitobakery.impultienda.ar/checkout?p=3e559482-2689-41d8-a4f0-7f6cc47f88cd"),
    ("📱", "Kit Vende en Redes", "5.90",
     "Qué publicar, cómo escribirlo y cómo fotografiar tus productos para que "
     "se vean de tienda y no caseros.",
     "Para cuando ya tengas tus primeras tandas y quieras que te encuentren.",
     "https://lomitobakery.impultienda.ar/checkout?p=4299c3a2-a25a-42d2-8d5b-87e5f6f9d216"),
    ("📅", "Pack Fechas que Venden", "5.90",
     "Las fechas del año en que más se vende en México y qué preparar para cada una, "
     "con recetas de temporada.",
     "Día de Muertos, Navidad y San Valentín concentran los pedidos más grandes.",
     "https://lomitobakery.impultienda.ar/checkout?p=3e5e4caa-821c-435b-be78-20a60ecd595e"),
]

def tarjeta(ico, nom, precio, desc, gancho, url):
    return f"""<div class="card" style="margin-bottom:4mm">
      <div style="padding:3.4mm 4mm">
        <div style="display:flex;justify-content:space-between;align-items:baseline">
          <span style="font-size:10pt;font-weight:800">{ico} &nbsp;{nom}</span>
          <span style="font-size:11pt;font-weight:800;color:#B5533C">US$ {precio}</span></div>
        <div style="font-size:8pt;color:#7A6354;line-height:1.35;margin-top:1.2mm">{desc}</div>
        <div style="font-size:8pt;line-height:1.35;margin-top:1.8mm"><b>{gancho}</b></div>
        <a href="{url}" style="display:block;margin-top:2.8mm;background:#B5533C;color:#fff;
           text-decoration:none;text-align:center;font-size:8.5pt;font-weight:800;
           padding:2.4mm;border-radius:99px">AGREGARLO A MI PAQUETE &rarr;</a>
      </div>
    </div>"""

p3 = G.pg("", f"""
  <div class="hdbar">CUANDO YA ESTÉS VENDIENDO</div>
  <div class="pad grow">
    <div class="ttl2 serif">Tres cosas que no vienen incluidas</div>
    <div class="lede" style="margin-top:2.5mm;margin-bottom:5mm">
      Con el curso y los 5 bonos ya tienes todo para empezar. Esto es para después,
      cuando los pedidos empiecen a llegar. Toca el botón de la que te sirva.
    </div>
    {"".join(tarjeta(*o) for o in OFERTAS)}
  </div>
  <div class="pad fnote" style="padding-top:0">
    Se suman a tu carpeta al instante. &nbsp;·&nbsp; lomitobakery.impultienda.ar
  </div>""")

G.render([p1, p2, p3], "Empieza por acá · Pastelería Canina que Vende", "00-LEEME-PRIMERO")
