# -*- coding: utf-8 -*-
"""7-sosyal-bilgiler-14 çalışma kâğıdı görselleri.
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
    return kart4('OSMANLI ISLAHAT KURUMLARI VE ALANLARI', [('İlk Türk Matbaası', '1727 · Müteferrika', 'Kültür ve Bilim'), ('Nizam-ı Cedit', 'III. Selim dönemi', 'Modern Askeri Ordu'), ('Şirket-i Hayriye', 'Boğaz vapurları', 'Ulaşım ve Ticaret'), ('Memleket Sandığı', '1863 · Mithat Paşa', 'Ziraat Bankası temeli')], '7-sosyal-14 ıslahat kurumları kartları')

def g1():
    return uclu_sema('LALE DEVRİ (1718–1730) YENİLİKLERİ (ASKERİ ISLAHAT YOK)', [('Kültür ve Sanat', 'İlk Türk Matbaası (1727)', 'Yalova Kağıt Fabrikası'), ('Diplomasi', 'Geçici Elçilikler', 'Paris: 28 Mehmet Çelebi'), ('Sağlık & Sosyal', 'Çiçek Aşısı uygulaması', 'Tulumbacılar (İtfaiye)')], '7-sosyal-14 Lale Devri şeması')

def g2():
    return karsilastir2('III. SELİM VE II. MAHMUT DÖNEMİ YENİLİKLERİ', 'III. Selim (Nizam-ı Cedit)', 'Avrupa tarzı Nizam-ı Cedit ordusu', 'İrad-ı Cedit hazinesi · Londra kalıcı elçilik', 'II. Mahmut (Modernleşme)', '1826 Vaka-i Hayriye (Yeniçeri kaldırıldı)', 'Nazırlıklar, Takvim-i Vekayi, Tıbbiye', '7-sosyal-14 III. Selim ve II. Mahmut')

def g5():
    return karsilastir2('II. MAHMUT DÖNEMİ YÖNETİM VE KURUM DÖNÜŞÜMÜ', 'Kaldırılan Klasik Kurumlar', 'Divan-ı Hümayun kaldırıldı', 'Yeniçeri Ocağı kaldırıldı (1826)', 'Kurulan Modern Kurumlar', 'Nazırlıklar (Bakanlıklar) ve Muhtarlıklar', 'Asakir-i Mansure-i Muhammediye ordusu', '7-sosyal-14 II. Mahmut kurum dönüşümü')

def g6():
    return kart4('19. YÜZYIL ULAŞIM, HABERLEŞME VE EKONOMİ', [('Posta Nezareti', '1840 · Düzenli posta', 'Haberleşme ağı'), ('Telgraf Hatları', '1855 · Kırım Savaşı', 'Hızlı merkezî iletişim'), ('İzmir–Aydın Hattı', '1856 · İlk demiryolu', 'Tarımsal ticaret'), ('Ziraat Bankası', '1888 (1863 Sandık)', 'Çiftçiye kredi desteği')], '7-sosyal-14 ulaşım ve haberleşme')

def g7():
    return karsilastir2('İBRAHİM MÜTEFERRİKA MATBAASI VE KÜLTÜREL ETKİSİ', 'Kuruluşu ve İlk Eser (1727–1729)', 'Sait Efendi ve İbrahim Müteferrika kurdu', 'İlk basılan eser: Vankulu Lügatı (Sözlük)', 'Toplumsal ve Bilimsel Sonucu', 'Kitaplar ucuzladı ve hızla çoğaltıldı', 'Tarih, coğrafya ve fen bilgisi yaygınlaştı', '7-sosyal-14 matbaa kültür kartı')

def g8():
    return akis4('OSMANLI YENİLEŞME KRONOLOJİSİ (1727–1876)', [('1727 Lale Devri', 'İlk Türk Matbaası', 'Geçici elçilikler'), ('1793 III. Selim', 'Nizam-ı Cedit', 'Kalıcı elçilik (Londra)'), ('1826 II. Mahmut', 'Vaka-i Hayriye', 'Nazırlıklar & Gazete'), ('1839–1876 Hukuk', 'Tanzimat & Islahat', 'Kanun-i Esasi')], '7-sosyal-14 kronoloji akışı')

def g11():
    return uclu_sema('HUKUK VE DEMOKRATİKLEŞME ADIMLARI', [('1839 Tanzimat', 'Kanun üstünlüğü', 'Can, mal, ırz güvencesi'), ('1856 Islahat', 'Tam eşitlik ilkesi', 'Toplumsal kaynaşma'), ('1876 Kanun-i Esasi', 'İlk Türk Anayasası', 'Meclis-i Mebusan açıldı')], '7-sosyal-14 demokratikleşme şeması')

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
