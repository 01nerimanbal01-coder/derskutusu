"""6. sınıf Sosyal Bilgiler 13. hafta (Türkistan’da Kurulan İlk Türk Devletleri ve Medeniyet Mirasımız) görselleri.
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
        ('Asya Hun Devleti (Ötüken)', 'İlk Türk devleti · Onlu Sistem', TUR, TUR_A),
        ('I. Kök Türk Devleti (552)', 'Türk adını kullanan ilk devlet', MAVI, MAVI_A),
        ('II. Kök Türk (Kutluk) Devleti', '38 harfli alfabe · Orhun Yazıtları', CAM, CAM_A),
        ('Uygur Devleti (Karabalğasun)', 'Yerleşik hayat · Kâğıt ve Matbaa', YES, YES_A),
    ], 'Türkistan’da kurulan ilk Türk devletleri ve temel özellikleri.')
    s[2]['gorsel'] = dortlu_kart([
        ('1. 12 Hayvanlı Türk Takvimi', 'Astronomi ve Bilim Mirası', MAVI, MAVI_A),
        ('2. Pazırık Halısı', 'En eski düğümlü halı (Dokuma)', TUR, TUR_A),
        ('3. Altın Elbiseli Adam', 'Zırh ve Maden İşçiliği Sanatı', MOR, MOR_A),
        ('4. İpek Yolu Ticareti', 'Kıtalararası Ekonomi ve Kültür', YES, YES_A),
    ], 'İlk Türk devletlerinin bilim, sanat, maden ve ekonomi mirası.')
    s[5]['gorsel'] = ikili_kart(
        'Orhun Yazıtları (Bilge Kağan)', '«Gece uyumadım, gündüz oturmadım;', 'aç milleti doyurdum, çıplak milleti giydirdim.»', MAVI, MAVI_A,
        'Devlet Yönetimi İlkesi', 'Halkın refahı ve huzuru esastır', '→ Sosyal Devlet Anlayışı', YES, YES_A,
        'Orhun Yazıtları’nda sosyal devlet ve halka hizmet anlayışı.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Türk Hukuk Sistemi: TÖRE', 'Kaynak: Kurultay kararları ve gelenek', 'Temel İlkeler: Adalet (Könilik), İyilik, Eşitlik', MOR, MOR_A,
        'Hukukun Üstünlüğü', '«İlge (Devlet) bırakılır, töre bırakılmaz.»', 'Kağan dahil herkes töreye bağlıdır!', YES, YES_A,
        'İlk Türk devletlerinde töre ve hukukun üstünlüğü ilkesi.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Konargöçer Yaşam (Hun & Kök Türk)', 'Yaylak – Kışlak · Hayvancılık', 'Sanat: Taşınabilir halı, kemer, silah', TUR, TUR_A,
        'Yerleşik Yaşam (Uygurlar)', 'Tarım · Şehir ve Saray Mimarisi', 'Sanat: Fresk (duvar resmi) ve minyatür', YES, YES_A,
        'Konargöçer ve yerleşik yaşamın Türk sanatına yansımaları.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Asya Hun Devleti (MÖ 220/209)', 'Teoman ve Metehan · Onlu Sistem', TUR, TUR_A),
        ('2. I. Kök Türk Devleti (552)', 'Bumin Kağan · İstemi Yabgu', MAVI, MAVI_A),
        ('3. Orhun Yazıtları (732–735)', 'II. Kök Türk · Bilge Kağan & Tonyukuk', CAM, CAM_A),
        ('4. Uygur Devleti (744–840)', 'Yerleşik yaşam, kâğıt ve matbaa', YES, YES_A),
    ], 'İlk Türk devletlerinin kronolojik tarihsel gelişim şeması.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Pazırık Halısı', 'Hayvancılık ve yün dokumacılığı', TUR, TUR_A),
        ('2. Demir Kılıç ve Ok Uçları', 'Demir madenciliği ve askerlik', MAVI, MAVI_A),
        ('3. Altın Elbiseli Adam', 'Kuyumculuk ve maden sanatı', MOR, MOR_A),
        ('4. Sulama Kanalı ve Saban (✓)', 'Tarımsal üretim ve yerleşik yaşam', YES, YES_A),
    ], 'Arkeolojik buluntulardan ekonomik faaliyet ve yaşam tarzı çıkarımı.')
    s[11]['gorsel'] = ikili_kart(
        'Metehan ve Onlu Sistem (MÖ 209)', 'Onbaşı (10) · Yüzbaşı (100)', 'Binbaşı (1000) · Tümenbaşı (10 000)', MAVI, MAVI_A,
        'Tarihsel Miras ve Önemi', 'Türk Kara Kuvvetleri kuruluş yılı', 'Modern dünya ordularına örnek teşkilat', YES, YES_A,
        'Metehan’ın kurduğu Onlu Askerî Sistem ve günümüze mirası.'
    )
