"""9. sınıf Tarih 1. hafta (tarih öğrenmenin faydaları) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def ok(x1, y1, x2, y2, renk=GRI, kalin=1.8):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/><polygon points="{u}" fill="{renk}"/>'


def yildiz(x, y, r, renk=ALTIN):
    p = ' '.join(f'{x + (r if k % 2 == 0 else r * 0.45) * math.cos(-math.pi / 2 + k * math.pi / 5):.1f},{y + (r if k % 2 == 0 else r * 0.45) * math.sin(-math.pi / 2 + k * math.pi / 5):.1f}' for k in range(10))
    return f'<polygon points="{p}" fill="{renk}"/>'


SU = '#5aa9e6'


def satir_kartlari(kart, etiket, en_fazla):
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 4 + len(kart) * 29, ic, etiket, en_fazla)


def eser_kartlari():
    ic = ''
    metin = [['Lidya Kralı Kroisos’a', 'ait altın broş; önü at,', 'arkası balık biçiminde.'], ['Roma Dönemi’nde', 'Zeugma’daki villaları', 'süsleyen mozaik.']]
    for i, (c, d) in enumerate([(TUR, TUR_A), (MOR, MOR_A)]):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 66, d, c, 8, 1.3) + rozet(x + 15, 18, 'AB'[i], c) + ''.join(yazi(x + 50, 26 + k * 15, s, 10.2, LAC, 'start', True) for k, s in enumerate(metin[i]))
    ic += f'<circle cx="28" cy="46" r="13" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1"/><path d="M20 48 q4 -12 12 -8 q-2 6 4 10 q-8 4 -16 -2 Z" fill="#fff6cf" stroke="{KAHVE}" stroke-width="0.8"/>'
    renk = ['#c9a27a', '#8a5a2b', '#e6d3b3', '#a9744a', '#f2e6d0']
    ic += ''.join(f'<rect x="{196 + (k % 5) * 6}" y="{32 + (k // 5) * 6}" width="5.4" height="5.4" fill="{renk[(k * 7 + k // 5) % 5]}"/>' for k in range(25))
    return svg(360, 74, ic, 'Kart A: Lidya Kralı Kroisos’a ait altın broş; önü at, arkası balık biçiminde. Kart B: Roma Dönemi’nde Zeugma’daki villaları süsleyen mozaik.', 19)


def zincir():
    ad = [['Tarihi', 'bilmek'], ['Ortak', 'değerler'], None, ['Toplumun', 'oluşması']]
    ic = ''
    for i, a in enumerate(ad):
        x = 6 + i * 90
        bos = a is None
        ic += kutu(x, 6, 76, 40, '#fff' if bos else MAVI_A, TUR if bos else MAVI, 8, 1.4, ' stroke-dasharray="4 3"' if bos else '')
        ic += yazi(x + 38, 32, '?', 15, TUR) if bos else ''.join(yazi(x + 38, 23 + k * 13, s, 11, LAC) for k, s in enumerate(a))
        if i < 3:
            ic += ok(x + 77, 26, x + 89, 26)
    return svg(360, 52, ic, 'Şema: tarihi bilmek, ortak değerler, soru işareti, toplumun oluşması', 12)


def deprem_kartlari():
    ic = ''
    veri = [('27 Aralık 1939 · Erzincan', ['Depremden sonra bütün yurtta', 'yardım kampanyası başlatıldı.']), ('6 Şubat 2023 · Kahramanmaraş', ['Depremlerden sonra halk', 'topyekûn seferber oldu.'])]
    for i, (b, m) in enumerate(veri):
        x = 4 + i * 180
        ic += kutu(x, 4, 172, 64, KIR_A, KIR, 8, 1.3) + f'<rect x="{x}" y="4" width="172" height="20" rx="8" fill="{KIR}"/><rect x="{x}" y="14" width="172" height="10" fill="{KIR}"/>' + yazi(x + 86, 18.5, b, 9.6, '#fff')
        ic += ''.join(yazi(x + 86, 41 + k * 15, s, 10.5, LAC, 'middle', True) for k, s in enumerate(m))
    return svg(360, 72, ic, 'İki olay: 27 Aralık 1939 Erzincan depreminden sonra bütün yurtta yardım kampanyası başlatıldı. 6 Şubat 2023 Kahramanmaraş depremlerinden sonra halk topyekûn seferber oldu.', 18)


def fayda_kartlari():
    return satir_kartlari([('A', 'Kişinin bakış açısı genişler.', MAVI, MAVI_A), ('B', 'Ortak kimlik oluşur.', KIR, KIR_A),
                           ('C', 'Empati kurma becerisi gelişir.', YES, YES_A), ('D', 'Kültürel miras korunur.', TUR, TUR_A)],
                          'Kartlar: A Kişinin bakış açısı genişler. B Ortak kimlik oluşur. C Empati kurma becerisi gelişir. D Kültürel miras korunur.', 30)


def soru_listesi():
    s = ['Olay hangi dönemde yaşandı?', 'O dönemin koşulları nasıldı?', 'Başka nedenleri ve sonuçları olabilir mi?', 'Olaya farklı bakan görüşler var mı?']
    ic = kutu(4, 4, 352, 84, '#fffdf5', KAHVE, 8, 1.4)
    for k, a in enumerate(s):
        y = 22 + k * 19
        ic += f'<circle cx="18" cy="{y - 4}" r="3.2" fill="{TUR}"/>' + yazi(28, y, a, 11.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Sorular: Olay hangi dönemde yaşandı? O dönemin koşulları nasıldı? Başka nedenleri ve sonuçları olabilir mi? Olaya farklı bakan görüşler var mı?', 22)


def hizmet():
    ic = kutu(4, 4, 352, 66, '#fff', SOLUK, 8, 1.4) + f'<rect x="4" y="4" width="352" height="18" rx="8" fill="{GRI_A}"/>'
    ic += ''.join(f'<circle cx="{16 + k * 11}" cy="13" r="3" fill="{c}"/>' for k, c in enumerate([KIR, ALTIN, YES]))
    ic += yazi(180, 40, 'Alt-Üst Soy Raporu', 13, LAC) + yazi(180, 58, 'Talep çok yoğun. Bekleme süresi uzamıştır.', 10.5, SOLUK, 'middle', True)
    return svg(360, 74, ic, 'Hizmet ekranı: Alt-Üst Soy Raporu. Talep çok yoğun. Bekleme süresi uzamıştır.', 18)


def abide():
    ic = f'<rect x="4" y="4" width="352" height="104" rx="8" fill="#dff1fd"/><path d="M4 96 H356 V100 a8 8 0 0 1 -8 8 H12 a8 8 0 0 1 -8 -8 Z" fill="#cfe8b9"/>'
    ic += f'<rect x="120" y="84" width="120" height="12" fill="#c9c2b2" stroke="{SOLUK}" stroke-width="1"/>'
    for x in (150, 190):
        ic += f'<rect x="{x}" y="34" width="14" height="50" fill="#b9b1a0" stroke="{SOLUK}" stroke-width="0.8"/>'
    for x in (132, 214):
        ic += f'<rect x="{x}" y="30" width="18" height="54" fill="#e9e3d6" stroke="{SOLUK}" stroke-width="1"/>'
    ic += f'<rect x="124" y="16" width="112" height="16" fill="#e9e3d6" stroke="{SOLUK}" stroke-width="1"/>'
    return svg(360, 112, ic, 'Çanakkale Şehitler Abidesi çizimi: bir kaide üzerinde dört sütun ve üstünde düz bir tavan', 24)


def notlar():
    """İki öğrencinin kervansaray notu: tek nedenli ve çok yönlü değerlendirme."""
    ic = yazi(180, 16, 'Konu: Anadolu Selçuklu kervansaraylarının yapılması', 11.5, LAC)
    kart = [(4, 'Ece’nin notu', TUR, TUR_A, ['Sultan çok zengindi.', 'Bu yüzden yollara', 'kervansaray yaptırdı.']),
            (184, 'Kaan’ın notu', MAVI, MAVI_A, ['Yollar güvenli değildi.', 'Tüccarlar konaklayacak', 'yer arıyordu. Han da', 'yolcuları buluşturuyordu.'])]
    for x, bas, c, d, satir in kart:
        ic += kutu(x, 26, 172, 90, d, c, 6, 1.3) + yazi(x + 86, 44, bas, 11.5, c)
        ic += ''.join(yazi(x + 12, 64 + k * 15, t, 11, LAC, 'start', True) for k, t in enumerate(satir))
    return svg(360, 120, ic, 'Konu: Anadolu Selçuklu kervansaraylarının yapılması. Ece’nin notu: Sultan çok zengindi. Bu yüzden yollara kervansaray yaptırdı. Kaan’ın notu: Yollar güvenli değildi. Tüccarlar konaklayacak yer arıyordu. Han da yolcuları buluşturuyordu.', 28)


def baris():
    """Hiroşima: 1945 yıkım, yalnız bir yapı ayakta; bugün barış anıtı. Zaman şeridi + kubbe iskeleti."""
    ic = f'<line x1="20" y1="104" x2="340" y2="104" stroke="{GRI}" stroke-width="2"/>'
    for x, yil, ust, alt in [(70, '1945', 'Kente atom bombası atılır.', 'Yalnız bu yapı ayakta kalır.'), (290, 'Bugün', 'Yapı onarılmadan', 'barış anıtı olarak korunur.')]:
        ic += f'<circle cx="{x}" cy="104" r="6" fill="{KIR if yil == "1945" else YES}"/>' + yazi(x, 122, yil, 12, LAC)
        ic += yazi(x, 138, ust, 10.5, SOLUK, 'middle', True) + yazi(x, 152, alt, 10.5, SOLUK, 'middle', True)
    ic += f'<rect x="150" y="56" width="60" height="38" fill="#e9e3d6" stroke="{SOLUK}" stroke-width="1.2"/>'
    ic += ''.join(f'<rect x="{156 + 13 * k}" y="66" width="7" height="12" fill="{GRI}"/>' for k in range(4))
    ic += f'<path d="M160 56 Q180 20 200 56" fill="none" stroke="{SOLUK}" stroke-width="2"/><line x1="180" y1="30" x2="180" y2="56" stroke="{SOLUK}" stroke-width="1.6"/><path d="M168 56 Q180 34 192 56" fill="none" stroke="{SOLUK}" stroke-width="1.4"/>'
    ic += f'<path d="M150 94 l6 -8 l8 6 l6 -6" fill="none" stroke="{KAHVE}" stroke-width="1.2"/>'
    return svg(360, 158, ic, 'Zaman şeridi: 1945, kente atom bombası atılır, yalnız bu yapı ayakta kalır. Bugün, yapı onarılmadan barış anıtı olarak korunur. Ortada kubbesinin yalnız iskeleti kalmış yapı çizimi.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = eser_kartlari()
    s[2]['gorsel'] = zincir()
    s[3]['gorsel'] = deprem_kartlari()
    s[5]['gorsel'] = fayda_kartlari()
    s[7]['gorsel'] = soru_listesi()
    s[8]['gorsel'] = hizmet()
    s[9]['gorsel'] = abide()
    s[12]['gorsel'] = notlar()
    s[13]['gorsel'] = baris()
