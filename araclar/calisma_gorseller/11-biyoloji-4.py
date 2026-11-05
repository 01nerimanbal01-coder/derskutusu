"""11. sınıf Biyoloji 4. hafta (Koleoptil ve Yönelme Deneyleri) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def bilim_insanlari_kartlari():
    kartlar = [
        ('1. Darwin (1880)', 'Uç Noktada Algılama', YES, YES_A),
        ('2. Boysen-Jensen', 'Jelatin vs Mika Levha', MAVI, MAVI_A),
        ('3. Paál (1919)', 'Asimetrik Tepe Yerleşimi', TUR, TUR_A),
        ('4. Went (1928)', 'Agar Blok ve Oksin Tayini', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Tarihsel koleoptil deneyleri kartı.', 34)


def darwin_deney_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'DARWİN DENEYLERİ: IŞIK VE UÇ ALGISI', 10.0, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Opak Başlıklı Tepe', 9.2, TUR)
    ic += yazi(92, 76, 'Işık algılanamaz', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Düz / Dik Büyüme', 8.6, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'Açık / Doğal Tepe', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Işık tek yönlü algılanır', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Işığa Doğru Bükülme', 8.6, YES, ince=True)
    return svg(360, 125, ic, 'Darwin koleoptil deneyi karşılaştırma şeması.', 34)


def boysen_jensen_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'BOYSEN-JENSEN: KİMYASAL İLETİM KANITI', 10.0, MAVI)
    ic += kutu(16, 36, 96, 70, '#ffffff', YES)
    ic += yazi(64, 56, 'Jelatin Blok', 9.0, YESIL_K)
    ic += yazi(64, 76, 'Geçirgen doku', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Yönelme Gerçekleşir', 8.4, YES, ince=True)
    ic += kutu(132, 36, 96, 70, '#ffffff', KIR)
    ic += yazi(180, 56, 'Gölgede Mika', 9.0, KIR)
    ic += yazi(180, 76, 'Geçirimsiz engel', 8.4, LAC, ince=True)
    ic += yazi(180, 92, 'Yönelme Engellenir', 8.4, KIR, ince=True)
    ic += kutu(248, 36, 96, 70, '#ffffff', TUR)
    ic += yazi(296, 56, 'Işıkta Mika', 9.0, TUR)
    ic += yazi(296, 76, 'Oksin gölgeden akar', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'Kıvrılma Görülür', 8.4, TUR, ince=True)
    return svg(360, 125, ic, 'Boysen-Jensen jelatin ve mika deney kesiti.', 34)


def klinostat_cihaz_modeli():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'KLİNOSTAT DÜZENEĞİ VE DÖNME ETKİSİ', 10.0, CAM)
    adımlar = [
        ('1. Fide Montajı', 'Yatay eksene bağlanır', 16),
        ('2. Sürekli Dönüş', 'Yavaş motor dönüşü', 102),
        ('3. Eşit Yerçekimi', 'Her yüzeye 360° etki', 188),
        ('4. Düz Gelişim', 'Bükülme olmadan uzama', 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 54, b, 8.2, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Klinostat düzeneği işleyiş basamakları.', 34)


def kontrollu_deney_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'KONTROLLÜ BİYOLOJİ DENEYİ DEĞİŞKENLERİ TABLOSU', 9.8, MOR)
    satirlar = [
        ('Değişken Türü', 'Deneydeki Karşılığı', 'Kontrol Durumu', MOR),
        ('Bağımsız Değişken', 'Işık Yönü / Opak Kılık / Agar', 'Araştırmacı Değiştirir', MAVI),
        ('Bağımlı Değişken', 'Koleoptilin Bükülme Açısı', 'Ölçülen Biyolojik Sonuç', YESIL_K),
        ('Sabit Faktörler', 'Sıcaklık (24°C), Nem ve Tohum Cinsi', 'Bütün Gruplarda Eşit', TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.2, r)
        ic += yazi(180, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Kontrollü deney değişken tablosu.', 34)


def agar_blok_went_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'WENT DENEYİ: ASİMETRİK AGAR BLOK VE OKSİN', 10.0, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Sol Yarıya Agar Blok', 9.2, YESIL_K)
    ic += yazi(92, 76, 'Oksin sol gövdeye sızar', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Sol hücreler daha çok uzar', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Karanlıkta Sağa Bükülme', 9.2, TUR)
    ic += yazi(267, 76, 'Işık olmadan da yönelir', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Derişim ile açı doğru orantılı', 8.4, TUR, ince=True)
    return svg(360, 125, ic, 'Went asimetrik agar blok şeması.', 34)


def oksin_gradyenti_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'DOKULARDA OKSİN DERİŞİMİ VE TEPKİ FARKLILIĞI', 10.0, TUR)
    kartlar = [
        ('Gövde Hücresi', 'Yüksek oksinde uzama artar', 16),
        ('Kök Hücresi', 'Düşük oksinde uzama artar', 102),
        ('Yüksek Derişim', 'Kök uzamasını baskılar', 188),
        ('Işık Tarafı', 'Oksin ışıktan kaçar', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Oksin derişimi ve organ tepkisi kartları.', 34)


def deney_asama_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, 'BİTKİ YÖNELME DENEYİ METODOLOJİK AŞAMALARI', 10.0, CAM)
    kutular = ['Hipotez Kurma', 'Değişken Seçimi', 'Kontrol Grubu', 'Açı Ölçümü']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', CAM, r=4)
        ic += yazi(x + 37, 66, f'Adım {i + 1}', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.2, CAM)
    return svg(360, 125, ic, 'Deney basamakları akış kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bilim_insanlari_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = darwin_deney_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = boysen_jensen_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = klinostat_cihaz_modeli()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = kontrollu_deney_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = agar_blok_went_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = oksin_gradyenti_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = deney_asama_kutulari()
    s[10]['en_fazla'] = 34
