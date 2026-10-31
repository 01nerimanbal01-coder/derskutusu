"""7. sınıf Fen Bilimleri 4. hafta (Yıldız, ışık yılı, takımyıldız, galaksi ve evren) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk=LAC, r=11, boy=12):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.35, metin, boy, renk)


def yildiz_boyutlari():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="12" fill="#f7f9fd" stroke="{GRI}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Yıldızların Büyüklük Sıralaması (Küçükten Büyüğe: P < R < S < T)', 12, LAC)
    yildizlar = [
        (90, 68, 12, '#f5c421', '#d99b00', 'P', 'En küçük'),
        (215, 68, 18, '#dbeafe', '#2451d6', 'R', '2. sırada'),
        (355, 68, 25, '#fed7aa', '#ee7d12', 'S', '3. sırada'),
        (505, 68, 34, '#fca5a5', '#d63a3a', 'T', 'En büyük'),
    ]
    for i, (cx, cy, r, dolgu, kenar, harf, alt) in enumerate(yildizlar):
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="2"/>'
        ic += yazi(cx, cy + 4, harf, 12.5, LAC)
        ic += yazi(cx, 116, alt, 11, LAC, ince=True)
        if i < 3:
            nx = yildizlar[i + 1][0] - yildizlar[i + 1][2] - 12
            sx = cx + r + 12
            ic += f'<line x1="{sx}" y1="{cy}" x2="{nx}" y2="{cy}" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{nx - 5} {cy - 4} l5 4 l-5 4" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 134, ic, 'Küçükten büyüğe sıralanmış dört yıldız modeli: P, R, S ve T.', 25)


def renk_sicaklik_kartlari():
    kartlar = [
        ('X Yıldızı', 'Görünüm: Mavi - Beyaz', 'Çok yüksek yüzey sıcaklığı', '#60a5fa', MAVI, MAVI_A),
        ('Y Yıldızı', 'Görünüm: Sarı - Turuncu', 'Orta düzey yüzey sıcaklığı', '#f5c421', TUR, TUR_A),
        ('Z Yıldızı', 'Görünüm: Kırmızı', 'Düşük yüzey sıcaklığı', '#ef4444', KIR, '#fde8e8'),
    ]
    ic = ''
    for i, (bas, renk_ad, acik, yrenk, kenar, arka) in enumerate(kartlar):
        x = 6 + i * 198
        cx = x + 96
        ic += f'<rect x="{x}" y="6" width="192" height="122" rx="10" fill="{arka}" stroke="{kenar}" stroke-width="1.8"/>'
        ic += yazi(cx, 25, bas, 12.5, kenar)
        ic += f'<circle cx="{cx}" cy="58" r="20" fill="{yrenk}" stroke="{kenar}" stroke-width="2"/>'
        ic += yazi(cx, 96, renk_ad, 11.5, LAC)
        ic += yazi(cx, 114, acik, 11, LAC, ince=True)
    return svg(600, 134, ic, 'Üç yıldız gözlem kartı: X (Mavi-Beyaz), Y (Sarı-Turuncu), Z (Kırmızı).', 17)


def gok_bilimi_kartlari():
    kart = [
        ('1. Kart · Örnekler', 'Aldebaran, Rigel ve Antares', 'Isı ve ışık yayan dev küreler', TUR, TUR_A),
        ('2. Kart · Örnekler', 'Avcı, Başak, Ejderha, Kraliçe', 'Gökyüzünde çizilen yıldız şekilleri', MAVI, MAVI_A),
        ('3. Kart · Örnekler', 'Samanyolu ve Andromeda', 'Milyarlarca yıldızlı sarmal sistemler', MOR, MOR_A),
        ('4. Kart · Örnek', 'Tarantula (170 bin ışık yılı)', 'Yıldızların doğduğu gaz-toz bulutu', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 66
        ic += f'<rect x="{x}" y="{y}" width="286" height="58" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="58" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 36, s1, 12, LAC, 'start')
        ic += yazi(x + 18, y + 51, s2, 11, LAC, 'start', ince=True)
    return svg(600, 136, ic, 'Dört gök bilimi kartı: 1. Aldebaran/Rigel/Antares, 2. Avcı/Başak/Ejderha/Kraliçe, 3. Samanyolu/Andromeda, 4. Tarantula.', 17)


def buyukayi_haritasi():
    ic = f'<rect x="6" y="6" width="588" height="132" rx="12" fill="#0f1e46" stroke="{MAVI}" stroke-width="1.8"/>'
    # Cezve 7 yıldızı
    pts = [(55, 92), (105, 82), (145, 96), (185, 116), (255, 120), (265, 76), (185, 80)]
    cizgiler = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 2)]
    for a, b in cizgiler:
        ic += f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" x2="{pts[b][0]}" y2="{pts[b][1]}" stroke="#93c5fd" stroke-width="2"/>'
    for i, (px, py) in enumerate(pts):
        renk = '#fb923c' if i in (4, 5) else '#fff'
        ic += f'<circle cx="{px}" cy="{py}" r="5" fill="{renk}"/>'
    # 5 kat doğrultu
    ic += f'<line x1="265" y1="76" x2="455" y2="34" stroke="#fb923c" stroke-width="2.2" stroke-dasharray="6 4"/>'
    ic += f'<circle cx="455" cy="34" r="10" fill="#fde047" stroke="#f59e0b" stroke-width="2"/>'
    ic += yazi(145, 52, 'Büyükayı (7 yıldızlı cezve)', 12, '#e0f2fe')
    ic += yazi(335, 96, 'Uçtaki iki yıldız arası = d', 11, '#fed7aa')
    ic += yazi(360, 32, '5 · d uzaklık', 11.5, '#fde047')
    ic += yazi(455, 62, 'K Yıldızı (?)', 12.5, '#fde047')
    # Sağda yön oku
    ic += f'<line x1="545" y1="108" x2="545" y2="36" stroke="#4ade80" stroke-width="2.4"/>'
    ic += f'<path d="M539 44 l6 -10 l6 10" fill="none" stroke="#4ade80" stroke-width="2.2"/>'
    ic += yazi(545, 24, 'Yön: ?', 12, '#4ade80')
    return svg(600, 144, ic, 'Büyükayı takımyıldızının 7 yıldızlı cezve şekli ve uçtaki iki yıldız arası uzaklığın 5 katı ilerisindeki K yıldızı.', 17)


def buyukluk_basamaklari():
    ic = ''
    for i in range(5):
        x = 16 + i * 116
        h = 26 + i * 14
        y = 104 - h
        ic += f'<rect x="{x}" y="{y}" width="96" height="{h}" rx="6" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
        ic += f'<circle cx="{x + 48}" cy="{y - 14}" r="{6 + i * 2.2:.1f}" fill="#f5c421" stroke="{TUR}" stroke-width="1.5"/>'
        ic += yazi(x + 48, y + h / 2 + 4, f'{i + 1}. Basamak', 11.5, LAC)
        if i < 4:
            ic += f'<line x1="{x + 99}" y1="88" x2="{x + 113}" y2="88" stroke="{LAC}" stroke-width="1.8"/>'
    ic += yazi(300, 122, 'En küçük yıldızdan (1) en büyük yıldıza (5) doğru sıralama basamakları', 11.5, LAC, ince=True)
    return svg(600, 130, ic, '1’den 5’e kadar büyüyen yıldız sıralama basamakları.', 16)


def yildiz_kaymasi_sema():
    ic = f'<rect x="6" y="6" width="286" height="114" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(149, 24, 'Dünya Atmosferi (Yakın Çevre)', 12, MAVI)
    # Dünya yayı ve atmosfer
    ic += f'<path d="M24 108 Q149 78 274 108" fill="#4f8fe8" stroke="#1d4ed8" stroke-width="2"/>'
    ic += f'<path d="M20 92 Q149 60 278 92" fill="none" stroke="#60a5fa" stroke-width="1.6" stroke-dasharray="5 3"/>'
    # Gök taşı ve izi
    ic += f'<line x1="65" y1="38" x2="155" y2="72" stroke="{TUR}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<circle cx="158" cy="73" r="5" fill="{KIR}"/>'
    ic += yazi(149, 52, 'Sürtünmeyle yanan gök taşı', 11.5, LAC)
    ic += yazi(149, 106, 'Dünya yüzeyi ve atmosfer', 11, '#fff')

    ic += f'<rect x="308" y="6" width="286" height="114" rx="10" fill="#0f1e46" stroke="{LAC}" stroke-width="1.8"/>'
    ic += yazi(451, 24, 'Derin Uzay (Gerçek Yıldızlar)', 12, '#fde047')
    for cx, cy in [(355, 58), (445, 50), (535, 62)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="7" fill="#fde047" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(451, 86, 'En yakın yıldız (Proxima Centauri)', 11.5, '#e0f2fe')
    ic += yazi(451, 104, 'Uzaklık: Yaklaşık 40 trilyon km', 11.5, '#fb923c')
    return svg(600, 126, ic, 'Sol: Dünya atmosferinde sürtünmeyle yanan gök taşı. Sağ: Trilyonlarca km uzaktaki gerçek yıldızlar.', 16)


def galaksi_olcek():
    ic = f'<rect x="6" y="6" width="588" height="126" rx="10" fill="#f7f9fd" stroke="{GRI}" stroke-width="1.6"/>'
    # Samanyolu (sol, r=28)
    cx1, cy = 140, 62
    ic += f'<ellipse cx="{cx1}" cy="{cy}" rx="42" ry="24" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<path d="M{cx1 - 30} {cy - 8} Q{cx1} {cy - 22} {cx1 + 30} {cy + 8} M{cx1 - 30} {cy + 8} Q{cx1} {cy + 22} {cx1 + 30} {cy - 8}" fill="none" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<circle cx="{cx1 + 18}" cy="{cy - 6}" r="4.5" fill="{YES}"/>'
    ic += yazi(cx1 + 18, 24, 'Güneş sistemi (Avcı kolu)', 11, YESIL_K)
    ic += f'<line x1="{cx1 + 18}" y1="28" x2="{cx1 + 18}" y2="{cy - 11}" stroke="{YESIL_K}" stroke-width="1.4"/>'
    ic += yazi(cx1, 104, 'Samanyolu Galaksisi (Sarmal)', 12, MAVI)
    ic += yazi(cx1, 120, 'Çap: 1 birim', 11.5, LAC, ince=True)

    # Andromeda (sağ, 2 kat çap: rx=84)
    cx2 = 430
    ic += f'<ellipse cx="{cx2}" cy="{cy}" rx="84" ry="36" fill="{MOR_A}" stroke="{MOR}" stroke-width="2"/>'
    ic += f'<path d="M{cx2 - 64} {cy - 12} Q{cx2} {cy - 34} {cx2 + 64} {cy + 12} M{cx2 - 64} {cy + 12} Q{cx2} {cy + 34} {cx2 + 64} {cy - 12}" fill="none" stroke="{MOR}" stroke-width="2.4"/>'
    ic += yazi(cx2, 108, 'Andromeda Galaksisi (Sarmal)', 12, MOR)
    ic += yazi(cx2, 123, 'Çap: Yaklaşık 2 birim (En yakın galaksi)', 11.5, LAC, ince=True)
    return svg(600, 138, ic, 'Samanyolu galaksisi (çap 1 birim, Avcı kolunda Güneş sistemi) ve Andromeda galaksisi (çap yaklaşık 2 birim).', 17)


def isik_yili_olcek():
    ic = f'<rect x="6" y="6" width="588" height="116" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += yazi(300, 24, '1 Işık Yılı = Işığın boşlukta 1 yılda aldığı yol (Yaklaşık 9,46 trilyon km)', 12, KAHVE)
    # Ölçek çubuğu: Dünya -> Proxima Centauri (4,24 ışık yılı)
    ic += f'<circle cx="52" cy="68" r="14" fill="{MAVI}"/><text x="52" y="102" text-anchor="middle" font-size="11.5" {YAZI} fill="{MAVI}">Dünya</text>'
    for i in range(4):
        x = 76 + i * 96
        renk = YES_A if i % 2 == 0 else MAVI_A
        ic += f'<rect x="{x}" y="60" width="96" height="16" fill="{renk}" stroke="{LAC}" stroke-width="1.4"/>'
        ic += yazi(x + 48, 53, '1 ışık yılı', 11, LAC, ince=True)
    # 0.24 parça
    ic += f'<rect x="460" y="60" width="28" height="16" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(474, 53, '+0,24', 10.5, TUR)
    ic += f'<circle cx="514" cy="68" r="12" fill="{TUR}" stroke="{KIR}" stroke-width="1.8"/>'
    ic += yazi(514, 102, 'Proxima Centauri', 11.5, KIR)
    ic += yazi(280, 104, 'Toplam uzaklık = 4,24 ışık yılı (Yaklaşık 40 trilyon km)', 12, LAC)
    return svg(600, 128, ic, 'Dünya ile Proxima Centauri arasındaki 4,24 ışık yılı (yaklaşık 40 trilyon km) uzaklık ölçeği.', 16)


def takimyildiz_kume_kart():
    ic = f'<rect x="6" y="6" width="286" height="108" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(149, 25, '1. Kart · Takımyıldız', 12.5, MAVI)
    ic += yazi(149, 48, 'Dünya’dan bakıldığında birbirine', 11.5, LAC, ince=True)
    ic += yazi(149, 66, 'yakın görünen yıldızların gökyüzünde', 11.5, LAC, ince=True)
    ic += yazi(149, 84, 'oluşturduğu şekillerdir (Büyükayı, Avcı).', 11.5, LAC, ince=True)
    ic += yazi(149, 102, 'Gözlemi kolaylaştırmak için adlandırılır.', 11, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="108" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(451, 25, '2. Kart · Yıldız Kümesi', 12.5, YESIL_K)
    ic += yazi(451, 48, 'Uzayda gerçekten bir arada bulunan ve', 11.5, LAC, ince=True)
    ic += yazi(451, 66, 'kütle çekim kuvvetiyle birbirine', 11.5, LAC, ince=True)
    ic += yazi(451, 84, 'tutunan yıldız topluluklarıdır.', 11.5, LAC, ince=True)
    ic += yazi(451, 102, 'Onlarca ile milyonlarca yıldız içerir.', 11, YESIL_K)
    return svg(600, 120, ic, '1. Kart: Takımyıldız (yakın görünen şekil), 2. Kart: Yıldız Kümesi (kütle çekimiyle bağlı topluluk).', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yildiz_boyutlari()
    s[4]['gorsel'] = renk_sicaklik_kartlari()
    s[5]['gorsel'] = gok_bilimi_kartlari()
    s[6]['gorsel'] = buyukayi_haritasi()
    s[7]['gorsel'] = buyukluk_basamaklari()
    s[8]['gorsel'] = yildiz_kaymasi_sema()
    s[9]['gorsel'] = galaksi_olcek()
    s[10]['gorsel'] = isik_yili_olcek()
    s[12]['gorsel'] = takimyildiz_kume_kart()
