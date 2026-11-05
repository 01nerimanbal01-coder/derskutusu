"""9. sınıf Kimya 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('Özel atom ve iyon dizilimleri', [
        ('₈O (Nötr)', '1s² 2s² 2p⁴', MAVI, MAVI_A),
        ('₂₄Cr (Özel)', '[Ar] 4s¹ 3d⁵', YES, YES_A),
        ('₂₉Cu (Özel)', '[Ar] 4s¹ 3d¹⁰', TUR, TUR_A),
        ('₂₂Ti²⁺ (Katyon)', '[Ar] 3d² (4s kopar)', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Küresel simetri kararlılığı', 'KÜRESEL SİMETRİ: YARI DOLU VE TAM DOLU ORBİTALLER', [
        ('Yarı Dolu Kararlılık', 's¹, p³, d⁵, f⁷', MAVI, '#f4f8fe'),
        ('Tam Dolu Kararlılık', 's², p⁶, d¹⁰, f¹⁴', YES, YES_A),
        ('₂₄Cr ve ₂₉Cu', '4s¹ 3d⁵ ve 4s¹ 3d¹⁰', TUR, TUR_A)
    ], YES, YES_A)
def g2():
    return bilgi_panosu('Geçiş metallerinde katyon dizilimi ve izoelektroniklik', 'ALTIN KURAL: Z > 20 KATYONLARDA ÖNCE 4s ELEKTRONU KOPAR!',
        '₂₀Ca (20 e⁻): [Ar] 4s²  ·  ₂₁Sc⁺ (20 e⁻): [Ar] 4s¹ 3d¹ (4s’den 1 elektron kopmuştur)',
        'Elektron sayıları eşit (20) olsa da dizilimleri farklı olduğu için Ca ve Sc⁺ izoelektronik değildir!', CAM, CAM_A)
def g3():
    return dörtlu_kart('Üç temel dizilim ilkesi', [
        ('Aufbau İlkesi', 'Düşük enerjiden başla', MAVI, MAVI_A),
        ('Pauli İlkesi', 'En çok 2 zıt e⁻ (↑↓)', YES, YES_A),
        ('Hund Kuralı', 'Önce tek tek aynı yön', TUR, TUR_A),
        ('n + ℓ Kuralı', '4s enerjisi < 3d', MOR, MOR_A)
    ])
def g5():
    return akis_karti('Aufbau orbital dolma sırası', [
        ('1. 1s² → 2s²', 'İlk 4 elektron', MAVI, MAVI_A),
        ('2. 2p⁶ → 3s²', '5 - 12. elektronlar', YES, YES_A),
        ('3. 3p⁶ → 4s²', '13 - 20. elektronlar', TUR, TUR_A),
        ('4. 3d¹⁰ → 4p⁶', '21 - 36. elektronlar', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('Demir (₂₆Fe) ve iyonlarının dizilimi', 'GEÇİŞ METALLERİNDE ELEKTRON KOPARMA SIRASI', [
        ('Nötr ₂₆Fe (26 e⁻)', '[₁₈Ar] 4s² 3d⁶', MAVI, '#f4f8fe'),
        ('₂₆Fe²⁺ Katyonu', '[₁₈Ar] 3d⁶ (4s² kopar)', YES, YES_A),
        ('₂₆Fe³⁺ Katyonu', '[₁₈Ar] 3d⁵ (Küresel!)', TUR, TUR_A)
    ], MAVI, MAVI_A)
def g7():
    return bilgi_panosu('Temel hâl ve uyarılmış hâl farkı', 'TEMEL HÂL (KARARLI)  ile  UYARILMIŞ HÂL (KARARSIZ) AYRIMI',
        'Alt enerjili orbital dolmadan elektron dışarıdan enerji alıp üst orbitale çıkarsa atom UYARILMIŞ olur',
        '₂₄Cr ([Ar] 4s¹ 3d⁵) ve ₂₉Cu ([Ar] 4s¹ 3d¹⁰) dizilimleri kendiliğinden olduğu için TEMEL HÂLDİR!', TUR, TUR_A, '#fff6ea')
def g8():
    return dörtlu_kart('Temel kavramlar özeti', [
        ('Küresel Simetri', 'Eşit yük dağılımı', YES, YES_A),
        ('Temel Hâl', 'En düşük enerjili hâl', MAVI, MAVI_A),
        ('Değerlik e⁻', 'Kimyasal bağı belirler', TUR, TUR_A),
        ('İzoelektronik', 'Aynı dizilim, farklı Z', MOR, MOR_A)
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
