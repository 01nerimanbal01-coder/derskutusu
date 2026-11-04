"""11. sınıf Türk Dili ve Edebiyatı 1. hafta görselleri.
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


def karagoz_bolum_kartlari():
    kartlar = [
        ('1. Mukaddime', 'Giriş &amp; Gazel', TUR, TUR_A),
        ('2. Muhavere', 'Karagöz-Hacivat Atışması', YES, YES_A),
        ('3. Fasıl', 'Asıl Oyun &amp; Yan Tipler', MAVI, MAVI_A),
        ('4. Bitiş', 'Kapanış &amp; Af Dileme', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Karagöz oyununun dört yapısal bölümü.', 34)


def sahne_ve_diyalog_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'GÖLGE OYUNU DİYALOG VE MİZAH YAPISI', 10.3, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Hacivat (Aydın Dili)', 9.4, TUR)
    ic += yazi(92, 76, 'Kuzum Karagöz\'üm,', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'gel hasbihâl edelim...', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Karagöz (Halk Sağduyusu)', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Bakkal İshak\'ın kelini', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'mi dövelim? (Yanlış Anlama)', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Karagöz ve Hacivat diyalog mizahı modeli.', 34)


def hayalbaz_duzenek_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'ŞEYH KÜŞTERİ MEYDANI PERDE DÜZENEĞİ', 10.2, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Beyaz Perde (Ayna)', 9.6, CAM)
    ic += yazi(92, 76, 'Işık arkadan vurur', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Tasvirler yansıtılır', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, MOR_A, MOR)
    ic += yazi(267, 56, 'Hayalî (Hayalbaz)', 9.6, MOR)
    ic += yazi(267, 76, 'Tüm seslendirme &amp; taklit', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Yardak ile müzik icrası', 8.8, MOR, ince=True)
    return svg(360, 125, ic, 'Gölge oyunu sahne ve hayalbaz şeması.', 34)


def metin_turleri_karsilastirma():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'METİN TÜRLERİ VE OKUMA AMAÇLARI', 10.3, YESIL_K)
    ic += kutu(20, 38, 95, 68, TUR_A, TUR)
    ic += yazi(67, 58, 'Karagöz', 9.4, TUR)
    ic += yazi(67, 78, 'Mizah &amp; Eleştiri', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Seyirlik Sanat', 8.8, TUR, ince=True)

    ic += kutu(132, 38, 95, 68, YES_A, YES)
    ic += yazi(179, 58, 'Mektup', 9.4, YESIL_K)
    ic += yazi(179, 78, 'Duygu Paylaşımı', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Samimi Hitap', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 38, 95, 68, MAVI_A, MAVI)
    ic += yazi(292, 58, 'Dilekçe', 9.4, MAVI)
    ic += yazi(292, 78, 'Resmi Başvuru', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Yasal Hak Arama', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Üç metin türünün okuma amaçları.', 34)


def perde_akis_adimlari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'KARAGÖZ OYUNU PERDE AKIŞ SIRASI', 10.2, MOR)
    adımlar = [
        ('1. Giriş', 'Mukaddime', 16),
        ('2. Atışma', 'Muhavere', 102),
        ('3. Olay', 'Fasıl', 188),
        ('4. Bitiş', 'Kapanış', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Karagöz oyun akışı basamakları.', 34)


def dilekce_yerlesim_krokisi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'RESMİ DİLEKÇE YERLEŞİM ŞABLONU', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Kurum Başlığı (Üst Orta)', 9.2, MAVI)
    ic += yazi(92, 76, 'Gerekçeli Metin (Gövde)', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Arz ederim / Saygılarımla', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Alt Yerleşim Düzeni', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Sağ Alt: Tarih ve İmza', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Sol Alt: İletişim Adresi', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Dilekçe yerleşim ve biçim şablonu.', 34)


def hitap_eslestirme_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'METİN TÜRLERİ VE KARAKTERİSTİK HİTAPLAR', 10.1, YESIL_K)
    kartlar = [
        ('Özel Mektup', 'Sevgili Kardeşim', 16),
        ('Dilekçe', 'Makam Başlığı', 102),
        ('Gölge Oyunu', 'Hay Hak! Medet!', 188),
        ('Edebi Mektup', 'Aziz Dostum', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Metin türü ve hitap eşleştirmesi.', 34)


def perde_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, TUR)
    harfler = ['P', 'E', 'R', 'D', 'E']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 22, 74, h, 16.0, TUR)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Perde kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = karagoz_bolum_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = sahne_ve_diyalog_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = hayalbaz_duzenek_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = metin_turleri_karsilastirma()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = perde_akis_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = dilekce_yerlesim_krokisi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = hitap_eslestirme_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = perde_sifre_kutulari()
    s[10]['en_fazla'] = 34
