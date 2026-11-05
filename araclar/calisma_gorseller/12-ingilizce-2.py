"""12. sınıf İngilizce 2. hafta (Decades and Intonation) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_on_yil_karti():
    on_yillar = [
        ('The 1970s', 'Disco &amp; Classic Rock', MAVI, MAVI_A),
        ('The 1980s', 'Synthesizers &amp; MTV', YES, YES_A),
        ('The 1990s', 'Grunge &amp; Alternative', TUR, TUR_A),
        ('The 2000s', 'Digital Pop &amp; Streaming', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(on_yillar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Four musical decades and genres cards.', 34)


def yas_grubu_muzik_grafigi():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'CROSS-GENERATIONAL MUSIC PREFERENCE SURVEY', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Older Age (50+)', 10.0, YES)
    ic += yazi(95, 74, 'Classical &amp; Jazz (%65)', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Younger Age (15-25)', 10.0, TUR)
    ic += yazi(265, 74, 'Modern Pop &amp; Indie (%75)', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Survey bar comparing music taste by generation.', 34)


def polite_disagreement_karti():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'POLITE DISAGREEMENT FORMULA', 10.6, MOR)
    ic += yazi(180, 52, '“I hear what you say, but I have a completely different opinion.”', 9.8, LAC)
    ic += yazi(180, 76, 'Acknowledges the other perspective before stating a counterview.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Formula for expressing disagreement politely in English.', 34)


def tonlama_desenleri_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Rising Intonation (↗)', 10.4, YES)
    ic += yazi(91, 50, 'Yes / No Questions', 9.6, LAC, ince=True)
    ic += yazi(91, 76, '“Do you like jazz? ↗”', 9.5, YES)

    ic += kutu(184, 6, 170, 98, MAVI_A, MAVI)
    ic += yazi(269, 26, 'Falling Intonation (↘)', 10.4, MAVI)
    ic += yazi(269, 50, 'Wh- Questions &amp; Facts', 9.6, LAC, ince=True)
    ic += yazi(269, 76, '“What is your genre? ↘”', 9.5, MAVI)
    return svg(360, 110, ic, 'Rising and falling intonation rules chart.', 34)


def muzik_teknoloji_siralamasi():
    medyalar = [
        ('1. Vinyl Record', 'Analog turntable disc', MAVI, MAVI_A),
        ('2. Cassette Tape', 'Magnetic portable tape', YES, YES_A),
        ('3. Compact Disc', 'Optical CD player', TUR, TUR_A),
        ('4. Cloud Stream', 'Digital smartphone app', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(medyalar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Evolution of audio listening technology timeline.', 34)


def beg_to_differ_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'EXPRESSING REASONED DISAGREEMENT', 10.6, TUR)
    ic += yazi(180, 52, 'Speaker B: “I beg to differ, because the lyrics are very deep.”', 9.8, LAC)
    ic += yazi(180, 76, 'Form: “I beg to differ” = formal, polite disagreement with justification.', 9.3, TUR, ince=True)
    return svg(360, 110, ic, 'Conversation panel for reasoned disagreement.', 34)


def dort_kultur_karti():
    terimler = [
        ('Nostalgic Track', 'Past emotional memory', MAVI, MAVI_A),
        ('Chart Topper', 'Ranked #1 on top lists', YES, YES_A),
        ('Sound Track', 'Original film score', TUR, TUR_A),
        ('Acoustic Set', 'Natural live sound', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(terimler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Four musical culture and industry terms.', 34)


def sifre_record_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'MUSIC HISTORY AND VOCABULARY PUZZLE', 10.8, YES)
    ic += yazi(180, 50, 'RHYTHM · ERA · CONCERT · OPINION · RELEASE · DECADE', 9.6, LAC)
    ic += yazi(180, 76, 'Unravel the clues to find the 6-letter secret English word.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Crossword puzzle board for music terms.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_on_yil_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = yas_grubu_muzik_grafigi()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = polite_disagreement_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = tonlama_desenleri_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = muzik_teknoloji_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = beg_to_differ_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_kultur_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_record_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
