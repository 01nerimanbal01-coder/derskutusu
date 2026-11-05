"""8. sınıf Matematik 9. hafta (Kareköklü İfadelerde Toplama-Çıkarma ve Doğal Sayı Yapan Çarpanlar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 11-12 pt (K150 EK); tek parça vektörel karekök sembolü (K196/K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K, GRI = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="11.2" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="10.5" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, katsayi, ic_metin, renk=LAC):
    """cx merkezli, y taban çizgili, üst çizgisi bitişik vektörel karekök ifadesi çizer."""
    boy = 11.5
    ic_str = str(ic_metin)
    kat_str = str(katsayi) if katsayi else ''
    w_ic = max(13, len(ic_str) * 7.2 + 4)
    w_kat = len(kat_str) * 7.2 + (2 if kat_str else 0)
    toplam_w = w_kat + 10 + w_ic
    sol = cx - toplam_w / 2
    out = ''
    if kat_str:
        out += yazi(sol + w_kat - 1, y, kat_str, renk, 'end')
    rx = sol + w_kat
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.5
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.5:.1f} {orta_y - 1.5:.1f} '
            f'L{rx + 5.5:.1f} {alt_y:.1f} L{rx + 9.5:.1f} {ust_y:.1f} '
            f'H{rx + 10 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 10 + w_ic / 2, y, ic_str, renk, 'middle')
    return out


def dikdortgen_cerceve_cevre():
    """Soru 2 (s[1]): Kısa kenarı kök 28 cm ve uzun kenarı kök 175 cm olan dikdörtgen çerçeve."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Dikdörtgen Resim Çerçevesi · Çevre Uzunluğu', MAVI)
    ic += kutu(64, 28, 190, 44, '#fff', MAVI, 6, 1.5)
    ic += yazi(159, 54, 'Çevre = ? cm', MAVI)
    ic += kok_ciz(150, 84, '', '175', LAC)
    ic += yazi(180, 84, 'cm', LAC, 'start', True)
    ic += kok_ciz(286, 54, '', '28', TUR)
    ic += yazi(314, 54, 'cm', TUR, 'start', True)
    return svg(360, 94, ic, 'Kısa kenarı karekök 28 cm ve uzun kenarı karekök 175 cm olan dikdörtgen çerçeve.', 15)


def carpan_tablo_kartlari():
    """Soru 3 (s[2]): kök 50, kök 75, kök 40, kök 99 doğal sayı çarpan kartları."""
    kartlar = [
        (4, '1. Sayı', '50', '5', '2', MAVI, MAVI_A),
        (93, '2. Sayı', '75', '5', '3', YES, YES_A),
        (182, '3. Sayı', '40', '2', '10', TUR, TUR_A),
        (271, '4. Sayı', '99', '3', '11', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s_ic, kat, k_ic, r, z in kartlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 21, bas, r)
        ic += kok_ciz(x + 42, 46, '', s_ic, LAC)
        ic += kok_ciz(x + 42, 72, kat, k_ic, r)
    return svg(360, 88, ic, 'Dört kareköklü ifadenin a kök b dönüşüm kartları.', 14)


def carpan_carki_72():
    """Soru 6 (s[5]): Merkezde kök 72 = 6 kök 2 ve çevresinde 4 seçenek."""
    ic = kutu(4, 4, 352, 88, MOR_A, MOR, 8)
    ic += yazi(180, 20, 'Doğal Sayı Çarpan Çarkı · Merkez: 6 kök 2', MOR)
    ic += kutu(126, 28, 108, 54, '#fff', MOR, 8, 1.5)
    ic += yazi(180, 45, 'Merkez İfade', MOR)
    ic += kok_ciz(180, 70, '', '72', LAC)

    ic += kutu(12, 28, 104, 25, MAVI_A, MAVI, 6)
    ic += yazi(32, 45, 'A)', MAVI)
    ic += kok_ciz(72, 45, '', '12', LAC)

    ic += kutu(12, 57, 104, 25, TUR_A, TUR, 6)
    ic += yazi(32, 74, 'B)', TUR)
    ic += kok_ciz(72, 74, '', '20', LAC)

    ic += kutu(244, 28, 104, 25, YES_A, YES, 6)
    ic += yazi(264, 45, 'C)', YESIL_K)
    ic += kok_ciz(304, 45, '', '50', LAC)

    ic += kutu(244, 57, 104, 25, KIR_A, KIR, 6)
    ic += yazi(264, 74, 'D)', KIR)
    ic += kok_ciz(304, 74, '', '48', LAC)
    return svg(360, 96, ic, 'Merkezde karekök 72 bulunan doğal sayı çarpan çarkı.', 15)


def kablo_kesim_modeli():
    """Soru 7 (s[6]): Boyu kök 300 m olan kablodan kök 75 m ve kök 12 m kesilmesi."""
    ic = kutu(4, 4, 352, 84, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Elektrik Kablosu Kesim Modeli · Toplam: 10 kök 3 m', KAHVE)
    ic += kutu(14, 28, 110, 34, TUR_A, TUR, 6)
    ic += yazi(42, 50, '1. Parça:', TUR, 'center', True)
    ic += kok_ciz(95, 50, '', '75', TUR)

    ic += kutu(130, 28, 96, 34, MOR_A, MOR, 6)
    ic += yazi(156, 50, '2. Parça:', MOR, 'center', True)
    ic += kok_ciz(202, 50, '', '12', MOR)

    ic += kutu(232, 28, 114, 34, YES_A, YES, 6)
    ic += yazi(289, 50, 'Kalan = ? m', YESIL_K)
    ic += yazi(180, 78, 'Başlangıçtaki Toplam Uzunluk: karekök 300 m', LAC, 'middle', True)
    return svg(360, 92, ic, 'Karekök 300 metrelik kablodan karekök 75 ve karekök 12 metrelik parçaların kesilmesi.', 15)


def uc_kare_karton_kl():
    """Soru 8 (s[7]): Alanları 45, 20 ve 5 cm² olan yan yana üç kare karton."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Yan Yana Üç Karesel Karton · |KL| Uzunluğu', MAVI)
    ic += kutu(58, 26, 94, 48, '#fff', MAVI, 5)
    ic += yazi(105, 54, '45 cm²', MAVI)
    ic += kutu(152, 34, 76, 40, '#fff', TUR, 5)
    ic += yazi(190, 58, '20 cm²', TUR)
    ic += kutu(228, 44, 56, 30, '#fff', YES, 5)
    ic += yazi(256, 63, '5 cm²', YESIL_K)
    ic += yazi(46, 74, 'K', KIR)
    ic += yazi(296, 74, 'L', KIR)
    ic += yazi(180, 86, '|KL| Toplam Taban Uzunluğu = ? cm', LAC)
    return svg(360, 96, ic, 'Alanları 45, 20 ve 5 santimetrekare olan yan yana üç kare.', 15)


def toplama_cikarma_akis():
    """Soru 9 (s[8]): kök 147 - kök 48 + kök 27 işleminin 4 adımı."""
    adlar = [
        ('1. Adım', 'Çarpan ayır', MAVI, MAVI_A),
        ('2. Adım', 'a kök b yaz', TUR, TUR_A),
        ('3. Adım', '(7 - 4 + 3)', MOR, MOR_A),
        ('4. Adım', 'Sonuç: 6 kök 3', YES, YES_A),
    ]
    ic = kutu(4, 4, 352, 82, '#fff', GRI, 8)
    ic += yazi(180, 20, 'Kök İçlerini Eşitleyerek Toplama ve Çıkarma Sırası', LAC)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 26, 78, 50, z, r, 7)
        ic += yazi(x + 39, 44, ust, r)
        ic += yazi(x + 39, 64, alt, LAC, 'middle', True)
    return svg(360, 90, ic, 'Kareköklü ifadelerde toplama ve çıkarma 4 adımlı çözüm şeması.', 14)


def klmn_dort_sayi_karti():
    """Soru 10 (s[9]): K=kök 20, L=kök 27, M=kök 45, N=kök 75 kartları."""
    kartlar = [
        (4, 'K Kartı', '20', '2', '5', MAVI, MAVI_A),
        (93, 'L Kartı', '27', '3', '3', TUR, TUR_A),
        (182, 'M Kartı', '45', '3', '5', YES, YES_A),
        (271, 'N Kartı', '75', '5', '3', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s_ic, kat, k_ic, r, z in kartlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 21, bas, r)
        ic += kok_ciz(x + 42, 46, '', s_ic, LAC)
        ic += kok_ciz(x + 42, 72, kat, k_ic, r)
    return svg(360, 88, ic, 'K, L, M ve N kareköklü sayı kartları.', 14)


def dikdortgen_cevre_carpan_karti():
    """Soru 12 (s[11]): Kenarları kök 12 cm ve kök 48 cm olan dikdörtgen."""
    ic = kutu(4, 4, 352, 84, YES_A, YES, 8)
    ic += yazi(180, 20, 'Dikdörtgenin Çevresi ve Doğal Sayı Çarpanı', YESIL_K)
    ic += kutu(54, 28, 176, 44, '#fff', YES, 6)
    ic += yazi(142, 54, 'Çevre = 2 · (a + b)', YESIL_K)
    ic += kok_ciz(135, 82, '', '48', LAC)
    ic += yazi(162, 82, 'cm', LAC, 'start', True)
    ic += kok_ciz(268, 54, '', '12', TUR)
    ic += yazi(296, 54, 'cm', TUR, 'start', True)
    return svg(360, 92, ic, 'Kenarları karekök 12 cm ve karekök 48 cm olan dikdörtgen.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dikdortgen_cerceve_cevre()
    s[2]['gorsel'] = carpan_tablo_kartlari()
    s[5]['gorsel'] = carpan_carki_72()
    s[6]['gorsel'] = kablo_kesim_modeli()
    s[7]['gorsel'] = uc_kare_karton_kl()
    s[8]['gorsel'] = toplama_cikarma_akis()
    s[9]['gorsel'] = klmn_dort_sayi_karti()
    s[11]['gorsel'] = dikdortgen_cevre_carpan_karti()
