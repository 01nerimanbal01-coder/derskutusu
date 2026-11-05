"""5. sınıf Türkçe 12. hafta (Atatürk ve Çiftlik Dinleme Metni ve Tema Değerlendirmesi) görselleri.
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
        '1925 Öncesi: Çorak ve Bataklık', 'Uzmanlar: «Burada ot bile bitmez!»', 'Susuz ve verimsiz arazi', TUR, TUR_A,
        'Atatürk’ün Azmi ve Bilim', 'Toprak ıslahı + Binlerce fidan', 'Yeşil Atatürk Orman Çiftliği', YES, YES_A,
        'Atatürk Orman Çiftliği’nin kuruluş süreci ve ana fikir şeması.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Çift-lik', 'Kök: çift (İsim) + -lik', MAVI, MAVI_A),
        ('2. Bak-ım-lı', 'Kök: bak- (Fiil) + -ım-lı', YES, YES_A),
        ('3. Orman-cı', 'Kök: orman (İsim) + -cı', TUR, TUR_A),
        ('4. Bil-gi', 'Kök: bil- (Fiil) + -gi', MOR, MOR_A),
    ], 'Kök ve yapım eki almış dört türemiş sözcük kartı.')
    s[5]['gorsel'] = dortlu_kart([
        ('1. Unvan Yazımı', 'Gazi Mustafa Kemal Paşa (Doğru)', YES, YES_A),
        ('2. Bayram Adı', 'Cumhuriyet Bayramı’nda (Doğru)', MAVI, MAVI_A),
        ('3. Kurum Adı Eki (!)', 'Türk Dil Kurumu’na (Kesme olmaz!)', KIR, KIR_A),
        ('4. Şehir Özel Adı', 'Ankara’dan (Kesme ile ayrılır)', CAM, CAM_A),
    ], 'Büyük harfler ve kesme işareti kullanım panosu.')
    s[6]['gorsel'] = dortlu_kart([
        ('1. Düşünce Yönü Değiştirme', 'Arazi çoraktı; [1: fakat] pes edilmedi.', TUR, TUR_A),
        ('2. Neden-Sonuç Bağlantısı', 'Çok çalışıldı; [2: bu yüzden] yeşerdi.', MAVI, MAVI_A),
        ('3. Özetleme ve Toparlama', '[3: Kısacası] azim engelleri aştı.', YES, YES_A),
        ('Geçiş İfadeleri', 'fakat · bu yüzden · kısacası', MOR, MOR_A),
    ], 'Geçiş ve bağlantı ifadeleri tamamlama şeması.')
    s[7]['gorsel'] = dortlu_kart([
        ('Olay', 'Çorak arazinin çiftliğe dönüşümü', MAVI, MAVI_A),
        ('Kişiler / Varlık Kadrosu', 'Atatürk, uzmanlar, çalışanlar', YES, YES_A),
        ('Yer (Mekân)', 'Ankara (AOÇ arazisi)', TUR, TUR_A),
        ('Zaman', '1925 yılı bahar ayları', MOR, MOR_A),
    ], 'Atatürk ve Çiftlik metninin hikâye unsurları haritası.')
    s[8]['gorsel'] = dortlu_kart([
        ('1. Serim (Giriş)', 'Örnek çiftlik için arazi arayışı', MAVI, MAVI_A),
        ('2. Düğüm (Engel)', 'Arazinin çorak ve bataklık olması', KIR, KIR_A),
        ('3. Düğüm (Çaba)', 'Bataklığın kurutulup ağaçlandırılması', TUR, TUR_A),
        ('4. Çözüm (Sonuç)', 'Yemyeşil örnek çiftliğin doğuşu', YES, YES_A),
    ], 'Metnin serim, düğüm ve çözüm bölümleri akışı.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. su-la-ma', 'Yapım eki → Türemiş sözcük', YES, YES_A),
        ('2. ağaç-lar (!)', '-lar çoğul çekim ekidir → Basit!', KIR, KIR_A),
        ('3. üre-tim', 'Yapım eki → Türemiş sözcük', MAVI, MAVI_A),
        ('4. köy-lü', 'Yapım eki → Türemiş sözcük', MOR, MOR_A),
    ], 'Yapım eki ve çekim eki karşılaştırma kartları.')
    s[11]['gorsel'] = ikili_kart(
        'Yazma Planı: Giriş & Gelişme', 'Konu: Atatürk’ün doğa sevgisi', 'Örnek: Çorak toprağı yeşertmesi', YES, YES_A,
        'Bağlantı ve Sonuç Bölümü', 'Bağlaç: bu yüzden / çünkü / fakat', 'Toparlama: kısacası / özetle', MAVI, MAVI_A,
        'Bilgilendirici metin yazma planı ve bağlantı ifadeleri kartı.'
    )
