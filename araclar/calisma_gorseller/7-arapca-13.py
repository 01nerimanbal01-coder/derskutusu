"""7. sınıf Arapça 13. hafta (Mevsimler ve Hava Olayları) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT_TR = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
FONT_AR = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="16"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_TR} font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT_AR} fill="{renk}">{metin}</text>'


def ankara_hava_karti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, 'Hava Tahmini (حَالَةُ الطَّقْسِ)', MAVI, kalin=True)
    ic += yazi_ar(92, 56, 'الْمَدِينَةُ: أَنْقَرَةُ (فَصْلُ الشِّتَاءِ)', LAC)
    ic += yazi(92, 86, 'Sıcaklık: -3 °C (Kar Yağışlı)', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 24, 'Durum Özeti', CAM, kalin=True)
    ic += yazi_ar(269, 56, 'الطَّقْسُ بَارِدٌ وَمُثْلِجٌ', LAC)
    ic += yazi(269, 86, 'Soğuk (بَارِدٌ) + Karlı (مُثْلِجٌ)', CAM, kalin=True)
    return svg(ic, 'Ankara kış mevsimi soğuk ve karlı hava durumu kartı.')


def dort_mevsim_kartlari():
    kartlar = [
        (6, 6, '1. فَصْلُ الرَّبِيعِ', 'İlkbahar — مُعْتَدِلٌ', YES, YES_A),
        (184, 6, '2. فَصْلُ الصَّيْفِ', 'Yaz — حَارٌّ وَمُشْمِسٌ', TUR, TUR_A),
        (6, 60, '3. فَصْلُ الْخَرِيفِ', 'Sonbahar — مُمْطِرٌ وَعَاصِفٌ', MOR, MOR_A),
        (184, 60, '4. فَصْلُ الشِّتَاءِ', 'Kış — بَارِدٌ وَمُثْلِجٌ', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 22, b1, r)
        ic += yazi(x + 85, y + 41, b2, LAC, kalin=True)
    return svg(ic, 'Dört mevsimin Arapça isimleri ve hava özellikleri.')


def baglac_semsiye_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 24, 'Sebep-Sonuç Cümlesi (أَدَوَاتُ الرَّبْطِ)', TUR, kalin=True)
    ic += yazi_ar(180, 56, 'أَحْمِلُ الْمِظَلَّةَ [ ..... ] الْجَوَّ مُمْطِرٌ الْيَوْمَ', LAC)
    ic += yazi(180, 88, 'Şemsiyeyi taşıyorum [ çünkü ] bugün hava yağmurludur.', MAVI, kalin=True)
    return svg(ic, 'Şemsiye taşıma nedenini açıklayan Arapça bağlaç kartı.')


def termometre_kartlari():
    kartlar = [
        (6, 6, '1. Kart: 35 °C (Yaz)', 'حَارٌّ جِدًّا — أَشْعُرُ بِالْحَرِّ', KIR, KIR_A),
        (184, 6, '2. Kart: 20 °C (Bahar)', 'مُعْتَدِلٌ — مَا أَجْمَلَ الْجَوَّ!', YES, YES_A),
        (6, 60, '3. Kart: -5 °C (Kış?)', 'حَارٌّ وَمُشْمِسٌ فِي الصَّيْفِ (؟)', MOR, MOR_A),
        (184, 60, '4. Kart: 10 °C (Güz)', 'مُمْطِرٌ وَغَائِمٌ فِي الْخَرِيفِ', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 19, b1, r, kalin=True)
        ic += yazi_ar(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört farklı sıcaklık derecesi ve Arapça hava durumu eşleştirmesi.')


def ceviri_balonu_karti():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 24, 'Günlük Hava Durumu Konuşması', MAVI, kalin=True)
    ic += yazi_ar(180, 58, 'الْجَوُّ مُشْمِسٌ الْيَوْمَ لٰكِنْ بَارِدٌ؛ لِذٰلِكَ أَلْبَسُ الْمِعْطَفَ السَّمِيكَ.', LAC)
    ic += yazi(180, 90, 'İpucu: مُشْمِسٌ (güneşli) · لٰكِنْ (fakat) · لِذٰلِكَ (bu yüzden) · الْمِعْطَفَ (palto)', CAM, kalin=True)
    return svg(ic, 'Güneşli fakat soğuk havada palto giyme cümlesi.')


def mevsim_dongusu_adimlari():
    adimlar = [
        (6, '1. İlkbahar', 'الرَّبِيعُ', YES, YES_A),
        (94, '2. Yaz', 'الصَّيْفُ', TUR, TUR_A),
        (182, '3. Sonbahar', 'الْخَرِيفُ', MOR, MOR_A),
        (270, '4. Kış', 'الشِّتَاءُ', MAVI, MAVI_A),
    ]
    ic = ''
    for x, ad, ar, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 34, ad, r, kalin=True)
        ic += yazi_ar(x + 42, 72, ar, LAC)
    return svg(ic, 'İlkbahardan kışa dört mevsimin sıralı döngüsü.')


def ayet_denge_karti():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 24, 'Kâinattaki İlahi Ölçü (Yûnus Suresi, 5. Ayet)', YES, kalin=True)
    ic += yazi_ar(180, 56, 'هُوَ الَّذِي جَعَلَ الشَّمْسَ ضِيَاءً وَالْقَمَرَ نُورًا وَقَدَّرَهُ مَنَازِلَ', LAC)
    ic += yazi_ar(180, 88, 'لِتَعْلَمُوا عَدَدَ السِّنِينَ وَالْحِسَابَ', YES)
    return svg(ic, 'Yûnus suresi 5. ayette Güneş, Ay ve yılların hesabı.')


def mevsim_yazma_ipucu():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 24, '1. Kalıp: Sevdiğim Mevsim', YES, kalin=True)
    ic += yazi_ar(92, 56, 'أُحِبُّ فَصْلَ الرَّبِيعِ / الصَّيْفِ', LAC)
    ic += yazi(92, 86, 'لِأَنَّ الْجَوَّ مُعْتَدِلٌ وَمُشْمِسٌ', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 24, '2. Kalıp: Beğeni İfadesi', CAM, kalin=True)
    ic += yazi_ar(269, 56, 'مَا أَجْمَلَ الْجَوَّ فِي الرَّبِيعِ!', LAC)
    ic += yazi(269, 86, '(Baharda hava ne kadar güzel!)', CAM, kalin=True)
    return svg(ic, 'Sevilen mevsimi ve nedenini yazma ipucu kartları.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ankara_hava_karti()
    s[2]['gorsel'] = dort_mevsim_kartlari()
    s[5]['gorsel'] = baglac_semsiye_karti()
    s[6]['gorsel'] = termometre_kartlari()
    s[7]['gorsel'] = ceviri_balonu_karti()
    s[8]['gorsel'] = mevsim_dongusu_adimlari()
    s[9]['gorsel'] = ayet_denge_karti()
    s[11]['gorsel'] = mevsim_yazma_ipucu()
