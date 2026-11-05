"""10. sınıf Fizik 4. hafta (Bir Boyutta Sabit İvmeli Hareket: Hız-Zaman, İvme-Zaman Grafikleri, Hareket Denklemleri ve Serbest Düşme) çalışma kâğıdı görselleri.
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
    kartlar = [('v-t Eğimi', 'İvmeyi (a = Δv/Δt) verir', '#2451d6', '#e8eefe'), ('v-t Alanı', 'Yer değiştirmeyi (Δx) verir', '#12a150', '#e3f6ea'), ('a-t Alanı', 'Hız değişimini (Δv) verir', '#ee7d12', '#fff1df'), ('Serbest Düşme', 'İvme g = 10 m/s², h = 5t²', '#7c3aed', '#f0e9fe')]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 temel kurallar ve kavramlar kartı', 34)
def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'SABİT İVMELİ HAREKET DENKLEMLERİ VE HESAP', 10.5, MAVI)
    boxes = [('Hız: v = v₀ + a · t', 'v = 0 + 4 · 5 = 20 m/s', '#2451d6'), ('Yol: Δx = v₀t + ½ · a · t²', 'Δx = ½ · 4 · 25 = 50 metre', '#12a150')]
    for i, (b, d, c) in enumerate(boxes):
        x = 16 + i * 168
        ic += kutu(x, 34, 160, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 80, 52, b, 8.5, c)
        ic += yazi(x + 80, 72, d, 7, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 ana konu ve kavramsal model şeması', 34)
def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'Serbest Düşmede Hız ve Alınan Yol (g = 10 m/s²)', 11, YES)
    ic += kutu(16, 34, 156, 54, '#ffffff', '#12a150', 6, 1.2)
    ic += yazi(94, 52, '1. saniyede: v = 10 m/s', 9, '#12a150')
    ic += yazi(94, 72, 'Alınan yol h₁ = 5 m', 7.5, LAC, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', '#2451d6', 6, 1.2)
    ic += yazi(266, 52, '2. saniyede: v = 20 m/s', 9, '#2451d6')
    ic += yazi(266, 72, 'Alınan yol h₂ = 15 m (Top. 20 m)', 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 model ve yasa karşılaştırma şeması', 34)
def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'Serbest Düşmede Saniyelik Yol Oranları (h, 3h, 5h)', 10.5, TUR)
    boxes = [('t = 1 s', '5 m yol katedilir (h)', '#2451d6'), ('t = 2 s', '15 m yol katedilir (3h)', '#12a150'), ('t = 3 s', '25 m yol katedilir (5h)', '#ee7d12')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 sınıflandırma ve ayrıntı şeması', 34)
def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'SERBEST DÜŞEN CİSMİN ZAMANLA DÜŞÜŞ BASAMAKLARI', 10.5, MOR)
    steps = [('t = 1 s', 'v = 10 m/s, H = 5 m'), ('t = 2 s', 'v = 20 m/s, H = 20 m'), ('t = 3 s', 'v = 30 m/s, H = 45 m'), ('t = 4 s', 'v = 40 m/s, H = 80 m')]
    for i, (b, d) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 süreç ve akış basamakları modeli', 34)
def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'Hız ve İvme Vektörleri Yön İlişkisi', 10.5, LAC)
    boxes = [('Hızlanan Hareket', 'v ve a aynı yönlü (v · a > 0)', '#12a150'), ('Yavaşlayan Hareket', 'v ve a zıt yönlü (v · a < 0)', '#d63a3a'), ('Serbest Düşme', 'Aşağı yönde düzgün hızlanır', '#2451d6')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 karşılaştırma ve ilişki diyagramı', 34)
def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    cards = [('İvme (a)', 'Birim zamandaki hız değişimi'), ('Konum (x)', 'Referansa olan yönlü uzaklık'), ('Yer Çekimi (g)', 'Düşüş ivmesi ~10 m/s²'), ('Fren Mesafesi', 'Durana kadar alınan yol')]
    for i, (b, d) in enumerate(cards):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-fizik-4 temel terminoloji kavram kartları', 34)
def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: D - Ü - Ş - M - E', 11.5, YES)
    harfler = [('1', 'D'), ('2', 'Ü'), ('3', 'Ş'), ('4', 'M'), ('5', 'E')]
    for i, (no, h) in enumerate(harfler):
        x = 48 + i * 55
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, '10-fizik-4 dersi şifre anahtar harf kutuları', 34)

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
