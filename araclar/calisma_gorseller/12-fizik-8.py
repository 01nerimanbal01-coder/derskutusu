"""12. sınıf Fizik 8. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return kart4('Kepler kanunları ve Zîc-i Uluğ Bey', [('1. Yörüngeler', 'Elips ve Güneş odakta', TUR, TUR_A), ('2. Alanlar', 'Eşit sürede eşit alan', YES, YES_A), ('3. Periyotlar', 'R³ / T² = Sabit', MOR, MOR_A), ('Zîc-i Uluğ Bey', 'Semerkant kataloğu', MAVI, MAVI_A)])

def g1():
    return uclu('Periyotlar kanunu yarıçap ve periyot hesabı', 'KEPLER 3. KANUNU · R_K / R_L = 1 / 4 İSE T_K / T_L ORANI', ('Yarıçap Oranı', 'R_K / R_L = 1 / 4', MAVI, MAVI_A), ('Küp - Kare Bağıntısı', '(T_K/T_L)² = (1/4)³ = 1/64', MOR, MOR_A), ('Periyot Oranı', 'T_K / T_L = 1 / 8', YES, YES_A), MOR, MOR_A)

def g2():
    return pano('Gezegen hareketinde açısal momentumun korunumu', 'ELİPTİK YÖRÜNGEDE NET TORK VE AÇISAL MOMENTUM', 'Kütle çekim kuvveti dönme merkezi (Güneş) üzerinden geçer → Net Tork = 0', 'Dış tork sıfır olduğundan L = m · v · r açısal momentumu daima korunur.', YES, YES_A, '#eaf8f0')

def g3():
    return kart4('Evren modelleri ve gezegen enerjisi', [('Batlamyus', 'Yer merkezli model', TUR, TUR_A), ('Uzaklaşırken', 'I = m·r² artar', MAVI, MAVI_A), ('Yarıçap Artarsa', 'Periyot (T) artar', MOR, MOR_A), ('Günberi Konumu', 'Kinetik enerji max', KIR, KIR_A)])

def g5():
    return akis4('Gök bilimi tarihsel gelişim sırası', [('1. Batlamyus', 'Yer merkezli model', TUR, TUR_A), ('2. Uluğ Bey', 'Semerkant Zîc\'i', CAM, CAM_A), ('3. Kopernik', 'Güneş merkezli', MAVI, MAVI_A), ('4. Kepler', 'Elips yörünge yasası', MOR, MOR_A)])

def g6():
    return pano('Kepler Alanlar Kanunu süre hesabı', 'ALANLAR KANUNU · TOPLAM ALAN = 6S · PERİYOT T = 12 AY', 'Yarıçap vektörü eşit zaman aralıklarında eşit alanlar tarar (A₁ / A₂ = t₁ / t₂)', '6S alan 12 ayda taranırsa → 2S taralı alan (2/6) × 12 = 4 ayda taranır.', MAVI, MAVI_A, '#f4f8fe')

def g7():
    return uclu('Güneş merkezli model, hız ve gözlem', 'ASTRONOMİ ÖNCÜLERİ VE YÖRÜNGE DİNAMİĞİ', ('Kopernik', 'Heliosentrik model', MAVI, MAVI_A), ('Kinetik Enerji', 'Günberide maksimum', KIR, KIR_A), ('Tycho Brahe', 'Hassas gözlem verisi', TUR, TUR_A), TUR, TUR_A)

def g8():
    return kart4('Kepler kanunları matematiksel bağıntıları', [('Ortalama R', '(r_min + r_max) / 2', MAVI, MAVI_A), ('Periyotlar', 'R₁³/T₁² = R₂³/T₂²', MOR, MOR_A), ('Alanlar Oranı', 'A₁ / A₂ = t₁ / t₂', YES, YES_A), ('Korunum', 'L = m·v·r = sabit', TUR, TUR_A)])

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
