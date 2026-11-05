"""11. sınıf Matematik 8. hafta görselleri (SVG; insan figürü yok K024; beyaz bant yok K178; 24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket):
    stil = ' style="width:100%;max-height:24mm;display:block;margin:1mm auto;"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+81},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def uclu(baslik, k1, a1, k2, a2, k3, a3, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 22, baslik, 10.0, c)
    for i, (k, a, rk, dk) in enumerate([(k1, a1, MAVI, MAVI_A), (k2, a2, TUR, TUR_A), (k3, a3, YES, YES_A)]):
        x = 12 + i * 114
        ic += kutu(x, 32, 108, 70, dk, rk) + yazi(x + 54, 54, k, 9.2, rk) + yazi(x + 54, 78, a, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.2, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def g0():
    return cizelge4([('Eşkenar Dörtgen', '4 eşit kenar · e ⊥ f', MAVI, MAVI_A), ('Dikdörtgen', 'Açılar 90° · e = f', TUR, TUR_A), ('Kare', 'Düzgün · e=f ve e⊥f', YES, YES_A), ('Deltoid', 'Komşu kenarlar eşit', MOR, MOR_A)], 'Özel dörtgenlerin temel özellikleri')
def g1():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 20, 'EŞKENAR DÖRTGENDE KÖŞEGEN DİK ÜÇGENİ (6-8-10)', 9.8, MAVI)
    ic += f'<polygon points="95,28 165,64 95,100 25,64" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<line x1="25" y1="64" x2="165" y2="64" stroke="{TUR}" stroke-width="1.3"/>'
    ic += f'<line x1="95" y1="28" x2="95" y2="100" stroke="{YES}" stroke-width="1.3"/>'
    ic += yazi(125, 58, '8', 9.0, TUR) + yazi(86, 48, '6', 9.0, YES) + yazi(138, 42, 'a=10', 9.2, MAVI)
    ic += kutu(185, 30, 158, 70, YES_A, YES)
    ic += yazi(264, 52, 'Çevre = 4 · 10 = 40 cm', 9.2, YES)
    ic += yazi(264, 78, 'Alan = (16 · 12) / 2 = 96 cm^2', 9.2, LAC, ince=True)
    return svg(360, 115, ic, 'Eşkenar dörtgen köşegen ve alan hesabı')
def g2():
    return ikili('KÖŞEGEN DİKLİĞİ VE ALAN BAĞINTISI', 'Eşkenar Dörtgen · Kare · Deltoid', 'Köşegenler dik (e ⊥ f) -> Alan = e·f / 2', 'Dikdörtgen ve Paralelkenar', 'Köşegenler eşit/ortalanır -> Alan = a·h', YES, YES_A, MAVI, MAVI_A, 'Köşegen dikliği ve alan formülleri')
def g3():
    return uclu('ÖZEL DÖRTGENLERDE AÇI VE ORTA NOKTA', 'Açıortay Köşegen', 'Eşkenar dörtgen ve kare', 'Deltoid Simetrisi', 'Tek köşegen açıortaydır', 'Orta Nokta Dörtgeni', 'Daima paralelkenar olur', MOR, MOR_A, 'Açıortay köşegen ve orta nokta dörtgeni')
def g6():
    return akis4([('1. Dörtgen', 'Genel 4 kenarlı', GRI, GRI_A), ('2. Paralelkenar', 'Karşılıklı paralel', MAVI, MAVI_A), ('3. Dikdörtgen', 'Eşkenar Dörtgen', TUR, TUR_A), ('4. Kare', 'En özel kesişim', YES, YES_A)], 'Özel dörtgenler kapsama hiyerarşisi')
def g7():
    return kart('DELTOİDDE İÇ AÇILAR ÖZELLİĞİ (|AB|=|AD|, |BC|=|CD|)', 'Simetri ekseni olmayan köşegenin uçlarındaki açılar eşittir: m(B) = m(D)', '70° + 50° + 2·m(B) = 360°  =>  2·m(B) = 240°  =>  m(B) = m(D) = 120°', TUR, TUR_A, 'Deltoidde açı hesabı')
def g8():
    return ikili('EŞKENAR DÖRTGEN İLE DELTOİD FARKI', 'Eşkenar Dörtgen', '4 kenar eşit · 2 köşegen ortalanır', 'Deltoid', 'Komşu 2şer kenar eşit · 1 köşegen ortalanır', MAVI, MAVI_A, MOR, MOR_A, 'Eşkenar dörtgen ve deltoid karşılaştırması')
def g9():
    return ikili('DİKDÖRTGENDE PİSAGOR VE ALAN (a=5 cm, b=12 cm)', 'Köşegen Uzunluğu (5-12-13)', 'e^2 = 5^2 + 12^2  =>  e = 13 cm', 'Dikdörtgenin Alanı', 'Alan = a · b = 5 · 12 = 60 cm^2', CAM, CAM_A, YES, YES_A, 'Dikdörtgen köşegen ve alan hesabı')

def uygula(o):
    s = o['sorular']
    for idx, fn in [(0, g0), (1, g1), (2, g2), (3, g3), (6, g6), (7, g7), (8, g8), (9, g9)]:
        s[idx]['gorsel'] = fn()
