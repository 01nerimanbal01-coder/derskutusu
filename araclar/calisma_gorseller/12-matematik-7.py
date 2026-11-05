"""12. sınıf Matematik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.4, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.4, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.4, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.4, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Özel sayı dizileri ve genel terimleri', [('Üçgensel Dizi', 'n·(n+1) / 2', MAVI, MAVI_A), ('Karesel Dizi', 'bn = n² (1,4,9..)', YES, YES_A), ('Fibonacci', 'Fn = Fn-1 + Fn-2', TUR, TUR_A), ('Sabit Dizi', 'p/s = r/t koşulu', MOR, MOR_A)])

def g1():
    return pano('Gerçek sayı dizisi olma koşulu', 'GERÇEK SAYI DİZİSİ TANIM KÜMESİ KOŞULU (f : Z+ → R)', 'Her n ∈ Z+ = {1, 2, 3, ...} için f(n) = an bir gerçek sayı olmalıdır.', 'Paydayı pozitif tam sayıda sıfır yapan (ör. n - 4 = 0 → n = 4) ifadeler dizi belirtmez!', KIR, KIR_A, '#fef2f2')

def g2():
    return pano('Rasyonel ifadeli sabit dizi kuralı', 'SABİT DİZİ: TÜM TERİMLERİ BİRBİRİNE EŞİT DİZİ (an = c)', 'an = (p·n + r) / (s·n + t) sabit dizi ise: p / s = r / t = c olur.', 'Örnek: (6n - k) / (2n + 4) sabit ise 6/2 = -k/4 → k = -12 ve an = 3', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('Dizilerin temel özellikleri', [('Tanım Kümesi', 'Z+ = {1,2,3,...}', MAVI, MAVI_A), ('Genel Terim', 'Kural şarttır', TUR, TUR_A), ('5. Üçgensel', '5·6 / 2 = 15', YES, YES_A), ('7. Fibonacci', '5 + 8 = 13', MOR, MOR_A)])

def g5():
    return akis4('İndirgemeli dizide terimlerin hesabı', [('1. Terim (a1)', 'a1 = 2 (Verilen)', MAVI, MAVI_A), ('2. Terim (a2)', '2 + 3(1) = 5', YES, YES_A), ('3. Terim (a3)', '5 + 3(2) = 11', TUR, TUR_A), ('4. Terim (a4)', '11 + 3(3) = 20', MOR, MOR_A)])

def g6():
    return pano('Sonlu dizi tanım kümesi ve terimleri', '5 TERİMLİ SONLU DİZİ: A5 = {1, 2, 3, 4, 5} → R', 'Genel Terim: an = 3n - 2 → Terimler: (1, 4, 7, 10, 13)', 'Sadece ilk k pozitif tam sayıda tanımlanan dizilere sonlu dizi denir.', MOR, MOR_A, '#f5f0ff')

def g7():
    return pano('İndirgemeli, eşit ve sonlu dizi kavramları', 'DİZİ TÜRLERİ: İNDİRGEMELİ · EŞİT · SONLU DİZİ', 'İndirgemeli: Önceki terimle tanımlı · Eşit: an = bn · Sonlu: Ak kümesinde', 'Her indirgemeli dizide terimleri bulmak için başlangıç terimi verilir.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Dizi temel kavramları', [('İndis (n)', 'Pozitif tam sayı', MAVI, MAVI_A), ('Genel Terim', 'an = f(n) kuralı', YES, YES_A), ('Sabit Dizi', '(c, c, c, ...)', TUR, TUR_A), ('İndirgeme', 'Önceki terim bağı', MOR, MOR_A)])

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
