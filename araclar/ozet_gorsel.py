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


if __name__ == '__main__':
    yaz('5-matematik-1.json', mat5)
    yaz('8-matematik-1.json', mat8)
    if (OZET / '6-matematik-1.json').exists():
        yaz('6-matematik-1.json', mat6)
    print('görseller yazıldı')
