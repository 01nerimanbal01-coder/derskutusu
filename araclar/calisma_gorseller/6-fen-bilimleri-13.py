"""6. sınıf Fen Bilimleri 13. hafta (Denetleyici Sistem Sağlığı ve Işığın Yansıması) görselleri.
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
        ('1. Kask ve Emniyet Kemeri (✓)', 'Beyin ve omuriliği darbeden korur', YES, YES_A),
        ('2. Düzenli Gece Uykusu (✓)', 'Büyüme hormonu salgısını destekler', MAVI, MAVI_A),
        ('3. Bilinçsiz İlaç Kullanımı (✗)', 'Sistemlerin dengesini bozar!', KIR, KIR_A),
        ('4. B Vitamini ve İyotlu Tuz (✓)', 'Sinir ve tiroit sağlığını korur', CAM, CAM_A),
    ], 'Denetleyici ve düzenleyici sistem sağlığı doğru ve yanlış uygulamalar.')
    s[2]['gorsel'] = ikili_kart(
        'Düzgün Yansıma (Ayna / Durgun Su)', 'Pürüzsüz yüzey · Paralel yansıma', 'Net ve parlak görüntü oluşur', MAVI, MAVI_A,
        'Dağınık Yansıma (Duvar / Kâğıt)', 'Pürüzlü yüzey · Dağınık yansıma', 'Net görüntü oluşmaz (Etraf aydınlanır)', TUR, TUR_A,
        'Düzgün yansıma ve dağınık yansıma özelliklerinin karşılaştırması.'
    )
    s[5]['gorsel'] = ikili_kart(
        '1. Durum: Delikler Aynı Hizada', 'Mum → [Delik 1] → [Delik 2] → [Delik 3]', 'Işık doğrusal geçer ve görülür', YES, YES_A,
        '2. Durum: Ortadaki Karton Kaydırıldı', 'Işık doğrusal yayıldığı için', 'engellenir ve mum ışığı görülmez', KIR, KIR_A,
        'Üç delikli karton deneyinde ışığın doğrusal yayılması.'
    )
    s[6]['gorsel'] = ikili_kart(
        'K Yüzeyi (Pürüzsüz ve Parlak)', 'Paralel Gelen ⇉ Paralel Yansıyan', 'Örnek: Düzlem ayna, düz folyo', CAM, CAM_A,
        'L Yüzeyi (Pürüzlü ve Mat)', 'Paralel Gelen ⇉ Farklı Yönlere Saçılan', 'Örnek: Buruşuk folyo, halı, duvar', MOR, MOR_A,
        'K (düzgün) ve L (dağınık) yüzeylerinde ışık ışınlarının yansıması.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Durgun Göl Suyu (Taş Atmadan Önce)', 'Pürüzsüz yüzey → Düzgün yansıma', 'Ağaçların görüntüsü çok nettir', YES, YES_A,
        'Dalgalı Göl Suyu (Taş Atıldıktan Sonra)', 'Pürüzlü yüzey → Dağınık yansıma', 'Görüntü bozulur ve bulanıklaşır', TUR, TUR_A,
        'Durgun ve dalgalı su yüzeyinde yansıma ve görüntü farkı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Adım: Düz Folyo Gözlemi', 'Paralel yansıma ve net görüntü', MAVI, MAVI_A),
        ('2. Adım: Folyoyu Buruşturma', 'Yüzeyi pürüzlü hâle getirme', TUR, TUR_A),
        ('3. Adım: Buruşuk Folyo Gözlemi', 'Farklı yönlere dağınık yansıma', MOR, MOR_A),
        ('4. Adım: Bilimsel Çıkarım', 'Pürüzlülük artarsa görüntü bozulur', YES, YES_A),
    ], 'Alüminyum folyo ile düzgün ve dağınık yansıma deney basamakları.')
    s[9]['gorsel'] = ikili_kart(
        'Dağınık Yansımanın Günlük Önemi 1', 'Gölgede kalan köşeleri aydınlatır', 'Cisimleri her açıdan görmemizi sağlar', YES, YES_A,
        'Dağınık Yansımanın Günlük Önemi 2', 'Mat kitap sayfası gözü kamaştırmaz', 'Rahat okuma olanağı sunar', MAVI, MAVI_A,
        'Dağınık yansımanın aydınlanma ve görme üzerindeki olumlu etkileri.'
    )
    s[11]['gorsel'] = dortlu_kart([
        ('Fiziksel Koruma', 'Kask, dizlik ve emniyet kemeri', MAVI, MAVI_A),
        ('Beslenme Düzeni', 'B vitamini, omega-3 ve iyotlu tuz', YES, YES_A),
        ('Uyku ve Dinlenme', 'Düzenli gece uykusu ve spor', CAM, CAM_A),
        ('Kaçınılacak Unsurlar', 'Sigara, alkol, stres, bilinçsiz ilaç', KIR, KIR_A),
    ], 'Denetleyici ve düzenleyici sistemlerin sağlığını koruma rehberi.')
