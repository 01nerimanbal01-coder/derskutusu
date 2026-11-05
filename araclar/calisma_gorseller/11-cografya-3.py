"""11. sınıf Coğrafya 3. hafta (Web Tabanlı CBS Uygulamaları) görselleri.
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


def cbs_bilesen_kartlari():
    kartlar = [
        ('1. Donanım', 'Bilgisayar &amp; Sunucu', MAVI, MAVI_A),
        ('2. Yazılım', 'CBS Programı &amp; Kod', YES, YES_A),
        ('3. Veri Tabanı', 'Mekânsal &amp; Öznitelik', TUR, TUR_A),
        ('4. Canlı Güç', 'Uzman &amp; Karar Verici', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.8, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'CBS temel bileşenleri kartı.', 34)


def vektor_raster_semasi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'MEKÂNSAL VERİ MODELLERİ: VEKTÖR VE RASTER', 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 54, 'Vektör Veri Modeli', 9.2, MAVI)
    ic += yazi(92, 72, '• Nokta: Kuyu, Direk, Durak', 8.2, LAC, ince=True)
    ic += yazi(92, 86, '• Çizgi: Akarsu, Yol, Fay', 8.2, LAC, ince=True)
    ic += yazi(92, 98, '• Poligon: Göl, Orman, Ada', 8.2, LAC, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 54, 'Raster Veri Modeli', 9.2, TUR)
    ic += yazi(267, 72, '• Piksel ve Hücre Ağı', 8.2, LAC, ince=True)
    ic += yazi(267, 86, '• Sayısal Yükseklik (DEM)', 8.2, LAC, ince=True)
    ic += yazi(267, 98, '• Uydu Görüntüleri', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Vektör ve raster veri modelleri şeması.', 34)


def tampon_bolge_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'TAMPON BÖLGE (BUFFER) ANALİZİ VE TAŞKIN KORUMA', 9.8, CAM)
    ic += kutu(16, 36, 96, 70, '#ffffff', CAM)
    ic += yazi(64, 56, 'Akarsu Ekseni', 9.0, CAM)
    ic += yazi(64, 76, 'Merkez çizgi', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Kaynak vektör', 8.4, CAM, ince=True)
    ic += kutu(132, 36, 96, 70, TUR_A, TUR)
    ic += yazi(180, 56, '500 m Tampon', 9.0, TUR)
    ic += yazi(180, 76, 'Riskli Kuşak', 8.4, KIR, ince=True)
    ic += yazi(180, 92, 'Yapılaşma Yasak', 8.4, TUR, ince=True)
    ic += kutu(248, 36, 96, 70, YES_A, YES)
    ic += yazi(296, 56, 'Güvenli Alan', 9.0, YESIL_K)
    ic += yazi(296, 76, 'Taşkın Dışı', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'İmar Uygun', 8.4, YES, ince=True)
    return svg(360, 125, ic, 'Tampon bölge etki alanı kesiti.', 34)


def oznitelik_tablosu_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'MEKÂNSAL VERİ VE ÖZNİTELİK TABLOSU İLİŞKİSİ', 9.8, MOR)
    basliklar = [('ID', 40), ('Nesne Adı', 110), ('Geometri', 190), ('Risk Puanı', 270)]
    for ad, x in basliklar:
        ic += kutu(x - 20, 32, 65, 18, MOR, MOR, r=2)
        ic += yazi(x + 12, 45, ad, 8.4, '#ffffff')
    satirlar = [
        ('01', 'Sakarya Nehri', 'Çizgi', 'Yüksek (85)'),
        ('02', 'Sapanca Gölü', 'Poligon', 'Orta (45)'),
        ('03', 'Deprem İstasyonu', 'Nokta', 'Düşük (10)'),
    ]
    for i, s in enumerate(satirlar):
        y = 54 + i * 20
        ic += kutu(20, y, 320, 18, '#ffffff', MOR, r=2)
        ic += yazi(52, y + 13, s[0], 8.2, LAC, ince=True)
        ic += yazi(122, y + 13, s[1], 8.2, LAC, ince=True)
        ic += yazi(202, y + 13, s[2], 8.2, LAC, ince=True)
        ic += yazi(282, y + 13, s[3], 8.2, KIR if 'Yüksek' in s[3] else LAC, ince=True)
    return svg(360, 125, ic, 'Mekânsal öznitelik tablosu şeması.', 34)


def cakistirma_overlay_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'ÇAKIŞTIRMA (OVERLAY) İLE YER SEÇİMİ KATMANLARI', 9.8, YESIL_K)
    katmanlar = [
        ('1. Eğim Katmanı', 'Düz &amp; Az Eğimli', 16, YES),
        ('2. Jeoloji Katmanı', 'Sağlam Zemin', 102, TUR),
        ('3. Ulaşım Katmanı', 'Ana Yola Yakın', 188, MAVI),
        ('4. Sentez Harita', 'En Uygun Alan', 274, MOR),
    ]
    for baslik, acik, x, r in katmanlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', r)
        ic += yazi(x + 35, 54, baslik, 8.2, r)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, acik, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Çakıştırma analizi yer seçimi katmanları.', 34)


def heyelan_egim_diyagrami():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'EĞİM DERECESİ VE HEYELAN DUYARLILIK SINIFLARI', 9.8, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, '%0 - %15 Eğim', 9.2, YESIL_K)
    ic += yazi(92, 76, 'Düşük Duyarlılık', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Yerleşime Çok Uygun', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(267, 56, '>%35 Dik Eğim', 9.2, KIR)
    ic += yazi(267, 76, 'Yüksek Heyelan Riski', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Yapılaşmaya Kapalı', 8.6, KIR, ince=True)
    return svg(360, 125, ic, 'Eğim kademeleri ve heyelan risk diyagramı.', 34)


def dem_yukseklik_kartlari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'SAYISAL YÜKSEKLİK MODELİ (DEM) TÜREVLERİ', 10.0, CAM)
    kartlar = [
        ('Eğim Haritası', 'Yamaç dikliği derecesi', 16),
        ('Bakı Haritası', 'Güneş alma cephesi', 102),
        ('Akış Yönü', 'Su drenaj yönlenmesi', 188),
        ('Havza Sınırı', 'Su ayrım çizgisi tespiti', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 54, b, 8.4, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Sayısal Yükseklik Modeli analiz türevleri.', 34)


def cbs_katman_sentez_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'CBS ANALİZ AŞAMALARI', 10.2, YESIL_K)
    kutular = ['Veri Girişi', 'Depolama', 'Mekânsal Analiz', 'Karar Destek']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'{i + 1}. Adım', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.6, YESIL_K)
    return svg(360, 125, ic, 'CBS analiz aşamaları akış kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cbs_bilesen_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = vektor_raster_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = tampon_bolge_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = oznitelik_tablosu_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = cakistirma_overlay_semasi()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = heyelan_egim_diyagrami()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = dem_yukseklik_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = cbs_katman_sentez_kutulari()
    s[10]['en_fazla'] = 34
