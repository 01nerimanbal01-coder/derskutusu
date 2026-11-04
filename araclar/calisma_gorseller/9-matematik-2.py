"""9. sınıf Matematik 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; tek parça vektörel kök sembolü; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, katsayi, ic_metin, renk=LAC, boy=11, ince=False):
    """cx merkezli, y taban çizgili, üst çizgisi bitişik vektörel karekök ifadesi çizer."""
    ic_str = str(ic_metin)
    kat_str = str(katsayi) if katsayi else ''
    w_ic = max(12, len(ic_str) * (boy * 0.62) + 4)
    w_kat = len(kat_str) * (boy * 0.62) + (2 if kat_str else 0)
    toplam_w = w_kat + 10 + w_ic
    sol = cx - toplam_w / 2
    out = ''
    if kat_str:
        out += yazi(sol + w_kat - 1, y, kat_str, boy, renk, 'end', ince=ince)
    rx = sol + w_kat
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.5
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.5:.1f} {orta_y - 1.5:.1f} '
            f'L{rx + 5.5:.1f} {alt_y:.1f} L{rx + 9.5:.1f} {ust_y:.1f} '
            f'H{rx + 10 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.3" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 10 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    return out


def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
    ic += kok_ciz(34, 30, '', 'a', MAVI, 11) + yazi(50, 30, '·', 11, MAVI) + kok_ciz(66, 30, '', 'b', MAVI, 11)
    ic += kok_ciz(50, 62, '', 'a·b', LAC, 10.5, ince=True)
    ic += kok_ciz(136, 30, '(', 'a)²', YES, 11) + yazi(136, 62, 'a (a ≥ 0)', 10.5, LAC, ince=True)
    ic += kok_ciz(222, 30, '', 'a : b', TUR, 11)
    ic += kok_ciz(204, 62, '', 'a', LAC, 10, ince=True) + yazi(222, 62, ':', 10.5, LAC, ince=True) + kok_ciz(240, 62, '', 'b', LAC, 10, ince=True)
    ic += yazi(308, 30, 'Kök Tanımı', 10.5, MOR) + kok_ciz(308, 62, '', 'a', LAC, 10.5, ince=True)
    return svg(360, 100, ic, 'Köklü sayı kuralları eşitlik kartları', 34)


def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'KÖKLÜ İFADELERDE ÇIKARMA VE SADELEŞTİRME', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI)
    ic += kok_ciz(68, 52, '', '75', LAC, 12) + yazi(96, 52, '−', 12, LAC) + kok_ciz(122, 52, '', '12', LAC, 12)
    ic += yazi(150, 52, '=', 12, LAC) + kok_ciz(180, 52, '5', '3', MAVI, 12) + yazi(208, 52, '−', 12, LAC) + kok_ciz(236, 52, '2', '3', MAVI, 12)
    ic += yazi(264, 52, '=', 12, LAC) + kok_ciz(294, 52, '3', '3', YES, 12)
    ic += yazi(180, 72, 'Kök içleri eşitlendiğinde katsayılar arasında çıkarma yapılır.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Köklü ifade çıkarma işlemi çözümü', 34)


def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(142, 28, 'KÖK DIŞINA ÇIKARMA ·', 11, TUR) + kok_ciz(228, 28, 'a', 'b', TUR, 11) + yazi(268, 28, 'BİÇİMİ', 11, TUR)
    ic += kok_ciz(64, 52, '', '48', LAC, 12) + yazi(92, 52, '=', 12, LAC) + kok_ciz(132, 52, '', '16 · 3', MAVI, 11.5)
    ic += yazi(172, 52, '=', 12, LAC) + kok_ciz(202, 52, '', '16', MAVI, 11.5) + yazi(224, 52, '·', 12, LAC) + kok_ciz(244, 52, '', '3', MAVI, 11.5)
    ic += yazi(266, 52, '=', 12, LAC) + kok_ciz(296, 52, '4', '3', YES, 12)
    ic += yazi(180, 70, 'Tam kare çarpan kök dışına katsayı olarak çıkar.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Kök dışına çıkarma kartı', 34)


def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Toplama', 'Kök içleri aynı', MAVI, MAVI_A), ('Çarpma', 'Kök derecesi aynı', TUR, TUR_A), ('Eşlenik', 'Paydayı kurtar', YES, YES_A), ('Mutlak Değer', '', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        if alt:
            ic += yazi(x + 40, 62, alt, 9, LAC, ince=True)
    ic += kok_ciz(294, 62, '', 'x²', LAC, 9.5, ince=True) + yazi(324, 62, '= |x|', 9.5, LAC, ince=True)
    return svg(360, 98, ic, 'Köklü sayılar işlem kuralları panosu', 34)


def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Kesir', 'Paydayı incele', YES, YES_A), ('2. Eşlenik', '', MAVI, MAVI_A), ('3. Genişlet', 'Pay ve paydayı', TUR, TUR_A), ('4. Sadeleştir', 'Rasyonel payda', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c)
        if alt:
            ic += yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    ic += kok_ciz(116, 55, '', 'b', LAC, 9.5, ince=True) + yazi(146, 55, 'ile çarp', 9, LAC, ince=True)
    return svg(360, 96, ic, 'Paydayı rasyonel yapma basamakları akış şeması', 34)


def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(148, 22, 'SAYI DOĞRUSUNDA', 11, CAM) + kok_ciz(216, 22, '', '50', CAM, 11) + yazi(256, 22, 'DEĞERİ', 11, CAM)
    ic += f'<line x1="30" y1="52" x2="330" y2="52" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<circle cx="80" cy="52" r="3" fill="{LAC}"/><circle cx="180" cy="52" r="3" fill="{LAC}"/><circle cx="280" cy="52" r="3" fill="{LAC}"/>'
    ic += yazi(66, 42, '6 =', 10, SOLUK, ince=True) + kok_ciz(92, 42, '', '36', SOLUK, 10, ince=True)
    ic += yazi(166, 42, '7 =', 10, LAC) + kok_ciz(192, 42, '', '49', LAC, 10)
    ic += yazi(266, 42, '8 =', 10, SOLUK, ince=True) + kok_ciz(292, 42, '', '64', SOLUK, 10, ince=True)
    ic += f'<polygon points="195,47 190,38 200,38" fill="{KIR}"/>'
    ic += kok_ciz(112, 72, '', '50', KIR, 10) + yazi(210, 72, '(7 ile 8 arasında, 7\'ye çok yakın)', 10, KIR)
    return svg(360, 96, ic, 'Sayı doğrusunda kök 50 konumu şeması', 34)


def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    kartlar = [(MAVI, MAVI_A), (TUR, TUR_A), (YES, YES_A), (MOR, MOR_A)]
    for i, (c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
    ic += kok_ciz(34, 32, '', '2', MAVI, 10.5) + yazi(50, 32, '·', 10.5, MAVI) + kok_ciz(66, 32, '', '8', MAVI, 10.5)
    ic += yazi(26, 62, '=', 9.5, LAC, ince=True) + kok_ciz(48, 62, '', '16', LAC, 9.5, ince=True) + yazi(72, 62, '= 4', 9.5, LAC, ince=True)
    ic += kok_ciz(118, 32, '', '50', TUR, 10.5) + yazi(138, 32, ':', 10.5, TUR) + kok_ciz(156, 32, '', '2', TUR, 10.5)
    ic += yazi(112, 62, '=', 9.5, LAC, ince=True) + kok_ciz(134, 62, '', '25', LAC, 9.5, ince=True) + yazi(158, 62, '= 5', 9.5, LAC, ince=True)
    ic += kok_ciz(208, 32, '', '27', YES, 10.5) + yazi(236, 32, ': 3', 10.5, YES)
    ic += yazi(198, 62, '=', 9.5, LAC, ince=True) + kok_ciz(220, 62, '3', '3', LAC, 9.5, ince=True) + yazi(246, 62, ': 3', 9.5, LAC, ince=True)
    ic += kok_ciz(308, 32, '(', '5)²', MOR, 10.5) + yazi(308, 62, '= 5', 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Köklü sayı işlem sonuçları eşleştirme kartı', 34)


def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: K - Ö - K - L - Ü', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'Ö'), ('3', 'K'), ('4', 'L'), ('5', 'Ü')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Köklü şifresi harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
