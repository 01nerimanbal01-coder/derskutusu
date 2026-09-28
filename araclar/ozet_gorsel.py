#!/usr/bin/env python3
"""Konu özetlerinin SVG görsellerini üretir ve ilgili özet JSON'una yazar.

Renkler stil.css'teki sınıflarla verilir (açık/koyu temaya uyar): g-mf/g-ma/g-ms mavi, g-tf/g-ta/g-ts turuncu,
g-yf/g-ya/g-ys yeşil, g-of/g-oa/g-os mor, g-c çizgi, g-y metin, g-s soluk metin, g-b beyaz.
Kurallar: çizgiler yazıya ve dairelere değmez; her görselde renk anlamlıdır (ör. asal = turuncu); yazılar kitap puntosuna yakın.
Çalıştırma: LC_ALL=en_US.UTF-8 python3 araclar/ozet_gorsel.py && python3 araclar/ozet_uret.py
"""
import json
import math
from pathlib import Path

OZET = Path(__file__).resolve().parent / 'ozetler'


def svg(w, h, ic, etiket):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{etiket}">{ic}</svg>'


def ok_isareti(kimlik, sinif):
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" class="{sinif}"/></marker>')


def dugum(x, y, metin, tur, r=22):
    """tur: kok | bilesik | asal"""
    if tur == 'kok':
        return (f'<rect x="{x - 34}" y="{y - 21}" width="68" height="42" rx="21" class="g-mf"/>'
                f'<text x="{x}" y="{y + 7}" text-anchor="middle" font-size="20" font-weight="800" class="g-b">{metin}</text>')
    if tur == 'asal':
        return (f'<circle cx="{x}" cy="{y}" r="{r}" class="g-tf"/>'
                f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="18" font-weight="800" class="g-b">{metin}</text>')
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="g-ma"/><circle cx="{x}" cy="{y}" r="{r}" class="g-ms" stroke-width="2"/>'
            f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="18" font-weight="700" class="g-mf">{metin}</text>')


def dal(x1, y1, r1, x2, y2, r2, bosluk=5):
    # iki düğümü, kenarlarına değmeden birleştir
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    a = (x1 + ux * (r1 + bosluk), y1 + uy * (r1 + bosluk))
    b = (x2 - ux * (r2 + bosluk), y2 - uy * (r2 + bosluk))
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'


def carpan_agaci_72():
    D = {'72': (180, 34, 'kok', 24), '8': (110, 108, 'bilesik', 22), '9': (250, 108, 'bilesik', 22),
         '2a': (66, 182, 'asal', 20), '4': (150, 182, 'bilesik', 22), '3a': (222, 182, 'asal', 20), '3b': (280, 182, 'asal', 20),
         '2b': (122, 252, 'asal', 20), '2c': (178, 252, 'asal', 20)}
    kenar = [('72', '8'), ('72', '9'), ('8', '2a'), ('8', '4'), ('4', '2b'), ('4', '2c'), ('9', '3a'), ('9', '3b')]
    ic = ''.join(dal(D[a][0], D[a][1], D[a][3], D[b][0], D[b][1], D[b][3]) for a, b in kenar)
    ic += ''.join(dugum(x, y, k.rstrip('abc'), t, r) for k, (x, y, t, r) in D.items())
    ic += ('<text x="180" y="306" text-anchor="middle" font-size="19" font-weight="700" class="g-y">72 = '
           '<tspan class="g-tf">2</tspan><tspan dy="-8" font-size="13" class="g-tf">3</tspan><tspan dy="8"> · </tspan>'
           '<tspan class="g-tf">3</tspan><tspan dy="-8" font-size="13" class="g-tf">2</tspan></text>'
           '<circle cx="104" cy="332" r="7" class="g-tf"/><text x="116" y="337" font-size="13" class="g-s">asal çarpan</text>'
           '<circle cx="214" cy="332" r="7" class="g-ma"/><circle cx="214" cy="332" r="7" class="g-ms" stroke-width="1.5"/><text x="226" y="337" font-size="13" class="g-s">asal değil</text>')
    return svg(360, 346, ic, '72 için çarpan ağacı: 72 = 8 · 9, 8 = 2 · 4, 4 = 2 · 2, 9 = 3 · 3; sonuç 72 = 2 üssü 3 çarpı 3 üssü 2')


def noktalar():
    ic = ''
    for x, y, h, s in [(90, 46, 'A', 'g-mf'), (230, 58, 'B', 'g-tf')]:
        ic += (f'<circle cx="{x}" cy="{y}" r="11" class="{s.replace("f", "a")}"/><circle cx="{x}" cy="{y}" r="5" class="{s}"/>'
               f'<text x="{x}" y="{y - 20}" text-anchor="middle" font-size="18" font-weight="700" class="{s}">{h}</text>')
    return svg(320, 80, ic, 'A ve B noktaları')


def dogru_isin_parca():
    ic = '<defs>' + ok_isareti('okM', 'g-mf') + ok_isareti('okY', 'g-yf') + '</defs>'
    satirlar = [(40, 'doğru', 'g-mf', 'g-ms', 'g-ma', 'okM', True, True), (112, 'ışın', 'g-yf', 'g-ys', 'g-ya', 'okY', False, True),
                (184, 'doğru parçası', 'g-tf', 'g-ts', 'g-ta', None, False, False)]
    for y, ad, f, st, a, ok, sol, sag in satirlar:
        ic += f'<rect x="10" y="{y - 14}" width="104" height="28" rx="14" class="{a}"/><text x="62" y="{y + 5}" text-anchor="middle" font-size="13" font-weight="700" class="{f}">{ad}</text>'
        x1, x2 = (136 if sol else 170), (410 if sag else 330)
        m = f' marker-end="url(#{ok})"' if sag else ''
        m += f' marker-start="url(#{ok})"' if sol else ''
        ic += f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="{st}" stroke-width="3" stroke-linecap="round"{m}/>'
        for x, h in [(170, 'A'), (330, 'B')]:
            ic += f'<circle cx="{x}" cy="{y}" r="5" class="{f}"/><text x="{x}" y="{y - 12}" text-anchor="middle" font-size="15" font-weight="700" class="g-y">{h}</text>'
    return svg(420, 206, ic, 'Doğru iki yönde, ışın A noktasından başlayıp tek yönde uzanır; doğru parçası A ile B arasında kalır')


def aci():
    ic = '<defs>' + ok_isareti('okA', 'g-mf') + '</defs>'
    ic += '<path d="M60 150 L130 150 A70 70 0 0 0 113.6 104.9 Z" class="g-ta"/>'
    ic += '<path d="M130 150 A70 70 0 0 0 113.6 104.9" class="g-ts" stroke-width="2.5"/>'
    ic += '<line x1="60" y1="150" x2="290" y2="150" class="g-ms" stroke-width="3" stroke-linecap="round" marker-end="url(#okA)"/>'
    ic += '<line x1="60" y1="150" x2="205" y2="28" class="g-ms" stroke-width="3" stroke-linecap="round" marker-end="url(#okA)"/>'
    ic += '<circle cx="60" cy="150" r="6" class="g-tf"/>'
    ic += '<circle cx="174" cy="54" r="5" class="g-mf"/><circle cx="240" cy="150" r="5" class="g-mf"/>'
    ic += '<text x="44" y="172" font-size="17" font-weight="800" class="g-tf">B</text><text x="152" y="50" font-size="17" font-weight="700" class="g-y">A</text><text x="234" y="176" font-size="17" font-weight="700" class="g-y">C</text>'
    ic += '<text x="140" y="126" font-size="14" font-weight="700" class="g-tf">ABC</text><path d="M140 112 L151.5 106 L163 112" class="g-ts" stroke-width="1.6"/>'
    ic += '<text x="300" y="186" text-anchor="end" font-size="12.5" class="g-s">köşe: B · kollar: [BA ve [BC</text>'
    return svg(320, 196, ic, 'Köşesi B, kolları BA ve BC ışınları olan ABC açısı')


def cember():
    ic = '<circle cx="130" cy="90" r="70" class="g-ma"/><circle cx="130" cy="90" r="70" class="g-ms" stroke-width="3"/>'
    ic += '<line x1="130" y1="90" x2="200" y2="90" class="g-ts" stroke-width="3" stroke-linecap="round"/>'
    ic += '<circle cx="130" cy="90" r="5.5" class="g-tf"/><circle cx="200" cy="90" r="4.5" class="g-mf"/>'
    ic += '<text x="116" y="84" font-size="17" font-weight="800" class="g-tf">O</text><text x="160" y="80" font-size="15" font-weight="700" class="g-tf">r</text>'
    ic += '<text x="228" y="70" font-size="13" class="g-s">O: merkez</text><text x="228" y="92" font-size="13" class="g-s">r: yarıçap</text><text x="228" y="114" font-size="13" class="g-s">mavi çizgi: çember</text>'
    return svg(340, 180, ic, 'Merkezi O, yarıçapı r olan çember')


def dikme():
    ic = '<line x1="30" y1="140" x2="290" y2="140" class="g-ms" stroke-width="3" stroke-linecap="round"/>'
    ic += '<line x1="160" y1="140" x2="160" y2="24" class="g-ts" stroke-width="3" stroke-linecap="round"/>'
    ic += '<rect x="160" y="122" width="18" height="18" class="g-ta"/><path d="M160 122 H178 V140" class="g-ts" stroke-width="2"/>'
    ic += '<circle cx="160" cy="140" r="5.5" class="g-tf"/>'
    ic += '<text x="166" y="162" font-size="16" font-weight="800" class="g-tf">P</text><text x="276" y="132" font-size="16" font-weight="700" class="g-mf">d</text>'
    ic += '<text x="186" y="118" font-size="13" class="g-s">90 derece</text>'
    return svg(320, 170, ic, 'd doğrusuna P noktasından çizilen dikme; dik açı 90 derece')


def ornek_sekiller():
    ic = '<defs>' + ok_isareti('okO', 'g-of') + '</defs>'
    for y, no, sol, sag, uc2 in [(28, 'I.', True, True, False), (78, 'II.', False, True, False), (128, 'III.', False, False, True)]:
        ic += f'<rect x="8" y="{y - 15}" width="40" height="30" rx="9" class="g-oa"/><text x="28" y="{y + 5}" text-anchor="middle" font-size="14" font-weight="800" class="g-of">{no}</text>'
        x1, x2 = (74 if sol else 100), (330 if sag else 260)
        m = (' marker-start="url(#okO)"' if sol else '') + (' marker-end="url(#okO)"' if sag else '')
        ic += f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="g-os" stroke-width="3" stroke-linecap="round"{m}/>'
        if not sol:
            ic += f'<circle cx="100" cy="{y}" r="5" class="g-of"/>'
        if uc2:
            ic += f'<circle cx="260" cy="{y}" r="5" class="g-of"/>'
    return svg(340, 146, ic, 'Üç şekil: I iki yönde oklu, II bir ucunda nokta öbür ucunda ok, III iki ucunda nokta')


def yaz(dosya, degisim):
    p = OZET / dosya
    o = json.loads(p.read_text(encoding='utf-8'))
    degisim(o)
    p.write_text(json.dumps(o, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def mat5(o):
    g = {'Nokta': noktalar(), 'Doğru, ışın ve doğru parçası': dogru_isin_parca(), 'Açı': aci(), 'Çember': cember(), 'Dikme': dikme()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
    for x in o['ornekler']:
        if x.get('gorsel'):
            x['gorsel'] = ornek_sekiller()


def mat8(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Asal çarpanlara ayırma':
            b['gorsel'] = carpan_agaci_72()


def dikdortgen_modeli_12():
    """Alanı 12 birimkare olan dikdörtgenler: 1 × 12, 2 × 6, 3 × 4 (kareli)."""
    birim, ic, y = 16, '', 14
    renk = [('g-ma', 'g-ms', 'g-mf'), ('g-ya', 'g-ys', 'g-yf'), ('g-ta', 'g-ts', 'g-tf')]
    for (en, boy), (a, st, f) in zip([(12, 1), (6, 2), (4, 3)], renk):
        x0 = 20
        for i in range(boy):
            for j in range(en):
                ic += f'<rect x="{x0 + j * birim + 1}" y="{y + i * birim + 1}" width="{birim - 2}" height="{birim - 2}" rx="3" class="{a}"/>'
        ic += f'<rect x="{x0}" y="{y}" width="{en * birim}" height="{boy * birim}" rx="4" class="{st}" stroke-width="2.2"/>'
        ic += f'<text x="{x0 + en * birim + 16}" y="{y + boy * birim / 2 + 6}" font-size="16" font-weight="800" class="{f}">{en} · {boy} = 12</text>'
        y += boy * birim + 22
    ic += '<text x="20" y="' + str(y + 8) + '" font-size="13.5" class="g-s">Kenar uzunlukları 12’nin çarpanlarıdır: 1, 2, 3, 4, 6, 12</text>'
    return svg(330, y + 18, ic, 'Alanı 12 birimkare olan üç dikdörtgen: 12’ye 1, 6’ya 2, 4’e 3; kenarlar 12’nin çarpanları')


def kat_sayi_dogrusu_3():
    """Sayı doğrusunda 3'er atlama: 3'ün katları."""
    x0, adim, y = 24, 22, 70
    ic = '<defs>' + ok_isareti('okS', 'g-mf') + '</defs>'
    ic += f'<line x1="{x0 - 6}" y1="{y}" x2="{x0 + 13 * adim + 14}" y2="{y}" class="g-ms" stroke-width="2.5" marker-end="url(#okS)"/>'
    for n in range(0, 14):
        x = x0 + n * adim
        kat = n % 3 == 0 and n > 0
        ic += f'<line x1="{x}" y1="{y - 6}" x2="{x}" y2="{y + 6}" class="g-c" stroke-width="2"/>'
        ic += f'<text x="{x}" y="{y + 24}" text-anchor="middle" font-size="{14 if kat else 12}" font-weight="{800 if kat else 400}" class="{"g-tf" if kat else "g-s"}">{n}</text>'
        if kat:
            ic += f'<circle cx="{x}" cy="{y}" r="6" class="g-tf"/>'
            ic += f'<path d="M{x - 3 * adim + 4} {y - 8} Q{x - 1.5 * adim} {y - 46} {x - 4} {y - 8}" class="g-ts" stroke-width="2.2"/>'
            ic += f'<text x="{x - 1.5 * adim}" y="{y - 32}" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">+3</text>'
    ic += f'<text x="{x0}" y="{y + 50}" font-size="13.5" class="g-s">3’ün katları: 3, 6, 9, 12, … (sayı doğrusunda 3’er atlama; sonu yok)</text>'
    return svg(350, y + 60, ic, 'Sayı doğrusunda 0’dan başlayarak 3’er atlama: 3, 6, 9, 12; bunlar 3’ün katlarıdır')


def mat6(o):
    g = {'Çarpan: bir sayıyı oluşturan çarpımlar': dikdortgen_modeli_12(), 'Kat: bir sayının tekrarlanan toplamı': kat_sayi_dogrusu_3()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]


# ---------- 7. sınıf Matematik 1. hafta: tam sayılar ve rasyonel sayılar ----------
EKSI = '−'


def isaretli(n):
    return f'{EKSI}{-n}' if n < 0 else str(n)


def kesir_svg(x, y, pay, payda, sinif='g-y', boy=14, isaret=''):
    """Pay üstte, payda altta; çizgi yazı rengiyle. (x, y) kesir çizgisinin ortası."""
    g = max(len(pay), len(payda)) * boy * 0.62 + 6
    ic = ''
    if isaret:
        ic += f'<text x="{x - g / 2 - 3:.1f}" y="{y + boy * 0.35:.1f}" text-anchor="end" font-size="{boy}" font-weight="700" class="{sinif}">{isaret}</text>'
    ic += (f'<text x="{x}" y="{y - 3:.1f}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{pay}</text>'
           f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" class="{sinif.replace("f", "s") if sinif.endswith("f") else "g-c"}" stroke-width="1.6"/>'
           f'<text x="{x}" y="{y + boy + 1:.1f}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{sinif}">{payda}</text>')
    return ic


def dikey_tam_sayi():
    """Deniz seviyesi 0; yukarısı pozitif (mavi), aşağısı negatif (turuncu)."""
    x, y0, adim = 70, 150, 30
    ic = '<defs>' + ok_isareti('okD', 'g-mf') + '</defs>'
    ic += f'<line x1="{x}" y1="{y0 + 3 * adim + 22}" x2="{x}" y2="{y0 - 3 * adim - 26}" class="g-ms" stroke-width="2.5" marker-end="url(#okD)"/>'
    for n in range(-3, 4):
        y = y0 - n * adim
        s = 'g-mf' if n > 0 else ('g-tf' if n < 0 else 'g-yf')
        ic += f'<line x1="{x - 7}" y1="{y}" x2="{x + 7}" y2="{y}" class="g-c" stroke-width="2"/>'
        ic += f'<text x="{x - 16}" y="{y + 5}" text-anchor="end" font-size="15" font-weight="800" class="{s}">{("+" + str(n)) if n > 0 else isaretli(n)}</text>'
    ic += f'<rect x="{x + 22}" y="{y0 - 3 * adim - 8}" width="8" height="{3 * adim}" rx="4" class="g-mf"/>'
    ic += f'<text x="{x + 40}" y="{y0 - 1.5 * adim}" font-size="14" font-weight="700" class="g-mf">pozitif tam sayılar</text>'
    ic += f'<text x="{x + 40}" y="{y0 - 1.5 * adim + 18}" font-size="12.5" class="g-s">deniz seviyesinin üstü</text>'
    ic += f'<circle cx="{x}" cy="{y0}" r="6" class="g-yf"/>'
    ic += f'<text x="{x + 40}" y="{y0 + 5}" font-size="14" font-weight="700" class="g-yf">0: deniz seviyesi</text>'
    ic += f'<rect x="{x + 22}" y="{y0 + 8}" width="8" height="{3 * adim}" rx="4" class="g-tf"/>'
    ic += f'<text x="{x + 40}" y="{y0 + 1.5 * adim + 8}" font-size="14" font-weight="700" class="g-tf">negatif tam sayılar</text>'
    ic += f'<text x="{x + 40}" y="{y0 + 1.5 * adim + 26}" font-size="12.5" class="g-s">deniz seviyesinin altı</text>'
    return svg(300, 300, ic, 'Dikey sayı doğrusu: 0 deniz seviyesi; +1, +2, +3 yukarıda pozitif, −1, −2, −3 aşağıda negatif tam sayılar')


def yatay_tam_sayi():
    x0, adim, y = 30, 28, 60
    ic = '<defs>' + ok_isareti('okY', 'g-mf') + '</defs>'
    ic += f'<line x1="{x0 - 20}" y1="{y}" x2="{x0 + 10 * adim + 22}" y2="{y}" class="g-ms" stroke-width="2.5" marker-end="url(#okY)" marker-start="url(#okY)"/>'
    for i, n in enumerate(range(-5, 6)):
        x = x0 + i * adim
        s = 'g-mf' if n > 0 else ('g-tf' if n < 0 else 'g-yf')
        ic += f'<line x1="{x}" y1="{y - 7}" x2="{x}" y2="{y + 7}" class="g-c" stroke-width="2"/>'
        ic += f'<text x="{x}" y="{y + 26}" text-anchor="middle" font-size="14" font-weight="700" class="{s}">{isaretli(n)}</text>'
    ic += f'<circle cx="{x0 + 5 * adim}" cy="{y}" r="6" class="g-yf"/>'
    ic += f'<rect x="{x0 - 4}" y="{y - 38}" width="{4 * adim + 8}" height="8" rx="4" class="g-tf"/>'
    ic += f'<text x="{x0 + 2 * adim}" y="{y - 46}" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">negatif</text>'
    ic += f'<rect x="{x0 + 6 * adim - 4}" y="{y - 38}" width="{4 * adim + 8}" height="8" rx="4" class="g-mf"/>'
    ic += f'<text x="{x0 + 8 * adim}" y="{y - 46}" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">pozitif</text>'
    ic += f'<text x="{x0 + 5 * adim}" y="{y + 56}" text-anchor="middle" font-size="13" class="g-s">Ardışık iki tam sayı arasında başka tam sayı yoktur.</text>'
    return svg(344, 128, ic, 'Yatay sayı doğrusu −5’ten 5’e: 0’ın solunda negatif, sağında pozitif tam sayılar')


def denk_kesir_2_3():
    """0–1 aralığı 3, 6 ve 9 eş parçaya bölünmüş; 2/3, 4/6, 6/9 aynı noktada."""
    x0, x1 = 60, 300
    satir = [(3, 2, 'g-mf', 'g-ms'), (6, 4, 'g-yf', 'g-ys'), (9, 6, 'g-of', 'g-os')]
    ic, hx = '', x0 + (x1 - x0) * 2 / 3
    for k, (payda, pay, f, s) in enumerate(satir):
        y = 52 + k * 62
        ic += f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" class="{s}" stroke-width="2.5"/>'
        for i in range(payda + 1):
            x = x0 + (x1 - x0) * i / payda
            ic += f'<line x1="{x:.1f}" y1="{y - 6}" x2="{x:.1f}" y2="{y + 6}" class="g-c" stroke-width="{2 if i in (0, payda) else 1.4}"/>'
        ic += f'<line x1="{x0}" y1="{y}" x2="{hx:.1f}" y2="{y}" class="{s}" stroke-width="6" stroke-linecap="round" opacity=".55"/>'
        ic += f'<circle cx="{hx:.1f}" cy="{y}" r="6" class="{f}"/>'
        ic += kesir_svg(hx + 24, y - 26, str(pay), str(payda), f, 14)   # kesir tamamen çizginin üstünde
        ic += f'<text x="{x0 - 14}" y="{y + 5}" text-anchor="end" font-size="13" class="g-s">0</text>'
        ic += f'<text x="{x1 + 14}" y="{y + 5}" font-size="13" class="g-s">1</text>'
    ic += f'<line x1="{hx:.1f}" y1="14" x2="{hx:.1f}" y2="{52 + 2 * 62 + 18}" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += f'<text x="180" y="{52 + 2 * 62 + 44}" text-anchor="middle" font-size="13" class="g-s">Denk kesirler sayı doğrusunda aynı noktaya karşılık gelir.</text>'
    return svg(360, 52 + 2 * 62 + 56, ic, '0 ile 1 arası 3, 6 ve 9 eş parçaya bölünmüş üç sayı doğrusu; 2 bölü 3, 4 bölü 6 ve 6 bölü 9 aynı noktada')


def sayi_kumeleri():
    """Doğal ⊂ tam ⊂ rasyonel (iç içe alanlar; sembol kullanılmaz)."""
    ic = ('<rect x="10" y="10" width="340" height="190" rx="22" class="g-oa"/><rect x="10" y="10" width="340" height="190" rx="22" class="g-os" stroke-width="2"/>'
          '<text x="26" y="36" font-size="14" font-weight="800" class="g-of">Rasyonel sayılar</text>'
          '<rect x="30" y="50" width="220" height="136" rx="18" class="g-ya"/><rect x="30" y="50" width="220" height="136" rx="18" class="g-ys" stroke-width="2"/>'
          '<text x="44" y="74" font-size="14" font-weight="800" class="g-yf">Tam sayılar</text>'
          '<rect x="50" y="88" width="120" height="84" rx="14" class="g-ma"/><rect x="50" y="88" width="120" height="84" rx="14" class="g-ms" stroke-width="2"/>'
          '<text x="62" y="110" font-size="13.5" font-weight="800" class="g-mf">Doğal sayılar</text>'
          '<text x="110" y="148" text-anchor="middle" font-size="15" font-weight="700" class="g-mf">0   5   12</text>'
          f'<text x="210" y="118" text-anchor="middle" font-size="15" font-weight="700" class="g-yf">{EKSI}1</text>'
          f'<text x="210" y="156" text-anchor="middle" font-size="15" font-weight="700" class="g-yf">{EKSI}7</text>')
    ic += kesir_svg(298, 92, '3', '4', 'g-of', 15)
    ic += kesir_svg(298, 152, '2', '5', 'g-of', 15, isaret=EKSI)
    return svg(360, 210, ic, 'İç içe üç alan: doğal sayılar tam sayıların içinde, tam sayılar rasyonel sayıların içinde; örnekler 0, 5, 12; −1, −7; 3 bölü 4, eksi 2 bölü 5')


def rasyonel_dogru():
    """−2 ile 2 arası çeyreklere bölünmüş; −3/2, −1/4 ve 5/4 işaretli."""
    x0, y = 26, 96
    birim = 76
    ic = '<defs>' + ok_isareti('okR', 'g-mf') + '</defs>'
    ic += f'<line x1="{x0 - 14}" y1="{y}" x2="{x0 + 4 * birim + 18}" y2="{y}" class="g-ms" stroke-width="2.5" marker-end="url(#okR)" marker-start="url(#okR)"/>'
    for i in range(17):
        x = x0 + i * birim / 4
        tam = i % 4 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (8 if tam else 5)}" x2="{x:.1f}" y2="{y + (8 if tam else 5)}" class="g-c" stroke-width="{2 if tam else 1.3}"/>'
        if tam:
            n = i // 4 - 2
            ic += f'<text x="{x:.1f}" y="{y + 28}" text-anchor="middle" font-size="14" font-weight="700" class="{"g-yf" if n == 0 else "g-s"}">{isaretli(n)}</text>'
    for deger, pay, payda, f in ((-1.5, '3', '2', 'g-tf'), (-0.25, '1', '4', 'g-tf'), (1.25, '5', '4', 'g-mf')):
        x = x0 + (deger + 2) * birim
        ic += f'<circle cx="{x:.1f}" cy="{y}" r="6.5" class="{f}"/>'
        ic += kesir_svg(x + (6 if deger < 0 else 0), y - 44, pay, payda, f, 14, isaret=EKSI if deger < 0 else '')
    return svg(360, 140, ic, 'Sayı doğrusu −2’den 2’ye çeyreklere bölünmüş; eksi 3 bölü 2, eksi 1 bölü 4 ve 5 bölü 4 noktaları')


def mutlak_deger_4():
    x0, adim, y = 30, 28, 84
    ic = '<defs>' + ok_isareti('okM', 'g-mf') + ok_isareti('okMt', 'g-tf') + ok_isareti('okMm', 'g-mf') + '</defs>'
    ic += f'<line x1="{x0 - 20}" y1="{y}" x2="{x0 + 10 * adim + 22}" y2="{y}" class="g-ms" stroke-width="2.5" marker-end="url(#okM)" marker-start="url(#okM)"/>'
    for i, n in enumerate(range(-5, 6)):
        x = x0 + i * adim
        ic += f'<line x1="{x}" y1="{y - 7}" x2="{x}" y2="{y + 7}" class="g-c" stroke-width="2"/>'
        vurgu = n in (-4, 0, 4)
        s = 'g-tf' if n == -4 else ('g-mf' if n == 4 else ('g-yf' if n == 0 else 'g-s'))
        ic += f'<text x="{x}" y="{y + 26}" text-anchor="middle" font-size="{14 if vurgu else 12.5}" font-weight="{800 if vurgu else 400}" class="{s}">{isaretli(n)}</text>'
    xs = x0 + 5 * adim
    ic += f'<path d="M{xs - 4} {y - 10} Q{xs - 2 * adim} {y - 58} {xs - 4 * adim + 6} {y - 12}" class="g-ts" stroke-width="2.4" marker-end="url(#okMt)"/>'
    ic += f'<path d="M{xs + 4} {y - 10} Q{xs + 2 * adim} {y - 58} {xs + 4 * adim - 6} {y - 12}" class="g-ms" stroke-width="2.4" marker-end="url(#okMm)"/>'
    ic += f'<text x="{xs - 2 * adim}" y="{y - 50}" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">4 birim</text>'
    ic += f'<text x="{xs + 2 * adim}" y="{y - 50}" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">4 birim</text>'
    ic += f'<circle cx="{xs}" cy="{y}" r="6" class="g-yf"/><circle cx="{xs - 4 * adim}" cy="{y}" r="6" class="g-tf"/><circle cx="{xs + 4 * adim}" cy="{y}" r="6" class="g-mf"/>'
    ic += (f'<text x="{xs - 2 * adim}" y="{y + 58}" text-anchor="middle" font-size="16" font-weight="800" class="g-tf">|{EKSI}4| = 4</text>'
           f'<text x="{xs + 2 * adim}" y="{y + 58}" text-anchor="middle" font-size="16" font-weight="800" class="g-mf">|4| = 4</text>')
    return svg(344, 158, ic, '−4 ve 4 sayı doğrusunda 0’a 4’er birim uzaklıkta; mutlak değer −4 = 4, mutlak değer 4 = 4')


def ornek_a_noktasi():
    """−1 ile 1 arası beşte birlere bölünmüş; A noktası 0'ın solunda 3. çizgide."""
    x0, birim, y = 50, 130, 60
    ic = '<defs>' + ok_isareti('okA', 'g-mf') + '</defs>'
    ic += f'<line x1="{x0 - 26}" y1="{y}" x2="{x0 + 2 * birim + 28}" y2="{y}" class="g-ms" stroke-width="2.5" marker-end="url(#okA)" marker-start="url(#okA)"/>'
    for i in range(11):
        x = x0 + i * birim / 5
        tam = i % 5 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (8 if tam else 5)}" x2="{x:.1f}" y2="{y + (8 if tam else 5)}" class="g-c" stroke-width="{2 if tam else 1.3}"/>'
        if tam:
            ic += f'<text x="{x:.1f}" y="{y + 28}" text-anchor="middle" font-size="14" font-weight="700" class="g-s">{isaretli(i // 5 - 1)}</text>'
    xa = x0 + 2 * birim / 5
    ic += f'<circle cx="{xa:.1f}" cy="{y}" r="6.5" class="g-tf"/><text x="{xa:.1f}" y="{y - 18}" text-anchor="middle" font-size="16" font-weight="800" class="g-tf">A</text>'
    return svg(360, 104, ic, 'Sayı doğrusu −1’den 1’e; her birim 5 eş parçaya bölünmüş; A noktası 0’ın solunda')


def mat7(o):
    g = {'Tam sayılar: yönü olan sayılar': dikey_tam_sayi(), 'Tam sayılar sayı doğrusunda': yatay_tam_sayi(),
         'Tam sayılar yetmediğinde: rasyonel sayılar': denk_kesir_2_3(), 'Sayı kümeleri iç içe': sayi_kumeleri(),
         'Rasyonel sayılar sayı doğrusunda': rasyonel_dogru(), 'Mutlak değer: sıfıra uzaklık': mutlak_deger_4()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
    for x in o['ornekler']:
        if x.get('gorsel'):
            x['gorsel'] = ornek_a_noktasi()


# ---------- 5. sınıf Fen Bilimleri: Güneş'in yapısı ve dönme hareketi ----------
def gunes_katmanlari():
    """Kesit: içten dışa çekirdek, ışınım, konveksiyon, ışık küre, renk küre, taç; etiketler sağda, çizgiler yazıya değmez."""
    cx, cy = 120, 160
    katman = [(150, 'g-ta', '.35'), (116, 'g-ta', '.7'), (108, 'g-tf', '.45'), (100, 'g-tf', '.6'), (66, 'g-tf', '.8'), (30, 'g-tf', '1')]
    ic = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{s}" opacity="{o}"/>' for r, s, o in katman)
    etiket = [('Taç (korona)', 'en dış katman', 133), ('Renk küre (kromosfer)', '', 112), ('Işık küre (fotosfer)', 'görünen yüzey', 104),
              ('Konveksiyon katmanı', 'enerji akıntılarla taşınır', 83), ('Işınım katmanı', 'enerji ışıkla taşınır', 48), ('Çekirdek', 'enerji üretilir', 12)]
    import math as _m
    for k, (ad, alt, r) in enumerate(etiket):
        aci = _m.radians(-58 + k * 23)
        px, py = cx + r * _m.cos(aci), cy + r * _m.sin(aci)
        ty = 30 + k * 50
        ic += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" class="g-y"/>'
        ic += f'<line x1="{px:.1f}" y1="{py:.1f}" x2="292" y2="{ty - 5}" class="g-c" stroke-width="1.4"/>'
        ic += f'<text x="298" y="{ty}" font-size="14" font-weight="700" class="g-tf">{ad}</text>'
        if alt:
            ic += f'<text x="298" y="{ty + 17}" font-size="12.5" class="g-s">{alt}</text>'
    return svg(470, 320, ic, 'Güneş’in kesiti: içten dışa çekirdek, ışınım katmanı, konveksiyon katmanı, ışık küre, renk küre ve taç')


def gunes_leke():
    """Aynı lekenin 1., 4. ve 7. günde Güneş diskindeki yeri: leke soldan sağa kayar → Güneş döner."""
    ic = '<defs>' + ok_isareti('okG', 'g-tf') + '</defs>'
    for k, (gun, dx) in enumerate(((1, -38), (4, -12), (7, 16))):
        cx = 70 + k * 120
        ic += f'<circle cx="{cx}" cy="80" r="50" class="g-ta"/><circle cx="{cx}" cy="80" r="50" class="g-ts" stroke-width="2"/>'
        ic += f'<ellipse cx="{cx + dx}" cy="70" rx="{7 if k == 1 else 5.5}" ry="6" class="g-y" opacity=".85"/>'
        ic += f'<text x="{cx}" y="152" text-anchor="middle" font-size="14" font-weight="700" class="g-y">{gun}. gün</text>'
    ic += '<path d="M40 22 Q190 -6 340 22" class="g-ts" stroke-width="2.2" marker-end="url(#okG)"/>'
    ic += '<text x="190" y="176" text-anchor="middle" font-size="13" class="g-s">Koyu leke her gün biraz daha sağda görülür: Güneş kendi ekseni etrafında döner.</text>'
    return svg(380, 186, ic, 'Üç Güneş diski: aynı leke 1. gün solda, 4. gün ortaya yakın, 7. gün ortanın sağında; Güneş dönüyor')


def gunes_dunya_boyut():
    """Güneş'in bir parçası ve Dünya aynı ölçekte (çap oranı yaklaşık 109)."""
    R = 327                       # Güneş yarıçapı (px); Dünya yarıçapı 3 px → oran 109
    ic = ('<defs><clipPath id="kesGD"><rect x="0" y="0" width="380" height="180" rx="10"/></clipPath></defs>'   # dev daire görselin dışına taşmasın
          f'<g clip-path="url(#kesGD)"><circle cx="{-R + 150}" cy="90" r="{R}" class="g-ta"/><circle cx="{-R + 150}" cy="90" r="{R}" class="g-ts" stroke-width="2"/></g>')
    ic += '<text x="40" y="96" font-size="15" font-weight="800" class="g-tf">Güneş</text>'
    ic += '<circle cx="250" cy="90" r="3" class="g-mf"/>'
    ic += '<line x1="258" y1="84" x2="286" y2="60" class="g-c" stroke-width="1.4"/><text x="290" y="58" font-size="14" font-weight="700" class="g-mf">Dünya</text>'
    ic += '<text x="190" y="200" text-anchor="middle" font-size="13" class="g-s">Aynı ölçek: Güneş’in çapı Dünya’nın çapının yaklaşık 109 katıdır.</text>'
    return svg(380, 210, ic, 'Aynı ölçekte Güneş’in bir parçası ve yanında küçük bir nokta olarak Dünya; çap oranı yaklaşık 109')


def fen5(o):
    g = {'Güneş: bize en yakın yıldız': gunes_dunya_boyut(), 'Güneş’in katmanlı yapısı': gunes_katmanlari(),
         'Güneş de döner': gunes_leke()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]


if __name__ == '__main__':
    yaz('5-matematik-1.json', mat5)
    yaz('8-matematik-1.json', mat8)
    if (OZET / '6-matematik-1.json').exists():
        yaz('6-matematik-1.json', mat6)
    if (OZET / '7-matematik-1.json').exists():
        yaz('7-matematik-1.json', mat7)
    if (OZET / '5-fen-bilimleri-2.json').exists():
        yaz('5-fen-bilimleri-2.json', fen5)
    print('görseller yazıldı')
