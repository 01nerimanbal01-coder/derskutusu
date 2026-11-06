"""7. sınıf Türkçe 11. hafta (Yapılarına Göre Fiiller, Ek-Fiil ve Düşünceyi Geliştirme Yolları) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); 1em gövde puntosu (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="1em"'


def svg(ic, etiket, w=350, h=96):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def fiil_yapisi_kartlari():
    kartlar = [
        (4, 3, '1. Kart', 'süsledik', MAVI, MAVI_A),
        (179, 3, '2. Kart', 'taşıyıverdi', TUR, TUR_A),
        (4, 50, '3. Kart', 'ulaştı', YES, YES_A),
        (179, 50, '4. Kart', 'sahip çıktı', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 167, 42, z, r)
        ic += yazi(x + 83.5, y + 17, b1, r, kalin=True)
        ic += f'<text x="{x + 83.5:.1f}" y="{y + 36:.1f}" text-anchor="middle" {FONT} font-weight="600" text-decoration="underline" fill="{LAC}">{b2}</text>'
    return svg(ic, 'Yapılarına göre fiil örneklerinin yer aldığı dört kart.', h=95)


def sergi_metni_panosu():
    ic = kutu(4, 3, 342, 96, YES_A, YES)
    ic += yazi(175, 20, 'Millî Mücadele Sergisi Kartı', YES, kalin=True)
    ic += yazi(14, 40, '1. «Fedakârlık, vatan için her zorluğu', LAC, hiza='start')
    ic += yazi(14, 59, 'göze almaktır.»', LAC, hiza='start')
    ic += yazi(14, 78, '2. «Örneğin Şerife Bacı ve Nezahat', MAVI, hiza='start', kalin=True)
    ic += yazi(14, 95, 'Onbaşı cepheye cephane taşımıştır.»', MAVI, hiza='start', kalin=True)
    return svg(ic, 'Tanımlama ve örneklendirme içeren Millî Mücadele sergisi tanıtım kartı.', h=102)


def yazim_denetim_panosu():
    satirlar = [
        (3, 'I. Zor günlerde sabretmeyi bildik.', YES, YES_A),
        (28, 'II. Mektubu okuyunca hüzün hissetti.', MAVI, MAVI_A),
        (53, 'III. Tehlikeyi uzaktan farketti.', KIR, KIR_A),
        (78, 'IV. Köylüler askere yardım etti.', TUR, TUR_A),
    ]
    ic = ''
    for y, metin, r, z in satirlar:
        ic += kutu(4, y, 342, 22, z, r, r=5)
        ic += yazi(14, y + 15.5, metin, LAC, hiza='start', kalin=True)
    return svg(ic, 'Yardımcı fiilli birleşik fiillerin yazımını karşılaştıran dört cümle panosu.', h=103)


def ek_fiil_iki_gorev():
    ic = kutu(4, 3, 167, 86, MOR_A, MOR)
    ic += yazi(87.5, 20, '1. Cümle', MOR, kalin=True)
    ic += yazi(87.5, 40, '«Dedem cesur bir', LAC)
    ic += yazi(87.5, 60, 'çocukmuş.»', MOR, kalin=True)
    ic += yazi(87.5, 80, '(çocuk-imiş)', LAC)
    ic += kutu(179, 3, 167, 86, CAM_A, CAM)
    ic += yazi(262.5, 20, '2. Cümle', CAM, kalin=True)
    ic += yazi(262.5, 40, '«Cepheye her gün', LAC)
    ic += yazi(262.5, 60, 'su taşıyordu.»', CAM, kalin=True)
    ic += yazi(262.5, 80, '(taşı-yor-idi)', LAC)
    return svg(ic, 'Ek-fiilin isimleri yüklem yapma ve basit fiilleri birleşik zamanlı yapma görevleri.', h=92)


def kuralli_birlesik_seridi():
    adimlar = [
        (4, 3, 'Yeterlik (-ebil-)', 'Örnek: aşabilir', MAVI, MAVI_A),
        (179, 3, 'Tezlik (-iver-)', 'Örnek: ulaştırıverdi', TUR, TUR_A),
        (4, 50, 'Sürerlik (-ekal-)', 'Örnek: bakakaldı', YES, YES_A),
        (179, 50, 'Yaklaşma (-eyaz-)', 'Örnek: düşeyazdı', MOR, MOR_A),
    ]
    ic = ''
    for x, y, ad, ek, r, z in adimlar:
        ic += kutu(x, y, 167, 42, z, r)
        ic += yazi(x + 83.5, y + 17, ad, r, kalin=True)
        ic += yazi(x + 83.5, y + 36, ek, LAC)
    return svg(ic, 'Dört kurallı birleşik fiil türünün ek ve örnek kartları.', h=95)


def yeterlik_olumsuz_kart():
    ic = kutu(4, 3, 342, 86, MAVI_A, MAVI)
    ic += f'<text x="14" y="21" {FONT} font-weight="500" fill="{LAC}">Yürüdü kağnılar, fırtınada <tspan font-weight="700" text-decoration="underline" fill="{KIR}">durmadı</tspan>,</text>'
    ic += f'<text x="14" y="41" {FONT} font-weight="500" fill="{LAC}">Çelikten irademiz asla <tspan font-weight="700" text-decoration="underline" fill="{KIR}">bükülmez</tspan>,</text>'
    ic += f'<text x="14" y="61" {FONT} font-weight="500" fill="{LAC}">Bu sarp siperleri düşman <tspan font-weight="700" text-decoration="underline" fill="{KIR}">aşamaz</tspan>,</text>'
    ic += f'<text x="14" y="81" {FONT} font-weight="500" fill="{LAC}">Bağımsızlık meşalesi hiç <tspan font-weight="700" text-decoration="underline" fill="{KIR}">sönmeyecek</tspan>!</text>'
    return svg(ic, 'Olumsuz fiiller içinde yeterlik fiilinin olumsuzunu gösteren dörtlük panosu.', h=92)


def tanik_gosterme_panosu():
    ic = kutu(4, 3, 342, 86, TUR_A, TUR)
    ic += yazi(175, 20, 'Millî Mücadelede Anadolu Kadını', TUR, kalin=True)
    ic += yazi(14, 40, 'Atatürk bir konuşmasında şöyle demiştir:', LAC, hiza='start')
    ic += yazi(14, 60, '«Dünyada hiçbir milletin kadını, ben Anadolu', MAVI, hiza='start', kalin=True)
    ic += yazi(14, 80, 'kadınından fazla çalıştım diyemez!»', MAVI, hiza='start', kalin=True)
    return svg(ic, 'Atatürk’ün doğrudan sözünü içeren tanık gösterme panosu.', h=92)


def muze_bilgi_notu():
    ic = kutu(4, 3, 342, 86, CAM_A, CAM)
    ic += yazi(175, 20, 'İstiklal Yolu Müzesi Ziyaretçi Notu', CAM, kalin=True)
    ic += yazi(14, 40, '«Sergimizi 2026 yılının ilk üç ayında 48.500', LAC, hiza='start')
    ic += yazi(14, 60, 'öğrenci gezdi; ecdadımız bağımsızlık uğruna', LAC, hiza='start')
    ic += f'<text x="14" y="80" {FONT} font-weight="500" fill="{LAC}">her türlü tehlikeyi <tspan font-weight="700" text-decoration="underline" fill="{KIR}">göze almıştır</tspan>.»</text>'
    return svg(ic, 'Sayısal veri ve anlamca kaynaşmış birleşik fiil içeren müze bilgi notu.', h=92)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = fiil_yapisi_kartlari()
    s[5]['gorsel'] = sergi_metni_panosu()
    s[6]['gorsel'] = yazim_denetim_panosu()
    s[7]['gorsel'] = ek_fiil_iki_gorev()
    s[8]['gorsel'] = kuralli_birlesik_seridi()
    s[9]['gorsel'] = yeterlik_olumsuz_kart()
    s[11]['gorsel'] = tanik_gosterme_panosu()
    if len(s) > 12:
        s[12]['gorsel'] = muze_bilgi_notu()
