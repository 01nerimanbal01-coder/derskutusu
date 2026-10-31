"""6. sınıf Arapça 8. hafta (Geniş Aile Bireyleri, Meslekler, Nerede Çalışıyor?, İsim Tamlaması ve Aile Hadisleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 12 pt, Arapça yazı Arial 22 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="22"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:17mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def aile_meslek_kartlari():
    kartlar = [
        ('1. Kart', 'خالَتي مُمَرِّضَة', YES, YES_A),
        ('2. Kart', 'عَمّي سائِق', MAVI, MAVI_A),
        ('3. Kart', 'جَدّي فَلّاح', TUR, TUR_A),
        ('4. Kart', 'والِدي شُرْطِيّ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört akraba ve meslek tanıtım kartı.', 22)


def meslek_sifat_kartlari():
    kartlar = [
        ('K', 'شُرْطِيٌّ نَشيطٌ', MAVI, MAVI_A),
        ('L', 'طَبّاخَةٌ ماهِرَةٌ', YES, YES_A),
        ('M', 'مُعَلِّمَةٌ ماهِرٌ', KIR, '#fdeaea'),
        ('N', 'فَلّاحٌ نَشيطٌ', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 105, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Meslek ve sıfat uyumu cümle kartları.', 22)


def isim_tamlamasi_kartlari():
    kartlar = [
        ('1', 'وَلَدُ الْخالَةِ', MAVI, MAVI_A),
        ('2', 'بِنْتُ الْعَمَّةِ', YES, YES_A),
        ('3', 'وَلَدُ الْعَمِّ', TUR, TUR_A),
        ('4', 'رَبَّةُ الْبَيْتِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 14, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört Arapça isim tamlaması kartı.', 22)


def calisma_yeri_soru_panosu():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 24, 'Eril Özne Sorusu', MAVI, kalin=True)
    ic += ar_yazi(91, 56, 'أَيْنَ يَعْمَلُ؟', LAC)
    ic += tr_yazi(91, 80, 'Nerede çalışıyor? (Erkek)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 24, 'Dişil Özne Sorusu', MOR, kalin=True)
    ic += ar_yazi(269, 56, 'أَيْنَ تَعْمَلُ؟', LAC)
    ic += tr_yazi(269, 80, 'Nerede çalışıyor? (Kadın)', LAC)
    return svg(360, 100, ic, 'Eril ve dişil öznelerde çalışma yeri soru kalıpları.', 21)


def aile_kusaklari_semasi():
    kartlar = [
        ('Kuşak A', 'جَدّ - جَدَّة', MAVI, MAVI_A),
        ('Kuşak B', 'والِد - والِدَة', YES, YES_A),
        ('Kuşak C', 'وَلَد - بِنْت', TUR, TUR_A),
        ('Kuşak D', 'حَفيد - حَفيدَة', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 52
        ic += f'<rect x="{x}" y="{y}" width="172" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 28, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 116, y + 31, ar_metin, LAC)
    return svg(360, 110, ic, 'Dört nesil aile kuşakları kartları.', 22)


def aile_hadis_panosu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.4"/>'
    ic += ar_yazi(180, 34, 'خَيْرُكُمْ خَيْرُكُمْ لِأَهْلِهِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += ar_yazi(180, 86, 'اَلْأَقْرَبُونَ أَوْلَى بِالْمَعْرُوفِ', LAC)
    return svg(360, 110, ic, 'Aileye ve yakın akrabalara iyiliği öğütleyen iki hikmetli söz panosu.', 22)


def ogretmen_calisma_diyalogu():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 33, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(210, 35, 'أَيْنَ تَعْمَلُ الْمُعَلِّمَةُ؟', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(16, 85, 'Cevap (Okulda):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(235, 87, '؟', YESIL_K)
    return svg(360, 110, ic, 'Kadın öğretmenin nerede çalıştığını soran diyalog kartı.', 22)


def olumlu_olumsuz_cumle_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, 'Olumlu:', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(215, 35, 'تَعْمَلُ الطَّبّاخَةُ في الْمَطْبَخِ', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, 'Olumsuz:', KIR, 'start', kalin=True)
    ic += ar_yazi(215, 87, 'لا تَعْمَلُ الطَّبّاخَةُ في الصَّفِّ', LAC)
    return svg(360, 110, ic, 'Aşçının çalışma yeriyle ilgili olumlu ve olumsuz Arapça cümle kartları.', 22)


def akraba_soru_cevap_karti():
    ic = f'<rect x="6" y="6" width="348" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 33, '1. Kart:', MAVI, 'start', kalin=True)
    ic += ar_yazi(210, 35, 'كَمْ عَمًّا لَكَ؟ - ثَلاثَة', LAC)

    ic += f'<rect x="6" y="58" width="348" height="46" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 85, '2. Kart:', TUR, 'start', kalin=True)
    ic += ar_yazi(210, 87, 'هَلِ الْحَفيدَةُ مُحامِيَةٌ؟', LAC)
    return svg(360, 110, ic, 'Amca sayısı ve kız torunun mesleğiyle ilgili iki soru kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = aile_meslek_kartlari()
    s[4]['gorsel'] = meslek_sifat_kartlari()
    s[5]['gorsel'] = isim_tamlamasi_kartlari()
    s[6]['gorsel'] = calisma_yeri_soru_panosu()
    s[7]['gorsel'] = aile_kusaklari_semasi()
    s[8]['gorsel'] = aile_hadis_panosu()
    s[9]['gorsel'] = ogretmen_calisma_diyalogu()
    s[11]['gorsel'] = olumlu_olumsuz_cumle_karti()
    s[12]['gorsel'] = akraba_soru_cevap_karti()
