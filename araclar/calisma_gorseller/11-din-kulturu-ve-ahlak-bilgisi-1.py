"""11. sınıf Din Kültürü ve Ahlak Bilgisi 1. hafta görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kader_kavram_kartlari():
    kartlar = [
        ('1. Külli İrade', 'Mutlak irade', MOR, MOR_A),
        ('2. Cüzi İrade', 'Sorumlu seçim', MAVI, MAVI_A),
        ('3. Tevekkül', 'Tedbir ve güven', YES, YES_A),
        ('4. Ecel &amp; Ömür', 'Takdir edilen süre', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.2, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Kader kavramları temel kartları.', 34)


def kader_sorumluluk_akisi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İNSAN İRADESİ VE SORUMLULUK DÖNGÜSÜ', 10.3, MAVI)
    ic += kutu(16, 36, 95, 70, YES_A, YES)
    ic += yazi(63, 54, 'Akıl &amp; Cüzi İrade', 9.4, YESIL_K)
    ic += yazi(63, 74, 'Özgür Tercih', 8.8, LAC, ince=True)
    ic += yazi(63, 90, 'Emek Verme', 8.8, YESIL_K, ince=True)

    ic += kutu(132, 36, 95, 70, TUR_A, TUR)
    ic += yazi(179, 54, 'Eylem &amp; Çaba', 9.4, TUR)
    ic += yazi(179, 74, 'Meşru Çalışma', 8.8, LAC, ince=True)
    ic += yazi(179, 90, 'Tedbir Alma', 8.8, TUR, ince=True)

    ic += kutu(248, 36, 95, 70, MOR_A, MOR)
    ic += yazi(295, 54, 'Sonuç &amp; Mesuliyet', 9.4, MOR)
    ic += yazi(295, 74, 'Kişisel Sorumluluk', 8.8, LAC, ince=True)
    ic += yazi(295, 90, 'Tevekkül Bilinci', 8.8, MOR, ince=True)
    return svg(360, 125, ic, 'İnsan iradesi ve sorumluluk döngüsü modeli.', 34)


def evrensel_yasalar_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'EVRENDEKİ ÖLÇÜ VE YASALAR (SÜNNETULLAH)', 10.3, YESIL_K)
    yasalar = [
        ('Fiziksel Yasalar', 'Madde ve Enerji', MAVI, 16),
        ('Biyolojik Yasalar', 'Canlılar ve Hayat', YES, 130),
        ('Toplumsal Yasalar', 'Adalet ve Ahlak', TUR, 244),
    ]
    for b, d, r, x in yasalar:
        ic += kutu(x, 36, 100, 70, '#ffffff', r)
        ic += yazi(x + 50, 56, b, 9.4, r)
        ic += f'<line x1="{x + 10}" y1="66" x2="{x + 90}" y2="66" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 50, 86, d, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Evrensel yasalar karşılaştırma şeması.', 34)


def tevekkul_terazisi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'DOĞRU TEVEKKÜL ANLAYIŞI DENGESİ', 10.3, CAM)
    ic += kutu(20, 38, 145, 68, TUR_A, TUR)
    ic += yazi(92, 58, '1. Kanat: Tedbir &amp; Gayret', 9.6, TUR)
    ic += yazi(92, 78, 'Çalışma, emek, önlem', 8.9, LAC, ince=True)
    ic += yazi(92, 92, 'Cüzi iradeyi kullanma', 8.9, TUR, ince=True)

    ic += kutu(195, 38, 145, 68, YES_A, YES)
    ic += yazi(267, 58, '2. Kanat: Teslimiyet &amp; Dua', 9.6, YESIL_K)
    ic += yazi(267, 78, "Sonucu Allah'a bırakma", 8.9, LAC, ince=True)
    ic += yazi(267, 92, 'Huzur ve rıza hali', 8.9, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Doğru tevekkül dengesi şeması.', 34)


def sinav_tevekkul_basamaklari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 20, 'BAŞARI VE TEVEKKÜL UYGULAMA ADIMLARI', 10.2, TUR)
    adımlar = [
        ('1. Karar', 'İradeyi koyma', 16),
        ('2. Emek', 'Planlı çalışma', 102),
        ('3. Gayret', 'Sınavda dikkat', 188),
        ('4. Tevekkül', 'Huzurla güven', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 56, b, 9.3, TUR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Başarı ve tevekkül uygulama basamakları.', 34)


def toplumsal_yasa_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'TOPLUMLARIN GELİŞİMİNİ DÜZENLEYEN İLKELER', 10.2, MOR)
    ic += kutu(20, 36, 95, 70, '#ffffff', MOR)
    ic += yazi(67, 56, 'Fiziksel Yasa', 9.2, LAC)
    ic += yazi(67, 82, 'Gezegen &amp; Su', 8.6, MOR, ince=True)

    ic += kutu(132, 36, 95, 70, '#ffffff', MOR)
    ic += yazi(179, 56, 'Biyolojik Yasa', 9.2, LAC)
    ic += yazi(179, 82, 'Canlı &amp; Doğa', 8.6, MOR, ince=True)

    ic += kutu(245, 36, 95, 70, YES_A, YES)
    ic += yazi(292, 56, '[ ? = Toplumsal ]', 9.4, YESIL_K)
    ic += yazi(292, 82, 'Adalet &amp; Barış', 8.6, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Toplumsal yasalar soru işareti diyagramı.', 34)


def ayet_yasa_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'AYETLER VE EVRENSEL YASA EŞLEŞTİRMELERİ', 10.1, YESIL_K)
    kartlar = [
        ('Gece &amp; Gündüz', 'Fiziksel Yasa', 16),
        ('İnsanın Yaratılışı', 'Biyolojik Yasa', 102),
        ('Kavimlerin Akıbeti', 'Toplumsal Yasa', 188),
        ('Ölçülü Yağmur', 'Kader İlkesi', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Ayetler ve evrensel yasalar tablosu.', 34)


def kader_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'KADER KAVRAMI ŞİFRE KUTULARI', 10.4, MAVI)
    harfler = ['K', 'A', 'D', 'E', 'R']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 22, 74, h, 16.0, MAVI)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Kader kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kader_kavram_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = kader_sorumluluk_akisi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = evrensel_yasalar_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = tevekkul_terazisi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = sinav_tevekkul_basamaklari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = toplumsal_yasa_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = ayet_yasa_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = kader_sifre_kutulari()
    s[10]['en_fazla'] = 34
