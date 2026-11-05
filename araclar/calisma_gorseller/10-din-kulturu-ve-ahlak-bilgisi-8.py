# -*- coding: utf-8 -*-
"""10-din-kulturu-ve-ahlak-bilgisi-8 çalışma kâğıdı görselleri.
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
    return kart4('ALLAH\'IN (CC) VARLIĞI VE BİRLİĞİ DELİLLERİ', [
        ('Gaye ve Nizam', 'Ölçü, uyum ve amaç', 'Mülk 3 / Kamer 49'),
        ('Hudûs ve İmkân', 'Sonradan yaratılma', 'Vâcibü\'l-Vücûd'),
        ('Ekmel ve Fıtrat', 'Mükemmel varlık fikri', 'Doğuştan inanma (Rûm 30)'),
        ('Burhân-ı Temânu', 'Karşılıklı engelleme', 'Tevhit (Enbiyâ 22)')
    ], '10-din-kulturu-ve-ahlak-bilgisi-8 deliller özeti')

def g1():
    return karsilastir2('GAYE VE NİZAM (TELEOLOJİK) DELİLİ',
        'Ayet-i Kerime Vurgusu', 'Kamer 49: Her şeyi bir ölçüye göre yarattık', 'Mülk 3: Rahmân\'ın yaratışında uyumsuzluk yok',
        'Kozmik ve Biyolojik Düzen', 'Hassas fizik sabitleri ve yaşam dengesi', 'Sonsuz ilim, irade ve kudret kanıtı',
        '10-din-kulturu-ve-ahlak-bilgisi-8 gaye ve nizam')

def g2():
    return uclu_sema('KELAM VE FELSEFEDE KOZMOLOJİK DELİLLER', [
        ('Hudûs Delili', 'Hâdis (sonradan olan)', 'Muhdis\'e (Yaratıcı) muhtaç'),
        ('İmkân Delili', 'Mümkün varlıklar', 'Vâcibü\'l-Vücûd\'a dayanır'),
        ('Teselsül İptali', 'Sonsuz zincir olamaz', 'İlk sebep Allah\'tır (cc)')
    ], '10-din-kulturu-ve-ahlak-bilgisi-8 hudus ve imkan')

def g4():
    return karsilastir2('İBN RÜŞD\'ÜN KUR\'ANÎ DELİL SİSTEMİ',
        'İnayet Delili (Uygunluk)', 'Gece-gündüz, su, atmosfer ve güneşin', 'insan yaşamına tam uygun kılınması',
        'İhtira Delili (Yoktan Yaratma)', 'Canlıların, hayatın ve bilincin', 'hiç yokken Allah tarafından icat edilmesi',
        '10-din-kulturu-ve-ahlak-bilgisi-8 inayet ve ihtira')

def g6():
    return karsilastir2('İÇ DÜNYADAN (ENFÜS) HAREKET EDEN DELİLLER',
        'Ekmel Varlık Delili (Ontolojik)', 'Kusurlu insan zihnindeki tam/mükemmel', 'varlık fikri Ekmel olan Allah\'tan gelir',
        'Fıtrat Delili (Rûm Suresi 30. Ayet)', 'İnsanın doğuştan getirdiği tertemiz', 'inanma ve Yaratıcı\'ya yönelme yeteneği',
        '10-din-kulturu-ve-ahlak-bilgisi-8 ekmel ve fıtrat')

def g7():
    return akis4('HUDÛS DELİLİNİN AKIL YÜRÜTME ZİNCİRİ', [
        ('1. Gözlem', 'Âlem sürekli değişir', 'Oluş ve bozuluş'),
        ('2. Hâdislik', 'Değişen her şey', 'sonradan olmuştur'),
        ('3. Muhtaçlık', 'Hâdis olan kendi', 'kendini yaratamaz'),
        ('4. Sonuç', 'Ezeli Yaratıcı (Muhdis)', 'Allah\'tır (cc)')
    ], '10-din-kulturu-ve-ahlak-bilgisi-8 hudus zinciri')

def g8():
    return karsilastir2('TEVHİT VE BURHÂN-I TEMÂNU (ENBİYÂ 22)',
        'Ayet-i Kerime (Enbiyâ Suresi 22)', 'Yerde ve gökte Allah\'tan başka ilahlar', 'olsaydı ikisinin de düzeni bozulurdu',
        'Mantıksal Çıkarım (Temânu)', 'İki irade çatışır, kaos doğardı', 'Düzenin birliği Yaratıcı\'nın birliğini kanıtlar',
        '10-din-kulturu-ve-ahlak-bilgisi-8 burhan-ı temanu')

def g11():
    return uclu_sema('EVRENDEKİ BİRLİK VE TEVHİT İLİŞKİSİ', [
        ('Evrensel Yasalar', 'Atomdan galaksiye', 'Aynı fizik yasaları'),
        ('Kusursuz Ahenk', 'İrade çatışması yok', 'Kaos yerine nizam'),
        ('Tevhit Sonucu', 'Tek İrade ve Kudret', 'Lâ ilâhe illallah')
    ], '10-din-kulturu-ve-ahlak-bilgisi-8 tevhit ve nizam')

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
