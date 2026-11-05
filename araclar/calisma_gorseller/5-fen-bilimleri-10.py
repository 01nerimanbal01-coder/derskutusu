"""5. sınıf Fen Bilimleri 10. hafta (Kütle ve Ağırlık İlişkisi, Yer Çekimi Kuvveti ve Konuma Göre Ağırlık Değişimi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kesif_robotu_dunya_ay():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Dünya Yüzeyi Ölçümü', 10.3, MAVI)
    ic += yazi(91, 44, 'Robotun Kütlesi = 36 kg', 10.0, LAC)
    ic += yazi(91, 65, 'Dünya Ağırlığı = ? N (1 kg ≈ 10 N)', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Ay Yüzeyi Ölçümü', 10.3, TUR)
    ic += yazi(269, 44, 'Ay’da Kütle = ? kg', 10.0, LAC)
    ic += yazi(269, 65, 'Ay’da Ağırlık = ? N (6’da 1’i)', 9.4, TUR, ince=True)
    return svg(360, 88, ic, '36 kg kütleli keşif robotunun Dünya ve Ay ölçümleri.', 15)


def dort_cisim_kutle_kartlari():
    kartlar = [
        ('1. Çelik Küre', 'Kütle: 6 kg', MAVI, MAVI_A),
        ('2. Kaya Örneği', 'Kütle: 12 kg', YES, YES_A),
        ('3. Uydu Parçası', 'Kütle: 30 kg', TUR, TUR_A),
        ('4. Oksijen Tüpü', 'Kütle: 48 kg', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.8, LAC)
    return svg(360, 84, ic, 'Farklı kütlelere sahip dört cismin ölçüm kartları.', 15)


def dag_kesiti_yukseklik_sema():
    noktalar = [
        ('P Noktası', 'Deniz Kıyısı (0 m)', 'Merkeze en yakın', MAVI, MAVI_A),
        ('R Noktası', 'Dağ Yamacı (1800 m)', 'Orta yükseklik', YES, YES_A),
        ('S Noktası', 'Dağ Zirvesi (3900 m)', 'Merkeze en uzak', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(noktalar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 22, bas, 10.3, r)
        ic += yazi(x + 56, 45, s1, 9.6, LAC)
        ic += yazi(x + 56, 66, s2, 9.3, LAC, ince=True)
    return svg(360, 88, ic, 'Deniz kıyısı P, yamaç R ve zirve S noktalarında ağırlık karşılaştırması.', 15)


def geoit_kutup_ekvator_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'K · Kuzey Kutbu (Basık)', 10.2, MAVI)
    ic += yazi(91, 44, 'Yerin merkezine DAHA YAKIN', 9.5, LAC)
    ic += yazi(91, 65, 'Yer çekimi kuvveti en fazla', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'M · Ekvator Çizgisi (Şişkin)', 10.2, MOR)
    ic += yazi(269, 44, 'Yerin merkezine DAHA UZAK', 9.5, LAC)
    ic += yazi(269, 65, 'M’den K’ye gidilirse ne olur?', 9.4, MOR, ince=True)
    return svg(360, 88, ic, 'Dünya üzerinde Ekvator M ve Kuzey Kutbu K noktaları.', 15)


def kutle_agirlik_benzerlik_fark():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Ortak Yön (Benzerlik)', 10.2, YESIL_K)
    ic += yazi(91, 44, 'Madde miktarı (kütle) artarsa', 9.5, LAC, ince=True)
    ic += yazi(91, 64, 'ağırlık da doğru orantılı artar.', 9.5, YESIL_K)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'Temel Ayrım (Farklılık)', 10.2, TUR)
    ic += yazi(269, 44, 'Kütle: Terazi · kg · Değişmez', 9.5, LAC)
    ic += yazi(269, 64, 'Ağırlık: Dinamometre · N · Değişir', 9.3, TUR)
    return svg(360, 88, ic, 'Kütle ve ağırlığın benzerlik ve farklılık karşılaştırması.', 15)


def dort_konum_agirlik_siralama():
    kartlar = [
        ('Konum A', 'Ay Yüzeyi', '6’da 1 çekim', MOR, MOR_A),
        ('Konum B', 'Kutup Kıyısı', 'En güçlü çekim', MAVI, MAVI_A),
        ('Konum C', 'Ekvator Zirve', 'Dünya’da en az', TUR, TUR_A),
        ('Konum D', 'Ekvator Kıyısı', 'Orta çekim', YES, YES_A),
    ]
    ic = ''
    for i, (bas, yer, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 22, bas, 10.1, r)
        ic += yazi(x + 41, 44, yer, 9.5, LAC)
        ic += yazi(x + 41, 64, alt, 8.9, LAC, ince=True)
    return svg(360, 86, ic, 'Aynı çantanın dört farklı konumdaki çekim karşılaştırması.', 15)


def x_ve_y_cisimleri_deneyi():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'X Cismi · Dünya’da Ölçüm', 10.2, MAVI)
    ic += yazi(91, 44, 'Uzama: 3 Bölme (30 N)', 9.9, LAC)
    ic += yazi(91, 65, '(Her 1 bölme = 10 N)', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Y Cismi · Ay’da Ölçüm', 10.2, YESIL_K)
    ic += yazi(269, 44, 'Uzama: 2 Bölme (20 N)', 9.9, LAC)
    ic += yazi(269, 65, '(Dünya çekimi Ay’ın 6 katıdır)', 9.3, YESIL_K, ince=True)
    return svg(360, 88, ic, 'X cisminin Dünya’da, Y cisminin Ay’da dinamometre ölçümü.', 15)


def esit_kollu_terazi_ay_deneyi():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Dünya’da Eşit Kollu Terazi', 10.0, TUR)
    ic += yazi(91, 44, 'Sol Kefe: 15 kg = Sağ: Kaya', 9.7, LAC)
    ic += yazi(91, 65, 'Durum: Yatay Denge Sağlandı', 9.4, TUR, ince=True)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 22, '2. Ay Yüzeyinde Aynı Terazi', 10.0, CAM)
    ic += yazi(269, 44, 'Sol Kefe: 15 kg = Sağ: Kaya', 9.7, LAC)
    ic += yazi(269, 65, 'Denge neden hiç bozulmaz?', 9.4, CAM)
    return svg(360, 88, ic, 'Dünya ve Ay’da eşit kollu terazi dengesinin korunması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kesif_robotu_dunya_ay()
    s[2]['gorsel'] = dort_cisim_kutle_kartlari()
    s[5]['gorsel'] = dag_kesiti_yukseklik_sema()
    s[6]['gorsel'] = geoit_kutup_ekvator_karti()
    s[7]['gorsel'] = kutle_agirlik_benzerlik_fark()
    s[8]['gorsel'] = dort_konum_agirlik_siralama()
    s[9]['gorsel'] = x_ve_y_cisimleri_deneyi()
    s[11]['gorsel'] = esit_kollu_terazi_ay_deneyi()
