"""6. sınıf Türkçe 14. hafta (3. Tema: Farklı Dünyalar, Zamirler ve Sözcükte Yapı) görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, ACIK = '#9aa6bd', '#eef1f6', '#475569', '#f8fafc'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: Mısır - İspanya - Norveç üçlü coğrafya sembollü gezi kartı
    ic0 = kutu(4, 4, 352, 107, GRI_A, GRI)
    ulkeler = [
        ('MISIR', 'Nil ve Piramitler', TUR, TUR_A, 0),
        ('İSPANYA', 'Akdeniz ve Endülüs', KIR, KIR_A, 1),
        ('NORVEÇ', 'Fiyort ve Kuzey Işığı', CAM, CAM_A, 2),
    ]
    for i, (b, alt, c, d, tip) in enumerate(ulkeler):
        x = 10 + i * 115
        ic0 += kutu(x, 11, 110, 93, d, c)
        ic0 += yazi(x + 55, 27, b, 9.2, c)
        if tip == 0:
            ic0 += f'<polygon points="{x+32},68 {x+52},40 {x+72},68" fill="{ACIK}" stroke="{c}" stroke-width="1.2"/>'
        elif tip == 1:
            ic0 += f'<circle cx="{x+55}" cy="54" r="13" fill="{ACIK}" stroke="{c}" stroke-width="1.3"/>'
        else:
            ic0 += f'<polyline points="{x+28},68 {x+44},42 {x+58},62 {x+74},38 {x+86},68" fill="none" stroke="{c}" stroke-width="1.5"/>'
        ic0 += yazi(x + 55, 90, alt, 8.1, LAC)
    s[0]['gorsel'] = svg(ic0, 'Mısır, İspanya ve Norveç coğrafi kültür kartları')

    # s[1]: Kök + Yapım Eki + Yapım Eki + Çekim Eki vagon modeli (yol-cu-luk-lar)
    ic1 = kutu(6, 6, 348, 103, GRI_A, GRI)
    ic1 += yazi(180, 22, 'Sözcükte Yapı Çözümlemesi: «yolculuklar»', 9.0, MAVI)
    parcalar = [
        ('yol', 'İsim Kökü', MAVI, MAVI_A),
        ('-cu', '1. Yapım Eki', YES, YES_A),
        ('-luk', '2. Yapım Eki', TUR, TUR_A),
        ('-lar', 'Çekim Eki', MOR, MOR_A),
    ]
    for i, (ek, tur, c, d) in enumerate(parcalar):
        x = 12 + i * 85
        ic1 += kutu(x, 32, 78, 56, d, c)
        ic1 += yazi(x + 39, 54, ek, 11.0, c)
        ic1 += yazi(x + 39, 76, tur, 7.8, LAC, ince=True)
        if i < 3:
            ic1 += yazi(x + 81.5, 62, '+', 10.0, SOLUK)
    s[1]['gorsel'] = svg(ic1, 'Yolculuklar sözcüğünün kök ve eklerine ayrılması')

    # s[2]: Basit - Türemiş - Birleşik sözcük kutuları
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    yapilar = [
        ('1. Grup', 'nehir-ler', 'ülke-miz-de', MAVI, MAVI_A),
        ('2. Grup', 'gez-gin', 'göz-lem-ci', YES, YES_A),
        ('3. Grup', 'Ak + deniz', 'gök + yüzü', MOR, MOR_A),
    ]
    for i, (b, s1, s2, c, d) in enumerate(yapilar):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        ic2 += yazi(x + 55, 29, b, 8.8, c)
        ic2 += f'<line x1="{x+10}" y1="38" x2="{x+100}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic2 += yazi(x + 55, 60, s1, 9.0, LAC)
        ic2 += yazi(x + 55, 82, s2, 9.0, c)
    s[2]['gorsel'] = svg(ic2, 'Üç farklı yapıda sözcük grubu kartları')

    # s[5]: Üç farklı «ki» karşılaştırması (Sıfat -ki / İlgi zamiri -ki / Bağlaç ki)
    ic5 = kutu(4, 4, 352, 107, GRI_A, GRI)
    kiler = [
        ('Sıfat Yapan -ki', 'Haritadaki ülke', '(Önündeki ismi niteler)', MAVI, MAVI_A),
        ('İlgi Zamiri -ki', 'seninki (= valizin)', '(Düşen ismin yerini tutar)', YES, YES_A),
        ('Bağlaç Olan ki', 'Seyahat et ki...', '(Ayrı yazılır, cümle bağlar)', TUR, TUR_A),
    ]
    for i, (b, orn, acik, c, d) in enumerate(kiler):
        x = 10 + i * 115
        ic5 += kutu(x, 11, 110, 93, d, c)
        ic5 += yazi(x + 55, 29, b, 8.5, c)
        ic5 += f'<line x1="{x+8}" y1="38" x2="{x+102}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic5 += yazi(x + 55, 61, orn, 8.4, LAC)
        ic5 += yazi(x + 55, 83, acik, 7.3, SOLUK, ince=True)
    s[5]['gorsel'] = svg(ic5, 'Sıfat yapan ki, ilgi zamiri ki ve bağlaç ki farkı')

    # s[6]: TDK Özel Adlara Gelen Ekler ve Kalıplaşmış ki Panosu
    ic6 = kutu(6, 6, 170, 103, YES_A, YES)
    ic6 += yazi(91, 23, 'TDK · Özel Adlara Ekler', 8.8, YES)
    ic6 += yazi(91, 46, 'Çekim eki ayrılır:', 8.0, SOLUK, ince=True)
    ic6 += yazi(91, 61, 'Norveç’te, Mısır’ın ✓', 8.5, LAC)
    ic6 += yazi(91, 79, 'Yapım eki ayrılmaz:', 8.0, SOLUK, ince=True)
    ic6 += yazi(91, 94, 'Mısırlıların, İspanyolca ✓', 8.3, YES)

    ic6 += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic6 += yazi(269, 23, 'TDK · Kalıplaşmış «ki»', 8.8, MOR)
    ic6 += yazi(269, 48, 'Sanki · Oysaki · Mademki', 8.2, LAC)
    ic6 += yazi(269, 68, 'Belki · Halbuki · Çünkü', 8.2, LAC)
    ic6 += yazi(269, 88, 'Meğerki · İllaki (Bitişik!)', 8.2, MOR)
    s[6]['gorsel'] = svg(ic6, 'TDK özel ad ekleri ve kalıplaşmış ki kuralları')

    # s[7]: İyelik zamiri inceleme kartı («Yolculuğ-umuz»)
    ic7 = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic7 += yazi(180, 24, 'Ek Hâlindeki Zamir Çözümlemesi', 9.2, CAM)
    ic7 += kutu(24, 34, 150, 58, ACIK, CAM, r=5)
    ic7 += yazi(99, 57, 'Yolculuğ - umuz', 10.2, LAC)
    ic7 += yazi(99, 78, '(Kime ait? → Bizim)', 8.3, CAM)
    ic7 += kutu(188, 34, 148, 58, YES_A, YES, r=5)
    ic7 += yazi(262, 56, '«Yolculuğumuz çok', 8.6, LAC)
    ic7 += yazi(262, 74, 'verimli geçti.»', 8.6, LAC)
    s[7]['gorsel'] = svg(ic7, 'Yolculuğumuz sözcüğünde iyelik zamiri çözümlemesi')

    # s[8]: Gezi yazısı 4 adımlı üretim akışı
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    akis = [
        ('1. Gözlem', 'Açık fikirlilik', MAVI, MAVI_A),
        ('2. Anlatım', 'Karşılaştırma', YES, YES_A),
        ('3. Söz Varlığı', 'Kök ve ek seçimi', TUR, TUR_A),
        ('4. TDK Denetimi', 'Kesme ve -ki eki', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(akis):
        x = 10 + i * 86
        ic8 += kutu(x, 14, 80, 87, d, c)
        ic8 += yazi(x + 40, 38, b, 8.5, c)
        ic8 += f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 74, alt, 7.8, LAC, ince=True)
        if i < 3:
            ic8 += f'<polygon points="{x+81},57 {x+85},52 {x+85},62" fill="{c}"/>'
    s[8]['gorsel'] = svg(ic8, 'Gezi yazısı yazma ve TDK denetim basamakları')

    # s[9]: Ova Çocuk + Mısır-İspanya-Norveç ortak tema panosu
    ic9 = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic9 += yazi(180, 22, '3. TEMA: FARKLI DÜNYALAR · METİNLER ARASI BAKIŞ', 8.8, TUR)
    ic9 += kutu(16, 32, 156, 64, ACIK, YES, r=5)
    ic9 += yazi(94, 52, 'Ova Çocuk Metni', 8.8, YES)
    ic9 += yazi(94, 72, 'Bozkır/ova → Dinginlik,', 8.0, LAC, ince=True)
    ic9 += yazi(94, 86, 'doğayla uyum ve konukseverlik', 7.8, SOLUK, ince=True)

    ic9 += kutu(188, 32, 156, 64, ACIK, MAVI, r=5)
    ic9 += yazi(266, 52, 'Mısır–İspanya–Norveç', 8.8, MAVI)
    ic9 += yazi(266, 72, 'Çöl / Akdeniz / Fiyort →', 8.0, LAC, ince=True)
    ic9 += yazi(266, 86, 'Farklı giyim, mimari ve kültür', 7.8, SOLUK, ince=True)
    s[9]['gorsel'] = svg(ic9, 'Ova Çocuk ile Mısır-İspanya-Norveç metinlerinin karşılaştırılması')
