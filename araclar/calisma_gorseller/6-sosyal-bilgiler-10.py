"""6. sınıf Sosyal Bilgiler 10. hafta (Ülkemizin Doğal ve Beşerî Çevre Özellikleri Arasındaki İlişki ve 2. Öğrenme Alanı Değerlendirmesi) çalışma kâğıdı görselleri.
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


def yerlesme_konut_kartlari():
    kartlar = [
        ('1. Kart · D. Karadeniz', 'Engebe, orman → Dağınık, ahşap', YES, YES_A),
        ('2. Kart · İç Anadolu (!)', 'Orman, bol su → Dağınık, ahşap', KIR, KIR_A),
        ('3. Kart · Akdeniz (!)', 'Bozkır → Dağınık, kerpiç ev', TUR, TUR_A),
        ('4. Kart · G.Doğu (!)', 'Bol yağış → Dağınık, taş ev', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 9.8, r)
        ic += yazi(x + 86, y + 31, alt, 8.9, LAC, ince=True)
    return svg(360, 94, ic, 'Bölgelere göre yerleşme dokusu ve konut tipi kartları.', 16)


def sanayi_hammadde_panosu():
    kartlar = [
        ('1. Konya', 'Buğday → Un sanayi', MAVI, MAVI_A),
        ('2. Adana', 'Pamuk (?) → Dokuma (?)', YES, YES_A),
        ('3. Zonguldak', 'Taş kömürü → ? sanayi', TUR, TUR_A),
        ('4. B. Karadeniz', 'Orman (?) → Kâğıt/Kereste', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.7, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 8.6, LAC, ince=True)
    return svg(360, 84, ic, 'Şehirlerde ham maddeye bağlı gelişen sanayi kolları panosu.', 15)


def cografi_konum_panosu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Mutlak (Matematik) Konum', 9.9, MAVI)
    ic += yazi(91, 44, '• 36°–42° Kuzey paralelleri', 9.2, LAC, ince=True)
    ic += yazi(91, 64, '• Orta kuşak → Dört mevsim', 9.2, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'Göreceli (Özel) Konum', 9.9, TUR)
    ic += yazi(269, 44, '• Üç kıta kavşağı ve boğazlar', 9.2, LAC, ince=True)
    ic += yazi(269, 64, '• Batıdan doğuya artan yükselti', 9.2, TUR)
    return svg(360, 88, ic, 'Mutlak ve göreceli konum sonuçları karşılaştırma panosu.', 15)


def muhendislik_projeleri_kartlari():
    kartlar = [
        ('A · Boğaz Köprüleri', 'Kıtalar arası ulaşım', MAVI, MAVI_A),
        ('B · Ovit ve Zigana', 'Dağları aşan kara yolu tüneli', TUR, TUR_A),
        ('C · GAP ve Atatürk B.', 'Tarımsal sulama ve pamuk', YES, YES_A),
        ('D · Ordu-Giresun H.', 'Deniz dolgulu havalimanı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 9.8, r)
        ic += yazi(x + 86, y + 31, alt, 9.1, LAC, ince=True)
    return svg(360, 94, ic, 'Dört beşerî mühendislik projesinin amaç kartları.', 16)


def nufus_dagilisi_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Yoğun Nüfuslu Alanlar', 9.9, YESIL_K)
    ic += yazi(91, 44, 'Çukurova ve Marmara Kıyıları:', 9.2, LAC)
    ic += yazi(91, 64, 'Ilıman iklim, düz ova, sanayi', 9.1, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Seyrek Nüfuslu Alanlar', 9.9, MOR)
    ic += yazi(269, 44, 'Hakkâri ve Tunceli Çevresi:', 9.2, LAC)
    ic += yazi(269, 64, 'Yüksek engebeli yer şekli, soğuk', 9.1, MOR, ince=True)
    return svg(360, 88, ic, 'Yoğun ve seyrek nüfuslu bölgelerin coğrafi nedenleri kartı.', 15)


def pamuk_uretim_zinciri():
    adimlar = [
        ('1. Tarım', 'Çukurova’da hasat', YES, YES_A),
        ('2. Ulaşım', 'Fabrikaya taşıma', MAVI, MAVI_A),
        ('3. Sanayi', 'Dokuma ve giyim', TUR, TUR_A),
        ('4. Ticaret', 'Pazar ve ihracat', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 54, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'Pamuğun tarladan fabrikaya ve pazara uzanan üretim zinciri.', 15)


def surdurulebilir_cevre_panosu():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Doğayla Uyumlu Planlama (✓)', 9.8, YESIL_K)
    ic += yazi(91, 44, '• Ovaları tarıma ayırmak', 9.2, LAC, ince=True)
    ic += yazi(91, 64, '• Güneş ve rüzgâr enerjisi', 9.2, YESIL_K)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'Doğal Dengeye Zarar (!)', 9.8, KIR)
    ic += yazi(269, 44, '• Verimli tarım ovalarını', 9.2, LAC, ince=True)
    ic += yazi(269, 64, 'betonlaştırıp imara açmak', 9.2, KIR)
    return svg(360, 88, ic, 'Sürdürülebilir çevre ve yanlış arazi kullanımı karşılaştırması.', 15)


def daglar_ulasim_semasi():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'TÜRKİYE’DE DAĞLARIN UZANIŞI VE ULAŞIM YÖNÜ', 10.1, CAM)
    ic += yazi(180, 44, 'Kuzey Anadolu ve Toros Dağları: Doğu – Batı doğrultusunda uzanır.', 9.3, LAC)
    ic += yazi(180, 64, 'Sonuç: Doğu-Batı ulaşımı kolay  |  Kuzey-Güney ulaşımı: Geçit ve Tünel', 9.2, CAM, ince=True)
    return svg(360, 88, ic, 'Dağların doğu-batı uzanışının ulaşım hatlarına etkisi şeması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yerlesme_konut_kartlari()
    s[2]['gorsel'] = sanayi_hammadde_panosu()
    s[5]['gorsel'] = cografi_konum_panosu()
    s[6]['gorsel'] = muhendislik_projeleri_kartlari()
    s[7]['gorsel'] = nufus_dagilisi_karti()
    s[8]['gorsel'] = pamuk_uretim_zinciri()
    s[9]['gorsel'] = surdurulebilir_cevre_panosu()
    s[11]['gorsel'] = daglar_ulasim_semasi()
