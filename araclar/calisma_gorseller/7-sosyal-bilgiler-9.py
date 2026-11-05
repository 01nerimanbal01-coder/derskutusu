"""7. sınıf Sosyal Bilgiler 9. hafta (Bölgesel ve Küresel Sorunların Çözümünde Türkiye’nin Rolü ve Uluslararası Kuruluşlar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kuresel_sorun_sinif_panosu():
    kartlar = [
        ('1. Çevre ve İklim', 'Küresel ısınma · Kuraklık', YES, YES_A),
        ('2. İnsani ve Sosyal', '? (Boş bırakılan kart)', KIR, KIR_A),
        ('3. Güvenlik ve Barış', 'Uluslararası terör · Savaş', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 104}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 56, 56, alt, 9.2, LAC, ince=True)
    return svg(360, 86, ic, 'Küresel sorunların üç ana grupta sınıflandırılması panosu.', 15)


def bm_kriz_senaryo_kartlari():
    kartlar = [
        ('1. Salgın Kriz', 'WHO · Sağlık', YES, YES_A),
        ('2. Çocuk Kriz', '? · Çocuk Hakları', MAVI, MAVI_A),
        ('3. Miras Kriz', '? · Kültür/Eğitim', TUR, TUR_A),
        ('4. Göç Kriz', 'UNHCR · ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.3, LAC, ince=True)
    return svg(360, 82, ic, 'Dört küresel kriz senaryosu ve BM uzmanlık kuruluşları.', 14)


def turkiye_uc_kurum_bulteni():
    kutular = [
        ('I. Kurum', 'Deprem bölgesinde arama-kurtarma', MAVI, MAVI_A),
        ('II. Kurum', 'Afrika’da su kuyusu ve okul inşası', YES, YES_A),
        ('III. Kurum', 'Savaş mağdurlarına çadır ve gıda', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 23, bas, 10.2, r)
        ic += yazi(x + 56, 52, alt, 9.1, LAC, ince=True)
    return svg(360, 86, ic, 'AFAD, TİKA ve Türk Kızılay’ın küresel görev bülteni.', 15)


def yerel_kuresel_olcek_kartlari():
    kutular = [
        ('1. Kart (Yerel)', 'Mahalle parkı lambası', MAVI, MAVI_A),
        ('2. Kart (Yerel)', 'Köy yolu heyelanı', YES, YES_A),
        ('3. Kart (Küresel)', 'Sera gazı ve iklim krizi', KIR, KIR_A),
        ('4. Kart (Yerel)', 'Apartman su kesintisi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r)
        ic += yazi(x + 86, y + 14, bas, 10.0, r)
        ic += yazi(x + 86, y + 29, icerik, 9.5, LAC, ince=True)
    return svg(360, 90, ic, 'Yerel ve küresel ölçekli sorunların karşılaştırma kartları.', 15)


def tahil_koridoru_diplomasi_karti():
    ic = kutu(6, 6, 348, 74, TUR_A, TUR)
    ic += yazi(180, 22, 'Karadeniz Tahıl Koridoru Anlaşması (İstanbul)', 10.4, TUR)
    ic += yazi(180, 44, 'Rusya-Ukrayna Savaşı’nda Türkiye ve BM iş birliği', 9.6, LAC, ince=True)
    ic += yazi(180, 64, 'Türkiye’nin Rolü: ?  ·  Küresel Gıdaya Katkısı: ?', 9.6, MAVI)
    return svg(360, 86, ic, 'Karadeniz Tahıl Koridoru Anlaşması ve Türkiye’nin arabuluculuğu.', 14)


def iklim_goc_zinciri_seridi():
    adimlar = [
        ('1. Neden', 'Fosil Yakıt & Sera Gazı', KIR, KIR_A),
        ('2. İklim', 'Isınma & Kuraklık', TUR, TUR_A),
        ('3. Gıda', 'Tarım Kaybı & Açlık', MOR, MOR_A),
        ('4. Sonuç', 'Zorunlu İklim Göçü', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 52, alt, 8.9, LAC, ince=True)
    return svg(360, 82, ic, 'Fosil yakıt tüketiminden zorunlu iklim göçüne uzanan zincir.', 14)


def turkiye_uyelikler_panosu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Küresel Barış ve Uzmanlık', 10.1, MAVI)
    ic += yazi(91, 43, 'BM (Kurucu Üye) · NATO · AGİT', 9.3, LAC, ince=True)
    ic += yazi(91, 63, 'FAO · WHO · UNICEF · UNESCO', 9.3, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Bölgesel ve Kültürel İş Birliği', 10.1, YES)
    ic += yazi(269, 43, 'TDT (Türk Devletleri Teşkilatı)', 9.3, LAC, ince=True)
    ic += yazi(269, 63, 'KEİ (Karadeniz) · İİT · D-8', 9.3, YES)
    return svg(360, 88, ic, 'Türkiye’nin üyesi olduğu küresel ve bölgesel kuruluşlar panosu.', 15)


def sifir_atik_vatandas_karti():
    ic = kutu(6, 6, 170, 74, YES_A, YES)
    ic += yazi(91, 22, '1. Evde ve Okulda Tasarruf', 10.1, YES)
    ic += yazi(91, 43, 'Su ve elektrik israfını önleme', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 'Karbon ve su ayak izini azaltma', 9.3, YES)

    ic += kutu(184, 6, 170, 74, CAM_A, CAM)
    ic += yazi(269, 22, '2. Sıfır Atık (30 Mart BM)', 10.1, CAM)
    ic += yazi(269, 43, 'Atıkları kaynağında ayrıştırma', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'Geri dönüşüm ve ağaçlandırma', 9.3, CAM)
    return svg(360, 86, ic, 'Sıfır Atık ve küresel vatandaşlık sorumluluk kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kuresel_sorun_sinif_panosu()
    s[2]['gorsel'] = bm_kriz_senaryo_kartlari()
    s[5]['gorsel'] = turkiye_uc_kurum_bulteni()
    s[6]['gorsel'] = yerel_kuresel_olcek_kartlari()
    s[7]['gorsel'] = tahil_koridoru_diplomasi_karti()
    s[8]['gorsel'] = iklim_goc_zinciri_seridi()
    s[9]['gorsel'] = turkiye_uyelikler_panosu()
    s[11]['gorsel'] = sifir_atik_vatandas_karti()
