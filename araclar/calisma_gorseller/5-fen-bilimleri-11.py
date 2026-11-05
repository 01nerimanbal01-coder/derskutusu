"""5. sınıf Fen Bilimleri 11. hafta (Sürtünme Kuvveti, Pürüzlü-Kaygan Yüzeyler, Hava ve Su Direnci) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def egik_duzlem_uc_zemin():
    zeminler = [
        ('1. P Zemini', 'Alınan Yol = 35 cm', 'Kısa mesafede durdu', KIR, KIR_A),
        ('2. R Zemini', 'Alınan Yol = 90 cm', 'En uzağa ulaştı', YES, YES_A),
        ('3. S Zemini', 'Alınan Yol = 60 cm', 'Orta mesafede durdu', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(zeminler):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 22, bas, 10.3, r)
        ic += yazi(x + 56, 45, s1, 9.9, LAC)
        ic += yazi(x + 56, 66, s2, 9.4, LAC, ince=True)
    return svg(360, 88, ic, 'Eğik düzlemden bırakılan arabanın P, R ve S zeminlerinde aldığı yollar.', 15)


def gunluk_yasam_surtunme_kartlari():
    kartlar = [
        ('1. Kış Zinciri', 'Buzlu yolda lastik', MAVI, MAVI_A),
        ('2. Yağlama', 'Kapı menteşesi', YES, YES_A),
        ('3. Paraşüt', 'Geniş kubbe yüzeyi', TUR, TUR_A),
        ('4. Hızlı Tren', 'Sivri (V) burun', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Günlük yaşamda sürtünmeyi artıran ve azaltan dört uygulama kartı.', 15)


def dort_zemin_dinamometre_olcumu():
    olcumler = [
        ('K Zemini', 'Dinamometre: 14 N', MAVI, MAVI_A),
        ('L Zemini', 'Dinamometre: 28 N', KIR, KIR_A),
        ('M Zemini', 'Dinamometre: 6 N', YES, YES_A),
        ('N Zemini', 'Dinamometre: 19 N', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, deger, r, z) in enumerate(olcumler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, deger, 9.8, LAC)
    return svg(360, 94, ic, 'Özdeş takozun K, L, M ve N zeminlerinde dinamometre çekim değerleri.', 15)


def iki_kizak_hareket_yonu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Kızak · Buz Pisti', 10.3, MAVI)
    ic += yazi(91, 44, 'Hareket Yönü: Kuzey (↑)', 9.9, LAC)
    ic += yazi(91, 65, 'Sürtünme Yönü: ?', 9.8, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Kızak · Karlı Zemin', 10.3, TUR)
    ic += yazi(269, 44, 'Hareket Yönü: Batı (←)', 9.9, LAC)
    ic += yazi(269, 65, 'Sürtünme Yönü: ?', 9.8, TUR, ince=True)
    return svg(360, 88, ic, 'Kuzey ve Batı yönlerinde kayan iki kızağın hareket kartları.', 15)


def parasut_ucak_hava_direnci():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Paraşüt Tasarımı', 10.3, YESIL_K)
    ic += yazi(91, 44, 'Geniş kubbe yüzey alanı', 9.7, LAC)
    ic += yazi(91, 65, 'Hedef: Yavaş ve güvenli iniş', 9.4, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Yolcu Uçağı Tasarımı', 10.3, MOR)
    ic += yazi(269, 44, 'Sivri ve aerodinamik burun', 9.7, LAC)
    ic += yazi(269, 65, 'Hedef: Hızlı ve ekonomik uçuş', 9.4, MOR, ince=True)
    return svg(360, 88, ic, 'Paraşüt ve yolcu uçağının hava direncine göre tasarım kartları.', 15)


def dort_zemin_puruzluluk_kartlari():
    kartlar = [
        ('Kart A', 'Cilalı seramik', MAVI, MAVI_A),
        ('Kart B', 'Çakıllı toprak', KIR, KIR_A),
        ('Kart C', 'Buz pisti', CAM, CAM_A),
        ('Kart D', 'Ahşap tahta', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 54, met, 9.3, LAC, ince=True)
    return svg(360, 84, ic, 'Farklı pürüzlülüğe sahip dört zemin kartı.', 15)


def hava_su_bilye_deneyi():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'I. Kap · Hava Ortamı', 10.3, CAM)
    ic += yazi(91, 44, 'Özdeş cam bilye bırakıldı', 9.7, LAC, ince=True)
    ic += yazi(91, 65, 'Tabana Ulaşma: 0,4 saniye', 9.8, LAC)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'II. Kap · Su Ortamı', 10.3, MAVI)
    ic += yazi(269, 44, 'Özdeş cam bilye bırakıldı', 9.7, LAC, ince=True)
    ic += yazi(269, 65, 'Tabana Ulaşma: 1,8 saniye', 9.8, LAC)
    return svg(360, 88, ic, 'Hava ve su dolu silindirlerde özdeş cam bilyelerin düşüş süresi.', 15)


def surtunme_olumlu_olumsuz_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, 'Olumsuz Etkileri', 10.3, KIR)
    ic += yazi(91, 44, '• Dişli ve taban aşınması', 9.6, LAC, ince=True)
    ic += yazi(91, 64, '• Fazladan enerji kaybı', 9.6, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Vazgeçilmez Olumlu Etkileri', 10.3, YESIL_K)
    ic += yazi(269, 44, '• Yürüme ve güvenli frenleme', 9.6, LAC, ince=True)
    ic += yazi(269, 64, '• Kalem tutma ve yazı yazma', 9.6, LAC, ince=True)
    return svg(360, 88, ic, 'Sürtünme kuvvetinin olumlu ve olumsuz etkileri.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = egik_duzlem_uc_zemin()
    s[2]['gorsel'] = gunluk_yasam_surtunme_kartlari()
    s[5]['gorsel'] = dort_zemin_dinamometre_olcumu()
    s[6]['gorsel'] = iki_kizak_hareket_yonu()
    s[7]['gorsel'] = parasut_ucak_hava_direnci()
    s[8]['gorsel'] = dort_zemin_puruzluluk_kartlari()
    s[9]['gorsel'] = hava_su_bilye_deneyi()
    s[11]['gorsel'] = surtunme_olumlu_olumsuz_karti()
