"""6. sınıf Matematik 11. hafta (Cebirsel Düşünme: Cebirsel İfade Yazma, Terim, Katsayı, Sabit Terim ve Değer Bulma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

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


def cebirsel_serit_modeli():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 21, 'CEBİRSEL ŞERİT MODELİ · TOPLAM UZUNLUK', 10.1, MAVI)
    parcalar = [
        (MAVI, '#dbeafe', 'a cm', 54),
        (MAVI, '#dbeafe', 'a cm', 54),
        (MAVI, '#dbeafe', 'a cm', 54),
        (MAVI, '#dbeafe', 'a cm', 54),
        (TUR, TUR_A, '2', 32),
        (TUR, TUR_A, '2', 32),
        (TUR, TUR_A, '2', 32),
    ]
    x = 14
    for r, z, et, gen in parcalar:
        ic += kutu(x, 30, gen, 26, z, r, 4, 1.2)
        ic += yazi(x + gen / 2, 47, et, 9.2, LAC)
        x += gen + 3
    ic += yazi(180, 72, '4 adet “a cm” çubuk + 3 adet “2 cm” küp   →   a = 8 cm için Toplam = ?', 9.2, LAC, ince=True)
    return svg(360, 88, ic, 'Dört adet a cm çubuk ve üç adet 2 cm küpten oluşan cebirsel şerit modeli.', 15)


def terim_katsayi_panosu():
    ifade_kart = [
        ('1. İfade', '5x + 2y + 7', MAVI, MAVI_A),
        ('2. İfade', '8a − 3b + 10', YES, YES_A),
        ('3. İfade', '6m + n − 4', TUR, TUR_A),
        ('4. İfade', '9k + 5', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ifd, r, z) in enumerate(ifade_kart):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, ifd, 9.6, LAC)
    return svg(360, 84, ic, 'Terim ve katsayıları çözümlenecek dört cebirsel ifade kartı.', 15)


def kumbara_depo_durumlari():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 21, '1. Durum · Kumbara', 10.1, YESIL_K)
    ic += yazi(91, 43, 'Başlangıç: 120 TL var', 9.5, LAC)
    ic += yazi(91, 63, '6 hafta her hafta +x TL eklenir', 9.1, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 21, '2. Durum · Su Deposu', 10.1, CAM)
    ic += yazi(269, 43, 'Başlangıç: 250 L su var', 9.5, LAC)
    ic += yazi(269, 63, '4 saat her saat −y L harcanır', 9.1, CAM, ince=True)
    return svg(360, 88, ic, 'Kumbarada para biriktirme ve su deposundan su kullanma cebirsel kartları.', 15)


def uslu_deger_bulma_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'CEBİRSEL İFADENİN DEĞERİNİ BULMA · İŞLEM ÖNCELİĞİ', 10.1, MOR)
    ic += yazi(180, 46, 'Cebirsel İfade:   3x² − 4x + 9     (x = 4 için değerini bulunuz)', 10.2, LAC)
    ic += yazi(180, 67, 'Dikkat: Önce x² = 4² üslü ifadesi hesaplanır, sonra 3 ile çarpılır!', 9.2, MOR, ince=True)
    return svg(360, 88, ic, 'x eşittir 4 için 3x kare eksi 4x artı 9 ifadesinin değer kartı.', 15)


def dikdortgen_bahce_cevresi():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 21, 'Bahçe Kenar Uzunlukları', 10.0, YESIL_K)
    ic += yazi(91, 43, 'Kısa Kenar = k metre', 9.5, LAC)
    ic += yazi(91, 63, 'Uzun Kenar = (2k + 3) metre', 9.5, YESIL_K)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 21, 'İstenen Hesaplama', 10.0, TUR)
    ic += yazi(269, 43, '1) Çevre Cebirsel İfadesi = ?', 9.3, LAC)
    ic += yazi(269, 63, '2) k = 5 m için Çevre = ? m', 9.3, TUR)
    return svg(360, 88, ic, 'Kenarları k ve 2k artı 3 metre olan dikdörtgen bahçe çevre kartı.', 15)


def deger_bulma_siralama_adimlari():
    adimlar = [
        ('1. Yerine Koy', 'm = 3 yaz', MAVI, MAVI_A),
        ('2. Üs & Parantez', '3² ve (3 + 5)', YES, YES_A),
        ('3. Çarpma', '2 · 8 = 16', TUR, TUR_A),
        ('4. Topla / Çıkar', '16 + 9 − 6', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += yazi(x + 41, 54, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Cebirsel ifadede işlem önceliğine göre değer bulma adımları.', 15)


def dort_terim_benzerlik_kartlari():
    kartlar = [
        ('I. Kart', '6a²  (Değişken: a, Üs: 2)', MAVI, MAVI_A),
        ('II. Kart', '6a   (Değişken: a, Üs: 1)', YES, YES_A),
        ('III. Kart', '6b   (Değişken: b, Üs: 1)', TUR, TUR_A),
        ('IV. Kart', '−9a  (Değişken: a, Üs: 1)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Benzer terimleri belirlemek için verilen dört terim kartı.', 16)


def kirtasiye_para_ustu_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 21, 'Alışveriş ve İndirim', 10.1, MAVI)
    ic += yazi(91, 43, '4 kalem × p TL = 4p TL', 9.5, LAC)
    ic += yazi(91, 63, 'İndirim kuponu: −15 TL', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 21, 'Ödeme ve Para Üstü', 10.1, YESIL_K)
    ic += yazi(269, 43, 'Verilen Para: 100 TL', 9.5, LAC)
    ic += yazi(269, 63, 'p = 18 TL için Para Üstü = ?', 9.3, YESIL_K)
    return svg(360, 88, ic, 'Kırtasiye alışverişinde cebirsel ifade ve para üstü hesaplama kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cebirsel_serit_modeli()
    s[2]['gorsel'] = terim_katsayi_panosu()
    s[5]['gorsel'] = kumbara_depo_durumlari()
    s[6]['gorsel'] = uslu_deger_bulma_karti()
    s[7]['gorsel'] = dikdortgen_bahce_cevresi()
    s[8]['gorsel'] = deger_bulma_siralama_adimlari()
    s[9]['gorsel'] = dort_terim_benzerlik_kartlari()
    s[11]['gorsel'] = kirtasiye_para_ustu_karti()
