"""7. sınıf Sosyal Bilgiler 12. hafta (Osmanlı Devleti’ni Cihan Devleti Yapan Politikalar ve Deniz Hâkimiyeti) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def bosna_ahidnamesi_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 26, 'Fatih Sultan Mehmed’in Bosna Ahidnamesi (1463)', TUR, kalin=True)
    ic += yazi(180, 52, '«Bosna rahiplerine buyurdum ki; kimse onlara ve kiliselerine', LAC)
    ic += yazi(180, 74, 'engel olmayıp incitmeye, canları ve malları güvencem altındadır.»', LAC, kalin=True)
    ic += yazi(180, 96, 'Temel İlkeler: Gönül Kazanma (Hoşgörü) + İnanç Özgürlüğü', MAVI, kalin=True)
    return svg(ic, 'Fatih Sultan Mehmed’in Bosna Ahidnamesi bilgi kartı.')


def deniz_fetihleri_panosu():
    kartlar = [
        (6, 6, '1. Kırım’ın Fethi (1475)', 'Karadeniz · İpek Yolu', MAVI, MAVI_A),
        (184, 6, '2. Preveze Zaferi (1538)', 'Barbaros · Akdeniz Üstünlüğü', CAM, CAM_A),
        (6, 60, '3. Mısır Seferi (1517)', 'Baharat Yolu · Kızıldeniz', TUR, TUR_A),
        (184, 60, '4. Kıbrıs’ın Fethi (1571)', 'Doğu Akdeniz Güvenliği', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Osmanlı deniz fetihleri ve ticaret yolları panosu.')


def iskan_politikasi_semasi():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'İskânın İlkeleri', YES, kalin=True)
    ic += yazi(92, 52, '• Konargöçer Türkmenler seçilir', LAC)
    ic += yazi(92, 74, '• Göç edenlere tohum/vergi desteği', LAC)
    ic += yazi(92, 95, '• 5 yıl geri dönmeme kuralı', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, 'İskânın Sonuçları', MAVI, kalin=True)
    ic += yazi(269, 52, '• Balkanlar Türkleşti ve şenlendi', LAC)
    ic += yazi(269, 74, '• Fetihler kalıcı hâle geldi', LAC)
    ic += yazi(269, 95, '• Yerli halka baskı yapılmadı!', KIR, kalin=True)
    return svg(ic, 'Osmanlı iskân politikasının ilkeleri ve sonuçları şeması.')


def yavuz_seferleri_karti():
    ic = kutu(6, 6, 172, 103, MOR_A, MOR)
    ic += yazi(92, 26, 'Doğu ve Anadolu Siyaseti', MOR, kalin=True)
    ic += yazi(92, 54, '• Çaldıran (1514): Doğu güvenliği', LAC)
    ic += yazi(92, 82, '• Turnadağ (1515): Siyasi birlik', MOR, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Mısır Seferi (1516-1517)', TUR, kalin=True)
    ic += yazi(269, 52, '• Mercidabık ve Ridaniye', LAC)
    ic += yazi(269, 74, '• Halifelik Osmanlıya geçti', LAC)
    ic += yazi(269, 95, '• Baharat Yolu denetim altına alındı', YES, kalin=True)
    return svg(ic, 'Yavuz Sultan Selim dönemi doğu ve Mısır seferleri kartı.')


def anadolu_beylikleri_tablosu():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 24, 'Anadolu Türk Siyasi Birliğini Sağlama Yöntemleri', CAM, kalin=True)
    ic += yazi(180, 50, '• Karesioğulları: İlk katılan denizci beylik (Orhan Bey)', LAC)
    ic += yazi(180, 74, '• Germiyanoğulları: Çeyiz (Evlilik) yoluyla (Kütahya ve çevresi)', MAVI, kalin=True)
    ic += yazi(180, 96, '• Hamitoğulları: Satın alma (Altın/Para) yoluyla (Isparta ve çevresi)', YES, kalin=True)
    return svg(ic, 'Anadolu beyliklerinin Osmanlıya katılma yöntemleri kartı.')


def denizcilik_kronoloji_kartlari():
    adimlar = [
        (6, '1345', 'Karesi Donanması', MAVI, MAVI_A),
        (94, '1475', 'Kırım’ın Fethi', YES, YES_A),
        (182, '1538', 'Preveze Zaferi', TUR, TUR_A),
        (270, '1571', 'Kıbrıs’ın Fethi', MOR, MOR_A),
    ]
    ic = ''
    for x, yil, olay, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, yil, r, kalin=True)
        ic += yazi(x + 42, 70, olay, LAC, kalin=True)
    return svg(ic, 'Osmanlı denizcilik tarihindeki dört önemli gelişmenin kronolojisi.')


def istanbul_antlasmasi_karti():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 26, '1533 İstanbul (İbrahim Paşa) Antlaşması Maddesi', MAVI, kalin=True)
    ic += yazi(180, 56, '«Avusturya Arşidükü (Kralı), protokol bakımından', LAC, kalin=True)
    ic += yazi(180, 80, 'Osmanlı Sadrazamına (Veziriazamına) eşit sayılacaktır.»', KIR, kalin=True)
    return svg(ic, '1533 İstanbul Antlaşması protokol maddesi bilgi kartı.')


def cihan_devleti_sutunlari():
    sutunlar = [
        (6, 'Gaza & Cihat', 'Adalet İdeali', TUR, TUR_A),
        (94, 'İstimalet', 'Hoşgörü & Güven', YES, YES_A),
        (182, 'İskân & İmar', 'Kalıcı Yerleşim', MAVI, MAVI_A),
        (270, 'Millet Sistemi', 'Din Özgürlüğü', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in sutunlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Osmanlı Devleti’ni cihan devleti yapan dört temel sütun.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bosna_ahidnamesi_karti()
    s[2]['gorsel'] = deniz_fetihleri_panosu()
    s[5]['gorsel'] = iskan_politikasi_semasi()
    s[6]['gorsel'] = yavuz_seferleri_karti()
    s[7]['gorsel'] = anadolu_beylikleri_tablosu()
    s[8]['gorsel'] = denizcilik_kronoloji_kartlari()
    s[9]['gorsel'] = istanbul_antlasmasi_karti()
    s[11]['gorsel'] = cihan_devleti_sutunlari()
