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
    """Doğrunun dışındaki P noktasından çizilen dikme (en kısa doğru parçası); diklik ⊥ ile gösterilir."""
    ic = '<line x1="30" y1="140" x2="300" y2="140" class="g-ms" stroke-width="3" stroke-linecap="round"/>'
    ic += '<line x1="160" y1="34" x2="74" y2="140" class="g-c" stroke-width="1.6" stroke-dasharray="5 5"/>'
    ic += '<line x1="160" y1="34" x2="248" y2="140" class="g-c" stroke-width="1.6" stroke-dasharray="5 5"/>'
    ic += '<line x1="160" y1="34" x2="160" y2="140" class="g-ts" stroke-width="3" stroke-linecap="round"/>'
    ic += '<rect x="160" y="124" width="16" height="16" class="g-ta"/><path d="M160 124 H176 V140" class="g-ts" stroke-width="2"/>'
    ic += '<circle cx="160" cy="34" r="5.5" class="g-tf"/><circle cx="160" cy="140" r="4.5" class="g-tf"/>'
    ic += '<text x="160" y="20" text-anchor="middle" font-size="16" font-weight="800" class="g-tf">P</text>'
    ic += '<text x="160" y="164" text-anchor="middle" font-size="16" font-weight="800" class="g-tf">H</text>'
    ic += '<text x="292" y="132" font-size="16" font-weight="700" class="g-mf">d</text>'
    ic += '<text x="196" y="174" font-size="14" font-weight="700" class="g-tf">[PH] ⊥ d</text>'
    ic += '<text x="165" y="200" text-anchor="middle" font-size="12.5" class="g-s">Kesikli çizgiler daha uzundur; dikme en kısa doğru parçasıdır.</text>'
    return svg(330, 210, ic, 'd doğrusunun dışındaki P noktasından d doğrusuna çizilen dikme PH; diklik sembolü; öteki doğru parçaları daha uzun')


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


def bolen_listesi_72():
    """Bölen listesi yöntemi (MEB 8. sınıf kitabı): 72 | 2, 36 | 2, 18 | 2, 9 | 3, 3 | 3, 1; asal bölenler turuncu."""
    satir = [(72, 2), (36, 2), (18, 2), (9, 3), (3, 3), (1, None)]
    x_sayi, x_cizgi, x_bolen, y0, ad = 118, 140, 162, 34, 30
    ic = f'<line x1="{x_cizgi}" y1="{y0 - 20}" x2="{x_cizgi}" y2="{y0 + (len(satir) - 1) * ad + 10}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    for i, (n, b) in enumerate(satir):
        y = y0 + i * ad
        ic += f'<text x="{x_sayi}" y="{y}" text-anchor="end" font-size="18" font-weight="{800 if i == 0 else 600}" class="{"g-mf" if i == 0 else "g-y"}">{n}</text>'
        if b:
            ic += f'<circle cx="{x_bolen + 12}" cy="{y - 6}" r="13" class="g-tf"/><text x="{x_bolen + 12}" y="{y}" text-anchor="middle" font-size="16" font-weight="800" class="g-b">{b}</text>'
    y = y0 + len(satir) * ad + 22
    ic += (f'<text x="140" y="{y}" text-anchor="middle" font-size="19" font-weight="700" class="g-y">72 = '
           '<tspan class="g-tf">2</tspan><tspan dy="-8" font-size="13" class="g-tf">3</tspan><tspan dy="8"> · </tspan>'
           '<tspan class="g-tf">3</tspan><tspan dy="-8" font-size="13" class="g-tf">2</tspan></text>')
    ic += (f'<text x="210" y="{y0 + 4}" font-size="12.5" class="g-s">Her satırda sayıyı kalansız</text><text x="210" y="{y0 + 20}" font-size="12.5" class="g-s">bölen en küçük asal sayı</text>'
           f'<text x="210" y="{y0 + 36}" font-size="12.5" class="g-s">sağa yazılır; bölüm alta.</text>'
           f'<text x="210" y="{y0 + 4 * ad + 4}" font-size="12.5" class="g-s">Bölüm 1 olunca durulur.</text>')
    return svg(380, y + 16, ic, 'Bölen listesi yöntemiyle 72: 72, 36, 18, 9, 3, 1 ve sağda asal bölenler 2, 2, 2, 3, 3; sonuç 72 = 2 üssü 3 çarpı 3 üssü 2')


def mat8(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Bölen listesi yöntemi':
            b['gorsel'] = bolen_listesi_72()


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
        ic += f'<text x="{x0 + en * birim + 16}" y="{y + boy * birim / 2 + 6}" font-size="16" font-weight="800" class="{f}">{en} × {boy} = 12</text>'
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
    """Güneş katmanlıdır: içte çekirdek (en sıcak), dışta yüzey (lekeler burada görülür). Yalnız kitaptaki bilgiler."""
    cx, cy = 120, 130
    ic = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{s}" opacity="{o}"/>' for r, s, o in ((104, 'g-ta', '.75'), (80, 'g-tf', '.45'), (56, 'g-tf', '.65'), (30, 'g-tf', '1')))
    ic += f'<circle cx="{cx}" cy="{cy}" r="104" class="g-ts" stroke-width="2"/>'
    ic += f'<ellipse cx="{cx - 40}" cy="{cy - 70}" rx="7" ry="5.5" class="g-y" opacity=".8"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="3" class="g-b"/><line x1="{cx + 3}" y1="{cy}" x2="262" y2="{cy + 40}" class="g-c" stroke-width="1.4"/>'
    ic += f'<text x="268" y="{cy + 44}" font-size="14" font-weight="800" class="g-tf">Çekirdek</text><text x="268" y="{cy + 61}" font-size="12.5" class="g-s">en sıcak bölge</text>'
    ic += f'<line x1="{cx + 74}" y1="{cy - 74}" x2="262" y2="{cy - 86}" class="g-c" stroke-width="1.4"/>'
    ic += f'<text x="268" y="{cy - 88}" font-size="14" font-weight="800" class="g-tf">Yüzey</text><text x="268" y="{cy - 71}" font-size="12.5" class="g-s">Güneş lekeleri burada görülür</text>'
    ic += f'<line x1="{cx + 70}" y1="{cy + 10}" x2="262" y2="{cy - 16}" class="g-c" stroke-width="1.4"/>'
    ic += f'<text x="268" y="{cy - 14}" font-size="14" font-weight="800" class="g-tf">Katmanlar</text><text x="268" y="{cy + 3}" font-size="12.5" class="g-s">Dünya gibi iç içe katmanlar</text>'
    return svg(470, 260, ic, 'Güneş’in kesiti: iç içe katmanlar; merkezde en sıcak bölge olan çekirdek, dışta lekelerin görüldüğü yüzey')


def gunes_leke():
    """Aynı lekenin 1., 4. ve 7. günde Güneş diskindeki yeri: leke soldan sağa kayar → Güneş döner."""
    ic = '<defs>' + ok_isareti('okG', 'g-tf') + '</defs>'
    for k, (gun, dx) in enumerate(((1, -38), (4, -12), (7, 16))):
        cx = 70 + k * 120
        ic += f'<circle cx="{cx}" cy="80" r="50" class="g-ta"/><circle cx="{cx}" cy="80" r="50" class="g-ts" stroke-width="2"/>'
        ic += f'<ellipse cx="{cx + dx}" cy="70" rx="{7 if k == 1 else 5.5}" ry="6" class="g-y" opacity=".85"/>'
        ic += f'<text x="{cx}" y="152" text-anchor="middle" font-size="14" font-weight="700" class="g-y">{gun}. gün</text>'
    ic += '<path d="M40 22 Q190 -6 340 22" class="g-ts" stroke-width="2.2" marker-end="url(#okG)"/>'
    ic += '<text x="190" y="176" text-anchor="middle" font-size="13" class="g-s">Lekeler hep aynı yöne kayar: Güneş kendi ekseni etrafında döner.</text>'
    return svg(380, 186, ic, 'Üç Güneş diski: aynı leke 1. gün solda, 4. gün ortaya yakın, 7. gün ortanın sağında; Güneş dönüyor')


def gunes_dunya_boyut():
    """Güneş’in bir parçası ve Dünya: Güneş Dünya’dan çok daha büyüktür."""
    R = 327
    ic = ('<defs><clipPath id="kesGD"><rect x="0" y="0" width="380" height="180" rx="10"/></clipPath></defs>'   # dev daire görselin dışına taşmasın
          f'<g clip-path="url(#kesGD)"><circle cx="{-R + 150}" cy="90" r="{R}" class="g-ta"/><circle cx="{-R + 150}" cy="90" r="{R}" class="g-ts" stroke-width="2"/></g>')
    ic += '<text x="40" y="96" font-size="15" font-weight="800" class="g-tf">Güneş</text>'
    ic += '<circle cx="250" cy="90" r="3" class="g-mf"/>'
    ic += '<line x1="258" y1="84" x2="286" y2="60" class="g-c" stroke-width="1.4"/><text x="290" y="58" font-size="14" font-weight="700" class="g-mf">Dünya</text>'
    ic += '<text x="190" y="200" text-anchor="middle" font-size="13" class="g-s">Güneş Dünya’dan çok daha büyüktür; çok uzakta olduğu için küçük görünür.</text>'
    return svg(380, 210, ic, 'Güneş’in bir parçası ve yanında küçük bir nokta olarak Dünya: Güneş Dünya’dan çok daha büyüktür')


def fen5(o):
    g = {'Güneş: bize en yakın yıldız': gunes_dunya_boyut(), 'Güneş’in katmanlı yapısı': gunes_katmanlari(),
         'Güneş de döner': gunes_leke()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]


# ---------- 6. sınıf Fen Bilimleri: Güneş sistemi ----------
def gunes_sistemi():
    """Gezegenler Güneş'e yakınlık sırasıyla; boyutlar yaklaşık gerçek oranda, uzaklıklar ölçeksiz.
    Karasal = turuncu, gazsal = mor; halkalar gazsal gezegenlerde. Halkalar ve yazılar birbirine değmez."""
    ic = ('<defs><clipPath id="kesGS"><rect x="0" y="0" width="640" height="236"/></clipPath></defs>'
          '<g clip-path="url(#kesGS)"><circle cx="-40" cy="110" r="100" class="g-tf" opacity=".9"/></g>'
          '<text x="8" y="115" font-size="13" font-weight="800" class="g-b">Güneş</text>')
    gez = [('Merkür', 82, 2.2, 'k', 184), ('Venüs', 108, 4.3, 'k', 204), ('Dünya', 136, 4.5, 'k', 184), ('Mars', 162, 2.6, 'k', 204),
           ('Jüpiter', 272, 50, 'g', 184), ('Satürn', 412, 42, 'g', 184), ('Uranüs', 518, 18, 'g', 184), ('Neptün', 590, 17.5, 'g', 184)]
    y = 110
    for ad, x, r, grup, ly in gez:
        a, s, f = ('g-ta', 'g-ts', 'g-tf') if grup == 'k' else ('g-oa', 'g-os', 'g-of')
        if grup == 'g':
            rx, ry, kal = (r * 1.75, r * 0.34, 5) if ad == 'Satürn' else (r * 1.3, r * 0.24, 1.6)
            ic += f'<ellipse cx="{x}" cy="{y}" rx="{rx:.1f}" ry="{ry:.1f}" class="{s}" stroke-width="{kal}" opacity=".75" transform="rotate(-14 {x} {y})"/>'
        ic += f'<circle cx="{x}" cy="{y}" r="{r}" class="{a}"/><circle cx="{x}" cy="{y}" r="{r}" class="{s}" stroke-width="1.6"/>'
        if grup == 'k':
            ic += f'<line x1="{x}" y1="{y + r + 5:.1f}" x2="{x}" y2="{ly - 14}" class="g-c" stroke-width="1.2"/>'
        ic += f'<text x="{x}" y="{ly}" text-anchor="middle" font-size="13" font-weight="700" class="{f}">{ad}</text>'
    import random as _r
    _r.seed(7)
    for i in range(34):   # asteroit kuşağı: Mars ile Jüpiter arası
        ic += f'<circle cx="{184 + _r.random() * 20:.1f}" cy="{y - 42 + _r.random() * 84:.1f}" r="{0.8 + _r.random() * 1.2:.1f}" class="g-y" opacity=".55"/>'
    ic += '<text x="194" y="54" text-anchor="middle" font-size="12" font-weight="700" class="g-y">asteroit kuşağı</text>'
    ic += ('<rect x="70" y="8" width="104" height="6" rx="3" class="g-tf"/><text x="122" y="30" text-anchor="middle" font-size="12.5" font-weight="700" class="g-tf">karasal</text>'
           '<rect x="222" y="8" width="390" height="6" rx="3" class="g-of"/><text x="417" y="30" text-anchor="middle" font-size="12.5" font-weight="700" class="g-of">gazsal</text>')
    ic += '<text x="320" y="228" text-anchor="middle" font-size="12.5" class="g-s">Boyutlar yaklaşık gerçek orandadır; gezegenler arasındaki uzaklıklar ölçekli değildir.</text>'
    return svg(640, 236, ic, 'Güneş ve Güneş’e yakınlık sırasıyla Merkür, Venüs, Dünya, Mars (karasal, küçük), asteroit kuşağı, Jüpiter, Satürn, Uranüs, Neptün (gazsal, büyük, halkalı)')


def meteor_yolu():
    """Gök taşı → atmosferde parlayan meteor → yere ulaşan meteorit ve meteor çukuru."""
    ic = '<defs>' + ok_isareti('okMY', 'g-tf') + '</defs>'
    ic += '<text x="12" y="20" font-size="12.5" class="g-s">uzay</text>'
    ic += '<rect x="0" y="74" width="380" height="72" class="g-ma" opacity=".45"/><text x="372" y="92" text-anchor="end" font-size="12.5" font-weight="700" class="g-mf">atmosfer</text>'
    ic += '<path d="M0 190 H262 Q300 216 338 190 H380 V232 H0 Z" class="g-ya"/><path d="M0 190 H262 Q300 216 338 190 H380" class="g-ys" stroke-width="2"/>'
    ic += '<path d="M44 30 l10 -6 l10 3 l3 9 l-7 8 l-11 0 l-6 -7 z" class="g-y" opacity=".75"/>'
    ic += '<text x="76" y="30" font-size="13.5" font-weight="700" class="g-y">gök taşı</text>'
    ic += '<line x1="66" y1="48" x2="150" y2="84" class="g-c" stroke-width="2" stroke-dasharray="5 5"/>'
    ic += '<line x1="152" y1="85" x2="258" y2="138" class="g-ts" stroke-width="8" stroke-linecap="round" opacity=".3"/>'
    ic += '<line x1="152" y1="85" x2="258" y2="138" class="g-ts" stroke-width="3" stroke-linecap="round" marker-end="url(#okMY)"/>'
    ic += '<text x="150" y="124" font-size="13.5" font-weight="700" class="g-tf">meteor</text><text x="150" y="140" font-size="12" class="g-s">atmosfere giren gök taşı</text>'
    ic += '<line x1="264" y1="150" x2="296" y2="194" class="g-c" stroke-width="2" stroke-dasharray="5 5"/>'
    ic += '<path d="M292 200 l6 -5 l8 2 l2 6 l-6 5 l-8 -1 z" class="g-y" opacity=".85"/>'
    ic += '<line x1="312" y1="196" x2="336" y2="166" class="g-c" stroke-width="1.2"/><text x="340" y="164" font-size="13.5" font-weight="700" class="g-y">meteorit</text>'
    ic += '<text x="300" y="226" text-anchor="middle" font-size="12.5" font-weight="700" class="g-yf">meteor çukuru</text>'
    return svg(380, 234, ic, 'Atmosfere giren gök taşı meteor; yeryüzüne ulaşan gök taşı meteorit; açtığı çukur meteor çukurudur')


def fen6(o):
    g = {'Güneş sistemi': gunes_sistemi(), 'Asteroit kuşağı, gök taşı, meteor ve meteorit': meteor_yolu()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]


# ---------- 7. sınıf Fen Bilimleri: uzay araştırmaları teknolojileri ----------
def uydu_simge(x, y, a, s, f):
    return (f'<rect x="{x - 19}" y="{y - 3.5}" width="12" height="7" rx="1.5" class="{a}"/><rect x="{x - 19}" y="{y - 3.5}" width="12" height="7" rx="1.5" class="{s}" stroke-width="1.3"/>'
            f'<rect x="{x + 7}" y="{y - 3.5}" width="12" height="7" rx="1.5" class="{a}"/><rect x="{x + 7}" y="{y - 3.5}" width="12" height="7" rx="1.5" class="{s}" stroke-width="1.3"/>'
            f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" rx="2.5" class="{f}"/>')


def yapay_uydular():
    cx, cy, R = 230, 136, 96
    ic = f'<circle cx="{cx}" cy="{cy}" r="{R}" class="g-c" stroke-width="1.5" stroke-dasharray="5 6"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="46" class="g-ma"/><circle cx="{cx}" cy="{cy}" r="46" class="g-ms" stroke-width="2"/>'
    ic += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="15" font-weight="800" class="g-mf">Dünya</text>'
    uydu = [(cx, cy - R, ('g-ya', 'g-ys', 'g-yf'), ('Gözlem', 'İMECE, GÖKTÜRK'), 'ust'),
            (cx + R, cy, ('g-ta', 'g-ts', 'g-tf'), ('Meteoroloji', 'hava tahmini'), 'sag'),
            (cx, cy + R, ('g-oa', 'g-os', 'g-of'), ('Konum', 'yer-yön bulma'), 'alt'),
            (cx - R, cy, ('g-ma', 'g-ms', 'g-mf'), ('Haberleşme', 'TÜRKSAT'), 'sol')]
    for x, y, (a, s, f), (ad, ornek), yer in uydu:
        ic += uydu_simge(x, y, a, s, f)
        if yer == 'ust':
            ic += f'<text x="{x}" y="{y - 26}" text-anchor="middle" font-size="14" font-weight="800" class="{f}">{ad}</text><text x="{x}" y="{y - 12}" text-anchor="middle" font-size="12" class="g-s">{ornek}</text>'
        elif yer == 'alt':
            ic += f'<text x="{x}" y="{y + 26}" text-anchor="middle" font-size="14" font-weight="800" class="{f}">{ad}</text><text x="{x}" y="{y + 41}" text-anchor="middle" font-size="12" class="g-s">{ornek}</text>'
        elif yer == 'sag':
            ic += f'<text x="{x + 26}" y="{y - 2}" font-size="14" font-weight="800" class="{f}">{ad}</text><text x="{x + 26}" y="{y + 14}" font-size="12" class="g-s">{ornek}</text>'
        else:
            ic += f'<text x="{x - 26}" y="{y - 2}" text-anchor="end" font-size="14" font-weight="800" class="{f}">{ad}</text><text x="{x - 26}" y="{y + 14}" text-anchor="end" font-size="12" class="g-s">{ornek}</text>'
    return svg(460, 284, ic, 'Dünya çevresinde dolanan yapay uydular ve kullanım alanları: gözlem, meteoroloji, konum, haberleşme')


def teleskoplar():
    """Yıldız ışığı: uzay teleskobuna dümdüz ulaşır; atmosferden geçerek yer tabanlı teleskoba titreşerek ulaşır."""
    ic = '<rect x="0" y="92" width="460" height="148" class="g-ma" opacity=".4"/>'
    ic += '<text x="452" y="110" text-anchor="end" font-size="12.5" font-weight="700" class="g-mf">atmosfer</text>'
    ic += '<path d="M0 240 L60 196 L118 150 L178 196 L240 240 Z" class="g-ya"/><path d="M0 240 L60 196 L118 150 L178 196 L240 240" class="g-ys" stroke-width="2"/>'
    ic += '<path d="M104 150 A14 14 0 0 1 132 150 Z" class="g-y" opacity=".8"/><rect x="104" y="150" width="28" height="10" class="g-y" opacity=".8"/>'
    ic += '<text x="118" y="206" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">Gözlemevi</text><text x="118" y="222" text-anchor="middle" font-size="11.5" class="g-yf">yer tabanlı teleskop</text>'
    ic += '<path d="M56 8 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1 z" class="g-tf"/>'
    ic += '<text x="78" y="22" font-size="12" class="g-s">yıldız</text>'
    ic += '<line x1="70" y1="30" x2="238" y2="58" class="g-ts" stroke-width="2" stroke-dasharray="6 4"/>'
    ic += ('<g transform="rotate(-12 262 62)"><rect x="244" y="54" width="38" height="16" rx="3" class="g-oa"/><rect x="244" y="54" width="38" height="16" rx="3" class="g-os" stroke-width="1.8"/>'
           '<rect x="250" y="36" width="10" height="16" rx="1.5" class="g-os" stroke-width="1.5"/><rect x="250" y="72" width="10" height="16" rx="1.5" class="g-os" stroke-width="1.5"/></g>')
    ic += '<text x="300" y="54" font-size="13" font-weight="800" class="g-of">Uzay teleskobu</text><text x="300" y="70" font-size="11.5" class="g-s">Hubble, James Webb</text>'
    ic += '<line x1="58" y1="36" x2="94" y2="92" class="g-ts" stroke-width="2" stroke-dasharray="6 4"/>'
    ic += '<line x1="94" y1="92" x2="114" y2="136" class="g-ts" stroke-width="1.4" stroke-dasharray="2 5" opacity=".6"/>'
    ic += '<text x="160" y="124" font-size="11.5" class="g-s">atmosfer ışınların bir</text><text x="160" y="138" font-size="11.5" class="g-s">bölümünü engeller; ışık</text><text x="160" y="152" font-size="11.5" class="g-s">kirliliği gözlemi zorlaştırır</text>'
    return svg(460, 242, ic, 'Bir yıldızın ışığı uzaydaki teleskoba engelsiz ulaşır; dağdaki gözlemevine atmosferden geçerken bir bölümü engellenir')


def fen7(o):
    g = {'Yapay uydular': yapay_uydular(), 'Teleskoplar: yerde ve uzayda': teleskoplar()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]


# ---------- 5. sınıf Sosyal Bilgiler: gruplar ve roller (yalnız MEB kitabındaki roller) ----------
def gruplar_roller():
    cx, cy, r = 230, 152, 34
    ic = f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-mf"/><text x="{cx}" y="{cy + 6}" text-anchor="middle" font-size="18" font-weight="800" class="g-b">Ben</text>'
    kutu = [(20, 22, 'Aile', ('çocuk, kardeş,', 'abla ya da ağabey'), ('g-ta', 'g-ts', 'g-tf'), (180, 92)),
            (280, 22, 'Okul', ('öğrenci, sınıf başkanı,', 'nöbetçi'), ('g-ma', 'g-ms', 'g-mf'), (280, 92)),
            (20, 212, 'Arkadaş grubu', ('oyun arkadaşı, lider,', 'arabulucu'), ('g-ya', 'g-ys', 'g-yf'), (180, 212)),
            (280, 212, 'Sosyal sorumluluk', ('gönüllü, yönetici,', 'kampanya sorumlusu'), ('g-oa', 'g-os', 'g-of'), (280, 212))]
    import math as _m
    for x, y, ad, roller, (a, s, f), (kx, ky) in kutu:
        ic += f'<rect x="{x}" y="{y}" width="160" height="70" rx="12" class="{a}"/><rect x="{x}" y="{y}" width="160" height="70" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 12}" y="{y + 24}" font-size="14.5" font-weight="800" class="{f}">{ad}</text>'
        ic += f'<text x="{x + 12}" y="{y + 44}" font-size="12.5" class="g-y">{roller[0]}</text><text x="{x + 12}" y="{y + 60}" font-size="12.5" class="g-y">{roller[1]}</text>'
        dx, dy = kx - cx, ky - cy; L = _m.hypot(dx, dy); ux, uy = dx / L, dy / L
        ic += f'<line x1="{cx + ux * (r + 5):.1f}" y1="{cy + uy * (r + 5):.1f}" x2="{kx - ux * 6:.1f}" y2="{ky - uy * 6:.1f}" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    ic += '<text x="230" y="306" text-anchor="middle" font-size="12.5" class="g-s">Birden çok grupta yer aldığımız için aynı anda birden fazla role sahip oluruz.</text>'
    return svg(460, 316, ic, 'Ortada Ben; çevresinde dört grup ve roller: Aile (çocuk, kardeş, abla ya da ağabey), Okul (öğrenci, sınıf başkanı, nöbetçi), Arkadaş grubu (oyun arkadaşı, lider, arabulucu), Sosyal sorumluluk (gönüllü, yönetici, kampanya sorumlusu)')


def sosyal5(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Dâhil olduğumuz gruplar ve rollerimiz':
            b['gorsel'] = gruplar_roller()


# ---------- 6. sınıf Sosyal Bilgiler: zaman içinde değişen gruplar ve roller ----------
def zaman_seridi_roller():
    ic = '<defs>' + ok_isareti('okZS', 'g-mf') + '</defs>'
    ic += '<line x1="20" y1="40" x2="452" y2="40" class="g-ms" stroke-width="3" marker-end="url(#okZS)"/>'
    evre = [(20, 'Çocukluk', ('g-ta', 'g-ts', 'g-tf'), [('Aile', 'çocuk, kardeş'), ('Akraba grubu', 'torun, kuzen, yeğen'), ('Arkadaş grubu', 'planlayıcı, arabulucu')]),
            (172, 'Okul yılları', ('g-ya', 'g-ys', 'g-yf'), [('Okul ve sınıf', 'öğrenci, nöbetçi,'), ('', 'sınıf başkanı'), ('Müzik grubu', 'solist, gitarist')]),
            (324, 'Yetişkinlik', ('g-oa', 'g-os', 'g-of'), [('Meslek grubu', 'çalışan, idareci'), ('Odak grubu', 'araştırmacı, lider'), ('Sivil toplum kur.', 'gönüllü')])]
    for x, ad, (a, s, f), satir in evre:
        ic += f'<circle cx="{x + 64}" cy="40" r="8" class="{f}"/>'
        ic += f'<text x="{x + 64}" y="24" text-anchor="middle" font-size="14.5" font-weight="800" class="{f}">{ad}</text>'
        ic += f'<rect x="{x}" y="60" width="128" height="176" rx="12" class="{a}"/><rect x="{x}" y="60" width="128" height="176" rx="12" class="{s}" stroke-width="2"/>'
        y = 84
        for grup, rol in satir:
            if grup:
                ic += f'<text x="{x + 10}" y="{y}" font-size="12.5" font-weight="800" class="{f}">{grup}</text>'
                y += 17
            ic += f'<text x="{x + 10}" y="{y}" font-size="12" class="g-y">{rol}</text>'
            y += 22
    ic += '<text x="236" y="262" text-anchor="middle" font-size="12.5" class="g-s">Zaman ilerledikçe dâhil olduğumuz gruplar ve bu gruplardaki rollerimiz değişir.</text>'
    return svg(472, 272, ic, 'Zaman şeridi: çocuklukta aile, akraba ve arkadaş grupları; okul yıllarında okul, sınıf ve müzik grubu; yetişkinlikte meslek grubu, odak grubu ve sivil toplum kuruluşu, her birinde roller')


def sosyal6(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Hayat boyunca değişen gruplarımız':
            b['gorsel'] = zaman_seridi_roller()


# ---------- 7. sınıf Sosyal Bilgiler: gruplarda ve sosyal hayatta iletişim ----------
def iletisim_turleri():
    ic = '<defs>' + ok_isareti('okIT', 'g-c') + '</defs>'
    ic += '<rect x="146" y="10" width="180" height="54" rx="12" class="g-oa"/><rect x="146" y="10" width="180" height="54" rx="12" class="g-os" stroke-width="2"/>'
    ic += '<text x="236" y="34" text-anchor="middle" font-size="16" font-weight="800" class="g-of">İletişim</text>'
    ic += '<text x="236" y="53" text-anchor="middle" font-size="11.5" class="g-y">duygu · düşünce · bilgi · deneyim</text>'
    tur = [(20, 'Sözlü', ('g-ma', 'g-ms', 'g-mf'), ('Ses ve sözcüklerle,', 'konuşma yoluyla', 'aktarılır.'), ('Komşuya', '“Günaydın!” demek')),
           (172, 'Yazılı', ('g-ya', 'g-ys', 'g-yf'), ('Yazı aracılığıyla', 'aktarılır.', ''), ('Arkadaşa telefonla', 'mesaj göndermek')),
           (324, 'Sözsüz', ('g-ta', 'g-ts', 'g-tf'), ('Jest, mimik, beden', 'hareketi, kıyafet', 'gibi unsurlarla.'), ('Gülümsemek, başını', 'sallamak'))]
    for x, ad, (a, s, f), tanim, ornek in tur:
        ic += f'<line x1="236" y1="68" x2="{x + 64}" y2="96" class="g-c" stroke-width="2" marker-end="url(#okIT)"/>'
        ic += f'<rect x="{x}" y="102" width="128" height="160" rx="12" class="{a}"/><rect x="{x}" y="102" width="128" height="160" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 64}" y="127" text-anchor="middle" font-size="15" font-weight="800" class="{f}">{ad}</text>'
        for i, satir in enumerate(tanim):
            if satir:
                ic += f'<text x="{x + 10}" y="{150 + i * 16}" font-size="11.5" class="g-y">{satir}</text>'
        ic += f'<text x="{x + 10}" y="{211}" font-size="11" font-weight="800" class="{f}">Örnek</text>'
        for i, satir in enumerate(ornek):
            ic += f'<text x="{x + 10}" y="{228 + i * 16}" font-size="11.5" class="g-y">{satir}</text>'
    ic += '<text x="236" y="288" text-anchor="middle" font-size="12.5" class="g-s">İletişim bazen yüz yüze, bazen teknolojik araçlarla kurulur.</text>'
    return svg(472, 298, ic, 'İletişim üç grupta incelenir: sözlü iletişim (ses ve sözcüklerle konuşarak), yazılı iletişim (yazı aracılığıyla), sözsüz iletişim (jest, mimik, beden hareketi, kıyafet); her biri için bir örnek')


def ben_sen_dili():
    ic = ''
    sutun = [(16, 'Ben dili', ('g-ya', 'g-ys', 'g-yf'), '✓', ('Olumlu ve yapıcıdır.', 'Davranışı merkeze alır.', ('Kişi iletişim kurmaya', 'açık olur.'), 'Benlik saygısını destekler.'), ('“Sözüm kesildiğinde', 'anlatacaklarımı unutuyorum.”')),
             (244, 'Sen dili', ('g-ta', 'g-ts', 'g-tf'), '✗', ('Olumsuz ve suçlayıcıdır.', 'Kişiyi hedef alır.', ('Karşıdakinin iletişimden', 'kaçınmasına yol açar.'), 'Benlik saygısını zedeler.'), ('“Sen hep sözümü', 'kesiyorsun!”'))]
    for x, ad, (a, s, f), isaret, madde, ornek in sutun:
        ic += f'<rect x="{x}" y="10" width="212" height="226" rx="12" class="{a}"/><rect x="{x}" y="10" width="212" height="226" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 106}" y="36" text-anchor="middle" font-size="16" font-weight="800" class="{f}">{ad}</text>'
        y = 62
        for m in madde:
            satirlar = m if isinstance(m, tuple) else (m,)
            ic += f'<text x="{x + 12}" y="{y}" font-size="13" font-weight="800" class="{f}">{isaret}</text>'
            for satir in satirlar:
                ic += f'<text x="{x + 30}" y="{y}" font-size="12" class="g-y">{satir}</text>'
                y += 17
            y += 5
        ic += f'<rect x="{x + 10}" y="170" width="192" height="54" rx="9" class="g-z"/>'
        ic += f'<text x="{x + 106}" y="193" text-anchor="middle" font-size="12" font-style="italic" class="g-y">{ornek[0]}</text>'
        ic += f'<text x="{x + 106}" y="211" text-anchor="middle" font-size="12" font-style="italic" class="g-y">{ornek[1]}</text>'
    ic += '<text x="236" y="262" text-anchor="middle" font-size="12.5" class="g-s">Ben dili duyguyu anlatır; sen dili kişiyi suçlar.</text>'
    return svg(472, 272, ic, 'Ben dili ile sen dili karşılaştırması. Ben dili: olumlu ve yapıcı, davranışı merkeze alır, kişi iletişime açık olur, benlik saygısını destekler. Sen dili: olumsuz ve suçlayıcı, kişiyi hedef alır, iletişimden kaçınmaya yol açar, benlik saygısını zedeler')


def sosyal7(o):
    for b in o['bolumler']:
        if b['baslik'] == 'İletişim ve iletişimin yolları':
            b['gorsel'] = iletisim_turleri()
        elif b['baslik'] == 'Ben dili ve sen dili':
            b['gorsel'] = ben_sen_dili()


# ---------- 5. sınıf Türkçe: tahmin etme, görsel unsurlar, cümleyi genişletme ----------
def tahmin_dongusu():
    ic = '<defs>' + ok_isareti('okTD', 'g-c') + '</defs>'
    kutu = [(16, 12, '1. Başlamadan önce', ('Başlığa ve görsellere bak,', 'içeriği tahmin et.'), ('g-ma', 'g-ms', 'g-mf')),
            (256, 12, '2. Gerekçeni söyle', ('Tahminini hangi ipucuna', 'dayandırdığını açıkla.'), ('g-ya', 'g-ys', 'g-yf')),
            (256, 130, '3. Okurken, dinlerken', ('Durduğun yerlerde sonraki', 'bölümleri tahmin et.'), ('g-ta', 'g-ts', 'g-tf')),
            (16, 130, '4. Kontrol et', ('Tahminin doğru çıktı mı?', 'Nedenini düşün.'), ('g-oa', 'g-os', 'g-of'))]
    for x, y, bas, satir, (a, s, f) in kutu:
        ic += f'<rect x="{x}" y="{y}" width="200" height="84" rx="12" class="{a}"/><rect x="{x}" y="{y}" width="200" height="84" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 14}" y="{y + 28}" font-size="14.5" font-weight="800" class="{f}">{bas}</text>'
        ic += f'<text x="{x + 14}" y="{y + 52}" font-size="12.5" class="g-y">{satir[0]}</text><text x="{x + 14}" y="{y + 70}" font-size="12.5" class="g-y">{satir[1]}</text>'
    ic += '<line x1="222" y1="54" x2="248" y2="54" class="g-c" stroke-width="2.5" marker-end="url(#okTD)"/>'
    ic += '<line x1="356" y1="100" x2="356" y2="124" class="g-c" stroke-width="2.5" marker-end="url(#okTD)"/>'
    ic += '<line x1="250" y1="172" x2="224" y2="172" class="g-c" stroke-width="2.5" marker-end="url(#okTD)"/>'
    ic += '<text x="236" y="244" text-anchor="middle" font-size="12.5" class="g-s">Tahmin yaparken metindeki bilgilerle birlikte kendi bildiklerinden de yararlan.</text>'
    return svg(472, 254, ic, 'Tahmin etme stratejisinin dört adımı: 1. başlamadan önce başlığa ve görsellere bakıp tahmin et, 2. gerekçeni söyle, 3. okurken ve dinlerken sonraki bölümleri tahmin et, 4. tahminini kontrol et')


def sokak_oyunlari_grafigi():
    ic = '<text x="236" y="22" text-anchor="middle" font-size="14.5" font-weight="800" class="g-y">5/A Sınıfının En Sevdiği Sokak Oyunları</text>'
    x0, olcek = 120, 32
    for n in range(0, 11):
        x = x0 + n * olcek
        ic += f'<line x1="{x}" y1="38" x2="{x}" y2="200" class="g-c" stroke-width="{1.4 if n == 0 else 0.6}"/>'
        if n % 2 == 0:
            ic += f'<text x="{x}" y="218" text-anchor="middle" font-size="12" class="g-s">{n}</text>'
    veri = [('Seksek', 6, 'g-mf'), ('Saklambaç', 9, 'g-tf'), ('Körebe', 4, 'g-yf'), ('Yakalamaca', 7, 'g-of')]
    for i, (ad, v, f) in enumerate(veri):
        y = 48 + i * 38
        ic += f'<text x="{x0 - 10}" y="{y + 18}" text-anchor="end" font-size="13" class="g-y">{ad}</text>'
        ic += f'<rect x="{x0}" y="{y}" width="{v * olcek}" height="26" rx="5" class="{f}"/>'
        ic += f'<text x="{x0 + v * olcek + 8}" y="{y + 18}" font-size="13" font-weight="800" class="{f}">{v}</text>'
    ic += '<text x="280" y="240" text-anchor="middle" font-size="12.5" class="g-s">Öğrenci sayısı</text>'
    return svg(472, 250, ic, 'Çubuk grafik: 5/A sınıfının en sevdiği sokak oyunları. Seksek 6, saklambaç 9, körebe 4, yakalamaca 7 öğrenci')


def cumle_merdiveni():
    satirlar = [([('Ece koşuyor.', 0)], ''),
                ([('Ece ', 0), ('parkta', 1), (' koşuyor.', 0)], 'nerede?'),
                ([('Ece ', 0), ('sabah', 1), (' parkta koşuyor.', 0)], 'ne zaman?'),
                ([('Ece sabah parkta ', 0), ('köpeğiyle', 1), (' koşuyor.', 0)], 'kiminle?'),
                ([('Ece sabah parkta köpeğiyle ', 0), ('yarışmak için', 1), (' koşuyor.', 0)], 'ne için?')]
    ic = ''
    for i, (parca, soru) in enumerate(satirlar):
        y = 10 + i * 42
        ic += f'<rect x="{16 + i * 10}" y="{y}" width="{440 - i * 10}" height="32" rx="9" class="g-ma"/><rect x="{16 + i * 10}" y="{y}" width="{440 - i * 10}" height="32" rx="9" class="g-ms" stroke-width="1.5"/>'
        ic += f'<text x="{28 + i * 10}" y="{y + 21}" font-size="13.5" class="g-y">'
        for yazi, yeni in parca:
            ic += f'<tspan class="g-tf" font-weight="800">{yazi}</tspan>' if yeni else f'<tspan>{yazi}</tspan>'
        ic += '</text>'
        if soru:
            ic += f'<text x="446" y="{y + 21}" text-anchor="end" font-size="12" font-style="italic" class="g-s">{soru}</text>'
    ic += '<text x="236" y="236" text-anchor="middle" font-size="12.5" class="g-s">Turuncu kelimeler her adımda eklenen yeni ayrıntıdır.</text>'
    return svg(472, 246, ic, 'Cümleyi genişletme: Ece koşuyor. Ece parkta koşuyor. Ece sabah parkta koşuyor. Ece sabah parkta köpeğiyle koşuyor. Ece sabah parkta köpeğiyle yarışmak için koşuyor.')


def turkce5(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Tahmin etme stratejisi':
            b['gorsel'] = tahmin_dongusu()
        elif b['baslik'] == 'Görsel unsurlar':
            b['gorsel'] = sokak_oyunlari_grafigi()
        elif b['baslik'] == 'Hazırlıksız konuşma ve cümleyi genişletme':
            b['gorsel'] = cumle_merdiveni()


# ---------- 6. sınıf Türkçe: Kaşgarlı Mahmut, göz uygulamaları ----------
def kelime_seyyahi():
    ic = '<defs>' + ok_isareti('okKS', 'g-c') + '</defs>'
    adim = [(16, 'Merak', ('Her şeyin nedenini', 'araştırır: “Neden', 'tepük denmiş?”'), ('g-ma', 'g-ms', 'g-mf')),
            (170, 'Yolculuk', ('Türk boylarını bir', 'uçtan bir uca', 'gezer.'), ('g-ya', 'g-ys', 'g-yf')),
            (324, 'Sözlük', ('Dîvânu Lugâti’t-Türk:', 'Türkçenin ilk', 'sözlüğü'), ('g-ta', 'g-ts', 'g-tf'))]
    for x, bas, satir, (a, s, f) in adim:
        ic += f'<rect x="{x}" y="12" width="132" height="112" rx="12" class="{a}"/><rect x="{x}" y="12" width="132" height="112" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 66}" y="38" text-anchor="middle" font-size="15" font-weight="800" class="{f}">{bas}</text>'
        for i, y in enumerate(satir):
            ic += f'<text x="{x + 66}" y="{62 + i * 18}" text-anchor="middle" font-size="12" class="g-y">{y}</text>'
    ic += '<line x1="150" y1="68" x2="166" y2="68" class="g-c" stroke-width="2.5" marker-end="url(#okKS)"/>'
    ic += '<line x1="304" y1="68" x2="320" y2="68" class="g-c" stroke-width="2.5" marker-end="url(#okKS)"/>'
    ic += '<rect x="170" y="146" width="286" height="92" rx="12" class="g-oa"/><rect x="170" y="146" width="286" height="92" rx="12" class="g-os" stroke-width="2"/>'
    ic += '<line x1="390" y1="126" x2="390" y2="142" class="g-c" stroke-width="2.5" marker-end="url(#okKS)"/>'
    ic += '<text x="184" y="170" font-size="13.5" font-weight="800" class="g-of">Sözlükte neler var?</text>'
    for i, y in enumerate(['7500 kelime', 'Atasözü ve deyim örnekleri', 'Türk boyları ve damgaları (Kayı, Bayat…)']):
        ic += f'<circle cx="190" cy="{188 + i * 18}" r="3.5" class="g-of"/><text x="200" y="{192 + i * 18}" font-size="12" class="g-y">{y}</text>'
    ic += '<text x="16" y="170" font-size="13.5" font-weight="800" class="g-mf">Kaşgarlı Mahmut</text>'
    ic += '<text x="16" y="190" font-size="12" class="g-s">Kelimelere meraklı</text><text x="16" y="207" font-size="12" class="g-s">bir “kelime seyyahı”</text>'
    return svg(472, 248, ic, 'Kaşgarlı Mahmut: merak, Türk boylarını gezme, Türkçenin ilk sözlüğü Dîvânu Lugâti’t-Türk. Sözlükte 7500 kelime, atasözü ve deyim örnekleri, Türk boyları ve damgaları var')


def goz_uygulamalari():
    ic = '<defs>' + ok_isareti('okGU', 'g-mf') + '</defs>'
    kart = [(16, ('Sola,', 'sonra sağa')), (130, ('Yukarı,', 'sonra aşağı')), (244, ('Gözle', '“0” çiz')), (358, ('Gözle yatay', '“8” çiz'))]
    for i, (x, ad) in enumerate(kart):
        ic += f'<rect x="{x}" y="12" width="98" height="132" rx="12" class="g-ma"/><rect x="{x}" y="12" width="98" height="132" rx="12" class="g-ms" stroke-width="2"/>'
        cx, cy = x + 49, 70
        ic += f'<ellipse cx="{cx}" cy="{cy}" rx="20" ry="12" class="g-z"/><ellipse cx="{cx}" cy="{cy}" rx="20" ry="12" class="g-ms" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="6" class="g-mf"/>'
        if i == 0:
            ic += f'<line x1="{cx - 26}" y1="{cy}" x2="{cx - 42}" y2="{cy}" class="g-ms" stroke-width="2.5" marker-end="url(#okGU)"/><line x1="{cx + 26}" y1="{cy}" x2="{cx + 42}" y2="{cy}" class="g-ms" stroke-width="2.5" marker-end="url(#okGU)"/>'
        elif i == 1:
            ic += f'<line x1="{cx}" y1="{cy - 16}" x2="{cx}" y2="{cy - 34}" class="g-ms" stroke-width="2.5" marker-end="url(#okGU)"/><line x1="{cx}" y1="{cy + 16}" x2="{cx}" y2="{cy + 34}" class="g-ms" stroke-width="2.5" marker-end="url(#okGU)"/>'
        elif i == 2:
            ic += f'<ellipse cx="{cx}" cy="{cy}" rx="34" ry="30" class="g-ts" stroke-width="2" stroke-dasharray="5 4"/>'
        else:
            ic += f'<path d="M{cx} {cy} C{cx + 12} {cy - 26} {cx + 44} {cy - 26} {cx + 44} {cy} C{cx + 44} {cy + 26} {cx + 12} {cy + 26} {cx} {cy} C{cx - 12} {cy - 26} {cx - 44} {cy - 26} {cx - 44} {cy} C{cx - 44} {cy + 26} {cx - 12} {cy + 26} {cx} {cy}Z" class="g-ts" stroke-width="2" stroke-dasharray="5 4"/>'
        ic += f'<text x="{cx}" y="120" text-anchor="middle" font-size="12" font-weight="800" class="g-mf">{ad[0]}</text><text x="{cx}" y="135" text-anchor="middle" font-size="12" font-weight="800" class="g-mf">{ad[1]}</text>'
    ic += '<text x="236" y="170" text-anchor="middle" font-size="12.5" class="g-s">Başını oynatmadan yalnız gözlerini hareket ettir; her hareketi 15 saniye sürdür.</text>'
    return svg(472, 180, ic, 'Göz uygulamaları: sola sonra sağa bakma, yukarı sonra aşağı bakma, gözle 0 çizme, gözle yatay 8 çizme; her biri 15 saniye, baş oynatılmadan')


def turkce6(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Kaşgarlı Mahmut ve ilk Türkçe sözlük':
            b['gorsel'] = kelime_seyyahi()
        elif b['baslik'] == 'Tahmin ederek ve akıcı okuma':
            b['gorsel'] = goz_uygulamalari()


# ---------- 7. sınıf Türkçe: noktalı virgül, e-posta ----------
def noktali_virgul():
    satir = [('Virgüllü sıralı cümleleri ayırır', [('Erken kalktı, kahvaltısını yaptı', 0), (';', 1), (' okula koştu.', 0)], ('g-ma', 'g-ms', 'g-mf')),
             ('Virgülle ayrılmış takımları ayırır', [('Bahçede elma, armut', 0), (';', 1), (' bostanda biber, fasulye var.', 0)], ('g-ya', 'g-ys', 'g-yf')),
             ('Özneyi sıralı ögelerden ayırır', [('Başarı', 0), (';', 1), (' sabır, emek ve düzenli çalışmayla gelir.', 0)], ('g-oa', 'g-os', 'g-of'))]
    ic = ''
    for i, (bas, parca, (a, s, f)) in enumerate(satir):
        y = 12 + i * 76
        ic += f'<rect x="16" y="{y}" width="440" height="64" rx="12" class="{a}"/><rect x="16" y="{y}" width="440" height="64" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<circle cx="38" cy="{y + 22}" r="11" class="{f}"/><text x="38" y="{y + 27}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="58" y="{y + 27}" font-size="13.5" font-weight="800" class="{f}">{bas}</text>'
        ic += f'<text x="30" y="{y + 51}" font-size="13" class="g-y">'
        for yazi, vurgu in parca:
            ic += f'<tspan class="g-tf" font-weight="800" font-size="16">{yazi}</tspan>' if vurgu else f'<tspan>{yazi}</tspan>'
        ic += '</text>'
    return svg(472, 242, ic, 'Noktalı virgülün üç görevi: 1. virgüllü sıralı cümleleri ayırır, 2. virgülle ayrılmış takımları ayırır, 3. özneyi sıralı ögelerden ayırır; her biri için örnek cümle')


def eposta_sablonu():
    ic = '<rect x="16" y="10" width="300" height="262" rx="12" class="g-z"/><rect x="16" y="10" width="300" height="262" rx="12" class="g-ms" stroke-width="2"/>'
    ic += '<rect x="16" y="10" width="300" height="30" rx="12" class="g-ma"/><text x="30" y="30" font-size="12.5" font-weight="800" class="g-mf">Yeni ileti</text>'
    satir = [(58, 'Alıcı: iletisim@belediye.bel.tr', 'g-s'), (78, 'Konu: Okul önündeki yaya geçidi', 'g-y'), (98, 'Ek: yaya-gecidi.jpg', 'g-s'),
             (126, 'Merhaba,', 'g-y'), (148, 'Ben Ada Er, 7. sınıf öğrencisiyim.', 'g-y'), (170, 'Okulumuzun önündeki yaya geçidinin', 'g-y'),
             (186, 'çizgileri silinmiş, sürücüler fark etmiyor.', 'g-y'), (208, 'Çizgilerin yenilenmesini öneriyorum;', 'g-y'),
             (224, 'böylece öğrenciler güvenle geçebilir.', 'g-y'), (246, 'Bilgilerinize sunarım. Saygılarımla, Ada Er', 'g-y')]
    for y, s, c in satir:
        ic += f'<text x="28" y="{y}" font-size="11.5" class="{c}">{s}</text>'
    ic += '<line x1="24" y1="108" x2="308" y2="108" class="g-c" stroke-width="1"/>'
    etiket = [(78, 'Konu ve ek', 'g-mf'), (126, 'Selam', 'g-yf'), (148, 'Kendini tanıtma', 'g-yf'), (178, 'Sorun', 'g-tf'), (216, 'Öneri ve gerekçe', 'g-of'), (246, 'Kapanış ve ad', 'g-yf')]
    for y, ad, c in etiket:
        ic += f'<line x1="318" y1="{y - 4}" x2="334" y2="{y - 4}" class="g-c" stroke-width="1.5"/><circle cx="338" cy="{y - 4}" r="3" class="{c}"/>'
        ic += f'<text x="346" y="{y}" font-size="12" font-weight="800" class="{c}">{ad}</text>'
    return svg(472, 282, ic, 'Bir sorunu bildiren e-posta örneği ve bölümleri: konu ve ek, selam, kendini tanıtma, sorun, öneri ve gerekçe, kapanış ve ad')


def turkce7(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Noktalı virgülün görevleri':
            b['gorsel'] = noktali_virgul()
        elif b['baslik'] == 'Bir sorun için e-posta yazmak':
            b['gorsel'] = eposta_sablonu()


# ---------- 5. sınıf Din Kültürü: evrendeki düzen ----------
def insan_evren_donguleri():
    ic = ''
    sutun = [(16, 'İnsan vücudunda', ('Solunum', 'Sindirim', 'Dolaşım'), 'Susayınca su içme ihtiyacı', ('g-ma', 'g-ms', 'g-mf')),
             (256, 'Evrende', ('Suyun döngüsü', 'Mevsimlerin oluşumu', 'Gece ile gündüzün değişimi'), 'Su ihtiyacını karşılayan su döngüsü', ('g-ya', 'g-ys', 'g-yf'))]
    for x, bas, madde, ornek, (a, s, f) in sutun:
        ic += f'<rect x="{x}" y="12" width="200" height="196" rx="12" class="{a}"/><rect x="{x}" y="12" width="200" height="196" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<text x="{x + 100}" y="38" text-anchor="middle" font-size="15" font-weight="800" class="{f}">{bas}</text>'
        for i, m in enumerate(madde):
            ic += f'<circle cx="{x + 20}" cy="{62 + i * 24}" r="4" class="{f}"/><text x="{x + 32}" y="{66 + i * 24}" font-size="12.5" class="g-y">{m}</text>'
        ic += f'<rect x="{x + 10}" y="140" width="180" height="56" rx="9" class="g-z"/>'
        k = ornek.split(' ')
        ic += f'<text x="{x + 100}" y="163" text-anchor="middle" font-size="12" class="g-y">{" ".join(k[:3])}</text><text x="{x + 100}" y="181" text-anchor="middle" font-size="12" class="g-y">{" ".join(k[3:])}</text>'
    ic += '<circle cx="236" cy="110" r="16" class="g-tf"/><text x="236" y="115" text-anchor="middle" font-size="15" font-weight="800" class="g-b">=</text>'
    ic += '<text x="236" y="236" text-anchor="middle" font-size="12.5" class="g-s">İkisinde de her şey bir düzen içinde işler ve denge korunur.</text>'
    return svg(472, 246, ic, 'İnsan vücudunda solunum, sindirim, dolaşım; evrende suyun döngüsü, mevsimlerin oluşumu, gece ile gündüzün değişimi. Susayınca su içme ihtiyacı ile su döngüsü benzer; ikisinde de denge korunur')


def din5(o):
    for b in o['bolumler']:
        if b['baslik'] == 'İnsan vücudu ve evrendeki düzen':
            b['gorsel'] = insan_evren_donguleri()


# ---------- 5. sınıf İngilizce: okul kuralları levhaları ----------
def okul_kurallari():
    ic = ''
    levha = [(16, 'Don’t run', 'in the classroom.', 'kosu'), (130, 'Don’t shout', 'in the library.', 'ses'),
             (244, 'You mustn’t', 'chew gum.', 'sakiz'), (358, 'Line up,', 'nice and straight!', 'sira')]
    for x, s1, s2, tur in levha:
        cx, cy = x + 49, 62
        yasak = tur != 'sira'
        ic += f'<rect x="{x}" y="12" width="98" height="150" rx="12" class="{"g-ta" if yasak else "g-ya"}"/><rect x="{x}" y="12" width="98" height="150" rx="12" class="{"g-ts" if yasak else "g-ys"}" stroke-width="2"/>'
        ic += f'<circle cx="{cx}" cy="{cy}" r="34" class="g-z"/><circle cx="{cx}" cy="{cy}" r="34" class="{"g-ts" if yasak else "g-ys"}" stroke-width="5"/>'
        if tur == 'kosu':
            ic += f'<circle cx="{cx + 6}" cy="{cy - 18}" r="5" class="g-mf"/><path d="M{cx + 4} {cy - 11}L{cx - 2} {cy + 6}M{cx - 2} {cy + 6}L{cx - 12} {cy + 18}M{cx - 2} {cy + 6}L{cx + 10} {cy + 16}M{cx + 2} {cy - 4}L{cx - 12} {cy - 6}M{cx + 2} {cy - 4}L{cx + 14} {cy + 2}" class="g-ms" stroke-width="4" stroke-linecap="round" fill="none"/>'
        elif tur == 'ses':
            ic += f'<path d="M{cx - 16} {cy - 6}h8l10 -9v30l-10 -9h-8z" class="g-mf"/><path d="M{cx + 8} {cy - 8}q6 8 0 16M{cx + 13} {cy - 13}q10 13 0 26" class="g-ms" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
        elif tur == 'sakiz':
            ic += f'<circle cx="{cx}" cy="{cy}" r="14" class="g-of"/><circle cx="{cx - 5}" cy="{cy - 5}" r="4" class="g-z"/>'
        else:
            for i in range(3):
                ic += f'<circle cx="{cx - 16 + i * 16}" cy="{cy - 8}" r="5" class="g-mf"/><rect x="{cx - 21 + i * 16}" y="{cy - 1}" width="10" height="18" rx="4" class="g-mf"/>'
        if yasak:
            ic += f'<line x1="{cx - 24}" y1="{cy + 24}" x2="{cx + 24}" y2="{cy - 24}" class="g-ts" stroke-width="5" stroke-linecap="round"/>'
        f = 'g-tf' if yasak else 'g-yf'
        ic += f'<text x="{cx}" y="124" text-anchor="middle" font-size="12" font-weight="800" class="{f}">{s1}</text><text x="{cx}" y="141" text-anchor="middle" font-size="11.5" class="g-y">{s2}</text>'
    ic += '<text x="236" y="186" text-anchor="middle" font-size="12.5" class="g-s">Don’t run = You mustn’t run = You can’t run</text>'
    return svg(472, 196, ic, 'Okul kuralları levhaları: Don’t run in the classroom, Don’t shout in the library, You mustn’t chew gum, Line up nice and straight')


def ingilizce5(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Rules at school':
            b['gorsel'] = okul_kurallari()


# ---------- 6. sınıf İngilizce: sıklık zarfları ----------
def siklik_zarflari():
    ic = ''
    zarf = [('always', 'her zaman', 5), ('usually', 'genellikle', 4), ('often', 'sık sık', 3), ('sometimes', 'bazen', 2), ('never', 'asla', 0)]
    for i, (en, tr, n) in enumerate(zarf):
        x = 16 + i * 90
        ic += f'<rect x="{x}" y="12" width="80" height="116" rx="12" class="g-ma"/><rect x="{x}" y="12" width="80" height="116" rx="12" class="g-ms" stroke-width="2"/>'
        ic += f'<text x="{x + 40}" y="38" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">{en}</text>'
        ic += f'<text x="{x + 40}" y="56" text-anchor="middle" font-size="11.5" class="g-s">{tr}</text>'
        for k in range(5):
            cy = 110 - k * 11
            ic += f'<rect x="{x + 28}" y="{cy - 8}" width="24" height="8" rx="3" class="{"g-tf" if k < n else "g-z"}"/>'
    ic += '<text x="236" y="152" text-anchor="middle" font-size="12.5" class="g-y">I <tspan class="g-tf" font-weight="800">always</tspan> walk to school. She <tspan class="g-tf" font-weight="800">never</tspan> takes the bus.</text>'
    ic += '<text x="236" y="172" text-anchor="middle" font-size="12" class="g-s">Sıklık zarfı fiilden önce gelir.</text>'
    return svg(472, 182, ic, 'Sıklık zarfları çoktan aza: always, usually, often, sometimes, never. Örnek: I always walk to school. She never takes the bus.')


def ingilizce6(o):
    for b in o['bolumler']:
        if b['baslik'] == 'Routines and frequency':
            b['gorsel'] = siklik_zarflari()


if __name__ == '__main__':
    yaz('5-matematik-1.json', mat5)
    yaz('8-matematik-1.json', mat8)
    if (OZET / '6-matematik-1.json').exists():
        yaz('6-matematik-1.json', mat6)
    if (OZET / '7-matematik-1.json').exists():
        yaz('7-matematik-1.json', mat7)
    if (OZET / '5-fen-bilimleri-2.json').exists():
        yaz('5-fen-bilimleri-2.json', fen5)
    if (OZET / '6-fen-bilimleri-1.json').exists():
        yaz('6-fen-bilimleri-1.json', fen6)
    if (OZET / '7-fen-bilimleri-1.json').exists():
        yaz('7-fen-bilimleri-1.json', fen7)
    if (OZET / '5-sosyal-bilgiler-1.json').exists():
        yaz('5-sosyal-bilgiler-1.json', sosyal5)
    if (OZET / '6-sosyal-bilgiler-1.json').exists():
        yaz('6-sosyal-bilgiler-1.json', sosyal6)
    if (OZET / '7-sosyal-bilgiler-1.json').exists():
        yaz('7-sosyal-bilgiler-1.json', sosyal7)
    if (OZET / '5-turkce-1.json').exists():
        yaz('5-turkce-1.json', turkce5)
    if (OZET / '6-turkce-1.json').exists():
        yaz('6-turkce-1.json', turkce6)
    if (OZET / '7-turkce-1.json').exists():
        yaz('7-turkce-1.json', turkce7)
    if (OZET / '5-din-kulturu-ve-ahlak-bilgisi-1.json').exists():
        yaz('5-din-kulturu-ve-ahlak-bilgisi-1.json', din5)
    if (OZET / '5-ingilizce-4.json').exists():
        yaz('5-ingilizce-4.json', ingilizce5)
    if (OZET / '6-ingilizce-4.json').exists():
        yaz('6-ingilizce-4.json', ingilizce6)
    print('görseller yazıldı')
