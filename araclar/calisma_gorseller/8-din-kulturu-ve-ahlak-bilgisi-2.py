"""8. sınıf Din Kültürü ve Ahlak Bilgisi 2. hafta (İnsanın İradesi ve Kader) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def irade_karsilastirma_sema():
    ic = kutu(6, 6, 286, 78, MOR_A, MOR, 9, 1.5)
    ic += yazi(149, 24, 'Küllî İrade (Allah’ın Mutlak İradesi)', 10.8, MOR)
    ic += yazi(149, 45, '• Anne-baba, ırk, göz rengi, kalp atışı', 10.1, LAC, ince=True)
    ic += yazi(149, 65, '• İnsan seçemediği için SORUMLU DEĞİLDİR', 10.1, MOR)

    ic += kutu(308, 6, 286, 78, YES_A, YES, 9, 1.5)
    ic += yazi(451, 24, 'Cüzî İrade (İnsanın Sınırlı İradesi)', 10.8, YES)
    ic += yazi(451, 45, '• Çalışmak, ibadet etmek, dürüst olmak', 10.1, LAC, ince=True)
    ic += yazi(451, 65, '• İnsan kendi seçtiği için SORUMLUDUR', 10.1, YES)
    return svg(600, 90, ic, 'Küllî irade ve cüzî irade alanları ile sorumluluk karşılaştırması.', 16)


def insanin_bes_ozelligi():
    kutular = [
        ('1. Akıl ve İrade', 'İyiyi kötüden ayırır', MAVI, MAVI_A),
        ('2. Düşünme', 'Tefekkür ve öğüt', TUR, TUR_A),
        ('3. Vahiy Rehberi', 'Kitap ve peygamber', MOR, MOR_A),
        ('4. Özgür Seçim', 'Baskısız tercih', YES, YES_A),
        ('5. Sorumluluk', 'Mükellef olma', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 66, z, r, 8, 1.4)
        ic += yazi(x + 56, 26, bas, 10.1, r)
        ic += yazi(x + 56, 50, alt, 9.6, LAC, ince=True)
    return svg(600, 78, ic, 'İnsanı diğer varlıklardan ayıran beş temel özellik.', 15)


def varlik_ve_sorumluluk_panosu():
    kartlar = [
        ('Cansız Varlıklar', 'Fiziksel yasalara uyar', 'Sorumluluğu yoktur', GRI, GRI_A),
        ('Bitki ve Hayvanlar', 'Biyolojik yasa ve içgüdü', 'Sorumluluğu yoktur', TUR, TUR_A),
        ('Akıllı ve İradeli İnsan', 'Cüzî iradeyle seçim yapar', 'Eylemlerinden sorumludur', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.6, r)
        ic += yazi(x + 96, 46, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.1, r)
    return svg(600, 86, ic, 'Varlık türlerinin irade ve sorumluluk açısından karşılaştırılması.', 16)


def fiil_olusum_sureci():
    adimlar = [
        ('1. Rehberlik', 'Akıl + Vahiy', MAVI, MAVI_A),
        ('2. Özgür Tercih', 'Cüzî İrade (İnsan)', TUR, TUR_A),
        ('3. Fiili Yaratma', 'Küllî İrade (Allah)', MOR, MOR_A),
        ('4. Karşılık', 'Sorumluluk (İnsan)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Akıl, cüzî irade, küllî irade ve sorumluluk süreci şeması.', 15)


def iki_yol_siralama_karti():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'İlahi Rehberlik (Beled 10 · İnsan 3)', 10.6, MAVI)
    ic += yazi(149, 46, '“Ona iki yolu (hayır ve şerri) gösterdik.”', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'Akıl ve vahiy doğru ile yanlışı bildirir.', 10.0, MAVI)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Özgür Seçim ve Sonuç (Nahl 93)', 10.6, YES)
    ic += yazi(451, 46, '“Yaptıklarınızdan sorumlu tutulacaksınız.”', 10.1, LAC, ince=True)
    ic += yazi(451, 63, 'Kul seçer, Allah yaratır, kul üstlenir.', 10.0, YES)
    return svg(600, 84, ic, 'İki yolun gösterilmesi ve özgür tercihin sorumluluk doğurması.', 16)


def yanlis_kader_algisi_karti():
    ic = kutu(6, 6, 286, 72, KIR_A, KIR, 8, 1.5)
    ic += yazi(149, 24, 'Hatalı Tutum ve Söylem', 10.8, KIR)
    ic += yazi(149, 46, 'Hiç ders çalışmayıp düşük not alınca:', 10.0, LAC, ince=True)
    ic += yazi(149, 63, '“Ne yapayım, talihim karaymış!”', 10.2, KIR)

    ic += kutu(308, 6, 286, 72, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'İslam’ın Doğru Kader Anlayışı', 10.8, YES)
    ic += yazi(451, 46, 'Kişi cüzî iradesiyle üzerine düşeni yapar;', 10.0, LAC, ince=True)
    ic += yazi(451, 63, 'ihmalinin suçunu kadere yükleyemez.', 10.1, YES)
    return svg(600, 84, ic, 'Yanlış kader söylemi ile doğru sorumluluk bilinci karşılaştırması.', 16)


def uc_ilke_panosu():
    ilkeler = [
        ('1. İlke · Beled Suresi 10', 'İnsana iyi ve kötü iki yolun', 'açıkça gösterilmesi', MAVI, MAVI_A),
        ('2. İlke · Bakara Suresi 286', 'Kimseye gücünün üstünde', 'yükümlülük yüklenmemesi', YES, YES_A),
        ('3. İlke · Tirmizî Hadisi', 'Kulun Allah’ı gözetip yalnız', 'O’nun takdirine güvenmesi', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(ilkeler):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.4, r)
        ic += yazi(x + 96, 46, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 96, 64, s2, 10.0, r)
    return svg(600, 86, ic, 'Kader ve sorumlulukla ilgili üç temel ayet ve hadis ilkesi.', 16)


def pusula_isik_karti():
    ic = kutu(6, 6, 286, 70, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Akıl · İçsel Pusula', 10.8, MAVI)
    ic += yazi(149, 46, 'Neden-sonuç bağı kurar, düşünür,', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'faydalı ile zararlıyı ayırt eder.', 10.1, MAVI)

    ic += kutu(308, 6, 286, 70, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Vahiy · Yolu Aydınlatan Işık', 10.8, TUR)
    ic += yazi(451, 46, 'Peygamberler ve ilahi kitaplarla', 10.1, LAC, ince=True)
    ic += yazi(451, 63, 'hak ile batılın sınırlarını gösterir.', 10.1, TUR)
    return svg(600, 82, ic, 'Aklın pusulaya, vahyin ise yolu aydınlatan ışığa benzetilmesi.', 15)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = irade_karsilastirma_sema()
    s[1]['gorsel'] = insanin_bes_ozelligi()
    s[3]['gorsel'] = varlik_ve_sorumluluk_panosu()
    s[5]['gorsel'] = fiil_olusum_sureci()
    s[6]['gorsel'] = iki_yol_siralama_karti()
    s[7]['gorsel'] = yanlis_kader_algisi_karti()
    s[8]['gorsel'] = uc_ilke_panosu()
    s[11]['gorsel'] = pusula_isik_karti()
