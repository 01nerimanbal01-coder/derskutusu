"""12. sınıf Fizik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}"/>'

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
    return kart4('Kütle çekim enerjisi bağıntıları', [('Potansiyel (Ep)', '-G·M·m / d', MAVI, MAVI_A), ('Kurtulma (Ekurt)', '+G·M·m / R', YES, YES_A), ('Toplam (Et)', '-G·M·m / (2r)', KIR, KIR_A), ('Bağlanma (Ebağ)', '+G·M·m / (2r)', MOR, MOR_A)])

def g1():
    return uclu('Yörünge yarıçapı artışının enerjilere etkisi', 'UYDU YÖRÜNGESİ: r → 2r ÇIKARILDIĞINDA ENERJİ DEĞİŞİMİ', ('Potansiyel ve Toplam', 'Sıfıra yaklaşır, ARTAR', YES, YES_A), ('Kinetik Enerji (Ek)', 'Hız düşer, AZALIR', KIR, KIR_A), ('Bağlanma Enerjisi', 'Koparmak kolay, AZALIR', MOR, MOR_A), MAVI, MAVI_A)

def g2():
    return pano('Kurtulma enerjisi ve kurtulma hızı karşılaştırması', 'KURTULMA ENERJİSİ VE KURTULMA HIZI İLİŞKİSİ', 'E(kurtulma) = +G·M·m / R (Cismin m kütlesiyle doğru orantılıdır)', '__F12_1__', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('Çekim potansiyel ve kurtulma özellikleri', [('Sonsuzda Ep', 'd → ∞ iken Ep = 0', MAVI, MAVI_A), ('Kurtulma Hızı', 'Kütleye (m) bağlı değil', YES, YES_A), ('Kinetik Enerji', '+G·M·m / (2r)', TUR, TUR_A), ('Güneş', 'En yüksek kurtulma hızı', MOR, MOR_A)])

def g5():
    return akis4('Gök cisimlerinin kurtulma hızı sıralaması', [('1. Ay', 'En düşük (~8.280 km/h)', CAM, CAM_A), ('2. Mars', 'Küçük kütleli gezegen', YES, YES_A), ('3. Jüpiter', 'En büyük gezegen', TUR, TUR_A), ('4. Güneş', 'En yüksek (~2,2M km/h)', MOR, MOR_A)])

def g6():
    return pano('İki uydunun kütle çekim potansiyel enerjisi oranı', 'YÖRÜNGE KARŞILAŞTIRMASI: X VE Y UYDULARI', 'X Uydusu: Kütle = 9m, Yörünge Yarıçapı = 3d → Ep(X) = -3·G·Mm/d', 'Y Uydusu: Kütle = 12m, Yörünge Yarıçapı = 4d → Ep(Y) = -3·G·Mm/d', MOR, MOR_A, '#f5f0ff')

def g7():
    return pano('Kurtulma, bağlanma ve bağlı sistem kavramları', 'ÇEKİM ALANINDAN KURTULMA VE BAĞLANMA ENERJİSİ', 'Yüzeyden Sonsuza: Kurtulma Enerjisi · Yörüngeden Sonsuza: Bağlanma Enerjisi', 'Negatif (-) toplam enerji, uydunun gezegene kütle çekimiyle bağlı olduğunu gösterir.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Yörünge yarıçapı r arttıkça değişimler', [('Hız ve Ek', '__F12_2__', KIR, KIR_A), ('Potansiyel (Ep)', 'Artar (0’a yaklaşır)', YES, YES_A), ('Toplam (Et)', 'Artar (Üst yörünge)', MAVI, MAVI_A), ('Bağlanma (Ebağ)', 'Azalır (Kolay kopar)', MOR, MOR_A)])

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

_eski_uygula = uygula
def _temizle12(svg_s):
    svg_s = svg_s.replace('<text x="180.0" y="82.0" text-anchor="middle" font-size="8.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">__F12_1__</text>', '<text x="88.0" y="82.0" text-anchor="end" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">v(kurtulma) = </text><path d="M 88.8 78.9 L 90.1 78.9 L 91.5 82.6 L 93.8 74.1 L 138.8 74.1" fill="none" stroke="#5b6479" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="116.3" y="82.0" text-anchor="middle" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">2·G·M / R</text><text x="139.3" y="82.0" text-anchor="start" font-size="8.2" font-family="Noto Sans, sans-serif" font-weight="400" fill="#5b6479">  (m kütlesine bağlı DEĞİLDİR!)</text>')
    svg_s = svg_s.replace('<text x="50.0" y="72.0" text-anchor="middle" font-size="8.0" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">__F12_2__</text>', '<text x="58.0" y="72.0" text-anchor="end" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">Azalır: v ∝ 1/</text><path d="M 58.8 69.1 L 60.1 69.1 L 61.5 72.6 L 63.8 64.7 L 70.4 64.7" fill="none" stroke="#0b2257" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/><text x="67.1" y="72.0" text-anchor="middle" font-size="7.6" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">r</text>')
    return svg_s

def uygula(o):
    _eski_uygula(o)
    for q in o['sorular']:
        if q.get('gorsel'):
            q['gorsel'] = _temizle12(q['gorsel'])
