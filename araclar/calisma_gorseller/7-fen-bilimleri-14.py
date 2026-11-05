# -*- coding: utf-8 -*-
"""7-fen-bilimleri-14 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
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
        ic += kutu(x, 27, 80, 77, a, c, 6, 0.75)
        ic += yazi(x + 40, 44, b, 8.3, c)
        ic += f'<line x1="{x + 6}" y1="52" x2="{x + 74}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 69, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, r1=MAVI, a1=MAVI_A, r2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, r1, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, r1)
    ic += kutu(12, 27, 162, 77, a1, r1, 6, 0.75)
    ic += yazi(93, 45, sol_b, 8.8, r1)
    ic += yazi(93, 66, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 86, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 27, 162, 77, a2, r2, 6, 0.75)
    ic += yazi(267, 45, sag_b, 8.8, r2)
    ic += yazi(267, 66, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 86, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 27, 108, 77, a, c, 6, 0.75)
        ic += yazi(x + 54, 45, b, 8.6, c)
        ic += yazi(x + 54, 66, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 86, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.5, ana_renk)
    renkler = [MAVI, YES, TUR, MOR]
    for i, (b, d1, d2) in enumerate(adimlar):
        c = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 78, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 39, 46, b, 8.2, c)
        ic += yazi(x + 39, 67, d1, 7.4, LAC, ince=True)
        ic += yazi(x + 39, 86, d2, 7.0, SOLUK, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+80},64 {x+85},60 {x+85},68" fill="{ana_renk}"/>'
    return svg(ic, etiket)


def g0():
    return kart4('SOLUNUM SİSTEMİ ORGANLARI VE GÖREVLERİ', [('Burun', 'Mukus + Kılcal damar', 'Isıtır, nemlendirir'), ('Gırtlak', 'Ses telleri + Kapak', 'Soluk borusunu korur'), ('Alveol', 'Hava kesecikleri', 'O2 ve CO2 değişimi'), ('Diyafram', 'Çizgili solunum kası', 'Kasılır ve gevşer')], '7-fen-14 solunum organları kartları')

def g1():
    return karsilastir2('SOLUK ALMA VE SOLUK VERME MEKANİZMASI', 'I. Durum: Soluk Alma', 'Diyafram kasılır ve düzleşir', 'Göğüs boşluğu genişler, O2 dolar', 'II. Durum: Soluk Verme', 'Diyafram gevşer ve kubbeleşir', 'Göğüs boşluğu daralır, CO2 atılır', '7-fen-14 soluk alıp verme modeli')

def g2():
    return uclu_sema('SOLUK ALIP VERME SÜREÇ ANALİZİ', [('Diyafram & Kaburga', 'Alma: Kasılır (Düz)', 'Verme: Gevşer (Kubbe)'), ('Göğüs & Akciğer', 'Alma: Hacim artar', 'Verme: Hacim azalır'), ('İç Basınç & Hava', 'Alma: Basınç düşer, girer', 'Verme: Basınç artar, çıkar')], '7-fen-14 soluk mekanizması şeması')

def g5():
    return kart4('KALP-DAMAR TEDAVİ YÖNTEMLERİ (TEKNOLOJİ)', [('Anjiyo', 'Damar görüntüleme', 'Tıkanıklığı saptama'), ('Balon & Stent', 'Dar damarı açma', 'Metal kafes tüp'), ('Bypass', 'Köprüleme ameliyatı', 'Yeni damar yolu'), ('Kalp Pili', 'Elektrik uyarısı', 'Ritmi düzenleme')], '7-fen-14 dolaşım teknolojileri')

def g6():
    return karsilastir2('FEN DENEYİ: BALON VE PET ŞİŞE SOLUNUM MODELİ', 'Modeldeki Yapı Karşılıkları', 'Y Borusu: Soluk borusu ve bronşlar', 'İç Balonlar: Akciğer · Alt Zar: Diyafram', 'Alt Zar Aşağı Çekildiğinde', 'Şişe içi hacim artar, basınç düşer', 'İç balonlar şişer (Soluk alma olayı)', '7-fen-14 solunum deney düzeneği')

def g7():
    return uclu_sema('BURUNDAN NEFES ALMANIN 3 TEMEL AVANTAJI', [('1. Temizleme', 'Burun kılları ve mukus', 'Toz ve mikrobu tutar'), ('2. Nemlendirme', 'Mukus salgısı ile', 'Kuru havayı nemlendirir'), ('3. Isıtma', 'Yüzey kılcal damarları', 'Soğuk havayı ısıtır')], '7-fen-14 burun yapısı avantajları')

def g8():
    return akis4('TEMİZ HAVANIN SOLUNUM YOLU SIRALAMASI', [('1. Üst Yol', 'Burun -> Yutak', 'Isınma ve iletim'), ('2. Geçiş', 'Gırtlak -> Soluk b.', 'Kıkırdak halkalı'), ('3. Dallanma', 'Bronş -> Bronşçuk', 'Sağ (3) ve Sol (2) lob'), ('4. Gaz Değişimi', 'Alveol Kesecikleri', 'Kana O2 geçişi')], '7-fen-14 solunum yolu akışı')

def g11():
    return karsilastir2('ALVEOL VE KILCAL DAMAR ARASINDA GAZ ALIŞVERİŞİ', 'Alveolden Kılcal Damara', 'Oksijen (O2) difüzyonla kana geçer', 'Alyuvarlarla doku hücrelerine taşınır', 'Kılcal Damardan Alveole', 'Karbondioksit (CO2) alveole geçer', 'Soluk verme ile vücuttan uzaklaştırılır', '7-fen-14 alveol gaz alışverişi')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
