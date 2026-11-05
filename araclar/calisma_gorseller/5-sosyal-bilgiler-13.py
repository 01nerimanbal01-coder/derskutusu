"""5. sınıf Sosyal Bilgiler 13. hafta (Komşularımızla İlişkiler ve Ortak Miras Ögeleri) görselleri.
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
    s[1]['gorsel'] = dortlu_kart([
        ('Batı: Bulgaristan & Yunanistan', 'Kapıkule ve İpsala Sınır Kapıları', MAVI, MAVI_A),
        ('Kuzeydoğu: Gürcistan & Nahçıvan', 'Sarp ve Dilucu Sınır Kapıları', YES, YES_A),
        ('Doğu: İran', 'Gürbulak Sınır Kapısı', TUR, TUR_A),
        ('Güney: Irak & Suriye', 'Habur ve Cilvegözü Kapıları', MOR, MOR_A),
    ], 'Türkiye’nin komşu ülkeleri ve başlıca sınır kapıları.')
    s[2]['gorsel'] = dortlu_kart([
        ('1. Göbeklitepe (Şanlıurfa)', 'Taşınmaz Somut Kültürel Miras', TUR, TUR_A),
        ('2. Pamukkale - Hierapolis', 'Doğal + Kültürel → Karma Miras', CAM, CAM_A),
        ('3. Karagöz ve Ebru Sanatı', 'Somut Olmayan Kültürel Miras', MOR, MOR_A),
        ('4. Divriği Ulu Camii (Sivas)', 'Taşınmaz Somut Kültürel Miras', YES, YES_A),
    ], 'Türkiye’deki somut, somut olmayan ve karma miras örnekleri.')
    s[5]['gorsel'] = ikili_kart(
        'Türkiye’nin İhracatı (Dış Satım)', 'Otomotiv · Makine · Beyaz Eşya', 'Tekstil · Demir-Çelik · Gıda', YES, YES_A,
        'Türkiye’nin İthalatı (Dış Alım)', 'Ham Petrol · Doğal Gaz', 'Enerji Hammaddeleri (İran, Irak, Az.)', TUR, TUR_A,
        'Türkiye’nin komşu ülkelerle ihracat ve ithalat ürünleri.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('1. Efes Antik Kenti (İzmir)', 'Somut Miras (Antik Mimari)', MAVI, MAVI_A),
        ('2. Selimiye Camii (Edirne)', 'Somut Miras (Mimar Sinan Eseri)', YES, YES_A),
        ('3. Çini ve Ebru Sanatı', 'Somut Olmayan Miras (El Sanatı)', MOR, MOR_A),
        ('4. Nemrut Dağı (Adıyaman)', 'Somut Miras (Anıt Heykeller)', TUR, TUR_A),
    ], 'Somut ve somut olmayan kültürel miras örneklerinin ayrımı.')
    s[7]['gorsel'] = ikili_kart(
        'Doğal Oluşum Boyutu', 'Peri Bacaları (Kapadokya)', 'Beyaz Travertenler (Pamukkale)', CAM, CAM_A,
        'Kültürel / Tarihi Boyutu', 'Kaya Kiliseleri ve Yeraltı Şehirleri', 'Hierapolis Antik Kenti', TUR, TUR_A,
        'Karma miras alanlarının doğal ve kültürel bileşenleri.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Azerbaycan (Doğu Başlangıç)', 'Bakü — Hazar Enerji ve Demiryolu', YES, YES_A),
        ('2. Gürcistan (Kafkasya Geçişi)', 'Tiflis — Ara Bağlantı Ülkesi', MAVI, MAVI_A),
        ('3. Türkiye (Anadolu Köprüsü)', 'Kars → Eskişehir → Edirne Hattı', TUR, TUR_A),
        ('4. Yunanistan / Bulgaristan', 'Avrupa’ya Açılan Batı Kapısı', MOR, MOR_A),
    ], 'TANAP ve Bakü-Tiflis-Kars koridorunun doğudan batıya güzergâhı.')
    s[9]['gorsel'] = dortlu_kart([
        ('Müzeleri Kurallı Gezmek (✓)', 'Mirasımızı tanıma ve koruma', YES, YES_A),
        ('Duvarlara İsim Kazımak (✗)', 'Tarihi dokuya zarar verir (Yanlış!)', KIR, KIR_A),
        ('El Sanatlarını Yaşatmak (✓)', 'Kuşaktan kuşağa aktarım', MAVI, MAVI_A),
        ('Okul Projeleriyle Tanıtmak (✓)', 'Ortak bilinç oluşturma', CAM, CAM_A),
    ], 'Kültürel mirası koruma bilinci doğru ve yanlış tutumlar.')
    s[11]['gorsel'] = ikili_kart(
        'Kıtalararası Köprü Türkiye', 'Asya · Avrupa · Orta Doğu Kesişimi', '8 Kara Komşusu ve Sınır Kapıları', MAVI, MAVI_A,
        'Ticaret ve Enerji Koridoru', 'TANAP · BTC · Demir İpek Yolu', 'Bölgesel Barış ve Ekonomik İş Birliği', YES, YES_A,
        'Türkiye’nin jeopolitik konumu ile enerji ve ulaşım koridoru rolü.'
    )
