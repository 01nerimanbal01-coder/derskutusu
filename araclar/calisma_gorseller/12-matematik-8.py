"""12. sınıf Matematik 8. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.5, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Aritmetik dizi temel formülleri', [('Ortak Fark (d)', 'a_(n+1) - a_n', MAVI, MAVI_A), ('Genel Terim', 'a₁ + (n - 1)·d', YES, YES_A), ('Toplam (S_n)', '(n/2)·(a₁ + a_n)', MOR, MOR_A), ('Terim Farkı', 'a_n = S_n - S_(n-1)', TUR, TUR_A)])

def g1():
    return uclu('Aritmetik dizide iki terimden 20. terimi bulma', 'ARİTMETİK DİZİDE a₅ = 14 VE a₁₂ = 35 İSE a₂₀ HESABI', ('1. Ortak Fark (d)', '(35 - 14) / (12 - 5) = 3', MAVI, MAVI_A), ('2. İndis Farkı', 'a₂₀ = a₁₂ + (20 - 12)·d', MOR, MOR_A), ('3. Sonuç', 'a₂₀ = 35 + 8·3 = 59', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('Rasyonel genel terimli dizide tam sayı terimler', 'TAM SAYI TERİMLER · a_n = (4n + 30) / n = 4 + (30 / n)', 'n ∈ ℤ⁺ sayısı 30 sayısının pozitif tam bölenleri olmalıdır: {1, 2, 3, 5, 6, 10, 15, 30}', '30 sayısının 8 tane pozitif tam böleni olduğundan 8 terimi tam sayıdır.', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('Dizi özellikleri ve işaret incelemesi', [('a_n = 5n - 2', 'Ortak fark d = 5', YES, YES_A), ('Orta Terim', '(a₄ + a₁₂)/2 = a₈', MAVI, MAVI_A), ('Toplamdan Terim', 'a₇ = S₇ - S₆', MOR, MOR_A), ('(n-7)/(n+2) < 0', 'n ∈ {1..6} → 6 terim', TUR, TUR_A)])

def g5():
    return akis4('İndirgemeli dizide taraf tarafa toplama', [('1. Değer Yaz', 'n = 1, 2, ..., 9', MAVI, MAVI_A), ('2. Topla', 'Ara terimler gider', CAM, CAM_A), ('3. Eşitle', 'a₁₀ - a₁ = 9·5 = 45', MOR, MOR_A), ('4. Sonuç', 'a₁₀ = 4 + 45 = 49', YES, YES_A)])

def g6():
    return pano('Kuadratik dizinin en küçük terimi', 'EN KÜÇÜK TERİM · a_n = n² - 9n + 14 (n ∈ ℤ⁺)', 'Parabol tepe noktası apsisi: r = -b / (2a) = 9 / 2 = 4,5 → En yakın tam sayılar n = 4 veya 5', 'n = 4 için a₄ = 4² - 9·4 + 14 = 16 - 36 + 14 = -6 (En küçük terim).', MOR, MOR_A, '#f5f0ff')

def g7():
    return uclu('İndirgemeli, aritmetik ve sabit dizi', 'DİZİ TÜRLERİ VE ORTALAMA ÖZELLİĞİ', ('İndirgemeli Dizi', 'Önceki terime bağlı', TUR, TUR_A), ('Aritmetik Ortalama', 'a_n = (a_(n-k)+a_(n+k))/2', MAVI, MAVI_A), ('Sabit Dizi (d = 0)', 'Tüm terimler eşit', YES, YES_A), YES, YES_A)

def g8():
    return kart4('Aritmetik dizi bağıntı özetleri', [('Ortak Fark', '(a_n - a_p) / (n - p)', MAVI, MAVI_A), ('İndis Toplamı', 'k+m=p+r ⇒ a_k+a_m=a_p+a_r', MOR, MOR_A), ('k Terim Ekleme', 'd = (y - x) / (k + 1)', TUR, TUR_A), ('Orta Terim', 'a_n = (a_(n-k)+a_(n+k))/2', YES, YES_A)])

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
