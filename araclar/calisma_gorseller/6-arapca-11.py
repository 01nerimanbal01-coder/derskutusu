"""6. sınıf Arapça 11. hafta (Ev Eşyaları ve Günlük Etkinlikler: Odalardaki Eşyalar, Muzâri Fiiller ve Diyaloglar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe yazı Noto Sans 10.5 pt, Arapça yazı Arial 19 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="10.2"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def tr_yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def oda_esya_uyum_kartlari():
    kartlar = [
        ('1. Kart', 'غُرْفَةُ الْجُلُوسِ : أَرِيكَةٌ', MAVI, MAVI_A),
        ('2. Kart', 'غُرْفَةُ النَّوْمِ : سَرِيرٌ', YES, YES_A),
        ('3. Kart (!)', 'اَلْمَطْبَخُ : وِسَادَةٌ', KIR, KIR_A),
        ('4. Kart', 'غُرْفَةُ الدِّرَاسَةِ : حَاسُوبٌ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 112, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Dört oda ve eşya eşleştirme kartı.', 16)


def aile_etkinlik_tablo_kartlari():
    kartlar = [
        ('1', 'اَلْأَبُ عَلَى الْأَرِيكَةِ', MAVI, MAVI_A),
        ('2', 'اَلْأُمُّ فِي الْمَطْبَخِ', YES, YES_A),
        ('3', 'اَلْأَخُ عَلَى السَّرِيرِ', TUR, TUR_A),
        ('4', 'اَلْأُخْتُ فِي غُرْفَةِ الدِّرَاسَةِ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 10, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 100, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Aile bireylerinin bulunduğu odaları gösteren dört kart.', 16)


def nine_etkinlik_diyalog_panosu():
    ic = f'<rect x="6" y="6" width="348" height="38" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 29, 'Soru:', MAVI, 'start', kalin=True)
    ic += ar_yazi(210, 31, 'مَاذَا تَفْعَلُ جَدَّتِي فِي غُرْفَةِ الْجُلُوسِ؟', LAC)

    ic += f'<rect x="6" y="50" width="348" height="38" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += tr_yazi(14, 73, 'Cevap (Oturuyor ve okuyor):', YESIL_K, 'start', kalin=True)
    ic += ar_yazi(260, 75, 'هِيَ تَجْلِسُ ...', YESIL_K)
    return svg(360, 94, ic, 'Ninenin oturma odasında ne yaptığını soran diyalog panosu.', 16)


def muzari_uyum_kontrol_kartlari():
    kartlar = [
        ('A', 'يَكْتُبُ الْوَلَدُ الْوَاجِبَ', MAVI, MAVI_A),
        ('B', 'تَطْبُخُ الْأُمُّ الطَّعَامَ', YES, YES_A),
        ('C (!)', 'يَنَامُ الْأُخْتُ عَلَى السَّرِيرِ', KIR, KIR_A),
        ('D', 'تُشَاهِدُ الْبِنْتُ التِّلْفَازَ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 104, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Muzâri fiil ve özne uyumunu sınayan dört kart.', 16)


def kardes_okuma_donusum_karti():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, 'Eril Cümle (أَخِي)', MAVI, kalin=True)
    ic += ar_yazi(91, 50, 'يَقْرَأُ أَخِي الْكِتَابَ', LAC)
    ic += tr_yazi(91, 72, 'Erkek kardeşim kitap okuyor', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, 'Dişil Cümle (أُخْتِي)', MOR, kalin=True)
    ic += ar_yazi(269, 50, '... أُخْتِي الْكِتَابَ', MOR)
    ic += tr_yazi(269, 72, 'Müennes biçime çeviriniz', LAC)
    return svg(360, 88, ic, 'Muzâri fiil cümlesini eril özneden dişil özneye dönüştürme kartı.', 15)


def calisma_odasi_diyalog_adimlari():
    kartlar = [
        ('1. Adım', 'مَاذَا يُوجَدُ فِي الْغُرْفَةِ؟', MAVI, MAVI_A),
        ('2. Adım', 'مَكْتَبٌ وَكُرْسِيٌّ وَمَكْتَبَةٌ', YES, YES_A),
        ('3. Adım', 'مَاذَا يَفْعَلُ وَالِدُكَ؟', TUR, TUR_A),
        ('4. Adım', 'يَجْلِسُ وَيَقْرَأُ الْجَرِيدَةَ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ar_metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 8, y + 23, bas, renk, 'start', kalin=True)
        ic += ar_yazi(x + 106, y + 26, ar_metin, LAC)
    return svg(360, 94, ic, 'Çalışma odasındaki eşyalar ve babanın etkinliği diyalog adımları.', 16)


def ev_plani_etkinlik_tablosu():
    satirlar = [
        ('Mutfak (اَلْمَطْبَخُ)', 'ثَلَّاجَةٌ وَفُرْنٌ (Buzdolabı-Fırın)', MAVI, MAVI_A),
        ('Oturma Odası', 'يُشَاهِدُ الْجَدُّ التِّلْفَازَ (Dede TV)', YES, YES_A),
        ('Çalışma Odası', 'تَكْتُبُ زَيْنَبُ الْوَاجِبَ (Ödev)', TUR, TUR_A),
        ('Yatak Odası', 'يَنَامُ الطِّفْلُ عَلَى السَّرِيرِ (Yatak)', MOR, MOR_A),
    ]
    ic = ''
    for i, (oda, bilgi, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="172" height="38" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += tr_yazi(x + 86, y + 16, oda, renk, kalin=True)
        ic += tr_yazi(x + 86, y + 32, bilgi, LAC)
    return svg(360, 94, ic, 'Ev odalarındaki eşya ve etkinlikleri gösteren bilgi kartları.', 16)


def ya_ta_muzari_karsilastirma():
    ic = f'<rect x="6" y="6" width="170" height="76" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += tr_yazi(91, 22, '1. Müzekker (Eril Özne)', TUR, kalin=True)
    ic += ar_yazi(91, 50, 'يَجْلِسُ أَحْمَدُ', LAC)
    ic += tr_yazi(91, 72, 'Ön ek: يَـ (Yâ harfi)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += tr_yazi(269, 22, '2. Müennes (Dişil Özne)', MAVI, kalin=True)
    ic += ar_yazi(269, 50, 'تَجْلِسُ فَاطِمَةُ', LAC)
    ic += tr_yazi(269, 72, 'Ön ek: تَـ (Tâ harfi)', LAC)
    return svg(360, 88, ic, 'Müzekker ve müennes öznelerde muzâri fiil ön eki karşılaştırma panosu.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = oda_esya_uyum_kartlari()
    s[2]['gorsel'] = aile_etkinlik_tablo_kartlari()
    s[5]['gorsel'] = nine_etkinlik_diyalog_panosu()
    s[6]['gorsel'] = muzari_uyum_kontrol_kartlari()
    s[7]['gorsel'] = kardes_okuma_donusum_karti()
    s[8]['gorsel'] = calisma_odasi_diyalog_adimlari()
    s[9]['gorsel'] = ev_plani_etkinlik_tablosu()
    s[11]['gorsel'] = ya_ta_muzari_karsilastirma()
