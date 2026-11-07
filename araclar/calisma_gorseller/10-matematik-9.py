"""10. sınıf Matematik 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu, K150 EK).

viewBox genişliği 360 birim ≈ yarım sütun (≈88 mm); 12 birimlik yazı ≈ 8,5–9 pt.
"""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def us(metin):
    return f'<tspan baseline-shift="super" font-size="70%">{metin}</tspan>'


def alt(metin):
    return f'<tspan baseline-shift="sub" font-size="70%">{metin}</tspan>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'



def f(formul, boy=None):
    """C2H6 → C₂H₆ (rakam harf/parantez ardındaysa alt simge)."""
    import re
    return re.sub(r'(?<=[A-Za-z)])(\d+)', lambda m: alt(m.group(1)), formul)


def tablo(baslik, sutunlar, satirlar, etiket, ilk=118, toplam=True):
    """İki yönlü sıklık tablosu; son satır ve son sütun toplam (koyu)."""
    n = len(sutunlar)
    w = (348 - ilk) / n
    sh = 26
    boy = 40 + sh * (len(satirlar) + 1)
    ic = kutu(2, 2, 356, boy - 4, GRI_A, GRI, 8)
    ic += yazi(180, 22, baslik, 11.5, SOLUK, ince=True)
    y0 = 32
    ic += f'<rect x="12" y="{y0}" width="336" height="{sh}" fill="{MAVI_A}"/>'
    for j, s in enumerate(sutunlar):
        ic += yazi(ilk + w * j + w / 2, y0 + 17, s, 11.5, MAVI)
    for i, sat in enumerate(satirlar):
        y = y0 + sh * (i + 1)
        son = toplam and i == len(satirlar) - 1
        ic += f'<rect x="12" y="{y}" width="336" height="{sh}" fill="{GRI_A if son else "#fff"}" stroke="{GRI}" stroke-width="0.6"/>'
        ic += yazi(20, y + 17, sat[0], 11.5, LAC, 'start', not son)
        for j, v in enumerate(sat[1:]):
            ic += yazi(ilk + w * j + w / 2, y + 17, v, 12, KIR if v == 'x' else LAC, ince=not (son or j == n - 1) and v != 'x')
    return svg(ic, 360, boy, etiket, 8 + boy * 0.24)


def yigilmis():
    ic = kutu(2, 2, 356, 176, GRI_A, GRI, 8)
    ox, oy, yuk = 52, 134, 108
    for p in (0, 50, 100):
        y = oy - yuk * p / 100
        ic += f'<line x1="{ox}" y1="{y}" x2="{ox + 200}" y2="{y}" stroke="{GRI}" stroke-width="0.5"/>' + yazi(ox - 6, y + 4, f'%{p}', 11, SOLUK, 'end', True)
    for i, ad in enumerate(('A', 'B', 'C')):
        x = ox + 18 + i * 64
        ic += f'<rect x="{x}" y="{oy - yuk}" width="40" height="{yuk * 0.65:.1f}" fill="{GRI_A}" stroke="{GRI}"/>'
        ic += f'<rect x="{x}" y="{oy - yuk * 0.35:.1f}" width="40" height="{yuk * 0.35:.1f}" fill="{YES}"/>'
        ic += yazi(x + 20, oy + 16, f'{ad} mah.', 11.5, LAC)
    ic += f'<rect x="270" y="56" width="14" height="14" fill="{YES}"/>' + yazi(290, 67, 'Yapıyor', 11.5, LAC, 'start', True)
    ic += f'<rect x="270" y="80" width="14" height="14" fill="{GRI_A}" stroke="{GRI}"/>' + yazi(290, 91, 'Yapmıyor', 11.5, LAC, 'start', True)
    ic += yazi(180, 170, 'Hanelerin geri dönüşüm yapma durumu (%)', 11, SOLUK, ince=True)
    return svg(ic, 360, 180, 'Üç mahallede geri dönüşüm yapan hanelerin yüzdelik dağılımı', 44)


def cubuk(veri, baslik, etiket, en_fazla, birim='%'):
    ic = kutu(2, 2, 356, 164, GRI_A, GRI, 8)
    ox, oy, yuk = 40, 120, 86
    ic += f'<line x1="{ox}" y1="{oy}" x2="346" y2="{oy}" stroke="{LAC}"/>'
    ic += yazi(180, 20, baslik, 11.5, SOLUK, ince=True)
    gw = 300 / len(veri)
    for i, (grup, cubuklar) in enumerate(veri):
        gx = ox + i * gw
        bw = (gw - 30) / len(cubuklar)
        for j, (deger, renk) in enumerate(cubuklar):
            h = yuk * deger / en_fazla
            x = gx + 15 + j * bw
            ic += f'<rect x="{x:.1f}" y="{oy - h:.1f}" width="{bw - 6:.1f}" height="{h:.1f}" rx="2" fill="{renk}"/>'
            ic += yazi(x + (bw - 6) / 2, oy - h - 4, f'{birim}{deger}' if birim == '%' else f'{deger}', 11.5, renk)
        ic += yazi(gx + gw / 2, oy + 16, grup, 11.5, LAC)
    return ic


def kutuphane():
    ic = cubuk([('Evde kütüphane var', [(68, MAVI)]), ('Evde kütüphane yok', [(41, TUR)])],
               'Sınavda başarılı olan öğrencilerin oranı', '', 100)
    ic += yazi(180, 156, 'Koşullu göreli sıklık (satır yüzdesi)', 11, SOLUK, ince=True)
    return svg(ic, 360, 168, 'Evinde kütüphane olan ve olmayan öğrencilerin başarı yüzdeleri', 40)


def salon():
    ic = cubuk([('Yetişkin (50 kişi)', [(30, MAVI), (20, TUR)]), ('Genç (150 kişi)', [(45, MAVI), (105, TUR)])],
               'Antrenman saati tercihi (kişi sayısı)', '', 110, birim='')
    ic += f'<rect x="96" y="146" width="12" height="12" fill="{MAVI}"/>' + yazi(112, 156, 'Sabah', 11.5, LAC, 'start', True)
    ic += f'<rect x="196" y="146" width="12" height="12" fill="{TUR}"/>' + yazi(212, 156, 'Akşam', 11.5, LAC, 'start', True)
    return svg(ic, 360, 168, 'Yetişkin ve gençlerin antrenman saati tercihleri', 40)


def anket_karti():
    satir = [('Araştırma sorusu', 'Kantin fiyatları uygun bulunuyor mu?'),
             ('Örneklem', 'Kantinde sıra bekleyen ilk 40 öğrenci'),
             ('Bulgu', '40 öğrenciden 34\'ü memnun (%85)'),
             ('Rapor', '"Okulun %85\'i kantinden memnundur."')]
    ic = kutu(2, 2, 356, 22 + 32 * len(satir), GRI_A, GRI, 8)
    for i, (a, b) in enumerate(satir):
        y = 12 + 32 * i
        ic += kutu(12, y, 336, 28, '#fff', GRI, 4)
        ic += yazi(20, y + 18, a, 11, MAVI, 'start') + yazi(124, y + 18, b, 10.5, LAC, 'start', True)
    return svg(ic, 360, 26 + 32 * len(satir), 'Kantin memnuniyeti araştırmasının özeti', 36)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = tablo('Bilim kulübü üyeliği ve kitap okuma', ['Düzenli okur', 'Okumaz', 'Toplam'],
                           [['Kulüp üyesi', '42', '18', '60'], ['Üye değil', '56', '84', '140'], ['Toplam', '98', '102', '200']],
                           'Kulüp üyeliği ile kitap okuma alışkanlığı tablosu')
    s[3]['gorsel'] = yigilmis()
    s[5]['gorsel'] = kutuphane()
    s[7]['gorsel'] = salon()
    s[9]['gorsel'] = anket_karti()
    s[10]['gorsel'] = tablo('Konut türü ve sebze yetiştirme', ['Yetiştirir', 'Yetiştirmez', 'Toplam'],
                            [['Bahçeli ev', '54', '66', '120'], ['Apartman', '27', '153', '180'], ['Toplam', '81', '219', '300']],
                            'Konut türü ile sebze yetiştirme tablosu')
    s[11]['gorsel'] = tablo('Gruplara göre etkinliğe katılım', ['Katılır', 'Katılmaz', 'Toplam'],
                            [['A grubu', '12', '18', '30'], ['B grubu', 'x', '42', 'x + 42']],
                            'Bilinmeyen x değeri içeren iki yönlü tablo', toplam=False)
