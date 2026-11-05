"""10. sınıf Matematik 2. hafta (Birim Çember, Geniş Açılar ve Yönlü Açılar) çalışma kâğıdı görselleri.
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
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kok_ciz(cx, y, on_metin, ic_metin, son_metin='', renk=LAC, boy=10, ince=False):
    ic_str = str(ic_metin)
    on_str = str(on_metin) if on_metin else ''
    son_str = str(son_metin) if son_metin else ''
    w_ic = max(12, len(ic_str) * (boy * 0.62) + 4)
    w_on = len(on_str) * (boy * 0.56) + (2 if on_str else 0)
    w_son = len(son_str) * (boy * 0.56) + (2 if son_str else 0)
    toplam_w = w_on + 10 + w_ic + w_son
    sol = cx - toplam_w / 2
    out = ''
    if on_str:
        out += yazi(sol + w_on - 1, y, on_str, boy, renk, 'end', ince=ince)
    rx = sol + w_on
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.5
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.5:.1f} {orta_y - 1.5:.1f} '
            f'L{rx + 5.5:.1f} {alt_y:.1f} L{rx + 9.5:.1f} {ust_y:.1f} '
            f'H{rx + 10 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.3" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 10 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    if son_str:
        out += yazi(rx + 10 + w_ic + 1, y, son_str, boy, renk, 'start', ince=ince)
    return out


def g0_genis_acilar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    degerler = [
        ('sin 150°', '+1/2', None, MAVI, MAVI_A),
        ('cos 120°', '-1/2', None, TUR, TUR_A),
        ('sin 135°', None, ('+', '2', '/2'), YES, YES_A),
        ('cos 135°', None, ('-', '2', '/2'), MOR, MOR_A)
    ]
    for i, (b, val, kok_bilgi, c, a) in enumerate(degerler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        if kok_bilgi:
            ic += kok_ciz(x + 40, 64, kok_bilgi[0], kok_bilgi[1], kok_bilgi[2], LAC, 11)
        else:
            ic += yazi(x + 40, 64, val, 12, LAC)
    return svg(360, 100, ic, 'Geniş açılarda trigonometrik oran kartları', 34)


def g1_birim_cember_120():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # Eksenler ve birim çember
    ic += f'<line x1="20" y1="50" x2="160" y2="50" stroke="{GRI}" stroke-width="1.2"/>' # x
    ic += f'<line x1="90" y1="10" x2="90" y2="90" stroke="{GRI}" stroke-width="1.2"/>' # y
    ic += f'<circle cx="90" cy="50" r="32" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    # 120 derece bitim kolu (cos 120 = -0.5 -> dx = -16, sin 120 = 0.866 -> dy = -28)
    ic += f'<line x1="90" y1="50" x2="74" y2="22" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<circle cx="74" cy="22" r="3" fill="{KIR}"/>'
    ic += yazi(60, 18, 'P(x,y)', 8.5, KIR)
    ic += yazi(155, 46, 'x', 8, LAC)
    ic += yazi(96, 16, 'y', 8, LAC)

    # Sağ hesap kutusu
    ic += kutu(176, 12, 170, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(261, 30, '120° BİTİM NOKTASI', 10, MAVI)
    ic += yazi(261, 48, 'cos 120° = -cos 60° = -1/2', 9.5, LAC)
    ic += kok_ciz(261, 64, 'sin 120° = sin 60° = ', '3', '/2', LAC, 9.2)
    ic += kok_ciz(261, 78, 'P = (-1/2, ', '3', '/2)', TUR, 9.8)
    return svg(360, 100, ic, 'Birim çember üzerinde 120 derecelik açı koordinatları', 34)


def g2_tam_kare():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += kutu(14, 12, 150, 76, '#eaf8f0', YES, 6, 1.2)
    ic += yazi(89, 28, 'TAM KARE AÇILIMI', 10, YES)
    ic += yazi(89, 48, '(sin x + cos x)²', 11, LAC)
    ic += yazi(89, 70, '= sin²x + cos²x + 2sinx cosx', 8.5, LAC)

    ic += kutu(176, 12, 170, 76, '#f4fbf6', YES, 6, 1.2)
    ic += yazi(261, 28, 'Özdeşlik Uygulaması', 10.5, YES)
    ic += yazi(261, 48, 'sin²x + cos²x = 1', 11, TUR)
    ic += yazi(261, 64, '1 + 2 sin x cos x = (4/3)²', 9.5, LAC, ince=True)
    ic += yazi(261, 78, 'sin x · cos x = 7/18', 10, MAVI)
    return svg(360, 100, ic, 'Trigonometrik tam kare özdeşlik çözümü', 34)


def g3_bolgeler():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    bolgeler = [
        ('1. Bölge (Dar)', 'sin: + / cos: +', '#f0f5fe'),
        ('2. Bölge (Geniş)', 'sin: + / cos: -', '#fef4e8'),
        ('3. Bölge', 'sin: - / cos: -', '#fdf0ef'),
        ('4. Bölge', 'sin: - / cos: +', '#f3effe')
    ]
    for i, (b, isar, bg) in enumerate(bolgeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, GRI, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, LAC)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{GRI}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, isar, 10, TUR)
    return svg(360, 100, ic, 'Koordinat düzleminde trigonometrik işaret tablosu', 34)


def g5_koordinat_akisi():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    adımlar = [
        ('1. Başlangıç', 'Pozitif x ekseni'),
        ('2. Dönme', 'Saat yönü tersi (+)'),
        ('3. P Noktası', 'Çember kesişimi'),
        ('4. Koordinat', '(cos α, sin α)')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#fef6ec', TUR, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, TUR)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{TUR}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Birim çemberde açı koordinatı bulma adımları', 34)


def g6_pisagor():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ic += kutu(14, 12, 140, 76, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(84, 30, 'TEMEL ÖZDEŞLİK', 10.5, CAM)
    ic += yazi(84, 52, 'sin²α + cos²α = 1', 12, LAC)
    ic += yazi(84, 72, 'Her reel açı için geçerlidir', 8.5, SOLUK, ince=True)

    ic += kutu(168, 12, 178, 76, '#f2fbfd', CAM, 6, 1.2)
    ic += yazi(257, 30, 'sin²140° + cos²140°', 11, CAM)
    ic += yazi(257, 52, 'Açı ölçüsü ne olursa olsun', 9, LAC, ince=True)
    ic += yazi(257, 72, 'Sonuç = 1', 14, TUR)
    return svg(360, 100, ic, 'Pisagor trigonometrik kare özdeşliği', 34)


def g8_yonlu_acilar():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 150, 76, '#ece4fd', MOR, 6, 1.2)
    ic += yazi(89, 28, 'Pozitif (+) Yön', 11, YES)
    ic += f'<circle cx="89" cy="54" r="18" fill="none" stroke="{YES}" stroke-width="2" stroke-dasharray="6,3"/>'
    ic += yazi(89, 56, 'İbre Tersi', 9, LAC)

    ic += kutu(176, 12, 170, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(261, 28, 'Negatif (-) Yön', 11, KIR)
    ic += f'<circle cx="261" cy="54" r="18" fill="none" stroke="{KIR}" stroke-width="2" stroke-dasharray="6,3"/>'
    ic += yazi(261, 56, 'Saat Yönü', 9, LAC)
    return svg(360, 100, ic, 'Pozitif ve negatif yönlü açılar şeması', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: B - İ - R - İ - M', 11.5, YES)
    harfler = [('1', 'B'), ('2', 'İ'), ('3', 'R'), ('4', 'İ'), ('5', 'M')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Birim şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_genis_acilar()
    s[1]['gorsel'] = g1_birim_cember_120()
    s[2]['gorsel'] = g2_tam_kare()
    s[3]['gorsel'] = g3_bolgeler()
    s[5]['gorsel'] = g5_koordinat_akisi()
    s[6]['gorsel'] = g6_pisagor()
    s[8]['gorsel'] = g8_yonlu_acilar()
    s[10]['gorsel'] = g10_sifre_seridi()
