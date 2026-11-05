"""10. sınıf Biyoloji 2. hafta (Fotosentez Reaksiyonları ve Hızı) çalışma kâğıdı görselleri.
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

def g0_kloroplast():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    # Kloroplast dış zarı
    ic += f'<ellipse cx="100" cy="50" rx="80" ry="36" fill="#c7ebd2" stroke="{YES}" stroke-width="2"/>'
    # Granum yığınları
    for gx in (60, 100, 140):
        for gy in (38, 46, 54):
            ic += f'<rect x="{gx-16}" y="{gy}" width="32" height="5" rx="2" fill="{YES}" stroke="{LAC}" stroke-width="0.6"/>'
    ic += yazi(100, 26, 'Granum (Tilakoit)', 8.5, LAC)
    ic += yazi(100, 76, 'Stroma Sıvısı', 8.5, LAC)
    # Sağ bilgi kutusu
    ic += kutu(195, 12, 150, 76, '#eaf8f0', YES, 6, 1.1)
    ic += yazi(270, 32, 'Işığa Bağımlı Evre', 10.5, YES)
    ic += yazi(270, 48, 'Tilakoit zarda H₂O -> O₂ + ATP', 9, LAC, ince=True)
    ic += yazi(270, 64, 'Işıktan Bağımsız Evre', 10.5, TUR)
    ic += yazi(270, 78, 'Stromada CO₂ -> Besin (PGAL)', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Kloroplast yapısı ve fotosentez evreleri', 34)


def g1_calvin_dongusu():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    # Calvin döngüsü halkası
    ic += f'<circle cx="90" cy="50" r="32" fill="none" stroke="{TUR}" stroke-width="3" stroke-dasharray="6,3"/>'
    ic += yazi(90, 46, 'Calvin', 11, TUR)
    ic += yazi(90, 58, 'Döngüsü', 9.5, LAC)
    # Girdiler ve çıktılar
    ic += yazi(90, 12, 'CO₂ Girişi', 9.5, YES)
    ic += yazi(22, 50, 'ATP, NADPH', 8.5, MAVI)
    ic += yazi(90, 92, 'PGAL (Besin)', 9.5, KIR)
    # Sağ açıklama kartı
    ic += kutu(160, 12, 186, 76, '#fef6ec', TUR, 6, 1.1)
    ic += yazi(253, 30, 'IŞIKTAN BAĞIMSIZ EVRE', 10.5, TUR)
    ic += yazi(253, 48, '• Doğrudan ışık harcanmaz', 9.5, LAC, ince=True)
    ic += yazi(253, 64, '• Enzimatik reaksiyonlar (Stroma)', 9.5, LAC, ince=True)
    ic += yazi(253, 78, '• ATP ve NADPH tüketilir', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Calvin döngüsü ve ışıktan bağımsız tepkimeler', 34)


def g2_fotoliz_semasi():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 14, 150, 72, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(89, 32, 'SUYUN FOTOLİZİ', 11, MAVI)
    ic += yazi(89, 52, 'H₂O -> 2H⁺ + 2e⁻ + 1/2 O₂', 10, LAC)
    ic += yazi(89, 72, 'Işık + Tilakoit Enzim', 9, SOLUK, ince=True)
    ic += kutu(176, 14, 170, 72, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(261, 32, 'Elektronların Kaderi', 10.5, MAVI)
    ic += yazi(261, 50, '• 2e⁻ -> PS II Klorofiline', 9.5, LAC, ince=True)
    ic += yazi(261, 64, '• 2H⁺ -> Tilakoit boşluğa', 9.5, LAC, ince=True)
    ic += yazi(261, 78, '• O₂ -> Atmosfere verilir', 9.5, YES, ince=True)
    return svg(360, 100, ic, 'Suyun fotolizi ve elektron aktarım şeması', 34)


def g3_isik_spektrumu():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    # Spektrum eksenleri
    ic += f'<line x1="40" y1="80" x2="330" y2="80" stroke="{GRI}" stroke-width="1.2"/>'
    ic += f'<line x1="40" y1="80" x2="40" y2="16" stroke="{GRI}" stroke-width="1.2"/>'
    ic += yazi(32, 22, 'Hız', 8.5, LAC, hiza='end')
    ic += yazi(330, 92, 'Dalga Boyu (nm)', 8.5, LAC, hiza='end')
    # Soğurma eğrisi (Mor yüksek, yeşil çukur, kırmızı yüksek)
    ic += f'<path d="M 50,26 Q 90,30 130,72 Q 185,76 240,70 Q 290,32 320,38" fill="none" stroke="{YES}" stroke-width="2.5"/>'
    ic += yazi(70, 20, 'Mor/Mavi (Yüksek)', 8.5, MOR)
    ic += yazi(185, 88, 'Yeşil (Düşük)', 8.5, YES)
    ic += yazi(305, 26, 'Kırmızı (Yüksek)', 8.5, KIR)
    return svg(360, 100, ic, 'Klorofilin ışığı soğurma ve fotosentez hız grafiği', 34)


def g5_ets_akisi():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    basamaklar = [
        ('1. Foton', 'Klorofil uyarılır'),
        ('2. ETS', 'Elektron aktarımı'),
        ('3. Gradient', 'Proton birikimi'),
        ('4. Sentez', 'ATP ve NADPH')
    ]
    for i, (b, acik) in enumerate(basamaklar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Tilakoit zarda ETS ve fotofosforilasyon akışı', 34)


def g6_minimum_kurali():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    # Liebig fıçısı şematiği (farklı boyda tahtalar)
    tahtalar = [
        ('Işık', 50, MAVI),
        ('CO₂', 28, KIR), # en kısa
        ('Sıcaklık', 56, TUR),
        ('Su', 62, CAM),
        ('Mineral', 48, YES)
    ]
    for i, (ad, h, col) in enumerate(tahtalar):
        x = 24 + i * 28
        y = 82 - h
        ic += f'<rect x="{x}" y="{y}" width="22" height="{h}" fill="{col}" opacity="0.8" rx="2" stroke="{LAC}" stroke-width="0.8"/>'
        ic += yazi(x + 11, 92, ad, 7.5, LAC)
    # Su seviyesi çizgisi
    ic += f'<line x1="18" y1="54" x2="168" y2="54" stroke="{KIR}" stroke-width="1.5" stroke-dasharray="4,2"/>'
    ic += yazi(90, 48, 'Sınır: CO₂ (Minimum)', 8.5, KIR)
    # Sağ açıklama kutusu
    ic += kutu(176, 12, 170, 76, '#fef6ec', TUR, 6, 1.1)
    ic += yazi(261, 30, 'MİNİMUM KURALI', 11, TUR)
    ic += yazi(261, 50, 'Fotosentez hızını ortamda', 9.5, LAC, ince=True)
    ic += yazi(261, 66, 'en az bulunan faktör', 9.5, LAC, ince=True)
    ic += yazi(261, 80, 'belirler ve sınırlar.', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Liebig minimum kuralı fıçı modeli', 34)


def g8_faktorler_karsilastirma():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ic += kutu(14, 10, 160, 80, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(94, 28, 'Çevresel Faktörler', 11, CAM)
    ic += yazi(94, 46, '• Işık şiddeti ve dalga boyu', 9, LAC, ince=True)
    ic += yazi(94, 60, '• Karbondioksit derişimi', 9, LAC, ince=True)
    ic += yazi(94, 74, '• Ortam sıcaklığı ve su', 9, LAC, ince=True)

    ic += kutu(186, 10, 160, 80, '#f2fbfd', CAM, 6, 1.2)
    ic += yazi(266, 28, 'Genetik Faktörler', 11, MOR)
    ic += yazi(266, 46, '• Klorofil pigment miktarı', 9, LAC, ince=True)
    ic += yazi(266, 60, '• Yaprak yüzeyi ve stoma', 9, LAC, ince=True)
    ic += yazi(266, 74, '• Enzimlerin çalışma kapasitesi', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Fotosentez hızını etkileyen faktörler tablosu', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: B - E - S - İ - N', 11.5, YES)
    harfler = [('1', 'B'), ('2', 'E'), ('3', 'S'), ('4', 'İ'), ('5', 'N')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Besin şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_kloroplast()
    s[1]['gorsel'] = g1_calvin_dongusu()
    s[2]['gorsel'] = g2_fotoliz_semasi()
    s[3]['gorsel'] = g3_isik_spektrumu()
    s[5]['gorsel'] = g5_ets_akisi()
    s[6]['gorsel'] = g6_minimum_kurali()
    s[8]['gorsel'] = g8_faktorler_karsilastirma()
    s[10]['gorsel'] = g10_sifre_seridi()
