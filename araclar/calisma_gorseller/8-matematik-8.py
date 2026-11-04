"""8. sınıf Matematik 8. hafta (Kareköklü İfadelerde Çarpma, Bölme, Paydayı Rasyonel Yapma ve Toplama-Çıkarma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); kesirler dikey (K155); tek parça vektörel kök sembolü."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, katsayi, ic_metin, renk=LAC):
    """cx merkezli, y taban çizgili, üst çizgisi bitişik vektörel karekök ifadesi çizer."""
    boy = 12
    ic_str = str(ic_metin)
    kat_str = str(katsayi) if katsayi else ''
    w_ic = max(13, len(ic_str) * 7.5 + 4)
    w_kat = len(kat_str) * 7.5 + (2 if kat_str else 0)
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


def dogal_sayi_carpan_sema():
    """Soru 1: Karekök 24 = 2 kök 6 ifadesini doğal sayı yapan çarpan modeli."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Doğal Sayı Yapan Çarpan Bulma Modeli', KAHVE)
    ic += kutu(12, 28, 102, 56, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(63, 46, '1. a kök b Yaz', MAVI)
    ic += kok_ciz(42, 72, '', '24', LAC)
    ic += yazi(66, 72, '=', MAVI)
    ic += kok_ciz(88, 72, '2', '6', MAVI)

    ic += kutu(125, 28, 102, 56, TUR_A, TUR, 7, 1.3)
    ic += yazi(176, 46, '2. Çarpan Seç', TUR)
    ic += kok_ciz(176, 72, '', '6', TUR)

    ic += kutu(238, 28, 108, 56, YES_A, YES, 7, 1.3)
    ic += yazi(292, 46, '3. Doğal Sayı', YESIL_K)
    ic += yazi(292, 72, '2 · 6 = 12', YESIL_K)
    return svg(360, 96, ic, 'Karekök 24 eşittir 2 kök 6 ifadesinin kök 6 ile çarpılarak 12 doğal sayısına dönüşme modeli.')


def dikdortgen_pano_alan():
    """Soru 3: Kısa kenarı 2 kök 3 dm ve uzun kenarı 5 kök 6 dm olan dikdörtgen pano."""
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Dikdörtgen Afiş Panosu · Alan Hesabı', MAVI)
    ic += kutu(66, 28, 196, 52, '#fff', MAVI, 6, 1.5)
    ic += yazi(164, 58, 'Alan = ? dm²', MAVI)
    ic += kok_ciz(152, 92, '5', '6', LAC)
    ic += yazi(186, 92, 'dm', LAC, 'start', True)
    ic += kok_ciz(294, 58, '2', '3', TUR)
    ic += yazi(326, 58, 'dm', TUR, 'start', True)
    return svg(360, 100, ic, 'Kısa kenarı 2 kök 3 dm, uzun kenarı 5 kök 6 dm olan dikdörtgen pano.')


def dort_islem_kartlari():
    """Soru 5: Dört işlem kartı (III. kart hatalı: kök 27 + kök 12 = kök 39)."""
    kartlar = [
        ('I. Kart · Çarpma', '30', MAVI, MAVI_A),
        ('II. Kart · Bölme', '12', YES, YES_A),
        ('III. Kart · Toplama', 'Hatalı Toplam', KIR, KIR_A),
        ('IV. Kart · Rasyonel', 'Payda = 5', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sonuc, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, bas, r)
        if i == 0:
            ic += kok_ciz(x + 42, y + 37, '2', '5', LAC)
            ic += yazi(x + 68, y + 37, '·', LAC)
            ic += kok_ciz(x + 94, y + 37, '3', '5', LAC)
            ic += yazi(x + 134, y + 37, '= 30', r)
        elif i == 1:
            ic += kok_ciz(x + 42, y + 37, '20', '18', LAC)
            ic += yazi(x + 74, y + 37, ':', LAC)
            ic += kok_ciz(x + 98, y + 37, '5', '2', LAC)
            ic += yazi(x + 136, y + 37, '= 12', r)
        elif i == 2:
            ic += kok_ciz(x + 38, y + 37, '', '27', LAC)
            ic += yazi(x + 64, y + 37, 've', LAC, 'middle', True)
            ic += kok_ciz(x + 92, y + 37, '', '12', LAC)
            ic += yazi(x + 114, y + 37, '->', r)
            ic += kok_ciz(x + 140, y + 37, '', '39', r)
        else:
            ic += yazi(x + 42, y + 37, '15 :', LAC)
            ic += kok_ciz(x + 74, y + 37, '', '5', LAC)
            ic += yazi(x + 98, y + 37, '=', r)
            ic += kok_ciz(x + 126, y + 37, '3', '5', r)
    return svg(360, 100, ic, 'Dört kareköklü işlem kartı: I çarpma, II bölme, III hatalı toplama, IV paydayı rasyonel yapma.')


def alani_verilen_karton():
    """Soru 6: Alanı 36 cm² ve uzun kenarı 3 kök 2 cm olan dikdörtgen karton."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Alanı Verilen Dikdörtgenin Kenarını Bulma', YESIL_K)
    ic += kutu(56, 28, 190, 46, '#fff', YES, 6, 1.4)
    ic += yazi(151, 56, 'Alan = 36 cm²', YESIL_K)
    ic += kok_ciz(140, 88, '3', '2', LAC)
    ic += yazi(170, 88, 'cm', LAC, 'start', True)
    ic += yazi(296, 56, 'x = ? cm', TUR)
    return svg(360, 96, ic, 'Alanı 36 santimetrekare ve uzun kenarı 3 kök 2 santimetre olan dikdörtgen karton.')


def ucgen_parkur_cevre():
    """Soru 7: Kenarları kök 75 m, kök 48 m ve kök 27 m olan üçgen yürüyüş parkuru."""
    ic = kutu(4, 4, 352, 92, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Üçgen Yürüyüş Parkuru · Çevre Hesabı', KAHVE)
    ic += f'<polygon points="180,28 100,78 260,78" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += kok_ciz(110, 52, '', '75', MAVI)
    ic += kok_ciz(250, 52, '', '48', YESIL_K)
    ic += kok_ciz(180, 90, '', '27', MOR)
    return svg(360, 98, ic, 'Kenar uzunlukları karekök 75, karekök 48 ve karekök 27 metre olan üçgen parkur.')


def rasyonel_toplama_akis():
    """Soru 8: Paydayı rasyonel yapma ve toplama 4 adımlı akış şeması."""
    adlar = [
        ('1. Adım', 'Rasyonel yap', MAVI, MAVI_A),
        ('2. Adım', 'a kök b yaz', TUR, TUR_A),
        ('3. Adım', 'Kökleri eşitle', YES, YES_A),
        ('4. Adım', 'Katsayı işlemi', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 86, '#fff', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Kareköklü İfadelerde Çok Adımlı İşlem Sırası', LAC)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 52, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Paydayı rasyonel yapma ve kareköklü toplama 4 adımlı çözüm şeması.')


def hedef_tahtasi_carpan():
    """Soru 9: Merkezde kök 54 = 3 kök 6 ve çevresinde 4 çarpan bölgesi."""
    ic = kutu(4, 4, 352, 94, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Doğal Sayı Çarpanı Hedef Panosu', MOR)
    ic += kutu(126, 30, 108, 56, '#fff', MOR, 8, 1.6)
    ic += yazi(180, 48, 'Merkez Sayı', MOR)
    ic += kok_ciz(180, 72, '', '54', LAC)

    ic += kutu(12, 28, 104, 28, MAVI_A, MAVI, 6, 1.2)
    ic += yazi(38, 46, '1)', MAVI)
    ic += kok_ciz(74, 46, '', '6', LAC)

    ic += kutu(12, 60, 104, 28, YES_A, YES, 6, 1.2)
    ic += yazi(38, 78, '2)', YESIL_K)
    ic += kok_ciz(74, 78, '', '24', LAC)

    ic += kutu(244, 28, 104, 28, TUR_A, TUR, 6, 1.2)
    ic += yazi(270, 46, '3)', TUR)
    ic += kok_ciz(306, 46, '3', '6', LAC)

    ic += kutu(244, 60, 104, 28, KIR_A, KIR, 6, 1.2)
    ic += yazi(270, 78, '4)', KIR)
    ic += kok_ciz(306, 78, '2', '3', LAC)
    return svg(360, 102, ic, 'Merkezde karekök 54 ve çevresinde 4 çarpan bölgesi panosu.')


def tahta_cita_kesim():
    """Soru 12: Toplam boyu kök 128 cm olan çıtadan 3 adet kök 8 cm parça kesilmesi."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Tahta Çıta Kesim Modeli · Toplam Boy: 8 kök 2 cm', KAHVE)
    for i in range(3):
        x = 16 + i * 74
        ic += kutu(x, 30, 70, 34, TUR_A, TUR, 5, 1.3)
        ic += kok_ciz(x + 35, 52, '', '8', TUR)
    ic += kutu(242, 30, 102, 34, YES_A, YES, 5, 1.4)
    ic += yazi(293, 52, 'Kalan = ?', YESIL_K)
    ic += yazi(180, 82, 'Toplam Uzunluk: karekök 128 cm', LAC, 'middle', True)
    return svg(360, 96, ic, 'Toplam boyu karekök 128 cm olan çıtadan 3 adet karekök 8 cm parça kesilmesi.')


def iki_kare_fayans_ab():
    """Soru 13: Alanları 50 cm² ve 18 cm² olan yan yana iki karesel fayans."""
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Yan Yana İki Karesel Fayans · |AB| Uzunluğu', MAVI)
    ic += kutu(76, 26, 112, 50, '#fff', MAVI, 5, 1.4)
    ic += yazi(132, 55, 'Alan = 50 cm²', MAVI)
    ic += kutu(188, 38, 84, 38, '#fff', TUR, 5, 1.4)
    ic += yazi(230, 61, '18 cm²', TUR)
    ic += yazi(66, 78, 'A', KIR)
    ic += yazi(282, 78, 'B', KIR)
    ic += yazi(180, 90, '|AB| Toplam Kenar Uzunluğu = ? cm', LAC)
    return svg(360, 98, ic, 'Alanları 50 ve 18 santimetrekare olan iki karesel fayansın yan yana görünümü.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dogal_sayi_carpan_sema()
    s[2]['gorsel'] = dikdortgen_pano_alan()
    s[4]['gorsel'] = dort_islem_kartlari()
    s[5]['gorsel'] = alani_verilen_karton()
    s[6]['gorsel'] = ucgen_parkur_cevre()
    s[7]['gorsel'] = rasyonel_toplama_akis()
    s[8]['gorsel'] = hedef_tahtasi_carpan()
    s[11]['gorsel'] = tahta_cita_kesim()
    s[12]['gorsel'] = iki_kare_fayans_ab()
