"""6. sınıf Sosyal Bilgiler 3. hafta (Kültürel Bağlarımızın ve Millî Değerlerimizin Toplumsal Birlikteliğe Etkisi) çalışma kâğıdı görselleri.
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


def kulturel_bag_sema():
    ic = f'<rect x="6" y="6" width="276" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(144, 24, 'Kültürel Bağlarımız (5 Temel Öge)', 11.4, MAVI)
    ic += yazi(22, 46, 'Dil, Din ve Sanat ögeleri', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 66, 'Eksik iki öge: K = ?', 10.8, MAVI, 'start')
    ic += yazi(22, 86, '→ Toplumda millî değerleri doğurur.', 10.4, LAC, 'start', ince=True)

    ic += f'<line x1="286" y1="54" x2="308" y2="54" stroke="{LAC}" stroke-width="2"/><path d="M303 49 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="312" y="6" width="282" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(453, 24, 'Millî Değerler ve Ortak Sonuç', 11.4, YESIL_K)
    ic += yazi(326, 46, 'Bağımsızlık, vatanseverlik, adalet, saygı', 10.4, LAC, 'start', ince=True)
    ic += yazi(326, 66, 'Kuşaktan kuşağa aktarılarak ulaşılan', 10.4, LAC, 'start', ince=True)
    ic += yazi(334, 86, 'ortak hedef: L = ?', 10.8, YESIL_K, 'start')
    return svg(600, 108, ic, 'Kültürel bağlar ve millî değerler kavram şeması: K eksik kültürel bağ ögeleri, L ulaşılan toplumsal hedef.', 22)


def dil_urunleri_panosu():
    kartlar = [
        ('1. Kart: Destanlar ve Ninniler', 'Destanlar kahramanlıkları anlatır,', 'ninniler çocukları uyutur.', MAVI, MAVI_A),
        ('2. Kart: Atasözleri ve Türküler', 'Atasözleri ders verir, türküler', 'sevgiyi ve duyguları paylaştırır.', YES, YES_A),
        ('3. Kart: Geleneksel Oyunlar', 'Çocuklara hiçbir şey öğretmeden', 'yalnızca vakit kaybettirir.', KIR, '#fdeaea'),
        ('4. Kart: Yazılı Eserlerimiz', 'Kutadgu Bilig ve Dede Korkut', 'vatan sevgisi ve sabrı aktarır.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 60
        ic += f'<rect x="{x}" y="{y}" width="286" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="54" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 17, bas, 10.6, renk, 'start')
        ic += yazi(x + 18, y + 33, s1, 10.0, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 48, s2, 10.0, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dil ürünleri panosu: 1. Destan ve ninni, 2. Atasözü ve türkü, 3. Oyunlar (hatalı açıklama), 4. Yazılı eserler.', 23)


def kultur_bag_kartlari():
    kartlar = [
        ('1. Kart', 'Köroğlu Destanı', 've yöresel türküler', MAVI, MAVI_A),
        ('2. Kart', 'İmarethane, aşevi', 've kervansaraylar', YES, YES_A),
        ('3. Kart', 'Halime Çavuş ve', 'Şerife Bacı mücadelesi', TUR, TUR_A),
        ('4. Kart', 'Çini, hat, minyatür', 've kilim dokumacılığı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="33" x2="{x + 122}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 53, s1, 10.4, LAC)
        ic += yazi(x + 68, 71, s2, 10.4, LAC, ince=True)
    return svg(600, 102, ic, 'Dört kültür kartı: 1. Köroğlu Destanı ve türküler, 2. İmarethane ve aşevi, 3. Halime Çavuş ve Şerife Bacı, 4. Çini, hat, minyatür ve kilim.', 22)


def mevlana_yunus_karti():
    ic = f'<rect x="8" y="8" width="282" height="90" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Mevlânâ Celâleddîn-i Rûmî', 11.4, MAVI)
    ic += yazi(149, 48, 'Cömertlikte akarsu, şefkatte güneş,', 10.4, LAC, ince=True)
    ic += yazi(149, 65, 'hoşgörüde deniz gibi olmayı öğütler.', 10.4, LAC, ince=True)
    ic += yazi(149, 83, '“Nasılsan öyle gel” çağrısını yapar.', 10.5, MAVI)

    ic += f'<rect x="310" y="8" width="282" height="90" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Yunus Emre', 11.4, YESIL_K)
    ic += yazi(451, 48, 'Yaratılanı Yaratan’dan ötürü hoş', 10.4, LAC, ince=True)
    ic += yazi(451, 65, 'görmeyi temel ilke sayar.', 10.4, LAC, ince=True)
    ic += yazi(451, 83, '“Sevelim sevilelim” anlayışını yayar.', 10.5, YESIL_K)
    return svg(600, 106, ic, 'Mevlânâ ve Yunus Emre öğütleri karşılaştırma kartı.', 22)


def zimem_zinciri():
    adimlar = [
        ('1. Adım', 'Ramazanda', 'bakkala gidiş', MAVI, MAVI_A),
        ('2. Adım', 'Zimem defterinin', 'açılması', TUR, TUR_A),
        ('3. Adım', 'Sayfaların satın', 'alınması', MOR, MOR_A),
        ('4. Adım', 'Borçların sessizce', 'silinmesi', YES, YES_A),
    ]
    ic = ''
    for i, (ust, s1, s2, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 28, ust, 11.2, renk)
        ic += yazi(x + 68, 52, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 68, 70, s2, 10.2, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 137}" y1="48" x2="{x + 147}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Osmanlı zimem defteri geleneğinin dört adımlı zinciri.', 22)


def deprem_dayanisma_karti():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, '6 Şubat 2023 Depremlerinde Toplumsal Dayanışma Örnekleri', 11.4, LAC)
    kutular = [
        ('Kurum ve Gönüllüler', 'AFAD, STK, belediyeler ve', '70 ilden on binlerce gönüllü', MAVI, MAVI_A),
        ('Gönülden Paylaşım', '84 yaşındaki Remzi Dede ve', '8 yaşındaki Muhammet’in bağışı', TUR, TUR_A),
        ('Evim Yuvan Olsun', '18 Şubat–15 Mart 2023 arası', '15 binden fazla konut kaydı', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.1, LAC, ince=True)
    return svg(600, 110, ic, '6 Şubat 2023 depremlerinde kurumlar, gönüllüler, bireysel bağışlar ve Evim Yuvan Olsun kampanyası.', 22)


def sanat_motif_karti():
    ic = f'<rect x="8" y="8" width="282" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Samsun Kavak Kilim Motifleri', 11.3, TUR)
    # Geometrik yıldız/koçboynuzu kilim motifi (insan figürü yok)
    ic += f'<polygon points="42,42 54,58 42,74 30,58" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.4"/>'
    ic += f'<polygon points="42,48 49,58 42,68 35,58" fill="{KIR}"/>'
    ic += yazi(72, 48, 'İnsan motifi → Çalışkanlık', 10.3, LAC, 'start', ince=True)
    ic += yazi(72, 65, 'Kuş motifi → Sevgi duygusu', 10.3, LAC, 'start', ince=True)
    ic += yazi(72, 82, 'Yıldız motifi → Üretkenlik', 10.3, LAC, 'start', ince=True)

    ic += f'<rect x="310" y="8" width="282" height="92" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Geleneksel Ebru Sanatı', 11.3, MAVI)
    ic += f'<path d="M326 56 q14 -12 28 0 t28 0 M326 70 q14 12 28 0 t28 0" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(394, 50, 'Kitap süslemede ve ciltlerde', 10.3, LAC, 'start', ince=True)
    ic += yazi(394, 66, 'yan kâğıdı olarak kullanılır.', 10.3, LAC, 'start', ince=True)
    ic += yazi(394, 82, 'Ön yargıları kaldırıp bağ kurar.', 10.3, MAVI, 'start')
    return svg(600, 108, ic, 'Samsun Kavak kilim motiflerinin anlamları ve geleneksel ebru sanatının toplumsal katkısı.', 22)


def metafor_aktarim_karti():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Metafor Kullanımı ve Bilgiyi Yeniden İfade Etme İlkeleri', 11.3, KAHVE)
    kutular = [
        ('Metafor Örneği', '“Tarih, milletin hafızası', 'gibidir; geçmişi korur.”', MAVI, MAVI_A),
        ('Olguları Koruma', 'Adlar, tarihler ve olaylar', 'değiştirilmeden aktarılır.', TUR, TUR_A),
        ('Anlam Bütünlüğü', 'Yorum bilgiden ayrılır; anlam', 'abartılmaz ve eksiltilmez.', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="58" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.2, LAC, ince=True)
    return svg(600, 108, ic, 'Metafor örneği ve bilgiyi yeniden ifade etme kuralları.', 22)


def iki_tarihi_olay_karti():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Olay · 28 Kasım 1919 Maraş', 11.2, KIR)
    ic += yazi(149, 49, 'Maraş Kalesi burcundaki bayrak indirilince', 10.3, LAC, ince=True)
    ic += yazi(149, 66, 'halk Ulu Cami’de toplanıp kaleye yürüdü', 10.3, LAC, ince=True)
    ic += yazi(149, 83, 've Türk bayrağını yeniden burca dikti.', 10.4, KIR)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Olay · 15 Temmuz 2016 Direnişi', 11.2, MAVI)
    ic += yazi(451, 49, 'Devlet ve millet darbe girişimine karşı', 10.3, LAC, ince=True)
    ic += yazi(451, 66, 'omuz omuza direnerek bağımsızlığı korudu;', 10.3, LAC, ince=True)
    ic += yazi(451, 83, '15 Temmuz’da bu birlik hafızada yaşatılır.', 10.4, MAVI)
    return svg(600, 104, ic, '28 Kasım 1919 Maraş bayrak olayı ve 15 Temmuz 2016 direnişi karşılaştırma kartları.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kulturel_bag_sema()
    s[4]['gorsel'] = dil_urunleri_panosu()
    s[5]['gorsel'] = kultur_bag_kartlari()
    s[6]['gorsel'] = mevlana_yunus_karti()
    s[7]['gorsel'] = zimem_zinciri()
    s[8]['gorsel'] = deprem_dayanisma_karti()
    s[9]['gorsel'] = sanat_motif_karti()
    s[10]['gorsel'] = metafor_aktarim_karti()
    s[12]['gorsel'] = iki_tarihi_olay_karti()
