"""6. sınıf Fen Bilimleri 7. hafta (Sabit Süratli ve Sabit Hızlı Hareket Grafikleri & Canlılarda Üremeye Giriş) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def ray_ve_cember_pisti():
    ic = kutu(8, 8, 284, 88, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(150, 26, 'K Treni (Doğrusal Ray — Yön Sabit)', 10.6, MAVI)
    ic += f'<line x1="28" y1="56" x2="272" y2="56" stroke="{LAC}" stroke-width="2.4"/>'
    ic += kutu(76, 42, 64, 18, MAVI, LAC, 4, 1.2)
    ic += yazi(108, 55, 'K Treni', 10.2, '#fff')
    ic += f'<line x1="146" y1="51" x2="196" y2="51" stroke="{TUR}" stroke-width="2.2"/><polygon points="196,46 206,51 196,56" fill="{TUR}"/>'
    ic += yazi(150, 82, 'Her 1 s’de 20 m (Doğu yönü)', 10.2, LAC, ince=True)

    ic += kutu(308, 8, 284, 88, TUR_A, TUR, 9, 1.5)
    ic += yazi(450, 26, 'L Aracı (Çembersel Pist — Yön Değişken)', 10.6, TUR)
    ic += f'<circle cx="376" cy="58" r="24" fill="none" stroke="{TUR}" stroke-width="2.2" stroke-dasharray="5 3"/>'
    ic += f'<circle cx="376" cy="34" r="6" fill="{KIR}"/>'
    ic += yazi(492, 54, 'Her 1 s’de 20 m yol alır;', 10.2, LAC, ince=True)
    ic += yazi(492, 74, 'yönü sürekli döner.', 10.2, KIR)
    return svg(600, 104, ic, 'Doğrusal rayda K treni ve çembersel pistte dönen L aracı karşılaştırması.', 22)


def yol_zaman_grafigi():
    ic = kutu(8, 6, 584, 98, KUM, GRI, 9, 1.5)
    ic += yazi(170, 24, 'Yol (m) – Zaman (s) Grafiği', 10.8, MAVI)
    # Eksenler
    ic += f'<line x1="56" y1="86" x2="290" y2="86" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="56" y1="86" x2="56" y2="30" stroke="{LAC}" stroke-width="1.8"/>'
    # Doğrusal artan çizgi
    ic += f'<line x1="56" y1="86" x2="248" y2="36" stroke="{YES}" stroke-width="2.5"/>'
    for i, (t, x_m) in enumerate([(1, 12), (2, 24), (3, 36)]):
        px = 56 + (i + 1) * 64
        py = 86 - (i + 1) * 16.5
        ic += f'<circle cx="{px}" cy="{py:.1f}" r="3.5" fill="{YES}"/>'
        ic += yazi(px, 98, f'{t} s', 10.0, LAC, ince=True)
        ic += yazi(36, py + 4, f'{x_m}', 10.0, LAC, ince=True)
    ic += kutu(326, 20, 248, 68, YES_A, YES, 8, 1.4)
    ic += yazi(450, 42, 'Grafik Verileri:', 10.8, YES)
    ic += yazi(450, 62, '1 s → 12 m · 2 s → 24 m · 3 s → 36 m', 10.4, LAC, ince=True)
    ic += yazi(450, 80, 't = 10 s sonunda alınan yol = ?', 10.4, LAC)
    return svg(600, 110, ic, '1 saniyede 12 metre, 2 saniyede 24 metre, 3 saniyede 36 metre gösteren doğrusal yol-zaman grafiği.', 22)


def hareket_veri_kartlari():
    kartlar = [
        ('1. K Aracı', 'Yol: 60 m · Zaman: 4 s', MAVI, MAVI_A),
        ('2. L Aracı', 'Yol: 180 km · Zaman: 2 h', TUR, TUR_A),
        ('3. M Aracı', 'Zaman: 5 s · Sürat: 20 m/s', YES, YES_A),
        ('4. N Aracı', 'Yol: 240 km · Sürat: 80 km/h', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, veri, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 76, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 24, renk, renk, 8, 1)
        ic += yazi(x + 69, 24, bas, 10.6, '#fff')
        ic += yazi(x + 69, 58, veri.replace('/', '÷'), 10.2, LAC, ince=True)
    return svg(600, 92, ic, 'K, L, M ve N araçlarının yol, zaman ve sürat verilerini içeren dört kart.', 22)


def iki_yatay_grafik():
    ic = kutu(8, 8, 284, 86, KIR_A, KIR, 9, 1.5)
    ic += yazi(150, 24, 'I. Grafik: Yol (m) – Zaman (s)', 10.6, KIR)
    ic += f'<line x1="48" y1="78" x2="256" y2="78" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="48" y1="78" x2="48" y2="34" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="48" y1="52" x2="246" y2="52" stroke="{KIR}" stroke-width="2.6"/>'
    ic += yazi(32, 56, '15 m', 10.0, KIR)

    ic += kutu(308, 8, 284, 86, YES_A, YES, 9, 1.5)
    ic += yazi(450, 24, 'II. Grafik: Sürat – Zaman (s)', 10.6, YES)
    ic += f'<line x1="348" y1="78" x2="556" y2="78" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="348" y1="78" x2="348" y2="34" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="348" y1="52" x2="546" y2="52" stroke="{YES}" stroke-width="2.6"/>'
    ic += yazi(330, 56, '15', 10.0, YES)
    return svg(600, 102, ic, 'Sol tarafta yatay çizgili yol-zaman grafiği, sağ tarafta yatay çizgili sürat-zaman grafiği.', 22)


def ureme_posterleri():
    posterler = [
        ('1. Poster: Amip', '1 hücre → 2 yeni amip', MAVI, MAVI_A),
        ('2. Poster: Hidra', 'Tomurcuk → yeni hidra', YES, YES_A),
        ('3. Poster: Kertenkele (!)', 'Kopan kuyruğun onarımı', KIR, KIR_A),
        ('4. Poster: Denizyıldızı', 'Kopan koldan yeni birey', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(posterler):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 10.6, renk)
        ic += yazi(x + 144, y + 35, alt, 10.2, LAC, ince=True)
    return svg(600, 104, ic, 'Dört poster: amip bölünmesi, hidra tomurcuklanması, kertenkele kuyruk onarımı ve denizyıldızı rejenerasyonu.', 22)


def cilek_vejetatif_karti():
    ic = kutu(8, 8, 584, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 584, 24, YES, YES, 9, 1)
    ic += yazi(300, 24, 'BAHÇE GÖZLEM KARTI · VERİMLİ ÇİLEK BİTKİSİ', 10.8, '#fff')
    ic += kutu(24, 40, 250, 42, '#fff', YES, 7, 1.4)
    ic += yazi(149, 58, 'Ata Bitki: İri ve Tatlı Çilek', 10.5, YES)
    ic += yazi(149, 74, 'Hedef: Birebir aynı kalıtsal yapı', 10.1, LAC, ince=True)
    ic += f'<line x1="282" y1="61" x2="326" y2="61" stroke="{TUR}" stroke-width="2.2"/><polygon points="326,56 336,61 326,66" fill="{TUR}"/>'
    ic += kutu(344, 40, 232, 42, TUR_A, TUR, 7, 1.4)
    ic += yazi(460, 58, 'Seçilecek Üreme Yöntemi = ?', 10.5, TUR)
    ic += yazi(460, 74, '(Sürünücü gövde mi, tohum mu?)', 10.1, LAC, ince=True)
    return svg(600, 100, ic, 'Ata çilek bitkisinden birebir aynı kalıtsal yapıda yeni fideler elde etme şeması.', 22)


def eseysiz_eseyli_sema():
    ic = kutu(8, 8, 284, 82, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(150, 26, 'K Olayı (Eşeysiz Üreme)', 10.8, MAVI)
    ic += yazi(150, 48, 'Tek ata canlı · Döllenme yok', 10.3, LAC, ince=True)
    ic += yazi(150, 68, 'Kalıtsal yapı: Atayla birebir aynı', 10.3, MAVI)

    ic += kutu(308, 8, 284, 82, MOR_A, MOR, 9, 1.5)
    ic += yazi(450, 26, 'L Olayı (Eşeyli Üreme)', 10.8, MOR)
    ic += yazi(450, 48, 'Yumurta + Sperm → Döllenme → Zigot', 10.3, LAC, ince=True)
    ic += yazi(450, 68, 'Kalıtsal yapı: Kalıtsal çeşitlilik var', 10.3, MOR)
    return svg(600, 98, ic, 'Eşeysiz üreme (K olayı) ve eşeyli üreme (L olayı) karşılaştırma kartları.', 22)


def ikili_surat_zaman_grafigi():
    ic = kutu(8, 6, 584, 96, KUM, GRI, 9, 1.5)
    ic += yazi(176, 22, 'Sürat – Zaman (s) Grafiği (6 Saniye)', 10.8, LAC)
    ic += f'<line x1="56" y1="86" x2="296" y2="86" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="56" y1="86" x2="56" y2="28" stroke="{LAC}" stroke-width="1.8"/>'
    # K aracı (20) ve L aracı (12)
    ic += f'<line x1="56" y1="42" x2="266" y2="42" stroke="{MAVI}" stroke-width="2.6"/>'
    ic += yazi(38, 46, '20', 10.2, MAVI)
    ic += yazi(280, 46, 'K', 10.5, MAVI)
    ic += f'<line x1="56" y1="62" x2="266" y2="62" stroke="{TUR}" stroke-width="2.6"/>'
    ic += yazi(38, 66, '12', 10.2, TUR)
    ic += yazi(280, 66, 'L', 10.5, TUR)
    ic += yazi(266, 98, '6 s', 10.0, LAC)

    ic += kutu(326, 20, 248, 66, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(450, 40, 'Alınan Yol = Sürat × Zaman', 10.6, MAVI)
    ic += yazi(450, 60, 'K sürati = 20 · L sürati = 12', 10.3, LAC, ince=True)
    ic += yazi(450, 78, 't = 6 s sonunda yol farkı = ?', 10.3, LAC)
    return svg(600, 108, ic, 'K (20) ve L (12) araçlarının 6 saniyelik sabit sürat-zaman grafiği.', 22)


def eseysiz_siniflama_tablosu():
    sutunlar = [
        ('1. Bölünerek', 'Bakteri', MAVI, MAVI_A),
        ('2. Tomurcuklanarak', 'Bira mayası', YES, YES_A),
        ('3. Rejenerasyon (!)', 'Menekşe yaprağı', KIR, KIR_A),
        ('4. Vejetatif', 'Patates yumrusu', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ornek, renk, arka) in enumerate(sutunlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 76, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 24, renk, renk, 8, 1)
        ic += yazi(x + 69, 24, bas, 10.4, '#fff')
        ic += yazi(x + 69, 58, ornek, 10.5, LAC)
    return svg(600, 92, ic, 'Dört eşeysiz üreme sütunu: 3. sütunda rejenerasyon altına yanlışlıkla menekşe yaprağı yazılmış.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ray_ve_cember_pisti()
    s[4]['gorsel'] = yol_zaman_grafigi()
    s[5]['gorsel'] = hareket_veri_kartlari()
    s[6]['gorsel'] = iki_yatay_grafik()
    s[8]['gorsel'] = ureme_posterleri()
    s[9]['gorsel'] = cilek_vejetatif_karti()
    s[10]['gorsel'] = eseysiz_eseyli_sema()
    s[12]['gorsel'] = ikili_surat_zaman_grafigi()
    s[13]['gorsel'] = eseysiz_siniflama_tablosu()
