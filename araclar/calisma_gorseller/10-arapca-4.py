"""10. sınıf Arapca 4. hafta (Akrabalarımı Ziyaret ve Sıla-i Rahim: Meslek ve İş Yeri Diyalogları, İsim Cümlesi, Fiil Cümlesi ve Muttasıl Zamirler) çalışma kâğıdı görselleri.
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

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [('Müzari Fiiller', 'Akraba ziyaretinde eylemler', '#2451d6', '#e8eefe'), ('Meslek Sorusu', 'مَا مِهْنَةُ عَمِّكَ؟', '#12a150', '#e3f6ea'), ('İş Yeri Sorusu', 'أَيْنَ يَعْمَلُ؟', '#ee7d12', '#fff1df'), ('Muttasıl Zamir', 'İsimlere bitişen iyelik', '#7c3aed', '#f0e9fe')]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 temel kurallar ve kavramlar kartı', 34)
def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'MESLEK VE ÇALIŞMA YERİ DİYALOG ŞEMASI', 10.5, MAVI)
    boxes = [('طَبِيبَةٌ فِي الْمُسْتَشْفَى', 'Hastanede doktor (Dişil)', '#2451d6'), ('مُهَنْدِسٌ فِي الْمَصْنَعِ', 'Fabrikada mühendis (Eril)', '#ee7d12')]
    for i, (b, d, c) in enumerate(boxes):
        x = 16 + i * 168
        ic += kutu(x, 34, 160, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 80, 52, b, 8.5, c)
        ic += yazi(x + 80, 72, d, 7, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 ana konu ve kavramsal model şeması', 34)
def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'Akrabalık İsimleri ve İyelik Zamirleri', 11, YES)
    ic += kutu(16, 34, 156, 54, '#ffffff', '#12a150', 6, 1.2)
    ic += yazi(94, 52, 'عَمّ + ـي = عَمِّي', 9, '#12a150')
    ic += yazi(94, 72, 'Benim amcam', 7.5, LAC, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', '#2451d6', 6, 1.2)
    ic += yazi(266, 52, 'خَالَة + ـكَ = خَالَتُكَ', 9, '#2451d6')
    ic += yazi(266, 72, 'Senin teyzen', 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 model ve yasa karşılaştırma şeması', 34)
def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'Fiil Cümlesi ve İsim Cümlesinde Fail Uyumu', 10.5, TUR)
    boxes = [('يَزُورُ الطُّلاَّبُ', 'Fiil tekil başlar (Açık fail)', '#2451d6'), ('الطُّلاَّبُ يَزُورُونَ', 'Haber mübtedaya uyar (Çoğul)', '#12a150'), ('تَزُورُ الطَّالِبَاتُ', 'Dişil tekil fiil başı', '#7c3aed')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 sınıflandırma ve ayrıntı şeması', 34)
def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'AKRABA ZİYARETİ VE SILA-İ RAHİM BASAMAKLARI', 10.5, MOR)
    steps = [('1. Niyet', 'Ziyaret kararı'), ('2. Selam', 'Esenlik dileme'), ('3. İkram', 'Hasbihal'), ('4. Dua', 'Rıza kazanma')]
    for i, (b, d) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 süreç ve akış basamakları modeli', 34)
def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'Muttasıl İyelik Zamirleri Karşılaştırma Şeması', 10.5, LAC)
    boxes = [('ـهُ / ـهَا', 'Onun (Eril / Dişil)', '#2451d6'), ('ـكَ / ـكِ', 'Senin (Eril / Dişil)', '#ee7d12'), ('ـي / ـنَا', 'Benim / Bizim', '#12a150')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 karşılaştırma ve ilişki diyagramı', 34)
def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    cards = [('Akraba', 'Kan bağı ve hısımlık'), ('Sıla-i Rahim', 'Ziyaret ve gözetme'), ('Meslek', 'Geçim sağlanan uzmanlık'), ('Muttasıl', 'Bitişik iyelik zamiri')]
    for i, (b, d) in enumerate(cards):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-arapca-4 temel terminoloji kavram kartları', 34)
def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: A - K - R - A - B - A', 11.5, YES)
    harfler = [('1', 'A'), ('2', 'K'), ('3', 'R'), ('4', 'A'), ('5', 'B'), ('6', 'A')]
    for i, (no, h) in enumerate(harfler):
        x = 41 + i * 48
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 21, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 21, 68, h, 16, LAC)
    return svg(360, 96, ic, '10-arapca-4 dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
