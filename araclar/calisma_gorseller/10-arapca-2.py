"""10. sınıf Arapça 2. hafta (Akrabalarım ve Meslekleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_zamirler():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('أَنْتَ', 'Sen (Eril)', MAVI, MAVI_A),
        ('أَنْتِ', 'Sen (Dişil)', TUR, TUR_A),
        ('أَنْتُمَا', 'Siz İkiniz', YES, YES_A),
        ('نَحْنُ', 'Biz (Çoğul)', MOR, MOR_A)
    ]
    for i, (ar, tr, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 36, ar, 16, c)
        ic += f'<line x1="{x + 10}" y1="48" x2="{x + 70}" y2="48" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 68, tr, 10, LAC, ince=True)
    return svg(360, 100, ic, 'Muhatap ve mütekellim zamirleri tablosu', 34)


def g1_ikil_muhendis():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += f'<circle cx="84" cy="38" r="20" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="84" y1="18" x2="84" y2="58" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="64" y1="38" x2="104" y2="38" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(84, 74, 'مُهَنْدِسَانِ (İki Mühendis)', 10, LAC)
    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 34, 'أَنْتُمَا تَعْمَلَانِ', 13, MAVI)
    ic += yazi(257, 52, 'فِي الْمَصْنَعِ', 12, LAC)
    ic += yazi(257, 72, 'Siz ikiniz fabrikada çalışıyorsunuz', 9, SOLUK, ince=True)
    return svg(360, 100, ic, 'İki mühendis ve fabrika çalışma cümlesi', 34)


def g2_vatan_savunma():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += kutu(14, 12, 120, 76, '#d8f3e2', YES, 6, 1.2)
    ic += f'<polygon points="74,20 104,32 94,66 74,78 54,66 44,32" fill="{YES}" opacity="0.2" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(74, 52, 'دِفَاع', 12, YES)
    ic += kutu(146, 12, 200, 76, '#eaf8f0', YES, 6, 1.2)
    ic += yazi(246, 36, 'يُدَافِعُ الْجُنْدِيُّ عَنِ الْوَطَنِ', 12, YES)
    ic += yazi(246, 56, 'Fiil: يُدَافِعُ عَنْ (Savunur)', 10, LAC)
    ic += yazi(246, 72, 'Asker vatanı savunur / korur', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Vatanı savunma cümlesi ve kalkan sembolü', 34)


def g3_dil_bilgisi():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    turler = [
        ('Tekil (Müfred)', 'أَنَا / أَنْتَ / أَنْتِ', MAVI, MAVI_A),
        ('İkil (Müsenna)', 'أَنْتُمَا (Eril/Dişil)', TUR, TUR_A),
        ('Çoğul (Cemi)', 'أَنْتُمْ / أَنْتُنَّ / نَحْنُ', YES, YES_A)
    ]
    for i, (b, ornek, c, d) in enumerate(turler):
        x = 10 + i * 115
        ic += kutu(x, 10, 108, 80, d, c, 6, 1.2)
        ic += yazi(x + 54, 32, b, 10.5, c)
        ic += f'<line x1="{x + 10}" y1="42" x2="{x + 98}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 54, 64, ornek, 11, LAC)
    return svg(360, 100, ic, 'Zamirlerin tekil ikil ve çoğul ayrımı', 34)


def g5_diyalog_akisi():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    adımlar = [
        ('1. Selam', 'السَّلَامُ عَلَيْكُمْ'),
        ('2. Kendisi', 'أَنَا طَالِبٌ'),
        ('3. Ailesi', 'أَبِي مُهَنْدِسٌ'),
        ('4. Kurum', 'فِي الشَّرِكَةِ')
    ]
    for i, (no, ar) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#fef6ec', TUR, 6, 1.2)
        ic += yazi(x + 40, 30, no, 10, TUR)
        ic += f'<line x1="{x + 10}" y1="40" x2="{x + 70}" y2="40" stroke="{TUR}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, ar, 10.5, LAC)
    return svg(360, 100, ic, 'Kendini tanıtma diyalog aşamaları', 34)


def g6_hastane_karti():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 120, 76, '#ece4fd', MOR, 6, 1.2)
    ic += f'<rect x="68" y="24" width="12" height="36" fill="{MOR}" rx="2"/>'
    ic += f'<rect x="56" y="36" width="36" height="12" fill="{MOR}" rx="2"/>'
    ic += yazi(74, 76, 'مُسْتَشْفَى (Hastane)', 10, LAC)
    ic += kutu(146, 12, 200, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(246, 36, 'أَنْتُنَّ تَعْمَلْنَ', 14, MOR)
    ic += yazi(246, 56, 'فِي الْمُسْتَشْفَى', 12, LAC)
    ic += yazi(246, 74, 'Siz kadınlar hastanede çalışıyorsunuz', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Kadın sağlık personeli ve hastane kartı', 34)


def g8_harficer_eslesme():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ciftler = [
        ('يُدَافِعُ', 'عَنْ', 'Savunmak', MAVI),
        ('يُحَافِظُ', 'عَلَى', 'Korumak', YES),
        ('تَهْتَمُّ', 'بِـ', 'İlgilenmek', TUR),
        ('يَسُوقُ', '—', 'Sürmek', MOR)
    ]
    for i, (f, cer, anl, col) in enumerate(ciftler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f2fbfd', col, 6, 1.2)
        ic += yazi(x + 40, 30, f, 12, col)
        ic += yazi(x + 40, 48, cer, 11, col)
        ic += f'<line x1="{x + 10}" y1="56" x2="{x + 70}" y2="56" stroke="{col}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 72, anl, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Fiil ve harf-i cer eşleşmeleri', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KELİME ŞİFRE ŞERİDİ: A - İ - L - E', 11.5, YES)
    harfler = [('1', 'A'), ('2', 'İ'), ('3', 'L'), ('4', 'E')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 25, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Aile şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_zamirler()
    s[1]['gorsel'] = g1_ikil_muhendis()
    s[2]['gorsel'] = g2_vatan_savunma()
    s[3]['gorsel'] = g3_dil_bilgisi()
    s[5]['gorsel'] = g5_diyalog_akisi()
    s[6]['gorsel'] = g6_hastane_karti()
    s[8]['gorsel'] = g8_harficer_eslesme()
    s[10]['gorsel'] = g10_sifre_seridi()
