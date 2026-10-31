"""7. sınıf Sosyal Bilgiler 7. hafta (Küreselleşmenin İnsan ve Toplum Hayatına Etkisi: kültür, ekonomi, küresel sorunlar ve çözüm önerileri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def duz(x, y, satirlar, boy=10.5, renk=LAC, hiza='start', ara=13):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, no, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="8.5" fill="{renk}"/>' + yazi(x, y + 4, str(no), 10.5, '#fff')


def kuresellesme_boyutlari_svg():
    """Soru 1: Küreselleşmenin dört temel boyutu (3. kart Ekonomi ve E-Ticaret soru işaretli)."""
    ic = kutu(66, 4, 228, 22, LAC, LAC, 11, 1) + yazi(180, 19, 'Küreselleşmenin Dört Temel Boyutu', 11.5, '#fff')
    kartlar = [
        (1, 'Bilim ve İletişim', 'Buluş ve haberlere anında erişim', MAVI, MAVI_A),
        (2, 'İnsani Dayanışma', 'Afetlerde sınır ötesi ortak yardım', YES, YES_A),
        (3, 'Ekonomi ve E-Ticaret', '? (Örnek uygulama nedir?)', TUR, TUR_A),
        (4, 'Kültürler Arası Tanışma', 'Sanat ve turizmle önyargıları aşma', MOR, MOR_A),
    ]
    for i, (no, bas, alt, c, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 32 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, c, 7, 1.3) + rozet(x + 14, y + 14, no, c)
        ic += yazi(x + 28, y + 17, bas, 10.5, c, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 114, ic, 'Küreselleşmenin dört boyutu: 1 Bilim ve İletişim, 2 İnsani Dayanışma, 3 Ekonomi ve E-Ticaret soru işaretli, 4 Kültürler Arası Tanışma.', 16)


def etki_kartlari_svg():
    """Soru 2: Tablo sorusu için dört günlük yaşam durumu kartı."""
    kartlar = [
        ('1. Durum', 'Tıbbi buluş paylaşımı', MAVI, MAVI_A),
        ('2. Durum', 'Hazır gıda yayılması', KIR, KIR_A),
        ('3. Durum', 'Afette uluslararası yardım', YES, YES_A),
        ('4. Durum', 'İhtiyaç dışı alışveriş', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, m, c, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 64, z, c, 8, 1.4)
        ic += yazi(x + 41, 22, no, 10.5, c)
        parcalar = m.split(' ', 1)
        ic += yazi(x + 41, 41, parcalar[0], 10.5, LAC)
        ic += yazi(x + 41, 56, parcalar[1], 10.5, LAC, 'middle', True)
    return svg(360, 76, ic, 'Dört günlük yaşam durumu kartı: 1 tıbbi buluş paylaşımı, 2 hazır gıda yayılması, 3 afette uluslararası yardım, 4 ihtiyaç dışı alışveriş.', 16)


def populer_kultur_panosu_svg():
    """Soru 4: Popüler kültürün toplum hayatındaki üç yansıması panosu."""
    sutunlar = [
        ('1. Dil ve İletişim', ['Yabancı kelimelerin', 'günlük konuşmaya', 'kontrolsüz girmesi'], MAVI, MAVI_A),
        ('2. Beslenme ve Giyim', ['Her ülkede aynı hazır', 'yemek ve tek tip', 'markaların yayılması'], TUR, TUR_A),
        ('3. Tüketim Alışkanlığı', ['Reklamlarla sürekli', 'yeni eşya alma ve', 'geçici moda akımları'], MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sat, c, z) in enumerate(sutunlar):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 86, z, c, 8, 1.4)
        ic += f'<rect x="{x}" y="6" width="114" height="22" rx="8" fill="{c}"/><rect x="{x}" y="18" width="114" height="10" fill="{c}"/>'
        ic += yazi(x + 57, 21, bas, 10.5, '#fff')
        ic += duz(x + 57, 44, sat, 10.5, LAC, 'middle', 14)
    return svg(360, 98, ic, 'Popüler kültür panosu: 1 Dil ve iletişimde yabancı kelimeler, 2 Beslenme ve giyimde tek tip markalar, 3 Tüketim alışkanlığında geçici moda akımları.', 16)


def cinar_agaci_ilkesi_svg():
    """Soru 5: Kökleri millî değerlerde, dalları evrensel bilimde çınar ağacı şeması."""
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.3)
    ic += kutu(12, 12, 152, 70, YES_A, YES, 8, 1.4)
    ic += yazi(88, 28, 'Dallar: Evrensel Gelişim', 11, YES)
    ic += duz(88, 46, ['Bilim ve teknoloji takibi', 'Uluslararası iş birliği'], 10.5, LAC, 'middle', 15)
    ic += yazi(180, 50, '↔', 13, LAC)
    ic += kutu(196, 12, 152, 70, TUR_A, TUR, 8, 1.4)
    ic += yazi(272, 28, 'Kökler: Millî Kimlik', 11, TUR)
    ic += duz(272, 46, ['Türkçenin doğru kullanımı', 'Gelenek ve yerli üretim'], 10.5, LAC, 'middle', 15)
    return svg(360, 94, ic, 'Denge şeması: solda dallar evrensel gelişim bilim ve teknoloji takibi, sağda kökler millî kimlik Türkçenin doğru kullanımı ve yerli üretim.', 16)


def dort_sorun_karti_svg():
    """Soru 7: Dört sorun kartı (3 küresel sorun, 4. kart yerel mahalle parkı sorunu)."""
    kartlar = [
        ('1. Kart · İklim', 'Sera gazı ve küresel ısınma', KIR, KIR_A),
        ('2. Kart · Sağlık', 'Sınır aşan salgın hastalıklar', MOR, MOR_A),
        ('3. Kart · Kaynak', 'Kuraklık ve temiz su kıtlığı', TUR, TUR_A),
        ('4. Kart · Yerel', 'Mahalle parkı taş onarımı', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, c, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, c, 7, 1.3)
        ic += yazi(x + 86, y + 16, bas, 10.5, c)
        ic += yazi(x + 86, y + 31, alt, 10.5, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört sorun kartı: 1 sera gazı ve küresel ısınma, 2 sınır aşan salgın hastalıklar, 3 kuraklık ve su kıtlığı, 4 mahalle parkı taş onarımı.', 16)


def bilincli_tuketici_listesi_svg():
    """Soru 9: Bilinçli tüketici kontrol listesi."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{YES}"/><rect x="4" y="16" width="352" height="10" fill="{YES}"/>'
    ic += yazi(180, 19, 'BİLİNÇLİ TÜKETİCİ KONTROL LİSTESİ', 11, '#fff')
    maddeler = [
        '✓ Alışverişten önce ihtiyaç listesi hazırlamak ve israftan kaçınmak',
        '✓ Yerli ve millî üretim damgalı ürünleri öncelikle tercih etmek',
        '✓ Cam, kâğıt ve metal atıkları geri dönüşüm kutularına ayırmak',
    ]
    for i, m in enumerate(maddeler):
        y = 32 + i * 18
        ic += kutu(12, y, 336, 15, '#fff', YES, 4, 1)
        ic += yazi(20, y + 11.5, m, 10.5, LAC, 'start', True)
    return svg(360, 94, ic, 'Bilinçli tüketici kontrol listesi: ihtiyaç listesi hazırlamak, yerli ve millî ürünleri tercih etmek, atıkları geri dönüşüme ayırmak.', 16)


def dijital_iletisim_kartlari_svg():
    """Soru 10: Dijital araçların ölçülü kullanımı ile dijital bağımlılık karşılaştırması."""
    ic = kutu(6, 6, 170, 74, KIR_A, KIR, 8, 1.4)
    ic += yazi(91, 22, '1. Durum: Dijital Bağımlılık', 11, KIR)
    ic += duz(91, 40, ['Saatlerce kesintisiz ekran,', 'aile içi sohbetin azalması'], 10.5, LAC, 'middle', 15)

    ic += kutu(184, 6, 170, 74, YES_A, YES, 8, 1.4)
    ic += yazi(269, 22, '2. Durum: Bilinçli Kullanım', 11, YES)
    ic += duz(269, 40, ['Bilgi ve araştırma için ekran,', 'ortak aile saatinde sohbet'], 10.5, LAC, 'middle', 15)
    return svg(360, 86, ic, 'Dijital iletişim karşılaştırma kartları: 1 dijital bağımlılık, 2 bilinçli kullanım ve ortak aile sohbeti.', 16)


def bakir_atolyesi_vaka_svg():
    """Soru 11: Geleneksel bakır işlemeciliği atölyesinin e-ticaretle dünyaya açılması şeması."""
    ic = kutu(4, 4, 352, 78, KUM, GRI, 8, 1.3)
    ic += kutu(12, 14, 148, 58, TUR_A, TUR, 7, 1.3)
    ic += yazi(86, 32, 'Geleneksel El Sanatı', 11, TUR)
    ic += yazi(86, 50, 'Anadolu bakır işlemeciliği', 10.5, LAC, 'middle', True)
    ic += yazi(180, 46, '→', 13, MAVI)
    ic += kutu(200, 14, 148, 58, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(274, 32, 'Küresel E-Ticaret Ağı', 11, MAVI)
    ic += yazi(274, 50, 'Dünya ülkelerine ihracat', 10.5, LAC, 'middle', True)
    return svg(360, 86, ic, 'Vaka şeması: geleneksel Anadolu bakır işlemeciliği ok küresel e-ticaret ağı ile dünya ülkelerine ihracat.', 16)


def surdurulebilir_afis_svg():
    """Soru 14: Sürdürülebilir yaşam ve sıfır atık afiş taslağı."""
    ic = kutu(4, 4, 352, 76, CAM_A, CAM, 8, 1.4)
    ic += yazi(180, 22, 'EVİMİZ DÜNYA · SÜRDÜRÜLEBİLİR YAŞAM ADIMLARI', 11, CAM)
    adimlar = [('Su Tasarrufu', MAVI, MAVI_A), ('Enerji Verimliliği', TUR, TUR_A), ('Sıfır Atık ve Dönüşüm', YES, YES_A)]
    for i, (ad, c, z) in enumerate(adimlar):
        x = 12 + i * 114
        ic += kutu(x, 30, 108, 40, z, c, 6, 1.3)
        ic += yazi(x + 54, 54, ad, 10.5, c)
    return svg(360, 84, ic, 'Sürdürülebilir yaşam afişi: Su tasarrufu, Enerji verimliliği, Sıfır atık ve dönüşüm.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kuresellesme_boyutlari_svg()
    s[1]['gorsel'] = etki_kartlari_svg()
    s[3]['gorsel'] = populer_kultur_panosu_svg()
    s[4]['gorsel'] = cinar_agaci_ilkesi_svg()
    s[6]['gorsel'] = dort_sorun_karti_svg()
    s[8]['gorsel'] = bilincli_tuketici_listesi_svg()
    s[9]['gorsel'] = dijital_iletisim_kartlari_svg()
    s[10]['gorsel'] = bakir_atolyesi_vaka_svg()
    s[13]['gorsel'] = surdurulebilir_afis_svg()
