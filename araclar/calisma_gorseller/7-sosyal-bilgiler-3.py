"""7. sınıf Sosyal Bilgiler 3. hafta (Özel Gereksinimli Bireyler İçin Fırsat Eşitliği: temel haklar, Anayasa m. 10, erişilebilirlik, başarı öyküleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kapsam_semasi_svg():
    """Özel gereksinimli birey kapsamı şeması (K kutusu soru işaretli)."""
    ic = kutu(76, 4, 208, 22, LAC, LAC, 11, 1)
    ic += yazi(180, 19, 'Özel Gereksinimli Birey Kapsamı', 11, '#fff')
    gruplar = [
        ('Görme ve işitme yetersizliği', MAVI, MAVI_A),
        ('Bedensel yetersizlik', MAVI, MAVI_A),
        ('Dil ve konuşma bozukluğu', TUR, TUR_A),
        ('Dikkat eksikliği ve hiperaktivite', TUR, TUR_A),
        ('Öğrenme güçlüğü', YES, YES_A),
        ('K: ?', MOR, MOR_A),
    ]
    for i, (ad, r, z) in enumerate(gruplar):
        x, y = 4 + (i % 2) * 180, 32 + (i // 2) * 23
        ic += kutu(x, y, 172, 19, z, r, 6, 1.3)
        ic += yazi(x + 86, y + 13.5, ad, 10.0, r if 'K:' in ad else LAC)
    return svg(360, 104, ic, 'Özel gereksinimli birey kapsamı şeması: görme ve işitme yetersizliği, bedensel yetersizlik, dil ve konuşma bozukluğu, dikkat eksikliği ve hiperaktivite, öğrenme güçlüğü ve K soru işareti.', 18)


def anayasa_ve_haklar_svg():
    """Anayasa Madde 10 ve yasal güvence bilgi panosu."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="8" fill="{MAVI}"/>'
    ic += yazi(90, 18, 'Anayasa · Madde 10', 11, '#fff')
    ic += yazi(90, 40, 'Dil, ırk, cinsiyet ve inanç', 10.5, LAC, ince=True)
    ic += yazi(90, 56, 'ayrımı gözetilmeksizin herkes', 10.5, LAC, ince=True)
    ic += yazi(90, 72, 'kanun önünde eşittir.', 10.5, MAVI)

    ic += kutu(184, 4, 172, 82, YES_A, YES, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="20" rx="8" fill="{YES}"/><rect x="184" y="16" width="172" height="8" fill="{YES}"/>'
    ic += yazi(270, 18, '4 Alanda Yasal Güvence', 11, '#fff')
    ic += yazi(196, 39, 'Eğitim (Kaynaştırma ve BEP)', 10.2, LAC, 'start', ince=True)
    ic += yazi(196, 55, 'Kamu binaları ve ulaşım', 10.5, LAC, 'start', ince=True)
    ic += yazi(196, 71, 'Sağlık ve sosyal yaşam', 10.5, LAC, 'start', ince=True)
    return svg(360, 90, ic, 'Anayasa Madde 10 kanun önünde eşitlik ve 4 alanda yasal güvence panosu.', 18)


def etki_tablosu_svg():
    """Fırsat eşitliğinin birey ve toplum kazanımları tablosu (III ve B yer değiştirmeli)."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="8" fill="{MAVI}"/>'
    ic += yazi(90, 18, 'Birey İçin Kazanımlar', 11, '#fff')
    sol = [
        'I. Yeteneklerini geliştirir.',
        'II. Öz güveni yükselir.',
        'III. Toplumsal barış hâkim olur.',
    ]
    for i, m in enumerate(sol):
        ic += yazi(12, 40 + i * 19, m, 10.2, KIR if i == 2 else LAC, 'start', ince=True)

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="20" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="8" fill="{TUR}"/>'
    ic += yazi(270, 18, 'Toplum İçin Kazanımlar', 11, '#fff')
    sag = [
        'A. Adalet ortamı güçlenir.',
        'B. Kendini değerli hisseder.',
        'C. Etkin katılımla huzur artar.',
    ]
    for i, m in enumerate(sag):
        ic += yazi(192, 40 + i * 19, m, 10.2, KIR if i == 1 else LAC, 'start', ince=True)
    return svg(360, 100, ic, 'Fırsat eşitliği kazanım tablosu: Birey sütununda I Yeteneklerini geliştirir, II Öz güveni yükselir, III Toplumsal barış hâkim olur; Toplum sütununda A Adalet ortamı güçlenir, B Kendini değerli hisseder, C Etkin katılımla huzur artar.', 19)


def dort_alan_kartlari_svg():
    """Dört yasal güvence uygulama kartı."""
    kartlar = [
        ('1. Kart', 'Bireyselleştirilmiş eğitim (BEP)', MAVI, MAVI_A),
        ('2. Kart', 'Bina girişinde rampa ve asansör', TUR, TUR_A),
        ('3. Kart', 'Hastanede kolay muayene erişimi', YES, YES_A),
        ('4. Kart', 'Sanat ve spor destek hizmetleri', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, alt, 10, LAC, 'start', ince=True)
    return svg(360, 88, ic, 'Dört uygulama kartı: 1. Kart Bireyselleştirilmiş eğitim, 2. Kart Bina girişinde rampa ve asansör, 3. Kart Hastanede kolay muayene erişimi, 4. Kart Sanat ve spor destek hizmetleri.', 18)


def basari_oykuleri_svg():
    """Batuhan Eruçar, Sare Aydın ve Yusuf Akgün başarı öyküsü kartları."""
    kartlar = [
        ('Batuhan Eruçar', ['Yüzmede 120’yi aşkın', 'madalya, kulüp kurdu'], MAVI, MAVI_A),
        ('Sare Aydın', ['Tıp fakültesi birincisi', 've psikiyatri uzmanı'], TUR, TUR_A),
        ('Yusuf Akgün', ['Ağzıyla resim sanatı', 've çoklu spor ödülü'], YES, YES_A),
    ]
    ic = ''
    for i, (ad, sat, r, z) in enumerate(kartlar):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 78, z, r, 8, 1.4)
        ic += f'<rect x="{x}" y="6" width="114" height="20" rx="8" fill="{r}"/><rect x="{x}" y="18" width="114" height="8" fill="{r}"/>'
        ic += yazi(x + 57, 20, ad, 10.2, '#fff')
        ic += yazi(x + 57, 44, sat[0], 9.4, LAC, ince=True)
        ic += yazi(x + 57, 62, sat[1], 9.4, LAC, ince=True)
    return svg(360, 90, ic, 'Üç başarı öyküsü kartı: Batuhan Eruçar yüzme madalyaları, Sare Aydın tıp fakültesi birinciliği, Yusuf Akgün ağzıyla resim ve sergiler.', 18)


def okul_duzenleme_panosu_svg():
    """Dört durum panosu (4. durum fırsat eşitliğine aykırı)."""
    durumlar = [
        ('1. Durum', 'Kaldırıma takip şeridi döşenmesi', MAVI, MAVI_A),
        ('2. Durum', 'Üstün yetenekli öğrenciye atölye', YES, YES_A),
        ('3. Durum', 'Laboratuvara kız-erkek eşit erişim', TUR, TUR_A),
        ('4. Durum', 'Öğrencinin geziye alınmaması', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, m, r, z) in enumerate(durumlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, m, 9.6, LAC, 'start', ince=True)
    return svg(360, 88, ic, 'Dört durum panosu: 1. durum takip şeridi, 2. durum destek atölyesi, 3. durum eşit laboratuvar erişimi, 4. durum öğrencinin geziye alınmaması.', 18)


def uc_portre_eslestirme_svg():
    """I, II ve III numaralı başarı rozetleri."""
    rozetler = [
        ('I. Rozet', ['Anzak Koyu Yüzme', 'Yarışı Birincisi'], MAVI, MAVI_A),
        ('II. Rozet', ['Tıp Fakültesi Birincisi', 'Psikiyatri Uzmanı'], TUR, TUR_A),
        ('III. Rozet', ['Ağzıyla Resim Sanatı', 've Çoklu Spor Ödülü'], YES, YES_A),
    ]
    ic = ''
    for i, (bas, sat, r, z) in enumerate(rozetler):
        x = 4 + i * 119
        ic += kutu(x, 6, 114, 74, z, r, 8, 1.4)
        ic += yazi(x + 57, 23, bas, 10.6, r)
        ic += yazi(x + 57, 44, sat[0], 9.5, LAC, ince=True)
        ic += yazi(x + 57, 60, sat[1], 9.5, LAC, ince=True)
    return svg(360, 86, ic, 'Üç başarı rozeti: I Anzak Koyu Yüzme Yarışı Birincisi, II Tıp Fakültesi Birincisi Psikiyatri Uzmanı, III Ağzıyla Resim Sanatı ve Çoklu Spor Ödülü.', 18)


def park_yeri_levhasi_svg():
    """Engelli araç park yeri ve kaldırım rampası uyarı kartı."""
    ic = kutu(4, 4, 352, 76, CAM_A, CAM, 8, 1.4)
    ic += kutu(14, 12, 92, 60, '#fff', MAVI, 7, 1.5)
    ic += yazi(60, 34, '[ P ]', 13, MAVI)
    ic += yazi(60, 56, 'Özel Park Yeri', 10.5, LAC)
    ic += kutu(116, 12, 228, 60, '#fff', CAM, 7, 1.2)
    ic += yazi(230, 30, 'Erişilebilirlik Alanı Uyarısı', 11, CAM)
    ic += yazi(126, 48, 'Park yeri ve rampa önü boş tutulmalıdır.', 10.5, LAC, 'start', ince=True)
    ic += yazi(126, 63, 'Eşit koşullarda ulaşım temel haktır.', 10.5, LAC, 'start', ince=True)
    return svg(360, 84, ic, 'Engelli araç park yeri levhası ve erişilebilirlik alanı uyarı kartı.', 18)


def okul_bahcesi_kroki_svg():
    """Okul bahçesi ve kütüphane girişi erişilebilirlik krokisi."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.3)
    ic += yazi(180, 19, 'OKUL ERİŞİLEBİLİRLİK KROKİSİ (Eksik Alanlar)', 11, LAC)
    ic += kutu(12, 28, 162, 50, KIR_A, KIR, 6, 1.3)
    ic += yazi(93, 45, '1. Kütüphane Girişi', 10.5, KIR)
    ic += yazi(93, 63, 'Yalnız 5 basamak merdiven var', 10, LAC, ince=True)
    ic += kutu(186, 28, 162, 50, TUR_A, TUR, 6, 1.3)
    ic += yazi(267, 45, '2. Bahçe Yürüyüş Yolu', 10.5, TUR)
    ic += yazi(267, 63, 'Düz beton (takip şeridi yok)', 10, LAC, ince=True)
    return svg(360, 90, ic, 'Okul erişilebilirlik krokisi: 1 Kütüphane girişinde yalnız 5 basamak merdiven var, 2 Bahçe yürüyüş yolunda takip şeridi yok.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kapsam_semasi_svg()
    s[2]['gorsel'] = anayasa_ve_haklar_svg()
    s[4]['gorsel'] = etki_tablosu_svg()
    s[5]['gorsel'] = dort_alan_kartlari_svg()
    s[6]['gorsel'] = basari_oykuleri_svg()
    s[8]['gorsel'] = okul_duzenleme_panosu_svg()
    s[9]['gorsel'] = uc_portre_eslestirme_svg()
    s[10]['gorsel'] = park_yeri_levhasi_svg()
    s[12]['gorsel'] = okul_bahcesi_kroki_svg()
