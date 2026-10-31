"""8. sınıf Matematik 3. hafta (Üslü İfadeler: Tam Sayı Kuvvetleri ve Temel Kurallar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def us_metin(x, y, taban, us, boy=11.5, renk=LAC):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="{boy}" {YAZI} fill="{renk}">'
            f'{taban}<tspan baseline-shift="super" font-size="75%">{us}</tspan></text>')


def dikey_kesir(cx, cy, pay, payda, renk=LAC, cizgi_w=26):
    ic = yazi(cx, cy - 5, pay, 10.5, renk)
    ic += f'<line x1="{cx - cizgi_w / 2:.1f}" y1="{cy - 1:.1f}" x2="{cx + cizgi_w / 2:.1f}" y2="{cy - 1:.1f}" stroke="{renk}" stroke-width="1.4"/>'
    ic += yazi(cx, cy + 12, payda, 10.5, renk)
    return ic


def kuvvet_oruntusu_semasi():
    """3 tabanında pozitif, sıfır ve negatif üs örüntü şeması."""
    kolonlar = [
        ('3', '2', '9', MAVI, MAVI_A, 8),
        ('3', '1', '3', MAVI, MAVI_A, 78),
        ('3', '0', '1', YES, YES_A, 148),
        ('3', '−1', 'kesir1', TUR, TUR_A, 218),
        ('3', '−2', 'kesir2', TUR, TUR_A, 288),
    ]
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    for tab, u, deg, r, z, x in kolonlar:
        ic += kutu(x, 10, 64, 74, z, r, 7, 1.3)
        ic += kutu(x + 8, 14, 48, 24, '#fff', r, 5, 1.1)
        ic += us_metin(x + 32, 31, tab, u, 11.5, r)
        if deg == 'kesir1':
            ic += dikey_kesir(x + 32, 62, '1', '3', LAC, 22)
        elif deg == 'kesir2':
            ic += dikey_kesir(x + 32, 62, '1', '9', LAC, 22)
        else:
            ic += yazi(x + 32, 65, deg, 12, LAC)
    return svg(360, 94, ic, '3 tabanında üs örüntüsü: 3 üssü 2 eşittir 9, 3 üssü 1 eşittir 3, 3 üssü 0 eşittir 1, 3 üssü eksi 1 eşittir 1 bölü 3, 3 üssü eksi 2 eşittir 1 bölü 9.', 26)


def dort_kart_semasi():
    """Dört numaralı üslü ifade kartı (II. kartta parantezsiz negatif taban hatası)."""
    ic = ''
    # I. kart
    ic += kutu(4, 4, 172, 40, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(14, 18, 'I. kart', 10.5, MAVI, 'start')
    ic += f'<text x="14" y="35" text-anchor="start" font-size="11" {YAZI} fill="{LAC}">(−4)<tspan baseline-shift="super" font-size="75%">2</tspan> = 16</text>'
    # II. kart
    ic += kutu(184, 4, 172, 40, KIR_A, KIR, 7, 1.3)
    ic += yazi(194, 18, 'II. kart', 10.5, KIR, 'start')
    ic += f'<text x="194" y="35" text-anchor="start" font-size="11" {YAZI} fill="{LAC}">−4<tspan baseline-shift="super" font-size="75%">2</tspan> = 16</text>'
    # III. kart
    ic += kutu(4, 50, 172, 42, YES_A, YES, 7, 1.3)
    ic += yazi(14, 65, 'III. kart', 10.5, YES, 'start')
    ic += f'<text x="14" y="82" text-anchor="start" font-size="11" {YAZI} fill="{LAC}">(−2)<tspan baseline-shift="super" font-size="75%">−3</tspan> = −</text>'
    ic += dikey_kesir(95, 76, '1', '8', LAC, 18)
    # IV. kart
    ic += kutu(184, 50, 172, 42, MOR_A, MOR, 7, 1.3)
    ic += yazi(194, 65, 'IV. kart', 10.5, MOR, 'start')
    ic += yazi(245, 78, 'Tersi karesi:', 10.5, LAC, 'start', True)
    ic += dikey_kesir(330, 76, '9', '4', LAC, 20)
    return svg(360, 96, ic, 'Dört üslü ifade kartı: I. kart eksi 4 parantez karesi 16, II. kart eksi 4 karesi 16, III. kart eksi 2 üssü eksi 3 eşittir eksi 1 bölü 8, IV. kart 9 bölü 4.', 26)


def uc_terimli_islem_karti():
    """A, B ve C üslü ifade kutuları."""
    ic = kutu(4, 4, 114, 72, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(61, 20, 'A Kutusu', 11, MAVI)
    ic += kutu(14, 28, 94, 40, '#fff', MAVI, 6, 1.1)
    ic += us_metin(61, 53, '(−3)', '2', 12, LAC)

    ic += kutu(123, 4, 114, 72, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 20, 'B Kutusu', 11, TUR)
    ic += kutu(133, 28, 94, 40, '#fff', TUR, 6, 1.1)
    ic += yazi(180, 42, '1', 10.5, LAC)
    ic += f'<line x1="164" y1="46" x2="196" y2="46" stroke="{LAC}" stroke-width="1.4"/>'
    ic += us_metin(180, 61, '2', '−4', 10.5, LAC)

    ic += kutu(242, 4, 114, 72, YES_A, YES, 8, 1.3)
    ic += yazi(299, 20, 'C Kutusu', 11, YES)
    ic += kutu(252, 28, 94, 40, '#fff', YES, 6, 1.1)
    ic += us_metin(299, 53, '7', '0', 12, LAC)
    return svg(360, 80, ic, 'A kutusu eksi 3 parantez karesi, B kutusu 1 bölü 2 üssü eksi 4, C kutusu 7 üssü 0.', 25)


def islem_agaci_semasi():
    """Üslü ifadelerde çarpma ve bölme işlem ağacı: (8^3 · 4^4) / 2^3 = M."""
    ic = kutu(4, 4, 352, 84, KUM, GRI, 8, 1.2)
    ic += kutu(14, 12, 76, 28, MAVI_A, MAVI, 6, 1.3) + us_metin(52, 31, '8', '3', 11.5, LAC)
    ic += yazi(101, 30, '·', 14, MAVI)
    ic += kutu(112, 12, 76, 28, MAVI_A, MAVI, 6, 1.3) + us_metin(150, 31, '4', '4', 11.5, LAC)
    ic += yazi(204, 30, '→', 13, MAVI)
    ic += kutu(220, 12, 124, 28, YES_A, YES, 6, 1.3) + yazi(282, 30, 'Çarpım = K', 11, YES)

    ic += kutu(14, 48, 174, 28, TUR_A, TUR, 6, 1.3)
    ic += f'<text x="101" y="67" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">Bölen ifade: 2<tspan baseline-shift="super" font-size="75%">3</tspan></text>'
    ic += yazi(204, 66, '→', 13, TUR)
    ic += kutu(220, 48, 124, 28, MOR_A, MOR, 6, 1.4)
    ic += f'<text x="282" y="67" text-anchor="middle" font-size="11" {YAZI} fill="{MOR}">M = K ÷ 2<tspan baseline-shift="super" font-size="75%">3</tspan></text>'
    return svg(360, 92, ic, 'İşlem ağacı: 8 üssü 3 çarpı 4 üssü 4 eşittir K; K bölü 2 üssü 3 eşittir M.', 26)


def denk_ifade_halkalari():
    """2^18 ifadesinin farklı tabanlarda yazılış şeması."""
    ic = kutu(4, 4, 352, 74, MAVI_A, MAVI, 8, 1.3)
    ic += f'<text x="180" y="21" text-anchor="middle" font-size="11" {YAZI} fill="{MAVI}">Temel İfade: 2<tspan baseline-shift="super" font-size="75%">18</tspan>  (Üslerin Çarpımı = 18)</text>'
    halkalar = [
        ('4 = 2', '2', 12),
        ('8 = 2', '3', 98),
        ('64 = 2', '6', 184),
        ('512 = 2', '9', 270),
    ]
    for tab, u, x in halkalar:
        ic += kutu(x, 30, 78, 36, '#fff', MAVI, 6, 1.2)
        ic += us_metin(x + 39, 53, tab, u, 10.5, LAC)
    return svg(360, 82, ic, '2 üssü 18 ifadesini 4, 8, 64 ve 512 tabanlarında yazma ipucu kartları.', 25)


def bes_sayi_karti():
    """Sıralama sorusu için 5 üslü ifade kartı."""
    ic = ''
    kartlar = [
        ('Kart 1', '−2', '3', MAVI, MAVI_A),
        ('Kart 2', '(−2)', '−1', TUR, TUR_A),
        ('Kart 3', '2', '−2', YES, YES_A),
        ('Kart 4', '9', '0', MOR, MOR_A),
        ('Kart 5', 'kesir5', '', CAM, CAM_A),
    ]
    for i, (ad, t, u, r, z) in enumerate(kartlar):
        x = 4 + i * 71
        ic += kutu(x, 4, 67, 68, z, r, 7, 1.3)
        ic += yazi(x + 33.5, 20, ad, 10.5, r)
        if ad == 'Kart 5':
            ic += yazi(x + 33.5, 38, '1', 10.5, LAC)
            ic += f'<line x1="{x + 18}" y1="42" x2="{x + 49}" y2="42" stroke="{LAC}" stroke-width="1.3"/>'
            ic += us_metin(x + 33.5, 57, '2', '−3', 10.5, LAC)
        else:
            ic += us_metin(x + 33.5, 50, t, u, 11, LAC)
    return svg(358, 76, ic, 'Beş sayı kartı: eksi 2 üssü 3, eksi 2 üssü eksi 1, 2 üssü eksi 2, 9 üssü 0, 1 bölü 2 üssü eksi 3.', 25)


def direk_parkuru_semasi():
    """3^7 m uzunluğunda 82 direkli yürüyüş parkuru şeması."""
    ic = kutu(4, 4, 352, 78, YES_A, YES, 8, 1.3)
    ic += f'<text x="180" y="21" text-anchor="middle" font-size="11" {YAZI} fill="{YES}">Yürüyüş Parkuru · Toplam Uzunluk = 3<tspan baseline-shift="super" font-size="75%">7</tspan> m (82 Direk)</text>'
    ic += f'<line x1="24" y1="54" x2="336" y2="54" stroke="{LAC}" stroke-width="2.2"/>'
    for x, et in [(30, '1. direk'), (100, '2. direk'), (170, '3. direk'), (326, '82. direk')]:
        ic += f'<line x1="{x}" y1="32" x2="{x}" y2="54" stroke="{TUR}" stroke-width="3"/>'
        ic += f'<circle cx="{x}" cy="30" r="4" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.2"/>'
        ic += yazi(x, 69, et, 10.5, LAC, 'middle', True)
    ic += yazi(248, 50, '· · · (81 eş aralık) · · ·', 10.5, YES)
    return svg(360, 86, ic, 'Toplam uzunluğu 3 üssü 7 metre olan ve 82 direkle 81 eş aralığa bölünen parkur.', 25)


def dikdortgen_levha_semasi():
    """Kısa kenarı 4^5 cm, uzun kenarı 8^4 cm olan levha ve 2^7 cm kare etiket."""
    ic = kutu(4, 4, 352, 78, MAVI_A, MAVI, 8, 1.3)
    ic += kutu(20, 16, 180, 54, '#fff', MAVI, 5, 1.5)
    ic += kutu(24, 20, 32, 24, TUR_A, TUR, 3, 1.2)
    ic += us_metin(40, 36, '2', '7', 10.5, TUR)
    ic += f'<text x="110" y="34" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">Uzun kenar: 8<tspan baseline-shift="super" font-size="75%">4</tspan> cm</text>'
    ic += f'<text x="110" y="54" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">Kısa kenar: 4<tspan baseline-shift="super" font-size="75%">5</tspan> cm</text>'
    ic += kutu(214, 16, 130, 54, '#fff', TUR, 6, 1.2)
    ic += yazi(279, 35, 'Eş Kare Etiket', 10.5, TUR)
    ic += f'<text x="279" y="55" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">Kenar = 2<tspan baseline-shift="super" font-size="75%">7</tspan> cm</text>'
    return svg(360, 86, ic, 'Kısa kenarı 4 üssü 5 cm, uzun kenarı 8 üssü 4 cm olan dikdörtgen levha ve bir kenarı 2 üssü 7 cm olan kare etiket.', 25)


def parantez_karsilastirma_karti():
    """(-2^4)^3 ile (-2^3)^4 ifadelerinin işaret karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 74, KIR_A, KIR, 8, 1.3)
    ic += yazi(90, 20, '1. İfade (Dış kuvvet: 3 tek)', 10.5, KIR)
    ic += f'<text x="90" y="50" text-anchor="middle" font-size="12" {YAZI} fill="{LAC}">(−2<tspan baseline-shift="super" font-size="75%">4</tspan>)<tspan baseline-shift="super" font-size="75%">3</tspan></text>'
    ic += yazi(90, 68, 'Taban negatif, kuvvet tek', 10.5, SOLUK, 'middle', True)

    ic += kutu(184, 4, 172, 74, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, '2. İfade (Dış kuvvet: 4 çift)', 10.5, YES)
    ic += f'<text x="270" y="50" text-anchor="middle" font-size="12" {YAZI} fill="{LAC}">(−2<tspan baseline-shift="super" font-size="75%">3</tspan>)<tspan baseline-shift="super" font-size="75%">4</tspan></text>'
    ic += yazi(270, 68, 'Taban negatif, kuvvet çift', 10.5, SOLUK, 'middle', True)
    return svg(360, 82, ic, 'Birinci ifade eksi 2 üssü 4 ün 3 üncü kuvveti, ikinci ifade eksi 2 üssü 3 ün 4 üncü kuvveti.', 25)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kuvvet_oruntusu_semasi()
    s[2]['gorsel'] = dort_kart_semasi()
    s[5]['gorsel'] = uc_terimli_islem_karti()
    s[6]['gorsel'] = islem_agaci_semasi()
    s[7]['gorsel'] = denk_ifade_halkalari()
    s[8]['gorsel'] = bes_sayi_karti()
    s[9]['gorsel'] = direk_parkuru_semasi()
    s[10]['gorsel'] = dikdortgen_levha_semasi()
    s[13]['gorsel'] = parantez_karsilastirma_karti()
