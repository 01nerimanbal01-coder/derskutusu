"""5. sınıf Matematik 14. hafta çalışma kâğıdı görselleri."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#475569'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="16" font-weight="700"'

def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:24mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'

def kart4(etiket, veri, ar=False):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 91, d, c) + yazi(x + 40, 34, b, 9.2, c)
        ic += f'<line x1="{x+8}" y1="46" x2="{x+72}" y2="46" stroke="{c}" stroke-width="0.8"/>'
        ic += (ar_yazi(x + 40, 76, alt, LAC) if ar else yazi(x + 40, 72, alt, 8.2, LAC, ince=True))
    return svg(ic, etiket)

def ikili(etiket, b1, s1a, s1b, c1, d1, b2, s2a, s2b, c2, d2, ar=False):
    ic = kutu(6, 6, 170, 103, d1, c1) + yazi(91, 26, b1, 9.8, c1)
    ic += (ar_yazi(91, 58, s1a, LAC) if ar else yazi(91, 56, s1a, 9.5, LAC))
    ic += yazi(91, 88, s1b, 8.5, SOLUK, ince=True)
    ic += kutu(184, 6, 170, 103, d2, c2) + yazi(269, 26, b2, 9.8, c2)
    ic += (ar_yazi(269, 58, s2a, LAC) if ar else yazi(269, 56, s2a, 9.5, LAC))
    ic += yazi(269, 88, s2b, 8.5, SOLUK, ince=True)
    return svg(ic, etiket)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A, ar=False):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 22, baslik, 9.8, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 14 + i * 113
        ic += kutu(x, 32, 106, 71, kd, kc) + yazi(x + 53, 52, b, 9.0, kc)
        ic += (ar_yazi(x + 53, 84, alt, LAC) if ar else yazi(x + 53, 80, alt, 8.2, LAC, ince=True))
    return svg(ic, etiket)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 91, d, c) + yazi(x + 40, 36, bas, 9.0, c) + yazi(x + 40, 70, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+81},56 {x+85},51 {x+85},61" fill="{c}"/>'
    return svg(ic, etiket)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe', ar=False):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 23, baslik, 9.8, c)
    ic += kutu(14, 34, 332, 67, ic_d, c)
    ic += (ar_yazi(180, 62, s1, LAC) if ar else yazi(180, 58, s1, 9.5, LAC))
    ic += yazi(180, 86, s2, 8.5, SOLUK, ince=True)
    return svg(ic, etiket)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kart4('Çevre ve alan temel bağıntıları', [
        ('Çevre = 28 cm', 'a + b = 14 cm', MAVI, MAVI_A),
        ('En Büyük Alan', '7 × 7 = 49 cm²', YES, YES_A),
        ('En Küçük Alan', '1 × 13 = 13 cm²', TUR, TUR_A),
        ('Alan = 36 cm²', 'Min Çevre = 24 cm', MOR, MOR_A)
    ])
    s[1]['gorsel'] = ikili('36 cm tel ile en büyük alanlı dikdörtgen',
        'Yarı Çevre Hesabı', 'a + b = 36 ÷ 2 = 18 cm', 'Kenarlar birbirine en yakın seçilir', MAVI, MAVI_A,
        'En Büyük Alan (a = 9, b = 9)', 'Alan = 9 × 9 = 81 cm²', '1 × 17 = 17 cm² (En küçük alan)', YES, YES_A)
    s[2]['gorsel'] = uclu('Alanı 24 cm² olan dikdörtgenlerde çevre değişimi', 'ALANI 24 cm² OLAN DİKDÖRTGENLERİN ÇEVRELERİ',
        ('1 cm × 24 cm', 'Çevre = 50 cm (En büyük)', KIR, KIR_A),
        ('2 cm × 12 cm', 'Çevre = 28 cm', TUR, TUR_A),
        ('4 cm × 6 cm', 'Çevre = 20 cm (En küçük)', YES, YES_A))
    s[5]['gorsel'] = akis4('Çok adımlı kütüphane problemi çözümü', [
        ('1. Toplam Kitap', '15 × 24 = 360', MAVI, MAVI_A),
        ('2. Ayrılanlar', '360 - 40 = 320', TUR, TUR_A),
        ('3. 8 Rafa Bölme', '320 ÷ 8 = 40 kitap', CAM, CAM_A),
        ('4. Kontrol', 'Adım adım doğrulama', YES, YES_A)
    ])
    s[6]['gorsel'] = pano('Kapı boşluklu bahçe teli problemi', 'BAHÇE KENARLARI: 12 m × 20 m · KAPI BOŞLUĞU: 3 m',
        'Çevre = 2 × (12 + 20) = 64 m → 1 Sıra Tel = 64 - 3 = 61 m',
        '2 Sıra Tel İçin Gereken Toplam Uzunluk: 2 × 61 = 122 metre', YES, YES_A)
    s[7]['gorsel'] = ikili('Birleşik iki dikdörtgenin dış çevresi',
        'Ayrı İken (4 cm × 9 cm)', 'Birinin Çevresi = 26 cm', 'İkisinin toplamı = 52 cm', TUR, TUR_A,
        '4 cm Kenardan Birleşince', 'Yeni Boyut: 4 cm × 18 cm', 'İçteki ortak kenar (2×4=8 cm) sayılmaz → 44 cm', MAVI, MAVI_A)
    s[8]['gorsel'] = kart4('Alanı 36 cm² olan dikdörtgenlerin çevreleri', [
        ('6 cm × 6 cm', 'Çevre = 24 cm', YES, YES_A),
        ('4 cm × 9 cm', 'Çevre = 26 cm', CAM, CAM_A),
        ('3 cm × 12 cm', 'Çevre = 30 cm', TUR, TUR_A),
        ('2 cm × 18 cm', 'Çevre = 40 cm', MOR, MOR_A)
    ])
    s[9]['gorsel'] = ikili('Kat ve eksiklik problemi kutu modeli',
        'Elif: [ 1 Kat ] · Kerem: [ 4 Kat - 15 TL ]', 'Toplam = 5 Kat - 15 TL = 235 TL', 'Eksik olan 15 TL toplama eklenir', MAVI, MAVI_A,
        '1 Katın Bulunması', '5 Kat = 235 + 15 = 250 TL', 'Elif (1 Kat) = 250 ÷ 5 = 50 TL', YES, YES_A)
