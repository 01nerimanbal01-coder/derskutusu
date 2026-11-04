"""10. sınıf Matematik 1. hafta (Dik Üçgende Trigonometrik Oranlar ve Trigonometrik Özdeşlikler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def g0_trig_oranlar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('sin α', 'Karşı / Hipotenüs', MAVI, MAVI_A),
        ('cos α', 'Komşu / Hipotenüs', YES, YES_A),
        ('tan α', 'Karşı / Komşu', TUR, TUR_A),
        ('cot α', 'Komşu / Karşı', MOR, MOR_A)
    ]
    for i, (b, oran, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 13, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, oran, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Dört temel trigonometrik oran tanımı kartı', 34)


def g1_ucgen_6_8_10():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # 6-8-10 dik üçgeni çizimi
    # Köşeler: C(50, 78) - dik açı, A(50, 24), B(170, 78)
    ic += '<polygon points="50,24 50,78 170,78" fill="#e0ebfd" stroke="' + MAVI + '" stroke-width="1.8"/>'
    ic += f'<rect x="50" y="68" width="10" height="10" fill="none" stroke="{MAVI}" stroke-width="1"/>'
    ic += f'<circle cx="55" cy="73" r="1.5" fill="{MAVI}"/>'
    ic += yazi(40, 24, 'A', 11, LAC)
    ic += yazi(40, 82, 'C', 11, LAC)
    ic += yazi(180, 82, 'B (α)', 11, LAC)
    ic += yazi(32, 54, '6 br', 10, MAVI)
    ic += yazi(110, 90, '8 br', 10, MAVI)
    ic += yazi(118, 46, '10 br', 10, MAVI)

    # Sağ bilgi kutusu
    ic += kutu(200, 14, 150, 72, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(275, 34, 'tan α = 6 / 8 = 3/4', 11, LAC)
    ic += yazi(275, 52, 'cot α = 8 / 6 = 4/3', 11, LAC)
    ic += yazi(275, 72, 'tan α + cot α = 25/12', 11, TUR)
    return svg(360, 100, ic, '6-8-10 dik üçgeni ve tan-cot hesaplama şeması', 34)


def g2_ucgen_3_4_5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    # 3-4-5 dik üçgeni
    ic += '<polygon points="50,22 50,76 150,76" fill="#eaf8f0" stroke="' + YES + '" stroke-width="1.8"/>'
    ic += f'<rect x="50" y="66" width="10" height="10" fill="none" stroke="{YES}" stroke-width="1"/>'
    ic += yazi(36, 52, '3', 11, YES)
    ic += yazi(100, 86, '4', 11, YES)
    ic += yazi(108, 44, '5', 11, YES)
    ic += yazi(158, 80, 'x', 11, LAC)

    ic += kutu(180, 10, 166, 70, YES_A, YES, 6, 1.1)
    ic += yazi(263, 30, 'sin x = Karşı / Hip = 3/5', 10.5, LAC)
    ic += yazi(263, 50, 'Pisagor: 3² + 4² = 5²', 10.5, SOLUK, ince=True)
    ic += yazi(263, 68, 'cos x = Komşu / Hip = 4/5', 11, YES)
    return svg(360, 96, ic, '3-4-5 dik üçgeninde sinüs ve kosinüs oranı', 34)


def g3_ozdeslikler():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ozdeslikler = [
        ('sin²x + cos²x', '= 1', MAVI, MAVI_A),
        ('tan x · cot x', '= 1', YES, YES_A),
        ('sin x / cos x', '= tan x', TUR, TUR_A),
        ('α + β = 90°', 'sin α = cos β', MOR, MOR_A)
    ]
    for i, (b, sonuc, c, d) in enumerate(ozdeslikler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, sonuc, 12, LAC)
    return svg(360, 98, ic, 'Dört temel trigonometrik özdeşlik kartı', 34)


def g5_problem_akisi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. Modelle', 'Üçgeni çiz', YES, YES_A),
        ('2. Kenarlar', 'Açıya göre adlandır', MAVI, MAVI_A),
        ('3. Oran Seç', 'Uygun oranı bul', TUR, TUR_A),
        ('4. Çöz', 'Denklemden hesapla', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Trigonometrik problem çözme adımları şeması', 34)


def g6_cebirsel_kart():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'TRİGONOMETRİK SADELEŞTİRME KARTI', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 52, '(1 − cos²x) / sin x = sin²x / sin x', 12, LAC)
    ic += yazi(180, 70, '= sin x  (En sade biçim)', 12, CAM)
    return svg(360, 96, ic, 'Trigonometrik özdeşlikle sadeleştirme kartı', 34)


def g8_tumler_acilar():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    tumler = [
        ('sin 20°', 'cos 70°', MAVI, MAVI_A),
        ('tan 35°', 'cot 55°', TUR, TUR_A),
        ('cos 40°', 'sin 50°', YES, YES_A),
        ('cot 15°', 'tan 75°', MOR, MOR_A)
    ]
    for i, (sol, sag, c, d) in enumerate(tumler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, sol, 11, c)
        ic += f'<line x1="{x + 12}" y1="42" x2="{x + 68}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, sag, 11, LAC)
    return svg(360, 96, ic, 'Tümler açıların eşit trigonometrik değerleri', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: O - R - A - N', 11.5, YES)
    harfler = [('1', 'O'), ('2', 'R'), ('3', 'A'), ('4', 'N')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 25, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Oran şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_trig_oranlar()
    s[1]['gorsel'] = g1_ucgen_6_8_10()
    s[2]['gorsel'] = g2_ucgen_3_4_5()
    s[3]['gorsel'] = g3_ozdeslikler()
    s[5]['gorsel'] = g5_problem_akisi()
    s[6]['gorsel'] = g6_cebirsel_kart()
    s[8]['gorsel'] = g8_tumler_acilar()
    s[10]['gorsel'] = g10_sifre_seridi()
