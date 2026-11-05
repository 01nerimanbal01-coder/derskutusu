"""11. sınıf Biyoloji 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def g0():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    elemanlar = [('Dendrit', 'Uyartıyı alır', MAVI, MAVI_A), ('Hücre Gövdesi', 'Çekirdek + Nissl', YES, YES_A), ('Miyelinli Akson', 'Atlamalı iletim', TUR, TUR_A), ('Ranvier Boğumu', 'İyon geçiş noktası', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Nöronun yapısal kısımları şeması', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'ÖZDEŞ İKİ NÖRONDA UYARAN ŞİDDETİ VE İMPULS', 10.5, MAVI)
    ic += kutu(16, 36, 156, 64, '#f4f8fe', MAVI) + yazi(94, 56, 'K Nöronu (Eşik Şiddet: E)', 10, MAVI) + yazi(94, 78, 'Hız: V  ·  İmpuls sayısı: Az', 8.5, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, YES_A, YES) + yazi(266, 56, 'L Nöronu (Şiddet: 4E)', 10, YES) + yazi(266, 78, 'Hız: V (Aynı) · İmpuls: Çok', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Uyaran şiddeti ve impuls frekansı karşılaştırması', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'MİYELİN KILIF VE ATLAMALI İLETİM PRENSİBİ', 10.5, TUR)
    ic += yazi(180, 58, 'Olgun nöronda sentrozom yoktur; bölünme gerçekleşmez.', 10, LAC)
    ic += yazi(180, 82, 'Miyelinli aksonlarda impuls Ranvier boğumlarında 10 kat hızlı ilerler.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Miyelinli nöron ve atlamalı iletim bilgi kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    evreler = [('Polarize', 'Dış (+) / İç (-)', MAVI, MAVI_A), ('Depolarize', 'Na+ içeri girer', TUR, TUR_A), ('Repolarize', 'K+ dışarı çıkar', YES, YES_A), ('Pompa', 'Na+/K+ aktif taşıma', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(evreler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Nöronda elektriksel yük değişimleri', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Ca2+ Girişi', 'Akson ucuna uyartı', YES, YES_A), ('2. Ekzositoz', 'Keseler boşalır', MAVI, MAVI_A), ('3. Difüzyon', 'Boşlukta yayılma', TUR, TUR_A), ('4. Yeni İmpuls', 'Dendritte Na+ açılır', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Sinapsta kimyasal iletim basamakları', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'REFLEKS YAYINDA GÖREV YAPAN NÖRON SIRASI', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'Reseptör -> Duyu Nöronu -> Ara Nöron -> Motor Nöron -> Efektör', 9.5, LAC) + yazi(180, 84, 'Merkezdeki cevabı kas ve bezlere Motor (Götürücü) nöron taşır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Refleks yayı nöron dizilimi', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'NÖRON GÖVDESİ, MİYELİN ÜRETİMİ VE SEÇİCİ DİRENÇ', 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Nissl Cisimcikleri (Granüllü ER) · Oligodendrosit · Seçici Direnç', 9.5, LAC) + yazi(180, 82, 'Durdurucu ve kolaylaştırıcı sinapslar impulsun hedefini belirler.', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Nöron yapıları ve seçici direnç özeti', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    glia = [('Mikroglia', 'Fagositoz savunma', MAVI, MAVI_A), ('Astrosit', 'Kan-beyin bariyeri', TUR, TUR_A), ('Ependim', 'BOS sıvısı üretimi', YES, YES_A), ('Nörotransmitter', 'Kimyasal elçi', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(glia):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Glia destek hücreleri ve görevleri', 34)

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
