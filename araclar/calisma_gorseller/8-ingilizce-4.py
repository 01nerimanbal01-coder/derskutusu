"""8. sınıf İngilizce 4. hafta (Teen Life: hoşlandıklarını/hoşlanmadıklarını anlatma, günlük etkinlikler, sıklık zarfları, zaman edatları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

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


def etkinlik_kartlari():
    """Dört boş zaman etkinliği kartı (karate, trekking, soccer, a concert)."""
    kartlar = [
        ('1. Kart', 'karate', TUR, TUR_A, 4),
        ('2. Kart', 'trekking', YES, YES_A, 92),
        ('3. Kart', 'soccer', MAVI, MAVI_A, 180),
        ('4. Kart', 'a concert', MOR, MOR_A, 268),
    ]
    ic = ''
    for i, (bas, alt, r, z, x) in enumerate(kartlar):
        cx = x + 44
        ic += kutu(x, 4, 86, 82, z, r, 8, 1.3)
        ic += yazi(cx, 19, bas, 10.5, r)
        if i == 0:
            # Karate kuşağı sembolü
            ic += f'<rect x="{cx - 24}" y="34" width="48" height="10" rx="4" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
            ic += f'<rect x="{cx - 6}" y="32" width="12" height="14" rx="3" fill="{LAC}"/>'
            ic += f'<line x1="{cx - 3}" y1="46" x2="{cx - 12}" y2="56" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
            ic += f'<line x1="{cx + 3}" y1="46" x2="{cx + 12}" y2="56" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
        elif i == 1:
            # Dağ ve yürüyüş rotası
            ic += f'<polygon points="{cx - 24},56 {cx - 6},28 {cx + 10},56" fill="{YES}" opacity="0.35" stroke="{YES}" stroke-width="1.5"/>'
            ic += f'<polygon points="{cx - 4},56 {cx + 12},34 {cx + 26},56" fill="{YES}" opacity="0.6" stroke="{YES}" stroke-width="1.5"/>'
        elif i == 2:
            # Futbol topu
            ic += f'<circle cx="{cx}" cy="42" r="14" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
            ic += f'<polygon points="{cx},35 {cx + 6},40 {cx + 4},47 {cx - 4},47 {cx - 6},40" fill="{LAC}"/>'
        else:
            # Sahne mikrofonu / nota
            ic += f'<circle cx="{cx - 6}" cy="48" r="5" fill="{MOR}"/>'
            ic += f'<line x1="{cx - 1}" y1="48" x2="{cx - 1}" y2="30" stroke="{MOR}" stroke-width="2"/>'
            ic += f'<line x1="{cx - 1}" y1="30" x2="{cx + 11}" y2="34" stroke="{MOR}" stroke-width="2.5"/>'
            ic += f'<circle cx="{cx + 6}" cy="50" r="5" fill="{MOR}"/><line x1="{cx + 11}" y1="50" x2="{cx + 11}" y2="34" stroke="{MOR}" stroke-width="2"/>'
        ic += yazi(cx, 76, alt, 11, LAC)
    return svg(358, 90, ic, 'Dört etkinlik kartı: 1. kart karate, 2. kart trekking, 3. kart soccer, 4. kart a concert.', 18)


def sally_hatice_kartlari():
    """Sally ve Hatice'nin günlük rutin karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(90, 19, 'Sally’s Routine', 11.5, '#fff')
    ic += yazi(12, 39, '- School: by bike · ends at 3.50', 10.5, LAC, 'start', True)
    ic += yazi(12, 55, '- Mon & Wed: cooking class', 10.5, LAC, 'start', True)
    ic += yazi(12, 71, '- Weekend: nature & camping', 10.5, LAC, 'start', True)
    ic += yazi(12, 87, '- Sun evening: comedy films', 10.5, MAVI, 'start')

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="22" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="10" fill="{TUR}"/>'
    ic += yazi(270, 19, 'Hatice’s Routine', 11.5, '#fff')
    ic += yazi(192, 39, '- School bus: at 8.15', 10.5, LAC, 'start', True)
    ic += yazi(192, 55, '- Classes finish: at 4.30', 10.5, LAC, 'start', True)
    ic += yazi(192, 71, '- Evening: homework & books', 10.5, LAC, 'start', True)
    ic += yazi(192, 87, '- Regular weekday timetable', 10.5, TUR, 'start')
    return svg(360, 100, ic, 'Sally ve Hatice günlük rutin kartları: Sally bisikletle okula gider, dersleri 3.50 de biter, Pazartesi-Çarşamba yemek kursuna katılır. Hatice 8.15 te okul servisine biner, okul 4.30 da biter.', 18)


def gorus_kartlari():
    """Arda ve Zeynep'in görüş ve hoşlanma/hoşlanmama kartları."""
    ic = kutu(4, 4, 172, 78, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, 'Arda’s Opinion', 11.5, YES)
    ic += yazi(90, 40, '“I think trekking is exciting', 10.5, LAC, 'middle', True)
    ic += yazi(90, 55, 'and terrific!”', 10.5, LAC, 'middle', True)
    ic += yazi(90, 72, '(Positive: exciting)', 10.5, YES)

    ic += kutu(184, 4, 172, 78, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, 'Zeynep’s Opinion', 11.5, KIR)
    ic += yazi(270, 40, '“I can’t stand loud music.', 10.5, LAC, 'middle', True)
    ic += yazi(270, 55, 'I think it is unbearable.”', 10.5, LAC, 'middle', True)
    ic += yazi(270, 72, '(Negative: unbearable)', 10.5, KIR)
    return svg(360, 86, ic, 'Arda ve Zeynep görüş kartları: Arda trekking için exciting ve terrific diyor; Zeynep yüksek sesli müziğe tahammül edemediğini ve unbearable bulduğunu söylüyor.', 18)


def zaman_edati_fisleri():
    """Dört öğrencinin in, on, at zaman edatlarıyla kurduğu cümle fişleri."""
    fisler = [
        ('1. fiş · Ela', 'Ela has piano lessons', 'on Tuesdays.', MAVI, MAVI_A),
        ('2. fiş · Bora', 'We have lunch together', 'at noon.', YES, YES_A),
        ('3. fiş · Tuna', 'I go jogging in the park', 'in Saturday morning.', KIR, KIR_A),
        ('4. fiş · Sude', 'My family goes camping', 'in summer.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 50
        ic += kutu(x, y, 172, 46, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 27, s1, 10.5, LAC, 'start', True)
        ic += yazi(x + 10, y + 40, s2, 10.5, LAC, 'start', True)
    return svg(360, 104, ic, 'Dört zaman edatı fişi: 1. fiş on Tuesdays, 2. fiş at noon, 3. fiş in Saturday morning, 4. fiş in summer.', 18)


def siklik_basamaklari():
    """Azdan çoğa sıklık zarfları sütun grafiği."""
    zarflar = [
        ('never', 14, GRI),
        ('rarely', 28, CAM),
        ('sometimes', 44, MOR),
        ('often', 60, TUR),
        ('usually', 76, MAVI),
        ('always', 92, YES),
    ]
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    ic += yazi(180, 19, 'Frequency Adverbs (azdan çoğa: never → always)', 11, LAC)
    for i, (ad, h, r) in enumerate(zarflar):
        x = 14 + i * 56
        bh = int(h * 0.45)
        by = 68 - bh
        ic += f'<rect x="{x}" y="{by}" width="42" height="{bh}" rx="5" fill="{r}"/>'
        ic += yazi(x + 21, 82, ad, 10.5, LAC)
    return svg(360, 94, ic, 'Sıklık zarfları azdan çoğa: never, rarely, sometimes, often, usually, always.', 18)


def enerji_anket_karti():
    """6 soruluk enerji anketi puan anahtarı ve Kerem'in cevap şeridi."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 19, 'ENERGY QUIZ · Points: A = 5  |  B = 3  |  C = 1', 11, '#fff')
    cevaplar = [('Q1', 'B'), ('Q2', 'A'), ('Q3', 'B'), ('Q4', 'C'), ('Q5', 'A'), ('Q6', 'B')]
    for i, (q, c) in enumerate(cevaplar):
        x = 12 + i * 56
        ic += kutu(x, 32, 48, 28, '#fff', MAVI, 6, 1.2)
        ic += yazi(x + 24, 45, f'{q}: {c}', 11, LAC)
        puan = {'A': '5 pt', 'B': '3 pt', 'C': '1 pt'}[c]
        ic += yazi(x + 24, 57, puan, 10.5, TUR, 'middle', True)
    ic += yazi(180, 76, '5–10: Be more energetic · 10–20: Not bad · 20–30: Really energetic', 10.5, LAC, 'middle', True)
    return svg(360, 96, ic, 'Enerji anketi kartı: A=5, B=3, C=1 puan. Kerem in cevapları Q1:B, Q2:A, Q3:B, Q4:C, Q5:A, Q6:B.', 18)


def dinleme_not_kartlari():
    """Üç gencin dinleme notları özet kartları."""
    kartlar = [
        ('1. Genç (Swim)', ['Morning training', 'Wakes up early'], MAVI, MAVI_A, 4),
        ('2. Genç (Music)', ['Plays instrument', 'Likes classical', 'Hates pop music'], MOR, MOR_A, 122),
        ('3. Genç (Soccer)', ['Training: 7.30 a.m.', 'Home at 6.00 p.m.', 'Helps his mum'], YES, YES_A, 240),
    ]
    ic = ''
    for bas, sat, r, z, x in kartlar:
        ic += kutu(x, 4, 116, 78, z, r, 8, 1.3)
        ic += yazi(x + 58, 19, bas, 10.5, r)
        for k, s_met in enumerate(sat):
            ic += yazi(x + 58, 37 + k * 16, s_met, 10.5, LAC, 'middle', True)
    return svg(360, 86, ic, 'Üç gencin dinleme notu kartı: 1. genç yüzme takımı sabah antrenmanı, 2. genç müzik dersi klasik müzik sever pop sevmez, 3. genç 7.30 futbol antrenmanı akşam 6 da annesine yardım eder.', 18)


def tercih_tablosu():
    """Dört arkadaşın etkinlik tercihlerini gösteren sembol tablosu."""
    ic = kutu(4, 4, 352, 96, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'Activity Preferences ( + : keen on / enjoy   − : dislike / hate )', 10.5, '#fff')
    basliklar = ['Name', 'Trekking', 'Bowling', 'Preparing dinner']
    xler = [44, 132, 218, 306]
    for x, b in zip(xler, basliklar):
        ic += yazi(x, 38, b, 10.5, MAVI)
    satirlar = [
        ('Emir', '+', '−', '+'),
        ('Cem', '−', '−', '+'),
        ('Duru', '+', '+', '+'),
        ('Aslı', '−', '+', '−'),
    ]
    for i, sat in enumerate(satirlar):
        y = 44 + i * 13
        for x, val in zip(xler, sat):
            renk = YES if val == '+' else (KIR if val == '−' else LAC)
            ic += yazi(x, y + 10, val, 11, renk)
    return svg(360, 104, ic, 'Etkinlik tercih tablosu: Emir trekking +, bowling -, preparing dinner +; Cem trekking -, bowling -, preparing dinner +; Duru üçü de +; Aslı trekking -, bowling +, preparing dinner -.', 18)


def karisik_cumle_seritleri():
    """A ve B karışık kelime şeritleri."""
    satirlar = [
        ('A', ['walk to school', 'I', 'on weekdays', 'usually'], MAVI, MAVI_A),
        ('B', ['draws pictures', 'My sister', 'in the afternoon', 'often'], TUR, TUR_A),
    ]
    ic = ''
    for r, (harf, kartlar, renk, dolgu) in enumerate(satirlar):
        y = 6 + r * 40
        ic += rozet(14, y + 15, harf, renk)
        x = 28
        for k in kartlar:
            w = 12 + len(k) * 5.8
            ic += kutu(x, y, w, 30, dolgu, renk, 6, 1.3)
            ic += yazi(x + w / 2, y + 19, k, 10.5, LAC, 'middle', True)
            x += w + 5
    return svg(360, 84, ic, 'Karışık kelime şeritleri: A satırı walk to school, I, on weekdays, usually. B satırı draws pictures, My sister, in the afternoon, often.', 18)


def rutin_ipucu_karti():
    """Açık uçlu yazma sorusu için üç soruluk ipucu kartı."""
    ic = kutu(4, 4, 352, 74, CAM_A, CAM, 8, 1.3)
    ic += yazi(180, 20, 'Writing Prompts · My Weekly Routine', 11.5, CAM)
    ic += yazi(16, 40, '1) What time do you wake up on weekdays? (always / usually + at)', 10.5, LAC, 'start', True)
    ic += yazi(16, 56, '2) What do you enjoy doing after school? (love / enjoy / fond of + -ing)', 10.5, LAC, 'start', True)
    ic += yazi(16, 72, '3) What do you do at the weekend? (often / sometimes + on / at)', 10.5, LAC, 'start', True)
    return svg(360, 82, ic, 'Yazma ipucu kartı: 1. What time do you wake up, 2. What do you enjoy doing after school, 3. What do you do at the weekend.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = etkinlik_kartlari()
    s[1]['gorsel'] = sally_hatice_kartlari()
    s[3]['gorsel'] = gorus_kartlari()
    s[5]['gorsel'] = zaman_edati_fisleri()
    s[6]['gorsel'] = siklik_basamaklari()
    s[7]['gorsel'] = enerji_anket_karti()
    s[8]['gorsel'] = dinleme_not_kartlari()
    s[9]['gorsel'] = tercih_tablosu()
    s[10]['gorsel'] = karisik_cumle_seritleri()
    s[13]['gorsel'] = rutin_ipucu_karti()
