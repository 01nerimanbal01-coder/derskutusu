"""5. sınıf Fen Bilimleri 12. hafta (Sürtünme Kuvveti Uygulamaları ve Hücre Kavramına Giriş) görselleri.
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
        ('1. Kış Lastiği ve Zincir', 'Derin dişli yüzey (Sürtünme +)', KIR, KIR_A),
        ('2. Geniş Paraşüt Kubbesi', 'Hava direnci artar (Sürtünme +)', TUR, TUR_A),
        ('3. Metal Bilyeli Rulman', 'Yuvarlanma ile kolay döner (Sürtünme −)', YES, YES_A),
        ('4. Hızlı Tren Sivri Burun', 'Hava direncini yarar (Sürtünme −)', MAVI, MAVI_A),
    ], 'Sürtünmeyi artıran ve azaltan dört mühendislik uygulaması.')
    s[2]['gorsel'] = ikili_kart(
        'Bitki Hücresi (Soğan/Yaprak)', 'Köşeli yapı · Hücre duvarı var', 'Kloroplast (yeşil kısımda) var', YES, YES_A,
        'Hayvan Hücresi (Epitel)', 'Yuvarlak/oval · Hücre duvarı yok', 'Kloroplast bulunmaz', MOR, MOR_A,
        'Bitki ve hayvan hücresinin yapısal karşılaştırma şeması.'
    )
    s[5]['gorsel'] = ikili_kart(
        'Dünya Ölçümü (K Cismi)', 'Kütle (m) = 36 kg', 'Ağırlık (G) = 360 N', MAVI, MAVI_A,
        'Ay Ölçümü (Yer Çekimi 1/6)', 'Kütle değişmez: m = ?', 'Ağırlık 1/6 olur: G = ?', TUR, TUR_A,
        'K cisminin Dünya ve Ay üzerindeki kütle ve ağırlık karşılaştırması.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('K Kısmı (En Dış Canlı Örtü)', 'Esnek ve seçici geçirgen yapı', MAVI, MAVI_A),
        ('L Kısmı (Merkezdeki Yapı)', 'Büyüme ve yönetim merkezi', KIR, KIR_A),
        ('M Kısmı (Yarı Akışkan Sıvı)', 'Organelleri üzerinde taşır', YES, YES_A),
        ('Temel Hücre Modeli', 'K + L + M ortak yapılardır', MOR, MOR_A),
    ], 'Hücrenin üç temel kısmını (K, L, M) gösteren model kartı.')
    s[7]['gorsel'] = ikili_kart(
        'K DinamometresiÖzelliği', 'Toplam 10 eş bölme', 'En fazla ölçüm: 50 N', CAM, CAM_A,
        'Ölçüm Durumu', '1 bölme = 50 ÷ 10 = 5 N', 'Asılı cisim → 3 bölme uzama', TUR, TUR_A,
        '10 bölmeli 50 N kapasiteli dinamometre ölçüm şeması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('Kalın Tüylü Halı', 'Çok pürüzlü (Sürtünme en çok)', KIR, KIR_A),
        ('Pürüzlü Toprak Zemin', 'Orta-yüksek sürtünme', TUR, TUR_A),
        ('Düz Ahşap Parke', 'Az pürüzlü zemin', MAVI, MAVI_A),
        ('Cilalı Cam / Buz Zemin', 'Çok kaygan (Sürtünme en az)', CAM, CAM_A),
    ], 'Dört farklı zeminde sürtünme ve alınan yol karşılaştırması.')
    s[9]['gorsel'] = ikili_kart(
        'X Preparatı (Mikroskop)', 'Köşeli şekil + Hücre çeperi', 'Bitkisel doku örneği', YES, YES_A,
        'Y Preparatı (Mikroskop)', 'Oval/yuvarlak şekil · Çeper yok', 'Hayvansal doku örneği', MOR, MOR_A,
        'X ve Y mikroskop preparatlarındaki hücre şekilleri.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Geniş Paraşüt Kubbesi', 'Hava direnci artırılır', 'Amaç: Güvenli ve yavaş iniş', TUR, TUR_A,
        'Buz Pateni İnce Bıçağı', 'Yüzey sürtünmesi azaltılır', 'Amaç: Rahat ve hızlı kayma', CAM, CAM_A,
        'Paraşüt kubbesi ve buz pateni bıçağında sürtünme kuvvetinin rolü.'
    )
