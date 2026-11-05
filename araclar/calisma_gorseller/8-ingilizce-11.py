"""8. sınıf İngilizce 11. hafta (Unit 4: On The Phone) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); eğik kesir ve beyaz bant yok (K155/K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#15803d', '#d63a3a', '#7c3aed', '#0e7490'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A, KUM = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#e0f2fe', '#fffbeb'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def santral_baglanti_karti():
    ic = kutu(4, 4, 412, 98, MAVI_A, MAVI, 8)
    ic += yazi(210, 22, 'Green Tech Switchboard — Extension 302', MAVI)
    ic += kutu(14, 34, 392, 26, KUM, TUR, 6)
    ic += yazi(210, 52, 'Receptionist: Good afternoon! How may I help you?', LAC, ince=True)
    ic += kutu(14, 66, 392, 28, YES_A, YES, 6)
    ic += yazi(210, 85, 'Nora: Could you ___ me ___ to Mr. Watson, please?', YES)
    return svg(420, 106, ic, 'Nora’nın santral görevlisinden dahili hatta bağlanmayı istemesi.', 21)


def cagri_durum_panosu():
    kartlar = [
        (4, 4, '1. Mrs. Clark', 'Free and ready now', YES, YES_A),
        (214, 4, '2. Mr. Ross', 'On another call now', KIR, KIR_A),
        (4, 58, '3. Line Quality', 'Noisy, weak signal', TUR, TUR_A),
        (214, 58, '4. Desk Note', 'Short written reminder', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 19, bas, r)
        ic += yazi(x + 101, y + 40, alt, LAC, ince=True)
    return svg(420, 110, ic, 'Sekreter ekranındaki dört farklı telefon çağrı durumu.', 22)


def calan_telefon_ani_karar():
    ic = kutu(4, 4, 412, 98, TUR_A, TUR, 8)
    # Geometrik masa telefonu ikonu (insan/el yok)
    ic += kutu(22, 42, 66, 40, MAVI_A, MAVI, 7)
    ic += f'<path d="M18 36 Q55 18 92 36" fill="none" stroke="{KIR}" stroke-width="3.5" stroke-linecap="round"/>'
    ic += yazi(55, 67, 'RING', KIR)
    ic += yazi(252, 28, '[The office phone rings]', TUR)
    ic += yazi(252, 56, 'Leo: My boxes are heavy. I cannot reach it.', LAC, ince=True)
    ic += yazi(252, 82, 'Maya (Spontaneous decision): ___', MAVI)
    return svg(420, 106, ic, 'Ofiste çalan telefona konuşma anında karar verme durumu.', 21)


def kerem_telefon_diyalogu():
    ic = kutu(4, 4, 412, 98, CAM_A, CAM, 8)
    ic += yazi(210, 22, 'Phone Call — Changing Plans with «then»', CAM)
    ic += kutu(14, 32, 392, 28, KUM, TUR, 6)
    ic += yazi(210, 51, 'Brother: Defne isn’t in. She has gone to the chess club.', LAC, ince=True)
    ic += kutu(14, 66, 392, 28, MOR_A, MOR, 6)
    ic += yazi(210, 85, 'Kerem: Oh, I see. ___', MOR)
    return svg(420, 106, ic, 'Defne evde olmadığında Kerem’in akşam tekrar arama kararı.', 21)


def sekreter_memo_notu():
    ic = kutu(4, 4, 412, 98, KUM, TUR, 8)
    ic += yazi(210, 23, 'PHONE MEMO PAD', TUR)
    ic += f'<line x1="20" y1="31" x2="400" y2="31" stroke="{TUR}" stroke-width="1.0"/>'
    ic += yazi(24, 52, 'Caller: Dr. Carter     ·     For: Mrs. Demir (Out of office)', LAC, 'start', True)
    ic += yazi(24, 78, 'Message: Friday’s meeting starts at 10:00 a.m.', MAVI, 'start')
    return svg(420, 106, ic, 'Dr. Carter tarafından Mrs. Demir için bırakılan telefon mesaj notu.', 21)


def telefon_akis_adimlari():
    adimlar = [
        (4, 'Step 1', 'Greeting', MAVI, MAVI_A),
        (108, 'Step 2', 'Ask for Mrs. Kaya', CAM, CAM_A),
        (212, 'Step 3', 'Not available', TUR, TUR_A),
        (316, 'Step 4', 'Leave message', YES, YES_A),
    ]
    ic = ''
    for x, bas, alt, r, z in adimlar:
        ic += kutu(x, 8, 100, 88, z, r, 7)
        ic += yazi(x + 50, 34, bas, r)
        ic += f'<line x1="{x+10}" y1="46" x2="{x+90}" y2="46" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 50, 72, alt, LAC, ince=True)
    return svg(420, 104, ic, 'Kibar bir telefon görüşmesinin dört temel adımı.', 21)


def cagri_merkezi_kayitlari():
    kartlar = [
        (4, 4, 'Kevin -> Ext. 208', 'Put me through, please', MAVI, MAVI_A),
        (214, 4, 'Sude -> Aunt', 'Line was engaged', KIR, KIR_A),
        (4, 58, 'Brian -> Mr. Demir', 'Left a call-back memo', YES, YES_A),
        (214, 58, 'Clara -> Office', 'Bad line, couldn’t hear', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 19, bas, r)
        ic += yazi(x + 101, y + 40, alt, LAC, ince=True)
    return svg(420, 110, ic, 'Dört arayanın çağrı merkezi kayıt özeti.', 22)


def bozuk_hat_sinyal_karti():
    ic = kutu(4, 4, 412, 96, KIR_A, KIR, 8)
    # Zayıf sinyal çubukları
    ic += f'<rect x="28" y="64" width="10" height="18" rx="2" fill="{KIR}"/>'
    ic += f'<rect x="44" y="52" width="10" height="30" rx="2" fill="#e2e8f0" stroke="{KIR}" stroke-width="1"/>'
    ic += f'<rect x="60" y="38" width="10" height="44" rx="2" fill="#e2e8f0" stroke="{KIR}" stroke-width="1"/>'
    ic += f'<rect x="76" y="24" width="10" height="58" rx="2" fill="#e2e8f0" stroke="{KIR}" stroke-width="1"/>'
    ic += yazi(252, 28, 'Connection Alert: It’s a bad line', KIR)
    ic += yazi(252, 56, 'Problem: I cannot hear the caller’s voice clearly.', LAC, ince=True)
    ic += yazi(252, 82, 'Two polite requests: 1) ?     2) ?', MAVI)
    return svg(420, 104, ic, 'Zayıf telefon sinyali ve kibar tekrar ya da ses yükseltme ricası.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = santral_baglanti_karti()
    s[2]['gorsel'] = cagri_durum_panosu()
    s[5]['gorsel'] = calan_telefon_ani_karar()
    s[6]['gorsel'] = kerem_telefon_diyalogu()
    s[7]['gorsel'] = sekreter_memo_notu()
    s[8]['gorsel'] = telefon_akis_adimlari()
    s[9]['gorsel'] = cagri_merkezi_kayitlari()
    s[11]['gorsel'] = bozuk_hat_sinyal_karti()
