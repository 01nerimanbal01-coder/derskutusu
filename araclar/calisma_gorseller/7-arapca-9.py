"""7. sınıf Arapça 9. hafta (2. Ünite: Alışveriş — 2. Ders: Kırtasiyede, Fiyat Sorma, Bağlaçlar ve 11-19 Sayıları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe Noto Sans 10.5-11 pt, Arapça Arial 20-21 pt RTL (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#0284c7', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e0f2fe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True, boy=10.5):
    ag = '700' if kalin else '500'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle', boy=20):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" fill="{renk}">{metin}</text>'


def kirtasiye_istek_fisi():
    ic = kutu(4, 4, 352, 42, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 21, 'Müşteri', MAVI, 'start')
    ic += yazi_ar(215, 32, 'أُرِيدُ حَقِيبَةً جَدِيدَةً وَأَلْوَانًا مِنْ فَضْلِكَ', LAC)
    ic += kutu(4, 52, 352, 42, YES_A, YES, 8)
    ic += yazi_tr(14, 69, 'Satıcı', YES, 'start')
    ic += yazi_ar(215, 80, 'تَفَضَّلْ، عِنْدِي حَقِيبَةٌ جَمِيلَةٌ وَأَلْوَانٌ', LAC)
    return svg(360, 98, ic, 'Kırtasiye konuşma fişi: Müşteri yeni bir çanta ve boya kalemleri ister.', 15)


def fiyat_zamir_kartlari():
    kartlar = [
        (4, 4, '1. Kart (Eril)', 'بِكَمْ هٰذَا الْمِقَصُّ؟', MAVI, MAVI_A),
        (184, 4, '2. Kart (Dişil - ة)', 'بِكَمْ هٰذِهِ الْمِبْرَاةُ؟', TUR, TUR_A),
        (4, 52, '3. Kart (Eril)', 'بِكَمْ هٰذَا الدَّفْتَرُ؟', YES, YES_A),
        (184, 52, '4. Kart (Dişil - ة)', 'بِكَمْ هٰذِهِ الْمِسْطَرَةُ؟', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in kartlar:
        ic += kutu(x, y, 172, 44, arka, renk, 7)
        ic += yazi_tr(x + 86, y + 16, bas, renk, boy=10.0)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=19)
    return svg(360, 100, ic, 'Müzekker ve müennes kırtasiye ürünlerinde fiyat sorma kartları.', 15)


def tercih_soru_karti():
    ic = kutu(4, 4, 352, 42, TUR_A, TUR, 8)
    ic += yazi_tr(14, 21, 'Satıcı', TUR, 'start')
    ic += yazi_ar(215, 32, 'أَتُفَضِّلُ الْحَقِيبَةَ الْكَبِيرَةَ أَمِ الصَّغِيرَةَ؟', LAC, boy=19)
    ic += kutu(4, 52, 352, 42, MAVI_A, MAVI, 8)
    ic += yazi_tr(14, 69, 'Müşteri', MAVI, 'start')
    ic += yazi_ar(215, 80, '؟ (Küçük çantayı tercih ederim)', KIR, boy=18)
    return svg(360, 98, ic, 'Büyük çantayı mı yoksa küçük çantayı mı tercih edersin sorusu.', 15)


def sayili_kirtasiye_raflari():
    raflar = [
        (4, 4, '1. Raf (11)', 'أَحَدَ عَشَرَ دَفْتَرًا', MAVI, MAVI_A),
        (184, 4, '2. Raf (12)', 'اِثْنَتَا عَشْرَةَ مِمْحَاةً', YES, YES_A),
        (4, 52, '3. Raf (?)', 'أَرْبَعَ عَشْرَةَ مِسْطَرَةً', KIR, KIR_A),
        (184, 52, '4. Raf (15)', 'خَمْسَةَ عَشَرَ قَلَمًا', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, renk, arka in raflar:
        ic += kutu(x, y, 172, 44, arka, renk, 7)
        ic += yazi_tr(x + 86, y + 16, bas, renk, boy=10.0)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=19)
    return svg(360, 100, ic, '11-15 arası sayılarla etiketlenmiş dört kırtasiye rafı.', 15)


def baglac_karsilastirma_karti():
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 20, 'A Cümlesi (أَمِ)', MAVI)
    ic += yazi_ar(90, 50, 'أَتُرِيدُ قَلَمًا أَزْرَقَ أَمِ أَسْوَدَ؟', LAC, boy=18)
    ic += yazi_tr(90, 78, 'Mavi mi yoksa siyah mı?', LAC, kalin=False, boy=9.8)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(270, 20, 'B Cümlesi (ثُمَّ)', YES)
    ic += yazi_ar(270, 50, 'آخُذُ الدَّفْتَرَ ثُمَّ الْمِمْحَاةَ', LAC, boy=18)
    ic += yazi_tr(270, 78, 'Defteri, sonra silgiyi alırım.', LAC, kalin=False, boy=9.8)
    return svg(360, 94, ic, 'Em ve sümme bağlaçlarının kırtasiye cümlelerinde kullanımı.', 15)


def kirtasiye_diyalog_adimlari():
    adimlar = [
        (4, '1. Karşılama', 'أَيَّ خِدْمَةٍ؟', MAVI, MAVI_A),
        (93, '2. İhtiyaç', 'بِحَاجَةٍ إِلَى', YES, YES_A),
        (182, '3. Sunum', 'تَفَضَّلْ', TUR, TUR_A),
        (271, '4. Toplam', 'بِكَمِ الْمَجْمُوعُ؟', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, ar, renk, arka in adimlar:
        ic += kutu(x, 6, 85, 76, arka, renk, 8)
        ic += yazi_tr(x + 42, 24, bas, renk, boy=10.0)
        ic += yazi_ar(x + 42, 60, ar, LAC, boy=18)
    return svg(360, 88, ic, 'Kırtasiye alışveriş diyaloğunun dört temel adımı.', 14)


def kirtasiye_kasa_fisi():
    ic = kutu(4, 4, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(90, 20, 'Alınan Ürünler', YES)
    ic += yazi_ar(90, 48, 'دَفْتَرٌ : ١١ لِيرَةً', LAC, boy=19)
    ic += yazi_ar(90, 76, 'وَمِقَصٌّ : ٤ لِيرَاتٍ', LAC, boy=19)

    ic += kutu(184, 4, 172, 86, TUR_A, TUR, 8)
    ic += yazi_tr(270, 20, 'Genel Toplam (الْمَجْمُوعُ)', TUR)
    ic += yazi_ar(270, 52, 'بِخَمْسَ عَشْرَةَ لِيرَةً', LAC, boy=19)
    ic += yazi_tr(270, 78, 'Toplam: 15 TL', LAC, boy=10.2)
    return svg(360, 94, ic, 'Kırtasiye kasa fişi: Defter 11 lira, makas 4 lira, toplam 15 lira.', 15)


def ticaret_ahlaki_levhasi():
    ic = kutu(4, 4, 172, 84, SARI_A, TUR, 8)
    ic += yazi_tr(90, 20, '1. İlke · Ölçü ve Tartı', TUR)
    ic += yazi_ar(90, 50, 'اِنْتَبِهْ لِلْكَيْلِ وَالْمِيزَانِ', LAC, boy=18)
    ic += yazi_tr(90, 76, 'Ölçü ve tartıya dikkat et!', LAC, kalin=False, boy=9.8)

    ic += kutu(184, 4, 172, 84, MOR_A, MOR, 8)
    ic += yazi_tr(270, 20, '2. İlke · Dürüst Ticaret', MOR)
    ic += yazi_ar(270, 50, 'اللّٰهُ لَا يُحِبُّ الْمُطَفِّفِينَ', LAC, boy=18)
    ic += yazi_tr(270, 76, 'Hile yapanları sevmez.', LAC, kalin=False, boy=9.8)
    return svg(360, 92, ic, 'Ticaret ahlakı ilkelerini içeren iki kırtasiye levhası.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kirtasiye_istek_fisi()
    s[2]['gorsel'] = fiyat_zamir_kartlari()
    s[5]['gorsel'] = tercih_soru_karti()
    s[6]['gorsel'] = sayili_kirtasiye_raflari()
    s[7]['gorsel'] = baglac_karsilastirma_karti()
    s[8]['gorsel'] = kirtasiye_diyalog_adimlari()
    s[9]['gorsel'] = kirtasiye_kasa_fisi()
    s[11]['gorsel'] = ticaret_ahlaki_levhasi()
