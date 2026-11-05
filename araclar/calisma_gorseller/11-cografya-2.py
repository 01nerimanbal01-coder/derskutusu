"""11. sınıf Coğrafya 2. hafta (Mekânsal Çözümler ve Web CBS) görselleri.
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


def sunger_sehir_kartlari():
    kartlar = [
        ('1. Sünger Şehir', 'Geçirgen Zemin', YES, YES_A),
        ('2. Web CBS', 'Bulut Tabanlı Analiz', MAVI, MAVI_A),
        ('3. Vektör Model', 'Nokta-Çizgi-Alan', TUR, TUR_A),
        ('4. Raster Model', 'Piksel Izgarası', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Mekânsal çözümler ve CBS kartları.', 34)


def sunger_sehir_hidroloji_kesiti():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'GELENEKSEL ŞEHİR VE SÜNGER ŞEHİR HİDROLOJİSİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, KIR_A, KIR)
    ic += yazi(92, 56, 'Geleneksel Şehir (Beton)', 9.4, KIR)
    ic += yazi(92, 76, '%80 Yüzey Akışı → Sel Riski', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Yeraltına süzülme: &lt; %10', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Sünger Şehir Modeli', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Yağmur bahçesi &amp; yeşil çatı', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Yeraltı akiferine süzülüş', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Sünger şehir hidrolojisi karşılaştırma şeması.', 34)


def musilaj_web_cbs_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'HAVZA ANALİZİ VE WEB CBS ÇÖZÜM MODELİ', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Marmara Havzası Verisi', 9.6, CAM)
    ic += yazi(92, 76, 'Noktasal atık su deşarjları', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Sıcaklık ve azot katmanları', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, MAVI_A, MAVI)
    ic += yazi(267, 56, 'Web CBS Sorgulama', 9.6, MAVI)
    ic += yazi(267, 76, 'Bulut üzerinden canlı izleme', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Müdahale haritası üretimi', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Web CBS havza analiz modeli.', 34)


def web_cbs_mimarisi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'WEB TABANLI CBS BULUT MİMARİSİ', 10.3, MAVI)
    ic += kutu(20, 38, 95, 68, '#ffffff', MAVI)
    ic += yazi(67, 58, 'Bulut Sunucu', 9.4, MAVI)
    ic += yazi(67, 78, 'Büyük Veri', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Depolama', 8.8, MAVI, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', YES)
    ic += yazi(179, 58, 'Web Servisi', 9.4, YESIL_K)
    ic += yazi(179, 78, 'WMS / WFS', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Veri İletimi', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(292, 58, 'İstemci Tarayıcı', 9.4, TUR)
    ic += yazi(292, 78, 'İnteraktif', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Harita Arayüzü', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Web CBS bulut mimarisi şeması.', 34)


def web_cbs_islem_adimlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 20, 'WEB CBS UYGULAMA İŞ AKIŞ ADIMLARI', 10.2, TUR)
    adımlar = [
        ('1. Veri', 'Koordinat Alımı', 16),
        ('2. Bulut', 'Katman Yükleme', 102),
        ('3. Analiz', 'Çakıştırma', 188),
        ('4. Paylaşım', 'Web Haritası', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 56, b, 9.3, TUR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Web CBS iş akışı basamakları.', 34)


def vektor_geometri_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'CBS VEKTÖR GEOMETRİK VERİ TÜRLERİ', 10.3, MOR)
    ic += kutu(20, 36, 95, 70, '#ffffff', MAVI)
    ic += yazi(67, 56, 'Nokta (Point)', 9.4, MAVI)
    ic += yazi(67, 76, 'İstasyon / Kuyu', 8.8, LAC, ince=True)
    ic += yazi(67, 92, '(X, Y Koordinatı)', 8.8, MAVI, ince=True)

    ic += kutu(132, 36, 95, 70, '#ffffff', TUR)
    ic += yazi(179, 56, 'Çizgi (Line)', 9.4, TUR)
    ic += yazi(179, 76, 'Nehir / Yol / Hat', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Uzunluk Ölçümü', 8.8, TUR, ince=True)

    ic += kutu(245, 36, 95, 70, '#ffffff', YESIL_K)
    ic += yazi(292, 56, 'Poligon (Polygon)', 9.4, YESIL_K)
    ic += yazi(292, 76, 'Göl / Orman / İl', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Alan &amp; Çevre', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Vektör geometri veri tipleri kartı.', 34)


def cbs_veri_karsilastirma_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'MEKÂNSAL VERİ ÖRNEĞİ VE CBS FORMATI', 10.1, YESIL_K)
    kartlar = [
        ('Rasathane', 'Nokta Geometrisi', 16),
        ('Boru Hattı', 'Çizgi Geometrisi', 102),
        ('Milli Park', 'Poligon Geometri', 188),
        ('Uydu Yükseklik', 'Raster Piksel', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'CBS veri formatı eşleştirme kartı.', 34)


def bulut_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, CAM)
    harfler = ['B', 'U', 'L', 'U', 'T']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', CAM, r=4)
        ic += yazi(x + 22, 74, h, 16.0, CAM)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Bulut kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sunger_sehir_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = sunger_sehir_hidroloji_kesiti()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = musilaj_web_cbs_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = web_cbs_mimarisi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = web_cbs_islem_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = vektor_geometri_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = cbs_veri_karsilastirma_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = bulut_sifre_kutulari()
    s[10]['en_fazla'] = 34
