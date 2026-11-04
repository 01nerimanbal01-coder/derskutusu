"""12. sınıf İngilizce 1. hafta (Music Preferences and Survey) çalışma kâğıdı görselleri.
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


def dort_muzik_terimi_karti():
    terimler = [
        ('1. Lyrics', 'Words of a song', MAVI, MAVI_A),
        ('2. Composer', 'Music creator', TUR, TUR_A),
        ('3. Genre', 'Style / category', YES, YES_A),
        ('4. Rhythm', 'Beat pattern', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(terimler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' / ')[0], 9.2, LAC, ince=True)
        if ' / ' in alt:
            ic += yazi(x + 41, 78, alt.split(' / ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Four musical vocabulary cards.', 34)


def emily_anket_grafik_karti():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'STUDENT MUSIC SURVEY RESULTS (EMILY)', 10.6, MAVI)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Folk Music (%70)', 10.0, YES)
    ic += yazi(95, 74, 'Primary listening choice', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Rock Music (%30)', 10.0, TUR)
    ic += yazi(265, 74, 'Occasional preference', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Survey bar results showing Emily music preference.', 34)


def prefer_rather_karsilastirma():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Prefer ... to ...', 10.4, YES)
    ic += yazi(91, 50, 'I prefer folk to rock.', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Form: prefer noun to noun', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Would rather ... than ...', 10.4, TUR)
    ic += yazi(269, 50, 'I would rather listen than read.', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'Form: rather + bare verb', 9.4, TUR)
    return svg(360, 110, ic, 'Comparison of prefer and would rather structures.', 34)


def gorus_bildirme_olcegi():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'OPINION AND AGREEMENT EXPRESSION SCALE', 10.6, CAM)
    ic += kutu(16, 38, 98, 56, YES_A, YES)
    ic += yazi(65, 56, 'I totally agree', 9.8, YES)
    ic += yazi(65, 74, 'Full agreement', 9.0, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, TUR_A, TUR)
    ic += yazi(180, 56, 'To some extent', 9.8, TUR)
    ic += yazi(180, 74, 'Partial view', 9.0, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, KIR_A, KIR)
    ic += yazi(295, 56, 'I disagree', 9.8, KIR)
    ic += yazi(295, 74, 'Polite disagreement', 9.0, LAC, ince=True)
    return svg(360, 110, ic, 'Scale of agreement and disagreement in discussions.', 34)


def anket_adimlari_akisi():
    adımlar = [
        ('1. Design', 'Prepare questionnaire', MAVI, MAVI_A),
        ('2. Collect', 'Interview 20 peers', TUR, TUR_A),
        ('3. Analyze', 'Calculate percentages', YES, YES_A),
        ('4. Report', 'Write summary draft', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Four stages of conducting a music preference survey.', 34)


def diyalog_kart_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'CONVERSATION CARD · JAZZ DISCUSSION', 10.6, MOR)
    ic += yazi(180, 52, 'Mark: “I see your point, but I find jazz too complicated.”', 10.0, LAC)
    ic += yazi(180, 76, 'Meaning: Acknowledging an opinion with partial agreement.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Dialogue card showing conversational nuance.', 34)


def dort_muzik_ozelligi_karti():
    nitelikler = [
        ('Upbeat Tempo', 'Fast &amp; lively rhythm', YES, YES_A),
        ('Live Show', 'Concert on stage', TUR, TUR_A),
        ('Catchy Tune', 'Memorable melody', MAVI, MAVI_A),
        ('Acoustic Track', 'Pure instruments', CAM, CAM_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(nitelikler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Four musical attributes and qualities cards.', 34)


def sifre_muzik_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'MUSICAL HARMONY AND PREFERENCE PUZZLE', 10.8, TUR)
    ic += yazi(180, 50, 'MUSIC · GENRE · LYRIC · SONG · BAND · RHYTHM', 9.8, LAC)
    ic += yazi(180, 76, 'Combine the highlighted letters to discover the 6-letter word.', 9.4, TUR, ince=True)
    return svg(360, 110, ic, 'Music crossword puzzle board.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_muzik_terimi_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = emily_anket_grafik_karti()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = prefer_rather_karsilastirma()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = gorus_bildirme_olcegi()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = anket_adimlari_akisi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = diyalog_kart_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_muzik_ozelligi_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_muzik_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
