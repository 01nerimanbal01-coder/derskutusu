"""9. sınıf Fizik 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    temel = [('Kütle (m)', 'kg · Terazi', MAVI, MAVI_A), ('Işık Şiddeti (I)', 'cd · Fotometre', YES, YES_A), ('Sıcaklık (T)', 'K · Termometre', TUR, TUR_A), ('Akım (i)', 'A · Ampermetre', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(temel):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Temel nicelikler, SI birimleri ve ölçüm araçları', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'SI BİRİM SİSTEMİNDE 7 TEMEL NİCELİK (KİSAMUZ)', 10.5, MAVI)
    ic += kutu(16, 36, 328, 64, '#f4f8fe', MAVI) + yazi(180, 58, 'Kütle (kg) · Işık (cd) · Sıcaklık (K) · Akım (A) · Madde (mol) · Uzunluk (m) · Zaman (s)', 9, LAC) + yazi(180, 82, 'Dikkat: SI sıcaklık birimi °C değil Kelvin (K); kütle birimi g değil kilogramdır (kg)!', 8.5, KIR)
    return svg(360, 115, ic, 'KISAMUZ 7 temel nicelik ve SI birimleri panosu', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'TÜRETİLMİŞ BİRİMLERİN TEMEL BİRİMLERLE İFADESİ', 10.5, TUR)
    ic += yazi(180, 58, 'Kuvvet (F = m·a): 1 N = kg·m/s²   |   Enerji (W = F·x): 1 J = kg·m²/s²', 10, LAC)
    ic += yazi(180, 82, 'Türetilmiş nicelikler birden fazla temel niceliğin çarpım veya bölümüyle kurulur.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Newton ve Joule birim türetme bağıntıları', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    gruplar = [('Temel-Skaler', '7 KİSAMUZ niceliği', MAVI, MAVI_A), ('Temel-Vektörel', 'YOKTUR (Boş küme)', KIR, KIR_A), ('Türetilmiş-Skaler', 'Sürat, Enerji, Basınç', YES, YES_A), ('Türetilmiş-Vektörel', 'Kuvvet, Hız, İvme', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(gruplar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.2, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Temel-türetilmiş ve skaler-vektörel çapraz tablo', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Temel', 'm, kg ve s ölç', YES, YES_A), ('2. Hız/İvme', 'm/s ve m/s² türet', MAVI, MAVI_A), ('3. Kuvvet (N)', 'F = m·a (kg·m/s²)', TUR, TUR_A), ('4. Güç (W)', 'P = W/t (kg·m²/s³)', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 10, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Temel birimlerden türetilmiş birimlere geçiş akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'GÜNLÜK BİRİMLERİN SI BİRİMLERİNE DÖNÜŞÜMÜ', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'T(K) = t(°C) + 273   |   1 km/h = (1000 m) / (3600 s) = (1 / 3,6) m/s', 10, LAC) + yazi(180, 84, 'Örnek: 27 °C = 300 K  ve  72 km/h = 72 / 3,6 = 20 m/s olarak hesaplanır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'SI birim dönüşümü hesaplama kartı', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'BASINÇ, ÖZ KÜTLE VE ISI BİRİMLERİ', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Basınç (P = F/A): Pascal (Pa)  ·  Öz Kütle (d = m/V): kg/m³  ·  Isı (Q): Joule (J)', 9.5, LAC) + yazi(180, 82, 'Kalori, litre ve atmosfer günlük birimlerdir; SI standart birimi değildir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Basınç, öz kütle ve ısı SI birimleri şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    turetilmis = [('İvme (a)', 'm / s²', MAVI, MAVI_A), ('Elektrik Yükü', 'Coulomb (A · s)', TUR, TUR_A), ('Güç (P)', 'Watt (J / s)', YES, YES_A), ('Hacim (V)', 'Metreküp (m³)', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(turetilmis):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Türetilmiş nicelikler ve SI birimleri kartı', 34)

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
