"""10. sınıf Cografya 4. hafta (Mekânsal Bilgi Teknolojilerinin Bileşenleri (CBS, Uzaktan Algılama, GPS) ve Afet Yönetiminde AYDES Uygulaması) çalışma kâğıdı görselleri.
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

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [('CBS', 'Mekânsal analiz ve katmanlama', '#2451d6', '#e8eefe'), ('Uzaktan Algılama', 'Uydu ve radar sensörleri', '#12a150', '#e3f6ea'), ('GPS / GNSS', 'Küresel koordinat konumu', '#ee7d12', '#fff1df'), ('AYDES', 'Afet Yönetim Karar Destek', '#7c3aed', '#f0e9fe')]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 temel kurallar ve kavramlar kartı', 34)
def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'AFAD VE AYDES AFET MÜDAHALE SİSTEMİ', 10.5, MAVI)
    boxes = [('AYDES Acil Müdahale Koordinasyonu', 'Enkaz, kaçış yolları ve ekipler', '#2451d6'), ('CBS Tabanlı Risk Haritaları', 'Toplanma alanları ve çadır kentler', '#12a150')]
    for i, (b, d, c) in enumerate(boxes):
        x = 16 + i * 168
        ic += kutu(x, 34, 160, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 80, 52, b, 8.5, c)
        ic += yazi(x + 80, 72, d, 7, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 ana konu ve kavramsal model şeması', 34)
def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'Uydu Görüntülerinde Vektör Geometri Tipleri', 11, YES)
    ic += kutu(16, 34, 156, 54, '#ffffff', '#ee7d12', 6, 1.2)
    ic += yazi(94, 52, 'Nokta & Çizgi', 9, '#ee7d12')
    ic += yazi(94, 72, 'Yangın kulesi & Tahliye yolu', 7.5, LAC, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', '#2451d6', 6, 1.2)
    ic += yazi(266, 52, 'Poligon (Alan)', 9, '#2451d6')
    ic += yazi(266, 72, 'Hasarlı bölge & Çadır alanı', 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 model ve yasa karşılaştırma şeması', 34)
def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'Mekânsal Afet Yönetiminin Üç Evresi', 10.5, TUR)
    boxes = [('Afet Öncesi', 'Fay ve zemin risk analizi', '#2451d6'), ('Afet Anı', 'AYDES ile anlık sevk ve idare', '#d63a3a'), ('Afet Sonrası', 'Uyduyla hasar tespiti', '#12a150')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 sınıflandırma ve ayrıntı şeması', 34)
def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'SEL VE TAŞKIN KRİZİNDE AYDES KULLANIM AKIŞI', 10.5, MOR)
    steps = [('1. Radar İkaz', 'Aşırı yağış uyarısı'), ('2. CBS Modelleme', 'Taşkın sahası tespiti'), ('3. Tahliye', 'AYDES rota sevki'), ('4. İyileştirme', 'Hasar haritalama')]
    for i, (b, d) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 süreç ve akış basamakları modeli', 34)
def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'Uzaktan Algılama Sensör Türleri ve İşlevleri', 10.5, LAC)
    boxes = [('Optik Uydular', 'Yüksek çözünürlük yer tespiti', '#2451d6'), ('Radar Uydular', 'Gece ve bulutlu veri', '#7c3aed'), ('Termal Sensör', 'Yangın ve ısı odağı', '#d63a3a')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 karşılaştırma ve ilişki diyagramı', 34)
def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    cards = [('CBS', 'Konum tabanlı sistem'), ('AYDES', 'Karar destek yazılımı'), ('Raster', 'Hücre piksel verisi'), ('Vektör', 'Nokta-çizgi-alan')]
    for i, (b, d) in enumerate(cards):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-cografya-4 temel terminoloji kavram kartları', 34)
def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: A - Y - D - E - S', 11.5, YES)
    harfler = [('1', 'A'), ('2', 'Y'), ('3', 'D'), ('4', 'E'), ('5', 'S')]
    for i, (no, h) in enumerate(harfler):
        x = 48 + i * 55
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, '10-cografya-4 dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
