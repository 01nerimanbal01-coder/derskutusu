"""8. sınıf Türkçe 11. hafta (Gardaşım Şiiri, Fiilde Çatı Uygulamaları ve Cümle Türleri) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def karma_cati_kartlari():
    kartlar = [
        (6, 6, '1. Kart: ...duygusunu anlattı.', 'Etken + Geçişli (?)', MAVI, MAVI_A),
        (184, 6, '2. Kart: ...çeşme onarıldı.', 'Edilgen (-l eki)', TUR, TUR_A),
        (6, 60, '3. Kart: ...sevinçle gülümsedi.', 'Geçişsiz (Onu ✗)', YES, YES_A),
        (184, 60, '4. Kart: ...dürüstlüktür.', 'İsim cümlesi', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Özne ve nesne ilişkisine göre dört farklı cümle kartı.')


def cati_analiz_sema():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Öznesine Göre', MAVI, kalin=True)
    ic += yazi(91, 52, '• Etken: Gerçek/Gizli özne', LAC)
    ic += yazi(91, 74, '• Edilgen: -l / -n eki var', KIR, kalin=True)
    ic += yazi(91, 96, '  ve Sözde Özne bulunur', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Nesnesine Göre', YES, kalin=True)
    ic += yazi(269, 52, '• Geçişli: «Onu» alabilir', LAC)
    ic += yazi(269, 74, '• Geçişsiz: «Onu» alamaz', LAC)
    ic += yazi(269, 96, 'Edilgen = Daima Geçişsiz!', YES, kalin=True)
    return svg(ic, 'Öznesine ve nesnesine göre fiilde çatı çözümleme anahtarı.')


def cati_aranmayan_cumleler():
    satirlar = [
        (6, 6, 'I. Yaprakları savuruyor.', MAVI, MAVI_A),
        (184, 6, 'II. Sofraya çorba kondu.', TUR, TUR_A),
        (6, 60, 'III. ...yanında olmaktır.', KIR, KIR_A),
        (184, 60, 'IV. ...özlemle anıyor.', YES, YES_A),
    ]
    ic = ''
    for x, y, m, r, z in satirlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 30, m, LAC, kalin=True)
    return svg(ic, 'Fiil ve fiilimsi yüklemli dört cümlenin karşılaştırılması.')


def gecisli_nesnesiz_sema():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 26, 'Geçişli Fiilde Nesne Kullanımı Kontrolü', TUR, kalin=True)
    ic += yazi(180, 52, '• «Fidanları sulardı» (Nesne yazılı ✓) · «Baklava ikram etti» (Nesne yazılı ✓)', LAC)
    ic += yazi(180, 76, '• «Sanatçı salonda duygulu okudu» → «Onu okudu» (Geçişli ✓, Nesne yazılı değil!)', MAVI, kalin=True)
    ic += yazi(180, 98, '• «İki saat uyudu» → «Onu uyudu ✗» (Geçişsiz fiil)', KIR, kalin=True)
    return svg(ic, 'Geçişli olduğu hâlde cümlede nesne almamış fiil örneği şeması.')


def etken_edilgen_donusum():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Etken ve Geçişli Cümle', MAVI, kalin=True)
    ic += yazi(91, 52, '«Belediye ekipleri çocuk', LAC)
    ic += yazi(91, 72, 'parkını boyadı.»', MAVI, kalin=True)
    ic += yazi(91, 96, 'Nesne: çocuk parkını', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Edilgen Dönüşüm (-n eki)', YES, kalin=True)
    ic += yazi(269, 52, 'Eski nesne → Sözde Özne', LAC)
    ic += yazi(269, 74, 'Yüklem: boya-n-dı', YES, kalin=True)
    ic += yazi(269, 96, 'İşi yapan belli değil!', KIR, kalin=True)
    return svg(ic, 'Etken cümlenin edilgen çatıya dönüştürülmesinde nesnenin sözde özne olması.')


def cumle_turleri_seridi():
    adimlar = [
        (6, 'Kurallı Fiil', 'Yüklem sonda', MAVI, MAVI_A),
        (94, 'Devrik Fiil', 'Yüklem başta', TUR, TUR_A),
        (182, 'Kurallı İsim', 'Ek-fiilli ad', YES, YES_A),
        (270, 'Eksiltili', 'Üç nokta (...)', MOR, MOR_A),
    ]
    ic = ''
    for x, ad, acik, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 72, acik, LAC)
    return svg(ic, 'Yüklemin türüne ve yerine göre dört cümle türü şeridi.')


def gardasim_dortluk_panosu():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 24, '«Gardaşım» Şiirinden Dörtlük', YES, kalin=True)
    ic += yazi(180, 48, '«Ağlayanı güldürelim gardaşım / Dostluk ile birleşelim gardaşım', LAC)
    ic += yazi(180, 70, 'Karanlığı aydınlığa çevirip / Sevgi dolu yaşayalım gardaşım»', LAC)
    ic += yazi(180, 96, 'İpucu: «Ağlamak - gülmek» ve «karanlık - aydınlık» ilişkisine dikkat ediniz.', MAVI, kalin=True)
    return svg(ic, 'Kardeşlik ana duygusu ve karşıtlık (tezat) sanatı içeren dörtlük panosu.')


def fiilimsi_yuklem_karsilastirma():
    ic = kutu(6, 6, 170, 103, KIR_A, KIR)
    ic += yazi(91, 26, '1. Cümle (Fiilimsi Yüklem)', KIR, kalin=True)
    ic += yazi(91, 52, '«En büyük erdem, düşenin', LAC)
    ic += yazi(91, 72, 'elinden tutmaktır (-mak).»', KIR, kalin=True)
    ic += yazi(91, 96, 'İsim cümlesi (Çatı aranmaz)', LAC)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, '2. Cümle (Çekimli Fiil)', MAVI, kalin=True)
    ic += yazi(269, 52, '«Komşumuz zor günümüzde', LAC)
    ic += yazi(269, 72, 'elimizden tuttu (-tu).»', MAVI, kalin=True)
    ic += yazi(269, 96, 'Fiil cümlesi (Çatı aranır)', YES, kalin=True)
    return svg(ic, 'Fiilimsi yüklemli isim cümlesi ile çekimli fiil cümlesinin çatı karşılaştırması.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = karma_cati_kartlari()
    s[2]['gorsel'] = cati_analiz_sema()
    s[5]['gorsel'] = cati_aranmayan_cumleler()
    s[6]['gorsel'] = gecisli_nesnesiz_sema()
    s[7]['gorsel'] = etken_edilgen_donusum()
    s[8]['gorsel'] = cumle_turleri_seridi()
    s[9]['gorsel'] = gardasim_dortluk_panosu()
    s[11]['gorsel'] = fiilimsi_yuklem_karsilastirma()
