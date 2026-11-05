"""12. sınıf Biyoloji 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return kart4('DNA replikasyonu enzimleri ve yapıları', [('Helikaz', 'Hidrojen bağı açar', KIR, KIR_A), ('DNA Polimeraz', 'Nükleotit ekler', MAVI, MAVI_A), ('DNA Ligaz', 'Fosfodiester kurar', YES, YES_A), ('Orijin', 'Başlangıç dizisi', MOR, MOR_A)])

def g1():
    return uclu('Meselson ve Stahl yarı korunumlu eşlenme deneyi', 'MESELSON-STAHL · 15N15N ATA DNA → 14N ORTAMDA EŞLENME', ('Başlangıç (0.)', '%100 Ağır (15N15N)', KIR, KIR_A), ('1. Bölünme', '%100 Melez (15N14N)', MOR, MOR_A), ('2. Bölünme', '%50 Melez · %50 Normal', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('Prokaryot ve ökaryot replikasyon orijini farkı', 'PROKARYOT VE ÖKARYOT HÜCRELERDE REPLİKASYON ORİJİNİ', 'Prokaryot (Halkasal DNA): Tek Replikasyon Orijini', 'Ökaryot (Doğrusal DNA): Çok Sayıda Orijin → Hızlı Eşlenme', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('Replikasyon özellikleri ve Aziz Sancar', [('Helikaz', 'ATP harcamaz', YES, YES_A), ('Prokaryot DNA', 'Tek orijinli halkasal', MAVI, MAVI_A), ('DNA Ligaz', 'ATP harcar, bağlar', TUR, TUR_A), ('Aziz Sancar', 'Nobel → Anıtkabir', MOR, MOR_A)])

def g5():
    return akis4('DNA replikasyonu gerçekleşme sırası', [('1. Orijin', 'Başlangıç noktası', MOR, MOR_A), ('2. Helikaz', 'Sarmal açılır', KIR, KIR_A), ('3. Polimeraz', 'Yeni zincir sentezi', MAVI, MAVI_A), ('4. Ligaz', 'Parçalar birleşir', YES, YES_A)])

def g6():
    return pano('Aziz Sancar Nobel Kimya Ödülü çalışması', 'PROF. DR. AZİZ SANCAR · 2015 NOBEL KİMYA ÖDÜLÜ', 'UV Hasarlı DNA → Nükleotit Kesip Çıkarma Onarımı Haritalaması', 'Hasarlı dizi kesilip çıkarılır; DNA polimeraz ve ligaz ile onarılır.', MOR, MOR_A, '#f5f0ff')

def g7():
    return pano('Yarı korunumlu eşlenme, ligaz ve sirkadiyen ritim', 'REPLİKASYON MEKANİZMASI VE BİYOLOJİK SAAT', 'Yarı Korunumlu Eşlenme · DNA Ligaz · Sirkadiyen Ritim Genleri', 'Her yeni DNA bir eski (kalıp) ve bir yeni sentezlenen zincir taşır.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('DNA eşlenmesi ve onarımı kavramları', [('Meselson-Stahl', '15N/14N izotop kanıtı', MAVI, MAVI_A), ('Kesip Çıkarma', 'UV DNA onarımı', YES, YES_A), ('Sirkadiyen Saat', 'Biyolojik ritim', TUR, TUR_A), ('Eşlenme Çatalı', 'Y biçimli açılma', MOR, MOR_A)])

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
