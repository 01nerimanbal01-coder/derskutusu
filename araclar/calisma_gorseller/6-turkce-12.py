"""6. sınıf Türkçe 12. hafta (1071’den 1922’ye Tek Millet İki Zafer ve Tema Değerlendirmesi) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115, mm=20):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ikili_kart(b1, s1a, s1b, r1, z1, b2, s2a, s2b, r2, z2, etiket, ar1=False, ar2=False):
    ic = kutu(6, 6, 170, 103, z1, r1)
    ic += yazi(91, 28, b1, r1, kalin=True)
    ic += (ar_yazi(91, 60, s1a, LAC) if ar1 else yazi(91, 58, s1a, LAC, kalin=True))
    ic += yazi(91, 90, s1b, r1)
    ic += kutu(184, 6, 170, 103, z2, r2)
    ic += yazi(269, 28, b2, r2, kalin=True)
    ic += (ar_yazi(269, 60, s2a, LAC) if ar2 else yazi(269, 58, s2a, LAC, kalin=True))
    ic += yazi(269, 90, s2b, r2)
    return svg(ic, etiket)


def dortlu_kart(kartlar, etiket, ar=False):
    konum = [(6, 6), (184, 6), (6, 60), (184, 60)]
    ic = ''
    for (x, y), (b1, b2, r, z) in zip(konum, kartlar):
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += (ar_yazi(x + 85, y + 41, b2, LAC) if ar else yazi(x + 85, y + 39, b2, LAC))
    return svg(ic, etiket)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ikili_kart(
        '26 Ağustos 1071 · Malazgirt', 'Komutan: Sultan Alparslan', 'Unvanı: Yurt Açan Zafer', MAVI, MAVI_A,
        '26-30 Ağustos 1922 · Büyük Taarruz', 'Komutan: Gazi Mustafa Kemal Atatürk', 'Unvanı: Yurt Kurtaran Zafer', YES, YES_A,
        '1071 Malazgirt Zaferi ile 1922 Büyük Taarruz karşılaştırma şeması.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Ağustos sabahı (Nesnel)', 'Tamlanan ekli → Belirtisiz İ.T.', MAVI, MAVI_A),
        ('2. Ordumuzun kararlılığı (Öznel)', 'İki taraf ekli → Belirtili İ.T.', TUR, TUR_A),
        ('3. Malazgirt Zaferi’nin yıl dönümü', '3 isim bağlı → Zincirleme İ.T.', MOR, MOR_A),
        ('4. Kahraman Mehmetçik (Öznel)', 'Niteleme + İsim → Sıfat Tamlaması', YES, YES_A),
    ], 'Tamlama türleri ve nesnel-öznel anlatım inceleme kartları.')
    s[5]['gorsel'] = dortlu_kart([
        ('1. Büyük Taarruz’un (Doğru)', 'Tarihî olay adı büyük + kesme', YES, YES_A),
        ('2. 26 ağustos 1071’de (Yanlış!)', 'Belirli tarihte «Ağustos» büyük olur!', KIR, KIR_A),
        ('3. Kurtuluş Savaşı’nda (Doğru)', 'Tarihî dönem/savaş adı büyük', MAVI, MAVI_A),
        ('4. her yıl eylül ayının (Doğru)', 'Belirli sayı yok → küçük harf', CAM, CAM_A),
    ], 'Tarihlerin ve tarihî olay adlarının yazımı denetim panosu.')
    s[6]['gorsel'] = ikili_kart(
        '1. Metin: Rafadan Tayfa', 'Tür: Çizgi Film (Kurgusal/Öyküleyici)', 'Konu: İstiklâl Marşı ve vatan sevgisi', TUR, TUR_A,
        '2. Metin: 1071’den 1922’ye', 'Tür: Tarihsel Bilgilendirici Metin', 'Konu: Bağımsızlık ve vatan sevgisi', MAVI, MAVI_A,
        'İki farklı metnin tür ve ortak tema açısından metinler arası karşılaştırması.'
    )
    s[7]['gorsel'] = ikili_kart(
        'İncelenen Cümle', '«O, Türk ordusunun sarsılmaz iradesini', 'bütün dünyaya gösterdi.»', MAVI, MAVI_A,
        'Dil Bilgisi İpuçları', 'Zamir: O · Sıfat: sarsılmaz / bütün', 'Belirtili İ.T.: ordusunun iradesi', MOR, MOR_A,
        'Cümle içinde zamir, sıfat tamlaması ve isim tamlaması analizi.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Metni Çözümleme', 'İçeriği ve ana olayı anlama', MAVI, MAVI_A),
        ('2. Bilgileri Ayrıştırma', 'Önemli bilgiyi ayrıntıdan ayırma', TUR, TUR_A),
        ('3. Kronolojik Sıralama', 'Zaman ve düşünce akışına dizme', MOR, MOR_A),
        ('4. Özgün İfade Etme', 'Kendi cümlelerimizle özetleme', YES, YES_A),
    ], 'Yapılandırılmış özetleme sürecinin dört basamağı.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Cümle', 'Sadece zarf ve isimler var', MAVI, MAVI_A),
        ('2. Cümle: Zaferin coşkusu', 'Belirtili İ.T. + Sıfat T. (bütün şehirler)', TUR, TUR_A),
        ('3. Cümle: Milletin sarsılmaz azmi', 'Hem Belirtili İ.T. hem Sıfat T. (bu büyük zafer)', YES, YES_A),
        ('4. Cümle: Onlar ...', 'Kişi zamiri ve zarf kullanımı', MOR, MOR_A),
    ], 'Dört cümlede isim ve sıfat tamlaması karşılaştırma kartları.')
    s[11]['gorsel'] = ikili_kart(
        '1071 Malazgirt: Yurt Açan', 'Anadolu’nun kapılarını Türk', 'milletine ebedî vatan olarak açtı', MAVI, MAVI_A,
        '1922 Büyük Taarruz: Yurt Kurtaran', 'Aynı bağımsızlık ruhuyla vatanı', 'işgalden kurtarıp Cumhuriyet’e taşıdı', YES, YES_A,
        '1071 Yurt Açan Zafer ve 1922 Yurt Kurtaran Zafer özetleme afişi.'
    )
