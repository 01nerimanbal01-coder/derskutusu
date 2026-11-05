"""11. sınıf Tarih 3. hafta (1683-1789 Siyasi ve Askeri Mücadeleler) görselleri.
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


def antlasma_kronoloji_kartlari():
    kartlar = [
        ('1. Karlofça (1699)', 'Büyük Toprak Kaybı', KIR, KIR_A),
        ('2. Pasarofça (1718)', 'Lale Devri Başlangıcı', TUR, TUR_A),
        ('3. Belgrad (1739)', 'Son Kazançlı Barış', YES, YES_A),
        ('4. Kaynarca (1774)', 'Kırım’ın Kaybı &amp; Rusya', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, '1683-1789 antlaşmalar kronoloji kartı.', 34)


def dis_politika_kirilma_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'OSMANLI DIŞ POLİTİKASINDA KÖKLÜ DEĞİŞİM (1699 KARLOFÇA)', 9.8, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, '1699 Öncesi Vizyon', 9.2, TUR)
    ic += yazi(92, 76, 'Fütuhat &amp; Taarruz Siyaseti', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Avrupa’ya Tek Taraflı Üstünlük', 8.2, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(267, 56, '1699 Sonrası Vizyon', 9.2, KIR)
    ic += yazi(267, 76, 'Savunma &amp; Mevcudu Koruma', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Denge Politikası &amp; Diplomasi', 8.2, KIR, ince=True)
    return svg(360, 125, ic, 'Osmanlı dış politika kırılma şeması.', 34)


def belgrad_kapitülasyon_kesiti():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, '1739 BELGRAD VE 1740 SÜREKLİ KAPİTÜLASYONLAR', 9.8, YESIL_K)
    ic += kutu(16, 36, 96, 70, '#ffffff', YES)
    ic += yazi(64, 56, 'Belgrad Zaferi', 9.0, YESIL_K)
    ic += yazi(64, 76, 'Son kazançlı barış', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Sırbistan geri alındı', 8.4, YES, ince=True)
    ic += kutu(132, 36, 96, 70, '#ffffff', MAVI)
    ic += yazi(180, 56, 'Fransız Arabulucu', 9.0, MAVI)
    ic += yazi(180, 76, 'Diplomatik destek', 8.4, LAC, ince=True)
    ic += yazi(180, 92, 'Barış masası lideri', 8.4, MAVI, ince=True)
    ic += kutu(248, 36, 96, 70, '#ffffff', TUR)
    ic += yazi(296, 56, '1740 İmtiyazı', 9.0, TUR)
    ic += yazi(296, 76, 'Kapitülasyon sürekli', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'Ekonomik tavizler', 8.4, TUR, ince=True)
    return svg(360, 125, ic, 'Belgrad ve kapitülasyon ilişkisi kesiti.', 34)


def lale_devri_isik_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'LALE DEVRİ (1718-1730) YENİLEŞME ALANLARI', 10.0, TUR)
    alanlar = [
        ('1. İlk Matbaa', 'İbrahim Müteferrika', 16),
        ('2. Çiçek Aşısı', 'İlk tıp uygulaması', 102),
        ('3. İtfaiye Ocağı', 'Tulumbacılar bölüğü', 188),
        ('4. Geçici Elçilik', 'Yirmisekiz Mehmed Çelebi', 274),
    ]
    for b, a, x in alanlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Lale Devri yenileşme alanları şeması.', 34)


def askeri_mucadele_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, '18. YÜZYIL SİYASİ GELİŞMELER VE ANTLAŞMALAR TABLOSU', 9.8, MOR)
    satirlar = [
        ('Antlaşma / Olay', 'Yıl', 'Karşı Devletler', 'Temel Sonuç', MOR),
        ('Karlofça', '1699', 'Avusturya, Leh, Ven.', 'Macaristan Kaybı', KIR),
        ('Pasarofça', '1718', 'Avusturya, Venedik', 'Batı Üstünlüğü Kabul', TUR),
        ('Belgrad', '1739', 'Avusturya, Rusya', 'Karadeniz Güvenliği', YESIL_K),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.2, r)
        ic += yazi(120, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(205, y + 13, k3, 7.8, LAC, ince=(i > 0))
        ic += yazi(295, y + 13, k4, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, '18. yüzyıl siyasi mücadeleler tablosu.', 34)


def kutsal_ittifak_cepheleri():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, '1683-1699 KUTSAL İTTİFAK SAVAŞ CEPHELERİ', 10.0, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Balkan &amp; Orta Avrupa', 9.0, CAM)
    ic += yazi(92, 76, '• Avusturya (Macaristan)', 8.2, LAC, ince=True)
    ic += yazi(92, 92, '• Lehistan (Podolya)', 8.2, LAC, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Deniz &amp; Doğu Avrupa', 9.0, TUR)
    ic += yazi(267, 76, '• Venedik (Mora &amp; Ege)', 8.2, LAC, ince=True)
    ic += yazi(267, 92, '• Rusya (Azak Kalesi)', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Kutsal İttifak cepheleri karşılaştırması.', 34)


def diplomasi_donusum_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, '18. YÜZYIL OSMANLI DİPLOMASİ DÖNÜŞÜMÜ', 10.0, TUR)
    kartlar = [
        ('1. Daimi Elçilik', 'Avrupa merkezlerinde temsil', 16),
        ('2. Denge Siyaseti', 'Büyük devletler arası rekabet', 102),
        ('3. Tercüme Odası', 'Yabancı dil &amp; uzman kâtip', 188),
        ('4. Hukuki Eşitlik', 'Karşılıklılık (mütekabiliyet)', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Diplomasi dönüşüm adımları kartı.', 34)


def tarihi_surec_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, '1683-1789 TARİHSEL DEĞİŞİM EVRELERİ', 10.0, YESIL_K)
    kutular = ['II. Viyana', 'Karlofça', 'Lale Devri', 'Kaynarca']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'{i + 1}. Dönüm', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.4, YESIL_K)
    return svg(360, 125, ic, 'Tarihsel değişim evreleri kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = antlasma_kronoloji_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = dis_politika_kirilma_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = belgrad_kapitülasyon_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = lale_devri_isik_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = askeri_mucadele_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = kutsal_ittifak_cepheleri()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = diplomasi_donusum_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = tarihi_surec_kutulari()
    s[10]['en_fazla'] = 34
