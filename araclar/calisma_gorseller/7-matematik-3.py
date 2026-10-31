"""7. sınıf Matematik 3. hafta (Rasyonel Sayılar ve Farklı Temsilleri: sonlu ve devirli ondalık gösterimler, paydanın asal çarpanları, 10'un kuvvetine genişletme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'
EKSI = '−'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
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


def devirli(x, y, on_kisim, devreden, renk=LAC, boy=12):
    """Ön kısım + üstü çizgili devreden kısım."""
    w1 = len(on_kisim) * boy * 0.56
    w2 = len(devreden) * boy * 0.6
    x0 = x - (w1 + w2) / 2
    ic = yazi(x0, y, on_kisim, boy, renk, 'start')
    xd = x0 + w1 + w2 / 2
    ic += yazi(xd, y, devreden, boy, renk, 'middle')
    ic += f'<line x1="{xd - w2 / 2 + 1:.1f}" y1="{y - boy + 1:.1f}" x2="{xd + w2 / 2 - 1:.1f}" y2="{y - boy + 1:.1f}" stroke="{renk}" stroke-width="1.6" stroke-linecap="round"/>'
    return ic


def bolme_adimlari_svg():
    """5 bölü 12 rasyonel sayısının payı paydasına bölme adımları."""
    ic = kutu(4, 4, 108, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(58, 22, 'Bölünen Kesir', 11, MAVI)
    ic += kesir(44, 50, '5', '12', LAC, 12.5)
    ic += yazi(78, 54, '= 5 ÷ 12', 11, LAC)
    ic += yazi(58, 80, 'Tam kısım: 0', 10.5, SOLUK, ince=True)

    ic += kutu(120, 4, 236, 86, TUR_A, TUR, 8, 1.4)
    ic += yazi(238, 20, 'Ondalık Kısım Bölme Adımları', 11, TUR)
    adimlar = [
        '1. adım: 50 ÷ 12 = 4   (kalan 2)',
        '2. adım: 20 ÷ 12 = 1   (kalan 8)',
        '3. adım: 80 ÷ 12 = 6   (kalan 8 → tekrar!)',
    ]
    for i, m in enumerate(adimlar):
        y = 26 + i * 19
        ic += kutu(128, y, 220, 16, '#fff', TUR, 4, 1.1)
        ic += yazi(136, y + 12, m, 10.5, LAC, 'start', ince=True)
    return svg(360, 94, ic, '5 bölü 12 bölme adımları: 1. adım 50 bölü 12 eşittir 4 kalan 2, 2. adım 20 bölü 12 eşittir 1 kalan 8, 3. adım 80 bölü 12 eşittir 6 kalan 8 tekrar ediyor.', 19)


def dort_rasyonel_kart_svg():
    """Dört rasyonel sayı kartı: 21/15, -9/20, 7/18, 2 tam 3/4."""
    kartlar = [
        ('1. Kart', '', '21', '15', MAVI, MAVI_A),
        ('2. Kart', EKSI, '9', '20', TUR, TUR_A),
        ('3. Kart', '', '7', '18', YES, YES_A),
        ('4. Kart', '2 ', '3', '4', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, on, p, q, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 68, z, r, 8, 1.4)
        ic += yazi(x + 41, 22, bas, 10.5, r)
        ic += kesir(x + 46 if on else x + 41, 48, p, q, LAC, 12, on)
    return svg(360, 80, ic, 'Dört rasyonel sayı kartı: 1. kart 21 bölü 15, 2. kart eksi 9 bölü 20, 3. kart 7 bölü 18, 4. kart 2 tam 3 bölü 4.', 18)


def asal_carpan_panosu_svg():
    """Paydanın asal çarpanları ve sadeleştirme için dört kart: 33/15, 7/25, 11/24, 14/35."""
    kartlar = [
        ('I. Kart', '33', '15', MAVI, MAVI_A),
        ('II. Kart', '7', '25', YES, YES_A),
        ('III. Kart', '11', '24', TUR, TUR_A),
        ('IV. Kart', '14', '35', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, p, q, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 68, z, r, 8, 1.4)
        ic += yazi(x + 41, 22, bas, 10.5, r)
        ic += kesir(x + 41, 48, p, q, LAC, 12)
    return svg(360, 80, ic, 'Dört rasyonel sayı kartı: I. kart 33 bölü 15, II. kart 7 bölü 25, III. kart 11 bölü 24, IV. kart 14 bölü 35.', 18)


def genisletme_semasi_svg():
    """Tablo sorusu için dört rasyonel sayı kartı: 9/25, 5/8, -13/20, 1 tam 7/50."""
    kartlar = [
        ('1. Sayı', '', '9', '25', MAVI, MAVI_A),
        ('2. Sayı', '', '5', '8', TUR, TUR_A),
        ('3. Sayı', EKSI, '13', '20', YES, YES_A),
        ('4. Sayı', '1 ', '7', '50', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, on, p, q, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 66, z, r, 8, 1.4)
        ic += yazi(x + 41, 22, bas, 10.5, r)
        ic += kesir(x + 46 if on else x + 41, 46, p, q, LAC, 11.5, on)
    return svg(360, 78, ic, 'Paydası 10 un kuvvetine genişletilecek dört sayı kartı: 9 bölü 25, 5 bölü 8, eksi 13 bölü 20 ve 1 tam 7 bölü 50.', 18)


def olcum_cihazlari_svg():
    """Derinlik ölçer (-1,36 m) ve dijital mutfak terazisi (2,4 kg) ekranları."""
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(91, 22, '1. Derinlik Ölçer Ekranı', 11, MAVI)
    ic += kutu(30, 30, 122, 28, '#fff', MAVI, 6, 1.2)
    ic += yazi(91, 49, f'{EKSI}1,36 m', 13, LAC)
    ic += yazi(91, 71, 'Deniz seviyesinin altı', 10.5, SOLUK, ince=True)

    ic += kutu(184, 6, 170, 74, YES_A, YES, 8, 1.4)
    ic += yazi(269, 22, '2. Mutfak Terazisi Ekranı', 11, YES)
    ic += kutu(208, 30, 122, 28, '#fff', YES, 6, 1.2)
    ic += yazi(269, 49, '2,4 kg', 13, LAC)
    ic += yazi(269, 71, 'Un paketi kütlesi', 10.5, SOLUK, ince=True)
    return svg(360, 86, ic, 'İki ölçüm ekranı: 1. derinlik ölçerde eksi 1,36 metre, 2. mutfak terazisinde 2,4 kilogram.', 18)


def kerem_islem_kartlari_svg():
    """Kerem'in yazdığı dört eşitlik kartı (4. kartta 2/9 = 0,29 hatası)."""
    kartlar = [
        ('1. Kart', EKSI, '7', '4', f'= {EKSI}1,75', False, '', MAVI, MAVI_A),
        ('2. Kart', '', '5', '6', '= ', True, ('0,8', '3'), YES, YES_A),
        ('3. Kart', '3 ', '1', '5', '= 3,2', False, '', TUR, TUR_A),
        ('4. Kart', '', '2', '9', '= 0,29', False, '', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, on, p, q, sag, dev_mi, dev_v, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += yazi(x + 12, y + 24, bas, 10.5, r, 'start')
        ic += kesir(x + 76, y + 20, p, q, LAC, 11, on)
        if dev_mi:
            ic += yazi(x + 102, y + 24, '=', 11.5, LAC)
            ic += devirli(x + 132, y + 24, dev_v[0], dev_v[1], LAC, 11.5)
        else:
            ic += yazi(x + 126, y + 24, sag, 11.5, LAC)
    return svg(360, 96, ic, 'Kerem işlem kartları: 1. kart eksi 7 bölü 4 eşittir eksi 1,75; 2. kart 5 bölü 6 eşittir 0,83 (3 devirli); 3. kart 3 tam 1 bölü 5 eşittir 3,2; 4. kart 2 bölü 9 eşittir 0,29.', 19)


def sayi_dogrusu_dort_es_svg():
    """-2 ile 2 arası her birim 4 eş parçaya bölünmüş sayı doğrusu; K, L, M, N noktaları."""
    x0, b, y = 28, 76, 46
    ic = '<defs><marker id="okM73" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0b2257"/></marker></defs>'
    ic += f'<line x1="{x0 - 14}" y1="{y}" x2="{x0 + 4 * b + 14}" y2="{y}" stroke="{LAC}" stroke-width="2" marker-start="url(#okM73)" marker-end="url(#okM73)"/>'
    for i in range(17):
        x = x0 + i * b / 4
        tam = i % 4 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (7 if tam else 4)}" x2="{x:.1f}" y2="{y + (7 if tam else 4)}" stroke="{LAC}" stroke-width="{1.7 if tam else 1.1}"/>'
        if tam:
            n = i // 4 - 2
            ic += yazi(x, y + 22, f'{EKSI}{-n}' if n < 0 else str(n), 11.5, LAC)
    noktalar = [(2, 'K', MOR), (7, 'L', KIR), (11, 'M', TUR), (15, 'N', MAVI)]
    for idx, ad, renk in noktalar:
        xk = x0 + idx * b / 4
        ic += f'<circle cx="{xk:.1f}" cy="{y}" r="4.8" fill="{renk}"/>'
        ic += kutu(xk - 11, y - 30, 22, 18, '#fff', renk, 4, 1.3)
        ic += yazi(xk, y - 17, ad, 11, renk)
    return svg(360, 78, ic, 'Sayı doğrusu eksi 2 ile 2 arası, her birim 4 eş parçaya bölünmüş: K noktası eksi 1,5 te, L noktası eksi 0,25 te, M noktası 0,75 te, N noktası 1,75 te.', 18)


def dogal_sayi_kutu_svg():
    """k bölü 18 rasyonel sayısı ve koşul kartı."""
    ic = kutu(4, 4, 352, 74, KUM, GRI, 8, 1.3)
    ic += kutu(14, 12, 92, 58, MAVI_A, MAVI, 7, 1.4)
    ic += kesir(60, 41, 'k', '18', MAVI, 13)
    ic += kutu(116, 12, 228, 58, '#fff', TUR, 7, 1.3)
    ic += yazi(230, 30, 'Verilen Koşullar', 11, TUR)
    ic += yazi(126, 47, 'k ∈ {1, 2, 3, 4, 5, 6, 7, 8, 9}', 10.5, LAC, 'start', ince=True)
    ic += yazi(126, 62, 'Ondalık gösterimi SONLU olacaktır.', 10.5, LAC, 'start', ince=True)
    return svg(360, 82, ic, 'k bölü 18 rasyonel sayısı kartı: k bir basamaklı doğal sayı ve ondalık gösterimi sonlu olacaktır.', 18)


def iki_kesir_karsilastirma_svg():
    """A kartı 36/15 (sonlu) ve B kartı 37/15 (devirli) karşılaştırma şeması."""
    ic = kutu(6, 6, 170, 74, YES_A, YES, 8, 1.4)
    ic += yazi(91, 22, 'A Kartı · Sonlu Gösterim', 11, YES)
    ic += kesir(56, 48, '36', '15', LAC, 12)
    ic += yazi(112, 52, '→ Sonlu', 11.5, YES)

    ic += kutu(184, 6, 170, 74, TUR_A, TUR, 8, 1.4)
    ic += yazi(269, 22, 'B Kartı · Devirli Gösterim', 11, TUR)
    ic += kesir(234, 48, '37', '15', LAC, 12)
    ic += yazi(292, 52, '→ Devirli', 11.5, TUR)
    return svg(360, 86, ic, 'İki kart: A kartı 36 bölü 15 sonlu gösterim, B kartı 37 bölü 15 devirli gösterim.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bolme_adimlari_svg()
    s[2]['gorsel'] = dort_rasyonel_kart_svg()
    s[4]['gorsel'] = asal_carpan_panosu_svg()
    s[5]['gorsel'] = genisletme_semasi_svg()
    s[6]['gorsel'] = olcum_cihazlari_svg()
    s[8]['gorsel'] = kerem_islem_kartlari_svg()
    s[9]['gorsel'] = sayi_dogrusu_dort_es_svg()
    s[10]['gorsel'] = dogal_sayi_kutu_svg()
    s[12]['gorsel'] = iki_kesir_karsilastirma_svg()
