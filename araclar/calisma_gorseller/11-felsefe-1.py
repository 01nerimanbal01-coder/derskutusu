"""11. sınıf Felsefe 1. hafta (Çevre Etiği: Değer, Sorumluluk ve Üç Yaklaşım) görselleri.
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


def cevre_etigi_uc_yaklasim():
    kartlar = [
        ('1. İnsan Merkezci', 'Antroposentrizm', TUR, TUR_A),
        ('2. Canlı Merkezci', 'Biyosentrizm', YES, YES_A),
        ('3. Çevre Merkezci', 'Ekosentrizm', MAVI, MAVI_A),
        ('4. Sorumluluk', 'Gelecek Kuşaklar', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Çevre etiğinde üç yaklaşım karşılaştırma kartı.', 34)


def deger_terazisi_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'FELSEFEDE İKİ DEĞER ANLAYIŞI KARŞILAŞTIRMASI', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, TUR_A, TUR)
    ic += yazi(92, 56, 'Araçsal Değer', 9.8, TUR)
    ic += yazi(92, 76, 'İnsanın faydasına araç', 8.9, LAC, ince=True)
    ic += yazi(92, 92, 'Faydacı yaklaşım', 8.9, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'İçsel Değer', 9.8, YESIL_K)
    ic += yazi(267, 76, 'Kendi varlığıyla değerli', 8.9, LAC, ince=True)
    ic += yazi(267, 92, 'Doğanın kendinde değeri', 8.9, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Araçsal değer ve içsel değer dengesi şeması.', 34)


def etik_cember_diyagrami():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'GENİŞLEYEN AHLAKİ ÇEMBER MODELİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 95, 70, TUR_A, TUR)
    ic += yazi(67, 56, 'İç Çember', 9.4, TUR)
    ic += yazi(67, 76, 'Yalnız İnsan', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Antroposentrik', 8.8, TUR, ince=True)

    ic += kutu(132, 36, 95, 70, YES_A, YES)
    ic += yazi(179, 56, 'Orta Çember', 9.4, YESIL_K)
    ic += yazi(179, 76, 'Tüm Canlılar', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Biyosentrik', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 36, 95, 70, MAVI_A, MAVI)
    ic += yazi(292, 56, 'Dış Çember', 9.4, MAVI)
    ic += yazi(292, 76, 'Bütün Ekosistem', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Ekosentrik', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Genişleyen etik çember modeli şeması.', 34)


def sorumluluk_ilkesi_modeli():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'HANS JONAS SORUMLULUK İLKESİ ETİĞİ', 10.3, MOR)
    ic += kutu(20, 38, 145, 68, '#ffffff', MOR)
    ic += yazi(92, 58, 'Bugünkü İnsan', 9.6, MOR)
    ic += yazi(92, 78, 'Teknolojik güç &amp; eylem', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Kaynakları tüketme riski', 8.8, KIR, ince=True)

    ic += kutu(195, 38, 145, 68, YES_A, YES)
    ic += yazi(267, 58, 'Gelecek Kuşaklar', 9.6, YESIL_K)
    ic += yazi(267, 78, 'Yaşam hakkı güvencesi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Ahlaki emanet bilinci', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Gelecek kuşaklar ve sorumluluk etiği modeli.', 34)


def cevre_tarih_seridi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'İNSAN-DOĞA İLİŞKİSİNİN TARİHSEL DÖNÜŞÜMÜ', 10.2, CAM)
    adımlar = [
        ('1. Dönem', 'Doğayla Uyum', 16),
        ('2. Dönem', 'Doğaya Hâkimiyet', 102),
        ('3. Dönem', 'Ekolojik Kriz', 188),
        ('4. Dönem', 'Çevre Etiği', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.3, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'İnsan doğa ilişkisinin felsefi zaman şeridi.', 34)


def xyz_yaklasim_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'X, Y, Z ÇEVRE ETİĞİ HİYERARŞİSİ', 10.2, TUR)
    ic += kutu(20, 36, 95, 70, '#ffffff', TUR)
    ic += yazi(67, 56, 'X: İnsan Odaklı', 9.2, TUR)
    ic += yazi(67, 82, 'Antroposentrik', 8.6, LAC, ince=True)

    ic += kutu(132, 36, 95, 70, '#ffffff', YES)
    ic += yazi(179, 56, 'Y: Canlı Odaklı', 9.2, YESIL_K)
    ic += yazi(179, 82, 'Biyosentrik', 8.6, LAC, ince=True)

    ic += kutu(245, 36, 95, 70, MAVI_A, MAVI)
    ic += yazi(292, 56, 'Z: [ ? = Ekosentrik ]', 9.2, MAVI)
    ic += yazi(292, 82, 'Bütüncül Çevre', 8.6, MAVI, ince=True)
    return svg(360, 125, ic, 'X, Y, Z yaklaşımları soru şeması.', 34)


def kavram_eslestirme_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'FELSEFİ KAVRAMLAR VE ETİK TANIMLARI', 10.1, YESIL_K)
    kartlar = [
        ('İçsel Değer', 'Kendinde Değer', 16),
        ('Araçsal Değer', 'Menfaat Aracı', 102),
        ('Biyotik Birlik', 'Ortak Yaşam Ağı', 188),
        ('Sorumluluk', 'Ahlaki Yükümlülük', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.3, LAC, ince=True)
    return svg(360, 125, ic, 'Felsefi kavramlar eşleştirme tablosu.', 34)


def etik_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MOR)
    harfler = ['E', 'T', 'İ', 'K']
    for i, h in enumerate(harfler):
        x = 75 + i * 56
        ic += kutu(x, 42, 48, 52, '#ffffff', MOR, r=4)
        ic += yazi(x + 24, 74, h, 16.0, MOR)
        ic += yazi(x + 24, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Etik kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cevre_etigi_uc_yaklasim()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = deger_terazisi_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = etik_cember_diyagrami()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = sorumluluk_ilkesi_modeli()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = cevre_tarih_seridi()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = xyz_yaklasim_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = kavram_eslestirme_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = etik_sifre_kutulari()
    s[10]['en_fazla'] = 34
