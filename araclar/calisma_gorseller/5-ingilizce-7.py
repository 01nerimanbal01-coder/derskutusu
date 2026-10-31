"""5. sınıf İngilizce 7. hafta (National and Religious Days, Celebrations & Theme 1 Revision) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#8a5a2b', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def bayram_takvimi_svg():
    ic = kutu(6, 6, 588, 96, '#fbfcff', GRI, 10, 1.4)
    ic += yazi(300, 22, 'SCHOOL CELEBRATION CALENDAR · Prepositions & National Days', 11.0, LAC)
    kartlar = [
        ('1. Republic Day', 'We celebrate it', 'K = ?  29 October.', KIR, KIR_A),
        ('2. Youth & Sports Day', 'We celebrate it', 'L = ?  May.', MAVI, MAVI_A),
        ('3. 23 April Celebration', '23 April is', 'M = ?', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 16 + i * 192
        ic += kutu(x, 32, 180, 60, arka, renk, 8, 1.5)
        ic += yazi(x + 90, 48, bas, 10.6, renk)
        ic += yazi(x + 90, 65, s1, 10.1, LAC, 'middle', True)
        ic += yazi(x + 90, 81, s2, 10.5, LAC)
    return svg(600, 108, ic, 'Okul kutlama takvimi: K (29 October öncesi edat), L (May öncesi edat) ve M (23 April bayram adı).', 22)


def kutlama_afisi_svg():
    ic = kutu(6, 6, 588, 98, KIR_A, KIR, 10, 1.5)
    ic += f'<rect x="6" y="6" width="588" height="24" rx="10" fill="{KIR}"/><rect x="6" y="18" width="588" height="12" fill="{KIR}"/>'
    ic += yazi(300, 22, '29 OCTOBER REPUBLIC DAY CEREMONY · SCHOOL GARDEN', 10.8, '#fff')
    etk = [
        ('09:30 · Preparation', 'Hang Turkish flags &', 'red-and-white balloons', MAVI, '#fff'),
        ('10:00 · Morning Program', 'Sing the National Anthem', '& read enthusiastic poems', YES, '#fff'),
        ('11:00 · Main Show', 'Folk dance club performs', 'in the school garden!', TUR, '#fff'),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(etk):
        x = 16 + i * 192
        ic += kutu(x, 36, 180, 60, arka, renk, 8, 1.4)
        ic += yazi(x + 90, 52, bas, 10.5, renk)
        ic += yazi(x + 90, 69, s1, 10.0, LAC, 'middle', True)
        ic += yazi(x + 90, 84, s2, 10.0, LAC, 'middle', True)
    return svg(600, 110, ic, '29 Ekim Cumhuriyet Bayramı okul bahçesi kutlama afişi ve saatli etkinlik programı.', 22)


def kulup_gorev_kartlari_svg():
    kartlar = [
        ('1. Mert', 'loves doing', 'experiments', MAVI, MAVI_A),
        ('2. Ece', 'enjoys playing', 'basketball', TUR, TUR_A),
        ('3. Kaan', 'likes reading', 'storybooks', YES, YES_A),
        ('4. Aslı', 'loves acting', 'in school plays', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += kutu(x, 6, 136, 86, arka, renk, 9, 1.5)
        ic += yazi(x + 68, 23, bas, 10.8, renk)
        ic += f'<line x1="{x + 12}" y1="31" x2="{x + 124}" y2="31" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, s1, 10.1, LAC, 'middle', True)
        ic += yazi(x + 68, 70, s2, 10.4, LAC)
    return svg(600, 98, ic, 'Dört öğrencinin sevdiği etkinlik kartları: Mert, Ece, Kaan ve Aslı.', 22)


def on_in_kural_karti_svg():
    ic = kutu(8, 6, 280, 86, MAVI_A, MAVI, 10, 1.5)
    ic += yazi(148, 24, 'PREPOSITION: ON + Day / Full Date', 10.6, MAVI)
    ic += yazi(148, 46, 'on 29 October / on 23 April', 10.2, LAC)
    ic += yazi(148, 64, 'on 30 August / on Monday', 10.1, LAC, 'middle', True)
    ic += yazi(148, 80, 'Question 1: Victory Day (30 August)', 10.1, MAVI)

    ic += kutu(312, 6, 280, 86, TUR_A, TUR, 10, 1.5)
    ic += yazi(452, 24, 'PREPOSITION: IN + Month Only', 10.6, TUR)
    ic += yazi(452, 46, 'in October / in April', 10.2, LAC)
    ic += yazi(452, 64, 'in May / in August', 10.1, LAC, 'middle', True)
    ic += yazi(452, 80, 'Question 2: Youth & Sports Day (May)', 10.1, TUR)
    return svg(600, 98, ic, 'Tarihlerde on ve in edatlarının kullanım kuralı kartı.', 22)


def milli_bayram_kronoloji_svg():
    kartlar = [
        ('23 April', 'Children’s Day', YES, YES_A),
        ('19 May', 'Youth & Sports Day', MAVI, MAVI_A),
        ('30 August', 'Victory Day', TUR, TUR_A),
        ('29 October', 'Republic Day', KIR, KIR_A),
    ]
    ic = ''
    for i, (tar, ad, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 78, arka, renk, 9, 1.5)
        ic += yazi(x + 68, 32, tar, 11.0, renk)
        ic += yazi(x + 68, 58, ad, 10.1, LAC, 'middle', True)
        if i < 3:
            ic += f'<line x1="{x + 138}" y1="47" x2="{x + 146}" y2="47" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 94, ic, 'Yıl içindeki dört millî bayramın kronolojik tarih kartları.', 22)


def dort_ogrenci_tablo_svg():
    ic = kutu(6, 6, 588, 98, '#fff', GRI, 9, 1.4)
    ic += f'<rect x="6" y="6" width="588" height="22" rx="9" fill="{LAC}"/><rect x="6" y="18" width="588" height="10" fill="{LAC}"/>'
    bas = [('Student', 65), ('Country', 185), ('Favourite Club & Activity', 355), ('School Rule', 515)]
    for b, x in bas:
        ic += yazi(x, 21, b, 10.4, '#fff')
    sat = [
        ('Emre', 'Türkiye', 'Chess club (strategy games)', 'Arrive on time'),
        ('Emily', 'the UK', 'Art club (painting pictures)', 'Keep class clean'),
        ('Kenji', 'Japan', 'Science club (experiments)', 'Wear a lab coat'),
        ('Leyla', 'Azerbaijan', 'Folk dance club (dancing)', 'Don’t run inside'),
    ]
    for i, (ad, ulk, klp, krl) in enumerate(sat):
        y = 30 + i * 17
        ic += f'<rect x="10" y="{y}" width="580" height="15" rx="3" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(65, y + 11.5, ad, 10.2, MAVI)
        ic += yazi(185, y + 11.5, ulk, 10.1, LAC, 'middle', True)
        ic += yazi(355, y + 11.5, klp, 10.1, LAC, 'middle', True)
        ic += yazi(515, y + 11.5, krl, 10.1, LAC, 'middle', True)
    return svg(600, 110, ic, 'Emre, Emily, Kenji ve Leyla’nın ülke, kulüp ve okul kuralı tablosu.', 23)


def okul_kurallari_tabela_svg():
    kurallar = [
        ('Rule 1 · Punctuality', 'You must arrive at school on time.', YES, YES_A),
        ('Rule 2 · Classroom', 'Keep your classroom clean and tidy!', MAVI, MAVI_A),
        ('Rule 3 · Library', 'You mustn’t shout in the library.', TUR, TUR_A),
        ('Rule 4 · Corridors', 'Don’t run fast in the corridors!', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, m, renk, arka) in enumerate(kurallar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 52
        ic += kutu(x, y, 286, 44, arka, renk, 8, 1.5)
        ic += yazi(x + 14, y + 17, bas, 10.5, renk, 'start')
        ic += yazi(x + 14, y + 34, m, 10.1, LAC, 'start', True)
    return svg(600, 112, ic, 'Dört temel okul kuralı panosu: zamanında gelme, sınıfı temiz tutma, kütüphanede sessizlik ve koridorda koşmama.', 22)


def diyalog_tamamlama_svg():
    ic = kutu(8, 6, 280, 86, MAVI_A, MAVI, 10, 1.5)
    ic += yazi(148, 23, 'Dialogue 1 · Asking Country', 10.6, MAVI)
    ic += yazi(20, 46, 'Arda: (1) ______________________?', 10.2, LAC, 'start')
    ic += yazi(20, 68, 'Baku Student: I am from Azerbaijan.', 10.2, MAVI, 'start', True)

    ic += kutu(312, 6, 280, 86, MOR_A, MOR, 10, 1.5)
    ic += yazi(452, 23, 'Dialogue 2 · Asking School Club', 10.6, MOR)
    ic += yazi(324, 46, 'Sude: (2) ______________________?', 10.2, LAC, 'start')
    ic += yazi(324, 68, 'Pelin: I am in the drama club.', 10.2, MOR, 'start', True)
    return svg(600, 98, ic, 'Ülke ve okul kulübü sorma diyalog kartları.', 22)


def cumhuriyet_bayrami_kart_svg():
    ic = kutu(8, 6, 584, 88, KIR_A, KIR, 10, 1.5)
    ic += yazi(300, 24, 'REPUBLIC DAY FACT CARD · 29 OCTOBER', 11.0, KIR)
    kutular = [
        ('Date', 'on 29 October', 20, KIR),
        ('Decoration', 'decorate with flags', 210, MAVI),
        ('Activities', 'sing Anthem & read poems', 400, YES),
    ]
    for bas, deg, x, r in kutular:
        ic += kutu(x, 34, 178, 48, '#fff', r, 8, 1.3)
        ic += yazi(x + 89, 52, bas, 10.5, r)
        ic += yazi(x + 89, 71, deg, 10.2, LAC, 'middle', True)
    return svg(600, 100, ic, '29 Ekim Cumhuriyet Bayramı tarih, süsleme ve kutlama etkinlikleri bilgi kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bayram_takvimi_svg()
    s[4]['gorsel'] = kutlama_afisi_svg()
    s[5]['gorsel'] = kulup_gorev_kartlari_svg()
    s[6]['gorsel'] = on_in_kural_karti_svg()
    s[7]['gorsel'] = milli_bayram_kronoloji_svg()
    s[8]['gorsel'] = dort_ogrenci_tablo_svg()
    s[9]['gorsel'] = okul_kurallari_tabela_svg()
    s[10]['gorsel'] = diyalog_tamamlama_svg()
    s[12]['gorsel'] = cumhuriyet_bayrami_kart_svg()
