"""5. sınıf İngilizce 11. hafta (Classroom Rules, Asking For Permission, Imperatives & Theme 2 Revision) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def olumlu_olumsuz_kural_tabelasi():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Rule · DO (+)', 10.4, YESIL_K)
    ic += yazi(91, 44, 'Konuşmadan önce söz iste', 9.7, LAC, ince=True)
    ic += yazi(91, 65, 'Positive Imperative → ?', 9.8, YESIL_K)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, '2. Rule · DON’T (–)', 10.4, KIR)
    ic += yazi(269, 44, 'Sınıf içinde yüksek sesle bağırma', 9.7, LAC, ince=True)
    ic += yazi(269, 65, 'Negative Imperative → ?', 9.8, KIR)
    return svg(360, 88, ic, 'Olumlu ve olumsuz sınıf kuralı tabelaları.', 15)


def zamir_ve_sayi_kartlari():
    kartlar = [
        ('1. Mrs. Kaya', 'She · 60', MAVI, MAVI_A),
        ('2. Mr. Demir', 'He · 75', YES, YES_A),
        ('3. My Books', 'They · 84', TUR, TUR_A),
        ('4. We', 'We · 100', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.6, LAC)
    return svg(360, 84, ic, 'Özne zamirleri ve 60-100 arası sayılar kartları.', 15)


def izin_cevap_kartlari():
    kartlar = [
        ('1. Kart (Accept)', 'Yes, of course. Use it.', YES, YES_A),
        ('2. Kart (Refuse)', 'Sorry, I need my ruler now.', KIR, KIR_A),
        ('3. Kart (Accept)', 'Sure! Here you are.', MAVI, MAVI_A),
        ('4. Kart (Accept)', 'Certainly! In my case.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, met, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Kabul ve ret bildiren dört izin yanıtı kartı.', 15)


def pelin_tuna_kalem_diyalogu():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += yazi(16, 25, 'Pelin: «I forgot my red board marker. ..............................?»', 9.7, MAVI, 'start')

    ic += kutu(6, 50, 348, 38, YES_A, YES)
    ic += yazi(16, 69, 'Tuna: «Sure! Here you are.» (Kırmızı kalemini ödünç veriyor)', 9.7, YESIL_K, 'start')
    return svg(360, 94, ic, 'Pelin ve Tuna arasındaki tahta kalemi ödünç isteme diyaloğu.', 15)


def zarf_tamamlama_kartlari():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. School Library Rule', 10.2, MAVI)
    ic += yazi(91, 44, 'Read your book ..........', 9.9, LAC)
    ic += yazi(91, 65, '(Sessizce oku → quietly / loudly?)', 9.1, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Classroom Rule', 10.2, TUR)
    ic += yazi(269, 44, 'Don’t talk ..........', 9.9, LAC)
    ic += yazi(269, 65, '(Yüksek sesle konuşma!)', 9.2, TUR, ince=True)
    return svg(360, 88, ic, 'Quietly ve loudly durum zarfları uygulama kartları.', 15)


def sinif_ici_izin_akis_kartlari():
    adimlar = [
        ('1. Door', 'May I come in?', MAVI, MAVI_A),
        ('2. Teacher', 'Yes, sit quietly.', YES, YES_A),
        ('3. Request', 'Can I borrow...?', TUR, TUR_A),
        ('4. Sharing', 'Here you are!', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 55, met, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Derse giriş ve kalem ödünç alma diyalog akışı.', 15)


def sinif_5a_kural_panosu():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'CLASS 5-A · CLASSROOM RULES & INVENTORY BOARD', 10.2, MAVI)
    ic += yazi(180, 44, '• DOs: Raise your hand before speaking & Tidy up your desk!', 9.5, YESIL_K)
    ic += yazi(180, 61, '• DON’Ts: Don’t run in the classroom & Don’t leave rubbish!', 9.5, KIR)
    ic += yazi(180, 76, '• Bookshelf: 92 (ninety-two) dictionaries and storybooks.', 9.3, LAC, ince=True)
    return svg(360, 88, ic, '5-A sınıf kuralları ve kitaplık envanter panosu.', 15)


def kutuphane_kural_tasarim_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Positive Rule · DO (+)', 10.3, YESIL_K)
    ic += yazi(91, 44, 'Fiilin yalın hâli (V1) ile başla:', 9.5, LAC, ince=True)
    ic += yazi(91, 65, 'Read quietly / Keep clean...', 9.5, YESIL_K)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'Negative Rule · DON’T (–)', 10.3, KIR)
    ic += yazi(269, 44, '«Don’t + V1» yapısı ile başla:', 9.5, LAC, ince=True)
    ic += yazi(269, 65, 'Don’t shout / Don’t eat...', 9.5, KIR)
    return svg(360, 88, ic, 'Okul kütüphanesi için olumlu ve olumsuz kural yazma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = olumlu_olumsuz_kural_tabelasi()
    s[2]['gorsel'] = zamir_ve_sayi_kartlari()
    s[5]['gorsel'] = izin_cevap_kartlari()
    s[6]['gorsel'] = pelin_tuna_kalem_diyalogu()
    s[7]['gorsel'] = zarf_tamamlama_kartlari()
    s[8]['gorsel'] = sinif_ici_izin_akis_kartlari()
    s[9]['gorsel'] = sinif_5a_kural_panosu()
    s[11]['gorsel'] = kutuphane_kural_tasarim_karti()
