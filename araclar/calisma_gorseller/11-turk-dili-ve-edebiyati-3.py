"""11. sınıf Türk Dili ve Edebiyatı 3. hafta (Karagöz Oyunu, Mektup ve Dilekçe) görselleri.
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
        ('1. Mukaddime', 'Giriş &amp; Perde Gazeli', MAVI, MAVI_A),
        ('2. Muhavere', 'Karagöz-Hacivat Atışması', TUR, TUR_A),
        ('3. Fasıl', 'Asıl Oyun &amp; Yan Tipler', YES, YES_A),
        ('4. Bitiş', 'Kapanış &amp; Af Dileme', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Karagöz oyunu dört temel bölüm kartı.', 34)


def dil_catismasi_modeli():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'GÖLGE OYUNUNDA DİL ÇATIŞMASI VE MİZAH', 10.0, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Hacivat (Yarı Aydın)', 9.2, MAVI)
    ic += yazi(92, 76, 'Ağdalı Osmanlıca sözler', 8.4, LAC, ince=True)
    ic += yazi(92, 92, 'Kitabi &amp; resmi üslup', 8.4, MAVI, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Karagöz (Halk Adamı)', 9.2, TUR)
    ic += yazi(267, 76, 'Sözleri yanlış anlama', 8.4, LAC, ince=True)
    ic += yazi(267, 92, 'Halk nükte ve taşlaması', 8.4, TUR, ince=True)
    return svg(360, 125, ic, 'Karagöz ve Hacivat dilsel çatışma şeması.', 34)


def dilekce_yapi_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 20, 'RESMÎ DİLEKÇE METNİNİN BİÇİMSEL YAPISI', 9.8, MAVI)
    ic += kutu(16, 32, 328, 20, '#ffffff', MAVI, r=2)
    ic += yazi(180, 46, 'KURUM ADI BAŞLIĞI (BÜYÜK HARFLERLE)', 8.8, MAVI)
    ic += yazi(310, 46, 'Tarih', 8.0, LAC, ince=True)
    ic += kutu(16, 56, 328, 30, '#ffffff', LAC, r=2)
    ic += yazi(180, 70, 'Talep Metni (Açık, net ve saygılı üslup)', 8.4, LAC, ince=True)
    ic += yazi(180, 82, 'Gereğini saygılarımla arz ederim.', 8.4, YESIL_K)
    ic += yazi(50, 102, 'İletişim &amp; Adres', 8.0, LAC, ince=True)
    ic += yazi(300, 102, 'İmza &amp; Ad Soyad', 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Resmî dilekçe şablon yapısı.', 34)


def mektup_turleri_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'MEKTUP TÜRLERİ VE NİTELİKLERİ', 10.0, YESIL_K)
    turler = [
        ('1. Edebi Mektup', 'Sanat ve fikir tanıklığı', 16),
        ('2. Resmî Mektup', 'Kurumlar arası yazışma', 102),
        ('3. Özel Mektup', 'Samimi içten paylaşımlar', 188),
        ('4. Açık Mektup', 'Topluma hitap eden yazı', 274),
    ]
    for b, a, x in turler:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Mektup türleri sınıflandırma kartı.', 34)


def tipler_karsilastirma_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'GELENEKSEL GÖLGE OYUNU TİPLERİ TABLOSU', 9.8, MOR)
    satirlar = [
        ('Tip Adı', 'Sosyal Konumu', 'Konuşma Dili', 'Temel Karakter Özelliği', MOR),
        ('Karagöz', 'Sıradan Halk', 'Öz Türkçe / Argo', 'Açık sözlü, hazırcevap', TUR),
        ('Hacivat', 'Yarı Aydın', 'Ağdalı Osmanlıca', 'Görgülü, kurnaz, arabulucu', MAVI),
        ('Çelebi', 'Şehir Beyefendisi', 'Kibar İstanbul Ağzı', 'Züppe, mirasyedi genç', YESIL_K),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(50, y + 13, k1, 8.2, r)
        ic += yazi(125, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(210, y + 13, k3, 7.8, LAC, ince=(i > 0))
        ic += yazi(295, y + 13, k4, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Gölge oyunu tipleri karşılaştırma tablosu.', 34)


def dilekce_yerlesim_plani():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'DİLEKÇEDE YERLEŞİM VE İMZA STANDARDI', 10.0, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Sağ Köşeler', 9.2, YESIL_K)
    ic += yazi(92, 76, '• Sağ Üst: Güncel Tarih', 8.4, LAC, ince=True)
    ic += yazi(92, 92, '• Sağ Alt: Islak İmza &amp; Ad', 8.4, YESIL_K, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(267, 56, 'Sol Alt Köşe', 9.2, CAM)
    ic += yazi(267, 76, '• Açık İkametgâh Adresi', 8.4, LAC, ince=True)
    ic += yazi(267, 92, '• İletişim Telefonu &amp; E-posta', 8.4, CAM, ince=True)
    return svg(360, 125, ic, 'Dilekçe yerleşim planı şeması.', 34)


def geleneksel_tiyatro_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'GELENEKSEL TÜRK TİYATROSU BİLEŞENLERİ', 10.0, TUR)
    kartlar = [
        ('1. Karagöz', 'Gölge Oyunu &amp; Tasvir', 16),
        ('2. Orta Oyunu', 'Meydan &amp; Canlı Oyuncu', 102),
        ('3. Meddah', 'Tek Kişilik Anlatı', 188),
        ('4. Köy Seyirliği', 'Kırsal Ritüel Oyunlar', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Geleneksel Türk tiyatrosu kolları kartı.', 34)


def sahneleme_adimlari_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'KARAGÖZ OYUNU SAHNELENME EVRELERİ', 10.0, YESIL_K)
    kutular = ['Perde Gazeli', 'Muhavere', 'Fasıl Çatışması', 'Hatamız Affola']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'Adım {i + 1}', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, 'Karagöz oyun evreleri kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = karagoz_bolum_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = dil_catismasi_modeli()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = dilekce_yapi_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = mektup_turleri_kartlari()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = tipler_karsilastirma_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = dilekce_yerlesim_plani()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = geleneksel_tiyatro_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = sahneleme_adimlari_kutulari()
    s[10]['en_fazla'] = 34
