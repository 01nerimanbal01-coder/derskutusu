"""6. sınıf Arapça 10. hafta (Evimin Bölümleri, Ev Eşyaları, Harf-i Cerler ve Bulunma Kalıpları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 10.5 pt, Arapça yazı Arial 18 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="10.2"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="17.5"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def esya_konum_kartlari():
    kartlar = [
        ('1. Kart', 'اَلْحَقِيبَةُ تَحْتَ الطَّاوِلَةِ', YES, YES_A),
        ('2. Kart', 'اَلْحَاسُوبُ عَلَى الطَّاوِلَةِ', MAVI, MAVI_A),
        ('3. Kart', 'اَلْكُرْسِيُّ أَمَامَ الطَّاوِلَةِ', TUR, TUR_A),
        ('4. Kart', 'اَلْمَكْتَبَةُ خَلْفَ الطَّاوِلَةِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Masa etrafındaki dört eşyanın konumunu gösteren Arapça kartlar.', 16)


def oda_esya_bulunma_kartlari():
    kartlar = [
        ('1', 'تِلْفَازٌ فِي غُرْفَةِ الْجُلُوسِ', MAVI, MAVI_A),
        ('2', 'غَسَّالَةٌ فِي الْحَمَّامِ', YES, YES_A),
        ('3', 'سَرِيرٌ فِي غُرْفَةِ النَّوْمِ', TUR, TUR_A),
        ('4', 'أَرِيكَةٌ فِي غُرْفَةِ الْجُلُوسِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 104, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Odalarda bulunan eşyaları gösteren dört cümle kartı.', 16)


def aile_oturma_diyalog_panosu():
    ic = f'<rect x="6" y="6" width="348" height="38" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(12, 29, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(205, 31, 'أَيْنَ تَجْلِسُ الْأُسْرَةُ فِي الْمَسَاءِ؟', LAC)

    ic += f'<rect x="6" y="50" width="348" height="38" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(12, 73, 'Cevap (Oturma odasında):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(255, 75, '؟', YESIL_K)
    return svg(360, 94, ic, 'Ailenin akşam nerede oturduğunu soran Arapça diyalog panosu.', 16)


def harfi_cer_hareke_kartlari():
    kartlar = [
        ('A', 'اَلْكِتَابُ فِي الْحَقِيبَةِ', MAVI, MAVI_A),
        ('B', 'اَلْمِرْآةُ فَوْقَ الْمِغْسَلَةِ', YES, YES_A),
        ('C (!)', 'اَلْحَاسُوبُ عَلَى الطَّاوِلَةُ', KIR, KIR_A),
        ('D', 'اَلْحَدِيقَةُ خَلْفَ الْمَنْزِلِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 108, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Harf-i cer ve yer zarflarından sonraki son hareke kuralı kartları.', 16)


def zit_zarf_donusum_karti():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, '1. Konum (Önünde: أَمَامَ)', MAVI, kalin=True)
    ic += ar_yazi(91, 50, 'اَلسَّيَّارَةُ أَمَامَ الْبَيْتِ', LAC)
    ic += tr_yazi(91, 72, 'Araba evin önündedir', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, '2. Zıt Konum (Arkasında)', TUR, kalin=True)
    ic += ar_yazi(269, 50, 'اَلسَّيَّارَةُ ... الْبَيْتِ', TUR)
    ic += tr_yazi(269, 72, 'Zıt zarfla tamamlayınız', LAC)
    return svg(360, 88, ic, 'Önünde ve arkasında zıt anlamlı yer zarfları dönüşüm kartı.', 15)


def ev_ziyareti_diyalog_kartlari():
    kartlar = [
        ('1. Adım', 'أَهْلًا وَسَهْلًا، تَفَضَّلِي', MAVI, MAVI_A),
        ('2. Adım', 'شُكْرًا، بَيْتُكِ جَمِيلٌ', YES, YES_A),
        ('3. Adım', 'مَاذَا يُوجَدُ فِي الْغُرْفَةِ؟', TUR, TUR_A),
        ('4. Adım', 'يُوجَدُ حَاسُوبٌ وَتُوجَدُ مَكْتَبَةٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 114, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Ev ziyareti ve çalışma odası tanıtımı diyalog basamakları.', 16)


def kat_plani_esya_tablosu():
    satirlar = [
        ('غُرْفَةُ الْجُلُوسِ (Oturma O.)', 'أَرِيكَةٌ وَسَجَّادَةٌ (Kanepe, Halı)', MAVI, MAVI_A),
        ('اَلْمَطْبَخُ (Mutfak)', 'فُرْنٌ وَثَلَّاجَةٌ (Fırın, Buzdolabı)', YES, YES_A),
        ('غُرْفَةُ النَّوْمِ (Yatak O.)', 'سَرِيرٌ وَخِزَانَةٌ (Yatak, Dolap)', TUR, TUR_A),
        ('اَلْحَمَّامُ (Banyo)', 'غَسَّالَةٌ وَمِغْسَلَةٌ (Çamaşır Mak.)', MOR, MOR_A),
    ]
    ic = ''
    for i, (oda, esya, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 86, y + 16, oda, renk, kalin=True)
        ic += tr_yazi(x + 86, y + 32, esya, LAC)
    return svg(360, 94, ic, 'Evdeki dört bölüm ve içindeki eşyaları gösteren kat planı.', 16)


def yucedu_tucedu_karsilastirma():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, '1. Müzekker Eşya (يُوجَدُ)', MAVI, kalin=True)
    ic += ar_yazi(91, 50, 'يُوجَدُ كُرْسِيٌّ فِي الْغُرْفَةِ', LAC)
    ic += tr_yazi(91, 72, 'Odada sandalye vardır', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, '2. Müennes Eşya (تُوجَدُ)', YESIL_K, kalin=True)
    ic += ar_yazi(269, 50, 'تُوجَدُ طَاوِلَةٌ فِي الْغُرْفَةِ', LAC)
    ic += tr_yazi(269, 72, 'Odada masa vardır (ـة)', LAC)
    return svg(360, 88, ic, 'Müzekker ve müennes eşyalarda yûcedü ve tûcedü kullanım farkı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = esya_konum_kartlari()
    s[2]['gorsel'] = oda_esya_bulunma_kartlari()
    s[5]['gorsel'] = aile_oturma_diyalog_panosu()
    s[6]['gorsel'] = harfi_cer_hareke_kartlari()
    s[7]['gorsel'] = zit_zarf_donusum_karti()
    s[8]['gorsel'] = ev_ziyareti_diyalog_kartlari()
    s[9]['gorsel'] = kat_plani_esya_tablosu()
    s[11]['gorsel'] = yucedu_tucedu_karsilastirma()
