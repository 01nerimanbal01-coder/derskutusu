"""12. sınıf İngilizce 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.8, kc) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Accepting, refusing and friendship idioms', [('Count me in!', 'Beni de say! (Kabul)', YES, YES_A), ('Rain check', 'Sonraya ertelemek', TUR, TUR_A), ('Can’t make it', 'Gelememek (Red)', KIR, KIR_A), ('Friend in need', 'Kara gün dostu', MAVI, MAVI_A)])

def g1():
    return uclu('Making invitations grammar patterns', 'MAKING INVITATIONS & SUGGESTIONS (GRAMMAR)', ('Would you like', '+ to V1 (to join)', MAVI, MAVI_A), ('Why don’t we', '+ V1 (join)', TUR, TUR_A), ('How about / Fancy', '+ V-ing (going)', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('Giving explanations because vs due to', 'GIVING EXPLANATIONS · BECAUSE VS. DUE TO / BECAUSE OF', 'because / since / as + Clause (Subject + Verb): "...because my battery died."', 'due to / because of / owing to + Noun Phrase: "...due to heavy traffic."', MOR, MOR_A, '#f5f0ff')

def g3():
    return kart4('Friendship expressions and apologizing rules', [('Would you like', 'Takes to + V1', MAVI, MAVI_A), ('Agreeing 100%', 'Couldn’t agree more', YES, YES_A), ('Fall out / Make up', 'Küsmek / Barışmak', TUR, TUR_A), ('Apologize for', 'Takes V-ing gerund', MOR, MOR_A)])

def g5():
    return akis4('Invitation, refusal and rescheduling dialogue flow', [('1. Invitation', 'How about Saturday?', MAVI, MAVI_A), ('2. Polite Refusal', 'Can’t make it (Dinner)', KIR, KIR_A), ('3. New Offer', 'What about Sunday?', TUR, TUR_A), ('4. Acceptance', 'Count me in! Awesome!', YES, YES_A)])

def g6():
    return pano('Phrasal verbs on friendship', 'PHRASAL VERBS ON FRIENDSHIP AND RELATIONSHIPS', 'Keep in touch (İletişimi sürdürmek) · Get along with (İyi geçinmek) · Back up (Desteklemek)', 'Drift apart (Zamanla uzaklaşmak) · Fall out (Bozuşmak) · Let down (Hayal kırıklığına uğratmak)', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Apologizing, expressing opinion and suggestions', 'APOLOGIZING AND EXPRESSING PERSONAL OPINIONS', 'Apologize FOR + V-ing  ·  As far as I’m CONCERNED  ·  Why DON’T we + V1', 'To my mind / From my point of view, honesty and loyalty are the pillars of friendship.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Core friendship phrasal verbs', [('Get along with', 'İyi anlaşmak', YES, YES_A), ('Count / Rely on', 'Güvenmek', MAVI, MAVI_A), ('Drift apart', 'Uzaklaşmak', TUR, TUR_A), ('Let down', 'Yarı yolda bırakmak', KIR, KIR_A)])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
