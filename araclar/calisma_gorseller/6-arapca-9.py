"""6. sınıf Arapça 9. hafta (Geniş Aile Diyalogları, İsim Tamlaması, Şemsi-Kameri Harfler ve 1. Ünite Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 11 pt, Arapça yazı Arial 20 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="10.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="19"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def semsi_kameri_meslek_kartlari():
    kartlar = [
        ('1. Kart', 'اَلْبَيْطَرِيُّ', MAVI, MAVI_A),
        ('2. Kart', 'اَلْمُحامي', YES, YES_A),
        ('3. Kart', 'اَلضّابِطُ', TUR, TUR_A),
        ('4. Kart', 'اَلْفَلّاحُ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Şemsi ve kameri harfle başlayan dört meslek kartı.', 16)


def akraba_fiil_uyum_kartlari():
    kartlar = [
        ('1', 'خالَتي مُمَرِّضَةٌ', YES, YES_A),
        ('2', 'جَدّي فَلّاحٌ', MAVI, MAVI_A),
        ('3', 'بِنْتُ الْعَمِّ طَبّاخَةٌ', TUR, TUR_A),
        ('4', 'وَلَدُ الْخالِ شُرْطِيٌّ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 12, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 102, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Dört akraba ve meslek cümle kartı.', 16)


def anne_meslek_diyalog_panosu():
    ic = f'<rect x="6" y="6" width="348" height="38" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 29, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(210, 31, 'ما مِهْنَةُ والِدَتِكِ؟', LAC)

    ic += f'<rect x="6" y="50" width="348" height="38" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 73, 'Cevap (Ev hanımı):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(245, 75, '؟', YESIL_K)
    return svg(360, 94, ic, 'Annenin mesleğini soran Arapça diyalog kartı.', 16)


def dort_tamlama_kontrol_karti():
    kartlar = [
        ('A', 'وَلَدُ الْعَمِّ', MAVI, MAVI_A),
        ('B', 'بِنْتُ الْخالَةِ', YES, YES_A),
        ('C', 'رَبَّةُ الْبَيْتِ', TUR, TUR_A),
        ('D (!)', 'اَلْوَلَدُ الْخالِ', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 110, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'İsim tamlaması kuralını sınayan dört kart.', 16)


def eril_disil_donusum_karti():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, 'Eril Cümle (Dayım)', MAVI, kalin=True)
    ic += ar_yazi(91, 50, 'خالي طَبّاخٌ ماهِرٌ', LAC)
    ic += tr_yazi(91, 72, 'Dayım usta bir aşçıdır', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, 'Dişil Cümle (Halam)', MOR, kalin=True)
    ic += ar_yazi(269, 50, 'عَمَّتي ... ...', MOR)
    ic += tr_yazi(269, 72, 'Müennes biçime çeviriniz', LAC)
    return svg(360, 88, ic, 'Eril meslek ve sıfat cümlesini dişil yapıya dönüştürme kartı.', 15)


def diyalog_akisi_kartlari():
    kartlar = [
        ('1. Adım', 'مَنْ هٰذا الرَّجُلُ؟', MAVI, MAVI_A),
        ('2. Adım', 'هٰذا عَمّي سَليمٌ', YES, YES_A),
        ('3. Adım', 'ما مِهْنَتُهُ؟', TUR, TUR_A),
        ('4. Adım', 'هُوَ بَيْطَرِيٌّ في الْمَزْرَعَةِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Akraba tanıtımı ve çalışma yeri diyalog adımları.', 16)


def akraba_calisma_yeri_tablosu():
    satirlar = [
        ('Amca (الْعَمّ)', 'Okulda (في الْمَدْرَسَةِ)', MAVI, MAVI_A),
        ('Teyze (الْخالَة)', 'Hastanede (في الْمُسْتَشْفى)', YES, YES_A),
        ('Dede (الْجَدّ)', 'Tarlada (في الْحَقْلِ)', TUR, TUR_A),
        ('Hala (الْعَمَّة)', 'Mahkemede / Ofiste (مُحامِيَة)', MOR, MOR_A),
    ]
    ic = ''
    for i, (kisi, yer, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 86, y + 17, kisi, renk, kalin=True)
        ic += tr_yazi(x + 86, y + 32, yer, LAC)
    return svg(360, 94, ic, 'Dört akrabanın çalışma yerlerini gösteren bilgi kartları.', 16)


def semsi_kameri_karsilastirma_panosu():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, '1. Şemsi Harf Örneği', TUR, kalin=True)
    ic += ar_yazi(91, 50, 'اَلطَّبّاخُ (Et-tabbâhu)', LAC)
    ic += tr_yazi(91, 72, 'İlk harf: ط (Şeddeli)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, '2. Kameri Harf Örneği', MAVI, kalin=True)
    ic += ar_yazi(269, 50, 'اَلْمُعَلِّمُ (El-muallimu)', LAC)
    ic += tr_yazi(269, 72, 'İlk harf: م (Lam cezimli)', LAC)
    return svg(360, 88, ic, 'Şemsi ve kameri harfle başlayan iki meslek kelimesinin okunuş panosu.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = semsi_kameri_meslek_kartlari()
    s[2]['gorsel'] = akraba_fiil_uyum_kartlari()
    s[5]['gorsel'] = anne_meslek_diyalog_panosu()
    s[6]['gorsel'] = dort_tamlama_kontrol_karti()
    s[7]['gorsel'] = eril_disil_donusum_karti()
    s[8]['gorsel'] = diyalog_akisi_kartlari()
    s[9]['gorsel'] = akraba_calisma_yeri_tablosu()
    s[11]['gorsel'] = semsi_kameri_karsilastirma_panosu()
