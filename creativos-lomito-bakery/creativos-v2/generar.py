# -*- coding: utf-8 -*-
"""Genera los 4 creativos estáticos v2 (1080x1350) para Meta.

Ángulos elegidos por los datos, no por intuición: el único anuncio que
vendió (15 B) es el de "negación", el que enfrenta la objeción. Tres de
los nueve competidores sostienen ese mismo ángulo. Por eso 1 y 2 atacan
objeciones y 3 y 4 son los de respaldo.

Todos los números salen del propio curso: $25 de costo y $70 de venta en
la receta 01, $350-380 el pastel de cumpleaños, 30 recetas, margen 80 %.
"""
import io, os, subprocess

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page { size: 1080px 1350px; margin: 0 }
*{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{width:1080px;height:1350px}
:root{--cream:#FDF3E3;--terra:#B5533C;--brown:#3B2B20;--gold:#C8821A;
      --mint:#9FD5BA;--muted:#7A6354;--line:#E3D2BC}
body{font-family:'Inter',sans-serif;color:var(--brown);background:var(--cream);
     width:1080px;height:1350px;display:flex;flex-direction:column;
     justify-content:center;padding:88px 76px;position:relative}
.serif{font-family:'Bitstream Charter','DejaVu Serif',serif}
.kick{font-size:28px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;
      color:var(--terra);margin-bottom:34px}
h1{font-size:96px;line-height:1.02;font-weight:800;letter-spacing:-.02em}
h1 em{font-style:normal;color:var(--terra)}
.sub{font-size:40px;line-height:1.3;color:var(--muted);margin-top:34px}
.sub b{color:var(--brown)}
.marca{position:absolute;left:76px;bottom:70px;font-size:27px;font-weight:800;
       letter-spacing:.2em;text-transform:uppercase;color:var(--terra)}
.marca::after{content:'';display:block;width:92px;height:6px;background:var(--mint);
              border-radius:3px;margin-top:16px}
/* tarjeta de números */
.card{background:#fff;border:3px solid var(--line);border-radius:28px;
      padding:38px 44px;margin-top:46px}
.row{display:flex;justify-content:space-between;align-items:baseline;
     padding:17px 0;border-bottom:2px solid var(--line);font-size:36px}
.row:last-child{border-bottom:0}
.row b{font-size:44px;font-weight:800}
.row .ok{color:var(--terra)}
/* contraste grande */
.vs{display:flex;align-items:center;gap:40px;margin-top:52px}
.vs .b{flex:1;background:#fff;border:3px solid var(--line);border-radius:28px;
       padding:34px;text-align:center}
.vs .b span{display:block;font-size:30px;color:var(--muted);margin-bottom:12px}
.vs .b strong{font-size:84px;font-weight:800;line-height:1}
.vs .b.win{background:var(--terra);border-color:var(--terra);color:#fff}
.vs .b.win span{color:#F7D9CF}
.vs .flecha{font-size:56px;color:var(--terra);font-weight:800}
.precio{margin-top:52px;background:var(--brown);color:#fff;border-radius:28px;
        padding:40px;text-align:center}
.precio .ch{font-size:30px;color:#C9B9A8;text-decoration:line-through}
.precio .gr{font-size:104px;font-weight:800;line-height:1.05}
.precio .pe{font-size:32px;color:#FFD89B;font-weight:800;letter-spacing:.1em}
"""

def render(nombre, cuerpo):
    html = (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap' rel='stylesheet'>"
            f"<style>{CSS}</style></head><body>{cuerpo}"
            f"<div class='marca'>Lomito Bakery</div>"
            f"</body></html>")
    h = os.path.join(OUT, f"_{nombre}.html")
    io.open(h, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350",
                    f"--screenshot={os.path.join(OUT, nombre + '.png')}",
                    "file://" + os.path.abspath(h)], capture_output=True)
    os.remove(h)
    p = os.path.join(OUT, nombre + ".png")
    print(f"  ✓ {nombre}.png · {os.path.getsize(p)//1024} KB")

# ── 1 · OBJECIÓN: no sé cocinar ──────────────────────────────
render("A1-no-se-cocinar", """
  <div class="kick">Nunca horneaste nada</div>
  <h1 class="serif">No necesitas<br>saber cocinar.<br><em>Necesitas<br>una receta.</em></h1>
  <div class="sub">30 recetas paso a paso, con el horno que ya tienes.
    <b>Ocho ingredientes de súper</b> y nada más.</div>""")

# ── 2 · OBJECIÓN: no sé cuánto cobrar ────────────────────────
render("A2-cuanto-cobrar", """
  <div class="kick">Lo difícil no es hornear</div>
  <h1 class="serif">Es saber<br><em>cuánto cobrar.</em></h1>
  <div class="sub">Cada receta ya viene con la cuenta hecha:</div>
  <div class="card">
    <div class="row"><span>Te cuesta hacerla</span><b>$25</b></div>
    <div class="row"><span>La vendes a</span><b class="ok">$70</b></div>
    <div class="row"><span>Tu ganancia</span><b class="ok">80 %</b></div>
  </div>""")

# ── 3 · CONTRASTE: el pastel de $350 ─────────────────────────
render("A3-pastel-350", """
  <div class="kick">El pedido que mejor se paga</div>
  <h1 class="serif">Un pastel de<br>cumpleaños<br><em>para perro.</em></h1>
  <div class="vs">
    <div class="b"><span>te cuesta</span><strong>$70</strong></div>
    <div class="flecha">→</div>
    <div class="b win"><span>lo vendes a</span><strong>$350</strong></div>
  </div>
  <div class="sub" style="font-size:34px">Pesos mexicanos. El número sale del propio curso.</div>""")

# ── 4 · PRECIO: filtra al que ya aceptó pagar ────────────────
render("A4-precio-229", """
  <div class="kick">Pastelería canina que vende</div>
  <h1 class="serif">30 recetas con<br>el precio de<br><em>venta incluido.</em></h1>
  <div class="precio">
    <div class="ch">$1,084 MXN</div>
    <div class="gr">$229</div>
    <div class="pe">CURSO + 5 BONOS · ACCESO INMEDIATO</div>
  </div>""")
