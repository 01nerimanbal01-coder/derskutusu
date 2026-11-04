"""5. sınıf Matematik 8. hafta (Kesişen Çemberler Yardımıyla Eşkenar ve İkizkenar Üçgen İnşası) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def prs_eskenar_cember_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<circle cx="72" cy="64" r="34" fill="{MAVI_A}" fill-opacity="0.55" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<circle cx="106" cy="64" r="34" fill="{TUR_A}" fill-opacity="0.55" stroke="{TUR}" stroke-width="1.5"/>'
    ic += f'<polygon points="72,64 106,64 89,35" fill="#12a15022" stroke="{YES}" stroke-width="2"/>'
    ic += yazi(58, 68, 'P', MAVI, kalin=True)
    ic += yazi(120, 68, 'R', TUR, kalin=True)
    ic += yazi(89, 28, 'S', YESIL_K, kalin=True)
    ic += yazi(248, 34, 'Eş Çemberlerle PRS Üçgeni', LAC, kalin=True)
    ic += yazi(248, 58, '|PR| = |PS| = |RS| = r', MAVI, kalin=True)
    ic += yazi(248, 80, 'Çevre(PRS) = 27 cm · r = ?', LAC)
    return svg(360, 104, ic, 'Birbirinin merkezinden geçen P ve R merkezli eş çemberlerle oluşan 27 cm çevreli PRS üçgeni.', 21)


def dort_insa_deneme_karti():
    kartlar = [
        ('1. Kart', '|AB| = 6 cm', 'R = 6 cm', YES, YES_A),
        ('2. Kart', '|AB| = 8 cm', 'R = 7 cm', MAVI, MAVI_A),
        ('3. Kart', '|AB| = 10 cm', 'R = 4 cm', KIR, '#fdeaea'),
        ('4. Kart', '|AB| = 6 cm', 'R = 5 cm', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 24, bas, renk, kalin=True)
        ic += yazi(x + 41, 50, s1, LAC)
        ic += yazi(x + 41, 74, s2, LAC, kalin=True)
    return svg(360, 98, ic, 'Taban uzunluğu ve pergel açıklığı R verilen dört üçgen inşa kartı.', 21)


def cember_konum_tablo_kartlari():
    kartlar = [
        ('1. Kart', 'r = 7 ve 7', 'd = 7 cm', YES, YES_A),
        ('2. Kart', 'r = 8 ve 8', 'd = 6 cm', MAVI, MAVI_A),
        ('3. Kart', 'r = 5 ve 6', 'd = 11 cm', TUR, TUR_A),
        ('4. Kart', 'r = 4 ve 5', 'd = 12 cm', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 24, bas, renk, kalin=True)
        ic += yazi(x + 41, 50, s1, LAC)
        ic += yazi(x + 41, 74, s2, LAC, kalin=True)
    return svg(360, 98, ic, 'Yarıçapları ve merkezler arası uzaklığı verilen dört çember çifti kartı.', 21)


def cift_kesisim_ikizkenar_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="46,52 114,52 80,18" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<polygon points="46,52 114,52 80,86" fill="#fff" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(35, 56, 'A', MAVI, kalin=True)
    ic += yazi(125, 56, 'B', MAVI, kalin=True)
    ic += yazi(80, 14, 'C', YESIL_K, kalin=True)
    ic += yazi(80, 96, 'D', TUR, kalin=True)
    ic += yazi(242, 32, 'Kesişen İki Eş Çember', MAVI, kalin=True)
    ic += yazi(242, 56, 'Yarıçap: R = 9 cm', LAC, kalin=True)
    ic += yazi(242, 78, 'Taban: |AB| = 12 cm', LAC)
    return svg(360, 104, ic, '9 cm yarıçaplı iki eş çemberin C ve D kesişimleriyle oluşan ABC ve ABD ikizkenar üçgenleri.', 21)


def ikizkenar_adim_kartlari():
    adimlar = [
        ('Taban', '6 cm [AB]', MAVI, MAVI_A),
        ('Pergel', '8 cm Açıklık', TUR, TUR_A),
        ('İki Yay', 'A ve B Merkez', MOR, MOR_A),
        ('Birleştir', 'C Tepe Noktası', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 30, ust, renk, kalin=True)
        ic += yazi(x + 41, 64, alt, LAC)
    return svg(360, 96, ic, '6 cm tabanlı ve 8 cm yan kenarlı ikizkenar üçgen inşa basamakları.', 21)


def orta_dikme_kesisim_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += f'<line x1="36" y1="52" x2="124" y2="52" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="80" y1="16" x2="80" y2="88" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<polygon points="36,52 80,16 124,52 80,88" fill="none" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(26, 56, 'K', MAVI, kalin=True)
    ic += yazi(134, 56, 'L', MAVI, kalin=True)
    ic += yazi(80, 13, 'M', KIR, kalin=True)
    ic += yazi(80, 96, 'N', KIR, kalin=True)
    ic += yazi(91, 47, 'H', LAC, kalin=True)
    ic += yazi(244, 32, 'Orta Dikme Özelliği', YESIL_K, kalin=True)
    ic += yazi(244, 56, '|KH| = |HL| ve [MN] ⊥ [KL]', LAC, kalin=True)
    ic += yazi(244, 78, '|KM| = |LM| = |KN| = |LN|', LAC)
    return svg(360, 104, ic, 'K ve L merkezli eş çemberlerin M ve N kesişim noktalarını birleştiren MN orta dikmesi.', 21)


def ikizkenar_cevre_hesap_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += f'<polygon points="44,78 124,78 84,22" fill="#fff" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(34, 82, 'A', MAVI, kalin=True)
    ic += yazi(134, 82, 'B', MAVI, kalin=True)
    ic += yazi(84, 16, 'C', TUR, kalin=True)
    ic += yazi(54, 48, '7 cm', LAC)
    ic += yazi(114, 48, '7 cm', LAC)
    ic += yazi(84, 92, '9 cm', LAC, kalin=True)
    ic += yazi(248, 34, 'ABC Üçgeni İnşa Verileri', TUR, kalin=True)
    ic += yazi(248, 58, 'Yarıçaplar: |AC| = |BC| = 7 cm', LAC)
    ic += yazi(248, 80, 'Merkezler Arası: |AB| = 9 cm', LAC, kalin=True)
    return svg(360, 104, ic, 'Yan kenarları 7 cm ve tabanı 9 cm olan ABC ikizkenar üçgeni.', 21)


def ayrik_cember_deneyi_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += f'<circle cx="48" cy="52" r="24" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<circle cx="116" cy="52" r="24" fill="#fff" stroke="{TUR}" stroke-width="1.6"/>'
    ic += f'<line x1="48" y1="52" x2="116" y2="52" stroke="{LAC}" stroke-width="1.6" stroke-dasharray="4 3"/>'
    ic += yazi(48, 56, 'A', MAVI, kalin=True)
    ic += yazi(116, 56, 'B', TUR, kalin=True)
    ic += yazi(248, 32, 'Kesişmeyen Çember Deneyi', KIR, kalin=True)
    ic += yazi(248, 56, 'Taban: |AB| = 12 cm', LAC, kalin=True)
    ic += yazi(248, 78, 'Eş Yaylar: r₁ = 5 cm · r₂ = 5 cm', LAC)
    return svg(360, 104, ic, 'Merkezler arası uzaklığı 12 cm ve yarıçapları 5 cm olan iki ayrık çember.', 21)


def distan_teget_cember_svg():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += f'<circle cx="48" cy="52" r="22" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<circle cx="102" cy="52" r="32" fill="#fff" stroke="{MOR}" stroke-width="1.6"/>'
    ic += f'<circle cx="70" cy="52" r="3" fill="{KIR}"/>'
    ic += yazi(48, 56, 'O₁', MAVI, kalin=True)
    ic += yazi(102, 56, 'O₂', MOR, kalin=True)
    ic += yazi(70, 24, 'T (Teğet)', KIR, kalin=True)
    ic += yazi(248, 32, 'Dıştan Teğet İki Çember', MOR, kalin=True)
    ic += yazi(248, 56, 'r₁ = 6 cm · |O₁O₂| = 15 cm', LAC, kalin=True)
    ic += yazi(248, 78, '2. Çemberin Çapı (2 × r₂) = ?', LAC)
    return svg(360, 104, ic, 'T noktasında dıştan teğet olan O1 (r1=6 cm) ve O2 merkezli iki çember.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = prs_eskenar_cember_svg()
    s[4]['gorsel'] = dort_insa_deneme_karti()
    s[5]['gorsel'] = cember_konum_tablo_kartlari()
    s[6]['gorsel'] = cift_kesisim_ikizkenar_svg()
    s[7]['gorsel'] = ikizkenar_adim_kartlari()
    s[8]['gorsel'] = orta_dikme_kesisim_svg()
    s[9]['gorsel'] = ikizkenar_cevre_hesap_svg()
    s[11]['gorsel'] = ayrik_cember_deneyi_svg()
    s[12]['gorsel'] = distan_teget_cember_svg()
