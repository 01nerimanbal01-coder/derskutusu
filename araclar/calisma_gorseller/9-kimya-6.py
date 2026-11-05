"""9. sınıf Kimya 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def dörtlu_kart(etiket, kartlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis_karti(etiket, adimlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def uclu_pano(etiket, ust_baslik, kutular, ana_renk=MAVI, ana_acik=MAVI_A):
    ic = kutu(4, 4, 352, 107, ana_acik, ana_renk) + yazi(180, 23, ust_baslik, 10, ana_renk)
    for i, (b, alt, c, d) in enumerate(kutular):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 66, d, c) + yazi(x + 52, 55, b, 9.5, c) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def bilgi_panosu(etiket, baslik, satir1, satir2, c=CAM, d=CAM_A, ic_d='#eaf7fa'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 25, baslik, 10, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, satir1, 9.6, LAC) + yazi(180, 82, satir2, 8.6, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return dörtlu_kart('Elektron dizilimi temel ilkeleri', [
        ('Aufbau Kuralı', 'Düşük enerjiden başla', MAVI, MAVI_A),
        ('Pauli İlkesi', 'En çok 2 e⁻, zıt spin (↑↓)', TUR, TUR_A),
        ('Hund Kuralı', 'Önce tek tek aynı yön (↑↑↑)', YES, YES_A),
        ('İzoelektronik', 'Aynı e⁻ sayısı ve dizilimi', MOR, MOR_A)
    ])

def g1():
    return uclu_pano('Kükürt ve p bloğu orbital dağılımı', 'TEMEL HÂL ELEKTRON DİZİLİMİ · TAM VE YARI DOLU ORBİTALLER', [
        ('₇N (1s² 2s² 2p³)', '2 tam dolu · 3 yarı dolu', MAVI, '#f4f8fe'),
        ('₈O (1s² 2s² 2p⁴)', '3 tam dolu · 2 yarı dolu', YES, YES_A),
        ('₁₆S (...3s² 3p⁴)', '7 tam dolu · 2 yarı dolu', TUR, TUR_A)
    ], MAVI, MAVI_A)

def g2():
    return bilgi_panosu('Fosfor atomu orbital şeması', '₁₅P ATOMUNUN TEMEL HÂL DİZİLİMİ VE HUND KURALI',
        '₁₅P : 1s² (↑↓)  2s² (↑↓)  2p⁶ (↑↓)(↑↓)(↑↓)  3s² (↑↓)  3p³ (↑)(↑)(↑)',
        '1s(1) + 2s(1) + 2p(3) + 3s(1) = 6 tam dolu orbital  |  3p³ = 3 yarı dolu orbital', CAM, CAM_A)

def g3():
    return dörtlu_kart('Alt kabuklar ve enerji kuralları', [
        ('s ve p Kabuğu', 's: 1 orb (2e⁻) · p: 3 (6e⁻)', MAVI, MAVI_A),
        ('d ve f Kabuğu', 'd: 5 (10e⁻) · f: 7 (14e⁻)', YES, YES_A),
        ('Bağıl Enerji', '3p < 4s < 3d < 4p', TUR, TUR_A),
        ('Katman (2n²)', 'n=1: 2 · n=2: 8 · n=3: 18', MOR, MOR_A)
    ])

def g5():
    return akis_karti('Aufbau orbital dolum sırası', [
        ('1. Katman', '1s² (2 e⁻)', MAVI, MAVI_A),
        ('2. Katman', '2s² 2p⁶ (8 e⁻)', YES, YES_A),
        ('3. Katman', '3s² 3p⁶ (8 e⁻)', TUR, TUR_A),
        ('4s → 3d Geçişi', '4s² → 3d¹⁰ → 4p⁶', MOR, MOR_A)
    ])

def g6():
    return uclu_pano('Küresel simetri özel durumları', 'KÜRESEL SİMETRİ · KROM (₂₄Cr) VE BAKIR (₂₉Cu) ÖZEL DURUMU', [
        ('₂₄Cr (Temel Hâl)', '[Ar] 4s¹ 3d⁵ (6 yarı dolu)', TUR, TUR_A),
        ('₂₉Cu (Temel Hâl)', '[Ar] 4s¹ 3d¹⁰ (Tam dolu d)', YES, YES_A),
        ('Kararlılık', 'Uyarılmış değil, temel hâl!', MAVI, '#f4f8fe')
    ], TUR, TUR_A)

def g7():
    return bilgi_panosu('Orbital kapasitesi ve küresel simetri', 'ORBİTAL · ALT KABUK KAPASİTESİ · KÜRESEL SİMETRİ',
        's¹ / s²  ·  p³ / p⁶  ·  d⁵ / d¹⁰ ile biten atomlar küresel simetri gösterir',
        'Her bir orbital zıt spinli en fazla 2 elektron alır; d alt kabuğu 10 elektron alır.', YES, YES_A, '#eaf8f0')

def g8():
    return dörtlu_kart('İyon dizilimleri ve elektron koparma', [
        ('₁₁Na⁺ ve ₉F⁻', '1s² 2s² 2p⁶ (10 e⁻)', MAVI, MAVI_A),
        ('₂₄Cr Atomu', '... 3p⁶ 4s¹ 3d⁵', TUR, TUR_A),
        ('₂₁Sc Atomu', '... 3p⁶ 4s² 3d¹', YES, YES_A),
        ('₂₂Ti²⁺ İyonu', 'Önce 4s² kopar → ...3d²', MOR, MOR_A)
    ])

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
