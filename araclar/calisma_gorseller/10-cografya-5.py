# -*- coding: utf-8 -*-
"""10-cografya-5 çalışma kâğıdı görselleri.
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
    return kart4('MEKÂNSAL VERİ SEMBOL TÜRLERİ', [('Nokta (●)', 'Zirve, Kuyu, Okul'), ('Çizgi (—)', 'Akarsu, Yol, Fay'), ('Alan (■)', 'Göl, Orman, İl'), ('Lejant', 'Sembol anahtarı')], '10-cografya-5 sembol türleri')

def g1():
    return karsilastir2('HARİTA TASARIMINDA İLK İKİ ADIM', '1. Amaç Belirleme', 'Ne için ve kime çizilecek?', 'Örn: Afet toplanma haritası', '2. Araç ve Yöntem Seçme', 'CBS, GPS, Uydu görüntüsü', 'Altlık harita ve ölçek seçimi', '10-cografya-5 ilk iki adım')

def g2():
    return uclu_sema('TEMEL HARİTA ELEMANLARI', [('Başlık & Çerçeve', 'Konuyu ve sınırı verir', 'Üst orta bölümde'), ('Ölçek & Yön Oku', 'Mesafe ve Kuzey (K)', '1/100.000 veya çizgi'), ('Lejant & Koordinat', 'İşaretler ve enlem-boylam', 'Harita anahtarı kutusu')], '10-cografya-5 harita elemanları')

def g3():
    return karsilastir2('DOĞRUSAL VE ALANSAL VERİ AYRIMI', 'Çizgisel (Doğrusal) Veriler', 'Akarsu, Kara yolu, Demir yolu', 'Boru hattı, Fay kuşağı', 'Alansal (Yüzeysel) Veriler', 'Göl, Baraj, Orman sahası', 'Tarım alanı, İdari bölge', '10-cografya-5 çizgisel ve alansal veriler')

def g5():
    return kart4('HARİTA OLUŞTURMA SÜRECİ (6 ADIM)', [('1-2. Amaç & Araç', 'Hedef ve CBS seçimi'), ('3. Veri Toplama', 'Saha, GPS, İstatistik'), ('4-5. Tür & Aktarım', 'Sembol ve elemanlar'), ('6. Düzenleme', 'Kontrol ve güncelleme')], '10-cografya-5 süreç adımları')

def g6():
    return uclu_sema('KARMA HARİTADA SEMBOL SEÇİMİ', [('Fındık Bölgesi', 'Yüzey kaplar', 'Alan Sembolü (■)'), ('Demir Yolu Hattı', 'Doğrusal uzanır', 'Çizgi Sembolü (—)'), ('Liman Kenti', 'Konumsal merkezdir', 'Nokta Sembolü (●)')], '10-cografya-5 karma sembol seçimi')

def g8():
    return kart4('VERİ TOPLAMA VE AKTARMA TEKNOLOJİLERİ', [('GPS / GNSS', 'Hassas nokta konumu'), ('Uzaktan Algılama', 'Uydu ve dron verisi'), ('İstatistik Kurumu', 'Nüfus ve ekonomik veri'), ('CBS (GIS)', 'Katmanlı harita üretimi')], '10-cografya-5 teknolojiler')

def g11():
    return karsilastir2('6. ADIM: KULLANMA VE YENİDEN DÜZENLEME', 'Harita Kontrolü', 'Sembol ve ölçek doğruluğu', 'Okunabilirlik testi', 'Güncelleme Süreci', 'Yeni yol, bina ve sınırların eklenmesi', 'Dinamik CBS katmanı yenileme', '10-cografya-5 yeniden düzenleme')

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
