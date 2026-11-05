"""10. sınıf Tarih 2. hafta (Türkistan’dan Türkiye’ye Askerî Mücadeleler) çalışma kâğıdı görselleri.
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

def g0_savaslar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    savaslar = [
        ('1176 Miryokefalon', 'Tapu alındı', MAVI, MAVI_A),
        ('1187 Hıttin', 'Kudüs kurtarıldı', TUR, TUR_A),
        ('1204 IV. Haçlı', 'İstanbul yağması', KIR, KIR_A),
        ('1243 Kösedağ', 'Moğol istilası', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(savaslar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Dört büyük askerî mücadele kronoloji kartı', 34)


def g1_miryokefalon():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(84, 28, '1176 MİRYOKEFALON', 10, MAVI)
    ic += yazi(84, 48, 'II. Kılıç Arslan', 9.5, LAC)
    ic += yazi(84, 62, 'vs.', 8.5, SOLUK)
    ic += yazi(84, 76, 'Manuel Komnenos', 9.5, LAC)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 28, 'Tarihî Dönüm Noktası', 10.5, MAVI)
    ic += yazi(257, 46, '• Anadolu kesin Türk yurdu oldu', 9, LAC, ince=True)
    ic += yazi(257, 60, '• Bizans savunmaya çekildi', 9, LAC, ince=True)
    ic += yazi(257, 74, '• Batı buraya "Türkiye" dedi', 9, YES)
    return svg(360, 100, ic, 'Miryokefalon zaferi sonuçları şeması', 34)


def g2_hittin():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += kutu(14, 12, 130, 76, '#d8f3e2', YES, 6, 1.2)
    ic += yazi(79, 28, '1187 HITTİN', 11, YES)
    ic += yazi(79, 48, 'Selahaddin Eyyubi', 9.5, LAC)
    ic += yazi(79, 72, 'Kudüs Fethi', 10, TUR)

    ic += kutu(156, 12, 190, 76, '#eaf8f0', YES, 6, 1.2)
    ic += yazi(251, 30, 'Kudüs Haçlılardan Alındı', 10.5, YES)
    ic += yazi(251, 50, '88 yıllık Haçlı işgaline son verildi.', 9, LAC, ince=True)
    ic += yazi(251, 68, 'III. Haçlı Seferi’ne yol açtı.', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Hıttin muharebesi ve Kudüsün fethi', 34)


def g3_beylikler():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    beylikler = [
        ('Danişment', 'Sivas / Medrese', '#fef6ec'),
        ('Saltuklu', 'Erzurum / Kümbet', '#fdf1e2'),
        ('Mengücek', 'Divriği / Taş Sanatı', '#fcecd8'),
        ('Çaka Beyi', 'İzmir / Donanma', '#fbe7ce')
    ]
    for i, (b, d, bg) in enumerate(beylikler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, TUR, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, TUR)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{TUR}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Anadolu ilk Türk beylikleri ve eserleri', 34)


def g5_tarih_akisi():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    olaylar = [
        ('1071', 'Malazgirt Zaferi'),
        ('1176', 'Miryokefalon'),
        ('1187', 'Hıttin / Kudüs'),
        ('1243', 'Kösedağ Savaşı')
    ]
    for i, (yil, ad) in enumerate(olaylar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f2fbfd', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, yil, 12, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, ad, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Türk tarihinin askerî dönüm noktaları kronolojisi', 34)


def g6_kosedag():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 140, 76, '#ece4fd', MOR, 6, 1.2)
    ic += yazi(84, 28, '1243 KÖSEDAĞ', 10.5, MOR)
    ic += yazi(84, 48, 'Selçuklu ordusu Moğol', 9, LAC, ince=True)
    ic += yazi(84, 62, 'İlhanlı kuvvetlerine', 9, LAC, ince=True)
    ic += yazi(84, 76, 'mağlup oldu.', 9, KIR)

    ic += kutu(168, 12, 178, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(257, 28, 'Tarihî Sonuçları', 10.5, MOR)
    ic += yazi(257, 46, '• Selçuklu bağımsızlığı sarsıldı', 9, LAC, ince=True)
    ic += yazi(257, 60, '• Anadolu Moğol tahakkümüne girdi', 8.5, LAC, ince=True)
    ic += yazi(257, 74, '• İkinci Beylikler Dönemi başladı', 9, TUR)
    return svg(360, 100, ic, 'Kösedağ savaşı ve beylikler dönemi başlangıcı', 34)


def g8_hacli_seferleri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    seferler = [
        ('I. Haçlı', 'Kudüs işgal edildi', MAVI, MAVI_A),
        ('II. Haçlı', 'Urfa geri alındı', YES, YES_A),
        ('III. Haçlı', 'Kudüs savunması', TUR, TUR_A),
        ('IV. Haçlı', 'İstanbul yağması', KIR, KIR_A)
    ]
    for i, (b, d, c, a) in enumerate(seferler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Haçlı seferleri karşılaştırma kartları', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: Z - A - F - E - R', 11.5, YES)
    harfler = [('1', 'Z'), ('2', 'A'), ('3', 'F'), ('4', 'E'), ('5', 'R')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Zafer şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_savaslar()
    s[1]['gorsel'] = g1_miryokefalon()
    s[2]['gorsel'] = g2_hittin()
    s[3]['gorsel'] = g3_beylikler()
    s[5]['gorsel'] = g5_tarih_akisi()
    s[6]['gorsel'] = g6_kosedag()
    s[8]['gorsel'] = g8_hacli_seferleri()
    s[10]['gorsel'] = g10_sifre_seridi()
