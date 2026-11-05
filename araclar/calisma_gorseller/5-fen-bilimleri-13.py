"""5. sınıf Fen Bilimleri 13. hafta (Hücrenin Temel Kısımları ve Organeller) görselleri.
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
        'X Organeli (Enerji Santrali)', 'Besin + Oksijen → Enerji', 'Kas ve karaciğerde çoktur', TUR, TUR_A,
        'Y Organeli (Besin Fabrikası)', 'Işık + Su + CO₂ → Besin + O₂', 'Bitkinin yeşil kısımlarında', YES, YES_A,
        'Mitokondri (X) ve kloroplast (Y) organellerinin görev karşılaştırması.'
    )
    s[2]['gorsel'] = ikili_kart(
        'Bitki Hücresi Özellikleri', 'Köşeli · Hücre duvarı + Kloroplast', 'Koful: Büyük ve az sayıda', YES, YES_A,
        'Hayvan Hücresi Özellikleri', 'Oval · Sentrozom + Lizozom', 'Koful: Küçük ve çok sayıda', MOR, MOR_A,
        'Bitki ve hayvan hücresinin organel ve şekil karşılaştırması.'
    )
    s[5]['gorsel'] = ikili_kart(
        'Hücre Zarı (Ortak Yapı)', 'Canlı · Esnek · İnce', 'Seçici geçirgen (Kontrollü geçiş)', MAVI, MAVI_A,
        'Hücre Duvarı (Bitkiye Özgü)', 'Cansız · Sert · Dayanıklı', 'Tam geçirgen (Bitkiyi korur)', YES, YES_A,
        'Hücre zarı ile hücre duvarının yapısal karşılaştırması.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('K Bölgesi (Yalnız Bitki)', 'Hücre duvarı · Kloroplast', YES, YES_A),
        ('L Bölgesi (Ortak Yapılar)', 'Zar · Sitoplazma · Çekirdek', MAVI, MAVI_A),
        ('L Bölgesi (Ortak Organeller)', 'Mitokondri · Ribozom · Golgi · ER', CAM, CAM_A),
        ('M Bölgesi (Yalnız Hayvan)', 'Sentrozom · Lizozom', MOR, MOR_A),
    ], 'Bitki ve hayvan hücresi Venn şeması bölgeleri (K, L, M).')
    s[7]['gorsel'] = ikili_kart(
        'Bitki Hücresinde Koful', 'Büyük hacimli', 'Az sayıda (Genellikle merkezi)', YES, YES_A,
        'Hayvan Hücresinde Koful', 'Küçük hacimli', 'Çok sayıda (Sitoplazmada dağınık)', TUR, TUR_A,
        'Bitki ve hayvan hücrelerinde koful büyüklüğü ve sayısı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Katman (En Dış)', 'Hücre Duvarı (Cansız çeper)', YES, YES_A),
        ('2. Katman (İç Örtü)', 'Hücre Zarı (Seçici geçirgen)', MAVI, MAVI_A),
        ('3. Katman (Orta Ortam)', 'Sitoplazma ve Organeller', TUR, TUR_A),
        ('4. Katman (En İç Merkez)', 'Çekirdek (Yönetim merkezi)', MOR, MOR_A),
    ], 'Bitki hücresinin dıştan içe doğru dört temel katmanı.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Rapor (Doğru)', 'Mitokondri ve ribozom ortaktır', YES, YES_A),
        ('2. Rapor (Doğru)', 'Yaprak hücresinde kloroplast var', CAM, CAM_A),
        ('3. Rapor (Hatalı!)', 'İnsan deri hücresinde kloroplast', KIR, KIR_A),
        ('4. Rapor (Doğru)', 'Salgı bezinde golgi çoktur', MAVI, MAVI_A),
    ], 'Dört farklı hücre gözlem raporunun doğruluk incelemesi.')
    s[11]['gorsel'] = dortlu_kart([
        ('Yönetim Müdürlüğü', 'Çekirdek (Hücreyi yönetir)', MOR, MOR_A),
        ('Enerji Santrali', 'Mitokondri (Enerji üretir)', TUR, TUR_A),
        ('Taşıma Koridorları', 'Endoplazmik Retikulum (İletim)', MAVI, MAVI_A),
        ('Paketleme Servisi', 'Golgi Cisimciği (Salgı paketler)', YES, YES_A),
    ], 'Hücre organellerinin fabrika birimlerine benzetilmesi modeli.')
