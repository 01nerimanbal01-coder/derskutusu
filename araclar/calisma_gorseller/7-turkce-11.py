"""7. sınıf Türkçe 11. hafta (Yapılarına Göre Fiiller, Ek-Fiil ve Düşünceyi Geliştirme Yolları) görselleri.
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


def fiil_yapisi_kartlari():
    kartlar = [
        (6, 6, '1. Kart', 'Bayraklarla süsledik.', MAVI, MAVI_A),
        (184, 6, '2. Kart', 'Hızlıca taşıyıverdi.', TUR, TUR_A),
        (6, 60, '3. Kart', 'Erkenden ulaştı.', YES, YES_A),
        (184, 60, '4. Kart', 'Emanete sahip çıktı.', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Yapılarına göre fiil örneklerinin yer aldığı dört cümle kartı.')


def birlesik_fiil_tablo_sema():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Kurallı Birleşik Fiiller', MAVI, kalin=True)
    ic += yazi(91, 52, '-ebil, -iver, -ekal, -eyaz', LAC)
    ic += yazi(91, 78, 'Daima BİTİŞİK yazılır', YES, kalin=True)
    ic += yazi(91, 98, '(çözebildik, bakakaldı)', LAC)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Yardımcı Fiilli (et-, ol-)', TUR, kalin=True)
    ic += yazi(269, 52, 'Ses olayı varsa BİTİŞİK:', LAC)
    ic += yazi(269, 74, 'sabretti, hissetti', KIR, kalin=True)
    ic += yazi(269, 96, 'Yoksa AYRI: fark etti', MAVI, kalin=True)
    return svg(ic, 'Kurallı ve yardımcı fiilli birleşik fiillerin yazım kuralı şeması.')


def sergi_metni_panosu():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 26, 'Millî Mücadele Sergisi Tanıtım Kartı', YES, kalin=True)
    ic += yazi(180, 52, '1. Cümle: «Fedakârlık, vatan için her zorluğu göze almaktır.»', LAC)
    ic += yazi(180, 76, '2. Cümle: «Örneğin Şerife Bacı ve Nezahat Onbaşı cepheye', LAC)
    ic += yazi(180, 96, 'cephane taşıyarak tarihe geçmiştir.»', MAVI, kalin=True)
    return svg(ic, 'Tanımlama ve örneklendirme içeren Millî Mücadele sergisi tanıtım kartı.')


def yazim_denetim_panosu():
    satirlar = [
        (6, 6, 'I. Zor günlerde sabretmeyi bildik.', YES, YES_A),
        (184, 6, 'II. Mektubu okuyunca hüzün hissetti.', MAVI, MAVI_A),
        (6, 60, 'III. Tehlikeyi uzaktan farketti.', KIR, KIR_A),
        (184, 60, 'IV. Köylüler askere yardım etti.', TUR, TUR_A),
    ]
    ic = ''
    for x, y, metin, r, z in satirlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 30, metin, LAC, kalin=True)
    return svg(ic, 'Yardımcı fiilli birleşik fiillerin yazımını karşılaştıran dört cümle panosu.')


def ek_fiil_iki_gorev():
    ic = kutu(6, 6, 170, 103, MOR_A, MOR)
    ic += yazi(91, 26, '1. Cümle (İsim Soylu)', MOR, kalin=True)
    ic += yazi(91, 54, '«Dedem o yıllarda cesur', LAC)
    ic += yazi(91, 74, 'bir çocukmuş (çocuk-imiş).»', MOR, kalin=True)
    ic += yazi(91, 98, 'İsmi yüklem yaptı', LAC)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 26, '2. Cümle (Birleşik Zaman)', CAM, kalin=True)
    ic += yazi(269, 54, '«Cepheye her gün su', LAC)
    ic += yazi(269, 74, 'taşıyordu (taşı-yor-idi).»', CAM, kalin=True)
    ic += yazi(269, 98, 'Birleşik zamanlı fiil yaptı', LAC)
    return svg(ic, 'Ek-fiilin isimleri yüklem yapma ve basit fiilleri birleşik zamanlı yapma görevleri.')


def kuralli_birlesik_seridi():
    adimlar = [
        (6, 'Yeterlik', '-ebil- (aşabilir)', MAVI, MAVI_A),
        (94, 'Tezlik', '-iver- (ulaştırıverdi)', TUR, TUR_A),
        (182, 'Sürerlik', '-ekal- (bakakaldı)', YES, YES_A),
        (270, 'Yaklaşma', '-eyaz- (düşeyazdı)', MOR, MOR_A),
    ]
    ic = ''
    for x, ad, ek, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 72, ek, LAC)
    return svg(ic, 'Dört kurallı birleşik fiil türünün ek ve örnek şeridi.')


def yeterlik_olumsuz_kart():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 26, 'Bir Hilal Uğruna Dörtlüğü', MAVI, kalin=True)
    ic += yazi(180, 52, '«Yürüdü kağnılar, fırtınada durmadı / Çelikten irademiz asla bükülmez', LAC)
    ic += yazi(180, 74, 'Bu sarp siperleri düşman aşamaz / Bağımsızlık meşalesi hiç sönmeyecek!»', KIR, kalin=True)
    ic += yazi(180, 98, 'İpucu: Olumlusu «-ebilir / -abilir» olan fiili bulunuz.', MAVI, kalin=True)
    return svg(ic, 'Olumsuz fiiller içinde yeterlik fiilinin olumsuzunu gösteren dörtlük panosu.')


def tanik_gosterme_panosu():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 26, 'Millî Mücadelede Anadolu Kadını', TUR, kalin=True)
    ic += yazi(180, 54, 'Atatürk bir konuşmasında şöyle demiştir:', LAC)
    ic += yazi(180, 76, '«Dünyada hiçbir milletin kadını, ben Anadolu kadınından', MAVI, kalin=True)
    ic += yazi(180, 96, 'fazla çalıştım diyemez!»', MAVI, kalin=True)
    return svg(ic, 'Atatürk’ün doğrudan sözünü içeren tanık gösterme panosu.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = fiil_yapisi_kartlari()
    s[2]['gorsel'] = birlesik_fiil_tablo_sema()
    s[5]['gorsel'] = sergi_metni_panosu()
    s[6]['gorsel'] = yazim_denetim_panosu()
    s[7]['gorsel'] = ek_fiil_iki_gorev()
    s[8]['gorsel'] = kuralli_birlesik_seridi()
    s[9]['gorsel'] = yeterlik_olumsuz_kart()
    s[11]['gorsel'] = tanik_gosterme_panosu()
