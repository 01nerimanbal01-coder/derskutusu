"""6. sınıf Fen Bilimleri 6. hafta (Sabit Süratli ve Sabit Hızlı Hareket: Sürat, Birimleri ve Yol-Zaman Grafiği) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kosu_pisti_verileri():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, '1. Kulvar (Elif’in Koşu Verisi)', 12, '#fff')
    ic += yazi(150, 52, 'Alınan Yol: 100 metre', 12, LAC)
    ic += yazi(150, 74, 'Geçen Süre: 20 saniye → Sürat = ?', 12, MAVI, ince=True)

    ic += kutu(308, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(450, 25, '2. Kulvar (Can’ın Koşu Verisi)', 12, '#fff')
    ic += yazi(450, 52, 'Alınan Yol: 150 metre', 12, LAC)
    ic += yazi(450, 74, 'Geçen Süre: 25 saniye → Sürat = ?', 12, TUR, ince=True)
    return svg(600, 100, ic, 'Elif ve Can koşu kulvarlarının yol ve zaman ölçüm kartları.', 22)


def oyuncak_araba_cetveli():
    ic = kutu(8, 8, 584, 88, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 584, 26, YES, YES, 9, 1)
    ic += yazi(300, 25, 'SABİT SÜRATLİ OYUNCAK ARABA DENEYİ · KONUM CETVELİ', 12, '#fff')
    ic += f'<line x1="48" y1="62" x2="552" y2="62" stroke="{LAC}" stroke-width="2.2"/>'
    noktalar = [(48, '0 s', '0 cm'), (174, '1 s', '20 cm'), (300, '2 s', '40 cm'), (426, '3 s', '60 cm'), (552, '4 s', '80 cm')]
    for x, t_str, x_str in noktalar:
        ic += f'<circle cx="{x}" cy="62" r="5" fill="{TUR}"/>'
        ic += yazi(x, 48, t_str, 12, TUR)
        ic += yazi(x, 84, x_str, 12, LAC, ince=True)
    return svg(600, 104, ic, '0, 1, 2, 3 ve 4. saniyelerde 0, 20, 40, 60 ve 80 cm konumlarını gösteren cetvel.', 22)


def dort_hareketli_kartlari():
    kartlar = [
        ('1. Bisikletli', 'Yol: 240 m · Süre: 30 s', MAVI, MAVI_A),
        ('2. Otobüs', 'Yol: 180 km · Süre: 3 h', TUR, TUR_A),
        ('3. Koşucu', 'Süre: 40 s · Sürat: 5 m÷s', YES, YES_A),
        ('4. Öğrenci', 'Yol: 90 m · Sürat: 1,5 m÷s', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Dört hareketlinin yol, süre ve sürat verilerini içeren kartlar.', 22)


def ikili_yol_zaman_grafigi():
    ic = kutu(8, 6, 584, 98, KUM, GRI, 9, 1.5)
    ic += yazi(170, 24, 'Yol (m) - Zaman (s) Grafiği', 12, MAVI)
    ic += f'<line x1="56" y1="86" x2="290" y2="86" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="56" y1="86" x2="56" y2="28" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="56" y1="86" x2="240" y2="34" stroke="{KIR}" stroke-width="2.6"/>'
    ic += f'<line x1="56" y1="86" x2="240" y2="56" stroke="{MAVI}" stroke-width="2.6"/>'
    ic += yazi(258, 38, 'K (100 m)', 12, KIR)
    ic += yazi(258, 60, 'L (60 m)', 12, MAVI)
    ic += yazi(240, 99, '5 s', 12, LAC)

    ic += kutu(326, 20, 248, 68, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(450, 42, 't = 5 s Sonundaki Konumlar:', 12, MAVI)
    ic += yazi(450, 62, 'K aracı: 100 m · L aracı: 60 m', 12, LAC, ince=True)
    ic += yazi(450, 80, 'Sürat = Yol ÷ Zaman', 12, KIR)
    return svg(600, 110, ic, '5 saniyede K aracının 100 m, L aracının 60 m yol aldığını gösteren yol-zaman grafiği.', 22)


def surat_siralama_kartlari():
    adimlar = [
        ('Yarış Bisikleti', '300 m · 30 s', MAVI, MAVI_A),
        ('Atlet Can', '150 m · 25 s', YES, YES_A),
        ('Patenci', '160 m · 40 s', TUR, TUR_A),
        ('Öğrenci', '90 m · 60 s', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Dört hareketlinin aldığı yol ve süre kartları.', 22)


def surat_mi_hiz_mi_panosu():
    kartlar = [
        ('I. Top Kartı', '“Top 3 m÷s ile yuvarlanıyor.” (Yön yok)', MAVI, MAVI_A),
        ('II. Otobüs Kartı', '“Otobüs kuzeye 60 km÷h ile gidiyor.” (Yön var)', YES, YES_A),
        ('III. Koşucu Kartı', '“Koşucunun çabukluğu 7 m÷s.” (Yön yok)', TUR, TUR_A),
        ('IV. Uçak Kartı', '“Uçak batıya 900 km÷h ile uçuyor.” (Yön var)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Yön belirten ve belirtmeyen dört hareket ifadesi kartı.', 22)


def bisiklet_hesap_karti():
    ic = kutu(8, 8, 584, 84, CAM_A, CAM, 9, 1.6)
    ic += kutu(8, 8, 584, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 25, 'SABİT SÜRATLİ BİSİKLET PARKURU · SÜRAT = 4 m÷s', 12, '#fff')
    ic += yazi(300, 52, 'Bağıntılar: Alınan Yol = Sürat × Süre · Geçen Süre = Alınan Yol ÷ Sürat', 12, LAC)
    ic += yazi(300, 76, '1. Görev: t = 2 min (120 s) için yol · 2. Görev: x = 600 m için süre', 12, CAM, ince=True)
    return svg(600, 100, ic, 'Sabit 4 metre bölü saniye süratli bisiklet parkuru hesap kartı.', 22)


def okul_yolu_karsilastirma():
    ic = kutu(8, 8, 284, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MOR, MOR, 9, 1)
    ic += yazi(150, 25, 'Ayşe’nin Yürüyüşü', 12, '#fff')
    ic += yazi(150, 52, 'Alınan Yol: 600 m', 12, LAC)
    ic += yazi(150, 74, 'Süre: 10 min = 600 s', 12, MOR, ince=True)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, 'Ali’nin Yürüyüşü', 12, '#fff')
    ic += yazi(450, 52, 'Alınan Yol: 600 m', 12, LAC)
    ic += yazi(450, 74, 'Süre: 8 min = 480 s', 12, YES, ince=True)
    return svg(600, 100, ic, '600 metrelik okul yolunu 600 saniyede ve 480 saniyede yürüyen iki kardeşin veri kartı.', 22)


def otobus_otomobil_karti():
    ic = kutu(8, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(150, 25, 'Otobüs Yolculuğu', 12, '#fff')
    ic += yazi(150, 52, 'Alınan Yol: 240 km', 12, LAC)
    ic += yazi(150, 74, 'Geçen Süre: 4 saat (4 h)', 12, TUR, ince=True)

    ic += kutu(308, 8, 284, 84, KIR_A, KIR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, KIR, KIR, 9, 1)
    ic += yazi(450, 25, 'Otomobil Yolculuğu', 12, '#fff')
    ic += yazi(450, 52, 'Alınan Yol: 350 km', 12, LAC)
    ic += yazi(450, 74, 'Geçen Süre: 5 saat (5 h)', 12, KIR, ince=True)
    return svg(600, 100, ic, '240 kilometreyi 4 saatte alan otobüs ile 350 kilometreyi 5 saatte alan otomobil kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kosu_pisti_verileri()
    s[4]['gorsel'] = oyuncak_araba_cetveli()
    s[5]['gorsel'] = dort_hareketli_kartlari()
    s[6]['gorsel'] = ikili_yol_zaman_grafigi()
    s[7]['gorsel'] = surat_siralama_kartlari()
    s[8]['gorsel'] = surat_mi_hiz_mi_panosu()
    s[9]['gorsel'] = bisiklet_hesap_karti()
    s[11]['gorsel'] = okul_yolu_karsilastirma()
    s[12]['gorsel'] = otobus_otomobil_karti()
