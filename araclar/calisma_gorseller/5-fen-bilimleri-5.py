"""5. sınıf Fen Bilimleri 5. hafta (Gökyüzündeki Komşumuz: Ay – Ay’ın Evreleri ve Evre Modeli) çalışma kâğıdı görselleri.
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


def ana_evreler_konum_sema():
    ic = kutu(6, 6, 588, 96, KUM, GRI, 9, 1.4)
    ic += f'<circle cx="52" cy="54" r="26" fill="{TUR}" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(52, 58, 'Güneş', '#fff', kalin=True)
    for y_ok in (30, 54, 78):
        ic += f'<line x1="84" y1="{y_ok}" x2="118" y2="{y_ok}" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<ellipse cx="240" cy="54" rx="88" ry="38" fill="none" stroke="{MAVI}" stroke-width="1.4" stroke-dasharray="4,3"/>'
    ic += f'<circle cx="240" cy="54" r="14" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(240, 58, 'Dünya', MAVI, kalin=True)
    konumlar = [
        (152, 54, '1', '1: Yeni Ay'),
        (240, 16, '4', '2: İlk Dördün'),
        (328, 54, '3', '3: Dolunay'),
        (240, 92, '2', '4: Son Dördün'),
    ]
    for cx, cy, no, _ in konumlar:
        ic += f'<circle cx="{cx}" cy="{cy}" r="9" fill="{GRI_A}" stroke="{LAC}" stroke-width="1.4"/>'
        ic += yazi(cx, cy + 4, no, LAC, kalin=True)
    ic += kutu(360, 14, 222, 80, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(471, 32, 'Ay’ın Dolanma Yönü: ↺', MAVI, kalin=True)
    ic += yazi(471, 54, '1: Güneş ile Dünya arasında', LAC, kalin=True)
    ic += yazi(471, 76, '3: Dünya, Güneş ile Ay arasında', LAC)
    return svg(600, 108, ic, 'Güneş ışınları ve Dünya etrafındaki 1, 2, 3, 4 numaralı Ay konumları.', 20)


def ekim_gozlem_takvimi():
    ic = kutu(6, 6, 588, 86, MAVI_A, MAVI, 9, 1.4)
    kartlar = [
        ('4 Ekim', 'İlk Dördün (◐)', YES, YES_A),
        ('? Ekim (+7 gün)', 'Dolunay (○)', TUR, TUR_A),
        ('? Ekim (+14 gün)', 'Son Dördün (◑)', MOR, MOR_A),
    ]
    for i, (tar, evre, renk, arka) in enumerate(kartlar):
        x = 16 + i * 192
        ic += kutu(x, 16, 180, 66, arka, renk, 8, 1.4)
        ic += yazi(x + 90, 40, tar, renk, kalin=True)
        ic += yazi(x + 90, 66, evre, LAC, kalin=True)
    return svg(600, 98, ic, '4 Ekim ilk dördün gözleminden sonra dolunay ve son dördün tarih hesaplama kartı.', 20)


def dort_evre_gorunum_kartlari():
    kartlar = [
        ('1. İlk Hilal', 'Ara Evre · Sağda ince kavis', MAVI, MAVI_A),
        ('2. İlk Dördün', 'Ana Evre · Sağ yarısı aydınlık', YES, YES_A),
        ('3. İlk Şişkin Ay', 'Ara Evre · Sağ tarafı dolgun', TUR, TUR_A),
        ('4. Son Dördün', 'Ana Evre · Sol yarısı aydınlık', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'İlk hilal, ilk dördün, ilk şişkin ay ve son dördün görünüm kartları.', 20)


def golge_bakis_acisi_panosu():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, 'A Kartı · Yanlış Açıklama (!)', KIR, kalin=True)
    ic += yazi(149, 50, '“Dünya’nın gölgesi her gece Ay’ın', LAC)
    ic += yazi(149, 72, 'üzerine düşerek evreleri oluşturur.”', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'B Kartı · Bilimsel Açıklama', YESIL_K, kalin=True)
    ic += yazi(451, 50, '“Ay dolanırken Güneş’ten ışık alan', LAC)
    ic += yazi(451, 72, 'yarısını Dünya’dan farklı açıyla görürüz.”', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'Ay evrelerinin gölgeden değil bakış açısından kaynaklandığını gösteren kartlar.', 20)


def buyuyen_ay_siralama_kartlari():
    kartlar = [
        ('İlk Hilal', 'Sağda ince kavis', MAVI, MAVI_A),
        ('İlk Dördün', 'Sağ yarım daire (D)', YES, YES_A),
        ('İlk Şişkin Ay', 'Yarımdan büyük dolgun', TUR, TUR_A),
        ('Dolunay', 'Tam parlak daire', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Yeni aydan dolunaya kadar büyüyen Ay evrelerinin sıralama kartları.', 20)


def fener_top_model_karti():
    kartlar = [
        ('1. Işık Kaynağı', 'El feneri = Güneş (Tek yönden ışık)', TUR, TUR_A),
        ('2. Küresel Cisim', 'Çubuktaki top = Ay (Yarısı aydınlık)', MAVI, MAVI_A),
        ('3. Gölge Önlemi', 'Top baş hizasının biraz üstünde tutulur', YES, YES_A),
        ('4. Dolanma Yönü', 'Saat yönünün tersine (↺) döndürülür', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'El feneri ve top ile kurulan Ay evreleri modelinin kuralları.', 20)


def dolanma_evre_farki_sema():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 25, '1. Dolanma Süresi (~27,3 Gün)', MAVI, kalin=True)
    ic += yazi(149, 50, 'Ay’ın Dünya çevresinde 1 tam tur', LAC, kalin=True)
    ic += yazi(149, 74, 'dolanmasını tamamlama süresidir.', LAC)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(451, 25, '2. Evre Döngüsü (~29,5 Gün)', TUR, kalin=True)
    ic += yazi(451, 50, 'Dünya da Güneş etrafında ilerlediği için', LAC, kalin=True)
    ic += yazi(451, 74, 'aynı evreye ~2 gün geç ulaşılır.', LAC)
    return svg(600, 98, ic, '27,3 günlük dolanma süresi ile 29,5 günlük evre döngüsü farkı kartı.', 20)


def super_ay_takvim_panosu():
    kartlar = [
        ('Hicrî Ay Takvimi', '29,5 günlük evre döngüsüne dayanır', YES, YES_A),
        ('Süper Ay Olayı', 'En yakın konumda büyük görünüm', TUR, TUR_A),
        ('Mikro Ay Olayı', 'En uzak konumda küçük görünüm', MAVI, MAVI_A),
        ('Gerçek Büyüklük', 'Ay’ın çapı ve kütlesi hiç değişmez', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Ay takvimi, Süper Ay ve Mikro Ay özelliklerini özetleyen pano.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ana_evreler_konum_sema()
    s[4]['gorsel'] = ekim_gozlem_takvimi()
    s[5]['gorsel'] = dort_evre_gorunum_kartlari()
    s[6]['gorsel'] = golge_bakis_acisi_panosu()
    s[7]['gorsel'] = buyuyen_ay_siralama_kartlari()
    s[8]['gorsel'] = fener_top_model_karti()
    s[10]['gorsel'] = dolanma_evre_farki_sema()
    s[11]['gorsel'] = super_ay_takvim_panosu()
