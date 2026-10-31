"""6. sınıf Türkçe 7. hafta (Cepheye Koşan At: Hikâye Unsurları, Anlatıcı Bakış Açıları, Deyimler ile İsim ve Sıfat Tamlamaları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def deyim_kartlari():
    kartlar = [
        ('1. Kart: Canını dişine takmak', 'Her türlü tehlikeyi göze alarak', 'var gücüyle çalışmak, çabalamak.', MAVI, MAVI_A),
        ('2. Kart: Gözden kaybolmak', 'Uzaklaşarak artık görünmez', 'duruma gelmek.', YES, YES_A),
        ('3. Kart: Kulak kabartmak', 'Öfkelenerek çevresindekilere', 'yüksek sesle bağırmak.', KIR, '#fdeaea'),
        ('4. Kart: Yüreği ağzına gelmek', 'Ansızın çok büyük bir korku', 'veya heyecan yaşamak.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 10.6, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.0, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 46, s2, 10.0, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört deyim kartı: 1. Canını dişine takmak, 2. Gözden kaybolmak, 3. Kulak kabartmak (hatalı anlam), 4. Yüreği ağzına gelmek.', 23)


def tamlama_panosu():
    tamlamalar = [
        ('1. Örnek', 'cephe yolu', '(Sadece 2. ek almış)', MAVI, MAVI_A),
        ('2. Örnek', 'atın yelesi', '(İkisi de ek almış)', YES, YES_A),
        ('3. Örnek', 'yorgun süvari', '(Sıfat + İsim)', TUR, TUR_A),
        ('4. Örnek', 'köy yolunun çeşmesi', '(3 isim bağlanmış)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ornek, ipucu, renk, arka) in enumerate(tamlamalar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 10.8, renk)
        ic += f'<line x1="{x + 14}" y1="32" x2="{x + 122}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, ornek, 10.2, LAC)
        ic += yazi(x + 68, 72, ipucu, 10.0, LAC, ince=True)
    return svg(600, 100, ic, 'Dört tamlama örneği: cephe yolu, atın yelesi, yorgun süvari ve köy yolunun çeşmesi.', 22)


def hikaye_parca_karti():
    ic = f'<rect x="8" y="6" width="584" height="94" rx="10" fill="{KUM}" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += f'<rect x="8" y="6" width="584" height="24" rx="10" fill="{KAHVE}"/><rect x="8" y="20" width="584" height="10" fill="{KAHVE}"/>'
    ic += yazi(300, 22, 'HİKÂYE PARÇASI · Cepheye Koşan At (Anlatıcı ve Unsurlar)', 11.1, '#fff')
    ic += yazi(22, 48, '“Bir kış sabahı şafak sökmeden önce doru atım Rüzgâr’ın dizginlerini sıkıca tuttum.', 10.4, LAC, 'start', ince=True)
    ic += yazi(22, 66, 'Ben genç seyis Kerem olarak İnebolu’dan Kastamonu’ya uzanan karlı dağ yolunda ilerledim', 10.4, LAC, 'start', ince=True)
    ic += yazi(22, 84, 've cephane yüklü arabayı azgın tipiye rağmen Rüzgâr’ın gayretiyle tepeye ulaştırdım.”', 10.4, LAC, 'start', ince=True)
    return svg(600, 106, ic, 'Genç seyis Kerem ve doru atı Rüzgâr’ın kış sabahı İnebolu-Kastamonu karlı dağ yolunda cephane taşımasını anlatan hikâye kartı.', 22)


def zincirleme_tuzak_karti():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. İfade: “atın beyaz yelesi”', 11.1, TUR)
    ic += yazi(149, 48, 'at (isim) + beyaz (sıfat) + yele (isim)', 10.3, LAC, ince=True)
    ic += yazi(149, 68, 'Ortadaki “beyaz” sözcüğü isim değil,', 10.2, LAC, ince=True)
    ic += yazi(149, 83, 'niteleme sıfatıdır (2 isim + 1 sıfat).', 10.2, TUR)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. İfade: “atın yelesinin rengi”', 11.1, YESIL_K)
    ic += yazi(451, 48, 'at (isim) + yele (isim) + renk (isim)', 10.3, LAC, ince=True)
    ic += yazi(451, 68, 'Üç sözcüğün tamamı isimdir ve ilgi-iyelik', 10.2, LAC, ince=True)
    ic += yazi(451, 83, 'ekleriyle birbirine bağlanmıştır (3 isim).', 10.2, YESIL_K)
    return svg(600, 102, ic, 'Atın beyaz yelesi ile atın yelesinin rengi tamlamalarının sözcük türleri karşılaştırma kartı.', 22)


def olay_orgusu_zinciri():
    adimlar = [
        ('Serim Başlangıcı', 'Mühimmatın yüklenmesi', MAVI, MAVI_A),
        ('Düğüm (Engel)', 'Çamura saplanması', TUR, TUR_A),
        ('Doruk Noktası', 'Atın arabayı çekmesi', MOR, MOR_A),
        ('Çözüm Sonucu', 'Cephanenin teslimi', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 34, ust, 10.8, renk)
        ic += yazi(x + 68, 60, alt, 10.0, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 137}" y1="48" x2="{x + 147}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Cepheye Koşan At öyküsünün serim, düğüm ve çözüm olay halkaları.', 22)


def bakis_acisi_metin_kartlari():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(149, 25, '1. Metin Kartı (Hâkim Bakış Açısı)', 11.0, MOR)
    ic += yazi(149, 46, '“Süvari atının yelesini okşadı. İçinden', 10.2, LAC, ince=True)
    ic += yazi(149, 63, 'geçen yetişememe korkusunu kimseye belli', 10.2, LAC, ince=True)
    ic += yazi(149, 80, 'etmiyor, kalbi vatan umuduyla çarpıyordu.”', 10.2, MOR)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 25, '2. Metin Kartı (Gözlemci Bakış Açısı)', 11.0, MAVI)
    ic += yazi(451, 46, '“Süvari atının yelesini okşadı. Çamurlu', 10.2, LAC, ince=True)
    ic += yazi(451, 63, 'patikadan yukarı doğru sessizce ilerledi', 10.2, LAC, ince=True)
    ic += yazi(451, 80, 've tepenin ardında gözden kayboldu.”', 10.2, MAVI)
    return svg(600, 104, ic, 'Aynı olayın 1. metinde hâkim bakış açısıyla, 2. metinde gözlemci bakış açısıyla anlatımı.', 22)


def deyim_atasozu_sema():
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, 'Deyimler ve Atasözleri Karşılaştırma Şeması', 11.3, LAC)
    kutular = [
        ('Deyimlerin Özelliği', 'Bir durumu etkileyici betimler;', 'öğüt veya kesin hüküm vermez.', MAVI, MAVI_A),
        ('Ortak Özellikleri', 'Kalıplaşmış ve çoğunlukla mecaz', 'anlamlı söz varlığı unsurlarıdır.', TUR, TUR_A),
        ('Atasözlerinin Özelliği', 'Deneyimlere dayanır; topluma', 'doğrudan ders ve öğüt verir.', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, bas, 10.7, renk)
        ic += yazi(x + 90, 65, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 81, s2, 10.1, LAC)
    return svg(600, 108, ic, 'Deyimler ve atasözlerinin ortak ve farklı özelliklerini gösteren şema.', 22)


def cumle_tamlama_karti():
    ic = f'<rect x="8" y="8" width="584" height="84" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 27, 'Cümlede Tamlama Çözümleme Kartı', 11.3, MAVI)
    ic += yazi(300, 50, '“Cesur süvari, cephe yolunun tozunu yutarak karargâha ulaştı.”', 11.0, LAC)
    ic += yazi(300, 72, 'İpucu: “Nasıl süvari?” sorusuna ve üç ismin birbirine bağlandığı öbeğe dikkat ediniz.', 10.2, MAVI, ince=True)
    return svg(600, 100, ic, 'Cesur süvari, cephe yolunun tozunu yutarak karargâha ulaştı cümlesi çözümleme kartı.', 22)


def cepheye_kosan_at_tema_karti():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, '“CEPHEYE KOŞAN AT” METNİ · Tema ve Millî Değerler Özeti', 11.2, KAHVE)
    kutular = [
        ('Ana Tema', 'Millî Mücadele ruhu,', 'bağımsızlık ve vatan sevgisi', KIR, '#fdeaea'),
        ('Fedakârlık Ruhu', 'Anadolu halkının ve cepheye', 'koşan atların üstün gayreti', MAVI, MAVI_A),
        ('Kazandırdığı Değer', 'Vatanseverlik, azim, birlik', 've geçmişe vefa duygusu', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 66, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 80, s2, 10.1, LAC)
    return svg(600, 104, ic, 'Cepheye Koşan At metninin ana teması, fedakârlık ruhu ve kazandırdığı millî değerler.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = deyim_kartlari()
    s[4]['gorsel'] = tamlama_panosu()
    s[5]['gorsel'] = hikaye_parca_karti()
    s[6]['gorsel'] = zincirleme_tuzak_karti()
    s[7]['gorsel'] = olay_orgusu_zinciri()
    s[8]['gorsel'] = bakis_acisi_metin_kartlari()
    s[9]['gorsel'] = deyim_atasozu_sema()
    s[10]['gorsel'] = cumle_tamlama_karti()
    s[12]['gorsel'] = cepheye_kosan_at_tema_karti()
