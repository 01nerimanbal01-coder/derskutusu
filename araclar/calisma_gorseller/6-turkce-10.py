"""6. sınıf Türkçe 10. hafta (Rafadan Tayfa - İstiklâl Marşı, Görsel-İşitsel Yorumlama, İsim Tamlamaları ve Zamirler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.1, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def tamlama_cesitleri_kartlari():
    kartlar = [
        ('1. Kart (Zincirleme)', 'Türk milletinin bağımsızlık coşkusu', YES, YES_A),
        ('2. Kart (Araya Sıfat)', 'Şanlı (S) bayrağın al (S) rengi', MAVI, MAVI_A),
        ('3. Kart (Sıfatlı)', 'Kahraman (S) ordunun büyük (S) zaferi', TUR, TUR_A),
        ('4. Kart (Sıfatlı)', 'Soğuk (S) kış gecesinin sessizliği', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 9.8, r)
        ic += yazi(x + 86, y + 31, alt, 8.8, LAC, ince=True)
    return svg(360, 94, ic, 'Zincirleme isim tamlaması ile sıfat almış tamlamaları ayırt etme kartları.', 16)


def zamir_turleri_panosu():
    kartlar = [
        ('1. Ben ve o', 'Kişi zamiri', MAVI, MAVI_A),
        ('2. Bunu aldım', 'İşaret zamiri (?)', YES, YES_A),
        ('3. Bazıları geldi', 'Belgisiz zamir (?)', TUR, TUR_A),
        ('4. Kim birinci?', 'Soru zamiri (?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'Sözcük hâlindeki dört zamir türünü gösteren pano.', 15)


def o_sozcugu_gorev_panosu():
    kartlar = [
        ('I. Cümle', '“O, İstiklâl Marşı’nı coşkuyla okudu.” (İnsan)', MAVI, MAVI_A),
        ('II. Cümle', '“Onu dikkatlice kitaplığın rafına koydum.” (Nesne)', YES, YES_A),
        ('III. Cümle', '“O gün mecliste büyük bir heyecan vardı.” (+İsim)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        y = 4 + i * 29
        ic += kutu(6, y, 348, 25, z, r, 6, 1.3)
        ic += yazi(48, y + 16, bas, 9.6, r)
        ic += yazi(210, y + 16, alt, 9.1, LAC, ince=True)
    return svg(360, 92, ic, 'O sözcüğünün kişi zamiri, işaret zamiri ve işaret sıfatı görevleri.', 16)


def mehmet_akif_bilgi_kartlari():
    kartlar = [
        ('1. Ödül Reddi', 'Para ödülü yüzünden başta katılmadı', MAVI, MAVI_A),
        ('2. Taceddin D.', 'Hamdullah Suphi Bey’in ricasıyla yazdı', YES, YES_A),
        ('3. Bağış', '500 lirayı Darülmesai’ye bağışladı', TUR, TUR_A),
        ('4. İthaf', 'Kahraman Ordumuza armağan etti', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 9.9, r)
        ic += yazi(x + 86, y + 31, alt, 8.9, LAC, ince=True)
    return svg(360, 94, ic, 'Mehmet Âkif Ersoy ve İstiklâl Marşı’nın yazılış süreci kartları.', 16)


def ilgi_zamiri_ki_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Sıfat Yapan -ki', 10.0, MAVI)
    ic += yazi(91, 44, '“mahalledeki tören”', 9.8, LAC)
    ic += yazi(91, 64, 'Hangi tören? → İsmi niteler', 9.1, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. İlgi Zamiri Olan -ki', 10.0, MOR)
    ic += yazi(269, 44, '“bizimki (= bizim törenimiz)”', 9.6, LAC)
    ic += yazi(269, 64, 'Düşen tamlanan ismin yerini tutar', 8.9, MOR, ince=True)
    return svg(360, 88, ic, 'Sıfat yapan -ki ile ilgi zamiri olan -ki ayrımı kartı.', 15)


def istiklal_marsi_kronoloji():
    adimlar = [
        ('1. Yarışma', 'Maarif Vekâleti ilanı', MAVI, MAVI_A),
        ('2. Yazılış', 'Taceddin Dergâhı', TUR, TUR_A),
        ('3. Kabul', '12 Mart 1921 TBMM', YES, YES_A),
        ('4. Bağış', 'Darülmesai’ye bağış', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += yazi(x + 41, 54, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'İstiklâl Marşı’nın yazılış ve kabul süreci kronolojisi.', 15)


def gorsel_isitsel_analiz_panosu():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'İşitsel Unsurlar (Ses ve Müzik)', 9.7, CAM)
    ic += yazi(91, 44, '• Gür ses tonu ve doğru vurgu', 9.1, LAC, ince=True)
    ic += yazi(91, 64, '• Coşkulu fon müziği → Heyecan', 9.1, CAM)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Görsel Unsurlar (Beden Dili)', 9.7, YESIL_K)
    ic += yazi(269, 44, '• Gururlu ve kararlı bakışlar', 9.1, LAC, ince=True)
    ic += yazi(269, 64, '• Dalgalanan al bayrak → Saygı', 9.1, YESIL_K)
    return svg(360, 88, ic, 'Dinleme/izleme içeriğindeki görsel ve işitsel unsurlar panosu.', 15)


def belirtili_belirtisiz_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Belirtisiz İsim Tamlaması', 9.8, TUR)
    ic += yazi(91, 44, 'vatan (eksiz) + toprağ-ı (-ı)', 9.4, LAC)
    ic += yazi(91, 64, 'Tamlayan ek almamış, tamlanan almış', 8.9, TUR, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Belirtili İsim Tamlaması', 9.8, YESIL_K)
    ic += yazi(269, 44, 'vatan-ın (-ın) + toprağ-ı (-ı)', 9.4, LAC)
    ic += yazi(269, 64, 'Hem tamlayan hem tamlanan ek almış', 8.9, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Belirtisiz ve belirtili isim tamlaması ek karşılaştırma kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tamlama_cesitleri_kartlari()
    s[2]['gorsel'] = zamir_turleri_panosu()
    s[5]['gorsel'] = o_sozcugu_gorev_panosu()
    s[6]['gorsel'] = mehmet_akif_bilgi_kartlari()
    s[7]['gorsel'] = ilgi_zamiri_ki_karti()
    s[8]['gorsel'] = istiklal_marsi_kronoloji()
    s[9]['gorsel'] = gorsel_isitsel_analiz_panosu()
    s[11]['gorsel'] = belirtili_belirtisiz_karti()
