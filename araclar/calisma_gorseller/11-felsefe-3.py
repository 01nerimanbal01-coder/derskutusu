"""11. sınıf Felsefe 3. hafta (Çevre Etiği Yaklaşımları) görselleri.
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


def cevre_etigi_kartlari():
    kartlar = [
        ('1. Antroposentrik', 'İnsan Merkezli Araç', TUR, TUR_A),
        ('2. Biyosentrik', 'Tüm Canlılar Eşit', YES, YES_A),
        ('3. Ekosentrik', 'Canlı + Cansız Bütün', MAVI, MAVI_A),
        ('4. Derin Ekoloji', 'Köklü Zihniyet Değişimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Çevre etiği 4 temel yaklaşım kartı.', 34)


def aracsal_icsel_deger_semasi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'ÇEVRE FELSEFESİNDE DEĞER SINIFLANDIRMASI', 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Araçsal Değer (Fayda)', 9.2, TUR)
    ic += yazi(92, 76, 'Doğa insanın emrindedir', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Tüketim &amp; maddi kazanç', 8.6, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'İçsel Değer (Öz Değer)', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Varlığın kendisi amaçtır', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Faydadan bağımsız ahlaki hak', 8.6, YES, ince=True)
    return svg(360, 125, ic, 'Araçsal ve içsel değer karşılaştırması.', 34)


def kusaklararasi_sorumluluk_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'HANS JONAS: GELECEK KUŞAKLARA KARŞI SORUMLULUK', 9.8, TUR)
    ic += kutu(16, 36, 96, 70, '#ffffff', MAVI)
    ic += yazi(64, 56, 'Bugünkü Kuşak', 9.0, MAVI)
    ic += yazi(64, 76, 'Teknolojik güç', 8.4, LAC, ince=True)
    ic += yazi(64, 92, 'Tüketim kararı', 8.4, MAVI, ince=True)
    ic += kutu(132, 36, 96, 70, '#ffffff', TUR)
    ic += yazi(180, 56, 'Ahlaki Köprü', 9.0, TUR)
    ic += yazi(180, 76, 'Sorumluluk ilkesi', 8.4, LAC, ince=True)
    ic += yazi(180, 92, 'Özen &amp; sakınma', 8.4, TUR, ince=True)
    ic += kutu(248, 36, 96, 70, '#ffffff', YES)
    ic += yazi(296, 56, 'Gelecek Kuşak', 9.0, YESIL_K)
    ic += yazi(296, 76, 'Varoluş hakkı', 8.4, LAC, ince=True)
    ic += yazi(296, 92, 'Temiz bir dünya', 8.4, YES, ince=True)
    return svg(360, 125, ic, 'Kuşaklararası etik sorumluluk kesiti.', 34)


def biyotik_topluluk_dongusu():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'ALDO LEOPOLD: TOPRAK ETİĞİ VE BİYOTİK TOPLULUK', 9.8, YESIL_K)
    kartlar = [
        ('Toprak &amp; Kaya', 'Cansız mineral temel', 16),
        ('Su &amp; Hava', 'Hayat döngüsü akışı', 102),
        ('Bitki &amp; Hayvan', 'Biyotik ağ paydaşı', 188),
        ('İnsan Türü', 'Eşit topluluk yurttaşı', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Toprak etiği biyotik topluluk kartı.', 34)


def sig_derin_ekoloji_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'SIĞ EKOLOJİ İLE DERİN EKOLOJİ KARŞILAŞTIRMASI', 9.8, MOR)
    satirlar = [
        ('Ölçüt', 'Sığ Ekoloji', 'Derin Ekoloji', MOR),
        ('Odak Noktası', 'İnsanın Çıkarları &amp; Refahı', 'Bütün Ekosistemin Dengesi', TUR),
        ('Yaklaşım', 'Mevcut Tüketime Filtre Takma', 'Köklü Yaşam Tarzı Değişimi', YESIL_K),
        ('Doğanın Rolü', 'Yalnızca Doğal Hammadde', 'İçsel Değer Taşıyan Canlı Ağ', MAVI),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(70, y + 13, k1, 8.4, r)
        ic += yazi(180, y + 13, k2, 8.2, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.2, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Sığ ve derin ekoloji karşılaştırma tablosu.', 34)


def ekolojik_ayakizi_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'EKOLOJİK AYAK İZİ VE DÜNYA TAŞIMA KAPASİTESİ', 10.0, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Aşırı Tüketim Çılgınlığı', 9.2, KIR)
    ic += yazi(92, 76, 'Kaynakların tükenmesi', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Biyoçeşitlilik kaybı', 8.6, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'Sürdürülebilir Uyum', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Döngüsel ekolojik yaşam', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Geleceğe saygılı tüketim', 8.6, YES, ince=True)
    return svg(360, 125, ic, 'Ekolojik ayak izi ve denge şeması.', 34)


def surdurulebilir_etik_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'SÜRDÜRÜLEBİLİR ÇEVRE ETİĞİ BASAMAKLARI', 10.0, YESIL_K)
    kartlar = [
        ('1. Farkındalık', 'Ekolojik sınırları kavrama', 16),
        ('2. Sadeleşme', 'Gereksiz tüketimi kısma', 102),
        ('3. Koruma', 'Doğal habitatı savunma', 188),
        ('4. Dayanışma', 'Bütün türlerle barışık olma', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Sürdürülebilir çevre etiği adımları.', 34)


def etik_deger_kutulari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 24, 'ÇEVRE FELSEFESİ SORUMLULUK AŞAMALARI', 10.2, MOR)
    kutular = ['Varlık Bilinci', 'İçsel Değer', 'Ahlaki Ödev', 'Biyotik Bütün']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', MOR, r=4)
        ic += yazi(x + 37, 66, f'{i + 1}. İlke', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.4, MOR)
    return svg(360, 125, ic, 'Çevre etiği sorumluluk akış kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cevre_etigi_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = aracsal_icsel_deger_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = kusaklararasi_sorumluluk_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = biyotik_topluluk_dongusu()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = sig_derin_ekoloji_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = ekolojik_ayakizi_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = surdurulebilir_etik_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = etik_deger_kutulari()
    s[10]['en_fazla'] = 34
