"""11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ogeler = [('Dilsel Katman', 'Kelime ve üslup'), ('İşitsel Katman', 'Vurgu, ton ve müzik'), ('Görsel Katman', 'Işık, renk ve açı'), ('Örtük İleti', 'Alt metin anlamı')]
    colors = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, alt) in enumerate(ogeler):
        c, d = colors[i]
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g0', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'DİNLEME / İZLEME SÜRECİNİ YÖNETME AŞAMALARI', 10, MAVI)
    ic += kutu(16, 36, 156, 64, '#f4f8fe', MAVI) + yazi(94, 56, '1. Süreç Öncesi Hazırlık', 9.5, MAVI) + yazi(94, 78, 'Başlık/görsel tahmini ve amaç', 8.5, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, YES_A, YES) + yazi(266, 56, '2-3. Sırası ve Sonrası', 9.5, YES) + yazi(266, 78, 'Not alma, özet ve eleştirel analiz', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g1', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'ÇOK MODLU METİNLERDE KATMANLAR ARASI KARŞITLIK (İRONİ)', 10, TUR)
    ic += yazi(180, 58, 'Sözlü Katman: “Teknoloji insanları birbirine yaklaştırıyor.”', 9.5, LAC)
    ic += yazi(180, 82, 'Görsel Katman: Aynı masada birbirine bakmayan insanlar -> Örtük İleti!', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g2', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('Çok Modlu', 'Tüm katmanlar kurucu'), ('Anahtar Not', 'Kavram odaklı kayıt'), ('Geçiş İfadesi', 'Yön değiştiren bağlaç'), ('Kanıt Sorgusu', 'Eleştirel denetim')]
    colors = [(MAVI, MAVI_A), (TUR, TUR_A), (YES, YES_A), (MOR, MOR_A)]
    for i, (b, alt) in enumerate(ogeler):
        c, d = colors[i]
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g3', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlar = [('1. İzleme Öncesi', 'Tahmin ve amaç'), ('2. İzleme Sırası', 'Katman ve not takibi'), ('3. Özetleme', 'Açık ve örtük ileti'), ('4. Değerlendirme', 'Güvenilirlik denetimi')]
    colors = [(YES, YES_A), (MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (bas, alt) in enumerate(adimlar):
        c, d = colors[i]
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g5', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'ELEŞTİREL DİNLEMEDE NESNEL VERİ VE ÖZNEL YARGI AYRIMI', 10, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'Nesnel: “1,2 °C arttı” (Kanıtlanabilir)  ·  Öznel: “Vicdanımız sızlamalı” (Duygusal)', 9.5, LAC) + yazi(180, 84, 'Eleştirel dinleyici, bilimsel kanıtlar ile kişisel yorumları birbirinden ayırt eder.', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g6', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'ÇOK MODLU METİN, TEZ (İDDİA) VE MANİPÜLASYON DENETİMİ', 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Çok Modlu Metin (Bütüncül Gösterge)  ·  Tez (Merkezî İddia)  ·  Manipülasyon', 9.5, LAC) + yazi(180, 82, 'Bilgi kaynaklarının güvenilirliği çapraz kontrolle denetlenmelidir.', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g7', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('Empatik Dinleme', 'Duygudaşlık kurma'), ('Eleştirel İzleme', 'Kanıt ve tutarlılık'), ('Jest', 'El, kol, baş hareketi'), ('Mimik', 'Yüz ve göz ifadeleri')]
    colors = [(MAVI, MAVI_A), (TUR, TUR_A), (YES, YES_A), (MOR, MOR_A)]
    for i, (b, tr) in enumerate(ogeler):
        c, d = colors[i]
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, '11. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri g8', 34)

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
