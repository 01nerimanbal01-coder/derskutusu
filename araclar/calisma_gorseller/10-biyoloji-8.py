# -*- coding: utf-8 -*-
"""10-biyoloji-8 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="width:100%;max-height:24mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 80, 78, a, c, 6, 0.75)
        ic += yazi(x + 40, 44, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 72}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 69, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, c1)
    ic += kutu(12, 26, 162, 78, a1, c1, 6, 0.75)
    ic += yazi(93, 44, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="52" x2="164" y2="52" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 70, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 89, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 26, 162, 78, a2, c2, 6, 0.75)
    ic += yazi(267, 44, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="52" x2="338" y2="52" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 70, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 89, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 26, 108, 78, a, c, 6, 0.75)
        ic += yazi(x + 54, 44, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 100}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 70, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 89, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM, arka_renk=CAM_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 78, 78, a, c, 6, 0.75)
        ic += yazi(x + 39, 44, b, 8.3, c)
        ic += yazi(x + 39, 68, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39, 88, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+80},64 {x+85},60 {x+85},68" fill="{ana_renk}"/>'
    return svg(ic, etiket)


def g0():
    return kart4('CANLILARDA SİNDİRİM TEMEL KAVRAMLARI', [
        ('Mekanik Sindirim', 'Enzim ve su yok', 'Diş, safra, taşlık'),
        ('Kimyasal (Hidroliz)', 'Enzim + Su kullanılır', 'Bağlar kopar, ATP yok'),
        ('Sindirim Kofulu', 'Besin kofulu + Lizozom', 'Hücre içi sindirim'),
        ('Gastrovasküler', 'Tek açıklıklı boşluk', 'Hidra ve planarya')
    ], '10-biyoloji-8 sindirim kavramları')

def g1():
    return kart4('SUBSTRAT YÜZEYİ VE ENZİM ETKİNLİĞİ DENEYİ', [
        ('1. Tüp (0 °C)', 'Tüm et + Su', 'Enzim yok -> Sindirim yok'),
        ('2. Tüp (37 °C)', 'Parça et + Pepsin', 'Yavaş kimyasal sindirim'),
        ('3. Tüp (37 °C)', 'Kıyma + Pepsin + Su', 'En hızlı sindirim!'),
        ('4. Tüp (90 °C)', 'Kıyma + Enzim', 'Enzim denatüre olur')
    ], '10-biyoloji-8 deney tüpleri')

def g2():
    return karsilastir2('MEKANİK VE KİMYASAL SİNDİRİM KARŞILAŞTIRMASI',
        'Mekanik (Fiziksel) Sindirim', 'Enzim ve su kullanılmaz, bağ kopmaz', 'Besin yüzey alanını artırır (Safra, diş)',
        'Kimyasal Sindirim (Hidroliz)', 'Su ve hidrolitik enzimlerle bağ kopar', 'Polimer -> Monomer (ATP harcanmaz)',
        '10-biyoloji-8 mekanik ve kimyasal sindirim')

def g4():
    return karsilastir2('HÜCRE İÇİ VE HÜCRE DIŞI SİNDİRİM',
        'Hücre İçi Sindirim', 'Endositoz -> Besin kofulu + Lizozom', 'Amip, öglena, paramesyum, sünger, akyuvar',
        'Hücre Dışı Sindirim (Daha Avantajlı)', 'Ekzositozla enzim salgılanır', 'Saprofitler, böcekçil bitki, omurgalılar',
        '10-biyoloji-8 hücre içi ve dışı sindirim')

def g6():
    return uclu_sema('HİDROLİZ (KİMYASAL SİNDİRİM) ÖZELLİKLERİ', [
        ('Karbonhidrat', 'Glikozit bağı kopar', 'Polisakkarit -> Glikoz'),
        ('Yağ (Lipit)', 'Ester bağı kopar', 'Yağ + 3 H2O -> 3 Yağ asidi'),
        ('Protein', 'Peptit bağı kopar', 'ATP harcanmaz / üretilmez')
    ], '10-biyoloji-8 hidroliz bağları')

def g7():
    return akis4('HÜCRE İÇİ SİNDİRİM (FAGOSİTOZ) BASAMAKLARI', [
        ('1. Fagositoz', 'Yalancı ayakla alma', 'Besin kofulu oluşur'),
        ('2. Birleşme', 'Besin kofulu + Lizozom', 'Sindirim kofulu'),
        ('3. Hidroliz', 'Su ve enzim etkisi', 'Monomer oluşumu'),
        ('4. Ekzositoz', 'Monomer sitoplazmaya', 'Atıklar dışarı atılır')
    ], '10-biyoloji-8 hücre içi sindirim sırası')

def g8():
    return uclu_sema('HAYVANLARDA SİNDİRİM SİSTEMİ TİPLERİ', [
        ('1. Boşluk Yok', 'Süngerler (Porifera)', 'Yalnız hücre içi'),
        ('2. Tek Açıklıklı', 'Hidra ve Planarya', 'Gastrovasküler boşluk'),
        ('3. İki Açıklıklı', 'Solucan -> Omurgalı', 'Ağız ve anüs ayrı')
    ], '10-biyoloji-8 sindirim yapıları')

def g11():
    return karsilastir2('TEK AÇIKLIKLI VE İKİ AÇIKLIKLI SİSTEM FARKI',
        'Tek Açıklıklı (Gastrovasküler)', 'Ağız ve anüs aynı açıklıktır', 'Besin ve atıklar birbirine karışır',
        'İki Açıklıklı (Sindirim Kanalı)', 'Ağızdan anüse tek yönlü akış vardır', 'Bölgeler özelleşir, sindirim verimi artar',
        '10-biyoloji-8 iki açıklıklı sistem avantajı')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[4]['gorsel'] = g4()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
