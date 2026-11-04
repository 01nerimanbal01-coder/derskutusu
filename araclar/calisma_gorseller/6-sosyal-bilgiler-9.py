"""6. sınıf Sosyal Bilgiler 9. hafta (Ülkemizin Doğal ve Beşerî Çevre Özellikleri Arasındaki İlişki) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yerlesme_konut_kartlari():
    kartlar = [
        ('1. Rize Kırsalı', 'Dağınık · Ahşap ev', YES, YES_A),
        ('2. Konya Kırsalı', 'Toplu · Kerpiç ev', TUR, TUR_A),
        ('3. Nevşehir Kırsalı', 'Toplu · Taş (tüf) ev', MAVI, MAVI_A),
        ('4. Şanlıurfa (!)', 'Dağınık · Ahşap ev (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, icerik, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Dört yörenin kırsal yerleşme dokusu ve konut yapı malzemesi kartları.', 16)


def nufus_analiz_panosu():
    yoreler = [
        ('1. Çukurova', 'Verimli delta · Sanayi', YES, YES_A),
        ('2. Hakkâri', 'Sarp dağlar · Sert kış', KIR, KIR_A),
        ('3. Zonguldak', 'Taş kömürü · Liman', MAVI, MAVI_A),
        ('4. Menteşe', 'Engebeli dağlık kıyı', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(yoreler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'Çukurova, Hakkâri, Zonguldak ve Menteşe nüfus yoğunluğu etkenleri.', 15)


def doga_insan_etkilesim_kartlari():
    ornekler = [
        ('I. Rize Çay Tarımı', 'Yağışlı iklim etkisi', MAVI, MAVI_A),
        ('II. Uludağ Kış Turizmi', 'Yükselti ve kar etkisi', MOR, MOR_A),
        ('III. Atatürk Barajı (GAP)', 'Beşerî mühendislik!', YES, YES_A),
        ('IV. Konya Tahıl Tarımı', 'Bozkır iklimi etkisi', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(ornekler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Doğanın insana etkisi ve insanın doğayı şekillendirmesi örnekleri.', 16)


def iklim_ekonomi_semasi():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'Akdeniz Kıyı Kuşağı', 10.2, TUR)
    ic += yazi(91, 43, 'Kışlar ılık · Güneşli gün çok', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'Ekonomik Faaliyet: [ K = ? ]', 9.6, TUR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Doğu Karadeniz Kıyısı', 10.2, YESIL_K)
    ic += yazi(269, 43, 'Her mevsim yağış · Gür orman', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'Ekonomik Faaliyet: [ L = ? ]', 9.6, YESIL_K)
    return svg(360, 88, ic, 'Akdeniz (K) ve Doğu Karadeniz (L) iklimlerinin ekonomik faaliyetlere etkisi.', 15)


def gap_etkilesim_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'GAP Öncesi (Kurak Ova)', 10.1, TUR)
    ic += yazi(91, 44, 'Sulama yetersiz · Verim düşük', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'Mevsimlik dış göç fazla', 9.5, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'GAP Sonrası (Sulama Kanalı)', 10.0, YESIL_K)
    ic += yazi(269, 44, 'Fırat ve Dicle suları ulaştı', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'Tarım, sanayi ve nüfus etkisi = ?', 9.3, YESIL_K)
    return svg(360, 88, ic, 'Güneydoğu Anadolu Projesi (GAP) öncesi ve sonrası değişim kartı.', 15)


def pamuk_uretim_zinciri():
    adimlar = [
        ('1. Tarım', 'Çukurova’da pamuk', YES, YES_A),
        ('2. Ulaşım', 'Fabrikaya taşıma', MAVI, MAVI_A),
        ('3. Sanayi', 'Kumaş ve giyim', TUR, TUR_A),
        ('4. Ticaret', 'Mağazada satış', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Pamuğun tarladan ticarete ekonomik faaliyet zinciri.', 15)


def surdurulebilirlik_raporu():
    maddeler = [
        ('Ulaşım Mühendisliği', 'Ovit ve Zigana tünelleri (Uygun)', YES, YES_A),
        ('Yenilenebilir Enerji', 'Güneş ve rüzgâr santrali (Uygun)', MAVI, MAVI_A),
        ('Yamaç Koruma', 'Ağaçlandırma ve teraslama (Uygun)', CAM, CAM_A),
        ('Dere Yatağı İmarı (!)', 'Dere yatağına bina yapmak (Yanlış!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(maddeler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 9.9, r)
        ic += yazi(x + 86, y + 31, alt, 9.1, LAC, ince=True)
    return svg(360, 94, ic, 'Sürdürülebilir çevre uygulamaları ve yanlış arazi kullanımı panosu.', 16)


def izmir_tunceli_karsilastirma():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'İzmir (Kıyı Ege)', 10.3, YESIL_K)
    ic += yazi(91, 44, 'Ilıman iklim · Gediz ve Menderes', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 'Doğal liman · Sanayi · Ticaret', 9.5, YESIL_K)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'Tunceli (Doğu Anadolu)', 10.3, MOR)
    ic += yazi(269, 44, 'Yüksek dağlık · Sert kış iklimi', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'Engebeli arazi · Kısıtlı sanayi', 9.5, MOR)
    return svg(360, 88, ic, 'İzmir ve Tunceli illerinin doğal ve beşerî özellik karşılaştırma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yerlesme_konut_kartlari()
    s[2]['gorsel'] = nufus_analiz_panosu()
    s[5]['gorsel'] = doga_insan_etkilesim_kartlari()
    s[6]['gorsel'] = iklim_ekonomi_semasi()
    s[7]['gorsel'] = gap_etkilesim_karti()
    s[8]['gorsel'] = pamuk_uretim_zinciri()
    s[9]['gorsel'] = surdurulebilirlik_raporu()
    s[11]['gorsel'] = izmir_tunceli_karsilastirma()
