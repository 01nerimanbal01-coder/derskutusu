"""9. sınıf Matematik 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('Cebirsel özdeşlikler ve dağılma özelliği', [
        ('(a + b)²', 'a² + 2ab + b²', MAVI, MAVI_A),
        ('(a - b)²', 'a² - 2ab + b²', TUR, TUR_A),
        ('a² - b²', '(a - b) · (a + b)', YES, YES_A),
        ('Dağılma', 'a·(b + c) = ab + ac', MOR, MOR_A)
    ])

def g1():
    return uclu_pano('Tam kare özdeşliği ve geometrik alan modeli', 'TAM KARE ÖZDEŞLİĞİ VE DEĞER HESAPLAMA BAĞINTILARI', [
        ('Toplamın Karesi', '(x+y)² = x² + 2xy + y²', MAVI, '#f4f8fe'),
        ('Kareler Toplamı', 'x² + y² = (x+y)² - 2xy', YES, YES_A),
        ('Örnek Çözüm', '8² = 40 + 2xy → xy = 12', TUR, TUR_A)
    ], MAVI, MAVI_A)

def g2():
    return bilgi_panosu('İki kare farkı sayısal analojisi', 'İKİ KARE FARKI ÖZDEŞLİĞİ · a² - b² = (a - b) · (a + b)',
        '2026² - 2024² = (2026 - 2024) · (2026 + 2024) = 2 · 4050 = 8100',
        'Paydadaki 4 ile bölündüğünde: 8100 / 4 = 2025 sonucu saniyeler içinde bulunur.', CAM, CAM_A)

def g3():
    return dörtlu_kart('Gerçek sayı işlem ve sıralama aksiyomları', [
        ('Birim Eleman', 'Toplama: 0 · Çarpma: 1', MAVI, MAVI_A),
        ('Ters Eleman', 'Toplama: -a · Çarpma: 1/a', YES, YES_A),
        ('Negatif Çarpım', 'c < 0 ise eşitsizlik döner', KIR, KIR_A),
        ('Basit Kesir', '0 < x < 1 ⇔ x² < x', MOR, MOR_A)
    ])

def g5():
    return akis_karti('Gruplandırma ve sıfır çarpan adımları', [
        ('1. Gruplandır', 'x(x-3) - y(x-3) = 0', MAVI, MAVI_A),
        ('2. Ortak Çarpan', '(x - 3) · (x - y) = 0', YES, YES_A),
        ('3. Sıfır Çarpan', 'a·b = 0 ⇒ a=0 ∨ b=0', TUR, TUR_A),
        ('4. Kökleri Bul', 'x = 3 veya x = y', MOR, MOR_A)
    ])

def g6():
    return uclu_pano('Gerçek sayılarda eşitsizlik özellikleri', 'SIRALAMA (EŞİTSİZLİK) ÖZELLİKLERİ VE İŞARET İNCELEMESİ', [
        ('Toplama Özelliği', 'a < b ⇒ a + c < b + c', YES, YES_A),
        ('Pozitif Çarpma (c>0)', 'a < b ⇒ a·c < b·c', MAVI, '#f4f8fe'),
        ('Negatif Çarpma (b<0)', 'a < b < 0 ⇒ a·b > b²', KIR, KIR_A)
    ], MOR, MOR_A)

def g7():
    return bilgi_panosu('Dağılma, özdeşlik ve geçişme kavramları', 'DAĞILMA ÖZELLİĞİ · ÖZDEŞLİK · GEÇİŞME ÖZELLİĞİ',
        'Ortak çarpan parantezi: a·b + a·c = a·(b + c)  |  Geçişme: a < b ve b < c ⇒ a < c',
        'Her gerçek sayı değeri için doğru olan cebirsel eşitliklere özdeşlik denir.', YES, YES_A, '#eaf8f0')

def g8():
    return dörtlu_kart('Çarpanlara ayırma temel yöntemleri', [
        ('Ortak Çarpan', '6x²y - 9xy² = 3xy(2x-3y)', MAVI, MAVI_A),
        ('İki Kare Farkı', 'x² - 16y² = (x-4y)(x+4y)', YES, YES_A),
        ('Tam Kare', 'x² - 10x + 25 = (x-5)²', TUR, TUR_A),
        ('Gruplandırma', 'ax+ay+bx+by = (x+y)(a+b)', MOR, MOR_A)
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
