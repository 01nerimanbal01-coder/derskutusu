"""10. sınıf Fizik 3. hafta (Bir Boyutta Sabit İvmeli Hareket: İvme ve Hız Değişimi İlişkisi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('v-t Eğimi', 'İvmeyi (a = Δv/Δt) verir', MAVI, MAVI_A),
        ('v-t Alanı', 'Yer değiştirmeyi (Δx) verir', YES, YES_A),
        ('Pozitif İvme', 'Hız vektörü yönünde artış', TUR, TUR_A),
        ('Negatif İvme', 'Ters yönde yavaşlama / hızlanma', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Hız-zaman grafiği eğim ve alan ilkeleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'DÜZGÜN HIZLANAN HAREKET VE İVME HESABI', 11, MAVI)
    # Hareket rayı
    ic += '<line x1="24" y1="56" x2="336" y2="56" stroke="#2451d6" stroke-width="2"/>'
    ic += '<circle cx="50" cy="56" r="10" fill="#ee7d12" stroke="#0b2257" stroke-width="1.2"/>'
    ic += yazi(50, 38, 't = 0 (v₀ = 0)', 8.5, TUR)
    ic += '<circle cx="280" cy="56" r="10" fill="#12a150" stroke="#0b2257" stroke-width="1.2"/>'
    ic += yazi(280, 38, 't = 4 s (v = 20 m/s)', 8.5, YES)
    ic += yazi(165, 48, 'a = (20 - 0) / 4 = 5 m/s²', 10, MAVI)
    ic += yazi(165, 78, 'Δx = 1/2 · a · t² = 1/2 · 5 · 16 = 40 m', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Düzgün hızlanan hareket ivme ve alınan yol hesabı', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'HIZ-ZAMAN (v-t) GRAFİĞİNDE ALAN = YER DEĞİŞTİRME', 10.5, YES)
    # Koordinat ekseni
    ic += '<line x1="60" y1="84" x2="300" y2="84" stroke="#9aa6bd" stroke-width="1.2"/>'
    ic += '<line x1="60" y1="84" x2="60" y2="34" stroke="#9aa6bd" stroke-width="1.2"/>'
    # Doğru
    ic += '<line x1="60" y1="84" x2="240" y2="40" stroke="#12a150" stroke-width="2.2"/>'
    # Üçgen tarama
    ic += '<polygon points="60,84 240,84 240,40" fill="#c8e6c9" fill-opacity="0.6"/>'
    ic += yazi(44, 42, '20', 9, LAC)
    ic += yazi(240, 94, 't = 4 s', 9, LAC)
    ic += yazi(160, 68, 'Alan = (20 · 4)/2 = 40 m', 9.5, YES)
    return svg(360, 100, ic, 'Hız-zaman grafiği altındaki alan ile yer değiştirme hesabı', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'DÜZGÜN YAVAŞLAYAN HAREKET VE FRENLEME', 11, TUR)
    # Yol ve araba
    ic += '<line x1="24" y1="56" x2="336" y2="56" stroke="#ee7d12" stroke-width="2"/>'
    ic += '<circle cx="60" cy="56" r="10" fill="#d63a3a" stroke="#0b2257" stroke-width="1.2"/>'
    ic += yazi(60, 38, 'v₁ = 30 m/s', 8.5, KIR)
    ic += '<circle cx="280" cy="56" r="10" fill="#9aa6bd" stroke="#0b2257" stroke-width="1.2"/>'
    ic += yazi(280, 38, 'v₂ = 0 (Durdu)', 8.5, SOLUK)
    ic += yazi(170, 48, 'Fren İvmesi: a = -6 m/s²', 9.5, TUR)
    ic += yazi(170, 78, 'Duruş Süresi: t = 30 / 6 = 5 s', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Düzgün yavaşlayan hareket fren mesafesi ve duruş süresi', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'İVME-ZAMAN GRAFİĞİNDEN HIZ DEĞİŞİMİNE GEÇİŞ', 10.5, MOR)
    # a-t grafiği dikdörtgen alan
    ic += '<line x1="60" y1="84" x2="280" y2="84" stroke="#9aa6bd" stroke-width="1.2"/>'
    ic += '<line x1="60" y1="84" x2="60" y2="34" stroke="#9aa6bd" stroke-width="1.2"/>'
    ic += '<rect x="60" y="44" width="160" height="40" fill="#f0e9fe" stroke="#7c3aed" stroke-width="1.5"/>'
    ic += yazi(44, 54, 'a = 4', 9, MOR)
    ic += yazi(220, 94, 't = 5 s', 9, LAC)
    ic += yazi(140, 64, 'Alan = a · t = 4 · 5 = 20 m/s (Δv)', 9.5, MOR)
    return svg(360, 100, ic, 'İvme-zaman grafiği altındaki dikdörtgen alan ile hız değişimi', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'HIZLANAN VE YAVAŞLAYAN HAREKET GRAFİKLERİ', 10.5, LAC)
    # Sol: Hızlanan
    ic += kutu(16, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(94, 50, 'Hızlanan Hareket (v · a > 0)', 9, YES)
    ic += yazi(94, 70, 'Hız ve ivme vektörleri aynı yönlüdür', 7.5, LAC, ince=True)
    # Sağ: Yavaşlayan
    ic += kutu(188, 34, 156, 54, '#ffffff', KIR, 6, 1.2)
    ic += yazi(266, 50, 'Yavaşlayan Hareket (v · a < 0)', 9, KIR)
    ic += yazi(266, 70, 'Hız ve ivme vektörleri zıt yönlüdür', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Hızlanan ve yavaşlayan hareket vektör işaretleri karşılaştırması', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    birimler = [
        ('Konum (x)', 'Metre (m)', MAVI),
        ('Zaman (t)', 'Saniye (s)', TUR),
        ('Hız (v)', 'Metre/saniye (m/s)', YES),
        ('İvme (a)', 'Metre/saniye² (m/s²)', MOR)
    ]
    for i, (b, d, c) in enumerate(birimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Mekanik temel büyüklükler ve SI birimleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: İ - V - M - E', 11.5, YES)
    harfler = [('1', 'İ'), ('2', 'V'), ('3', 'M'), ('4', 'E')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Fizik dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
