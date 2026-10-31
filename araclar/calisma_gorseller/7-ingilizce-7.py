"""7. sınıf İngilizce 7. hafta (Sports: routines, equipment, match scores, athlete profiles) çalışma kâğıdı görselleri (SVG; insan figürü yok K024; yazı 10-13 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=23):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def skor_panosu():
    ic = kutu(4, 4, 172, 84, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(90, 19, 'MATCH 1 · Final Score', 11, '#fff')
    ic += yazi(44, 46, 'Tigers', 11.5, LAC) + yazi(136, 46, 'Bears', 11.5, LAC)
    ic += kutu(66, 34, 48, 28, '#fff', MAVI, 6, 1.2) + yazi(90, 53, '3 - 1', 12.5, MAVI)
    ic += yazi(90, 78, 'Winner: Tigers', 10.5, YES)

    ic += kutu(184, 4, 172, 84, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="22" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="10" fill="{TUR}"/>'
    ic += yazi(270, 19, 'MATCH 2 · Final Score', 11, '#fff')
    ic += yazi(224, 46, 'Falcons', 11.5, LAC) + yazi(316, 46, 'Hawks', 11.5, LAC)
    ic += kutu(246, 34, 48, 28, '#fff', TUR, 6, 1.2) + yazi(270, 53, '2 - 2', 12.5, TUR)
    ic += yazi(270, 78, 'Result: Draw (Tie)', 10.5, SOLUK)
    return svg(360, 92, ic, 'İki maç skor tabelası: Match 1 Tigers 3 Bears 1, Match 2 Falcons 2 Hawks 2 (Draw).', 23)


def ekipman_kartlari():
    kartlar = [
        ('1. Kart', 'bow · arrows · target', MAVI, MAVI_A, 4),
        ('2. Kart', 'goggles · swimsuit', CAM, CAM_A, 122),
        ('3. Kart', 'racket · shuttlecock', YES, YES_A, 240),
    ]
    ic = ''
    for i, (bas, alt, r, z, x) in enumerate(kartlar):
        cx = x + 58
        ic += kutu(x, 4, 116, 88, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 11.5, r)
        if i == 0:
            ic += f'<circle cx="{cx - 14}" cy="48" r="13" fill="#fff" stroke="{KIR}" stroke-width="2"/><circle cx="{cx - 14}" cy="48" r="6" fill="none" stroke="{MAVI}" stroke-width="2"/>'
            ic += f'<path d="M{cx + 12} 33 q13 15 0 30" fill="none" stroke="{KAHVE}" stroke-width="2.2"/><line x1="{cx + 12}" y1="33" x2="{cx + 12}" y2="63" stroke="{SOLUK}" stroke-width="1"/>'
        elif i == 1:
            ic += f'<rect x="{cx - 24}" y="40" width="20" height="12" rx="5" fill="#fff" stroke="{CAM}" stroke-width="1.8"/>'
            ic += f'<rect x="{cx + 4}" y="40" width="20" height="12" rx="5" fill="#fff" stroke="{CAM}" stroke-width="1.8"/>'
            ic += f'<line x1="{cx - 4}" y1="46" x2="{cx + 4}" y2="46" stroke="{CAM}" stroke-width="1.8"/>'
        else:
            ic += f'<circle cx="{cx - 10}" cy="42" r="10" fill="none" stroke="{YES}" stroke-width="2"/>'
            ic += f'<line x1="{cx - 10}" y1="52" x2="{cx - 10}" y2="62" stroke="{KAHVE}" stroke-width="2.4"/>'
            ic += f'<polygon points="{cx + 12},54 {cx + 22},38 {cx + 6},38" fill="#fff" stroke="{TUR}" stroke-width="1.4"/>'
        ic += yazi(cx, 82, alt, 10.2, LAC, 'middle', True)
    return svg(360, 96, ic, 'Üç ekipman kartı: 1. kart bow arrows target, 2. kart goggles swimsuit, 3. kart racket shuttlecock.', 23)


def spor_kavram_rozetleri():
    ogeler = [
        ('bow & arrow', MAVI, MAVI_A),
        ('goggles', CAM, CAM_A),
        ('opponent', TUR, TUR_A),
        ('draw', MOR, MOR_A),
        ('go on a diet', YES, YES_A),
    ]
    ic = ''
    for i, (ad, r, z) in enumerate(ogeler):
        x = 2 + i * 71
        cx = x + 35
        ic += kutu(x, 4, 69, 76, z, r, 7, 1.3)
        ic += rozet(cx, 28, str(i + 1), r, 10)
        ic += yazi(cx, 62, ad, 10.2, LAC)
    return svg(358, 84, ic, 'Beş spor kavram rozeti: bow and arrow, goggles, opponent, draw, go on a diet.', 22)


def sporcu_haftalik_plan():
    gunler = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    satirlar = [
        ('do archery', [1, 1, 1, 1, 1, 0, 0], MAVI),
        ('go jogging', [1, 0, 1, 0, 1, 0, 0], YES),
        ('eat junk food', [0, 0, 0, 0, 0, 0, 0], KIR),
    ]
    ic = kutu(4, 4, 352, 104, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'Sinan’s Weekly Training Schedule', 11.5, '#fff')
    for j, g in enumerate(gunler):
        ic += yazi(132 + j * 32, 39, g, 10.5, SOLUK)
    for i, (ad, dizi, renk) in enumerate(satirlar):
        y = 46 + i * 19
        ic += f'<rect x="10" y="{y}" width="340" height="17" rx="3" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(16, y + 12.5, ad, 10.5, LAC, 'start', True)
        for j, v in enumerate(dizi):
            cx = 132 + j * 32
            if v:
                ic += f'<circle cx="{cx}" cy="{y + 8.5}" r="5.5" fill="{renk}"/>'
            else:
                ic += f'<line x1="{cx - 3.5}" y1="{y + 8.5}" x2="{cx + 3.5}" y2="{y + 8.5}" stroke="{GRI}" stroke-width="1.5"/>'
    return svg(360, 112, ic, 'Sinan haftalık antrenman çizelgesi: do archery 5 gün, go jogging 3 gün, eat junk food 0 gün.', 24)


def roportaj_panosu():
    ic = kutu(4, 4, 352, 98, KUM, MOR, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MOR}"/><rect x="4" y="16" width="352" height="10" fill="{MOR}"/>'
    ic += yazi(180, 19, 'INTERVIEW WITH CANSU (National Swimmer)', 11, '#fff')
    satirlar = [
        'Sport: Swimming (wears goggles and a swimsuit)',
        'Routine: Wakes up at 06:00 and trains six days a week',
        'Diet: Never goes on a strict diet; always eats healthy food',
        'Goal: Wants to win an Olympic gold medal for Türkiye',
    ]
    for i, s in enumerate(satirlar):
        ic += yazi(14, 40 + i * 16, s, 10.2, LAC, 'start', True)
    return svg(360, 106, ic, 'Milli yüzücü Cansu ile röportaj panosu: yüzme, haftada 6 gün antrenman, sağlıklı beslenme ve olimpiyat altın madalya hedefi.', 24)


def karisik_kelime_kartlari():
    satirlar = [
        ('A', ['junk food', 'never', 'Mete', 'eats'], MAVI, MAVI_A),
        ('B', ['work out?', 'do you', 'How often'], TUR, TUR_A),
    ]
    ic = ''
    for r, (harf, kartlar, renk, dolgu) in enumerate(satirlar):
        y = 6 + r * 40
        ic += rozet(14, y + 15, harf, renk)
        x = 30
        for k in kartlar:
            w = 16 + len(k) * 6.4
            ic += kutu(x, y, w, 30, dolgu, renk, 6, 1.3)
            ic += yazi(x + w / 2, y + 19, k, 11, LAC, 'middle', True)
            x += w + 6
    return svg(360, 84, ic, 'Karışık kelime kartları: A satırı junk food, never, Mete, eats; B satırı work out?, do you, How often.', 22)


def dil_bilgisi_fisleri():
    fisler = [
        ('I. fiş', ['Mete Gazoz won the gold', 'medal in archery.'], MAVI, MAVI_A),
        ('II. fiş', ['Our school team beat the', 'opponent 3-1 yesterday.'], YES, YES_A),
        ('III. fiş', ['Selin never eats fast food', 'in the evening.'], TUR, TUR_A),
        ('IV. fiş', ['He doesn’t never go', 'swimming on Mondays.'], KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, satir, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += f'<rect x="{x + 6}" y="{y + 6}" width="38" height="16" rx="4" fill="{r}"/>'
        ic += yazi(x + 25, y + 17.5, bas, 10.2, '#fff')
        ic += yazi(x + 48, y + 17, satir[0], 10.0, LAC, 'start', True)
        ic += yazi(x + 48, y + 31, satir[1], 10.0, LAC, 'start', True)
    return svg(360, 96, ic, 'Dört cümle fişi: I won the gold medal, II beat the opponent, III never eats fast food, IV doesn’t never go swimming (hatalı).', 23)


def sporcu_profil_karti():
    ic = kutu(4, 4, 352, 82, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{CAM}"/><rect x="4" y="16" width="352" height="10" fill="{CAM}"/>'
    ic += yazi(180, 19, 'ATHLETE PROFILE · Ece Demir', 11.5, '#fff')
    bilgiler = [
        ('Sport:', 'Tennis', 14, 58, 44),
        ('Equipment:', 'A racket and a ball', 155, 226, 44),
        ('Training:', 'Four times a week', 14, 72, 68),
        ('Diet:', 'Healthy food', 195, 230, 68),
    ]
    for bas, deg, x1, x2, y in bilgiler:
        ic += yazi(x1, y, bas, 10.5, CAM, 'start')
        ic += yazi(x2, y, deg, 10.5, LAC, 'start', True)
    return svg(360, 90, ic, 'Ece Demir sporcu profil kartı: Sport Tennis, Equipment a racket and a ball, Training four times a week.', 23)


def spor_ekipman_ucluleri():
    kartlar = [
        ('do archery', 'bow & arrows', MAVI, MAVI_A, 4),
        ('go swimming', 'goggles & pool', CAM, CAM_A, 122),
        ('go cycling', 'bike & helmet', YES, YES_A, 240),
    ]
    ic = ''
    for ad, ekp, r, z, x in kartlar:
        cx = x + 58
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        ic += yazi(cx, 32, ad, 11.5, r)
        ic += yazi(cx, 58, ekp, 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Üç spor ve ekipman kartı: do archery (bow and arrows), go swimming (goggles and pool), go cycling (bike and helmet).', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = skor_panosu()
    s[1]['gorsel'] = ekipman_kartlari()
    s[2]['gorsel'] = spor_kavram_rozetleri()
    s[3]['gorsel'] = sporcu_haftalik_plan()
    s[6]['gorsel'] = roportaj_panosu()
    s[7]['gorsel'] = karisik_kelime_kartlari()
    s[9]['gorsel'] = dil_bilgisi_fisleri()
    s[10]['gorsel'] = sporcu_profil_karti()
    s[12]['gorsel'] = spor_ekipman_ucluleri()
