"""7. sınıf Din Kültürü ve Ahlak Bilgisi 2. hafta (Melekleri Sınıflandırma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def uc_varlik_sema():
    kartlar = [
        ('Melek', 'Özü: Nur · Gayb âlemi', 'İradesi yok · Tam itaat', MAVI, MAVI_A),
        ('Cin', 'Özü: Yalın ateş · Gayb', 'İradeli · Emirlerden sorumlu', TUR, TUR_A),
        ('İnsan (Hz. Âdem)', 'Özü: Toprak · Görülür âlem', 'Akıl ve iradeli · Sorumlu', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 76, z, r, 8, 1.5)
        ic += yazi(x + 96, 25, bas, 11.2, r)
        ic += f'<line x1="{x + 14}" y1="32" x2="{x + 178}" y2="32" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 96, 51, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 96, 69, s2, 10.2, r)
    return svg(600, 88, ic, 'Melek, cin ve insanın yaratılış özü ile sorumluluk karşılaştırması.', 16)


def secde_tutum_sema():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.5)
    ic += yazi(149, 24, 'Meleklerin Tutumu', 11.2, YES)
    ic += yazi(149, 46, '• İsimleri Allah’ın öğrettiği kadar bildiler', 10.2, LAC, ince=True)
    ic += yazi(149, 64, '• Saygı emrine hemen uyup eğildiler', 10.2, LAC, ince=True)
    ic += yazi(149, 81, 'Sonuç: Tam İtaat ve Teslimiyet', 10.4, YES)

    ic += kutu(308, 6, 286, 86, KIR_A, KIR, 9, 1.5)
    ic += yazi(451, 24, 'İblis’in (Şeytanın) Tutumu', 11.2, KIR)
    ic += yazi(451, 46, '• “Ben ateşten, o çamurdan” diyerek böbürlendi', 10.2, LAC, ince=True)
    ic += yazi(451, 64, '• Yaratıldığı maddeyi üstünlük ölçüsü saydı', 10.2, LAC, ince=True)
    ic += yazi(451, 81, 'Sonuç: Kibir, İsyan ve Kovulma', 10.4, KIR)
    return svg(600, 98, ic, 'Hz. Âdem kıssasında meleklerin itaati ile İblis in kibri.', 17)


def ayet_bilgi_kartlari():
    kartlar = [
        ('Tahrim 6', 'Emre karşı gelmezler', MAVI, MAVI_A),
        ('Kehf 50', 'İblis cinlerdendir', TUR, TUR_A),
        ('Meryem 17', 'İnsan suretinde göründü', MOR, MOR_A),
        ('Zariyat 56', 'Cin ve insan kulluk içindir', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 11.0, r)
        ic += yazi(x + 71, 52, alt, 10.0, LAC, ince=True)
    return svg(600, 80, ic, 'Ayetlerde melek ve cinlerle ilgili temel ilkeler.', 15)


def gorev_zamani_panosu():
    kutular = [
        ('1. Kutu · Dünya Hayatı', 'Cebrail (vahiy) · Kiramen Kâtibin', MAVI, MAVI_A),
        ('2. Kutu · Ölüm Vakti', 'Azrail (can alma görevi)', TUR, TUR_A),
        ('3. Kutu · Kabir Hayatı', 'Mikâil (sorgulama görevi !)', KIR, KIR_A),
        ('4. Kutu · Kıyamet ve Diriliş', 'İsrafil (sûra iki kez üfleme)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 46
        ic += kutu(x, y, 286, 40, z, r, 7, 1.4)
        ic += yazi(x + 14, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 14, y + 32, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 100, ic, 'Görev zamanına göre melek grupları panosu.', 17)


def kissa_seridi():
    adimlar = [
        ('Halife Haberi', 'Hikmeti soruldu', MAVI, MAVI_A),
        ('İsimlerin Öğretimi', 'Âdem açıkladı', TUR, TUR_A),
        ('Saygı Emri', 'Melekler eğildi', YES, YES_A),
        ('İblis’in Kibri', 'Ateş iddiası ve ret', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.6, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Hz. Âdem kıssasındaki olay halkaları.', 15)


def iki_olcut_karti():
    ic = kutu(6, 6, 286, 74, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 25, '1. Tablo · Bilinirlik Ölçütü', 10.8, MAVI)
    ic += yazi(149, 47, 'Dört Büyük Melek: Cebrail, Mikâil,', 10.1, LAC, ince=True)
    ic += yazi(149, 65, 'İsrafil ve Azrail', 10.4, MAVI)

    ic += kutu(308, 6, 286, 74, MOR_A, MOR, 8, 1.5)
    ic += yazi(451, 25, '2. Tablo · Görev Zamanı Ölçütü', 10.8, MOR)
    ic += yazi(451, 47, 'Ölüm Anında Görev Yapan:', 10.1, LAC, ince=True)
    ic += yazi(451, 65, 'Azrail (Ölüm Meleği)', 10.4, MOR)
    return svg(600, 86, ic, 'Aynı meleğin iki farklı sınıflandırma ölçütündeki yeri.', 16)


def anahtar_ifade_tablosu():
    sat = [
        ('1. Satır: “Emre karşı gelmezler”', '→ İradesiz tam itaat', YES, YES_A),
        ('2. Satır: “İnsan biçiminde göründü”', '→ Farklı surete girme', MAVI, MAVI_A),
        ('3. Satır: “Kanatlarını indirirler”', '→ İlim yolcusundan hoşnutluk', TUR, TUR_A),
        ('4. Satır: “Rabler’ini tespih ederler”', '→ Gaybı kendiliğinden bilme (!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (s1, s2, r, z) in enumerate(sat):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, s1, 10.1, r, 'start')
        ic += yazi(x + 12, y + 31, s2, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Ayet ve hadis anahtar ifadelerinden özellik çıkarma kartları.', 16)


def melek_cin_kesisim():
    ic = kutu(6, 6, 190, 74, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(101, 25, 'Y · Yalnız Melek', 10.8, MAVI)
    ic += yazi(101, 47, 'Nurdan yaratılma', 10.1, LAC, ince=True)
    ic += yazi(101, 64, 'İradesi bulunmama', 10.1, LAC, ince=True)

    ic += kutu(205, 6, 190, 74, MOR_A, MOR, 9, 1.5)
    ic += yazi(300, 25, 'X · Ortak Özellik', 10.8, MOR)
    ic += yazi(300, 47, 'Gayb âlemine ait olma', 10.1, LAC, ince=True)
    ic += yazi(300, 64, 'Duyularla görülmeme', 10.1, MOR)

    ic += kutu(404, 6, 190, 74, TUR_A, TUR, 9, 1.5)
    ic += yazi(499, 25, 'Z · Yalnız Cin', 10.8, TUR)
    ic += yazi(499, 47, 'Ateşten yaratılma', 10.1, LAC, ince=True)
    ic += yazi(499, 64, 'İrade ve sorumluluk', 10.1, TUR)
    return svg(600, 86, ic, 'Melek ve cin varlıklarının ortak ve farklı yönleri şeması.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = uc_varlik_sema()
    s[1]['gorsel'] = secde_tutum_sema()
    s[3]['gorsel'] = ayet_bilgi_kartlari()
    s[5]['gorsel'] = gorev_zamani_panosu()
    s[6]['gorsel'] = kissa_seridi()
    s[7]['gorsel'] = iki_olcut_karti()
    s[8]['gorsel'] = anahtar_ifade_tablosu()
    s[11]['gorsel'] = melek_cin_kesisim()
