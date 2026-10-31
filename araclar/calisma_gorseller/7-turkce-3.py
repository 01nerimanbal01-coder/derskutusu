"""7. sınıf Türkçe 3. hafta (Gençliğin Kıymeti: Tahmin Etme, Düşünceyi Geliştirme Yolları, İkilemeler ve Üç Nokta) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–13 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def benzetme_semasi_svg():
    """Gençliğin Kıymeti yazısındaki dört benzetme eşleştirmesi."""
    kartlar = [
        ('İlkbahar ve Çiçek', '→ Gençlik (hazırlık çağı)', YES, YES_A),
        ('Olgun Şeftali', '→ Olgun yaşta verilen ürün', TUR, TUR_A),
        ('Akan Nehir Suyu', '→ Geri dönmeyen zaman', MAVI, MAVI_A),
        ('İyi Bahçıvan', '→ Gençlere destek yetişkin', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, alt, 10, LAC, 'start', True)
    return svg(360, 88, ic, 'Gençliğin Kıymeti benzetme şeması: İlkbahar ve çiçek gençlik hazırlık çağı, Olgun şeftali olgun yaşta verilen ürün, Akan nehir suyu geri dönmeyen zaman, İyi bahçıvan gençlere destek yetişkin.', 18)


def ikileme_ve_uc_nokta_panosu_svg():
    """İkilemelerin yazımı ve üç noktanın kullanımı özet panosu."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="20" rx="8" fill="{YES}"/><rect x="4" y="16" width="172" height="8" fill="{YES}"/>'
    ic += yazi(90, 18, 'İkilemelerin Yazımı', 11, '#fff')
    ic += yazi(14, 39, 'Ayrı yazılır, bitişmez.', 10.5, LAC, 'start', True)
    ic += yazi(14, 55, 'Araya işaret konmaz.', 10.5, LAC, 'start', True)
    ic += yazi(14, 71, 'Örnek: günden güne', 10.5, YES, 'start')

    ic += kutu(184, 4, 172, 82, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="20" rx="8" fill="{MAVI}"/><rect x="184" y="16" width="172" height="8" fill="{MAVI}"/>'
    ic += yazi(270, 18, 'Üç Nokta (…) Kuralları', 11, '#fff')
    ic += yazi(194, 39, 'Eksik cevaplarda (Şey…)', 10.5, LAC, 'start', True)
    ic += yazi(194, 55, 'Okura bırakılan sonlarda', 10.5, LAC, 'start', True)
    ic += yazi(194, 71, '! ve ? sonrası iki nokta (!..)', 10.2, MAVI, 'start')
    return svg(360, 90, ic, 'İkilemelerin yazımı ve üç nokta kuralları bilgi panosu.', 18)


def dusunce_yollari_kartlari_svg():
    """Dört düşünceyi geliştirme yolu cümle kartı."""
    kartlar = [
        ('I. Kart', 'Ömrümüz dört mevsim gibi ilerler.', MAVI, MAVI_A),
        ('II. Kart', 'Gençlikte bol vakit yaşla daralır.', TUR, TUR_A),
        ('III. Kart', 'Heraklit: Nehirde iki kez yıkanılmaz.', YES, YES_A),
        ('IV. Kart', 'Örneğin meyveli ağaç da güzeldir.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, m, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, m, 9.5, LAC, 'start', True)
    return svg(360, 88, ic, 'Dört cümle kartı: I. kart benzetme, II. kart karşılaştırma, III. kart Heraklit sözü tanık gösterme, IV. kart örneklendirme.', 18)


def uc_nokta_ornekleri_svg():
    """Tablo sorusu için dört üç nokta ve iki nokta örnek kartı."""
    kartlar = [
        ('1. Kart', '— Kitabı bitirdin mi? — Şey…', MAVI, MAVI_A),
        ('2. Kart', 'Ah… Gençliğin kıymetini bilmeli!', YES, YES_A),
        ('3. Kart', 'Sis dağıldı ve yemyeşil bir vadi…', MOR, MOR_A),
        ('4. Kart', 'Dikkat et!.. Vaktini boşa harcama.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, m, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, m, 9.6, LAC, 'start', True)
    return svg(360, 88, ic, 'Dört noktalama kartı: 1. kart eksik cevap, 2. kart ünlemde pekiştirme, 3. kart okura bırakılan cümle, 4. kart ünlem sonrası iki nokta.', 18)


def baglam_tahmin_karti_svg():
    """İhtimam sözcüğü bağlamdan anlam tahmin kartı."""
    ic = kutu(4, 4, 352, 76, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{CAM}"/><rect x="4" y="16" width="352" height="8" fill="{CAM}"/>'
    ic += yazi(180, 18, 'BAĞLAMDAN ANLAM TAHMİN KARTI · “ihtimam”', 11, '#fff')
    ic += yazi(16, 40, '“Bahçıvan fidanı her gün suladı, dalları kırılmasın diye', 10.5, LAC, 'start', True)
    ic += yazi(16, 55, 'destek çubuğu bağladı; bu ihtimam sayesinde fidan büyüdü.”', 10.5, LAC, 'start', True)
    ic += yazi(16, 71, 'İpucu: sulamak ve destek bağlamak → Tahmin ve Kontrol: ?', 10, CAM, 'start')
    return svg(360, 84, ic, 'Bağlamdan anlam tahmin kartı: ihtimam sözcüğü ve cümledeki ipuçları.', 18)


def ikileme_yazim_fisleri_svg():
    """Dört ikileme yazım fişi (IV. fişte günden-güne kısa çizgi hatası)."""
    fisler = [
        ('I. Fiş', 'enine boyuna tartıştılar', MAVI, MAVI_A),
        ('II. Fiş', 'arada sırada görüşüyoruz', YES, YES_A),
        ('III. Fiş', 'omuz omuza çalıştılar', TUR, TUR_A),
        ('IV. Fiş', 'günden-güne artıyor', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, m, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 14, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 28, m, 10.5, LAC, 'start', True)
    return svg(360, 88, ic, 'Dört ikileme yazım fişi: I enine boyuna, II arada sırada, III omuz omuza, IV günden-güne.', 18)


def oz_degerlendirme_formu_svg():
    """Elif'in okuma becerisi öz değerlendirme formu."""
    ic = kutu(4, 4, 352, 98, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="8" fill="{LAC}"/>'
    ic += yazi(180, 18, 'OKUMA BECERİSİ ÖZ DEĞERLENDİRME FORMU · Elif', 10.5, '#fff')
    maddeler = [
        ('1. Bilmediğim sözcükleri belirledim.', 'Evet', YES),
        ('2. Tahminimi sözlükle kontrol ettim.', 'Kısmen', TUR),
        ('3. Metinle ilgili soruları yanıtladım.', 'Evet', YES),
        ('4. Düşünceyi geliştirme yollarını buldum.', 'Hayır', KIR),
    ]
    for i, (m, yanit, r) in enumerate(maddeler):
        y = 28 + i * 17
        ic += f'<rect x="10" y="{y}" width="340" height="15" rx="3" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(16, y + 11.5, m, 10, LAC, 'start', True)
        ic += yazi(318, y + 11.5, yanit, 10.5, r)
    return svg(360, 106, ic, 'Elif okuma öz değerlendirme formu: 1 Evet, 2 Kısmen, 3 Evet, 4 Hayır.', 19)


def belgesel_kareleri_svg():
    """Kısa film ardışık üç kare ve anlatıcı sözü."""
    kareler = [
        ('1. Kare', 'Takvim yaprağı ilerler', MAVI, MAVI_A),
        ('2. Kare', 'Planlı ve düzenli çalışma', TUR, TUR_A),
        ('3. Kare', 'Bilim ödülü ve yeni buluş', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kareler):
        x = 4 + i * 119
        ic += kutu(x, 4, 114, 54, z, r, 7, 1.3)
        ic += yazi(x + 57, 21, bas, 10.5, r)
        ic += yazi(x + 57, 41, alt, 9.3, LAC, ince=True)
    ic += kutu(4, 62, 352, 22, MOR_A, MOR, 6, 1.2)
    ic += yazi(180, 77, 'Anlatıcı: “Gençlikte ekilen emek, gelecekte ürüne dönüşür.”', 10.2, MOR)
    return svg(360, 88, ic, 'Üç film karesi: 1 Takvim yaprağı ilerler, 2 Planlı ve düzenli çalışma, 3 Bilim ödülü ve yeni buluş.', 18)


def seftali_agaci_karti_svg():
    """Çiçekli şeftali ağacı (İlkbahar) ve meyveli şeftali ağacı (Olgunluk) kartları."""
    ic = kutu(6, 6, 170, 74, YES_A, YES, 8, 1.4)
    ic += yazi(91, 22, 'İlkbaharda Şeftali Ağacı', 11, YES)
    ic += yazi(91, 42, 'Pembe çiçeklerle donanır.', 10, LAC, ince=True)
    ic += yazi(91, 58, 'Meyve için hazırlık yapar.', 10, LAC, ince=True)

    ic += kutu(184, 6, 170, 74, TUR_A, TUR, 8, 1.4)
    ic += yazi(269, 22, 'Meyve Zamanı Şeftali Ağacı', 11, TUR)
    ic += yazi(269, 42, 'Dalları olgun meyve taşır.', 10, LAC, ince=True)
    ic += yazi(269, 58, 'Bahardaki özenin eseridir.', 10, LAC, ince=True)
    return svg(360, 86, ic, 'İki kart: İlkbaharda pembe çiçekli şeftali ağacı ve meyve zamanında olgun meyveli şeftali ağacı.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = benzetme_semasi_svg()
    s[2]['gorsel'] = ikileme_ve_uc_nokta_panosu_svg()
    s[4]['gorsel'] = dusunce_yollari_kartlari_svg()
    s[5]['gorsel'] = uc_nokta_ornekleri_svg()
    s[6]['gorsel'] = baglam_tahmin_karti_svg()
    s[8]['gorsel'] = ikileme_yazim_fisleri_svg()
    s[9]['gorsel'] = oz_degerlendirme_formu_svg()
    s[10]['gorsel'] = belgesel_kareleri_svg()
    s[12]['gorsel'] = seftali_agaci_karti_svg()
