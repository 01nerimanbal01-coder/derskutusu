"""7. sınıf Matematik 4. hafta (rasyonel sayılar, devirli ondalık gösterimler, karşılaştırma ve sıralama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'
EKSI = '−'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kesir(x, y, pay, payda, renk=LAC, boy=11.5, isaret=''):
    """Pay üstte, payda altta; (x, y) kesir çizgisinin ortası."""
    g = max(len(pay), len(payda)) * boy * 0.62 + 6
    ic = yazi(x - g / 2 - 2, y + boy * 0.35, isaret, boy, renk, 'end') if isaret else ''
    ic += yazi(x, y - 3, pay, boy, renk)
    ic += f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" stroke="{renk}" stroke-width="1.4"/>'
    return ic + yazi(x, y + boy + 1, payda, boy, renk)


def devirli(x, y, on_kisim, devreden, renk=LAC, boy=12.5):
    """Ön kısım + üstü çizgili devreden kısım."""
    w1 = len(on_kisim) * boy * 0.56
    w2 = len(devreden) * boy * 0.6
    x0 = x - (w1 + w2) / 2
    ic = yazi(x0, y, on_kisim, boy, renk, 'start')
    xd = x0 + w1 + w2 / 2
    ic += yazi(xd, y, devreden, boy, renk, 'middle')
    ic += f'<line x1="{xd - w2 / 2 + 1:.1f}" y1="{y - boy + 1:.1f}" x2="{xd + w2 / 2 - 1:.1f}" y2="{y - boy + 1:.1f}" stroke="{renk}" stroke-width="1.6" stroke-linecap="round"/>'
    return ic


def ok_tanim(kimlik, renk=LAC):
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="{renk}"/></marker>')


def elif_adim_karti():
    """Elif'in 2,45 devirli sayısını kesre çevirme işlem kartı."""
    ic = kutu(4, 4, 352, 96, KUM, GRI, 8, 1.3)
    ic += kutu(10, 12, 92, 80, MAVI_A, MAVI, 7, 1.4)
    ic += yazi(56, 30, 'Hedef sayı', 11, MAVI)
    ic += devirli(56, 56, '2,4', '5', LAC, 13)
    ic += yazi(56, 78, '(5 devrediyor)', 10.5, SOLUK, ince=True)
    adimlar = [
        ('1. adım:', 'Bütün rakamlar: 245', MAVI),
        ('2. adım:', 'Devretmeyen: 4 → Pay: 245 − 4 = 241', TUR),
        ('3. adım:', 'Payda: bir 9 ve bir 0 ile 90', YES),
    ]
    for i, (no, m, c) in enumerate(adimlar):
        y = 12 + i * 21
        ic += kutu(110, y, 238, 18, '#fff', c, 4, 1.1)
        ic += yazi(116, y + 13, no, 10.5, c, 'start')
        ic += yazi(164, y + 13, m, 10.5, LAC, 'start', ince=True)
    ic += kutu(110, 75, 238, 20, MOR_A, MOR, 4, 1.1)
    ic += yazi(116, 89, '4. adım:', 10.5, MOR, 'start')
    ic += yazi(164, 89, 'Yazılan kesir:', 10.5, LAC, 'start', ince=True)
    ic += kesir(258, 84, '241', '90', MOR, 10.5)
    return svg(360, 104, ic, 'Elif işlem kartı, hedef sayı 2,45 devirli (5 devrediyor). 1. adım bütün rakamlar 245. 2. adım devretmeyen kısım 4, pay 245 eksi 4 eşittir 241. 3. adım payda 90. 4. adım yazılan kesir 241 bölü 90.', 22)


def devirli_kartlar():
    """Tablo sorusu için dört devirli sayı kartı."""
    kartlar = [('0,', '6', MAVI, MAVI_A), ('0,3', '5', TUR, TUR_A), ('0,', '45', YES, YES_A), (f'{EKSI}1,', '7', MOR, MOR_A)]
    ic = ''
    for i, (on, dev, c, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 54, z, c, 8, 1.4)
        ic += yazi(x + 41, 22, f'{i + 1}. kart', 10.5, c)
        ic += devirli(x + 41, 46, on, dev, LAC, 13)
    return svg(360, 66, ic, 'Dört devirli ondalık gösterim kartı: 1. kart 0,6 devirli; 2. kart 0,35 (5 devirli); 3. kart 0,45 (45 devirli); 4. kart eksi 1,7 devirli.', 18)


def sayi_dogrusu_klm():
    """-2 ile 2 arası her birim 3 eş parçaya bölünmüş sayı doğrusu; K, L, M noktaları."""
    x0, b, y = 28, 76, 46
    ic = f'<defs>{ok_tanim("m74ok1")}</defs>'
    ic += f'<line x1="{x0 - 14}" y1="{y}" x2="{x0 + 4 * b + 14}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-start="url(#m74ok1)" marker-end="url(#m74ok1)"/>'
    for i in range(13):
        x = x0 + i * b / 3
        tam = i % 3 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (7 if tam else 4)}" x2="{x:.1f}" y2="{y + (7 if tam else 4)}" stroke="{LAC}" stroke-width="{1.7 if tam else 1.1}"/>'
        if tam:
            n = i // 3 - 2
            ic += yazi(x, y + 22, f'{EKSI}{-n}' if n < 0 else str(n), 12, LAC)
    for idx, ad, renk in [(1, 'K', KIR), (4, 'L', TUR), (10, 'M', MAVI)]:
        xk = x0 + idx * b / 3
        ic += f'<circle cx="{xk:.1f}" cy="{y}" r="5" fill="{renk}"/>'
        ic += kutu(xk - 11, y - 30, 22, 18, '#fff', renk, 4, 1.3)
        ic += yazi(xk, y - 17, ad, 11.5, renk)
    return svg(360, 78, ic, 'Sayı doğrusu eksi 2 ile 2 arası, her birim 3 eş parçaya bölünmüş. K noktası eksi 2 ile eksi 1 arasında soldan birinci bölmede, L noktası eksi 1 ile 0 arasında soldan birinci bölmede, M noktası 1 ile 2 arasında soldan birinci bölmede.', 19)


def sonsuz_dokuz_serit():
    """0,9; 0,99 ve 0,999 sayılarının 1'e uzaklığı ve 2,9 devirli kutusu."""
    ic = kutu(4, 4, 228, 86, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(118, 20, '1 tam sayısına yaklaşan adımlar', 11, MAVI)
    sat = [('0,9', '1’e uzaklık: 0,1'), ('0,99', '1’e uzaklık: 0,01'), ('0,999', '1’e uzaklık: ?')]
    for i, (s, u) in enumerate(sat):
        y = 28 + i * 19
        ic += kutu(12, y, 66, 16, '#fff', MAVI, 4, 1.1) + yazi(45, y + 12, s, 11, LAC)
        ic += yazi(88, y + 12, '→', 11.5, MAVI, 'start')
        ic += yazi(106, y + 12, u, 11, LAC, 'start', ince=True)
    ic += kutu(240, 4, 116, 86, TUR_A, TUR, 8, 1.3)
    ic += yazi(298, 22, 'Sonsuz 9’lar', 11.5, TUR)
    ic += devirli(278, 48, '0,', '9', LAC, 12.5) + yazi(312, 48, '= 1', 12.5, LAC)
    ic += f'<line x1="252" y1="58" x2="344" y2="58" stroke="{TUR}" stroke-width="1"/>'
    ic += devirli(278, 78, '2,', '9', TUR, 12.5) + yazi(314, 78, '= ?', 12.5, TUR)
    return svg(360, 94, ic, 'Solda 1 tam sayısına yaklaşan adımlar: 0,9 uzaklık 0,1; 0,99 uzaklık 0,01; 0,999 uzaklık soru işareti. Sağda sonsuz 9 lar kutusu: 0,9 devirli eşittir 1 ve 2,9 devirli eşittir soru işareti.', 20)


def uc_esitlik_karti():
    """I, II ve III numaralı üç rasyonel sayı eşitlik kartı."""
    ic = ''
    kartlar = [('I', MAVI, MAVI_A), ('II', TUR, TUR_A), ('III', YES, YES_A)]
    for i, (no, c, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 72, z, c, 8, 1.4)
        ic += f'<circle cx="{x + 18}" cy="22" r="10" fill="{c}"/>' + yazi(x + 18, 26, no, 11, '#fff')
        if i == 0:
            ic += devirli(x + 48, 52, '0,', '9', LAC, 12.5) + yazi(x + 82, 52, '= 1', 12.5, LAC)
        elif i == 1:
            ic += devirli(x + 42, 52, '1,', '4', LAC, 12.5) + yazi(x + 68, 52, '=', 12.5, LAC)
            ic += kesir(x + 88, 48, '14', '9', LAC, 11.5)
        else:
            ic += devirli(x + 48, 52, '3,', '9', LAC, 12.5) + yazi(x + 82, 52, '= 4', 12.5, LAC)
    return svg(360, 84, ic, 'Üç eşitlik kartı. I: 0,9 devirli eşittir 1. II: 1,4 devirli eşittir 14 bölü 9. III: 3,9 devirli eşittir 4.', 19)


def termometre_istasyonlar():
    """Dört dağ gözlem istasyonunun gece sıcaklık göstergeleri."""
    veri = [('Kuzey', f'{EKSI}18 °C', -18, MAVI, MAVI_A),
            ('Yamaç', f'{EKSI}5 °C', -5, TUR, TUR_A),
            ('Zirve', f'{EKSI}24 °C', -24, MOR, MOR_A),
            ('Vadi', '+4 °C', 4, YES, YES_A)]
    ic = ''
    for i, (ad, sic, v, c, z) in enumerate(veri):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 78, z, c, 8, 1.4)
        ic += yazi(x + 41, 22, ad, 11.5, c)
        ic += kutu(x + 10, 30, 62, 24, '#fff', c, 5, 1.1)
        ic += yazi(x + 41, 47, sic, 12.5, LAC)
        oran = (v + 30) / 40
        ic += kutu(x + 12, 62, 58, 8, '#fff', GRI, 4, 1)
        ic += f'<rect x="{x + 13}" y="63" width="{max(6, 56 * oran):.1f}" height="6" rx="3" fill="{c}"/>'
    return svg(360, 90, ic, 'Dört dağ gözlem istasyonu sıcaklık göstergesi: Kuzey eksi 18 derece, Yamaç eksi 5 derece, Zirve eksi 24 derece, Vadi artı 4 derece.', 20)


def deniz_araclari():
    """Deniz seviyesine göre dört su altı araştırma aracının kesirli derinlik şeması."""
    ic = kutu(4, 4, 352, 98, '#dff0fb', MAVI, 8, 1.3)
    ic += f'<line x1="4" y1="24" x2="356" y2="24" stroke="{MAVI}" stroke-width="2" stroke-dasharray="6 4"/>'
    ic += kutu(10, 8, 118, 16, '#fff', MAVI, 4, 1) + yazi(69, 19.5, 'Deniz seviyesi (0 m)', 10, MAVI)
    araclar = [('Alfa', '15', '2', 54, 82, MOR),
               ('Beta', '9', '2', 140, 64, TUR),
               ('Gama', '23', '4', 226, 74, KIR),
               ('Delta', '7', '4', 310, 52, YES)]
    for ad, p, q, cx, cy, c in araclar:
        ic += f'<line x1="{cx}" y1="24" x2="{cx}" y2="{cy - 10}" stroke="{c}" stroke-width="1.2" stroke-dasharray="3 3"/>'
        ic += f'<ellipse cx="{cx}" cy="{cy}" rx="18" ry="9" fill="#fff" stroke="{c}" stroke-width="1.6"/>'
        ic += f'<circle cx="{cx - 5}" cy="{cy}" r="2.6" fill="{c}"/><circle cx="{cx + 5}" cy="{cy}" r="2.6" fill="{c}"/>'
        ic += yazi(cx - 20, cy + 4, ad, 10.5, LAC, 'end')
        ic += kesir(cx + 26, cy - 2, p, q, c, 10.5, EKSI)
    return svg(360, 106, ic, 'Deniz seviyesi 0 metre çizgisi altında dört su altı aracı: Alfa eksi 15 bölü 2 metre, Beta eksi 9 bölü 2 metre, Gama eksi 23 bölü 4 metre, Delta eksi 7 bölü 4 metre.', 22)


def mutlak_deger_tartisma():
    """Mutlak değer ve sayı doğrusu karşılaştırma kartları."""
    ic = kutu(4, 6, 156, 78, TUR_A, TUR, 8, 1.4)
    ic += yazi(82, 24, '1. Kart: Sıfıra uzaklık', 11, TUR)
    ic += yazi(82, 46, f'|{EKSI}14| = 14 birim', 12, LAC)
    ic += yazi(82, 68, f'|{EKSI}6| = 6 birim', 12, LAC)
    ic += kutu(168, 6, 188, 78, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(262, 24, '2. Kart: Sayı doğrusu konumu', 11, MAVI)
    ic += f'<defs>{ok_tanim("m74ok2")}</defs>'
    ic += f'<line x1="184" y1="54" x2="340" y2="54" stroke="{LAC}" stroke-width="1.8" marker-start="url(#m74ok2)" marker-end="url(#m74ok2)"/>'
    for x, lbl, c in [(204, f'{EKSI}14', KIR), (268, f'{EKSI}6', TUR), (316, '0', LAC)]:
        ic += f'<circle cx="{x}" cy="54" r="4.5" fill="{c}"/>'
        ic += yazi(x, 74, lbl, 11.5, c)
    return svg(360, 90, ic, 'İki bilgi kartı. 1. kart sıfıra uzaklık: mutlak değer eksi 14 eşittir 14 birim, mutlak değer eksi 6 eşittir 6 birim. 2. kart sayı doğrusu konumu: soldan sağa eksi 14, eksi 6 ve 0.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = elif_adim_karti()
    s[1]['gorsel'] = devirli_kartlar()
    s[3]['gorsel'] = sayi_dogrusu_klm()
    s[4]['gorsel'] = sonsuz_dokuz_serit()
    s[6]['gorsel'] = uc_esitlik_karti()
    s[7]['gorsel'] = termometre_istasyonlar()
    s[9]['gorsel'] = deniz_araclari()
    s[11]['gorsel'] = mutlak_deger_tartisma()
