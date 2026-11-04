"""6. sınıf Sosyal Bilgiler 8. hafta (Ülkemizin Doğal ve Beşerî Çevre Özellikleri Arasındaki İlişki) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def cevre_siniflama_panosu():
    kartlar = [
        ('1. Kart (Beşerî)', 'Atatürk Barajı · Zigana Tüneli · Köprü', MAVI, MAVI_A),
        ('2. Kart (Doğal)', 'Toros Dağları · Çukurova · Fırat Nehri', YES, YES_A),
        ('3. Kart (Doğal)', 'Van Gölü · Erciyes Dağı · Kızılırmak', TUR, TUR_A),
        ('4. Kart (Doğal)', 'Kızılçam · Maki örtüsü · Bafra Ovası', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Doğal ve beşerî çevre unsurlarını içeren dört sınıflandırma kartı.', 22)


def iklim_hayvancilik_karti():
    kartlar = [
        ('İç Anadolu (Bozkır)', 'Koyun (Küçükbaş)', TUR, TUR_A),
        ('? Yöresi (Yaz Yağışı ve Çayır)', 'Sığır (Büyükbaş Mera)', YES, YES_A),
        ('Toroslar (Maki ve Çalı)', 'Kıl Keçisi Yetiştiriciliği', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 82, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 26, renk, renk, 9, 1)
        ic += yazi(x + 94, 25, bas, 12, '#fff')
        ic += yazi(x + 94, 60, alt, 12, LAC)
    return svg(600, 98, ic, 'Bitki örtüsüne göre hayvancılık türleri: bozkır-koyun, çayır-sığır (yöre soru işaretli), maki-kıl keçisi.', 22)


def iklim_bolgeleri_panosu():
    kartlar = [
        ('1. Karadeniz', 'Orman · Ahşap ev · Çay ve fındık', YES, YES_A),
        ('2. Akdeniz', 'Bitki: ? · Taş ev · Ürün: ?', TUR, TUR_A),
        ('3. Karasal', 'Bozkır · Konut: ? · Buğday ve arpa', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 82, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 26, renk, renk, 9, 1)
        ic += yazi(x + 94, 25, bas, 12, '#fff')
        ic += yazi(x + 94, 60, alt, 12, LAC, ince=True)
    return svg(600, 98, ic, 'Karadeniz, Akdeniz ve Karasal iklim bölgelerinin bitki örtüsü, konut ve ürün panosu.', 22)


def daginik_toplu_yerlesme():
    ic = kutu(8, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, 'Doğu Karadeniz: Dağınık Yerleşme', 12, '#fff')
    ic += yazi(150, 52, 'Arazi çok dağlık ve engebelidir', 12, LAC, ince=True)
    ic += yazi(150, 74, 'Su kaynakları her yerde boldur', 12, YES)

    ic += kutu(308, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(450, 25, 'İç Anadolu: Toplu Yerleşme', 12, '#fff')
    ic += yazi(450, 52, 'Arazi geniş ve düzdür (ova · plato)', 12, LAC, ince=True)
    ic += yazi(450, 74, 'Su kaynakları sınırlıdır (su etrafında)', 12, TUR)
    return svg(600, 100, ic, 'Doğu Karadeniz dağınık yerleşme ve İç Anadolu toplu yerleşme karşılaştırma şeması.', 22)


def gap_etkilesim_zinciri():
    adimlar = [
        ('1. Doğal Sorun', 'Yaz kuraklığı ve susuzluk', TUR, TUR_A),
        ('2. Beşerî Yatırım', 'Atatürk Barajı ve kanallar', MAVI, MAVI_A),
        ('3. Tarımsal Artış', 'Pamuk ve mısır bolluğu', YES, YES_A),
        ('4. Ekonomik Sonuç', 'Fabrikalar ve göçün azalması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC, ince=True)
    return svg(600, 96, ic, 'Güneydoğu Anadolu Projesi (GAP) etkileşim basamakları şeması.', 22)


def nufus_yogunlugu_kartlari():
    ic = kutu(8, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, 'Yoğun Nüfuslu Alanlar (Ovalar · Kıyılar)', 12, '#fff')
    ic += yazi(150, 52, 'Çukurova · Bafra · Gediz · Bursa', 12, LAC)
    ic += yazi(150, 74, 'Tarım, sanayi ve ulaşım çok elverişli', 12, YES, ince=True)

    ic += kutu(308, 8, 284, 84, KIR_A, KIR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, KIR, KIR, 9, 1)
    ic += yazi(450, 25, 'Seyrek Nüfuslu Alanlar (Engebeli)', 12, '#fff')
    ic += yazi(450, 52, 'Hakkâri · Tunceli · Menteşe Yöresi', 12, LAC)
    ic += yazi(450, 74, 'Dağlık ve sarp arazi ulaşımı zorlaştırır', 12, KIR, ince=True)
    return svg(600, 100, ic, 'Türkiye’de yoğun nüfuslu ovalar ile seyrek nüfuslu dağlık alanlar karşılaştırması.', 22)


def dogal_beseri_eslesme():
    kartlar = [
        ('1. Rize (Bol Yağış)', '→ Çay tarımının yapılması', YES, YES_A),
        ('2. Uludağ (Kalıcı Kar)', '→ Kış turizminin gelişmesi', MAVI, MAVI_A),
        ('3. Çoruh (Yüksek Eğim)', '→ Rafting ve hidroelektrik', CAM, CAM_A),
        ('4. Konya (Kurak Yaz) (!)', '→ Ormancılık ve balıkçılık (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Doğal çevre ve beşerî faaliyet eşleştirmeleri; 4. Konya kartı hatalı.', 22)


def dogu_karadeniz_projeleri():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, 'Deniz Dolgusu Havalimanları', 12, '#fff')
    ic += yazi(150, 52, 'Ordu–Giresun ve Rize–Artvin', 12, LAC)
    ic += yazi(150, 74, 'Neden: Kıyıda geniş düz arazi yok!', 12, MAVI, ince=True)

    ic += kutu(308, 8, 284, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, MOR, MOR, 9, 1)
    ic += yazi(450, 25, 'Dağları Aşan Karayolu Tünelleri', 12, '#fff')
    ic += yazi(450, 52, 'Zigana ve Ovit Tünelleri', 12, LAC)
    ic += yazi(450, 74, 'Neden: Kıyıya paralel sarp dağlar!', 12, MOR, ince=True)
    return svg(600, 100, ic, 'Deniz dolgusu havalimanları ve dağ tünellerinin yapılma nedenlerini gösteren kartlar.', 22)


def surdurulebilir_cevre_panosu():
    satirlar = [
        ('1. Uygulama', 'Güneş ve rüzgârdan yenilenebilir enerji üretmek', YES, YES_A),
        ('2. Uygulama (!)', 'Verimli tarım ovalarına fabrika ve beton siteler yapmak (?)', KIR, KIR_A),
        ('3. Uygulama', 'Eğimli yamaçları ağaçlandırarak erozyonu önlemek', MAVI, MAVI_A),
        ('4. Uygulama', 'Kurak tarlalarda damla sulama ile su tasarrufu yapmak', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 104, 22, renk, renk, 6, 1)
        ic += yazi(60, y + 15, no, 12, '#fff')
        ic += yazi(120, y + 15, metin, 12, LAC, 'start', ince=(i != 1))
    return svg(600, 112, ic, 'Sürdürülebilir çevre yönetimi panosu; 2. uygulamada verimli ovaların betonlaştırılması yanlış verilmiş.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cevre_siniflama_panosu()
    s[4]['gorsel'] = iklim_hayvancilik_karti()
    s[5]['gorsel'] = iklim_bolgeleri_panosu()
    s[6]['gorsel'] = daginik_toplu_yerlesme()
    s[7]['gorsel'] = gap_etkilesim_zinciri()
    s[8]['gorsel'] = nufus_yogunlugu_kartlari()
    s[9]['gorsel'] = dogal_beseri_eslesme()
    s[11]['gorsel'] = dogu_karadeniz_projeleri()
    s[12]['gorsel'] = surdurulebilir_cevre_panosu()
