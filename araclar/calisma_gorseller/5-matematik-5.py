"""5. sınıf Matematik 5. hafta (Çokgenler ve Çember: Ardışık Kesişen Doğrulardan Çokgenlere) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dogru_kesisim_kartlari():
    kartlar = [
        ('1. Kart · Ardışık 3 Doğru', 'd1-d2-d3 kapalı üçgen kurar', YES, YES_A),
        ('2. Kart · Yalnız 2 Doğru', 'Tek kesişim, açık bölge', MAVI, MAVI_A),
        ('3. Kart · İkisi Paralel', 'd1 // d3, zincir kapanmaz', TUR, TUR_A),
        ('4. Kart · Ortak Noktalı', '3 doğru tek noktadan geçer', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Ardışık kesişen ve kesişmeyen doğru takımlarını gösteren dört kart.', 20)


def cokgen_secim_sekilleri():
    kartlar = [
        ('1. Şekil: Üçgen Levha', '3 doğru parçası · Kapalı', MAVI, MAVI_A),
        ('2. Şekil: Yarım Daire (!)', 'Bir sınırı eğri çizgi', KIR, KIR_A),
        ('3. Şekil: Dörtgen Çerçeve', '4 doğru parçası · Kapalı', YES, YES_A),
        ('4. Şekil: Altıgen Petek', '6 doğru parçası · Kapalı', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Üçgen, yarım daire, dörtgen ve altıgen şekil kartları.', 20)


def cokgen_dogru_sayisi_kartlari():
    kartlar = [
        ('1. ABC Üçgeni', '3 doğru · 3 köşe · 3 açı', MAVI, MAVI_A),
        ('2. KLMN Dörtgeni', '4 doğru · 4 köşe · 4 açı', YES, YES_A),
        ('3. PRSTU Beşgeni', '5 doğru · 5 köşe · 5 açı', TUR, TUR_A),
        ('4. DEFGHİ Altıgeni', '6 doğru · 6 köşe · 6 açı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Üçgen, dörtgen, beşgen ve altıgenin doğru, köşe ve açı sayısı kartları.', 20)


def noktadas_uc_dogru_sema():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += f'<line x1="40" y1="50" x2="220" y2="50" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="60" y1="18" x2="200" y2="82" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<line x1="60" y1="82" x2="200" y2="18" stroke="{MOR}" stroke-width="2"/>'
    ic += f'<circle cx="130" cy="50" r="5" fill="{KIR}"/>'
    ic += yazi(130, 32, 'O (Tek Kesişim)', KIR, kalin=True)
    ic += yazi(232, 54, 'd1', MAVI, kalin=True)
    ic += yazi(212, 86, 'd2', TUR, kalin=True)
    ic += yazi(212, 22, 'd3', MOR, kalin=True)

    ic += kutu(265, 16, 315, 68, KIR_A, KIR, 8, 1.4)
    ic += yazi(422, 36, 'Kerem’in Çizimi: Aynı Noktadan Geçen 3 Doğru', KIR, kalin=True)
    ic += yazi(422, 56, '• d1, d2 ve d3 yalnız O noktasında kesişiyor.', LAC)
    ic += yazi(422, 75, '• Üçgen için 3 ayrı kesişim noktası (köşe) gerekir.', LAC, kalin=True)
    return svg(600, 100, ic, 'Aynı O noktasından geçen üç doğrunun kapalı bölge oluşturmadığını gösteren şema.', 20)


def gunluk_cokgen_nesneleri():
    kartlar = [
        ('Yol Ver Levhası', 'Üçgen · 3 kenar', MAVI, MAVI_A),
        ('Defter Sayfası', 'Dörtgen · 4 kenar', YES, YES_A),
        ('Topun Siyah Dilimi', 'Beşgen · 5 kenar', TUR, TUR_A),
        ('Dur Levhası', 'Sekizgen · 8 kenar', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Yol ver levhası, defter sayfası, futbol topu dilimi ve dur levhası çokgen modelleri.', 20)


def prstu_besgeni_sema():
    ic = kutu(6, 6, 588, 90, KUM, GRI, 9, 1.4)
    ic += f'<polygon points="135,16 205,42 180,82 90,82 65,42" fill="{TUR_A}" stroke="{TUR}" stroke-width="2.2"/>'
    ic += yazi(135, 13, 'P', TUR, kalin=True)
    ic += yazi(220, 44, 'R', LAC, kalin=True)
    ic += yazi(196, 88, 'S', LAC, kalin=True)
    ic += yazi(74, 88, 'T', LAC, kalin=True)
    ic += yazi(50, 44, 'U', LAC, kalin=True)

    ic += kutu(260, 16, 320, 70, TUR_A, TUR, 8, 1.4)
    ic += yazi(420, 35, 'PRSTU Beşgeni Elemanları', TUR, kalin=True)
    ic += yazi(420, 56, 'Köşeler: P, R, S, T, U (Ardışık sırada)', LAC, kalin=True)
    ic += yazi(420, 76, 'Kenarlar: [PR], [RS], [ST], [TU], [UP]', LAC)
    return svg(600, 102, ic, 'Köşeleri P, R, S, T, U olan beşgenin kenar ve açı şeması.', 20)


def paralel_ciftli_dortgen_karti():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += f'<polygon points="75,24 215,24 190,78 50,78" fill="{YES_A}" stroke="{YES}" stroke-width="2.2"/>'
    ic += yazi(62, 20, 'K', YESIL_K, kalin=True)
    ic += yazi(228, 20, 'L', YESIL_K, kalin=True)
    ic += yazi(204, 84, 'M', YESIL_K, kalin=True)
    ic += yazi(36, 84, 'N', YESIL_K, kalin=True)
    ic += yazi(145, 19, 'd1', MAVI, kalin=True)
    ic += yazi(130, 88, 'd3', MAVI, kalin=True)
    ic += yazi(216, 55, 'd2', TUR, kalin=True)
    ic += yazi(50, 55, 'd4', TUR, kalin=True)

    ic += kutu(260, 16, 320, 68, YES_A, YES, 8, 1.4)
    ic += yazi(420, 35, 'Karşılıklı Paralel Doğrulardan Dörtgen', YESIL_K, kalin=True)
    ic += yazi(420, 56, '• d1 // d3 ve d2 // d4 (Karşılıklı çiftler paralel)', LAC)
    ic += yazi(420, 75, '• Ardışık d1-d2, d2-d3, d3-d4, d4-d1 kesişir', LAC, kalin=True)
    return svg(600, 100, ic, 'Karşılıklı paralel d1-d3 ve d2-d4 doğrularının ardışık kesişerek oluşturduğu KLMN dörtgeni.', 20)


def cokgen_kurallari_panosu():
    kartlar = [
        ('Sayı Eşitliği Kuralı', 'Kenar = Köşe = Açı = Doğru sayısı', MAVI, MAVI_A),
        ('Adlandırma Kuralı', 'Kenar sayısına göre (-gen ekiyle)', YES, YES_A),
        ('Biçim Bağımsızlığı', 'Farklı kenar boyları adı değiştirmez', TUR, TUR_A),
        ('Kapanma Şartı', 'Son doğru ilk doğruyu kesmelidir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Çokgenlerin temel kurallarını özetleyen dörtlü bilgi panosu.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dogru_kesisim_kartlari()
    s[4]['gorsel'] = cokgen_secim_sekilleri()
    s[5]['gorsel'] = cokgen_dogru_sayisi_kartlari()
    s[6]['gorsel'] = noktadas_uc_dogru_sema()
    s[7]['gorsel'] = gunluk_cokgen_nesneleri()
    s[8]['gorsel'] = prstu_besgeni_sema()
    s[10]['gorsel'] = paralel_ciftli_dortgen_karti()
    s[11]['gorsel'] = cokgen_kurallari_panosu()
