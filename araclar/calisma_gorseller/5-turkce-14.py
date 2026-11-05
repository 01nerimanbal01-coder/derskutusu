"""5. sınıf Türkçe 14. hafta çalışma kâğıdı görselleri."""
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
    s[0]['gorsel'] = kart4('Düşünceyi geliştirme yolları', [
        ('Tanımlama', '«… nedir?» cevabı', MAVI, MAVI_A),
        ('Karşılaştırma', 'Benzer / farklı yön', TUR, TUR_A),
        ('Örneklendirme', 'Somut örnek verme', YES, YES_A),
        ('Benzetme', '«gibi» ile ilişki', MOR, MOR_A)
    ])
    s[1]['gorsel'] = ikili('Yüzey anlam ve derin anlam karşılaştırması',
        'Yüzey Anlam (Gerçek Boyut)', 'İplikle kumaşa desen işlemek', 'Kelimelerin sözlükteki ilk anlamı', MAVI, MAVI_A,
        'Derin Anlam (Asıl İleti)', 'Yüreği sevgi ve erdemle bezemek', 'Her Yüreğe Nakış Gerek dizelerinin mesajı', MOR, MOR_A)
    s[2]['gorsel'] = uclu('Geçiş ve bağlantı ifadeleri tablosu', 'KONUŞMA VE YAZMADA GEÇİŞ VE BAĞLANTI İFADELERİ',
        ('Yön Değiştirenler', 'ama, fakat, lakin, oysa', KIR, KIR_A),
        ('Destekleyenler', 'çünkü, yani, özellikle', MAVI, MAVI_A),
        ('Özetleyenler', 'kısacası, özetle, sonuçta', YES, YES_A))
    s[5]['gorsel'] = pano('Hikâye unsurları inceleme metni', 'ÖYKÜ PARÇASI · HİKÂYE UNSURLARI ANALİZİ',
        '«Elif ve dedesi, köy meydanındaki yaşlı çınarın altına yeni bir meşe fidanı dikip can suyu verdiler.»',
        'Şahıs: Elif ve dedesi · Yer: Köy meydanı çınar altı · Olay: Fidan dikimi · Zaman: Belirtilmemiş', CAM, CAM_A)
    s[6]['gorsel'] = ikili('Bağlaç ve ek olan de/ki yazımı',
        'Ayrı Yazılanlar (Bağlaç)', 'arkadaşlarıyla da · Anladım ki', 'Cümleden çıkarılınca anlam bozulmaz', YES, YES_A,
        'Bitişik Yazılanlar (Ek)', 'Yüreğindeki · Okuldaki · Bahçedeki', 'Bulunma ve sıfat yapan -de/-ki bitişiktir', KIR, KIR_A)
    s[7]['gorsel'] = pano('Noktalama işaretleri uygulaması', 'NOKTALAMA İŞARETLERİ UYGULAMA CÜMLESİ',
        'Yaşasın ( ! ) Dedem bana dönerek ( " ) İyilik yapan iyilik bulur ( . ) ( " ) dedi.',
        'Duygu bildiren sözden sonra ünlem (!), doğrudan alıntı cümlelerin başında ve sonunda tırnak (" ") kullanılır.', TUR, TUR_A)
    s[8]['gorsel'] = akis4('Metnin bölümleri ve olay akışı', [
        ('1. Giriş (Serim)', 'Bankta tanışma anı', MAVI, MAVI_A),
        ('2. Gelişme-1', 'Resimleri inceleme', CAM, CAM_A),
        ('3. Gelişme-2', 'Kitap sohbeti', YES, YES_A),
        ('4. Sonuç (Çözüm)', 'Yeni dostluğun doğuşu', MOR, MOR_A)
    ])
    s[9]['gorsel'] = ikili('Yüzey anlam ve derin anlam soruları',
        'Yüzey Anlam Soruları (5N1K)', 'Kim, nerede, ne zaman?', 'Cevabı metinde doğrudan geçen sorular', MAVI, MAVI_A,
        'Derin Anlam ve Çıkarım Soruları', 'Şairin asıl iletisi nedir?', 'Metnin ana duygusunu ve mesajını sorgular', MOR, MOR_A)
