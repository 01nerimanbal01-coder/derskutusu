#!/usr/bin/env python3
"""Öğrenme çıktısı yazılıları: araclar/cikti/<dosya>.json → public/yazili/cikti/<dosya>.pdf ve <dosya>-cevapli.pdf.

Her kâğıt tek bir öğrenme çıktısını ölçer: 2 A4 sayfa, 6–8 açık uçlu soru, 40 dakika, 100 puan. Düzen, InDesign'da
hazırlanan ilk 28 kâğıtla (DERSKUTUSU-YAZILI-CIKTI) aynıdır; bu araç aynı kâğıdı HTML'den başsız Chrome ile üretir,
böylece kâğıtlar bulutta da hazırlanabilir.

İçerik JSON'u (sorular MEB ders kitabıyla uyumlu ve özgün; metinlerde basit HTML kullanılabilir: <b>, <i>, <sup>, <br>):
  tablo "7-matematik", sinif 7, ders "MATEMATİK", donem 1, kod "MAT.7.4.4", ifade, konu,
  sorular[]: {puan, duzey (hatırlama|kavrama|uygulama|analiz|değerlendirme), giris, maddeler[] ("a) " öneki kendiliğinden),
              cevap[] (cevaplı kâğıtta kırmızı), vurgu? (girişten sonra kalın yönerge), bosluk? (en az cevap alanı, mm;
              0: cevap görselin içinde, ör. tablo),
              gorsel? {tur: svg|html|prizma|kupler|kareli|sutun|nokta|cizim|tablo|kartlar (alanları aşağıdaki işlevlerde), konum: sag|alt, genislik (mm)}, sayfa? (1|2; hiçbirinde yoksa bölüm ölçülerek seçilir)}
Puanların toplamı 100 olmalıdır. Öğrenci kâğıdındaki karekod cevaplı PDF'in site adresini açar.

Denetim: her sayfa ölçülür; taşan sayfa, öğrencinin yazacağı alanı 18 mm'den kısa kalan soru ya da cevap alanına
sığmayan cevap varsa PDF yazılmaz. Başarılı üretimde veri/yazili-cikti.json güncellenir.

Gerekenler: Chrome ya da Chromium (CHROME ortam değişkeniyle de verilebilir), Python paketleri qrcode ve pypdf.
Çalıştırma: python3 araclar/cikti_yazili_uret.py [--taslak] [dosya …]   (ad verilmezse araclar/cikti/ altındaki tüm kâğıtlar)
"""
import datetime
import glob
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
SITE = ARACLAR.parent
PUBLIC = SITE / 'public'
KAYNAK = ARACLAR / 'cikti'
HEDEF = PUBLIC / 'yazili' / 'cikti'
VERI = PUBLIC / 'veri' / 'yazili-cikti.json'
ADRES = 'https://derskutusu.com/yazili/cikti/'
YIL = '2026-2027'
EN_AZ_BOSLUK_MM = 18
TASLAK = False  # --taslak: denetim hatalarında da PDF yazar (yalnız gözden geçirme için), veriyi güncellemez
BUYUK = str.maketrans('iıçğöşü', 'İIÇĞÖŞÜ')


def tr_buyuk(s):
    return s.translate(BUYUK).upper()


def chrome_yolu():
    adaylar = [os.environ.get('CHROME', ''),
               '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
               *sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'), reverse=True),
               shutil.which('chromium') or '', shutil.which('chromium-browser') or '',
               shutil.which('google-chrome') or '']
    for a in adaylar:
        if a and Path(a).exists():
            return a
    sys.exit('Chrome/Chromium bulunamadı; CHROME ortam değişkeniyle yolunu verin.')


def karekod_svg(metin):
    try:
        import qrcode
        import qrcode.image.svg
    except ImportError:
        sys.exit('Karekod için qrcode paketi gerekli: python3 -m pip install qrcode')
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(metin)
    q.make(fit=True)
    m = q.get_matrix()
    n = len(m)
    yol = ''.join(f'M{x} {y}h1v1h-1z' for y, satir in enumerate(m) for x, v in enumerate(satir) if v)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges">'
            f'<path d="{yol}" fill="#000"/></svg>')


def logo(ad):
    svg = (PUBLIC / ad).read_text(encoding='utf-8')
    svg = re.sub(r'<svg[^>]*?(viewBox="[^"]+")[^>]*>', r'<svg xmlns="http://www.w3.org/2000/svg" \1>', svg, count=1)
    return (svg.replace('class="ly-1"', 'fill="#0b2257"').replace('class="ly-2"', 'fill="#2451d6"')
            .replace('class="ly-3"', 'fill="#5b6479"'))


def puan_cumlesi(sorular):
    gruplar = {}
    for i, s in enumerate(sorular, 1):
        gruplar.setdefault(s['puan'], []).append(i)

    def liste(nolar):
        if len(nolar) == 1:
            return f'{nolar[0]}. soru'
        return ', '.join(map(str, nolar[:-1])) + f' ve {nolar[-1]}. sorular'

    parcalar = [f'{liste(n)} {p} puan' for p, n in sorted(gruplar.items(), key=lambda g: g[1][0])]
    if len(parcalar) == 1 and len(sorular) > 1:
        return f'Her soru {sorular[0]["puan"]} puan değerindedir.'
    return '; '.join(parcalar) + ' değerindedir.'


# ---- Görseller: JSON'da {"tur": ...} olarak verilir; "svg" türü hazır SVG metnidir. ----
EGIK = (0.5, 0.42)  # eğik izdüşüm: derinlik ekseni sağa ve yukarı


def _nokta(x, y, z, s):
    return x * s + y * s * EGIK[0], -z * s - y * s * EGIK[1]


def _cokgen(noktalar, dolgu, cizgi='#222', kalin=1.1):
    return (f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in noktalar)}" fill="{dolgu}" '
            f'stroke="{cizgi}" stroke-width="{kalin}" stroke-linejoin="round"/>')


def _yazi(x, y, metin, boy=11, hiza='middle', kalin=True, renk='#111'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{boy}" text-anchor="{hiza}" fill="{renk}" '
            f'font-weight="{700 if kalin else 400}" font-family="Arial, Liberation Sans, sans-serif">{metin}</text>')


def _svg(icerik, x0, y0, x1, y1):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {x1 - x0:.1f} {y1 - y0:.1f}">'
            f'{icerik}</svg>')


def prizma(g):
    """Dikdörtgenler prizması: a (en), b (derinlik), c (yükseklik) birim; izgara: birim küp çizgileri; etiketler [en, derinlik, yükseklik]."""
    a, b, c = g['a'], g['b'], g['c']
    s = g.get('olcek', 22)
    P = lambda x, y, z: _nokta(x, y, z, s)
    renk = g.get('renk', ['#dfe9f7', '#c4d6ef', '#a9c2e6'])  # ön, üst, yan
    on = [P(0, 0, 0), P(a, 0, 0), P(a, 0, c), P(0, 0, c)]
    ust = [P(0, 0, c), P(a, 0, c), P(a, b, c), P(0, b, c)]
    yan = [P(a, 0, 0), P(a, b, 0), P(a, b, c), P(a, 0, c)]
    ic = _cokgen(on, renk[0]) + _cokgen(ust, renk[1]) + _cokgen(yan, renk[2])
    if g.get('izgara'):
        cz = []
        for i in range(1, a):
            cz += [(P(i, 0, 0), P(i, 0, c)), (P(i, 0, c), P(i, b, c))]
        for k in range(1, c):
            cz += [(P(0, 0, k), P(a, 0, k)), (P(a, 0, k), P(a, b, k))]
        for j in range(1, b):
            cz += [(P(0, j, c), P(a, j, c)), (P(a, j, 0), P(a, j, c))]
        ic += ''.join(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#222" '
                      f'stroke-width=".7"/>' for p, q in cz)
    if g.get('gizli'):
        arka = P(0, b, 0)
        for q in (P(0, 0, 0), P(a, b, 0), P(0, b, c)):
            ic += (f'<line x1="{arka[0]:.1f}" y1="{arka[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="#555" '
                   f'stroke-width=".9" stroke-dasharray="4 3"/>')
    et = g.get('etiketler')
    if et:
        x, y = P(a / 2, 0, 0)
        ic += _yazi(x, y + 15, et[0])
        x, y = P(a, b / 2, 0)
        ic += _yazi(x + 6, y + 10, et[1], hiza='start')
        x, y = P(a, b, c / 2)
        ic += _yazi(x + 6, y + 4, et[2], hiza='start')
    x1 = max(P(a, b, 0)[0], P(a, 0, 0)[0]) + (70 if et else 6)
    return _svg(ic, -6, P(0, b, c)[1] - 6, x1, 6 + (20 if et else 0))


def kupler(g):
    """Birim küp yapısı: yukseklik[satır][sütun]; ilk satır en öndedir."""
    h = g['yukseklik']
    s = g.get('olcek', 20)
    P = lambda x, y, z: _nokta(x, y, z, s)
    ic = ''
    derin = len(h)
    for y in range(derin - 1, -1, -1):
        for x in range(len(h[y])):
            for z in range(h[y][x]):
                ic += (_cokgen([P(x, y, z), P(x + 1, y, z), P(x + 1, y, z + 1), P(x, y, z + 1)], '#f6d38a', kalin=.9)
                       + _cokgen([P(x, y, z + 1), P(x + 1, y, z + 1), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)],
                                 '#fbe6b6', kalin=.9)
                       + _cokgen([P(x + 1, y, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x + 1, y, z + 1)],
                                 '#e2b55a', kalin=.9))
    en = max(len(r) for r in h)
    yuk = max(max(r) for r in h)
    return _svg(ic, -4, P(0, derin, yuk)[1] - 4, P(en, derin, 0)[0] + 4, 4)


def tablo(g, cevapli):
    """HTML tablo; hücre {"b": cevap} öğrencide boş, cevaplıda kırmızı yazılır."""
    def hucre(v):
        if isinstance(v, dict):
            return f'<td class="bos">{v["b"] if cevapli else "&nbsp;"}</td>'
        return f'<td>{v}</td>'
    bas = ''.join(f'<th>{b}</th>' for b in g['basliklar'])
    sat = ''.join('<tr>' + ''.join(hucre(v) for v in r) + '</tr>' for r in g['satirlar'])
    return f'<table class="gt"><tr>{bas}</tr>{sat}</table>'


def kartlar(g):
    """Not kâğıdı ya da konuşma kartları: [{baslik?, satirlar[]}]."""
    ic = ''
    for k in g['kartlar']:
        bas = f'<div class="kb">{k["baslik"]}</div>' if k.get('baslik') else ''
        ic += f'<div class="kart">{bas}' + ''.join(f'<div>{x}</div>' for x in k['satirlar']) + '</div>'
    return f'<div class="kartlar" style="flex-direction:{g.get("yon", "column")}">{ic}</div>'


def kareli(g):
    """Kareli zemin: en × boy birim kare; dikdortgenler [{x, y, en, boy, ad?, renk?}] (birim cinsinden, sol üst köşe)."""
    s = g.get('olcek', 14)
    en, boy = g['en'], g['boy']
    ic = ''.join(f'<line x1="{i * s}" y1="0" x2="{i * s}" y2="{boy * s}" stroke="#b9c2cf" stroke-width=".7"/>'
                 for i in range(en + 1))
    ic += ''.join(f'<line x1="0" y1="{j * s}" x2="{en * s}" y2="{j * s}" stroke="#b9c2cf" stroke-width=".7"/>'
                  for j in range(boy + 1))
    for d in g.get('dikdortgenler', []):
        ic += (f'<rect x="{d["x"] * s}" y="{d["y"] * s}" width="{d["en"] * s}" height="{d["boy"] * s}" '
               f'fill="{d.get("renk", "#c4d6ef")}" fill-opacity=".85" stroke="#1d3d7a" stroke-width="1.6"/>')
        if d.get('ad'):
            ic += _yazi((d['x'] + d['en'] / 2) * s, (d['y'] + d['boy'] / 2) * s + 4.5, d['ad'], 13)
    return _svg(ic, -2, -2, en * s + 2, boy * s + 2)


def sutun(g):
    """Sütun grafiği: kategoriler, degerler, alt? (eksenin başladığı değer), ust, adim, eksen_adi?, baslik?."""
    kat, deg = g['kategoriler'], g['degerler']
    alt, ust, adim = g.get('alt', 0), g['ust'], g['adim']
    W, H, sol, alt_bos, ust_bos = g.get('w', 300), g.get('h', 150), 34, 30, 18
    y = lambda v: ust_bos + (H - ust_bos - alt_bos) * (1 - (v - alt) / (ust - alt))
    ic = ''
    v = alt
    while v <= ust + 1e-9:
        ic += (f'<line x1="{sol}" y1="{y(v):.1f}" x2="{W - 4}" y2="{y(v):.1f}" stroke="#d5dae2" stroke-width=".7"/>'
               + _yazi(sol - 5, y(v) + 3.5, f'{v:g}', 9, 'end', False))
        v += adim
    ic += f'<line x1="{sol}" y1="{ust_bos - 6}" x2="{sol}" y2="{y(alt):.1f}" stroke="#222" stroke-width="1.1"/>'
    ic += f'<line x1="{sol}" y1="{y(alt):.1f}" x2="{W - 4}" y2="{y(alt):.1f}" stroke="#222" stroke-width="1.1"/>'
    aralik = (W - 4 - sol) / len(kat)
    for i, (k, d) in enumerate(zip(kat, deg)):
        x = sol + aralik * i + aralik * .22
        ic += (f'<rect x="{x:.1f}" y="{y(d):.1f}" width="{aralik * .56:.1f}" height="{y(alt) - y(d):.1f}" '
               f'fill="#7aa0dc" stroke="#1d3d7a" stroke-width=".9"/>' + _yazi(x + aralik * .28, y(alt) + 13, k, 9.5, kalin=False))
    if g.get('eksen_adi'):
        ic += _yazi(sol + 2, ust_bos - 9, g['eksen_adi'], 9, 'start', False)
    if g.get('baslik'):
        ic += _yazi(W / 2, H - 2, g['baslik'], 9.5)
    return _svg(ic, 0, 0, W, H)


def nokta(g):
    """Nokta grafiği: min, max, sayilar {değer: adet}, baslik?."""
    a, b, say = g['min'], g['max'], {int(k): v for k, v in g['sayilar'].items()}
    W, adim_x, r = g.get('w', 300), None, 5.2
    adim_x = (W - 30) / (b - a)
    yuk = max(say.values()) * 2 * r + 46
    taban = yuk - 30
    ic = f'<line x1="10" y1="{taban}" x2="{W - 10}" y2="{taban}" stroke="#222" stroke-width="1.1"/>'
    for v in range(a, b + 1):
        x = 15 + (v - a) * adim_x
        ic += (f'<line x1="{x:.1f}" y1="{taban - 3}" x2="{x:.1f}" y2="{taban + 3}" stroke="#222"/>'
               + _yazi(x, taban + 14, v, 9.5, kalin=False))
        for j in range(say.get(v, 0)):
            ic += f'<circle cx="{x:.1f}" cy="{taban - 8 - j * 2.2 * r:.1f}" r="{r}" fill="#2451d6"/>'
    if g.get('baslik'):
        ic += _yazi(W / 2, yuk - 2, g['baslik'], 9.5)
    return _svg(ic, 0, 0, W, yuk)


def cizim(g):
    """Serbest çizim (mm benzeri birim): oge [["dik", x, y, en, boy, dolgu?], ["yazi", x, y, metin, boy?], ["cizgi", x1, y1, x2, y2, kesik?], ["sil", x1, y1, x2, y2]]."""
    ic = ''
    for o in g['oge']:
        t = o[0]
        if t == 'dik':
            ic += (f'<rect x="{o[1]}" y="{o[2]}" width="{o[3]}" height="{o[4]}" fill="{o[5] if len(o) > 5 else "#dfe9f7"}" '
                   f'stroke="#1d3d7a" stroke-width="1.4"/>')
        elif t == 'yazi':
            ic += _yazi(o[1], o[2], o[3], o[4] if len(o) > 4 else 10.5)
        elif t == 'sil':  # kenarda boşluk (ör. kapı)
            ic += f'<line x1="{o[1]}" y1="{o[2]}" x2="{o[3]}" y2="{o[4]}" stroke="#fff" stroke-width="4"/>'
        elif t == 'cizgi':
            kesik = ' stroke-dasharray="4 3"' if len(o) > 5 and o[5] else ''
            ic += f'<line x1="{o[1]}" y1="{o[2]}" x2="{o[3]}" y2="{o[4]}" stroke="#222" stroke-width="1.1"{kesik}/>'
    return _svg(ic, *g['kutu'])


def gorsel_html(g, cevapli):
    tur = g.get('tur', 'svg')
    if tur == 'svg':
        return g['svg']
    if tur == 'tablo':
        return tablo(g, cevapli)
    if tur == 'kartlar':
        return kartlar(g)
    if tur == 'html':
        return g['html']
    return {'prizma': prizma, 'kupler': kupler, 'kareli': kareli, 'sutun': sutun, 'nokta': nokta, 'cizim': cizim}[tur](g)


CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: Arial, "Liberation Sans", Helvetica, sans-serif; color: #111; font-size: 10.2pt; line-height: 1.36;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.sayfa { width: 210mm; height: 297mm; padding: 11mm 12.5mm 7mm; display: flex; flex-direction: column; overflow: hidden;
  page-break-after: always; break-after: page; position: relative; }
.sayfa:last-child { page-break-after: auto; break-after: auto; }
.bas { display: grid; grid-template-columns: 36mm 1fr 32mm; border: 1.2px solid #111; height: 31mm; }
.bas .lg { border-right: 1px solid #111; display: flex; align-items: center; justify-content: center; }
.bas .lg svg { width: 25mm; height: 25mm; }
.bas .bilgi { padding: 4.5mm 4mm 0; font-weight: 700; }
.bas .bilgi .k { font-size: 9pt; } .bas .bilgi .o { font-size: 10.5pt; margin-top: 1.6mm; }
.bas .bilgi .d { font-size: 13.5pt; margin-top: .6mm; } .bas .bilgi .s { font-size: 10pt; }
.bas .puan { border-left: 1px solid #111; display: flex; flex-direction: column; }
.bas .puan div { background: #ececec; border-bottom: 1px solid #111; text-align: center; font-weight: 700; font-size: 10pt; padding: 1.3mm 0; }
.kimlik { display: grid; grid-template-columns: 1fr 45mm 36mm; border: 1px solid #111; margin-top: 2mm; font-weight: 700; font-size: 9.6pt; }
.kimlik div { padding: 2mm 1.6mm; } .kimlik div + div { border-left: 1px solid #111; }
.konu { margin: 2.4mm 0 0; font-size: 10pt; } .konu b { font-weight: 700; }
.dikkat { border: 1px solid #111; margin-top: 2.6mm; padding: 1.8mm 3.5mm 1.8mm; font-size: 8.8pt; line-height: 1.32; }
.dikkat .b { font-weight: 700; margin-bottom: .6mm; }
.dikkat ol { margin: 0; padding-left: 5mm; }
.ust2 { text-align: center; font-weight: 700; font-size: 8.6pt; padding: 0 0 2.5mm; border-bottom: 1px solid #999; margin-bottom: .5mm; }
.sorular { flex: 1 1 auto; display: flex; flex-direction: column; min-height: 0; }
.soru { flex: 1 1 auto; display: flex; flex-direction: column; border-bottom: 1.2px solid #111; padding: 3.2mm 0 1.5mm; min-height: 0; }
.soru.sabit { flex: 0 0 auto; } .soru.sabit .bosluk { flex: 0 0 auto; min-height: 9mm; }
.soru:last-child { border-bottom: 0; }
.soru .baslik { display: flex; align-items: baseline; font-weight: 700; font-size: 11pt; }
.soru .baslik .etiket { color: #d0242b; font-weight: 400; font-size: 7.4pt; margin-left: 4mm; }
.soru .baslik .p { margin-left: auto; font-size: 10pt; }
.govde { display: flex; gap: 6mm; margin: 1.2mm 0 0 4mm; }
.govde .metin { flex: 1 1 auto; min-width: 0; }
.govde .gorsel { flex: 0 0 auto; display: flex; align-items: flex-start; justify-content: center; }
.gorsel svg { display: block; width: 100%; height: auto; }
.altgorsel { margin: 2mm 0 0 4mm; display: flex; justify-content: center; }
.giris p { margin: 0 0 1mm; }
.vurgu { font-weight: 700; margin: 1mm 0; }
.maddeler { margin: .6mm 0 0; padding: 0; list-style: none; }
.maddeler li { padding-left: 5.2mm; text-indent: -5.2mm; margin: .5mm 0; }
.bosluk { flex: 1 1 auto; position: relative; min-height: 0; margin-left: 4mm; }
.cevap { position: absolute; left: 0; right: 0; top: 1mm; color: #d0242b; font-weight: 700; font-size: 8.9pt; line-height: 1.34; }
.cevap div { margin: .3mm 0; }
.son { display: grid; grid-template-columns: 1fr 26mm; gap: 4mm; align-items: end; margin-top: 2mm; }
table.pt { width: 100%; border-collapse: collapse; font-size: 10pt; text-align: center; }
table.pt td, table.pt th { border: 1px solid #111; padding: 2.4mm 1mm; }
table.pt th { background: #ececec; font-weight: 700; }
table.pt td.b { background: #ececec; font-weight: 700; }
table.pt td.k { color: #d0242b; font-weight: 700; font-size: 9pt; }
.qr { text-align: center; font-size: 6.4pt; color: #444; line-height: 1.2; }
.qr svg { width: 21mm; height: 21mm; display: block; margin: 0 auto 1mm; }
.imza { display: flex; align-items: baseline; margin-top: 3mm; font-size: 10pt; }
.imza i { font-weight: 700; font-size: 11.5pt; } .imza span { margin-left: auto; } .imza span + span { margin-left: 4mm; }
.gorsel > svg, .altgorsel svg { max-height: 52mm; }
table.gt { border-collapse: collapse; width: 100%; font-size: 9.6pt; text-align: center; }
table.gt th, table.gt td { border: 1px solid #111; padding: 1.3mm 1.2mm; }
table.gt th { background: #ececec; }
table.gt td.bos { color: #d0242b; font-weight: 700; min-width: 14mm; }
.kartlar { display: flex; gap: 2.5mm; }
.kart { border: 1px solid #888; border-radius: 2mm; background: #fbfbf4; padding: 2mm 3mm; font-size: 9.2pt; line-height: 1.35; flex: 1; }
.kart .kb { font-weight: 700; margin-bottom: .8mm; }
.serit { position: absolute; top: 2.6mm; left: 12.5mm; right: 12.5mm; display: flex; align-items: center; gap: 3mm;
  font-size: 7.6pt; color: #d0242b; white-space: nowrap; overflow: hidden; }
.serit span { overflow: hidden; text-overflow: ellipsis; min-width: 0; }
.serit b.e { background: #d0242b; color: #fff; border-radius: 1.6mm; padding: .8mm 3mm; font-size: 9.5pt; letter-spacing: .12em; }
.alt { border-top: 1px solid #111; margin-top: 3mm; padding-top: 2.6mm; display: flex; align-items: center; font-size: 7.6pt; color: #555; }
.alt svg { height: 7.2mm; width: auto; }
.alt .orta { flex: 1; text-align: center; } .alt .no { font-weight: 700; color: #111; font-size: 9.5pt; }
"""


def soru_html(s, no, kod, cevapli):
    etiket = f'<span class="etiket">{kod} · {html.escape(s["duzey"])}</span>' if cevapli else ''
    giris = ''.join(f'<p>{p}</p>' for p in ([s['giris']] if isinstance(s['giris'], str) else s['giris']))
    vurgu = f'<div class="vurgu">{s["vurgu"]}</div>' if s.get('vurgu') else ''
    harfler = 'abcçdefgğh'
    maddeler = ''.join(f'<li>{harfler[i]})&nbsp; {m}</li>' for i, m in enumerate(s.get('maddeler', [])))
    metin = f'<div class="giris">{giris}</div>{vurgu}' + (f'<ul class="maddeler">{maddeler}</ul>' if maddeler else '')
    g = s.get('gorsel')
    if g and g.get('konum', 'sag') == 'sag':
        govde = (f'<div class="govde"><div class="metin">{metin}</div>'
                 f'<div class="gorsel" style="width:{g.get("genislik", 60)}mm">{gorsel_html(g, cevapli)}</div></div>')
    elif g:  # görsel girişin altında, tam genişlikte; yönerge ve maddeler görselin altında
        govde = (f'<div class="govde"><div class="metin"><div class="giris">{giris}</div></div></div>'
                 f'<div class="altgorsel"><div style="width:{g.get("genislik", 120)}mm">{gorsel_html(g, cevapli)}</div></div>'
                 f'<div class="govde"><div class="metin">{vurgu}'
                 + (f'<ul class="maddeler">{maddeler}</ul>' if maddeler else '') + '</div></div>')
    else:
        govde = f'<div class="govde"><div class="metin">{metin}</div></div>'
    cevap = ''
    if cevapli:
        satirlar = s['cevap'] if isinstance(s['cevap'], list) else [s['cevap']]
        cevap = '<div class="cevap">' + ''.join(
            f'<div>{"Cevap: " if i == 0 else ""}{c}</div>' for i, c in enumerate(satirlar)) + '</div>'
    sabit = ' sabit' if s.get('bosluk', EN_AZ_BOSLUK_MM) == 0 else ''
    return (f'<section class="soru{sabit}" data-no="{no}" data-enaz="{s.get("bosluk", EN_AZ_BOSLUK_MM)}"><div class="baslik">{no}. SORU{etiket}'
            f'<span class="p">({s["puan"]} puan)</span></div>{govde}<div class="bosluk">{cevap}</div></section>')


def kagit_html(o, cevapli, ilk_adet=None):
    sorular = o['sorular']
    n = len(sorular)
    k = ilk_adet if ilk_adet is not None else (n + 1) // 2
    ilk = [i for i, s in enumerate(sorular) if s.get('sayfa', 1 if i < k else 2) == 1]
    ders = f'{o["sinif"]}. SINIF {tr_buyuk(o["ders"])} DERSİ'
    donem = f'{o["donem"]}. DÖNEM ÖĞRENME ÇIKTISI DEĞERLENDİRME SINAVI'
    alt = (lambda no: f'<div class="alt">{logo("logo-yazi.svg")}<div class="orta">Bu sınav kâğıdı tek bir öğrenme '
           f'çıktısını ölçmek üzere MEB ders kitabına göre hazırlanmıştır &nbsp;·&nbsp; derskutusu.com</div>'
           f'<div class="no">Sayfa {no} / 2</div></div>')
    s1 = ''.join(soru_html(sorular[i], i + 1, o['kod'], cevapli) for i in ilk)
    s2 = ''.join(soru_html(s, i + 1, o['kod'], cevapli) for i, s in enumerate(sorular) if i not in ilk)
    tablo = ('<table class="pt"><tr><th>SORU</th>' + ''.join(f'<th>{i}</th>' for i in range(1, n + 1))
             + '<th>TOPLAM</th></tr><tr><td class="b">PUAN</td>'
             + ''.join(f'<td class="k">{s["puan"]}</td>' for s in sorular) + '<td class="k b">100</td></tr></table>')
    serit = (f'<div class="serit"><b class="e">CEVAP ANAHTARI</b><span><b>Öğrenme çıktısı {o["kod"]}:</b> '
             f'{html.escape(o["ifade"])}</span></div>' if cevapli else '')
    karekod = karekod_svg(f'{ADRES}{o["dosya"]}-cevapli.pdf')
    baslik = f'{o["sinif"]}. Sınıf {o["ders_ad"]} · {o["kod"]} Öğrenme Çıktısı Yazılısı' + (' · Cevap Anahtarı' if cevapli else '')
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{html.escape(baslik)}</title>
<style>{CSS}</style></head><body>
<div class="sayfa">{serit}
  <div class="bas"><div class="lg">{logo('logo.svg')}</div>
    <div class="bilgi"><div class="k">{YIL} EĞİTİM-ÖĞRETİM YILI</div><div class="o">…………………………………… ORTAOKULU</div>
      <div class="d">{ders}</div><div class="s">{donem}</div></div>
    <div class="puan"><div>PUAN</div></div></div>
  <div class="kimlik"><div>Adı Soyadı:</div><div>Sınıfı / No:</div><div>Tarih:</div></div>
  <div class="konu"><b>Konu:</b> {html.escape(o['konu'])}</div>
  <div class="dikkat"><div class="b">ÖĞRENCİLERİN DİKKATİNE</div><ol>
    <li>Bu sınav kâğıdında <b>{n} soru</b> bulunmaktadır ve sınav süresi <b>40 dakikadır.</b> Cevaplarınızı her sorunun altında
      bırakılan boşluğa, okunaklı bir şekilde yazınız. İşlem gerektiren sorularda işlemlerinizi gösteriniz.</li>
    <li>Sınav 100 (yüz) tam puan üzerinden değerlendirilecektir. {puan_cumlesi(sorular)}</li></ol></div>
  <div class="sorular">{s1}</div>
  {alt(1)}
</div>
<div class="sayfa">
  <div class="ust2">{ders} &nbsp;·&nbsp; {donem} &nbsp;·&nbsp; {YIL}</div>
  <div class="sorular">{s2}</div>
  <div class="son"><div>{tablo}<div class="imza"><i>Başarılar dilerim.</i><span>Ders Öğretmeni: ………………………………</span>
    <span>İmza: …………</span></div></div><div class="qr">{karekod}Cevap anahtarı<br>için okutunuz</div></div>
  {alt(2)}
</div>
<script>
(() => {{
  const mm = 96 / 25.4, sonuc = [];
  document.querySelectorAll('.sayfa').forEach((p, i) => {{
    if (p.scrollHeight > p.clientHeight + 1) sonuc.push({{sayfa: i + 1, hata: 'taşma'}});
  }});
  document.querySelectorAll('.soru').forEach((s) => {{
    const b = s.querySelector('.bosluk'), c = b.querySelector('.cevap');
    sonuc.push({{soru: +s.dataset.no, enaz: +s.dataset.enaz, bosluk: +(b.clientHeight / mm).toFixed(1),
      cevap: c ? +((c.offsetHeight + 1 * mm) / mm).toFixed(1) : 0}});
  }});
  const pre = document.createElement('pre'); pre.id = 'olcum'; pre.style.display = 'none';
  pre.textContent = JSON.stringify(sonuc); document.body.appendChild(pre);
}})();
</script></body></html>"""


def chrome(args, timeout=120):
    return subprocess.run([chrome_yolu(), '--headless=new', '--no-sandbox', '--disable-gpu', '--no-first-run',
                           '--no-default-browser-check', '--disable-background-networking', '--hide-scrollbars',
                           '--run-all-compositor-stages-before-draw', '--virtual-time-budget=3000', *args],
                          capture_output=True, text=True, timeout=timeout)


def denetle(yol):
    r = chrome(['--window-size=794,1123', '--dump-dom', yol.as_uri()])
    m = re.search(r'<pre id="olcum"[^>]*>(\[.*?\])</pre>', r.stdout, re.S)
    if not m:
        raise RuntimeError('Ölçüm alınamadı: ' + r.stderr[-400:])
    sonuc = json.loads(html.unescape(m.group(1)))
    hatalar = [f'{x["sayfa"]}. sayfa taşıyor' for x in sonuc if x.get('hata')]
    for x in sonuc:
        if 'soru' not in x:
            continue
        if x['bosluk'] < x['enaz']:
            hatalar.append(f'{x["soru"]}. soruda cevap alanı {x["bosluk"]} mm (en az {x["enaz"]})')
        if x['cevap'] > x['bosluk']:
            hatalar.append(f'{x["soru"]}. sorunun cevabı alana sığmıyor ({x["cevap"]} > {x["bosluk"]} mm)')
    return sonuc, hatalar


def ust_veri(pdf, o, cevapli):
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        print('  (pypdf yok; PDF üst verisi Chrome varsayılanıyla kaldı)')
        return
    r = PdfReader(pdf)
    if len(r.pages) != 2:
        raise RuntimeError(f'{pdf.name}: {len(r.pages)} sayfa (2 olmalı)')
    w = PdfWriter(clone_from=r)
    w.add_metadata({'/Title': f'{o["sinif"]}. Sınıf {o["ders_ad"]} · {o["kod"]} Öğrenme Çıktısı Yazılısı'
                    + (' · Cevap Anahtarı' if cevapli else ''),
                    '/Subject': 'Öğrenme çıktısı yazılı kâğıdı · derskutusu.com',
                    '/Keywords': 'öğrenme çıktısı, yazılı, MEB, Ders Kutusu',
                    '/Author': 'Ders Kutusu', '/Creator': 'Ders Kutusu', '/Producer': 'Ders Kutusu'})
    with open(pdf, 'wb') as f:
        w.write(f)


def uret(ad):
    o = json.loads((KAYNAK / f'{ad}.json').read_text(encoding='utf-8'))
    o['dosya'] = ad
    o.setdefault('ders_ad', o['ders'][:1] + o['ders'][1:].lower())
    toplam = sum(s['puan'] for s in o['sorular'])
    if toplam != 100:
        raise RuntimeError(f'{ad}: puanların toplamı {toplam}')
    if not 6 <= len(o['sorular']) <= 8:
        raise RuntimeError(f'{ad}: {len(o["sorular"])} soru (6–8 olmalı)')
    HEDEF.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as gecici:
        ilk_adet = None
        if not any('sayfa' in s for s in o['sorular']):
            # Sayfa bölümü verilmemişse 1. sayfadaki soru sayısı, en sıkışık sorunun cevap alanını en geniş bırakacak
            # biçimde ölçülerek seçilir (cevaplı kâğıt da aynı bölümü kullanır).
            yol = Path(gecici) / 'olcum.html'
            en_iyi = None
            for k in range(1, len(o['sorular'])):
                yol.write_text(kagit_html(o, True, k), encoding='utf-8')
                olcum, hatalar = denetle(yol)
                pay = min(x['bosluk'] - max(x['enaz'], x['cevap']) for x in olcum if 'soru' in x)
                if any('taşıyor' in h for h in hatalar):
                    pay -= 1000
                if en_iyi is None or pay > en_iyi[0]:
                    en_iyi = (pay, k)
            ilk_adet = en_iyi[1]
        for cevapli in (False, True):
            yol = Path(gecici) / f'{ad}{"-cevapli" if cevapli else ""}.html'
            yol.write_text(kagit_html(o, cevapli, ilk_adet), encoding='utf-8')
            _, hatalar = denetle(yol)
            if hatalar and not TASLAK:
                raise RuntimeError(f'{yol.stem}: ' + '; '.join(hatalar))
            for h in hatalar:
                print('  UYARI (taslak):', h)
            pdf = HEDEF / f'{yol.stem}.pdf'
            r = chrome(['--no-pdf-header-footer', '--print-to-pdf-no-header', f'--print-to-pdf={pdf}', yol.as_uri()])
            if r.returncode != 0 or not pdf.exists():
                raise RuntimeError(f'{pdf.name} yazılamadı: {r.stderr[-400:]}')
            ust_veri(pdf, o, cevapli)
            print(f'  {pdf.relative_to(SITE)}')
    return {'kod': o['kod'], 'ifade': o['ifade'], 'konu': o['konu'], 'soru': len(o['sorular']), 'dosya': ad}, o['tablo']


def veri_guncelle(kayitlar):
    v = json.loads(VERI.read_text(encoding='utf-8'))
    for kayit, tablo in kayitlar:
        liste = v['tablolar'].setdefault(tablo, [])
        for i, k in enumerate(liste):
            if k['kod'] == kayit['kod']:
                liste[i] = kayit
                break
        else:
            liste.append(kayit)
    v['guncelleme'] = datetime.date.today().isoformat()
    VERI.write_text(json.dumps(v, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def main():
    global TASLAK
    TASLAK = '--taslak' in sys.argv
    adlar = [a for a in sys.argv[1:] if a != '--taslak'] or sorted(p.stem for p in KAYNAK.glob('*.json'))
    kayitlar, hatali = [], []
    for ad in adlar:
        print(ad)
        try:
            kayitlar.append(uret(ad))
        except (RuntimeError, subprocess.TimeoutExpired) as h:
            print('  HATA:', h)
            hatali.append(ad)
    if kayitlar and not TASLAK:
        veri_guncelle(kayitlar)
    if hatali:
        sys.exit(f'{len(hatali)} kâğıt üretilemedi: {", ".join(hatali)}')


if __name__ == '__main__':
    main()
