"""6. sınıf Fen Bilimleri 2. hafta (Güneş Sistemi Modeli, Güneş ve Ay Tutulmaları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def tutulma_k_l_semasi():
    # K şeması: Güneş tutulması
    ic = kutu(8, 6, 282, 98, TUR_A, TUR, 9, 1.6)
    ic += yazi(149, 22, 'K Şeması (Gündüz · Yeni Ay)', 10.8, TUR)
    ic += f'<polygon points="154,52 232,57 232,63 154,68" fill="{LAC}" opacity=".25"/>'
    ic += f'<circle cx="48" cy="60" r="24" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.5"/>' + yazi(48, 64, 'Güneş', 10.2, LAC)
    ic += f'<circle cx="150" cy="60" r="9" fill="{GRI}" stroke="{LAC}" stroke-width="1.2"/>' + yazi(150, 44, 'Ay', 10.2, LAC)
    ic += f'<circle cx="246" cy="60" r="20" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>' + yazi(246, 64, 'Dünya', 10.2, '#fff')
    ic += yazi(149, 94, 'Ay’ın gölgesi Dünya’da dar bölgeye düşer', 10, SOLUK, ince=True)

    # L şeması: Ay tutulması
    ic += kutu(310, 6, 282, 98, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(451, 22, 'L Şeması (Gece · Dolunay)', 10.8, MAVI)
    ic += f'<polygon points="448,42 568,50 568,70 448,78" fill="{LAC}" opacity=".25"/>'
    ic += f'<circle cx="350" cy="60" r="24" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.5"/>' + yazi(350, 64, 'Güneş', 10.2, LAC)
    ic += f'<circle cx="448" cy="60" r="20" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>' + yazi(448, 64, 'Dünya', 10.2, '#fff')
    ic += f'<circle cx="546" cy="60" r="9" fill="{SOLUK}" stroke="{LAC}" stroke-width="1.2"/>' + yazi(546, 44, 'Ay', 10.2, LAC)
    ic += yazi(451, 94, 'Ay, Dünya’nın gölgesi içinde kalır', 10, SOLUK, ince=True)
    return svg(600, 110, ic, 'K şemasında Güneş-Ay-Dünya (Güneş tutulması), L şemasında Güneş-Dünya-Ay (Ay tutulması).', 23)


def model_kontrol_listesi():
    maddeler = [
        ('1. Madde', 'Gezegenler Güneş’e yakınlık sırasıyla dizildi.', 'Doğru', YES, YES_A),
        ('2. Madde', 'Gezegenlerin hacim farkları modele yansıtıldı.', 'Doğru', MAVI, MAVI_A),
        ('3. Madde', 'Asteroit kuşağı Dünya ile Mars arasına konuldu.', 'Doğru (!)', KIR, KIR_A),
        ('4. Madde', 'Gaz devi gezegenlere halkaları eklendi.', 'Doğru', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, m, d, renk, arka) in enumerate(maddeler):
        y = 6 + i * 27
        ic += kutu(8, y, 584, 23, arka, renk, 6, 1.4)
        ic += kutu(8, y, 88, 23, renk, renk, 6, 1)
        ic += yazi(52, y + 15.5, no, 10.4, '#fff')
        ic += yazi(108, y + 15.5, m, 10.3, LAC, 'start', ince=True)
        ic += yazi(578, y + 15.5, d, 10.4, renk, 'end')
    return svg(600, 116, ic, 'Güneş sistemi modeli kontrol listesi; 3. maddede asteroit kuşağı yeri hatalı.', 22)


def karsilastirma_ozet_karti():
    ic = kutu(8, 8, 282, 82, TUR_A, TUR, 9, 1.6)
    ic += yazi(149, 26, 'Güneş Tutulması Özeti', 11, TUR)
    ic += yazi(149, 48, 'Sıralama: Güneş – Ay – Dünya', 10.4, LAC)
    ic += yazi(149, 68, 'Yeni ay evresi · Gündüz · Dar gözlem alanı', 10.2, SOLUK, ince=True)

    ic += kutu(310, 8, 282, 82, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(451, 26, 'Ay Tutulması Özeti', 11, MAVI)
    ic += yazi(451, 48, 'Sıralama: Güneş – Dünya – Ay', 10.4, LAC)
    ic += yazi(451, 68, 'Dolunay evresi · Gece · Geniş gözlem alanı', 10.2, SOLUK, ince=True)
    return svg(600, 98, ic, 'Güneş ve Ay tutulmalarının sıralama, evre, zaman ve alan özeti.', 22)


def sinif_fener_duzenegi():
    ic = kutu(8, 6, 584, 92, '#1c2536', LAC, 10, 1.6)
    ic += yazi(300, 22, 'Karanlık Sınıf Modelleme Düzeneği (Aynı Doğrultu)', 10.8, '#fff')
    # El feneri
    ic += kutu(36, 48, 52, 22, ALTIN, TUR, 4, 1.4) + f'<polygon points="88,48 106,40 106,78 88,70" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.2"/>'
    ic += f'<polygon points="106,42 460,28 460,90 106,76" fill="#fff3b0" opacity=".22"/>'
    ic += yazi(72, 86, 'El Feneri (Güneş)', 10.2, ALTIN)
    # Küçük küre (Ay)
    ic += f'<circle cx="270" cy="59" r="11" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.5"/>'
    ic += f'<polygon points="276,50 442,55 442,63 276,68" fill="#090d16" opacity=".65"/>'
    ic += yazi(270, 86, 'Küçük Küre (Ay)', 10.2, '#fff')
    # Büyük küre (Dünya)
    ic += f'<circle cx="460" cy="59" r="22" fill="{MAVI}" stroke="#fff" stroke-width="1.5"/>'
    ic += f'<circle cx="440" cy="59" r="5" fill="#090d16"/>'
    ic += yazi(460, 92, 'Büyük Küre (Dünya)', 10.2, '#9ec5fe')
    return svg(600, 104, ic, 'Karanlık sınıfta el feneri, ortada küçük köpük küre (Ay) ve sağda büyük köpük küre (Dünya) düzeneği.', 22)


def model_basamaklari_karti():
    kutular = [
        ('Tanımla & Araştır', 'Sorunu bul, veri topla', MAVI, MAVI_A),
        ('Seç & Oluştur', 'Uygun çözümle model kur', TUR, TUR_A),
        ('Test Et & Geliştir', 'Eksikleri sına, düzelt', MOR, MOR_A),
        ('Raporla & Sun', 'Modeli sınıfta paylaş', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kutular):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 76, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 136, 24, renk, renk, 9, 1)
        ic += yazi(x + 68, 24, bas, 10.5, '#fff')
        ic += yazi(x + 68, 56, alt, 10.1, LAC, ince=True)
    return svg(600, 92, ic, 'Bilimsel model oluşturma sürecinin dört ana aşaması.', 22)


def turkiye_2006_tutulma_karti():
    ic = kutu(8, 6, 584, 92, KUM, TUR, 9, 1.6)
    ic += kutu(8, 6, 584, 24, TUR, TUR, 9, 1)
    ic += yazi(300, 22, 'YURDUMUZDA TAM GÜNEŞ TUTULMASI KAYDI · 29 MART 2006', 10.8, '#fff')
    ic += yazi(24, 48, 'İzlenen Hat : Antalya kıyısından başlayıp Ordu’ya uzanan gölge kuşağı', 10.4, LAC, 'start')
    ic += yazi(24, 66, 'Süre ve Hız : Yaklaşık 4 dakika sürdü; gölge saatte ~3250 km hızla ilerledi', 10.4, LAC, 'start', ince=True)
    ic += yazi(24, 84, 'Diğer Tarihler : Önceki tam tutulma 11 Ağustos 1999 · Sonraki 30 Nisan 2060', 10.4, TUR, 'start')
    return svg(600, 104, ic, '29 Mart 2006 Türkiye tam Güneş tutulması bilgi kartı: Antalya-Ordu hattı, 4 dk süre, 1999 ve 2060 tarihleri.', 22)


def uzaklik_karsilastirma_grafigi():
    ic = kutu(8, 6, 282, 88, TUR_A, TUR, 8, 1.5)
    ic += yazi(149, 24, 'K Zamanı (Aynı Doğrultuda)', 10.8, TUR)
    ic += kutu(24, 36, 150, 18, MAVI, MAVI, 4, 1) + yazi(99, 49, 'Ay – Güneş uzaklığı', 10, '#fff')
    ic += kutu(24, 60, 230, 18, LAC, LAC, 4, 1) + yazi(139, 73, 'Dünya – Güneş uzaklığı', 10, '#fff')

    ic += kutu(310, 6, 282, 88, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(451, 24, 'L Zamanı (Aynı Doğrultuda)', 10.8, MAVI)
    ic += kutu(326, 36, 236, 18, MAVI, MAVI, 4, 1) + yazi(444, 49, 'Ay – Güneş uzaklığı', 10, '#fff')
    ic += kutu(326, 60, 166, 18, LAC, LAC, 4, 1) + yazi(409, 73, 'Dünya – Güneş uzaklığı', 10, '#fff')
    return svg(600, 100, ic, 'K zamanında Ay Güneş’e daha yakın; L zamanında Ay Güneş’e Dünya’dan daha uzak.', 22)


def fergani_bettani_karti():
    ic = kutu(8, 8, 282, 84, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(149, 26, 'Fergani (9. Yüzyıl)', 11, MAVI)
    ic += yazi(149, 48, '“Astronominin Özeti” eserinde Güneş ve', 10.3, LAC, ince=True)
    ic += yazi(149, 66, 'Ay tutulma zamanlarını hesapladı.', 10.3, LAC, ince=True)

    ic += kutu(310, 8, 282, 84, YES_A, YES, 9, 1.6)
    ic += yazi(451, 26, 'Bettânî (855–929)', 11, YES)
    ic += yazi(451, 48, 'Halkalı Güneş tutulmasını açıkladı; 1 yılı', 10.3, LAC, ince=True)
    ic += yazi(451, 66, '365 gün 5 sa. 46 dk. 24 sn. olarak ölçtü.', 10.3, LAC, ince=True)
    return svg(600, 98, ic, 'Fergani ve Bettânî’nin tutulmalar ve yıl hesabı üzerine çalışmaları.', 22)


def telif_patent_afisi():
    ic = kutu(8, 8, 584, 82, MOR_A, MOR, 9, 1.6)
    ic += yazi(300, 26, 'ÖZGÜN MODEL VE BULUŞLARI KORUMA KILAVUZU', 10.8, MOR)
    ic += kutu(24, 36, 264, 44, '#fff', MAVI, 6, 1.3)
    ic += yazi(156, 54, '1. Telif Hakkı : Eser ve modelin', 10.3, MAVI)
    ic += yazi(156, 70, 'izinsiz çoğaltılmasını önler.', 10.2, LAC, ince=True)
    ic += kutu(312, 36, 264, 44, '#fff', TUR, 6, 1.3)
    ic += yazi(444, 54, '2. Patent Hakkı : Buluşu üretme,', 10.3, TUR)
    ic += yazi(444, 70, 'kullanma ve satma hakkı verir.', 10.2, LAC, ince=True)
    return svg(600, 96, ic, 'Telif hakkı ve patent hakkı karşılaştırma afişi.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tutulma_k_l_semasi()
    s[4]['gorsel'] = model_kontrol_listesi()
    s[5]['gorsel'] = karsilastirma_ozet_karti()
    s[6]['gorsel'] = sinif_fener_duzenegi()
    s[7]['gorsel'] = model_basamaklari_karti()
    s[8]['gorsel'] = turkiye_2006_tutulma_karti()
    s[9]['gorsel'] = uzaklik_karsilastirma_grafigi()
    s[10]['gorsel'] = fergani_bettani_karti()
    s[12]['gorsel'] = telif_patent_afisi()
