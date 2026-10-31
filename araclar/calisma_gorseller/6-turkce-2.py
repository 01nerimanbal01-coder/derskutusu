"""6. sınıf Türkçe 2. hafta (Bir Kelime Seyyahı: Metnin Konusu, Boy Damgaları ve Paragraf Yazma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=23):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def duz(x, y, satirlar, boy=11, renk=LAC, hiza='start', ara=14):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def harf_kutu(x, y, h, renk=LAC):
    return f'<rect x="{x - 10}" y="{y - 10}" width="20" height="20" rx="5" fill="{renk}"/>' + yazi(x, y + 4.5, h, 11.5, '#fff')


def konu_ayrinti_semasi():
    """Soru 1: Bir Kelime Seyyahı metninin konusu (K) ve ayrıntıları (L) şeması."""
    ic = kutu(58, 4, 244, 34, MAVI_A, MAVI, 8, 1.4)
    ic += harf_kutu(78, 21, 'K', MAVI)
    ic += yazi(190, 18, 'METNİN KONUSU', 10.5, MAVI)
    ic += yazi(190, 32, '(Baştan sona en çok anlatılan: ?)', 10.5, LAC, 'middle', True)
    kollar = [
        (4, 'Tepük oyunu', 've adının anlamı', TUR, TUR_A, None),
        (124, 'Dedesiyle', 'sevgi bağı', YES, YES_A, None),
        (244, 'Ayrıntı: ?', '(Kişi ve kurumlar)', MOR, MOR_A, 'L'),
    ]
    for x, s1, s2, r, z, harf in kollar:
        cx = x + 56
        ic += f'<line x1="180" y1="38" x2="{cx}" y2="54" stroke="{SOLUK}" stroke-width="1.5"/>'
        ic += kutu(x, 54, 112, 42, z, r, 7, 1.3)
        if harf:
            ic += harf_kutu(x + 18, 75, harf, r)
            ic += yazi(x + 68, 71, s1, 11, r)
            ic += yazi(x + 68, 86, s2, 10.5, LAC, 'middle', True)
        else:
            ic += yazi(cx, 71, s1, 11, LAC)
            ic += yazi(cx, 86, s2, 10.5, SOLUK, 'middle', True)
    return svg(360, 100, ic, 'Konu ve ayrıntı şeması: üstte K kutusu Metnin Konusu, altta üç ayrıntı kutusu Tepük oyunu ve adı, Dedesiyle sevgi bağı ve L ayrıntı kutusu.', 19)


def aile_egitim_kartlari():
    """Soru 2: Karahanlı ailesi ve Kaşgar medreseleri bilgi kartları (insan figürü yok, sancak ve kubbe simgeli)."""
    ic = kutu(4, 4, 172, 88, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Karahanlı Ailesi', 11.5, MAVI)
    ic += duz(12, 37, [
        'Dede: Muhammet Buğra Han',
        'Anne: Rabia Hanım',
        '  (Âlim Seyfettin Bezügvar kızı)',
        'Baba: Hüseyin Çağrı Bey',
    ], 10.5, LAC, 'start', 13.5)

    ic += kutu(184, 4, 172, 88, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Kaşgar’da Eğitim ve İlim', 11.5, TUR)
    ic += duz(192, 37, [
        'Hamidiye ve Saciye Medreseleri',
        'Hoca: Şeyh İmam ez-Zahid',
        '  Hüseyin (takdirini kazanır)',
        'At, ok ve kargı talimi',
    ], 10.5, LAC, 'start', 13.5)
    return svg(360, 96, ic, 'Solda Karahanlı Ailesi kartı: Muhammet Buğra Han, Rabia Hanım, Hüseyin Çağrı Bey. Sağda Kaşgar Eğitim kartı: Hamidiye ve Saciye Medreseleri, Şeyh İmam ez-Zahid Hüseyin.', 19)


def bes_damga_seridi():
    """Soru 3: Kayı, İğdir, Çavuldur, Ala Yuntlu ve Dodurga boylarının damga şekilleri."""
    damgalar = [
        ('Kayı', MAVI, MAVI_A, '<path d="M18 14V44M23 14L34 44L45 14M50 14V44"/>'),
        ('İğdir', YES, YES_A, '<path d="M48 12L20 28H48L21 45"/>'),
        ('Çavuldur', TUR, TUR_A, '<path d="M10 42L27 24Q34 18 41 24L58 42M19 42L30 31Q34 27 38 31L49 42"/>'),
        ('Ala Yuntlu', MOR, MOR_A, '<path d="M24 14V28M12 28H56M12 35H56M12 42H56"/>'),
        ('Dodurga', CAM, CAM_A, '<path d="M12 16L24 42L36 16M32 42L44 16L56 42"/>'),
    ]
    ic = ''
    for i, (ad, r, z, cizim) in enumerate(damgalar):
        x = 4 + i * 71
        ic += kutu(x, 4, 67, 78, z, r, 7, 1.3)
        ic += f'<g transform="translate({x}, 2)" fill="none" stroke="{r}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">{cizim}</g>'
        ic += yazi(x + 33.5, 70, ad, 11, LAC)
    return svg(359, 86, ic, 'Beş Türk boyu damgası: Kayı, İğdir, Çavuldur, Ala Yuntlu ve Dodurga.', 18)


def dort_damga_karti():
    """Soru 4: Bayat, Eymür, Karaeyli (hatalı açıklama) ve Bayundur damga inceleme kartları."""
    kartlar = [
        ('I · Bayat', 'Damgada bir üçgen vardır.', TUR, TUR_A, '<path d="M14 10V36M21 10V36M21 22L28 10M38 21V36M32 21H44L38 9Z"/>'),
        ('II · Eymür', 'Damgada bir dörtgen vardır.', YES, YES_A, '<path d="M28 8L37 17L28 26L19 17ZM28 26V40M12 29H44"/>'),
        ('III · Karaeyli', 'Üç paralel çizgiden oluşur.', KIR, KIR_A, '<path d="M8 26H22V34H8ZM25 34Q35 16 48 34M31 34Q37 25 43 34"/>'),
        ('IV · Bayundur', 'Küçük ünlü harfi andırır.', MAVI, MAVI_A, '<path d="M14 12H42V23H14M14 12V34H42V40"/>'),
    ]
    ic = ''
    for i, (bas, acik, r, z, cizim) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += f'<g transform="translate({x + 2}, {y})" fill="none" stroke="{r}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{cizim}</g>'
        ic += yazi(x + 54, y + 17, bas, 11, r, 'start')
        ic += yazi(x + 54, y + 33, acik, 10.5, LAC, 'start', True)
    return svg(360, 96, ic, 'Dört damga inceleme kartı: I Bayat üçgen vardır, II Eymür dörtgen vardır, III Karaeyli üç paralel çizgiden oluşur, IV Bayundur küçük ünlü harfi andırır.', 19)


def deyim_sahne_karti():
    """Soru 5: Göz göze gelmek deyimi ve şifreli konuşma bilgi kartı (insan figürü yok, sandık ve mesaj sembolü)."""
    ic = kutu(4, 4, 352, 82, KUM, KAHVE, 8, 1.3)
    ic += kutu(12, 12, 156, 66, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(90, 29, 'Deyim: “göz göze gelmek”', 11, MAVI)
    ic += duz(90, 47, ['Dede: Göz işaretiyle sorar', 'Torun: Göz kırparak yanıtlar'], 10.5, LAC, 'middle', 15)
    ic += f'<line x1="174" y1="45" x2="196" y2="45" stroke="{KAHVE}" stroke-width="1.8"/>'
    ic += kutu(202, 12, 146, 66, TUR_A, TUR, 7, 1.3)
    ic += yazi(275, 29, 'Hazine Sandığına Yolculuk', 11, TUR)
    ic += duz(275, 47, ['“koşa koşa” eve gelir,', 'gözleri “ışıl ışıl” parlar.'], 10.5, LAC, 'middle', 15)
    return svg(360, 90, ic, 'Göz göze gelmek deyimi ve hazine sandığına yolculuk ikilemeler kartı.', 18)


def izleme_ekran_karti():
    """Soru 7: Ortak Sözcüklerimiz, Ortak Dilimiz karekodlu izleme içeriği ön inceleme kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="24" rx="8" fill="{MAVI}"/><rect x="4" y="18" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 20, 'KAREKOD İÇERİĞİ · Ortak Sözcüklerimiz, Ortak Dilimiz', 11, '#fff')
    ic += kutu(14, 36, 158, 46, '#fff', TUR, 6, 1.3)
    ic += yazi(93, 54, '1. Görsel Etiketi', 10.5, TUR)
    ic += yazi(93, 72, '“Kazakistan Türkçesi”', 11.5, LAC)
    ic += kutu(188, 36, 158, 46, '#fff', YES, 6, 1.3)
    ic += yazi(267, 54, '2. Görsel Etiketi', 10.5, YES)
    ic += yazi(267, 72, '“Kırgızistan Türkçesi”', 11.5, LAC)
    return svg(360, 94, ic, 'Karekod içeriği başlığı Ortak Sözcüklerimiz Ortak Dilimiz; ekran görsellerinde Kazakistan Türkçesi ve Kırgızistan Türkçesi yazıları.', 18)


def paragraf_plan_semasi():
    """Soru 9: Paragraf yazma öncesi 3 seçim ve başlatma/sürdürme/sonlandırma şeması."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.2)
    secimler = [
        ('1. Konu', 'Kelime madeni', MAVI, MAVI_A, 10),
        ('2. Hedef Kitle', 'Okul öncesi çocuklar', TUR, TUR_A, 126),
        ('3. Yazma Ortamı', 'Çizgili defter', YES, YES_A, 242),
    ]
    for bas, deger, r, z, x in secimler:
        ic += kutu(x, 10, 108, 36, z, r, 6, 1.2)
        ic += yazi(x + 54, 24, bas, 10.5, r)
        ic += yazi(x + 54, 39, deger, 10.5, LAC, 'middle', True)
    ic += kutu(10, 52, 340, 38, MOR_A, MOR, 6, 1.2)
    ic += yazi(180, 67, 'Paragraf Yapısı: Başlatma (hazırlar) → Sürdürme (bağlar) → Sonlandırma (toparlar)', 10.5, LAC)
    ic += yazi(180, 82, 'Üç bölüm de seçilen konuya ve hedef kitleye uygun kurulur.', 10.5, MOR, 'middle', True)
    return svg(360, 100, ic, 'Paragraf yazma planı: 1. Konu Kelime madeni, 2. Hedef Kitle Okul öncesi çocuklar, 3. Yazma Ortamı Çizgili defter; altta Başlatma, Sürdürme ve Sonlandırma akışı.', 19)


def dogrusunu_bilelim_karti():
    """Soru 10: Metindeki özgün yazım ile günümüz yazım kuralları karşılaştırma kartı."""
    ic = kutu(4, 4, 352, 80, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 20, 'DOĞRUSUNU BİLELİM · Yazım Karşılaştırması', 11.5, TUR)
    kartlar = [
        ('Metinde: İslâmiyet', 'Günümüzde: İslamiyet', MAVI, 12),
        ('Metinde: âdet', 'Günümüzde: âdet (görenek)', YES, 184),
    ]
    for s1, s2, r, x in kartlar:
        ic += kutu(x, 28, 164, 48, '#fff', r, 6, 1.2)
        ic += yazi(x + 82, 46, s1, 11, SOLUK, 'middle', True)
        ic += yazi(x + 82, 66, s2, 11.5, r)
    return svg(360, 88, ic, 'Doğrusunu bilelim yazım kartı: İslâmiyet kelimesi günümüzde düzeltme işareti olmadan İslamiyet; âdet görenek kelimesi düzeltme işaretiyle âdet yazılır.', 18)


def cumle_oyunu_karti():
    """Soru 13: K harfiyle hazırlanan Kelimelerle Cümle Kurma Oyunu kâğıdı."""
    ic = kutu(4, 4, 352, 84, YES_A, YES, 8, 1.3)
    ic += yazi(180, 20, 'KELİMELERLE CÜMLE KURMA OYUNU · “K” Harfi Listesi', 11, YES)
    etiketler = [
        ('İsimler:', 'kardeş, kitap, kütüphane', MAVI, 12, 28),
        ('Sıfat / Fiil:', 'kırmızı, kaybetmek', TUR, 186, 28),
        ('Deyim:', 'kara kara düşünmek', MOR, 12, 56),
        ('İkileme:', 'koşa koşa', KIR, 186, 56),
    ]
    for bas, m, r, x, y in etiketler:
        ic += kutu(x, y, 162, 24, '#fff', r, 5, 1.1)
        ic += yazi(x + 8, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 74, y + 16, m, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Kelimelerle cümle kurma oyunu K harfi listesi: kardeş, kitap, kütüphane, kırmızı, kaybetmek, kara kara düşünmek, koşa koşa.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = konu_ayrinti_semasi()
    s[1]['gorsel'] = aile_egitim_kartlari()
    s[2]['gorsel'] = bes_damga_seridi()
    s[3]['gorsel'] = dort_damga_karti()
    s[4]['gorsel'] = deyim_sahne_karti()
    s[6]['gorsel'] = izleme_ekran_karti()
    s[8]['gorsel'] = paragraf_plan_semasi()
    s[9]['gorsel'] = dogrusunu_bilelim_karti()
    s[12]['gorsel'] = cumle_oyunu_karti()
