# -*- coding: utf-8 -*-
"""10-matematik-6 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket, en_fazla=32):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 360 115"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.5, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 76, a, c, 6, 0.75)
        ic += yazi(x + 40, 48, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="58" x2="{x + 72}" y2="58" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 78, d, 7.5, LAC, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket):
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, MAVI)
    ic += kutu(14, 28, 160, 76, '#f8fafc', MAVI, 6, 0.75)
    ic += yazi(94, 48, sol_b, 9, MAVI)
    ic += yazi(94, 68, sol_d1, 8, LAC, ince=True)
    ic += yazi(94, 88, sol_d2, 7.5, SOLUK, ince=True)
    ic += kutu(186, 28, 160, 76, '#f8fafc', TUR, 6, 0.75)
    ic += yazi(266, 48, sag_b, 9, TUR)
    ic += yazi(266, 68, sag_d1, 8, LAC, ince=True)
    ic += yazi(266, 88, sag_d2, 7.5, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [MAVI, TUR, MOR]
    for i, (b, d1, d2) in enumerate(uclu):
        c = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 54, 48, b, 8.8, c)
        ic += yazi(x + 54, 68, d1, 7.8, LAC, ince=True)
        ic += yazi(x + 54, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)

def g0():
    return kart4('SİNÜS VE KOSİNÜS TEOREMLERİ ÖZETİ', [('Sinüs Teoremi', 'a/sinA = b/sinB = 2R'), ('Kosinüs Teoremi', 'a² = b² + c² - 2bc·cosA'), ('Pisagor Özel Hâli', 'A = 90° -> a² = b² + c²'), ('Bütünler Açılar', 'cos(180°-α) = -cos α')], '10-matematik-6 teoremler özeti')

def g1():
    return karsilastir2('KOSİNÜS TEOREMİ İLE KENAR HESABI', 'Verilen Elemanlar (KAK)', 'b = 5 cm, c = 8 cm, m(A) = 60°', 'cos 60° = 1/2', 'Bağıntıda Yerine Koyma', 'a² = 5² + 8² - 2 · 5 · 8 · (1/2)', 'a² = 25 + 64 - 40 = 49 -> a = 7 cm', '10-matematik-6 kosinüs hesabı')

def g2():
    return karsilastir2('KOSİNÜS TEOREMİNDEN PİSAGOR\'A GEÇİŞ', 'Genel Kosinüs Bağıntısı', 'a² = b² + c² - 2·b·c·cos A', 'Dar açıda cos A > 0, genişte cos A < 0', 'A = 90° (Dik Üçgen) Durumu', 'cos 90° = 0 olduğundan çarpım sıfırlanır', 'Doğrudan a² = b² + c² elde edilir', '10-matematik-6 Pisagor ilişkisi')

def g3():
    return uclu_sema('HANGİ DURUMDA HANGİ TEOREM SEÇİLİR?', [('İki Açı + Bir Kenar', 'AÇK verilen üçgenler', 'Sinüs Teoremi uygulanır'), ('İki Kenar + Aradaki Açı', 'KAK verilen üçgenler', 'Kosinüs Teoremi uygulanır'), ('Üç Kenar Uzunluğu', 'KKK verilen üçgenler', 'Kosinüs ile açı bulunur')], '10-matematik-6 teorem seçimi')

def g5():
    return kart4('SİNÜS TEOREMİNİN İSPAT BASAMAKLARI', [('1. Dikme İndirme', 'A\'dan [BC]\'ye h çizilir'), ('2. Sol Dik Üçgen', 'sin B = h/c -> h = c·sin B'), ('3. Sağ Dik Üçgen', 'sin C = h/b -> h = b·sin C'), ('4. Eşitleme', 'b / sin B = c / sin C')], '10-matematik-6 sinüs ispatı')

def g6():
    return karsilastir2('SİNÜS TEOREMİ UYGULAMASI', 'Verilenler (İki Açı ve Bir Kenar)', 'm(A) = 30° (sin 30° = 1/2)', 'm(B) = 45° (sin 45° = √2/2), a = 6 cm', 'Oran Eşitliği (a / sin A = b / sin B)', '6 / (1/2) = b / (√2 / 2)', '12 = 2b / √2 -> b = 6√2 cm', '10-matematik-6 sinüs uygulaması')

def g8():
    return kart4('BÜTÜNLER VE ÖZEL AÇI DEĞERLERİ', [('sin 30° = sin 150°', 'Değeri: 1 / 2'), ('cos 60° = 1 / 2', 'cos 120° = -1 / 2'), ('sin 45° = sin 135°', 'Değeri: √2 / 2'), ('sin 60° = sin 120°', 'Değeri: √3 / 2')], '10-matematik-6 özel açılar')

def g11():
    return karsilastir2('ÜÇ KENARI BİLİNEN ÜÇGENDE AÇI BULMA', 'Kenarlar: a = 7, b = 3, c = 5', 'a² = b² + c² - 2·b·c·cos A', '49 = 9 + 25 - 2 · 3 · 5 · cos A', 'Açı Hesabı', '49 = 34 - 30·cos A -> 30·cos A = -15', 'cos A = -1/2 -> m(A) = 120°', '10-matematik-6 üç kenardan açı')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
