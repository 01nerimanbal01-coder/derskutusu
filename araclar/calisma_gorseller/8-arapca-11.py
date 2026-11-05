"""8. sınıf Arapça 11. hafta (2. Ünite: El Sanatları ve Ünite Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); eğik kesir ve beyaz bant yok (K155/K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#15803d', '#d63a3a', '#7c3aed', '#0e7490'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A, KUM = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#e0f2fe', '#fffbeb'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle', boy=18):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" font-weight="700" fill="{renk}">{metin}</text>'


def atolye_tabelalari():
    ic = kutu(4, 4, 412, 28, MOR_A, MOR, 7)
    ic += yazi(115, 22, 'Kültür Merkezi Atölye Tabelaları', MOR)
    ic += yazi_ar(318, 23, 'الْفُنُونُ الْيَدَوِيَّةُ', LAC, boy=17)
    ic += kutu(4, 38, 200, 64, TUR_A, TUR, 8)
    ic += yazi(104, 57, '1. Atölye Tabelası', TUR)
    ic += yazi_ar(104, 88, 'وَرْشَةُ النَّقْشِ عَلَى الْخَشَبِ', LAC)
    ic += kutu(216, 38, 200, 64, CAM_A, CAM, 8)
    ic += yazi(316, 57, '2. Atölye Tabelası', CAM)
    ic += yazi_ar(316, 88, 'دَوْرَةُ فَنِّ الْخَزَفِ', LAC)
    return svg(420, 106, ic, '1. ahşap oymacılığı atölyesi ve 2. çini sanatı kursu tabelaları.', 21)


def malzeme_kartlari():
    kartlar = [
        (4, 4, '1. Malzeme Kartı', 'قَلَمُ الْقَصَبِ وَالْحِبْرُ', MAVI, MAVI_A),
        (214, 4, '2. Malzeme Kartı', 'الْفُرْشَاةُ وَحَوْضُ الْمَاءِ', CAM, CAM_A),
        (4, 58, '3. Malzeme Kartı', 'الزَّخْرَفَةُ بِاللَّوْنِ الذَّهَبِيِّ', TUR, TUR_A),
        (214, 58, '4. Malzeme Kartı', 'تَلْوِينُ الْأَطْبَاقِ الطِّينِيَّةِ', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 17, bas, r)
        ic += yazi_ar(x + 101, y + 40, ar, LAC, boy=16)
    return svg(420, 110, ic, 'Dört geleneksel sanat dalına ait Arapça malzeme kartları.', 22)


def sergi_tercih_diyalogu():
    ic = kutu(4, 4, 412, 46, MAVI_A, MAVI, 8)
    ic += yazi(72, 22, 'Selim (Soru):', MAVI, 'start')
    ic += yazi_ar(402, 40, 'أَيَّ فَنٍّ يَدَوِيٍّ تُفَضِّلُ يَا عُمَرُ؟', LAC, 'end', 17)
    ic += kutu(4, 56, 412, 48, YES_A, YES, 8)
    ic += yazi(72, 74, 'Ömer (Yanıt):', YES, 'start')
    ic += yazi_ar(402, 94, 'أُفَضِّلُ فَنَّ الْأَبْرُو لِأَنَّ الرَّسْمَ عَلَى الْمَاءِ مُمْتِعٌ', LAC, 'end', 16)
    return svg(420, 108, ic, 'Selim ve Ömer arasında geçen el sanatı tercihi diyaloğu.', 21)


def dort_hat_levhasi():
    kartlar = [
        (4, 4, 'I. Levha', 'اَلْعَمَلُ خَيْرٌ مِنَ التَّسَوُّلِ', MOR, MOR_A),
        (214, 4, 'II. Levha', 'مَا أَجْمَلَ هَذِهِ اللَّوْحَةَ الْفَنِّيَّةَ', MAVI, MAVI_A),
        (4, 58, 'III. Levha', 'يُقَامُ الْمَعْرِضُ فِي الْمَرْكَزِ الثَّقَافِيِّ', TUR, TUR_A),
        (214, 58, 'IV. Levha', 'تَسْقُطُ أَوْرَاقُ الْأَشْجَارِ فِي الْخَرِيفِ', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 17, bas, r)
        ic += yazi_ar(x + 101, y + 40, ar, LAC, boy=15)
    return svg(420, 110, ic, 'Atölye duvarındaki dört Arapça hat levhası.', 22)


def sergi_gezi_karti():
    ic = kutu(4, 4, 412, 98, KUM, TUR, 8)
    ic += yazi(210, 22, 'El Sanatları Sergisi Ziyaret Duyurusu', TUR)
    ic += f'<line x1="20" y1="30" x2="400" y2="30" stroke="{TUR}" stroke-width="1.0"/>'
    ic += yazi_ar(210, 58, 'نَزُورُ مَعْرِضَ الْفُنُونِ الْيَدَوِيَّةِ مَعَ مُعَلِّمِنَا يَوْمَ السَّبْتِ', LAC, boy=17)
    ic += yazi(210, 88, 'Sorulan Unsurlar: إِلَى أَيْنَ؟ (Yer) · مَعَ مَنْ؟ (Kişi) · مَتَى؟ (Zaman)', MOR, ince=True)
    return svg(420, 106, ic, 'Cumartesi günü öğretmenle el sanatları sergisi ziyaret kartı.', 21)


def ebru_uygulama_seridi():
    adimlar = [
        (4, '1. أَوَّلًا', 'خُذِ الْفُرْشَاةَ', MAVI, MAVI_A),
        (108, '2. ثُمَّ', 'اُرْسُمْ عَلَى الْمَاءِ', CAM, CAM_A),
        (212, '3. بَعْدَ ذَلِكَ', 'ضَعِ الْوَرَقَةَ', TUR, TUR_A),
        (316, '4. أَخِيرًا', 'اِرْفَعِ اللَّوْحَةَ', YES, YES_A),
    ]
    ic = ''
    for x, bas, ar, r, z in adimlar:
        ic += kutu(x, 6, 100, 92, z, r, 7)
        ic += yazi(x + 50, 28, bas, r)
        ic += f'<line x1="{x+10}" y1="38" x2="{x+90}" y2="38" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi_ar(x + 50, 72, ar, LAC, boy=15)
    return svg(420, 104, ic, 'Ebru yapımında dört aşamalı Arapça emir yönergeleri.', 21)


def sanat_merkezi_panosu():
    ic = kutu(4, 4, 412, 100, MOR_A, MOR, 8)
    ic += yazi(132, 23, 'Haftalık Sergi Panosu', MOR)
    ic += yazi_ar(315, 24, 'الْمَرْكَزُ الثَّقَافِيُّ', LAC, boy=16)
    ic += kutu(12, 34, 192, 62, KUM, TUR, 6)
    ic += yazi(108, 52, 'يَوْمُ السَّبْتِ — ١٠:٠٠ صَبَاحًا', TUR)
    ic += yazi_ar(108, 82, 'دَوْرَةُ الْخَطِّ الْعَرَبِيِّ', LAC, boy=16)
    ic += kutu(216, 34, 192, 62, YES_A, YES, 6)
    ic += yazi(312, 52, 'يَوْمُ الْأَحَدِ — صُنْعُ الْيَدِ', YES)
    ic += yazi_ar(312, 82, 'وَرْشَةُ فَنِّ الْأَبْرُو', LAC, boy=16)
    return svg(420, 108, ic, 'Kültür merkezi cumartesi hat kursu ve pazar el yapımı ebru atölyesi panosu.', 22)


def sifat_uyumu_karti():
    ic = kutu(4, 4, 200, 96, MAVI_A, MAVI, 8)
    ic += yazi(104, 23, 'İncelenen İsim Cümlesi', MAVI)
    ic += yazi_ar(104, 60, 'اَلْفُنُونُ الْيَدَوِيَّةُ جَمِيلَةٌ', LAC, boy=18)
    ic += yazi(104, 88, 'المبتدأ + الصفة + الخبر', MAVI, ince=True)
    ic += kutu(216, 4, 200, 96, YES_A, YES, 8)
    ic += yazi(316, 23, 'Dil Bilgisi İpucu', YES)
    ic += yazi(316, 54, 'اَلْفُنُونُ → Akılsız Çoğul', LAC)
    ic += yazi(316, 82, 'Sıfat ve haber sonu: ـة', YES, ince=True)
    return svg(420, 104, ic, 'Akılsız çoğul isim cümlesinde müennes sıfat ve haber uyumu kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = atolye_tabelalari()
    s[2]['gorsel'] = malzeme_kartlari()
    s[5]['gorsel'] = sergi_tercih_diyalogu()
    s[6]['gorsel'] = dort_hat_levhasi()
    s[7]['gorsel'] = sergi_gezi_karti()
    s[8]['gorsel'] = ebru_uygulama_seridi()
    s[9]['gorsel'] = sanat_merkezi_panosu()
    s[11]['gorsel'] = sifat_uyumu_karti()
