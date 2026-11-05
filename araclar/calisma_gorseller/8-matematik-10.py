"""8. sınıf Matematik 10. hafta (Ondalık İfadelerin Karekökleri ve Gerçek Sayılar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); tek parça vektörel karekök ve dikey kesir (K155/K196)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="10.8" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="10.0" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, katsayi, ic_metin, renk=LAC):
    """cx merkezli, y taban çizgili, üst çizgisi bitişik vektörel karekök ifadesi çizer."""
    boy = 11.2
    ic_str = str(ic_metin)
    kat_str = str(katsayi) if katsayi else ''
    w_ic = max(14, len(ic_str) * 6.8 + 5)
    w_kat = len(kat_str) * 6.8 + (2 if kat_str else 0)
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


def bitisik_iki_kare_bahce():
    """Soru 2 (s[1]): Alanları 3,61 m² ve 1,96 m² olan bitişik iki kare bahçe."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8)
    ic += yazi(180, 19, 'Bitişik İki Karesel Bahçe · |AB| Kenar Uzunlukları Toplamı', MAVI)
    ic += kutu(68, 25, 118, 46, '#fff', MAVI, 5)
    ic += yazi(127, 52, 'Alan = 3,61 m²', MAVI)
    ic += kutu(186, 33, 98, 38, '#fff', YES, 5)
    ic += yazi(235, 56, 'Alan = 1,96 m²', YESIL_K)
    ic += yazi(56, 72, 'A', KIR)
    ic += yazi(296, 72, 'B', KIR)
    ic += yazi(180, 84, '|AB| Toplam Uzunluğu = ? m', LAC)
    return svg(360, 94, ic, 'Alanları 3,61 ve 1,96 metrekare olan bitişik iki kare bahçe.', 15)


def dort_ondalik_sayi_karti():
    """Soru 3 (s[2]): kök(1,69), kök(0,0064), kök(1,6), kök(2,89) kartları."""
    kartlar = [
        (4, '1. Kart', '1,69', 'Rasyonel (Q)', MAVI, MAVI_A),
        (93, '2. Kart', '0,0064', 'Kümesi: ?', YES, YES_A),
        (182, '3. Kart', '1,6', 'Kümesi: ?', TUR, TUR_A),
        (271, '4. Kart', '2,89', 'Kümesi: ?', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s_ic, alt, r, z in kartlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 21, bas, r)
        ic += kok_ciz(x + 42, 48, '', s_ic, LAC)
        ic += yazi(x + 42, 72, alt, r, ince=True)
    return svg(360, 88, ic, 'Dört ondalık kareköklü ifadeyi gösteren sayı kartları.', 14)


def ondalik_islem_panosu():
    """Soru 6 (s[5]): (kök 2,56 - kök 0,49) / kök 0,0081 dikey kesir panosu."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8)
    ic += yazi(180, 19, 'Ondalık Kareköklü İfadelerde Dört İşlem Panosu', KAHVE)
    # Pay kısmı
    ic += kok_ciz(135, 44, '', '2,56', MAVI)
    ic += yazi(180, 44, '-', LAC)
    ic += kok_ciz(225, 44, '', '0,49', TUR)
    # Kesir çizgisi
    ic += f'<line x1="92" y1="53" x2="268" y2="53" stroke="{LAC}" stroke-width="1.6"/>'
    # Payda kısmı
    ic += kok_ciz(180, 74, '', '0,0081', YESIL_K)
    return svg(360, 94, ic, 'Payında karekök 2,56 eksi karekök 0,49, paydasında karekök 0,0081 bulunan kesir.', 15)


def hedef_tahtasi_dort_bolme():
    """Soru 7 (s[6]): 4 bölmeli sayı hedef tahtası."""
    ic = kutu(4, 4, 172, 44, KIR_A, KIR, 7)
    ic += yazi(52, 29, 'I. Bölme:', KIR)
    ic += kok_ciz(126, 29, '', '0,4', LAC)

    ic += kutu(184, 4, 172, 44, MAVI_A, MAVI, 7)
    ic += yazi(236, 29, 'II. Bölme:', MAVI)
    ic += kok_ciz(312, 29, '-', '1,44', LAC)

    ic += kutu(4, 52, 172, 44, YES_A, YES, 7)
    ic += yazi(90, 77, 'III. Bölme: 0,555... (Devirli)', YESIL_K)

    ic += kutu(184, 52, 172, 44, MOR_A, MOR, 7)
    ic += yazi(236, 77, 'IV. Bölme:', MOR)
    ic += kok_ciz(314, 77, '', '0,0009', LAC)
    return svg(360, 100, ic, 'Dört bölmeden oluşan rasyonel ve irrasyonel sayı hedef tahtası.', 15)


def basamak_karti_1ab():
    """Soru 8 (s[7]): kök(1,ab) rasyonel sayı basamak kartı."""
    ic = kutu(4, 4, 352, 82, MOR_A, MOR, 8)
    ic += yazi(180, 21, 'Tam Kare Basamak Analizi Kartı (a ≠ 0, b ≠ 0)', MOR)
    ic += kutu(24, 28, 140, 48, '#fff', MOR, 6)
    ic += kok_ciz(94, 56, '', '1,ab', MOR)
    ic += kutu(180, 28, 156, 48, '#fff', YES, 6)
    ic += yazi(258, 47, 'Sonuç: Rasyonel Sayı (Q)', YESIL_K)
    ic += yazi(258, 66, '1ab üç basamaklı tam kare', LAC, ince=True)
    return svg(360, 90, ic, 'Karekök 1,ab ifadesinin rasyonel sayı olma koşulunu gösteren kart.', 14)


def devirli_karekok_akis():
    """Soru 9 (s[8]): 2,777... devirli sayısının karekök alma adımları."""
    adimlar = [
        (4, '1. Pay Bulma', '27 - 2 = 25', 'işlemini yap', MAVI, MAVI_A),
        (93, '2. Kesir Yazma', 'Paydaya 9 yaz', '(Kesir: 25 ve 9)', TUR, TUR_A),
        (182, '3. Kök Alma', 'Pay ve paydayı', 'kök dışına çıkar', MOR, MOR_A),
        (271, '4. Sonuç', 'Pay 5, Payda 3', '-> Rasyonel (Q)', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r)
        ic += yazi(x + 42, 44, s1, LAC, ince=True)
        ic += yazi(x + 42, 64, s2, LAC)
    return svg(360, 88, ic, 'Devirli ondalık sayının rasyonel kesre çevrilerek karekökünün alınması.', 14)


def gercek_sayilar_venn_semasi():
    """Soru 10 (s[9]): R = Q U I ve N C Z C Q küme şeması."""
    ic = kutu(4, 4, 352, 88, '#f1f5f9', LAC, 8)
    ic += yazi(180, 19, 'GERÇEK (REEL) SAYILAR KÜMESİ (R = Q ∪ I)', LAC)
    ic += kutu(12, 25, 216, 60, MAVI_A, MAVI, 7)
    ic += yazi(120, 41, 'Rasyonel Sayılar (Q): N ⊂ Z ⊂ Q', MAVI)
    ic += yazi(120, 59, 'Tam kare kökler · Kesirler · Devirliler', LAC, ince=True)
    ic += yazi(120, 76, 'Örnek: 0, 5, -9, 0,5, 0,333...', MAVI)

    ic += kutu(236, 25, 112, 60, KIR_A, KIR, 7)
    ic += yazi(292, 41, 'İrrasyonel (I)', KIR)
    ic += yazi(292, 59, 'π sayısı · Kök içi', LAC, ince=True)
    ic += yazi(292, 76, 'tam kare olmayanlar', KIR)
    return svg(360, 96, ic, 'Gerçek sayılar kümesini oluşturan Rasyonel (Q) ve İrrasyonel (I) ayrık kümeleri.', 15)


def kl_basamak_farki_karti():
    """Soru 12 (s[11]): K = kök(0,16) ve L = kök(1,6) karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8)
    ic += yazi(90, 22, 'K İfadesi (2 Ondalık Basamak)', YESIL_K)
    ic += kok_ciz(90, 48, 'K = ', '0,16', LAC)
    ic += yazi(90, 72, 'Pay: 16 · Payda: 100 (Tam kare)', YESIL_K, ince=True)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8)
    ic += yazi(270, 22, 'L İfadesi (1 Ondalık Basamak)', TUR)
    ic += kok_ciz(270, 48, 'L = ', '1,6', LAC)
    ic += yazi(270, 72, 'Pay: 16 · Payda: 10 (Tam kare değil)', TUR, ince=True)
    return svg(360, 90, ic, 'Karekök 0,16 ile karekök 1,6 ifadelerinin payda karşılaştırma kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bitisik_iki_kare_bahce()
    s[2]['gorsel'] = dort_ondalik_sayi_karti()
    s[5]['gorsel'] = ondalik_islem_panosu()
    s[6]['gorsel'] = hedef_tahtasi_dort_bolme()
    s[7]['gorsel'] = basamak_karti_1ab()
    s[8]['gorsel'] = devirli_karekok_akis()
    s[9]['gorsel'] = gercek_sayilar_venn_semasi()
    s[11]['gorsel'] = kl_basamak_farki_karti()
