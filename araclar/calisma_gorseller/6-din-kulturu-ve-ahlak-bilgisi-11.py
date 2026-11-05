"""6. sınıf Din Kültürü ve Ahlak Bilgisi 11. hafta (Oruç İbadetinin Birey ve Toplum Hayatına Kazandırdıkları, İnfak ve Fitre) çalışma kâğıdı görselleri.
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


def oruc_kalkandir_hadis_karti():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'HADİS-İ ŞERİF KARTI · AHLAKİ KORUNMA (TAKVA)', 10.2, MAVI)
    ic += yazi(180, 44, '“Oruç bir kalkandır. Oruçlu kimse kötü söz söylemesin ve kavga etmesin.”', 9.5, LAC)
    ic += yazi(180, 66, 'Yalan, gıybet, iftira ve öfkeden uzak durma → İrade ve öz denetim', 9.3, MAVI, ince=True)
    return svg(360, 88, ic, 'Oruç bir kalkandır hadisini açıklayan bilgi kartı.', 15)


def yardim_turleri_panosu():
    kartlar = [
        ('1. Genel Sadaka', 'Sünnet · Sınır yok', MAVI, MAVI_A),
        ('2. Fitre', 'Hükmü ve zamanı = ?', YES, YES_A),
        ('3. Fidye', 'Oruç tutamayan bedeli', TUR, TUR_A),
        ('4. Tebessüm', 'Manevi sadaka = ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Sadaka, fitre, fidye ve manevi sadaka karşılaştırma panosu.', 15)


def fitre_verilebilecekler_semasi():
    kutular = [
        ('1. Kutu: Anne ve Baba', 'Bakmakla yükümlü (Usul)', KIR, KIR_A),
        ('2. Kutu: Küçük Çocuklar', 'Bakmakla yükümlü (Füru)', KIR, KIR_A),
        ('3. Kutu: Yoksul Komşu', 'İhtiyaç sahibi (Verilir)', YES, YES_A),
        ('4. Kutu: Dede ve Nine', 'Bakmakla yükümlü (Usul)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Fitre verilebilen ve verilemeyen yakınları gösteren şema.', 16)


def dort_kazanim_karti():
    kartlar = [
        ('1. Kart · Sağlık', 'Sindirim sistemi dinlenir', MAVI, MAVI_A),
        ('2. Kart · Dayanışma', 'İftar, erzak kolisi ve fitre', YES, YES_A),
        ('3. Kart · Öz Disiplin', 'Sahurla zaman yönetimi', TUR, TUR_A),
        ('4. Kart · İbadet Süresi', 'İmsaktan iftara kadar', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Orucun bireysel ve toplumsal yönlerini gösteren dört kart.', 16)


def aile_fitre_hesap_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'Aile Bireyleri Sayısı', 10.2, CAM)
    ic += yazi(91, 44, 'Anne + Baba + 3 Çocuk', 9.7, LAC)
    ic += yazi(91, 64, 'Toplam: 5 Kişilik Aile', 9.6, CAM)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '1 Kişilik Fitre Bedeli', 10.2, YESIL_K)
    ic += yazi(269, 44, 'Günlük Gıda Ölçüsü: 180 TL', 9.6, LAC)
    ic += yazi(269, 64, 'Toplam Fitre Tutarı = ? TL', 9.6, YESIL_K)
    return svg(360, 88, ic, 'Beş kişilik bir ailenin vereceği toplam fitre tutarı hesaplama kartı.', 15)


def oruc_degerler_zinciri():
    adimlar = [
        ('1. Sabır', 'Niyet ve irade', MAVI, MAVI_A),
        ('2. Empati', 'Şükür ve duyarlılık', YES, YES_A),
        ('3. İnfak', 'Fitre ve sadaka', TUR, TUR_A),
        ('4. Kardeşlik', 'Toplumsal barış', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Sabırdan toplumsal kardeşliğe uzanan dört aşamalı değer zinciri.', 15)


def fitre_fidye_karsilastirma():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 21, 'Fıtır Sadakası (Fitre)', 10.2, YESIL_K)
    ic += yazi(91, 42, '• Zengin olan her Müslüman verir', 9.1, LAC, ince=True)
    ic += yazi(91, 61, '• Bayram namazından önce (Vacip)', 9.1, YESIL_K)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 21, 'Oruç Fidyesi', 10.2, TUR)
    ic += yazi(269, 42, '• Yaşlı/kalıcı hasta (tutamayan)', 9.1, LAC, ince=True)
    ic += yazi(269, 61, '• Her gün için 1 fitre miktarı', 9.1, TUR)
    return svg(360, 88, ic, 'Fitre ve fidye ibadetlerinin karşılaştırma panosu.', 15)


def zimem_defteri_ahlak_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'ZİMEM DEFTERİ GELENEĞİ · GİZLİ İNFAK AHLAKI', 10.2, MOR)
    ic += yazi(180, 44, 'Hayırsever kişi mahalle bakkalındaki veresiye borçlarını gizlice sildirir.', 9.5, LAC)
    ic += yazi(180, 66, 'İlke: “Sağ elin verdiğini sol el görmemelidir.” (Riyadan uzaklık ve onur)', 9.2, MOR, ince=True)
    return svg(360, 88, ic, 'Zimem defteri geleneği ve gizli yardımlaşma ahlakı kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = oruc_kalkandir_hadis_karti()
    s[2]['gorsel'] = yardim_turleri_panosu()
    s[5]['gorsel'] = fitre_verilebilecekler_semasi()
    s[6]['gorsel'] = dort_kazanim_karti()
    s[7]['gorsel'] = aile_fitre_hesap_karti()
    s[8]['gorsel'] = oruc_degerler_zinciri()
    s[9]['gorsel'] = fitre_fidye_karsilastirma()
    s[11]['gorsel'] = zimem_defteri_ahlak_karti()
