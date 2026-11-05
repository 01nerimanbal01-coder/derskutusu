"""6. sınıf Din Kültürü ve Ahlak Bilgisi 13. hafta (Orucun Kazandırdıkları, Ramazan Kültürümüz ve Ünite Değerlendirmesi) görselleri.
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
        'Hadis-i Şerif (Buhârî, Savm 2)', '«Oruç bir kalkandır...»', 'Kötülüklerden koruyan manevi zırh', YES, YES_A,
        'Oruçlu Müminin Tutumu', 'Kötü söz ve kavgadan uzak durur', '«Ben oruçluyum» diyerek sabreder', MAVI, MAVI_A,
        'Orucun insanı kötülüklerden koruyan kalkan oluşu.'
    )
    s[2]['gorsel'] = ikili_kart(
        'Bireysel Kazanımlar', 'İrade eğitimi · Sabır · Öz denetim', 'Nimetlere şükür ve empati bilinci', MAVI, MAVI_A,
        'Toplumsal Kazanımlar', 'Fitre · Sadaka · İftar paylaşımı', 'Yardımlaşma ve kardeşlik ruhu', YES, YES_A,
        'Oruç ibadetinin bireye ve topluma kazandırdığı değerler.'
    )
    s[5]['gorsel'] = dortlu_kart([
        ('1. Mahya Geleneği', 'Minareler arası ışıklı güzel sözler', MAVI, MAVI_A),
        ('2. Diş Kirası', 'İftar misafirine verilen hediye', MOR, MOR_A),
        ('3. Tekne Orucu (Çocuklar İçin)', 'Öğleye kadar tutup oruca alışma', TUR, TUR_A),
        ('4. Mukabele Geleneği', 'Kur’an’ın karşılıklı okunması', YES, YES_A),
    ], 'Kültürümüzde yaşayan dört köklü Ramazan geleneği.')
    s[6]['gorsel'] = dortlu_kart([
        ('Farz Oruç', 'Ramazan ayı orucu (Bakara 183)', YES, YES_A),
        ('Vacip Oruç', 'Adak orucu (Söz verilen oruç)', MAVI, MAVI_A),
        ('Nafile / Sünnet Oruç', 'Aşure · Davud · Pazartesi-Perşembe', TUR, TUR_A),
        ('Şevval Orucu (6 Gün)', 'Ramazan’dan sonra tutulan sünnet', MOR, MOR_A),
    ], 'İslam’da farz, vacip ve nafile/sünnet oruç çeşitleri.')
    s[7]['gorsel'] = ikili_kart(
        'Zimem Defteri Uygulaması', 'Bakkalın veresiye defterindeki', 'yoksul borçlarının silinmesi', CAM, CAM_A,
        'Ahlaki İncelik (Gizlilik)', 'Veren el kimin borcunu ödediğini,', 'alan el kimin ödediğini bilmez', YES, YES_A,
        'Zimem defteri geleneğinde gizli yardımlaşma ve insan onuru.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Sahur Vakti (Gece)', 'Bereketli yemek ve oruca niyet', MAVI, MAVI_A),
        ('2. İmsak ve Mukabele (Gündüz)', 'Oruca başlama ve Kur’an tilaveti', CAM, CAM_A),
        ('3. İftar Vakti (Akşam Ezanı)', 'Dua ve şükürle orucu açma', TUR, TUR_A),
        ('4. Teravih Namazı (Yatsı)', 'Camide cemaatle 20 rekât sünnet', YES, YES_A),
    ], 'Ramazan gününde sahurdan teravihe ibadet sıralaması.')
    s[9]['gorsel'] = ikili_kart(
        'Nimetlerin Kıymetini Anlama', 'Bir yudum su ve bir lokma ekmeğin', 'değerini fark ederek şükretmek', YES, YES_A,
        'Davranışa Yansıması', 'Sofrada israftan kaçınmak ve', 'nimetleri ihtiyaç sahipleriyle paylaşmak', TUR, TUR_A,
        'Oruç ibadetinin şükür ve israfı önleme bilincine etkisi.'
    )
    s[11]['gorsel'] = ikili_kart(
        '1. Bireysel Öz Denetim', 'Nefsin isteklerine söz geçirme', 'Sabır ve güzel ahlak eğitimi', MAVI, MAVI_A,
        '2. Toplumsal Dayanışma', 'Fitre, zekât ve iftar sofralarıyla', 'sevgi ve barış köprüsü kurma', YES, YES_A,
        'Orucun öz denetim ve toplumsal dayanışma kazanımları.'
    )
