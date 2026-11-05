"""11. sınıf Din Kültürü 3. hafta (Akıl, İrade ve Sorumluluk) görselleri.
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


def irade_kavram_kartlari():
    kartlar = [
        ('1. Akıl (Temyiz)', 'İyiyi Kötüden Ayırma', YES, YES_A),
        ('2. Cüz’î İrade', 'Hür Seçim Yapabilme', MAVI, MAVI_A),
        ('3. Küllî İrade', 'İlahi Kuşatıcı Kudret', TUR, TUR_A),
        ('4. Mesuliyet', 'Hesap Verme Bilinci', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.8, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Akıl, irade ve sorumluluk kavram kartları.', 34)


def secim_ve_sorumluluk_semasi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İNSANIN TERCİH ÖZGÜRLÜĞÜ VE AHLAKİ MESULİYETİ', 9.8, MAVI)
    ic += kutu(16, 36, 96, 70, '#ffffff', YES)
    ic += yazi(64, 56, 'Hür Seçim', 9.2, YESIL_K)
    ic += yazi(64, 76, 'Cüz’î İrade', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Farklı Yollar', 8.4, YES, ince=True)
    ic += kutu(132, 36, 96, 70, '#ffffff', TUR)
    ic += yazi(180, 56, 'Eyleme Dönüş', 9.2, TUR)
    ic += yazi(180, 76, 'Bilinçli Tercih', 8.4, LAC, ince=True)
    ic += yazi(180, 92, 'Amel &amp; Davranış', 8.4, TUR, ince=True)
    ic += kutu(248, 36, 96, 70, '#ffffff', MOR)
    ic += yazi(296, 56, 'Ahlaki Mesuliyet', 9.2, MOR)
    ic += yazi(296, 76, 'Sonuçları Üstlenme', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'İlahi Karşılık', 8.4, MOR, ince=True)
    return svg(360, 125, ic, 'İrade ve mesuliyet süreci şeması.', 34)


def mukellefiyet_sartlari_kesiti():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'İSLAM DİNİNDE MÜKELLEFİYETİN İKİ TEMEL ŞARTI', 10.0, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, '1. Akıl Sağlığı (Temyiz)', 9.2, YESIL_K)
    ic += yazi(92, 76, 'Doğruyu yanlıştan ayırma', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Aklı olmayanın sorumluluğu yok', 8.6, YESIL_K, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(267, 56, '2. Bülûğ (Ergenlik)', 9.2, MAVI)
    ic += yazi(267, 76, 'Zihinsel &amp; bedensel olgunluk', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Bireysel kararları üstlenme', 8.6, MAVI, ince=True)
    return svg(360, 125, ic, 'Mükellefiyet şartları karşılaştırma kesiti.', 34)


def sorumluluk_bilinci_dongusu():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'SORUMLULUK BİLİNCİNİN BOYUTLARI', 10.2, TUR)
    kartlar = [
        ('Kendine Karşı', 'Sağlık &amp; Şahsiyet', 16),
        ('Yaratan’a Karşı', 'İbadet &amp; Şükür', 102),
        ('Topluma Karşı', 'Adalet &amp; Yardımlaşma', 188),
        ('Çevreye Karşı', 'Tabiatı Koruma Emaneti', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Sorumluluk bilincinin boyutları kartı.', 34)


def irade_karsilastirma_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'KÜLLÎ İRADE VE CÜZ’Î İRADE AYRIMI', 9.8, MOR)
    satirlar = [
        ('Alan', 'Küllî İrade (Allah’ın)', 'Cüz’î İrade (İnsanın)', MOR),
        ('Kapsam', 'Bütün Kâinat ve Kanunlar', 'Bireyin Kendi Tercihleri', MAVI),
        ('Seçim', 'Zorunlu (Doğum, Irk, Ecel)', 'Serbest (İman, Ahlak, Amel)', YESIL_K),
        ('Sorumluluk', 'İnsana Hesap Sorulmaz', 'Ahirette Tamamen Mesuldür', KIR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(70, y + 13, k1, 8.4, r)
        ic += yazi(180, y + 13, k2, 8.2, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.2, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Küllî ve cüz’î irade karşılaştırma tablosu.', 34)


def toplumsal_sorumluluk_piramidi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'BİREYDEN TOPLUMA AHLAKİ SORUMLULUK BASAMAKLARI', 9.8, CAM)
    adımlar = [
        ('1. Vicdan', 'İç muhakeme &amp; niyet', 16),
        ('2. Aile', 'Saygı, sevgi ve hak', 102),
        ('3. Toplum', 'Adalet ve dayanışma', 188),
        ('4. İnsanlık', 'Evrensel barış ve hayır', 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 54, b, 8.4, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Toplumsal ahlaki sorumluluk basamakları.', 34)


def emanet_bilinci_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'İLAHİ EMANET VE YERYÜZÜNÜ İMAR GÖREVİ', 10.0, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Emanet Kavramı', 9.2, YESIL_K)
    ic += yazi(92, 76, 'Akıl ve irade nimeti', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Ahlak yasalarına uyma borcu', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'İmar Sorumluluğu', 9.2, TUR)
    ic += yazi(267, 76, 'Tabiatı koruyup geliştirme', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Hakkı ve adaleti gözetme', 8.6, TUR, ince=True)
    return svg(360, 125, ic, 'Emanet ve yeryüzünü imar kartı.', 34)


def vicdan_muhakeme_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'AHLAKİ EYLEM VE KARAR MEKANİZMASI', 10.2, MAVI)
    kutular = ['Bilgi &amp; İdrak', 'Akıl &amp; Vicdan', 'Özgür Tercih', 'Sorumluluk']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 37, 66, f'{i + 1}. Basamak', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.4, MAVI)
    return svg(360, 125, ic, 'Ahlaki karar mekanizması akış kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = irade_kavram_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = secim_ve_sorumluluk_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = mukellefiyet_sartlari_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = sorumluluk_bilinci_dongusu()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = irade_karsilastirma_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = toplumsal_sorumluluk_piramidi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = emanet_bilinci_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = vicdan_muhakeme_kutulari()
    s[10]['en_fazla'] = 34
