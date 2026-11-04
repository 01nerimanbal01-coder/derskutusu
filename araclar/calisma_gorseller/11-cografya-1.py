"""11. sınıf Coğrafya 1. hafta (Mekânsal Sorunların Çözümünde Coğrafya) görselleri.
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


def cografya_ilke_kartlari():
    ilkeler = [
        ('1. Dağılış İlkesi', 'Yayılış ve etki alanı', MAVI, MAVI_A),
        ('2. İlgi İlkesi', 'İnsan-çevre bağı', YES, YES_A),
        ('3. Nedensellik', 'Sebep-sonuç analizi', TUR, TUR_A),
        ('4. CBS Planlama', 'Çok katmanlı çözüm', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(ilkeler):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.5, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Mekânsal sorun çözümünde coğrafi ilkeler kartı.', 34)


def havza_model_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'HAVZA YÖNETİMİ &amp; MEKÂNSAL VERİ MODELİ', 10.4, CAM)
    ic += kutu(16, 34, 100, 72, YES_A, YES)
    ic += yazi(66, 52, 'Yukarı Havza', 9.8, YESIL_K)
    ic += yazi(66, 72, 'Orman Koruma', 8.8, LAC, ince=True)
    ic += yazi(66, 90, 'Teraslama', 8.8, YESIL_K, ince=True)

    ic += kutu(130, 34, 100, 72, TUR_A, TUR)
    ic += yazi(180, 52, 'Orta Havza', 9.8, TUR)
    ic += yazi(180, 72, 'Tarım &amp; Sulama', 8.8, LAC, ince=True)
    ic += yazi(180, 90, 'Erozyon Kontrolü', 8.8, TUR, ince=True)

    ic += kutu(244, 34, 100, 72, MAVI_A, MAVI)
    ic += yazi(294, 52, 'Aşağı Havza', 9.8, MAVI)
    ic += yazi(294, 72, 'Kıyı &amp; Yerleşim', 8.8, LAC, ince=True)
    ic += yazi(294, 90, 'Taşkın Yatağı', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Havza yönetim kesiti ve mekânsal analiz modeli.', 34)


def taskin_kesit_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'AKARSU TAŞKIN RİSKİ VE DOĞRU YERLEŞİM KESİTİ', 10.2, YESIL_K)
    ic += kutu(16, 36, 150, 70, KIR_A, KIR)
    ic += yazi(91, 54, 'Hatalı Yerleşim Alanı', 9.8, KIR)
    ic += yazi(91, 74, 'Taşkın Tabanı / Alüvyon', 8.9, LAC, ince=True)
    ic += yazi(91, 92, 'Risk: Yüksek Su Baskını', 8.9, KIR)

    ic += kutu(194, 36, 150, 70, MAVI_A, MAVI)
    ic += yazi(269, 54, 'Önerilen Güvenli Alan', 9.8, MAVI)
    ic += yazi(269, 74, 'Sağlam Zeminli Yamaç', 8.9, LAC, ince=True)
    ic += yazi(269, 92, 'Plan: Yeşil Kuşak Koruması', 8.9, YESIL_K)
    return svg(360, 125, ic, 'Taşkın riski ve güvenli yerleşim analizi şeması.', 34)


def mekan_veri_dongusu():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'COĞRAFİ VERİDEN MEKÂNSAL ÇÖZÜME DÖNGÜSÜ', 10.3, TUR)
    adımlar = [
        ('1. Uydu &amp; İHA', 16),
        ('2. CBS Analiz', 102),
        ('3. Risk Tespiti', 188),
        ('4. Planlama', 274)
    ]
    for ad, x in adımlar:
        ic += kutu(x, 40, 70, 64, '#ffffff', TUR, r=4)
        ic += yazi(x + 35, 66, ad, 9.2, LAC)
        ic += yazi(x + 35, 86, 'Veri Adımı', 8.4, TUR, ince=True)
    return svg(360, 125, ic, 'Coğrafi veriden mekânsal çözüme ulaşma döngüsü.', 34)


def erozyon_planlama_basamaklari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'EROZYONLA MÜCADELE COĞRAFİ PLANLAMA ADIMLARI', 10.1, CAM)
    basamaklar = [
        ('1. Adım', 'Haritalama', MAVI, 16),
        ('2. Adım', 'Risk Belirleme', YES, 102),
        ('3. Adım', 'Ağaçlandırma', TUR, 188),
        ('4. Adım', 'Uydu İzleme', MOR, 274),
    ]
    for b, d, r, x in basamaklar:
        ic += kutu(x, 34, 70, 74, '#ffffff', r)
        ic += kutu(x + 6, 40, 58, 20, r, r, r=3)
        ic += yazi(x + 35, 54, b, 9.0, '#ffffff')
        ic += yazi(x + 35, 78, d, 8.8, LAC)
        ic += yazi(x + 35, 94, 'Uygulama', 8.2, r, ince=True)
    return svg(360, 125, ic, 'Erozyonla mücadelede 4 temel coğrafi planlama adımı.', 34)


def cbs_katman_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'CBS ÇOK KRİTERLİ YER SEÇİMİ KATMANLARI', 10.3, MOR)
    katmanlar = [
        ('Katman 1', 'Eğim &amp; Jeoloji', 16),
        ('Katman 2', 'Fay Hatları', 102),
        ('Katman 3', 'Su Havzaları', 188),
        ('Sonuç', 'Uygun Sanayi Alanı', 274),
    ]
    for k, acik, x in katmanlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, k, 9.4, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, acik, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'CBS yer seçimi çakıştırma katmanları şeması.', 34)


def mekan_sorun_sonuc_kartlari():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 20, 'ARAZİ KULLANIM HATALARI VE COĞRAFİ SONUÇLARI', 10.1, KIR)
    kartlar = [
        ('Kıyı Kumulu', 'Kıyı Erozyonu', 16),
        ('Fay Hattı', 'Deprem Riski', 102),
        ('Sulak Alan', 'Kuraklaşma', 188),
        ('Orman İmarı', 'Şiddetli Sel', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', KIR)
        ic += yazi(x + 35, 54, s, 9.1, KIR)
        ic += f'<line x1="{x + 8}" y1="62" x2="{x + 62}" y2="62" stroke="{KIR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Hatalı arazi kullanımının coğrafi sonuçları.', 34)


def mekan_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, YESIL_K)
    harfler = ['M', 'E', 'K', 'A', 'N']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 22, 74, h, 16.0, YESIL_K)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Mekan kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cografya_ilke_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = havza_model_kesiti()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = taskin_kesit_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = mekan_veri_dongusu()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = erozyon_planlama_basamaklari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = cbs_katman_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = mekan_sorun_sonuc_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = mekan_sifre_kutulari()
    s[10]['en_fazla'] = 34
