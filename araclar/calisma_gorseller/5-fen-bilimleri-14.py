"""5. sınıf Fen Bilimleri 14. hafta çalışma kâğıdı görselleri."""
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
    s[0]['gorsel'] = kart4('Hücre yapıları ve organizasyon basamakları', [
        ('Hücre Duvarı', 'Bitkide sert dış çeper', YES, YES_A),
        ('Kloroplast', 'Besin ve O2 üretimi', CAM, CAM_A),
        ('Sentrozom', 'Hayvanda bölünme', TUR, TUR_A),
        ('Doku Basamağı', 'Benzer hücre grubu', MOR, MOR_A)
    ])
    s[1]['gorsel'] = ikili('Mikroskobik hücre gözlemi',
        'K Hücresi · Bitki (Elodea)', 'Köşeli Şekil + Yeşil Kloroplast', 'Hücre duvarı ve büyük koful var', YES, YES_A,
        'L Hücresi · Hayvan (Deri/Epitel)', 'Oval Şekil + Sentrozom', 'Hücre duvarı ve kloroplast yok', TUR, TUR_A)
    s[2]['gorsel'] = uclu('Bitki ve hayvan hücresi farkları', 'BİTKİ VE HAYVAN HÜCRESİ KARŞILAŞTIRMASI',
        ('Şekil ve Çeper', 'Bitki: Köşeli · Hayvan: Oval', YES, YES_A),
        ('Özel Organel', 'Bitki: Kloroplast · Hayvan: Sentrozom', MAVI, MAVI_A),
        ('Koful Yapısı', 'Bitki: Büyük-Az · Hayvan: Küçük-Çok', MOR, MOR_A))
    s[5]['gorsel'] = uclu('Hücre Venn şeması özeti', 'BİTKİ VE HAYVAN HÜCRESİ VENN KÜMELERİ',
        ('Yalnız Bitkide', 'Hücre duvarı, Kloroplast', YES, YES_A),
        ('Ortak Yapılar (Kesişim)', 'Zar, Çekirdek, Mitokondri', MAVI, MAVI_A),
        ('Yalnız Hayvanda', 'Sentrozom, Lizozom', TUR, TUR_A))
    s[6]['gorsel'] = akis4('Hücreden organizmaya organizasyon şeması', [
        ('1. Hücre', 'Epitel / Kas hücresi', MAVI, MAVI_A),
        ('2. Doku (X)', 'Mide dokusu', CAM, CAM_A),
        ('3. Organ', 'Mide organı', YES, YES_A),
        ('4. Sistem', 'Sindirim sistemi', MOR, MOR_A)
    ])
    s[7]['gorsel'] = ikili('Soğan zarı ve yeşil yaprak hücresi karşılaştırması',
        'Soğan Zarı Hücresi (Toprak Altı)', 'Köşeli + Hücre Duvarı Var', 'Işık görmediği için Kloroplast YOK', TUR, TUR_A,
        'Yeşil Yaprak Hücresi (Işıklı)', 'Köşeli + Hücre Duvarı Var', 'Fotosentez yaptığı için Kloroplast VAR', YES, YES_A)
    s[8]['gorsel'] = akis4('Destek ve hareket sistemi organizasyonu', [
        ('1. Hücre', 'Kemik hücresi', MAVI, MAVI_A),
        ('2. Doku', 'Kemik dokusu', YES, YES_A),
        ('3. Organ', 'Uyluk kemiği', TUR, TUR_A),
        ('4. Sistem', 'Destek-hareket sistemi', MOR, MOR_A)
    ])
    s[9]['gorsel'] = akis4('Geçmişten günümüze hücre araştırmaları', [
        ('1665 · Hooke', 'İlk hücre gözlemi', MAVI, MAVI_A),
        ('1674 · Leeuwenhoek', 'Canlı tek hücreliler', CAM, CAM_A),
        ('1838-39 · Hücre Teorisi', 'Schleiden ve Schwann', YES, YES_A),
        ('1931 · Elektron Mik.', 'Organellerin keşfi', MOR, MOR_A)
    ])
