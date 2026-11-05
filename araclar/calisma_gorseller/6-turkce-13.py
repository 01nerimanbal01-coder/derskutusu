"""6. sınıf Türkçe 13. hafta (Ova Çocuk Metni, Beden Dili ve Sözcük Hâlindeki Zamirler) görselleri.
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
        ('1. «O kitabı okudum.»', 'İsimden önce → İşaret Sıfatı', TUR, TUR_A),
        ('2. «O, çalışkan bir öğrencidir.»', 'İnsan yerine → Kişi Zamiri (✓)', YES, YES_A),
        ('3. «O, alt dolaba konuldu.»', 'Cansız eşya yerine → İşaret Zamiri', MAVI, MAVI_A),
        ('4. «O sokakta konaklar var.»', 'İsimden önce → İşaret Sıfatı', MOR, MOR_A),
    ], '«O» sözcüğünün kişi zamiri, işaret zamiri ve işaret sıfatı ayrımı.')
    s[2]['gorsel'] = ikili_kart(
        'Sıfat (İsimden Önce Gelir)', 'Bu dergi · Şu elma · Bazı turistler', 'İsmi belirtir → Ön Ad (Sıfat)', TUR, TUR_A,
        'Zamir (İsmin Yerini Tutar)', 'Bunu · Şunu · Bazıları · Hangisi', 'İsim düşer, yerini tutar → Adıl (Zamir)', YES, YES_A,
        'İşaret, belgisiz ve soru sözcüklerinde sıfat ve zamir farkı.'
    )
    s[5]['gorsel'] = dortlu_kart([
        ('1. «...dün akşam mı izlediniz?»', 'mı → Soru Eki', MAVI, MAVI_A),
        ('2. «...eşyalardan hangisini koydun?»', 'hangisini → Soru Zamiri (✓)', YES, YES_A),
        ('3. «Kaç öğrenci katılacak?»', 'Kaç + isim → Soru Sıfatı', TUR, TUR_A),
        ('4. «...kütüphaneye nasıl gittiler?»', 'nasıl + fiil → Soru Zarfı', MOR, MOR_A),
    ], 'Soru zamiri ile soru sıfatı, soru zarfı ve soru eki ayrımı.')
    s[6]['gorsel'] = ikili_kart(
        'Karşılaştırma Cümlesi', 'Göçebe çadırları ↔ Şehirdeki taş evler', 'Benzerlik ve farklılık yönünden kıyaslama', MAVI, MAVI_A,
        'Çoklu Ortam ve Beden Dili', 'Fotoğraf ve harita anlamı somutlaştırır', 'Jest ve mimik iletişimi güçlendirir', CAM, CAM_A,
        'Metinde karşılaştırma yolu ile çoklu ortam ve beden dili unsurları.'
    )
    s[7]['gorsel'] = dortlu_kart([
        ('Cümle Analizi', '«Biz dün burasını temizledik,', MAVI, MAVI_A),
        ('Devamı', 'herkes görevini özenle yaptı.»', CAM, CAM_A),
        ('1. ve 2. Zamir', 'Biz (Kişi) · burasını (İşaret)', YES, YES_A),
        ('3. Zamir', 'herkes (Belgisiz Zamir)', MOR, MOR_A),
    ], 'Tek cümlede kişi, işaret ve belgisiz zamirlerin tespiti.')
    s[8]['gorsel'] = dortlu_kart([
        ('1. Bölüm: Serim (Giriş)', 'Kişi (Tayan) ve yer (ova) tanıtımı', MAVI, MAVI_A),
        ('2. Bölüm: Düğüm (Olay Başlangıcı)', 'Gezgin fotoğrafçının obaya gelişi', TUR, TUR_A),
        ('3. Bölüm: Düğüm (Merak Unsurları)', 'Dünya albümünün merak uyandırması', MOR, MOR_A),
        ('4. Bölüm: Çözüm (Sonuç ve İleti)', 'Farklı kültürlerin ufku genişletmesi', YES, YES_A),
    ], 'Öyküleyici metnin serim, düğüm ve çözüm bölümleri akışı.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Kart: Siz, orada, ben', 'Kişi ve işaret zamirleri var', YES, YES_A),
        ('2. Kart: hepsi, hangisini', 'Belgisiz ve soru zamirleri var', MAVI, MAVI_A),
        ('3. Kart: Güzel havalarda... (✗)', 'Sıfat ve isim var, zamir yok!', KIR, KIR_A),
        ('4. Kart: Kimse, bunu, bana', 'Belgisiz, işaret ve kişi zamiri var', CAM, CAM_A),
    ], 'Dört cümle kartında zamir varlığının incelenmesi.')
    s[11]['gorsel'] = ikili_kart(
        '1. Görev: «Şu» → İşaret Sıfatı', 'Kural: «Şu + İsim» (Örn: Şu kitap)', 'İsmin önüne gelerek işaret eder', TUR, TUR_A,
        '2. Görev: «Şu» → İşaret Zamiri', 'Kural: «Şu / Şunu» (İsim olmadan)', 'İsmin yerini tek başına tutar', YES, YES_A,
        '«Şu» sözcüğünü sıfat ve zamir olarak cümlede kullanma kuralı.'
    )
