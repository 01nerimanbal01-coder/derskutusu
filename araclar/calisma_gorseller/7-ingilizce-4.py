"""7. sınıf İngilizce 4. hafta (Sports: spor sözcükleri, sıklık zarfları, How often soruları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–13 pt (K150 EK); kesir yok (K155)."""

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


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def skor_tabelasi():
    """İki maçın dijital skor tabelası (Match 1: Eagles 4 - 2 Lions, Match 2: Sharks 1 - 1 Wolves)."""
    ic = kutu(4, 4, 172, 84, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(90, 19, 'MATCH 1 · Final Score', 11, '#fff')
    ic += yazi(44, 46, 'Eagles', 11.5, LAC) + yazi(136, 46, 'Lions', 11.5, LAC)
    ic += kutu(66, 34, 48, 28, '#fff', MAVI, 6, 1.2) + yazi(90, 53, '4 - 2', 13, MAVI)
    ic += yazi(90, 78, 'Winner: Eagles', 10.5, YES)

    ic += kutu(184, 4, 172, 84, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="22" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="10" fill="{TUR}"/>'
    ic += yazi(270, 19, 'MATCH 2 · Final Score', 11, '#fff')
    ic += yazi(224, 46, 'Sharks', 11.5, LAC) + yazi(316, 46, 'Wolves', 11.5, LAC)
    ic += kutu(246, 34, 48, 28, '#fff', TUR, 6, 1.2) + yazi(270, 53, '1 - 1', 13, TUR)
    ic += yazi(270, 78, 'Equal score', 10.5, SOLUK)
    return svg(360, 92, ic, 'İki maç skor tabelası: Match 1 Eagles 4 Lions 2, Match 2 Sharks 1 Wolves 1.', 24)


def ekipman_kartlari():
    """Üç spor ekipman kartı: 1 yay-ok-hedef, 2 raket-masa-file, 3 kayak-gözlük."""
    kartlar = [
        ('1. Kart', 'bow · arrows · target', MAVI, MAVI_A, 4),
        ('2. Kart', 'rackets · table · net', YES, YES_A, 122),
        ('3. Kart', 'skis · snow goggles', MOR, MOR_A, 240),
    ]
    ic = ''
    for i, (bas, alt, r, z, x) in enumerate(kartlar):
        cx = x + 58
        ic += kutu(x, 4, 116, 88, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 11.5, r)
        if i == 0:
            ic += f'<circle cx="{cx - 14}" cy="48" r="14" fill="#fff" stroke="{KIR}" stroke-width="2"/><circle cx="{cx - 14}" cy="48" r="7" fill="none" stroke="{MAVI}" stroke-width="2"/><circle cx="{cx - 14}" cy="48" r="2.5" fill="{ALTIN}"/>'
            ic += f'<path d="M{cx + 12} 32 q14 16 0 32" fill="none" stroke="{KAHVE}" stroke-width="2.2"/><line x1="{cx + 12}" y1="32" x2="{cx + 12}" y2="64" stroke="{SOLUK}" stroke-width="1"/>'
            ic += f'<line x1="{cx - 2}" y1="48" x2="{cx + 24}" y2="48" stroke="{LAC}" stroke-width="1.6"/>'
        elif i == 1:
            ic += f'<rect x="{cx - 32}" y="48" width="64" height="12" rx="2" fill="{YES}" stroke="{LAC}" stroke-width="1.1"/><line x1="{cx}" y1="42" x2="{cx}" y2="60" stroke="#fff" stroke-width="1.8"/>'
            ic += f'<circle cx="{cx - 16}" cy="38" r="8" fill="{KIR}" stroke="{LAC}" stroke-width="1.1"/><line x1="{cx - 16}" y1="46" x2="{cx - 16}" y2="53" stroke="{KAHVE}" stroke-width="2.2"/>'
            ic += f'<circle cx="{cx + 14}" cy="39" r="3.5" fill="{ALTIN}"/>'
        else:
            ic += f'<line x1="{cx - 26}" y1="60" x2="{cx + 18}" y2="34" stroke="{MOR}" stroke-width="3" stroke-linecap="round"/>'
            ic += f'<line x1="{cx - 20}" y1="64" x2="{cx + 24}" y2="38" stroke="{MOR}" stroke-width="3" stroke-linecap="round"/>'
            ic += f'<rect x="{cx - 14}" y="32" width="28" height="11" rx="5" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.3"/>'
        ic += yazi(cx, 82, alt, 10.5, LAC, 'middle', True)
    return svg(360, 96, ic, 'Üç ekipman kartı: 1. kart bow arrows target, 2. kart rackets table net, 3. kart skis snow goggles.', 24)


def spor_rozetleri():
    """Beş spor terimi rozeti (medal, spectators, equipment, go on a diet, train)."""
    ogeler = [
        ('medal', ALTIN, KUM),
        ('spectators', MAVI, MAVI_A),
        ('equipment', TUR, TUR_A),
        ('go on a diet', YES, YES_A),
        ('train', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, r, z) in enumerate(ogeler):
        x = 2 + i * 71
        cx = x + 35
        ic += kutu(x, 4, 69, 78, z, r, 7, 1.3)
        if i == 0:
            ic += f'<path d="M{cx - 8} 14 l5 14 h6 l5 -14" fill="none" stroke="{KIR}" stroke-width="2.5"/>'
            ic += f'<circle cx="{cx}" cy="38" r="11" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.3"/>'
            ic += yazi(cx, 42, '1', 11, LAC)
        elif i == 1:
            ic += f'<path d="M{cx - 20} 44 a20 12 0 0 1 40 0" fill="none" stroke="{MAVI}" stroke-width="2"/>'
            ic += f'<path d="M{cx - 14} 48 a14 8 0 0 1 28 0" fill="none" stroke="{MAVI}" stroke-width="2"/>'
            ic += f'<rect x="{cx - 12}" y="22" width="24" height="12" rx="2" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/>'
        elif i == 2:
            ic += f'<ellipse cx="{cx - 6}" cy="30" rx="8" ry="10" fill="none" stroke="{TUR}" stroke-width="1.8"/>'
            ic += f'<line x1="{cx - 6}" y1="40" x2="{cx - 6}" y2="50" stroke="{KAHVE}" stroke-width="2.2"/>'
            ic += f'<circle cx="{cx + 10}" cy="38" r="5" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1"/>'
        elif i == 3:
            ic += f'<circle cx="{cx - 6}" cy="36" r="9" fill="{KIR}"/><path d="M{cx - 6} 26 q3 -5 7 -3" fill="none" stroke="{YES}" stroke-width="1.8"/>'
            ic += f'<rect x="{cx + 7}" y="26" width="9" height="20" rx="2" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.2"/>'
        else:
            ic += f'<circle cx="{cx}" cy="36" r="11" fill="#fff" stroke="{MOR}" stroke-width="1.6"/>'
            ic += f'<line x1="{cx}" y1="36" x2="{cx}" y2="29" stroke="{MOR}" stroke-width="1.6"/><line x1="{cx}" y1="36" x2="{cx + 6}" y2="36" stroke="{MOR}" stroke-width="1.6"/>'
        ic += yazi(cx, 70, ad, 9.8, LAC)
    return svg(358, 86, ic, 'Beş spor rozeti: medal, spectators, equipment, go on a diet, train.', 22)


def haftalik_takvim():
    """Arda'nın haftalık spor çizelgesi (Mon-Sun)."""
    gunler = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    satirlar = [
        ('go cycling', [0, 1, 0, 0, 0, 1, 0], MAVI),
        ('do gymnastics', [1, 0, 1, 1, 1, 0, 0], TUR),
        ('go skating', [0, 0, 0, 0, 0, 0, 0], KIR),
    ]
    ic = kutu(4, 4, 352, 104, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'Arda’s Weekly Sports Plan', 11.5, '#fff')
    for j, g in enumerate(gunler):
        ic += yazi(132 + j * 32, 39, g, 10.5, SOLUK)
    for i, (ad, dizi, renk) in enumerate(satirlar):
        y = 46 + i * 19
        ic += f'<rect x="10" y="{y}" width="340" height="17" rx="3" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(16, y + 12.5, ad, 11, LAC, 'start', True)
        for j, v in enumerate(dizi):
            cx = 132 + j * 32
            if v:
                ic += f'<circle cx="{cx}" cy="{y + 8.5}" r="5.5" fill="{renk}"/>'
            else:
                ic += f'<line x1="{cx - 3.5}" y1="{y + 8.5}" x2="{cx + 3.5}" y2="{y + 8.5}" stroke="{GRI}" stroke-width="1.5"/>'
    return svg(360, 112, ic, 'Arda haftalık spor planı: go cycling Salı ve Cumartesi; do gymnastics Pazartesi, Çarşamba, Perşembe ve Cuma; go skating hiçbir gün.', 25)


def kulup_anketi():
    """Okul spor kulübü anket panosu (Sude, Emir, Nil, Bora)."""
    veriler = [
        ('Sude', 'go swimming', 'every day', MAVI, MAVI_A),
        ('Emir', 'go snowboarding', 'twice a year', TUR, TUR_A),
        ('Nil', 'play table tennis', 'Mon · Wed · Fri', YES, YES_A),
        ('Bora', 'do weight-lifting', '0 days (never)', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 98, KUM, GRI, 8, 1.3)
    ic += yazi(180, 20, 'SCHOOL SPORTS CLUB SURVEY', 11.5, LAC)
    for i, (ad, spor, siklik, r, z) in enumerate(veriler):
        x, y = 12 + (i % 2) * 172, 28 + (i // 2) * 34
        ic += kutu(x, y, 164, 30, z, r, 6, 1.2)
        ic += yazi(x + 8, y + 13, f'{ad}: {spor}', 10.5, LAC, 'start')
        ic += yazi(x + 8, y + 25, siklik, 10.5, r, 'start', True)
    return svg(360, 106, ic, 'Okul spor kulübü anket panosu: Sude go swimming every day, Emir go snowboarding twice a year, Nil play table tennis Mon Wed Fri, Bora do weight-lifting 0 days.', 24)


def kelime_kartlari():
    """İki satır karışık kelime kartı (A ve B)."""
    satirlar = [
        ('A', ['in the morning', 'usually', 'Tuna', 'goes jogging'], MAVI, MAVI_A),
        ('B', ['never', 'are', 'The players', 'late for training'], TUR, TUR_A),
    ]
    ic = ''
    for r, (harf, kartlar, renk, dolgu) in enumerate(satirlar):
        y = 6 + r * 40
        ic += rozet(14, y + 15, harf, renk)
        x = 28
        for k in kartlar:
            w = 12 + len(k) * 6.2
            ic += kutu(x, y, w, 30, dolgu, renk, 6, 1.3)
            ic += yazi(x + w / 2, y + 19, k, 11, LAC, 'middle', True)
            x += w + 5
    return svg(360, 84, ic, 'Karışık kelime kartları: A satırı in the morning, usually, Tuna, goes jogging. B satırı never, are, The players, late for training.', 22)


def cumle_kartlari():
    """Dört numaralı cümle fişi (IV. fişte Does Mert goes cycling hatası)."""
    fisler = [
        ('I. fiş', ['Defne always wears a', 'helmet while cycling.'], MAVI, MAVI_A),
        ('II. fiş', ['Our coach is usually in', 'the gym at eight.'], YES, YES_A),
        ('III. fiş', ['Do they often play', 'volleyball at school?'], TUR, TUR_A),
        ('IV. fiş', ['Does Mert goes cycling', 'on Saturdays?'], KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, satir, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += f'<rect x="{x + 6}" y="{y + 6}" width="38" height="16" rx="4" fill="{r}"/>'
        ic += yazi(x + 25, y + 17.5, bas, 10, '#fff')
        ic += yazi(x + 48, y + 17, satir[0], 9.8, LAC, 'start', True)
        ic += yazi(x + 48, y + 31, satir[1], 9.8, LAC, 'start', True)
    return svg(360, 96, ic, 'Dört cümle fişi: I. fiş Defne always wears a helmet while cycling, II. fiş Our coach is usually in the gym, III. fiş Do they often play volleyball, IV. fiş Does Mert goes cycling on Saturdays.', 24)


def pelin_karti():
    """Pelin'in sporcu bilgi kartı."""
    ic = kutu(4, 4, 352, 82, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{CAM}"/><rect x="4" y="16" width="352" height="10" fill="{CAM}"/>'
    ic += yazi(180, 19, 'ATHLETE CARD · Pelin Kaya', 11.5, '#fff')
    bilgiler = [
        ('Sport:', 'Archery', 14, 58, 42),
        ('Training:', 'Tue & Thu', 178, 240, 42),
        ('Diet:', 'Healthy food', 14, 58, 68),
        ('Paragliding:', '0 times (never)', 178, 252, 68),
    ]
    for bas, deg, x1, x2, y in bilgiler:
        ic += yazi(x1, y, bas, 10.5, CAM, 'start')
        ic += yazi(x2, y, deg, 10.5, LAC, 'start', True)
    return svg(360, 90, ic, 'Pelin sporcu kartı: Sport Archery, Training Tuesday and Thursday, Diet Healthy food, Paragliding 0 times never.', 24)


def spor_ikonlari():
    """Üç spor kartı: go cycling, play volleyball, do gymnastics (insan figürü yok, yalnız ekipman)."""
    kartlar = [
        ('go cycling', MAVI, MAVI_A, 4),
        ('play volleyball', TUR, TUR_A, 122),
        ('do gymnastics', YES, YES_A, 240),
    ]
    ic = ''
    for i, (ad, r, z, x) in enumerate(kartlar):
        cx = x + 58
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        if i == 0:
            ic += f'<circle cx="{cx - 18}" cy="40" r="10" fill="none" stroke="{MAVI}" stroke-width="2"/>'
            ic += f'<circle cx="{cx + 18}" cy="40" r="10" fill="none" stroke="{MAVI}" stroke-width="2"/>'
            ic += f'<path d="M{cx - 18} 40 l14 -14 h18 l-10 14 z" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
        elif i == 1:
            ic += f'<circle cx="{cx}" cy="36" r="13" fill="#fff" stroke="{TUR}" stroke-width="1.8"/>'
            ic += f'<path d="M{cx - 11} 30 q11 8 22 0 M{cx - 11} 42 q11 -8 22 0" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
        else:
            ic += f'<line x1="{cx - 14}" y1="16" x2="{cx - 14}" y2="30" stroke="{SOLUK}" stroke-width="1.8"/>'
            ic += f'<line x1="{cx + 14}" y1="16" x2="{cx + 14}" y2="30" stroke="{SOLUK}" stroke-width="1.8"/>'
            ic += f'<circle cx="{cx - 14}" cy="37" r="7" fill="none" stroke="{YES}" stroke-width="2"/>'
            ic += f'<circle cx="{cx + 14}" cy="37" r="7" fill="none" stroke="{YES}" stroke-width="2"/>'
        ic += yazi(cx, 68, ad, 11.5, LAC)
    return svg(360, 84, ic, 'Üç spor etkinlik kartı: go cycling bisiklet, play volleyball voleybol topu, do gymnastics jimnastik halkaları.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = skor_tabelasi()
    s[1]['gorsel'] = ekipman_kartlari()
    s[2]['gorsel'] = spor_rozetleri()
    s[3]['gorsel'] = haftalik_takvim()
    s[6]['gorsel'] = kulup_anketi()
    s[7]['gorsel'] = kelime_kartlari()
    s[9]['gorsel'] = cumle_kartlari()
    s[10]['gorsel'] = pelin_karti()
    s[12]['gorsel'] = spor_ikonlari()
