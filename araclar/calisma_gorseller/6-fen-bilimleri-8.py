"""6. sınıf Fen Bilimleri 8. hafta (Bitkilerde Üreme, Büyüme ve Gelişme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def cicek_gorev_panosu():
    kartlar = [
        ('1. Yumurtalık', 'Tohum taslağı ve yumurta taşır', YES, YES_A),
        ('2. Çanak Yaprak (!)', 'Polen üretip yayar (?)', KIR, KIR_A),
        ('3. Sapçık (!)', 'Etlenerek meyveyi oluşturur (?)', TUR, TUR_A),
        ('4. Dişicik Borusu (!)', 'Topraktan su ve mineral emer (?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Çiçek kısımları görev panosu: yalnız 1. yumurtalık kartı doğru verilmiş.', 22)


def dollenme_donusum_semasi():
    adimlar = [
        ('Zigot', 'Gelişir → K = ?', MAVI, MAVI_A),
        ('Tohum Taslağı', 'Dönüşür → L = ?', YES, YES_A),
        ('Yumurtalık', 'Etlenir → M = ?', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 80, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 26, renk, renk, 9, 1)
        ic += yazi(x + 94, 25, bas, 12, '#fff')
        ic += yazi(x + 94, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Döllenme sonrasında zigot (K), tohum taslağı (L) ve yumurtalığın (M) dönüştüğü yapılar şeması.', 22)


def cimlenme_kaplari():
    kaplar = [
        ('1. Kap (Tam)', 'Su var · 25 °C · Hava var', YES, YES_A),
        ('2. Kap (Kuru)', 'Su yok · 25 °C · Hava var', TUR, TUR_A),
        ('3. Kap (Soğuk)', 'Su var · 0 °C · Hava var', MAVI, MAVI_A),
        ('4. Kap (Havasız)', 'Su var · 25 °C · Hava yok', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, kosul, renk, arka) in enumerate(kaplar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, kosul, 12, LAC, ince=True)
    return svg(600, 96, ic, 'SOS çimlenme koşullarını test eden 1, 2, 3 ve 4 numaralı deney kapları.', 22)


def cenek_kutle_grafigi():
    ic = kutu(8, 6, 584, 96, KUM, GRI, 9, 1.5)
    ic += yazi(176, 23, 'Çenek Kütlesi – Zaman Grafiği', 12, TUR)
    ic += f'<line x1="48" y1="86" x2="296" y2="86" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="48" y1="86" x2="48" y2="32" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="56" y1="38" x2="276" y2="78" stroke="{TUR}" stroke-width="2.6"/>'
    ic += yazi(168, 98, 'İlk yaprak çıkana dek geçen zaman', 12, LAC, ince=True)

    ic += kutu(320, 18, 256, 70, YES_A, YES, 8, 1.5)
    ic += yazi(448, 38, 'Gözlem Notu:', 12, YES)
    ic += yazi(448, 58, 'Çimlenmede henüz yaprak yoktur;', 12, LAC, ince=True)
    ic += yazi(448, 76, 'embriyo çenek besinini kullanır.', 12, LAC)
    return svg(600, 108, ic, 'Çimlenme süresince çenek kütlesinin azalmasını gösteren grafik.', 22)


def hayat_dongusu_sema():
    adimlar = [
        ('1. Tozlaşma', 'Polen → Dişicik tepesi', MAVI, MAVI_A),
        ('2. Döllenme', 'Sperm ve Yumurta → Zigot', YES, YES_A),
        ('3. Tohum ve Meyve', 'Taslak → Tohum · Yumurtalık → Meyve', TUR, TUR_A),
        ('4. Çimlenme', 'SOS ile genç bitki oluşumu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Çiçekli bitkilerde tozlaşma, döllenme, tohum-meyve ve çimlenme döngüsü.', 22)


def karanlik_aydinlik_deneyi():
    ic = kutu(8, 8, 284, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MOR, MOR, 9, 1)
    ic += yazi(150, 25, 'K Düzeneği (Karanlık Dolap)', 12, '#fff')
    ic += yazi(150, 52, 'Nemli pamuk · 25 °C · Oksijen var', 12, LAC, ince=True)
    ic += yazi(150, 74, 'Işık: Yok (Karanlık) → Çimlenir!', 12, MOR)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, 'L Düzeneği (Aydınlık Pencere Önü)', 12, '#fff')
    ic += yazi(450, 52, 'Nemli pamuk · 25 °C · Oksijen var', 12, LAC, ince=True)
    ic += yazi(450, 74, 'Işık: Var (Güneşli) → Çimlenir!', 12, YES)
    return svg(600, 100, ic, 'Karanlık ve aydınlık ortamda SOS koşulları sağlanan K ve L çimlenme düzenekleri.', 22)


def tohum_yayilma_kartlari():
    kartlar = [
        ('1. Kart: Rüzgâr', 'Karahindiba tüyleriyle uçar', MAVI, MAVI_A),
        ('2. Kart: Hayvan Postu', 'Pıtrak dikeni kürklerle taşınır', TUR, TUR_A),
        ('3. Kart: Etli Meyve', 'Kiraz ve böğürtlen kuşlarla yayılır', YES, YES_A),
        ('4. Kart (!)', 'Tohumlar hiçbir yere taşınamaz (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Tohumların yayılma yollarını gösteren dört kart.', 22)


def cimlenme_buyume_panosu():
    ic = kutu(8, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(150, 25, 'I. Evre: Çimlenme (Yaprak Yok)', 12, '#fff')
    ic += yazi(150, 52, 'Gerekli: Su · Oksijen · Uygun Sıcaklık', 12, LAC, ince=True)
    ic += yazi(150, 74, 'Fotosentez yok · Işık gerekmez', 12, TUR)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, 'II. Evre: Genç Bitki (Yeşil Yapraklı)', 12, '#fff')
    ic += yazi(450, 52, 'Gerekli: Işık · Karbondioksit · Su · Toprak', 12, LAC, ince=True)
    ic += yazi(450, 74, 'Fotosentez başlar · Besin üretilir', 12, YES)
    return svg(600, 100, ic, 'Çimlenme evresi ile yeşil yapraklı büyüme evresinin karşılaştırma panosu.', 22)


def erkek_disi_organ_karti():
    satirlar = [
        ('1. Bilgi', 'Erkek organ → Başçık (polen üretir) ve Sapçık', MAVI, MAVI_A),
        ('2. Bilgi (!)', 'Döllenme → Erkek organın sapçık kısmında olur (?)', KIR, KIR_A),
        ('3. Bilgi', 'Dişicik Borusu → Poleni yumurtalığa ileten kanal', YES, YES_A),
        ('4. Bilgi', 'Tohum Taslağı → Döllenme sonrası tohuma dönüşür', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 92, 22, renk, renk, 6, 1)
        ic += yazi(54, y + 15, no, 12, '#fff')
        ic += yazi(110, y + 15, metin, 12, LAC, 'start', ince=(i != 1))
    return svg(600, 112, ic, 'Erkek ve dişi organ bilgileri kartı; 2. bilgide döllenme yeri yanlış verilmiş.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cicek_gorev_panosu()
    s[4]['gorsel'] = dollenme_donusum_semasi()
    s[5]['gorsel'] = cimlenme_kaplari()
    s[6]['gorsel'] = cenek_kutle_grafigi()
    s[7]['gorsel'] = hayat_dongusu_sema()
    s[8]['gorsel'] = karanlik_aydinlik_deneyi()
    s[9]['gorsel'] = tohum_yayilma_kartlari()
    s[11]['gorsel'] = cimlenme_buyume_panosu()
    s[12]['gorsel'] = erkek_disi_organ_karti()
