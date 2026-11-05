"""9. sınıf matematik 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def g0():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('Değişme', 'a+b = b+a · a·b = b·a', MAVI, MAVI_A), ('Birim Eleman', 'Toplama: 0 · Çarpma: 1', YES, YES_A), ('Ters Eleman', 'Toplama: -a · Çarpma: 1/a', TUR, TUR_A), ('Dağılma', 'a·(b+c) = a·b + a·c', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Gerçek sayılarda işlem özellikleri', 34)

def g1():
    b, s1, s2 = ('SAYI KÜMELERİNDE DÖRT İŞLEME GÖRE KAPALILIK ÖZELLİĞİ', 'ℕ: (+, ·) Kapalı  |  ℤ: (+, -, ·) Kapalı  |  ℚ ve ℝ: (+, -, · ve ÷[≠0]) Kapalı', 'Dikkat: İrrasyonel sayılar kümesi (ℚ\') dört işlemin hiçbirine göre kapalı değildir!')
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, b, 10, MAVI)
    ic += kutu(16, 36, 328, 64, '#f4f8fe', MAVI) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Sayı kümelerinde kapalılık özelliği', 34)

def g2():
    b, s1, s2 = ('GERÇEK SAYILARDA TERS ELEMAN UYGULAMASI', 'x = -3/5 sayısının toplama tersi A = +3/5  |  Çarpma tersi B = -5/3', 'Her a ≠ 0 gerçek sayısı için toplamaya göre tersiyle çarpmaya göre tersi çarpımı -1\'dir.')
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, b, 10, TUR) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Toplama ve çarpmaya göre ters eleman hesabı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Doğal (ℕ)', '{0, 1, 2, ...}', MAVI, MAVI_A), ('Tam (ℤ)', '{..., -1, 0, 1, ...}', TUR, TUR_A), ('Rasyonel (ℚ)', 'a/b (b ≠ 0)', YES, YES_A), ('Gerçek (ℝ)', 'ℚ ∪ ℚ\' birleşimi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Sayı kümeleri hiyerarşisi', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Örüntü', 'İşlemleri incele', YES, YES_A), ('2. Varsayım', 'Hipotez/iddia kur', MAVI, MAVI_A), ('3. Sınama', 'İspat / karşı örnek', TUR, TUR_A), ('4. Genelleme', 'Kuralı kesinleştir', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Matematiksel muhakeme ve genelleme basamakları', 34)

def g6():
    b, s1, s2 = ('ARADA OLMA (YOĞUNLUK) ÖZELLİĞİ · ℚ VE ℝ KÜMELERİ', 'Her a < b için  a < (a + b) / 2 < b  aritmetik ortalaması aradadır.', 'İki farklı rasyonel veya gerçek sayı arasında sonsuz rasyonel ve irrasyonel sayı vardır.')
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, b, 10, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, s1, 9.8, LAC) + yazi(180, 84, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Arada olma (yoğunluk) özelliği', 34)

def g7():
    b, s1, s2 = ('MATEMATİKSEL MUHAKEME KAVRAMLARI', 'Yoğunluk (Arada Olma)  ·  Yutan Eleman (Çarpmada 0)  ·  Karşı Örnek', 'Genellemenin yanlışlığını göstermek için tek bir karşı örnek (aksi örnek) yeterlidir.')
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, b, 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Yoğunluk, yutan eleman ve karşı örnek', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('ℕ Kümesi', 'En küçük eleman 0', MAVI, MAVI_A), ('ℤ Kümesi', 'Çıkarmaya kapalı', TUR, TUR_A), ('ℚ Kümesi', 'Oranlı ve devirli', YES, YES_A), ('ℚ\' Kümesi', 'π, e, kök dışına çıkmaz', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Sayı kümeleri sembol ve tanımları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
