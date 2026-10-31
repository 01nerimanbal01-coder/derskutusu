"""5. sınıf Arapça 5. hafta (Tanışma-Vedalaşma Diyalogları, Sınıf İçi Yönergeler, Cezm ve Şedde İle Kelime Okuma-Yazma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def cezm_sedde_kartlari():
    kartlar = [
        ('1. Kart', 'مَنْ', MAVI, MAVI_A),
        ('2. Kart', 'هَلْ', YES, YES_A),
        ('3. Kart', 'مُعَلِّمٌ', TUR, TUR_A),
        ('4. Kart', 'مِنْ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, kel, LAC)
    return svg(360, 96, ic, 'Cezimli ve şeddeli dört kelime kartı: men, hel, muallimün, min.', 18)


def sinif_eylem_panolari():
    kartlar = [
        ('K · Kerem (E)', 'اِفْتَحْ!', MAVI, MAVI_A),
        ('L · Selma (K)', 'اِسْتَمِعِي!', YES, YES_A),
        ('M · Yusuf (E)', 'اُنْظُرْ!', TUR, TUR_A),
        ('N · Zeynep (K)', 'أَغْلِقْ!', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, emir, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 128, y + 31, emir, LAC)
    return svg(360, 110, ic, 'Aç, dinle, bak ve kapat sınıf yönergesi panoları.', 18)


def okuma_isaretleri_kartlari():
    kartlar = [
        ('1. Kelime', 'هَلْ', MAVI, MAVI_A),
        ('2. Kelime', 'أُمٌّ', YES, YES_A),
        ('3. Kelime', 'جَدٌّ', TUR, TUR_A),
        ('4. Kelime', 'شُكْرًا', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 41, 25, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="33" x2="{x + 72}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 41, 68, kel, LAC)
    return svg(360, 96, ic, 'Hel, ümmün, ceddün ve şükran kelime inceleme kartları.', 18)


def cezm_sedde_karsilastirma():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Cezm (Sükûn) Örneği', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'مَنْ', LAC)
    ic += tr_yazi(91, 80, 'Men (Tek hecede bağlanır)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Şedde Örneği', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'جَدٌّ', LAC)
    ic += tr_yazi(269, 80, 'Ced-dün (İki kez okunur)', LAC)
    return svg(360, 100, ic, 'Men ve ceddün kelimelerinde cezm ile şedde karşılaştırması.', 18)


def butuncul_diyalog_halkalari():
    halkalar = [
        ('Halka K', 'كَيْفَ حَالُكِ؟', TUR, TUR_A),
        ('Halka L', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('Halka M', 'فِي أَمَانِ اللَّهِ', MOR, MOR_A),
        ('Halka N', 'مَا اسْمُكِ؟', YES, YES_A),
    ]
    ic = ''
    for i, (bas, soz, renk, arka) in enumerate(halkalar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 122, y + 31, soz, LAC)
    return svg(360, 110, ic, 'Bütüncül diyalog zincirinin dört halkası.', 18)


def sedde_acilim_semasi():
    ic = f'<rect x="6" y="6" width="144" height="84" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(78, 24, 'Şeddeli Kelime', MOR, kalin=True)
    ic += ar_yazi(78, 62, 'أُمٌّ', LAC)

    ic += f'<rect x="160" y="6" width="194" height="84" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(257, 24, 'Harf Açılımı (Üm - mün)', YESIL_K, kalin=True)
    ic += ar_yazi(257, 62, 'أُ - ؟ - ؟', YESIL_K)
    return svg(360, 96, ic, 'Ümmün kelimesindeki şeddeli mîm harfinin açılım şeması.', 18)


def guzel_soz_hadis_panosu():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += tr_yazi(180, 24, 'İletişim Ahlakı · Hadis-i Şerif', YESIL_K, kalin=True)
    ic += ar_yazi(180, 56, 'اَلْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ', LAC)
    ic += tr_yazi(180, 82, 'Güzel söz sadakadır. (Tebessüm ve nezaket)', LAC)
    return svg(360, 104, ic, 'Güzel söz sadakadır hadis-i şerif panosu.', 18)


def muallimun_sedde_alti_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Şedde Üstü Çizgi (Fetha)', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'تَشَرَّفْتُ', LAC)
    ic += tr_yazi(91, 80, 'Te - şer - raf - tü (-ra)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Şedde Altı Çizgi (Kesra)', TUR, kalin=True)
    ic += ar_yazi(269, 56, 'مُعَلِّمٌ', LAC)
    ic += tr_yazi(269, 80, 'Mu - al - li - mün (-li)', LAC)
    return svg(360, 100, ic, 'Şedde üstü fetha ve şedde altı kesra yazım karşılaştırması.', 18)


def tenvin_tablosu_panosu():
    kutular = [
        ('İki Üstün (-en)', 'مَرْحَبًا', TUR, TUR_A),
        ('İki Esre (-in)', 'بِخَيْرٍ', YES, YES_A),
        ('İki Ötre (-ün)', 'تِلْمِيذٌ', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, kel, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 56, 24, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="32" x2="{x + 102}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += ar_yazi(x + 56, 68, kel, LAC)
    return svg(360, 96, ic, 'İki üstün, iki esre ve iki ötre tenvin örnekleri.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cezm_sedde_kartlari()
    s[4]['gorsel'] = sinif_eylem_panolari()
    s[5]['gorsel'] = okuma_isaretleri_kartlari()
    s[6]['gorsel'] = cezm_sedde_karsilastirma()
    s[7]['gorsel'] = butuncul_diyalog_halkalari()
    s[8]['gorsel'] = sedde_acilim_semasi()
    s[9]['gorsel'] = guzel_soz_hadis_panosu()
    s[11]['gorsel'] = muallimun_sedde_alti_karti()
    s[12]['gorsel'] = tenvin_tablosu_panosu()
