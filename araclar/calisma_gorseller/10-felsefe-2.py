"""10. sınıf Felsefe 2. hafta (Felsefenin Alt Disiplinleri ve İşlevleri) çalışma kâğıdı görselleri.
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

def g0_alt_disiplinler():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    alanlar = [
        ('Ontoloji', 'Varlık felsefesi', MAVI, MAVI_A),
        ('Epistemoloji', 'Bilgi felsefesi', YES, YES_A),
        ('Etik', 'Ahlak felsefesi', TUR, TUR_A),
        ('Estetik', 'Sanat felsefesi', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(alanlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefenin temel dört alt disiplini kartı', 34)


def g1_sokratik():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += kutu(14, 12, 140, 76, '#fef6ec', TUR, 6, 1.2)
    ic += yazi(84, 30, '1. İroni (Alay)', 10.5, TUR)
    ic += yazi(84, 50, 'Sahte bilgiyi çürütme', 9, LAC, ince=True)
    ic += yazi(84, 68, 'Hiçbir şey bilmediğini fark ettirme', 8, SOLUK, ince=True)

    ic += kutu(168, 12, 178, 76, '#fffaf4', TUR, 6, 1.2)
    ic += yazi(257, 30, '2. Maiotik (Doğurtma)', 10.5, YES)
    ic += yazi(257, 50, 'Zihindeki doğru kavramı', 9, LAC, ince=True)
    ic += yazi(257, 68, 'sorularla açığa çıkarma', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Sokratik yöntem iki aşamalı şema', 34)


def g2_refleksif():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # Refleksif dairesel ok
    ic += f'<circle cx="84" cy="50" r="30" fill="none" stroke="{MAVI}" stroke-width="2.5" stroke-dasharray="8,4"/>'
    ic += yazi(84, 46, 'Düşünce', 10, MAVI)
    ic += yazi(84, 58, 'Üzerine Düşünüş', 8, LAC)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 30, 'REFLEKSİF DÜŞÜNME', 10.5, MAVI)
    ic += yazi(257, 48, 'Zihnin kendi ürettiği bilgi', 9, LAC, ince=True)
    ic += yazi(257, 62, 've yargıları yeniden', 9, LAC, ince=True)
    ic += yazi(257, 76, 'eleştirel süzgeçten geçirmesi', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Refleksif düşünme döngü şeması', 34)


def g3_bilim_din_sanat():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    alanlar = [
        ('Felsefe', 'Eleştirel akıl', MAVI, MAVI_A),
        ('Bilim', 'Deney & Olgu', YES, YES_A),
        ('Din', 'İnanç & Vahiy', TUR, TUR_A),
        ('Sanat', 'Sezgi & Estetik', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(alanlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefenin bilim din ve sanatla mukayesesi', 34)


def g5_sokratik_adimlari():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    adımlar = [
        ('1. Tanım', 'İlk kabulleniş'),
        ('2. İroni', 'Çelişkiyi görme'),
        ('3. Aporia', 'Tıkanma anı'),
        ('4. Doğurtma', 'Öz kavram')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Sokratik sorgulama adımları akış şeması', 34)


def g6_toplumsal_islev():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ic += kutu(14, 12, 150, 76, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(89, 28, 'Bireysel İşlev', 10.5, CAM)
    ic += yazi(89, 46, '• Ön yargılardan arınma', 9, LAC, ince=True)
    ic += yazi(89, 60, '• Bağımsız akıl yürütme', 9, LAC, ince=True)
    ic += yazi(89, 74, '• Hayata anlam katma', 9, LAC, ince=True)

    ic += kutu(176, 12, 170, 76, '#f2fbfd', CAM, 6, 1.2)
    ic += yazi(261, 28, 'Toplumsal İşlev', 10.5, TUR)
    ic += yazi(261, 46, '• Farklı fikirlere hoşgörü', 9, LAC, ince=True)
    ic += yazi(261, 60, '• Demokrasi ve hukuk bilinci', 9, LAC, ince=True)
    ic += yazi(261, 74, '• Toplumsal uzlaşı kültürü', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefenin bireysel ve toplumsal işlevleri', 34)


def g8_sorular():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    kartlar = [
        ('Varlık', 'Ne vardır?', MAVI),
        ('Bilgi', 'Ne bilebilirim?', YES),
        ('Ahlak', 'Ne yapmalıyım?', TUR),
        ('Sanat', 'Güzel nedir?', KIR)
    ]
    for i, (b, s, col) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f4effe', col, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, col)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{col}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, s, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefenin kök soruları şeması', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: E - T - İ - K', 11.5, YES)
    harfler = [('1', 'E'), ('2', 'T'), ('3', 'İ'), ('4', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 25, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Etik şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_alt_disiplinler()
    s[1]['gorsel'] = g1_sokratik()
    s[2]['gorsel'] = g2_refleksif()
    s[3]['gorsel'] = g3_bilim_din_sanat()
    s[5]['gorsel'] = g5_sokratik_adimlari()
    s[6]['gorsel'] = g6_toplumsal_islev()
    s[8]['gorsel'] = g8_sorular()
    s[10]['gorsel'] = g10_sifre_seridi()
