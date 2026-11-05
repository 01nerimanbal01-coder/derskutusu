"""8. sınıf Arapça 12. hafta (Doğruluk ve Güvenilirlik: الصِّدْقُ وَالْأَمَانَةُ, Bağlaçlar ve Nezaket İfadeleri) görselleri.
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


def durust_tuccar_karti():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 24, 'Ticaret ve Değerler Kartı (الصِّدْقُ وَالْأَمَانَةُ)', YES, kalin=True)
    ic += yazi_ar(180, 56, 'أَحْمَدُ تَاجِرٌ صَادِقٌ وَأَمِينٌ، لِذَلِكَ يُحِبُّهُ النَّاسُ', LAC)
    ic += yazi(180, 90, 'تَاجِرٌ (tüccar) · صَادِقٌ (dürüst) · أَمِينٌ (güvenilir) · لِذَلِكَ (bu yüzden)', MAVI, kalin=True)
    return svg(ic, 'Dürüst ve güvenilir tüccar Ahmet hakkında Arapça cümle kartı.')


def dort_kavram_tablosu():
    kartlar = [
        (6, 6, '1. الصَّادِقُ وَالْأَمِينُ', 'Ahlaki Sıfatlar', YES, YES_A),
        (184, 6, '2. لِأَنَّ / لِذَلِكَ', 'Sebep-Sonuç Bağlaçları', MAVI, MAVI_A),
        (6, 60, '3. مِنْ فَضْلِكَ / لَوْ سَمَحْتَ', 'Nezaket İfadeleri', TUR, TUR_A),
        (184, 60, '4. حِفْظُ الْأَمَانَةِ', 'Emanet Bilinci', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 22, b1, r)
        ic += yazi(x + 85, y + 41, b2, LAC, kalin=True)
    return svg(ic, 'Doğruluk, bağlaçlar ve nezaket ifadeleri kavram kartları.')


def sebep_sonuc_diyalogu():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, '1. Konuşmacı Sorusu', MAVI, kalin=True)
    ic += yazi_ar(92, 54, 'لِمَاذَا يَثِقُ النَّاسُ بِخَالِدٍ؟', LAC)
    ic += yazi(92, 86, '(İnsanlar Halid’e niçin güvenir?)', MAVI)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 24, '2. Konuşmacı Yanıtı', YES, kalin=True)
    ic += yazi_ar(269, 54, 'يَثِقُ النَّاسُ بِهِ [ ... ؟ ... ]', LAC)
    ic += yazi(269, 86, 'Sebep Bağlacı: لِأَنَّهُ ...', YES, kalin=True)
    return svg(ic, 'Halid’e duyulan güvenin sebebini soran Arapça diyalog panosu.')


def dort_ahlaki_ilke():
    kartlar = [
        (6, 6, '1. قَوْلُ الصِّدْقِ دَائِمًا', 'Daima Doğru Söz (+)', YES, YES_A),
        (184, 6, '2. أَدَاءُ الْأَمَانَةِ', 'Emaneti Teslim (+)', MAVI, MAVI_A),
        (6, 60, '3. خِيَانَةُ الْأَمَانَةِ وَالْكَذِبُ', 'Hıyanet ve Yalan (-)', KIR, KIR_A),
        (184, 60, '4. مُسَاعَدَةُ الْأَصْدِقَاءِ', 'Yardımlaşma (+)', TUR, TUR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 22, b1, r)
        ic += yazi(x + 85, y + 41, b2, LAC, kalin=True)
    return svg(ic, 'Dört ahlaki davranış ilkesinin karşılaştırılması.')


def hikmet_levhasi_karti():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Hikmet Levhası (حِكْمَةُ الْيَوْمِ)', CAM, kalin=True)
    ic += yazi_ar(180, 58, 'اَلْمُؤْمِنُ لَا يَكْذِبُ وَلَا يَخُونُ الْأَمَانَةَ', LAC)
    ic += yazi(180, 90, 'لَا يَكْذِبُ (yalan söylemez) · لَا يَخُونُ (hıyanet etmez)', MAVI, kalin=True)
    return svg(ic, 'Müminin yalan söylemeyeceğini ve emanete hıyanet etmeyeceğini bildiren levha.')


def kayip_cuzdan_adimlari():
    adimlar = [
        (6, '1. Bulma', 'وَجَدْتُ الْمِحْفَظَةَ', MAVI, MAVI_A),
        (94, '2. Teslim', 'نُسَلِّمُهَا لِصَاحِبِهَا', TUR, TUR_A),
        (182, '3. Teşekkür', 'أَنْتَ صَادِقٌ وَأَمِينٌ', YES, YES_A),
        (270, '4. Görev', 'حِفْظُ الْأَمَانَةِ وَاجِبٌ', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, ar, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 32, b1, r, kalin=True)
        ic += yazi_ar(x + 42, 70, ar, LAC)
    return svg(ic, 'Okul bahçesinde bulunan cüzdanın sahibine teslim edilmesi adımları.')


def baglac_kontrol_tablosu():
    kartlar = [
        (6, 6, '1. نَجَحَ لِأَنَّهُ اجْتَهَدَ', 'لِأَنَّ (Çünkü — Doğru)', YES, YES_A),
        (184, 6, '2. مُمْطِرٌ لِذَلِكَ أَخَذْتُ', 'لِذَلِكَ (Bu yüzden — Doğru)', MAVI, MAVI_A),
        (6, 60, '3. فَقِيرٌ لَكِنَّهُ كَرِيمٌ', 'لَكِنَّ (Fakat — Doğru)', TUR, TUR_A),
        (184, 60, '4. الصِّدْقَ لِأَنَّ الْكَذِبَ جَمِيلٌ', 'Anlamca Çelişkili (؟)', KIR, KIR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi_ar(x + 85, y + 22, b1, r)
        ic += yazi(x + 85, y + 41, b2, LAC, kalin=True)
    return svg(ic, 'Sebep-sonuç bağlaçlarının cümle içi uyum tablosu.')


def degerler_etki_karti():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Bireysel Kazanç', YES, kalin=True)
    ic += yazi_ar(92, 56, 'الصِّدْقُ يَهْدِي إِلَى الْبِرِّ', LAC)
    ic += yazi(92, 86, 'İyiliğe ve huzura ulaştırır', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, 'Toplumsal Kazanç', MAVI, kalin=True)
    ic += yazi_ar(269, 56, 'يَثِقُ النَّاسُ وَيُحِبُّونَهُ', LAC)
    ic += yazi(269, 86, 'Güven ve sevgiyi artırır', MAVI, kalin=True)
    return svg(ic, 'Doğruluk ve güvenilirliğin bireysel ve toplumsal faydaları kartı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = durust_tuccar_karti()
    s[2]['gorsel'] = dort_kavram_tablosu()
    s[5]['gorsel'] = sebep_sonuc_diyalogu()
    s[6]['gorsel'] = dort_ahlaki_ilke()
    s[7]['gorsel'] = hikmet_levhasi_karti()
    s[8]['gorsel'] = kayip_cuzdan_adimlari()
    s[9]['gorsel'] = baglac_kontrol_tablosu()
    s[11]['gorsel'] = degerler_etki_karti()
