"""9. sınıf Coğrafya 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('Türkiye coğrafi koordinatları', [
        ('36°-42° Kuzey', 'Orta Kuşak (Enlem)', MAVI, MAVI_A),
        ('26°-45° Doğu', '76 dk fark (Boylam)', YES, YES_A),
        ('Dönence Dışı', 'Gölge sıfır olmaz', TUR, TUR_A),
        ('Göreceli Konum', 'Yükselti ve boğazlar', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Güneyden kuzeye enlem etkisi', 'HATAY’DAN (36°K) SİNOP’A (42°K) GİDİLDİKÇE DEĞİŞİMLER', [
        ('Geliş Açısı & Sıcaklık', 'Kuzeye doğru AZALIR', KIR, KIR_A),
        ('Deniz Tuzluluğu', 'Akdeniz > Karadeniz', MAVI, '#f4f8fe'),
        ('Gece-Gündüz Farkı', 'Kuzeye doğru ARTAR', YES, YES_A)
    ], MAVI, MAVI_A)
def g2():
    return bilgi_panosu('Yıl içinde ve aynı anda dört mevsim farkı', 'ALTIN AYRIM: “YIL İÇİNDE” Mİ, “AYNI ANDA” MI?',
        'Yıl İçinde 4 Mevsim → Orta Kuşak (Mutlak Konum: ABCD Kuralı)',
        'Aynı Anda 4 Mevsim → Kısa mesafede yükselti ve yer şekli değişimi (Göreceli Konum)', TUR, TUR_A, '#fff6ea')
def g3():
    return dörtlu_kart('Orta Kuşak ABCD kuralı', [
        ('A - Akdeniz', 'Akdeniz iklim kuşağı', MAVI, MAVI_A),
        ('B - Batı', 'Batı rüzgârları etkisi', YES, YES_A),
        ('C - Cephe', 'Cephesel yağışlar', TUR, TUR_A),
        ('D - Dört Mevsim', 'Yıl içinde belirgin', MOR, MOR_A)
    ])
def g5():
    return akis_karti('Güneyden kuzeye deniz tuzluluğu', [
        ('1. Akdeniz', 'Tuzluluk ‰38 (En çok)', KIR, KIR_A),
        ('2. Ege Denizi', 'Tuzluluk ‰33', TUR, TUR_A),
        ('3. Marmara', 'Tuzluluk ‰23', MAVI, MAVI_A),
        ('4. Karadeniz', 'Tuzluluk ‰18 (En az)', YES, YES_A)
    ])
def g6():
    return bilgi_panosu('Boylam ve yerel saat hesabı', '26° DOĞU (GÖKÇEADA) — 45° DOĞU (IĞDIR) YEREL SAAT FARKI',
        'Meridyen Farkı: 45 - 26 = 19 Meridyen · Yerel Saat Farkı: 19 × 4 dk = 76 Dakika (1 sa 16 dk)',
        '45° Doğu Iğdır meridyeni (GMT+3) tüm Türkiye’de ulusal (ortak) saat olarak kullanılır.', CAM, CAM_A)
def g7():
    return uclu_pano('Türkiye’nin göreceli konumu', 'FİZİKİ VE JEOPOLİTİK GÖRECELİ (ÖZEL) KONUM', [
        ('Yükselti (1141 m)', 'Batıdan doğuya artar', TUR, TUR_A),
        ('Boğazlar & Kıta', 'Asya-Avrupa köprüsü', MAVI, '#f4f8fe'),
        ('Enerji Koridoru', 'TANAP ve TürkAkım', YES, YES_A)
    ], YES, YES_A)
def g8():
    return dörtlu_kart('Göreceli konum sonuçları', [
        ('Batı → Doğu', 'Yükselti artar, soğur', MAVI, MAVI_A),
        ('Genç Arazi', 'Fay hattı ve jeotermal', KIR, KIR_A),
        ('Su Yolları', 'İstanbul ve Çanakkale', CAM, CAM_A),
        ('Jeopolitik', 'Üç kıtanın kavşağı', MOR, MOR_A)
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
