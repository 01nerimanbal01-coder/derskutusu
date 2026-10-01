"""6. sınıf İngilizce 2. hafta (Revision 1: school places, times, family, routines, clothes) çalışma kâğıdı görselleri (SVG; insan figürü yok)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, SARI_A = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fff6c2'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def okul_plani():
    """Okul planı: 1 kütüphane, 2 laboratuvar, kantin + salon; dışarıda 3 basketbol sahası."""
    ic = kutu(4, 4, 232, 92, '#fff', LAC, 4, 1.6) + yazi(120, 16, 'SCHOOL · first floor', 10.5, LAC)
    odalar = [(8, 22, 70, 34, 'library', MAVI_A, MAVI), (82, 22, 70, 34, 'lab', YES_A, YES), (156, 22, 76, 34, 'lab', YES_A, YES),
              (8, 60, 110, 32, 'canteen', TUR_A, TUR), (122, 60, 110, 32, 'hall', MOR_A, MOR)]
    for x, y, w, h, ad, dolgu, cizgi in odalar:
        ic += kutu(x, y, w, h, dolgu, cizgi, 2, 1.2) + yazi(x + w / 2, y + h / 2 + 4, ad, 10.5, LAC)
    for i in range(3):  # sahalar
        x = 246 + i * 38
        ic += kutu(x, 30, 32, 50, '#dff0e5', YES, 2, 1.2) + f'<circle cx="{x + 16}" cy="55" r="5" fill="none" stroke="{YES}" stroke-width="1.2"/><line x1="{x}" y1="55" x2="{x + 32}" y2="55" stroke="{YES}" stroke-width="1"/>'
    ic += yazi(303, 92, 'basketball courts', 10, YES)
    return svg(360, 100, ic, 'Okul planı: kütüphane, iki laboratuvar, kantin ve salon; dışarıda üç basketbol sahası', 22)


def zil_cizelgesi():
    """Zil çizelgesi: Lesson 1 08:40, Break 09:20, Lesson 2 09:30, Lunch 12:00."""
    ic = yazi(180, 13, 'Bell schedule', 11.5, LAC)
    for i, (ad, saat, renk, acik) in enumerate([('Lesson 1', '08:40', MAVI, MAVI_A), ('Break', '09:20', TUR, TUR_A), ('Lesson 2', '09:30', MAVI, MAVI_A), ('Lunch', '12:00', YES, YES_A)]):
        x0 = 6 + i * 88
        ic += kutu(x0, 20, 82, 44, acik, renk, 6, 1.2) + yazi(x0 + 41, 36, ad, 11, renk) + yazi(x0 + 41, 56, saat, 14, LAC)
    return svg(360, 68, ic, 'Zil çizelgesi: Lesson 1 08:40, Break 09:20, Lesson 2 09:30, Lunch 12:00', 15)


def aile_notlari():
    """Ela'nın aile notları: üç yapışkan not."""
    notlar = [('Mum', ['medium height', 'curly hair', 'loves fancy outfits'], SARI_A, ALTIN), ('Dad', ['tall', 'good at cooking'], MAVI_A, MAVI), ('Brother', ['short straight hair', 'T-shirt and sneakers'], YES_A, YES)]
    ic = yazi(180, 13, "Ela's family", 11.5, LAC)
    for i, (kim, satirlar, dolgu, cizgi) in enumerate(notlar):
        x0 = 6 + i * 118
        ic += kutu(x0, 20, 112, 74, dolgu, cizgi, 3, 1.2) + f'<rect x="{x0 + 42}" y="16" width="28" height="8" rx="2" fill="{cizgi}" opacity="0.6"/>' + yazi(x0 + 56, 40, kim, 11.5, LAC)
        for k, m in enumerate(satirlar):
            ic += yazi(x0 + 56, 56 + k * 14, m, 10.5, LAC, 'middle', True)
    return svg(360, 100, ic, "Ela'nın aile notları: Mum medium height, curly hair, loves fancy outfits; Dad tall, good at cooking; Brother short straight hair, T-shirt and sneakers", 22)


def piknik_kartlari():
    """Piknik kartları: Dad mangal, Mum sandviç, Sister uçurtma, Grandma kitap."""
    ic = ''
    for i, (kim, renk, acik) in enumerate([('Dad', KIR, KIR_A), ('Mum', TUR, TUR_A), ('Sister', MAVI, MAVI_A), ('Grandma', MOR, MOR_A)]):
        x0 = 4 + i * 89; cx = x0 + 42
        ic += kutu(x0, 4, 84, 70, acik, renk, 8, 1.2) + yazi(cx, 19, kim, 11.5, renk) + yazi(cx, 69, 'now', 9.5, SOLUK, 'middle', True)
        if i == 0:  # mangal
            ic += f'<rect x="{cx - 16}" y="36" width="32" height="10" rx="3" fill="{LAC}"/><path d="M{cx - 12} 46 l-4 12 M{cx + 12} 46 l4 12" stroke="{LAC}" stroke-width="2"/>' + ''.join(f'<path d="M{cx + dx} 34 q3 -6 0 -10" fill="none" stroke="{KIR}" stroke-width="1.6"/>' for dx in (-8, 0, 8))
        elif i == 1:  # sandviç
            ic += f'<path d="M{cx - 16} 40 h32 v-4 a16 8 0 0 0 -32 0 z" fill="#e0a860"/><rect x="{cx - 16}" y="40" width="32" height="5" fill="{YES}"/><rect x="{cx - 16}" y="45" width="32" height="4" fill="{KIR}"/><rect x="{cx - 16}" y="49" width="32" height="7" rx="2" fill="#e0a860"/>'
        elif i == 2:  # uçurtma
            ic += f'<path d="M{cx} 24 L{cx + 11} 37 L{cx} 50 L{cx - 11} 37 Z" fill="{MAVI}"/><path d="M{cx} 24 V50 M{cx - 11} 37 H{cx + 11}" stroke="#fff" stroke-width="1"/><path d="M{cx} 50 q-5 3 -2 5 q3 2 -2 3" fill="none" stroke="{LAC}" stroke-width="1.2"/>'
        else:  # kitap
            ic += f'<path d="M{cx - 18} 32 h16 v26 h-16 z M{cx + 2} 32 h16 v26 h-16 z" fill="#fff" stroke="{MOR}" stroke-width="1.6"/><path d="M{cx - 2} 32 v26" stroke="{MOR}" stroke-width="2"/>' + ''.join(f'<line x1="{cx - 14}" y1="{y}" x2="{cx - 6}" y2="{y}" stroke="{GRI}" stroke-width="1"/><line x1="{cx + 6}" y1="{y}" x2="{cx + 14}" y2="{y}" stroke="{GRI}" stroke-width="1"/>' for y in (39, 45, 51))
    return svg(360, 78, ic, 'Piknik kartları (şu an): Dad mangal, Mum sandviç, Sister uçurtma, Grandma kitap', 18)


def duyuru():
    """Duyuru: MUSIC CLUB, every Friday, 4:00 p.m., music room, bring your instrument."""
    ic = kutu(60, 4, 240, 92, '#fff', MOR, 6, 1.6) + f'<rect x="60" y="4" width="240" height="24" rx="6" fill="{MOR}"/><rect x="60" y="18" width="240" height="10" fill="{MOR}"/>' + yazi(180, 21, 'MUSIC CLUB', 13, '#fff')
    ic += f'<circle cx="180" cy="4" r="4" fill="{KIR}"/>'
    for k, m in enumerate(['every Friday', '4:00 p.m. · music room', 'Bring your instrument!']):
        ic += yazi(180, 46 + k * 17, m, 11.5, LAC, 'middle', k != 2)
    return svg(360, 100, ic, 'Duyuru: Music club, every Friday, 4:00 p.m., music room, bring your instrument', 20)


def canta():
    """Piknik çantası: şapka, güneş gözlüğü, yağmurluk, spor ayakkabı (ad yok)."""
    ic = f'<path d="M20 30 h320 l-12 62 h-296 z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/><path d="M150 30 v-10 a30 10 0 0 1 60 0 v10" fill="none" stroke="{TUR}" stroke-width="3"/>'
    # şapka
    ic += f'<path d="M50 60 a18 14 0 0 1 36 0 z" fill="{KIR}"/><path d="M50 60 h54 l4 6 h-58 z" fill="{KIR}"/>'
    # güneş gözlüğü
    ic += f'<circle cx="138" cy="60" r="11" fill="{LAC}"/><circle cx="168" cy="60" r="11" fill="{LAC}"/><path d="M149 58 h8 M127 56 l-8 -6 M179 56 l8 -6" stroke="{LAC}" stroke-width="2.4"/>'
    # yağmurluk
    ic += f'<path d="M212 50 l-8 26 h7 l3 -14 z M260 50 l8 26 h-7 l-3 -14 z" fill="{ALTIN}" stroke="#c9960a" stroke-width="1.2"/><path d="M222 42 h28 l10 8 v30 h-48 v-30 z" fill="{ALTIN}" stroke="#c9960a" stroke-width="1.2"/><path d="M236 42 v38 M226 42 a10 9 0 0 1 20 0" fill="none" stroke="#c9960a" stroke-width="1.4"/>'
    # spor ayakkabı
    ic += f'<path d="M286 72 h48 v6 h-48 z" fill="{LAC}"/><path d="M286 72 v-14 q0 -6 6 -6 h10 l12 12 h20 v8 z" fill="{MAVI}"/><path d="M296 56 l6 6 M302 54 l6 6" stroke="#fff" stroke-width="1.4"/>'
    return svg(360, 100, ic, 'Piknik çantası: şapka, güneş gözlüğü, yağmurluk, spor ayakkabı', 20)


def gezi_kaydi():
    """Gezi kaydı: bu yıl 5 okul gezisi, Deniz hepsine katıldı (yeşil onay)."""
    ic = yazi(180, 13, 'School trips this year · Deniz', 11.5, LAC)
    for i in range(5):
        x0 = 6 + i * 70
        ic += kutu(x0, 20, 64, 40, YES_A, YES, 6, 1.2) + yazi(x0 + 32, 34, f'Trip {i + 1}', 10.5, LAC) + f'<circle cx="{x0 + 32}" cy="49" r="7" fill="{YES}"/><path d="M{x0 + 28} 49 l3 3 l5 -6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    return svg(360, 66, ic, 'Gezi kaydı: bu yıl beş okul gezisi, Deniz hepsine katıldı', 15)


def uye_karti():
    """Kulüp üye kartı: Ada; tall and slim, long wavy hair, hazel eyes; home: a house with a big garden (fotoğraf yeri boş)."""
    ic = kutu(30, 4, 300, 92, '#fff', CAM, 8, 1.6) + f'<rect x="30" y="4" width="300" height="20" rx="8" fill="{CAM}"/><rect x="30" y="14" width="300" height="10" fill="{CAM}"/>' + yazi(180, 18, 'NATURE CLUB · MEMBER CARD', 11, '#fff')
    ic += kutu(40, 32, 54, 54, GRI_A, GRI, 4, 1.2) + f'<rect x="55" y="52" width="24" height="16" rx="3" fill="none" stroke="{SOLUK}" stroke-width="1.6"/><circle cx="67" cy="60" r="4" fill="none" stroke="{SOLUK}" stroke-width="1.6"/>'
    satirlar = [('Name:', 'Ada Demir'), ('Looks:', 'tall and slim, long wavy hair'), ('Eyes:', 'hazel'), ('Home:', 'a house with a big garden')]
    for k, (a, b) in enumerate(satirlar):
        y = 44 + k * 14
        ic += yazi(104, y, a, 10.5, CAM, 'start') + yazi(150, y, b, 10.5, LAC, 'start', True)
    return svg(360, 100, ic, 'Kulüp üye kartı: Ada Demir; tall and slim, long wavy hair, hazel eyes; evinde büyük bahçe', 21)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = okul_plani()
    s[1]['gorsel'] = zil_cizelgesi()
    s[3]['gorsel'] = aile_notlari()
    s[5]['gorsel'] = piknik_kartlari()
    s[9]['gorsel'] = duyuru()
    s[11]['gorsel'] = uye_karti()
    s[12]['gorsel'] = canta()
    s[13]['gorsel'] = gezi_kaydi()
