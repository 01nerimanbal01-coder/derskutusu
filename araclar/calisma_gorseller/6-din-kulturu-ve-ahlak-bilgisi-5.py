"""6. sınıf Din Kültürü ve Ahlak Bilgisi 5. hafta (İlahi Kitaplar: Vahiy, Kitaplara İman, Suhuf, Tevrat, Zebur ve İncil) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def suhuf_dagilim_semasi():
    kartlar = [
        ('Hz. Âdem', '10 Sayfa (İlk Peygamber)', MAVI, MAVI_A),
        ('Hz. Şit', '50 Sayfa (En Çok Suhuf)', YES, YES_A),
        ('Hz. İdris', '30 Sayfa (Kur’an’da Anılır)', TUR, TUR_A),
        ('Hz. İbrahim', '10 Sayfa (Toplam 100 Sayfa)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört peygambere gönderilen toplam 100 sayfalık suhuf dağılımı şeması.', 21)


def uc_ilahi_kitap_panosu():
    kartlar = [
        ('1. Tevrat Kartı', 'Hz. Musa · İbranice · On Emir (İsrailoğulları)', MAVI, MAVI_A),
        ('2. Zebur Kartı (!)', 'Hz. Süleyman (?) · Yeni Fıkıh Hukuku (?)', KIR, KIR_A),
        ('3. İncil Kartı', 'Hz. İsa · Müjde · Tevrat’ı Doğrulayıcı', YES, YES_A),
        ('4. Ortak Özellik', 'Üçü de İsrailoğulları toplumuna gönderildi', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Tevrat, Zebur ve İncil özelliklerini karşılaştıran dörtlü bilgi panosu.', 21)


def vahiy_bilgi_kartlari():
    kartlar = [
        ('1. Hz. Âdem', 'İlk insan → 10 sahife', MAVI, MAVI_A),
        ('2. Hz. İdris', 'Sadık nebi → 30 sahife', YES, YES_A),
        ('3. Hz. Musa', 'İbranice kitap → Tevrat', TUR, TUR_A),
        ('4. Hz. Davud', 'Hükümdar nebi → Zebur', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört peygambere gönderilen suhuf ve ilahi kitap eşleştirme kartları.', 21)


def maide_46_dogrulama_karti():
    ic = kutu(6, 6, 588, 86, YES_A, YES, 9, 1.5)
    ic += kutu(6, 6, 588, 26, YES, YES, 9, 1)
    ic += yazi(300, 24, 'MÂİDE SURESİ 46. AYET MEALİ · VAHİY ZİNCİRİ', '#fff', kalin=True)
    ic += yazi(300, 50, '“… Meryem oğlu İsa’ya, içinde hidayet ve nur bulunan,', LAC, kalin=True)
    ic += yazi(300, 74, 'kendinden önceki Tevrat’ı doğrulayan İncil’i verdik …”', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'Mâide suresi 46. ayetinde İncil’in Tevrat’ı doğruladığını bildiren kart.', 21)


def kronolojik_vahiy_zinciri():
    adimlar = [
        ('1. Suhuf (100 s.)', 'Âdem · Şit · İdris · İbrahim', MAVI, MAVI_A),
        ('2. Tevrat', 'Hz. Musa (İlk Kitap)', YES, YES_A),
        ('3. Zebur', 'Hz. Davud (Mezmurlar)', TUR, TUR_A),
        ('4. İncil → Kur’an', 'Hz. İsa → Hz. Muhammed', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Suhuftan Kur’an-ı Kerim’e ilahi vahyin kronolojik gönderiliş zinciri.', 21)


def iki_ayri_soru_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(6, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(149, 24, '1. Soru: Kaynağı Allah mı?', '#fff', kalin=True)
    ic += yazi(149, 50, 'Tevrat, Zebur ve İncil’in ilk aslı', LAC, kalin=True)
    ic += yazi(149, 74, 'Allah’tan vahiydir → İman ederiz.', MAVI, kalin=True)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, TUR, TUR, 9, 1)
    ic += yazi(451, 24, '2. Soru: İlk Hâliyle Korundu mu?', '#fff', kalin=True)
    ic += yazi(451, 50, 'Önceki kitaplar zamanla değişti;', LAC, kalin=True)
    ic += yazi(451, 74, 'değişmeden korunan yalnız Kur’an’dır.', TUR, kalin=True)
    return svg(600, 98, ic, 'İlahi kitapların ilahi kaynağı ile günümüzdeki korunmuşluk durumunu ayıran kart.', 21)


def peygamber_kitap_butunlugu():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'PEYGAMBERLERE İMAN ↔ KİTAPLARA İMAN BÜTÜNLÜĞÜ', '#fff', kalin=True)
    ic += yazi(300, 50, 'Allah (Vahyin Kaynağı) → Peygamber (Elçi) → İlahi Kitap (Mesaj)', LAC, kalin=True)
    ic += yazi(300, 74, 'Kural: Elçiyi kabul edip getirdiği ilahi mesajı reddetmek tutarsızlıktır.', CAM, kalin=True)
    return svg(600, 98, ic, 'Peygamberlere iman ile kitaplara iman arasındaki ayrılmaz bağı gösteren şema.', 21)


def dort_incil_tek_incil_panosu():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(6, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(149, 24, 'İslam İnancında İncil', '#fff', kalin=True)
    ic += yazi(149, 50, 'Hz. İsa’ya Allah katından', LAC, kalin=True)
    ic += yazi(149, 74, 'indirilmiş TEK bir ilahi kitaptır.', YESIL_K, kalin=True)

    ic += kutu(308, 6, 286, 86, MOR_A, MOR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, MOR, MOR, 9, 1)
    ic += yazi(451, 24, 'Günümüzdeki Dört İncil', '#fff', kalin=True)
    ic += yazi(451, 50, 'Matta, Markos, Luka ve Yuhanna:', LAC, kalin=True)
    ic += yazi(451, 74, 'Hz. İsa’dan sonra yazılan metinler.', MOR, kalin=True)
    return svg(600, 98, ic, 'İslam inancındaki tek İncil ile Hristiyanlıktaki dört İncil metnini karşılaştıran pano.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = suhuf_dagilim_semasi()
    s[4]['gorsel'] = uc_ilahi_kitap_panosu()
    s[5]['gorsel'] = vahiy_bilgi_kartlari()
    s[6]['gorsel'] = maide_46_dogrulama_karti()
    s[7]['gorsel'] = kronolojik_vahiy_zinciri()
    s[8]['gorsel'] = iki_ayri_soru_karti()
    s[10]['gorsel'] = peygamber_kitap_butunlugu()
    s[11]['gorsel'] = dort_incil_tek_incil_panosu()
