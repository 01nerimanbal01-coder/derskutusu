"""10. sınıf Din Kültürü ve Ahlak Bilgisi 2. hafta (İslam’da Bilgi Kaynakları ve Türleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_bilgi_kaynaklari():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kaynaklar = [
        ('Selim Akıl', 'Doğru muhakeme', MAVI, MAVI_A),
        ('Salim Duyular', 'Dış dünya algısı', YES, YES_A),
        ('Sadık Haber', 'Vahiy ve mütevatir', TUR, TUR_A),
        ('Öznel Kaynak', 'Rüya ve ilham', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kaynaklar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'İslamda bilgi kaynakları kartları', 34)


def g1_mutevatir():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += kutu(14, 12, 140, 76, '#fef6ec', TUR, 6, 1.2)
    ic += yazi(84, 30, 'MÜTEVATİR HABER', 10, TUR)
    ic += yazi(84, 48, 'Yalan üzerine', 9.5, LAC, ince=True)
    ic += yazi(84, 62, 'birleşmesi aklen', 9.5, LAC, ince=True)
    ic += yazi(84, 76, 'imkânsız topluluk', 9.5, LAC, ince=True)

    ic += kutu(168, 12, 178, 76, '#fffaf4', TUR, 6, 1.2)
    ic += yazi(257, 30, 'Kesin Bilgi (Yakîn)', 10.5, TUR)
    ic += yazi(257, 48, '• Kuran-ı Kerim metni', 9.5, LAC, ince=True)
    ic += yazi(257, 62, '• Mütevatir sünnet uygulamaları', 9, LAC, ince=True)
    ic += yazi(257, 76, '• Herkes için bağlayıcıdır', 9, YES)
    return svg(360, 100, ic, 'Mütevatir haber ve kesin bilgi kavramı', 34)


def g2_akil_sorumluluk():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    # Terazi simgesi
    ic += f'<line x1="84" y1="24" x2="84" y2="68" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="54" y1="36" x2="114" y2="36" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<circle cx="54" cy="48" r="10" fill="none" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += f'<circle cx="114" cy="48" r="10" fill="none" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += yazi(84, 80, 'Selim Akıl', 9.5, LAC)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 30, 'DİNÎ MÜKELLEFİYET', 10.5, MAVI)
    ic += yazi(257, 48, 'Akıl ve irade sahibi olmak,', 9, LAC, ince=True)
    ic += yazi(257, 62, 'ilahi emir ve yasaklardan', 9, LAC, ince=True)
    ic += yazi(257, 76, 'sorumlu olmanın şartıdır.', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Akıl ve dinî sorumluluk dengesi şeması', 34)


def g3_bilgi_turleri():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    turler = [
        ('Gündelik', 'Tecrübe / duyu', '#f4fbf6'),
        ('Dinî', 'Vahiy / inanç', '#eaf8f0'),
        ('Bilimsel', 'Deney / yöntem', '#ddf5e6'),
        ('Felsefi', 'Eleştirel akıl', '#d0f2dc')
    ]
    for i, (b, n, bg) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, n, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Dört temel bilgi türü karşılaştırması', 34)


def g5_muaz_akisi():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    adımlar = [
        ('1. Kuran', 'Kitaptaki açık ayet'),
        ('2. Sünnet', 'Peygamber tatbikatı'),
        ('3. İctihad', 'Akıl ve muhakeme'),
        ('4. Hüküm', 'Adil uygulama')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#fef6ec', TUR, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, TUR)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{TUR}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Muaz bin Cebel bilgi ve hüküm çıkarma sırası', 34)


def g6_selim_akil():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(84, 30, 'SELİM AKIL', 11, MAVI)
    ic += yazi(84, 48, 'Fıtratını korumuş,', 9.5, LAC, ince=True)
    ic += yazi(84, 62, 'kötü arzulardan', 9.5, LAC, ince=True)
    ic += yazi(84, 76, 'arınmış berrak akıl', 9.5, LAC, ince=True)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 30, 'Bağlayıcı Bilgi', 10.5, MAVI)
    ic += yazi(257, 48, '• Vahyin muhatabı akıldır', 9.5, LAC, ince=True)
    ic += yazi(257, 64, '• İyiyi kötüden ayırt eder', 9.5, LAC, ince=True)
    ic += yazi(257, 78, '• Evrendeki ayetleri anlar', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Selim akıl ve fıtri düşünme yetisi', 34)


def g8_bilgi_ornekleri():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    kartlar = [
        ('Teknik', 'Değirmen / Alet', MAVI),
        ('Sanat', 'Hat / Estetik', YES),
        ('Bilim', 'Deney / Ölçüm', TUR),
        ('Gündelik', 'Tecrübe / Sezgi', MOR)
    ]
    for i, (t, o, col) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f2fbfd', col, 6, 1.2)
        ic += yazi(x + 40, 32, t, 11, col)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{col}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, o, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Bilgi türleri somut uygulama örnekleri', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: H - A - B - E - R', 11.5, YES)
    harfler = [('1', 'H'), ('2', 'A'), ('3', 'B'), ('4', 'E'), ('5', 'R')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Haber şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_bilgi_kaynaklari()
    s[1]['gorsel'] = g1_mutevatir()
    s[2]['gorsel'] = g2_akil_sorumluluk()
    s[3]['gorsel'] = g3_bilgi_turleri()
    s[5]['gorsel'] = g5_muaz_akisi()
    s[6]['gorsel'] = g6_selim_akil()
    s[8]['gorsel'] = g8_bilgi_ornekleri()
    s[10]['gorsel'] = g10_sifre_seridi()
