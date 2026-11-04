"""6. sınıf Matematik 9. hafta (Kesir, Ondalık ve Yüzde Gösterimleriyle Çok Adımlı Dört İşlem Problemleri Çözme ve Problem Kurma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kalanin_kesri_serit():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 21, 'ŞERİT MODELİ (5 EŞ PARÇA) · KALANIN KESİR PROBLEMİ', 10.1, MAVI)
    renkler = [(TUR, TUR_A, '1. Adım: %20'), (MOR, MOR_A, '2. Adım: Kalanın'), (YES, YES_A, 'Kalan'), (YES, YES_A, '180 L'), (YES, YES_A, '(3 Kutu)')]
    for i, (r, z, et) in enumerate(renkler):
        x = 16 + i * 66
        ic += kutu(x, 30, 62, 26, z, r, 5, 1.2)
        ic += yazi(x + 31, 47, et, 8.8, LAC)
    ic += yazi(180, 72, '1. Adım: Beşte biri (1 kutu) · 2. Adım: Kalan 4 kutunun çeyreği (1 kutu) · Kalan 3 kutu = 180 L', 8.9, LAC, ince=True)
    return svg(360, 88, ic, 'Beş eş parçalı şerit modeli üzerinde kalanın kesri ve parçadan bütüne geçiş.', 15)


def ardisik_indirim_panosu():
    urunler = [
        ('1. Mont (1000 TL)', '1. İndirim: %20', 'Ek Kasa: %10', MAVI, MAVI_A),
        ('2. Bot (600 TL)', '1. İndirim: %25', 'Ek Kasa: %10', YES, YES_A),
        ('3. Çanta (500 TL)', '1. İndirim: %30', 'Ek Kasa: %10', TUR, TUR_A),
        ('4. Kazak (400 TL)', '1. İndirim: %15', 'Ek Kasa: %10', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(urunler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 22, bas, 9.3, r)
        ic += yazi(x + 41, 44, s1, 9.1, LAC)
        ic += yazi(x + 41, 63, s2, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Dört ürüne uygulanan ardışık indirim oranları panosu.', 15)


def mert_butce_plani():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 22, 'MERT’İN AYLIK BÜTÇE PLANI · TOPLAM GELİR: 3000 TL', 10.2, YESIL_K)
    ic += yazi(180, 44, '• Ulaşım: Dörtte biri (%25)   |   • Yemek: %35 (İlk toplam = %60)', 9.6, LAC, ince=True)
    ic += yazi(180, 64, '• Kitap Alışverişi: Kalan paranın 0,3’ü   →   Son Kalan Tasarruf = ? TL', 9.7, YESIL_K)
    return svg(360, 88, ic, '3000 TL bütçenin kesir, yüzde ve ondalık harcama dağılımı.', 15)


def terzi_kumas_atolyesi():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Ceket Dikimi', 10.3, TUR)
    ic += yazi(91, 44, 'Toplam: 24 m kumaş', 9.8, LAC)
    ic += yazi(91, 64, 'Dörtte biri (%25) ceket oldu', 9.4, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, '2. Yelek Dikimi', 10.3, MAVI)
    ic += yazi(269, 44, 'Kalan kumaş ÷ 0,75 m', 9.8, LAC)
    ic += yazi(269, 64, 'Toplam Yelek Sayısı = ?', 9.7, MAVI)
    return svg(360, 88, ic, '24 metre kumaştan ceket ve 0,75 metrelik yelek dikimi.', 15)


def manav_kar_hesabi_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'Alış ve Fire Bilgisi', 10.3, CAM)
    ic += yazi(91, 44, '80 kg armut × 22,5 TL', 9.7, LAC)
    ic += yazi(91, 64, 'Fire: %10’u ezildi (8 kg)', 9.4, KIR, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Satış ve Net Kâr', 10.3, YESIL_K)
    ic += yazi(269, 44, 'Sağlam: 72 kg × 30 TL', 9.7, LAC)
    ic += yazi(269, 64, 'Net Kâr = Satış − Alış = ?', 9.5, YESIL_K)
    return svg(360, 88, ic, 'Manavın 80 kg armut alış, fire ve satış kârı hesabı.', 15)


def problem_cozme_genelleme_adimlari():
    adimlar = [
        ('1. Temsil', 'Şerit ve tablo çiz', MAVI, MAVI_A),
        ('2. Ortak Dil', 'Çevir ve çöz', YES, YES_A),
        ('3. Kontrol', 'Tahmin ve sağlama', TUR, TUR_A),
        ('4. Genelleme', 'Yeni problem kur', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 54, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Çok adımlı problem çözme ve genelleme basamakları.', 15)


def problem_kurma_islem_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'PROBLEM KURMA KARTI · MATEMATİKSEL İFADE', 10.3, MOR)
    ic += yazi(180, 45, 'İşlem: 360 × (1 − 0,25 − 0,35)', 10.4, LAC)
    ic += yazi(180, 66, 'Bütün = 360 · 1. Harcama = Çeyreği (0,25) · 2. Harcama = Bütünün 0,35’i', 9.2, LAC, ince=True)
    return svg(360, 88, ic, 'Verilen çok adımlı matematiksel ifadeye uygun problem kurma kartı.', 15)


def kisa_yol_zihinden_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Terim · Çarpma Kısa Yolu', 10.0, MAVI)
    ic += yazi(91, 45, '640 × 0,25 = ?', 10.4, LAC)
    ic += yazi(91, 65, 'İpucu: 0,25 ile çarpmak = 4’e bölmek', 8.9, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Terim · Bölme Kısa Yolu', 10.0, TUR)
    ic += yazi(269, 45, '45 ÷ 0,5 = ?', 10.4, LAC)
    ic += yazi(269, 65, 'İpucu: 0,5’e bölmek = 2 ile çarpmak', 8.9, LAC, ince=True)
    return svg(360, 88, ic, 'Ondalık çarpma ve bölmede birim kesir kısa yolları kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kalanin_kesri_serit()
    s[2]['gorsel'] = ardisik_indirim_panosu()
    s[5]['gorsel'] = mert_butce_plani()
    s[6]['gorsel'] = terzi_kumas_atolyesi()
    s[7]['gorsel'] = manav_kar_hesabi_karti()
    s[8]['gorsel'] = problem_cozme_genelleme_adimlari()
    s[9]['gorsel'] = problem_kurma_islem_karti()
    s[11]['gorsel'] = kisa_yol_zihinden_karti()
