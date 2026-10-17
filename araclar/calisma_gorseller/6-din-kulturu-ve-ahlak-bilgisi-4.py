"""6. sınıf DKAB 4. hafta (vahiy: rehberlik, Pusulamız Vahiy, ayetlerden çıkarım) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048); görsel içi yazı sayfa puntosunda (K150 EK: 13 birim ≈ gövde, 12 ≈ tablo puntosu); ayet levhası yok (K055)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=13, renk=LAC, hiza='start', ara=16):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def numara(x, y, n, renk=LAC, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4.3, str(n), 11.5, '#fff')


def ok(x1, y1, x2, y2, renk=SOLUK, kalin=2):
    a = math.atan2(y2 - y1, x2 - x1)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    bx, by = x2 - 7 * ux, y2 - 7 * uy
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<path d="M{bx + 5 * px:.1f} {by + 5 * py:.1f} L{x2:.1f} {y2:.1f} L{bx - 5 * px:.1f} {by - 5 * py:.1f} Z" fill="{renk}"/>')


def roller():
    """Peygamberlerin rolleri çarkı: beş dilim dolu, biri boş (önce dilimler, sonra etiketler)."""
    cx, cy, r1, r2 = 180, 66, 26, 62
    roller_ = ['Kul', 'Yönetici', 'Komşu', 'Baba', 'Eş', '?']
    renkler = [MAVI, YES, TUR, MOR, CAM, TUR]
    ic, etiket = '', ''
    for i, (ad, renk) in enumerate(zip(roller_, renkler)):
        a0, a1 = math.radians(-90 + i * 60 + 2), math.radians(-90 + (i + 1) * 60 - 2)
        p = [(cx + r1 * math.cos(a0), cy + r1 * math.sin(a0)), (cx + r2 * math.cos(a0), cy + r2 * math.sin(a0)),
             (cx + r2 * math.cos(a1), cy + r2 * math.sin(a1)), (cx + r1 * math.cos(a1), cy + r1 * math.sin(a1))]
        bos = ad == '?'
        d = (f'M{p[0][0]:.1f} {p[0][1]:.1f} L{p[1][0]:.1f} {p[1][1]:.1f} A{r2} {r2} 0 0 1 {p[2][0]:.1f} {p[2][1]:.1f} '
             f'L{p[3][0]:.1f} {p[3][1]:.1f} A{r1} {r1} 0 0 0 {p[0][0]:.1f} {p[0][1]:.1f} Z')
        kesik = ' stroke-dasharray="5 4"' if bos else ''
        ic += f'<path d="{d}" fill="{"#fff" if bos else renk}" stroke="{renk}" stroke-width="{1.6 if bos else 0}"{kesik}/>'
        am = math.radians(-90 + i * 60 + 30)
        tx, ty = cx + (r1 + r2) / 2 * math.cos(am), cy + (r1 + r2) / 2 * math.sin(am)
        etiket += yazi(tx, ty + 4.5, ad, 12 if len(ad) < 7 else 10, TUR if bos else '#fff')
    ic += etiket + f'<circle cx="{cx}" cy="{cy}" r="{r1 - 2}" fill="{LAC}"/>' + yazi(cx, cy + 4, 'Roller', 11, '#fff')
    ic += duz(6, 34, ['Peygamberler', 'hayatın her', 'rolünde', 'örnek oldu.'], 12.5, LAC, 'start', 15)
    ic += duz(256, 34, ['Toplumsal', 'sorunlara', 'çözüm', 'aradılar.'], 12.5, LAC, 'start', 15)
    return svg(360, 132, ic, 'Altı dilimli çark: Kul, Yönetici, Komşu, Baba, Eş ve soru işaretli boş dilim; ortada Roller yazısı. Yanlarda notlar: Peygamberler hayatın her rolünde örnek oldu. Toplumsal sorunlara çözüm aradılar.', 33)


def kilcik():
    """Balık kılçığı diyagramı (altı başlık) ve altında altı numaralı cevap kartı (iki sütun)."""
    ic = kutu(4, 32, 92, 36, LAC, LAC, 8) + duz(50, 47, ['Vahyin getirdikleri', 'nelerdir?'], 11, '#fff', 'middle', 13)
    ic += f'<line x1="96" y1="50" x2="298" y2="50" stroke="{SOLUK}" stroke-width="2.4"/>'
    ic += kutu(298, 36, 58, 28, TUR_A, TUR, 6, 1.4) + yazi(327, 54, 'Ana fikir', 11.5, TUR)
    ust = ['ahlak', 'aile', 'bilim']
    alt = ['toplumsal düzen', 'inanç', 'hukuk']
    for k, (u, a) in enumerate(zip(ust, alt)):
        x = 140 + k * 60
        ic += f'<line x1="{x}" y1="50" x2="{x - 16}" y2="18" stroke="{SOLUK}" stroke-width="1.6"/><line x1="{x}" y1="50" x2="{x - 16}" y2="82" stroke="{SOLUK}" stroke-width="1.6"/>'
        ic += kutu(x - 44, 4, 56, 18, MAVI_A, MAVI, 5, 1.2) + yazi(x - 16, 17, u, 11.5, MAVI)
        if k == 0:
            ic += kutu(x - 62, 78, 92, 18, YES_A, YES, 5, 1.2) + yazi(x - 16, 91, a, 11, YES)
        else:
            ic += kutu(x - 44, 78, 56, 18, YES_A, YES, 5, 1.2) + yazi(x - 16, 91, a, 11.5, YES)
    kartlar = ['Doğru sözlü olmak', 'Anne babaya saygı', 'Evreni gözlemleyip düşünmek', 'Haksızlık yapmamak', 'Allah’a inanmak', 'Komşularla yardımlaşmak']
    for i, m in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 104 + (i // 2) * 26
        ic += kutu(x, y, 172, 22, KUM, GRI, 5, 1.1) + numara(x + 12, y + 11, i + 1, LAC, 8) + yazi(x + 96, y + 15.5, m, 11.5, LAC)
    return svg(360, 182, ic, 'Balık kılçığı diyagramı: baş kısmında Vahyin getirdikleri nelerdir sorusu; üst kılçıklar ahlak, aile, bilim; alt kılçıklar toplumsal düzen, inanç, hukuk; kuyrukta Ana fikir. Altında numaralı kartlar: 1 Doğru sözlü olmak, 2 Anne babaya saygı, 3 Evreni gözlemleyip düşünmek, 4 Haksızlık yapmamak, 5 Allah’a inanmak, 6 Komşularla yardımlaşmak.', 46)


def levhalar():
    """Uyarı (üçgen) ve müjde (yeşil) levhaları solda; dört numaralı ifade sağda."""
    ic = f'<path d="M40 8 L72 62 H8 Z" fill="{KIR_A}" stroke="{KIR}" stroke-width="2.2" stroke-linejoin="round"/>'
    ic += yazi(40, 54, '!', 24, KIR) + yazi(40, 80, 'Uyarı', 12.5, KIR)
    ic += kutu(84, 14, 62, 48, YES_A, YES, 10, 2.2)
    nok = ' '.join(f'{115 + (12 if k % 2 == 0 else 5) * math.cos(math.radians(-90 + k * 36)):.1f},{38 + (12 if k % 2 == 0 else 5) * math.sin(math.radians(-90 + k * 36)):.1f}' for k in range(10))
    ic += f'<polygon points="{nok}" fill="{YES}"/>' + yazi(115, 80, 'Müjde', 12.5, YES)
    ifadeler = [['Kulak asmayanları bekleyen', 'sonucu gösterir.'], ['Güzel işlerin karşılığının', 'cennet olduğunu bildirir.'],
                ['İnsanlar dünya ve ahirette zor', 'duruma düşmesin diye seslenir.'], ['İnanıp iyilik yapanları', 'sevindirir.']]
    for i, m in enumerate(ifadeler):
        x, y = 160, 6 + i * 26
        ic += numara(x + 9, y + 11, i + 1, LAC, 8) + duz(x + 22, y + 8, m, 11, LAC, 'start', 12)
    return svg(360, 110, ic, 'Solda kırmızı üçgen uyarı levhası ve yeşil yıldızlı müjde levhası. Sağda dört numaralı ifade: 1 Kulak asmayanları bekleyen sonucu gösterir. 2 Güzel işlerin karşılığının cennet olduğunu bildirir. 3 İnsanlar dünya ve ahirette zor duruma düşmesin diye seslenir. 4 İnanıp iyilik yapanları sevindirir.', 28)


def tahta():
    """Yeşil tahta: soru ve dört cevap; 1 ile 4 birbirinin benzeri."""
    ic = kutu(4, 4, 352, 126, '#2f6b4f', '#8a5a2b', 6, 3)
    ic += yazi(180, 26, 'Vahyin Getirdikleri Nelerdir?', 13.5, '#fff') + f'<line x1="70" y1="31" x2="290" y2="31" stroke="#fff" stroke-width="1" opacity=".7"/>'
    cevaplar = ['Allah’a nasıl ibadet edeceğimizi öğretir.', 'İyi ve kötü davranışları bildirir.', 'Ailede sevgi ve saygıyı öğütler.', 'İbadetlerin nasıl yapılacağını gösterir.']
    for i, c in enumerate(cevaplar):
        y = 52 + i * 21
        ic += f'<circle cx="24" cy="{y - 4}" r="8" fill="#fff"/>' + yazi(24, y, str(i + 1), 11, '#2f6b4f') + duz(40, y, [c], 12.5, '#fff', 'start')
    ic += f'<rect x="300" y="118" width="44" height="7" rx="2" fill="#e8e3d6"/><rect x="310" y="112" width="26" height="6" rx="2" fill="#f7f3ea"/>'
    return svg(360, 134, ic, 'Yeşil tahta. Başlık: Vahyin Getirdikleri Nelerdir? Cevaplar: 1 Allah’a nasıl ibadet edeceğimizi öğretir. 2 İyi ve kötü davranışları bildirir. 3 Ailede sevgi ve saygıyı öğütler. 4 İbadetlerin nasıl yapılacağını gösterir. Köşede silgi ve tebeşir.', 34)


def pusula():
    """Ece'nin değerlendirme pusulası: dört yön, dört ifade (doğu ile batı yer değiştirmiş)."""
    cx, cy, r = 52, 62, 40
    ic = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{r - 8}" fill="none" stroke="{MAVI}" stroke-width=".8" stroke-dasharray="3 3"/>'
    ic += f'<polygon points="{cx},{cy - 26} {cx + 6},{cy} {cx},{cy + 26} {cx - 6},{cy}" fill="{KIR}"/><polygon points="{cx - 26},{cy} {cx},{cy - 6} {cx + 26},{cy} {cx},{cy + 6}" fill="{SOLUK}"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>' + yazi(cx, cy + 3.5, 'Vahyin', 8, MAVI)
    for h, dx, dy in [('K', 0, -r + 11), ('G', 0, r - 3), ('D', r - 8, 4.5), ('B', -r + 8, 4.5)]:
        ic += yazi(cx + dx, cy + dy, h, 12, LAC)
    satirlar = [('K', 'Bulduğum cüzdanı sahibine verdim.'), ('D', 'Erken kalkmayı hedefledim.'),
                ('G', 'Kardeşime bağırmayı bıraktım.'), ('B', 'Vahyin peygamberle geldiğini öğrendim.')]
    for i, (h, m) in enumerate(satirlar):
        y = 20 + i * 27
        ic += kutu(104, y - 14, 252, 22, KUM, GRI, 5, 1.1) + f'<rect x="108" y="{y - 11}" width="16" height="16" rx="4" fill="{LAC}"/>' + yazi(116, y + 1, h, 11, '#fff')
        ic += duz(130, y + 1, [m], 11.5, LAC, 'start')
    return svg(360, 122, ic, 'Solda pusula: ortada Vahyin yazısı; K kuzey, D doğu, G güney, B batı. Sağda Ece’nin yazdıkları: K Bulduğum cüzdanı sahibine verdim. D Erken kalkmayı hedefledim. G Kardeşime bağırmayı bıraktım. B Vahyin peygamberle geldiğini öğrendim.', 31)


def zincir():
    """Kavram şeması: Allah → akıl(?1) → iyi-kötü; Allah → vahiy → peygamber(?2) → insan; rehberlik → insan → ibadet(?3)."""
    def kart(x, y, w, m, bos=False, renk=MAVI, zemin=MAVI_A, boy=11.5):
        if bos:
            return kutu(x, y, w, 24, '#fff', TUR, 6, 1.4, ' stroke-dasharray="5 4"') + numara(x + 11, y + 12, m, TUR, 8) + yazi(x + w / 2 + 6, y + 17, '?', 14, TUR)
        return kutu(x, y, w, 24, zemin, renk, 6, 1.2) + yazi(x + w / 2, y + 16.5, m, boy, renk)
    ic = kart(4, 4, 56, 'Allah', False, LAC, '#dfe5f5') + ok(60, 16, 76, 16) + kart(78, 4, 70, 1, True) + ok(148, 16, 164, 16)
    ic += kart(166, 4, 190, 'iyi ile kötüyü ayırt eder', False, YES, YES_A)
    ic += kart(4, 40, 56, 'Allah', False, LAC, '#dfe5f5') + ok(60, 52, 76, 52) + kart(78, 40, 56, 'vahiy', False, MOR, MOR_A) + ok(134, 52, 150, 52)
    ic += kart(152, 40, 80, 2, True) + ok(232, 52, 248, 52) + kart(250, 40, 106, 'insan', False, CAM, CAM_A)
    ic += kart(4, 76, 150, 'rehberlik, yol göstericilik', False, MOR, MOR_A) + ok(154, 88, 170, 88) + kart(172, 76, 56, 'insan', False, CAM, CAM_A) + ok(228, 88, 244, 88)
    ic += kart(246, 76, 110, 3, True)
    ic += yazi(301, 118, 've görevlerini öğrenir', 11.5, SOLUK)
    return svg(360, 124, ic, 'Üç satırlı kavram şeması. 1. satır: Allah, ok, 1 numaralı soru işaretli boş kutu, ok, iyi ile kötüyü ayırt eder. 2. satır: Allah, ok, vahiy, ok, 2 numaralı boş kutu, ok, insan. 3. satır: rehberlik, yol göstericilik, ok, insan, ok, 3 numaralı boş kutu; altında ve görevlerini öğrenir.', 31)


def not_karti():
    """Arkadaşın yapışkan notu."""
    ic = f'<g transform="rotate(-2 180 36)">' + kutu(60, 6, 240, 58, '#fff6b0', '#e2cf5c', 3, 1.2)
    ic += f'<rect x="150" y="0" width="60" height="12" rx="2" fill="{GRI}" opacity=".55"/>'
    ic += yazi(180, 32, 'Aklım varken', 13.5, LAC) + yazi(180, 52, 'vahye ne gerek var?', 13.5, LAC) + '</g>'
    return svg(360, 70, ic, 'Yapışkan not: Aklım varken vahye ne gerek var?', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = roller()
    s[1]['gorsel'] = kilcik()
    s[3]['gorsel'] = levhalar()
    s[5]['gorsel'] = tahta()
    s[7]['gorsel'] = pusula()
    s[8]['gorsel'] = zincir()
    s[9]['gorsel'] = not_karti()
