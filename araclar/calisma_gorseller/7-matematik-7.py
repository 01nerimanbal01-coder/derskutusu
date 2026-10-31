"""7. sınıf Matematik 7. hafta (rasyonel sayıların karesi ve küpü, çok adımlı işlemler, gerçek yaşam problemleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'
EKSI = '−'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kesir(x, y, pay, payda, renk=LAC, boy=11, isaret='', sag_ek=''):
    """Pay üstte, payda altta; (x, y) kesir çizgisinin ortası."""
    g = max(len(pay), len(payda)) * boy * 0.62 + 6
    ic = yazi(x - g / 2 - 2, y + boy * 0.35, isaret, boy, renk, 'end') if isaret else ''
    ic += yazi(x, y - 3, pay, boy, renk)
    ic += f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" stroke="{renk}" stroke-width="1.4"/>'
    ic += yazi(x, y + boy + 1, payda, boy, renk)
    if sag_ek:
        ic += yazi(x + g / 2 + 2, y + boy * 0.35, sag_ek, boy, renk, 'start')
    return ic


def dort_uslu_kart_svg():
    """Soru 1: Dört üslü rasyonel sayı işlem kartı (2. kartta tam sayılı kesir hatası)."""
    kartlar = [
        ('1. Kart', f'({EKSI}', '3', '4', ')² =', '+', '9', '16', MAVI, MAVI_A),
        ('2. Kart', f'({EKSI}1 ', '1', '2', ')² =', '+', '5', '4', KIR, KIR_A),
        ('3. Kart', f'({EKSI}', '2', '3', ')³ =', EKSI, '8', '27', YES, YES_A),
        ('4. Kart', f'({EKSI}1 ', '1', '3', ')³ =', EKSI, '64', '27', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sol_on, p1, q1, sag_on, is2, p2, q2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 25, bas, 10.5, r, 'start')
        ic += kesir(x + 78, y + 21, p1, q1, LAC, 10.5, sol_on, sag_on)
        ic += kesir(x + 142, y + 21, p2, q2, r, 10.5, is2)
    return svg(360, 96, ic, 'Dört üslü rasyonel sayı işlem kartı: 1. kart eksi 3 bölü 4 karesi, 2. kart eksi 1 tam 1 bölü 2 karesi, 3. kart eksi 2 bölü 3 küpü, 4. kart eksi 1 tam 1 bölü 3 küpü.', 18)


def kare_kup_kartlar_svg():
    """Soru 2: Tablo sorusu için dört rasyonel sayı kartı."""
    kartlar = [
        ('1. Sayı', EKSI, '2', '5', MAVI, MAVI_A),
        ('2. Sayı', '+', '3', '4', TUR, TUR_A),
        ('3. Sayı', f'{EKSI}1 ', '1', '2', YES, YES_A),
        ('4. Sayı', EKSI, '1', '3', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, isaret, p, q, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 66, z, r, 8, 1.4)
        ic += yazi(x + 41, 22, bas, 10.5, r)
        ic += kesir(x + 46, 46, p, q, LAC, 11.5, isaret)
    return svg(360, 78, ic, 'Karesi ve küpü hesaplanacak dört rasyonel sayı kartı: eksi 2 bölü 5, artı 3 bölü 4, eksi 1 tam 1 bölü 2 ve eksi 1 bölü 3.', 18)


def merdivenli_kl_svg():
    """Soru 4: K = (2/3)/4 ve L = 2/(3/4) merdivenli kesir kartları."""
    ic = kutu(6, 6, 170, 82, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(91, 22, '1. Merdivenli İşlem (K)', 11, MAVI)
    ic += yazi(38, 60, 'K =', 12, LAC)
    ic += kesir(74, 42, '2', '3', LAC, 10.5)
    ic += f'<line x1="56" y1="56" x2="92" y2="56" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += yazi(74, 72, '4', 11.5, LAC)
    ic += yazi(128, 60, '(Ana çizgi)', 10.5, MAVI, ince=True)

    ic += kutu(184, 6, 170, 82, TUR_A, TUR, 8, 1.4)
    ic += yazi(269, 22, '2. Merdivenli İşlem (L)', 11, TUR)
    ic += yazi(216, 52, 'L =', 12, LAC)
    ic += yazi(252, 42, '2', 11.5, LAC)
    ic += f'<line x1="234" y1="48" x2="270" y2="48" stroke="{TUR}" stroke-width="2.2"/>'
    ic += kesir(252, 64, '3', '4', LAC, 10.5)
    ic += yazi(306, 52, '(Ana çizgi)', 10.5, TUR, ince=True)
    return svg(360, 94, ic, 'K ve L merdivenli kesir kartları: K eşittir 2 bölü 3 ana çizgi 4; L eşittir 2 ana çizgi 3 bölü 4.', 18)


def islem_agaci_ab_svg():
    """Soru 5: A = (-1/2)^2 ve B = (-1/2)^3 işlem ağacı."""
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.3)
    ic += kutu(14, 12, 104, 32, MAVI_A, MAVI, 7, 1.3)
    ic += kesir(58, 28, '1', '2', LAC, 10.5, f'A = ({EKSI}', ')²')
    ic += kutu(14, 50, 104, 32, TUR_A, TUR, 7, 1.3)
    ic += kesir(58, 66, '1', '2', LAC, 10.5, f'B = ({EKSI}', ')³')
    ic += f'<path d="M118 28 L164 47 M118 66 L164 47" stroke="{LAC}" stroke-width="1.6"/>'
    ic += kutu(164, 24, 178, 46, YES_A, YES, 8, 1.4)
    ic += yazi(253, 43, 'Hedef İşlem: A ÷ B = ?', 11.5, YES)
    ic += yazi(253, 61, '(Önce üslü değerleri bul!)', 10.5, LAC, ince=True)
    return svg(360, 94, ic, 'İşlem ağacı: A eşittir eksi 1 bölü 2 karesi, B eşittir eksi 1 bölü 2 küpü, hedef işlem A bölü B.', 18)


def su_deposu_svg():
    """Soru 7: 2/9'u dolu olan su deposuna 70 L eklenince 5/9'unun dolması şeması."""
    ic = kutu(4, 4, 352, 88, CAM_A, CAM, 8, 1.3)
    ic += yazi(180, 20, '9 Eş Bölmeli Su Deposu Modeli', 11.5, LAC)
    x0, w = 18, 36
    for i in range(9):
        x = x0 + i * w
        if i < 2:
            dolgu, cizgi = MAVI_A, MAVI
        elif i < 5:
            dolgu, cizgi = TUR_A, TUR
        else:
            dolgu, cizgi = '#fff', GRI
        ic += kutu(x, 28, w - 2, 34, dolgu, cizgi, 4, 1.2)
    ic += yazi(54, 78, 'İlk dolu: 2 bölme', 10.5, MAVI)
    ic += yazi(166, 78, '+70 L eklenen: 3 bölme', 10.5, TUR)
    ic += yazi(292, 78, 'Boş: 4 bölme', 10.5, SOLUK, ince=True)
    return svg(360, 96, ic, '9 eş bölmeli su deposu modeli: ilk dolu 2 bölme, eklenen 70 litre 3 bölme, kalan boş 4 bölme.', 18)


def kumas_topu_svg():
    """Soru 9: Kumaşın önce 1/4'ü, sonra kalanın 2/3'ü satılınca 18 m kalması şeması."""
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.3)
    ic += yazi(180, 20, 'Kumaş Topu · Kalanın Kesri Modeli', 11.5, LAC)
    parcalar = [
        (14, 80, KIR_A, KIR, '1. Satış'),
        (98, 160, TUR_A, TUR, '2. Satış (Kalanın 2 parça)'),
        (262, 82, YES_A, YES, 'Son: 18 m'),
    ]
    for x, w, z, r, et in parcalar:
        ic += kutu(x, 28, w, 34, z, r, 6, 1.3)
        ic += yazi(x + w / 2, 49, et, 10.5, r)
    ic += yazi(180, 78, 'Başlangıçtaki kumaşın tamamı = 4 eş ana bölme (? metre)', 10.5, LAC, ince=True)
    return svg(360, 94, ic, 'Kumaş topu modeli: 1. satış dörtte bir, 2. satış kalanın üçte ikisi, geriye kalan son parça 18 metre.', 18)


def ziplama_top_svg():
    """Soru 10: 135 cm yükseklikten bırakılan topun her çarpmada 2/3 yükselmesi şeması."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.3)
    ic += f'<line x1="16" y1="78" x2="344" y2="78" stroke="{LAC}" stroke-width="2"/>'
    direkler = [
        (48, 22, 56, 'Başlangıç', '135 cm', MAVI),
        (148, 36, 42, '1. Çarpma', '90 cm', TUR),
        (248, 48, 30, '2. Çarpma', '? cm', YES),
    ]
    for x, y, h, ad, boy_m, r in direkler:
        ic += f'<rect x="{x - 10}" y="{y}" width="20" height="{h}" rx="4" fill="#fff" stroke="{r}" stroke-width="1.4"/>'
        ic += f'<circle cx="{x}" cy="{y - 7}" r="6" fill="{r}"/>'
        ic += yazi(x + 36, y + 12, ad, 10.5, r, 'start')
        ic += yazi(x + 36, y + 26, boy_m, 11, LAC, 'start')
    return svg(360, 96, ic, 'Top zıplama modeli: başlangıç 135 santimetre, 1. çarpmadan sonra 90 santimetre, 2. çarpmadan sonra soru işareti santimetre.', 18)


def tuna_adimlar_svg():
    """Soru 11: Tuna'nın [1 - (-1/2)^2] ÷ (3/8) çok adımlı işlem kartı."""
    ic = kutu(4, 4, 352, 88, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 20, 'Tuna’nın Çok Adımlı İşlem Kartı', 11.5, MOR)
    ic += kutu(14, 28, 158, 54, '#fff', MOR, 6, 1.2)
    ic += yazi(93, 44, '1. Adım (Üslü ve Parantez):', 10.5, MOR)
    ic += kesir(66, 64, '1', '4', LAC, 10.5, '1 − (+', ') =')
    ic += kesir(132, 64, '3', '4', YES, 10.5)

    ic += kutu(184, 28, 160, 54, '#fff', TUR, 6, 1.2)
    ic += yazi(264, 44, '2. Adım (Bölme İşlemi):', 10.5, TUR)
    ic += kesir(220, 64, '3', '4', LAC, 10.5, '', ' ÷ ')
    ic += kesir(268, 64, '3', '8', LAC, 10.5, '', ' = ?')
    return svg(360, 96, ic, 'Tuna çok adımlı işlem kartı: 1. adımda parantez içi 3 bölü 4, 2. adımda 3 bölü 4 bölü 3 bölü 8 eşittir soru işareti.', 18)


def parantez_karsilastirma_svg():
    """Soru 14: (-3/5)^2 ile -(3/5)^2 parantez karşılaştırma kartları."""
    ic = kutu(6, 6, 170, 74, YES_A, YES, 8, 1.4)
    ic += yazi(91, 22, '1. Kart: Parantez Karesi', 11, YES)
    ic += kesir(68, 50, '3', '5', LAC, 11.5, f'({EKSI}', ')² = ?')

    ic += kutu(184, 6, 170, 74, KIR_A, KIR, 8, 1.4)
    ic += yazi(269, 22, '2. Kart: Eksi Parantez Dışında', 11, KIR)
    ic += kesir(246, 50, '3', '5', LAC, 11.5, f'{EKSI}(', ')² = ?')
    return svg(360, 86, ic, 'Parantez karşılaştırma kartları: 1. kart parantez içinde eksi 3 bölü 5 karesi, 2. kart eksi dışarıda 3 bölü 5 karesi.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_uslu_kart_svg()
    s[1]['gorsel'] = kare_kup_kartlar_svg()
    s[3]['gorsel'] = merdivenli_kl_svg()
    s[4]['gorsel'] = islem_agaci_ab_svg()
    s[6]['gorsel'] = su_deposu_svg()
    s[8]['gorsel'] = kumas_topu_svg()
    s[9]['gorsel'] = ziplama_top_svg()
    s[10]['gorsel'] = tuna_adimlar_svg()
    s[13]['gorsel'] = parantez_karsilastirma_svg()
