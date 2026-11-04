"""11. sınıf Matematik 1. hafta (İki Nicel Değişken ve Veri Toplama) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def degisken_turleri_kartlari():
    kartlar = [
        ('1. Nicel Değişken', 'Sayısal &amp; Ölçülebilir', MAVI, MAVI_A),
        ('2. Nitel Değişken', 'Kategorik &amp; Özellik', YES, YES_A),
        ('3. Evren (Kitle)', 'Tüm Hedef Bireyler', TUR, TUR_A),
        ('4. Örneklem', 'Seçilen Temsil Grubu', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'İstatistiksel değişken ve örneklem kartları.', 34)


def sacilma_grafigi_modeli():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İKİ NİCEL DEĞİŞKEN SAÇILMA (SCATTER) GRAFİĞİ', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'X Ekseni: Süre (saat)', 9.4, MAVI)
    ic += yazi(92, 76, 'Haftalık Kitap Okuma', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Nicel Veri 1', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Y Ekseni: Puan (0-100)', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Türkçe Sınav Başarısı', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Nicel Veri 2', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'İki nicel değişken saçılma eksenleri.', 34)


def sacilma_koordinat_krokisi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'EŞLEŞMİŞ VERİ ÇİFTLERİ (x, y) KOORDİNAT DÜZLEMİ', 10.2, YESIL_K)
    noktalar = [
        ('(2 s, 65 p)', 16),
        ('(4 s, 75 p)', 102),
        ('(6 s, 85 p)', 188),
        ('(8 s, 95 p)', 274),
    ]
    for p, x in noktalar:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 56, p, 9.4, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, 'Veri Noktası', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Eşleşmiş veri noktaları saçılma şeması.', 34)


def evren_orneklem_venn():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'EVREN VE ÖRNEKLEM İLİŞKİSİ MODELİ', 10.3, TUR)
    ic += kutu(20, 38, 145, 68, '#ffffff', TUR)
    ic += yazi(92, 58, 'HEDEF EVREN', 9.6, TUR)
    ic += yazi(92, 78, 'Okuldaki 1200 Öğrenci', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Bütünsel ana kitle', 8.8, TUR, ince=True)

    ic += kutu(195, 38, 145, 68, YES_A, YES)
    ic += yazi(267, 58, 'TEMSİLİ ÖRNEKLEM', 9.6, YESIL_K)
    ic += yazi(267, 78, 'Rastgele Seçilen 100 Kişi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Yansız alt küme', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Evren ve örneklem bağıntı kartı.', 34)


def istatistik_arastirma_adimlari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'İKİ NİCEL DEĞİŞKENLİ ARAŞTIRMA SÜRECİ', 10.2, CAM)
    adımlar = [
        ('1. Soru', 'Nicel Kriter', 16),
        ('2. Örneklem', 'Yansız Seçim', 102),
        ('3. Veri', 'Eşleşmiş (x,y)', 188),
        ('4. Analiz', 'Saçılma Grafiği', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.3, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Araştırma planlama basamakları şeması.', 34)


def arastirma_sorusu_karsilastirma():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'ARAŞTIRMA SORUSU DEĞERLENDİRME KRİTERLERİ', 10.2, MOR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MOR)
    ic += yazi(92, 56, 'Hatalı / Nitel Soru', 9.4, KIR)
    ic += yazi(92, 76, 'En sevilen yemek nedir?', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Tekil ve nitel veri', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Doğru / İki Nicel Soru', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Ekran süresi &amp; Uyku süresi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'İki sayısal nicelik bağı', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'İki nicel araştırma sorusu kriter kartı.', 34)


def degisken_ciftleri_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'DEĞİŞKEN ÇİFTLERİ VE İSTATİSTİKSEL TÜRÜ', 10.1, YESIL_K)
    kartlar = [
        ('Zaman &amp; Boy', 'İki Nicel', 16),
        ('Takım Tercihi', 'Tekil Nitel', 102),
        ('Hız &amp; Mesafe', 'İki Nicel', 188),
        ('Göz Rengi', 'Tekil Nitel', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Değişken türleri eşleştirme tablosu.', 34)


def veri_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['V', 'E', 'R', 'İ']
    for i, h in enumerate(harfler):
        x = 75 + i * 56
        ic += kutu(x, 42, 48, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 24, 74, h, 16.0, MAVI)
        ic += yazi(x + 24, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Veri kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = degisken_turleri_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = sacilma_grafigi_modeli()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = sacilma_koordinat_krokisi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = evren_orneklem_venn()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = istatistik_arastirma_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = arastirma_sorusu_karsilastirma()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = degisken_ciftleri_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = veri_sifre_kutulari()
    s[10]['en_fazla'] = 34
