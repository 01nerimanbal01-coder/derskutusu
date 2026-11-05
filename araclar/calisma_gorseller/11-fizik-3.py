"""11. sınıf Fizik 3. hafta (Serbest Düşme ve İki Boyutta Sabit İvmeli Hareket) görselleri.
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


def kok_ciz(cx, y, on_metin, ic_metin, son_metin='', renk=LAC, boy=8.2, ince=False):
    ic_str = str(ic_metin)
    on_str = str(on_metin) if on_metin else ''
    son_str = str(son_metin) if son_metin else ''
    w_ic = max(12, len(ic_str) * (boy * 0.62) + 4)
    w_on = len(on_str) * (boy * 0.56) + (2 if on_str else 0)
    w_son = len(son_str) * (boy * 0.56) + (2 if son_str else 0)
    toplam_w = w_on + 9 + w_ic + w_son
    sol = cx - toplam_w / 2
    out = ''
    if on_str:
        out += yazi(sol + w_on - 1, y, on_str, boy, renk, 'end', ince=ince)
    rx = sol + w_on
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.2
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.2:.1f} {orta_y - 1.2:.1f} '
            f'L{rx + 5.0:.1f} {alt_y:.1f} L{rx + 8.5:.1f} {ust_y:.1f} '
            f'H{rx + 9 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="0.75" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 9 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    if son_str:
        out += yazi(rx + 9 + w_ic + 1, y, son_str, boy, renk, 'start', ince=ince)
    return out


def atis_turleri_kartlari():
    kartlar = [
        ('1. Serbest Düşme', 'İlk Hızsız (V0=0)', YES, YES_A),
        ('2. Yatay Atış', 'Vx Sabit, Düşey Serbest', MAVI, MAVI_A),
        ('3. Eğik Atış', 'Parabolik Yörünge', TUR, TUR_A),
        ('4. Limit Hız', 'Fd = mg Dengesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Atış hareketleri temel türleri kartı.', 34)


def serbest_dusme_zaman_yol():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'SERBEST DÜŞMEDE EŞİT ZAMANLARDA ALINAN YOLLAR (h, 3h, 5h)', 9.6, YESIL_K)
    araliklar = [
        ('0 - t arası', 'Yol: h', 'Hız: V', 16, YES),
        ('t - 2t arası', 'Yol: 3h', 'Hız: 2V', 102, MAVI),
        ('2t - 3t arası', 'Yol: 5h', 'Hız: 3V', 188, TUR),
        ('Toplam Yol', 'H = 9h', 'Hız: 3V', 274, MOR),
    ]
    for baslik, yol, hiz, x, r in araliklar:
        ic += kutu(x, 34, 70, 72, '#ffffff', r)
        ic += yazi(x + 35, 54, baslik, 8.2, r)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 78, yol, 8.8, LAC)
        ic += yazi(x + 35, 94, hiz, 8.0, r, ince=True)
    return svg(360, 125, ic, 'Serbest düşmede yol-zaman dağılımı.', 34)


def yatay_atis_hiz_bilesenleri():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'YATAY ATIŞTA HIZ BİLEŞENLERİNİN DEĞİŞİMİ', 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Yatay Eksen (X)', 9.2, MAVI)
    ic += yazi(92, 76, 'İvme: ax = 0', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Vx = V0 (Sabit Hızlı)', 8.6, YESIL_K, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Düşey Eksen (Y)', 9.2, TUR)
    ic += yazi(267, 76, 'İvme: ay = g = 10 m/s²', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Vy = g.t (Düzgün Hızlanan)', 8.6, TUR, ince=True)
    return svg(360, 125, ic, 'Yatay ve düşey hız bileşenleri şeması.', 34)


def egik_atis_tepe_noktasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'EĞİK ATIŞTA TEPE NOKTASI KİNEMATİĞİ', 10.0, TUR)
    ic += kutu(16, 36, 96, 70, '#ffffff', TUR)
    ic += yazi(64, 56, 'Çıkış Aşaması', 9.0, TUR)
    ic += yazi(64, 76, 'Düşey hız azalır', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Vy > 0', 8.4, TUR, ince=True)
    ic += kutu(132, 36, 96, 70, '#ffffff', KIR)
    ic += yazi(180, 56, 'Tepe Noktası (Hmax)', 8.8, KIR)
    ic += yazi(180, 76, 'Vy = 0 (Sıfır)', 8.6, KIR, ince=True)
    ic += yazi(180, 92, 'Vtoplam = Vx', 8.6, LAC, ince=True)
    ic += kutu(248, 36, 96, 70, '#ffffff', YES)
    ic += yazi(296, 56, 'İniş Aşaması', 9.0, YESIL_K)
    ic += yazi(296, 76, 'Düşey hız artar', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'Vy < 0', 8.4, YES, ince=True)
    return svg(360, 125, ic, 'Eğik atış tepe noktası hız vektörleri.', 34)


def atis_degiskenler_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'ATIŞ HAREKETLERİNDE FORMÜL VE İLİŞKİLER TABLOSU', 9.8, MOR)
    satirlar = [
        ('Nicelik', 'Serbest Düşme', 'Yatay Atış', 'Eğik Atış', MOR),
        ('Düşey Yol (h)', '1/2 g.t²', '1/2 g.t²', 'Vy0.t - 1/2 g.t²', MAVI),
        ('Yatay Yol (X)', 'X = 0', 'Vx.t', 'Vx.t', YESIL_K),
        ('İvme Vektörü', 'g (Düşey)', 'g (Düşey)', 'g (Düşey)', TUR),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.2, r)
        ic += yazi(130, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(215, y + 13, k3, 8.0, LAC, ince=(i > 0))
        ic += yazi(300, y + 13, k4, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Atış hareketleri formül tablosu.', 34)


def aci_menzil_diyagrami():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'FIRLATMA AÇISI VE MENZİL İLİŞKİSİ', 10.2, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Maksimum Menzil (45°)', 9.0, YESIL_K)
    ic += yazi(92, 76, 'Xmax en büyük değer', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Sin(2θ) = 1 olur', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(267, 56, 'Tümler Açılar (θ1 + θ2 = 90°)', 8.8, CAM)
    ic += yazi(267, 76, '30° ve 60° menzilleri eşit', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'X1 = X2 (Eşit Menzil)', 8.6, CAM, ince=True)
    return svg(360, 125, ic, 'Açı ve menzil bağıntıları diyagramı.', 34)


def yatay_menzil_grafik_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'YATAY ATIŞ KİNEMATİK ADIMLARI', 10.0, TUR)
    kartlar = [
        ('1. Düşme Süresi', None, 16),
        ('2. Yatay Menzil', 'X = Vx . t', 102),
        ('3. Çarpma Hızı', 'V² = Vx² + Vy²', 188),
        ('4. İvme Sabiti', 'a = g = 10 m/s²', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        if a is None:
            ic += kok_ciz(x + 35, 82, 't = ', '2h/g', '', LAC, 8.0, ince=True)
        else:
            ic += yazi(x + 35, 82, a, 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Yatay atış kinematik adımları kartı.', 34)


def bagimsiz_eksenler_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'İKİ BOYUTLU HAREKETİN BAĞIMSIZ BİLEŞENLERİ', 10.0, YESIL_K)
    kutular = ['X: Sabit Hızlı', 'Y: Sabit İvmeli', 't: Ortak Zaman', 'Bileşke Vektör']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'{i + 1}. İlke', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, 'Bağımsız eksenler hareket kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = atis_turleri_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = serbest_dusme_zaman_yol()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = yatay_atis_hiz_bilesenleri()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = egik_atis_tepe_noktasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = atis_degiskenler_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = aci_menzil_diyagrami()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = yatay_menzil_grafik_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = bagimsiz_eksenler_kutulari()
    s[10]['en_fazla'] = 34
