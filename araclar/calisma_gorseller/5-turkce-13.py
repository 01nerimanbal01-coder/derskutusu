"""5. sınıf Türkçe 13. hafta (Duygularımız Metni, Öznel-Nesnel Yargılar ve Söz Sanatları) görselleri.
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
        ('1. Kart: «...büyüleyen eşsiz eser»', 'Kişisel beğeni → Öznel Yargı', MOR, MOR_A),
        ('2. Kart: «4 rafta toplam 160 kitap»', 'Kanıtlanabilir → Nesnel Yargı', YES, YES_A),
        ('3. Kart: «...tarifsiz bir huzur verir»', 'Kişisel duygu → Öznel Yargı', TUR, TUR_A),
        ('4. Kart: «En güzel işleyen metin...»', 'Kişisel yorum → Öznel Yargı', KIR, KIR_A),
    ], 'Öznel ve nesnel yargı cümle kartlarının karşılaştırması.')
    s[2]['gorsel'] = ikili_kart(
        'Benzetme (Teşbih) Sanatı', 'Pamuk gibi yumuşak bulutlar', 'Karınca gibi çalışkan öğrenciler', MAVI, MAVI_A,
        'Kişileştirme (Teşhis) Sanatı', 'Yorgun çınar derdini fısıldadı', 'Küskün bulutlar gözyaşı döktü', MOR, MOR_A,
        'Benzetme ve kişileştirme söz sanatları örnek kartları.'
    )
    s[5]['gorsel'] = dortlu_kart([
        ('Benzeyen (Zayıf Unsur)', 'Dedemin öğütleri', MAVI, MAVI_A),
        ('Kendisine Benzetilen (Güçlü)', 'Altın', TUR, TUR_A),
        ('Benzetme Yönü (Ortak Özellik)', 'Değerli olması', YES, YES_A),
        ('Benzetme Edatı', 'gibi', MOR, MOR_A),
    ], 'Benzetme sanatının dört temel unsuru şeması.')
    s[6]['gorsel'] = ikili_kart(
        'Yüzey Anlam (Doğrudan Yazılan)', 'Elif sınav sonucuna baktı,', 'yerinden sıçradı ve annesine sarıldı.', MAVI, MAVI_A,
        'Derin Anlam (Örtük Çıkarım)', 'Davranış ipuçlarından çıkarım:', 'Başarılı oldu → Büyük sevinç yaşadı!', YES, YES_A,
        'Metinde yüzey anlam ve derin anlam (örtük ileti) ayrımı.'
    )
    s[7]['gorsel'] = ikili_kart(
        '1. Cümle (Tanımlama)', '«Empati, kişinin kendisini başkasının', 'yerine koyabilme becerisidir.»', CAM, CAM_A,
        '2. Cümle (Örneklendirme)', '«Örneğin üzgün bir arkadaşımızı', 'dinlemek empatinin ilk adımıdır.»', TUR, TUR_A,
        'Tanımlama, örneklendirme ve bağlantı ifadesi inceleme kartı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Başlangıç (Heyecan/Korku)', 'Kuliste yüreğim ağzıma gelmişti.', KIR, KIR_A),
        ('2. Dönüşüm (Ancak...)', 'Öğretmenimin tebessümüyle sakinleştim.', MAVI, MAVI_A),
        ('3. Gerekçe (Çünkü...)', 'Haftalarca emekle hazırlanmıştım.', TUR, TUR_A),
        ('4. Sonuç (Sevinç)', 'Alkışlarla eteklerim zil çaldı.', YES, YES_A),
    ], 'Duygu değişimi ve bağlantı ifadeleriyle paragraf sıralama kartları.')
    s[9]['gorsel'] = ikili_kart(
        'Benzetme Boyutu', '«İnci gibi bembeyaz papatyalar»', 'Papatya → İnciye benzetilmiş', MAVI, MAVI_A,
        'Kişileştirme Boyutu', '«...baharın gelişine neşeyle gülümsedi»', 'Papatyaya gülümseme özelliği verilmiş', MOR, MOR_A,
        'Aynı dizede benzetme ve kişileştirme sanatının birlikte kullanımı.'
    )
    s[11]['gorsel'] = ikili_kart(
        '1. Görev: Benzetme Cümlesi', 'Kavram: Deniz (Örn: Çarşaf gibi)', 'Benzeyen + Benzetilen + Yön + Edat', MAVI, MAVI_A,
        '2. Görev: Kişileştirme Cümlesi', 'Kavram: Rüzgâr (Örn: Şarkı söyleyen)', 'İnsan dışı varlığa insani özellik', YES, YES_A,
        'Deniz ve rüzgâr kavramlarıyla söz sanatı üretme kartları.'
    )
