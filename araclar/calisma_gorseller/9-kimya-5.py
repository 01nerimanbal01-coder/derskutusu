"""9. sınıf kimya 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ogeler = [('s (l = 0)', '1 kutu · Maks 2 e⁻', MAVI, MAVI_A), ('p (l = 1)', '3 kutu · Maks 6 e⁻', YES, YES_A), ('d (l = 2)', '5 kutu · Maks 10 e⁻', TUR, TUR_A), ('f (l = 3)', '7 kutu · Maks 14 e⁻', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Orbital türleri ve elektron kapasiteleri', 34)

def g1():
    b, s1, s2 = ('MADELUNG-KLETCHKOWSKI (n + l) BAĞIL ENERJİ KURALI', '4s (4+0 = 4)  <  3d (3+2 = 5, n=3)  <  4p (4+1 = 5, n=4)', '(n+l) büyüdükçe enerji artar; (n+l) eşitse n sayısı büyük olanın enerjisi büyüktür.')
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, b, 10, MAVI)
    ic += kutu(16, 36, 328, 64, '#f4f8fe', MAVI) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Madelung-Kletchkowski (n+l) bağıl enerji kuralı', 34)

def g2():
    b, s1, s2 = ('ENERJİ DÜZEYLERİNDE ORBİTAL (n²) VE ELEKTRON (2n²)HESABI', 'K (n=1): 1 orb, 2 e⁻ | L (n=2): 4 orb, 8 e⁻ | M (n=3): 9 orb, 18 e⁻', '3. katmanda (M) 3s (1), 3p (3) ve 3d (5) olmak üzere toplam 9 orbital bulunur.')
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, b, 10, TUR) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Katmanlarda orbital ve elektron sayısı formülü', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('1. Katman (K)', 'Yalnız 1s vardır', MAVI, MAVI_A), ('2. Katman (L)', '2s ve 2p vardır', TUR, TUR_A), ('Eş Enerji', '2px = 2py = 2pz', YES, YES_A), ('Kapasite', '1 kutuda maks 2 e⁻', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Atom orbitallerinin temel kuralları', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. 2s (n+l=2)', 'Küresel alt kabuk', YES, YES_A), ('2. 2p (n+l=3)', '3 eş orbital', MAVI, MAVI_A), ('3. 3p (n+l=4)', 'M katmanı p', TUR, TUR_A), ('4. 3d (n+l=5)', '4s\'den sonra dolar', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Aufbau bağıl enerji dizilimi akışı', 34)

def g6():
    b, s1, s2 = ('BOHR YÖRÜNGESİ İLE MODERN ATOM ORBİTALİ FARKI', 'Yörünge: 2 boyutlu dairesel çizgi  |  Orbital: 3 boyutlu olasılık bulutu', 'Heisenberg Belirsizlik İlkesi gereği elektronun yeri ve hızı aynı anda kesin bilinemez.')
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, b, 10, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, s1, 9.8, LAC) + yazi(180, 84, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Bohr yörüngesi ve modern orbital karşılaştırması', 34)

def g7():
    b, s1, s2 = ('ORBİTAL GEOMETRİSİ VE KUTU DİYAGRAMI GÖSTERİMİ', 's: Küresel (n ≥ 1)  ·  p: Çift loblu (n ≥ 2)  ·  d: n ≥ 3  ·  f: n ≥ 4', 'Boş orbital: ( )   |   Yarı dolu orbital: (↑)   |   Tam dolu orbital: (↑↓)')
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, b, 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Orbital şekilleri ve doluluk türleri', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('Baş Kuantum (n)', 'Katman ve uzaklık', MAVI, MAVI_A), ('Açısal (l)', 'Orbital türü (0..3)', TUR, TUR_A), ('Dejener', 'Aynı alt kabuk eş E', YES, YES_A), ('Pauli İlkesi', 'Zıt spinli 2 e⁻', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Kuantum sayıları ve Pauli ilkesi', 34)

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
