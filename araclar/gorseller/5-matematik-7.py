"""5. sınıf Matematik, 7. hafta: çokgenler ve çember — merkez, yarıçap, çap; iki noktada kesişen çember çifti; merkezler ve
bir kesişim noktasıyla kurulan üçgen; kenar uzunluklarına göre üçgen çeşitleri; dinamik yazılımda sürükleyerek inceleme.

Görseller yalnız özet metnindeki (araclar/ozetler/5-matematik-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: mavi = A merkezli çember ve onun yarıçapı (|AK|, |AL|, |AC|); mor = B merkezli çember ve onun yarıçapı (|BC|);
turuncu = merkezler arasındaki uzaklık |AB| (üçgenin tabanı; sürüklemede değişen kenar); yeşil = ortaya çıkan eşkenar üçgen;
gri = çap, sonradan eklenen çemberler ve açıklama kutusu çerçevesi.
Ölçek: 1. görsel ölçeksiz (yarıçap r, çap 2r); 2. görselde 1 cm = 32 birim uzunluk (yarıçaplar 3 cm, |AB| = 4 cm);
3. görselde yazılımın 1 birimi = 12 uzunluk; 4. görselde yedi çemberin yarıçapı da eşittir (ölçeksiz, r = 56 uzunluk).
Çember kesişimleri ve üçgen köşeleri koordinatla hesaplanır; yazılar kenarların orta noktasından dik doğrultuda ötelenir.
"""
import math

from ozet_gorsel import svg


def _nk(cx, cy, r, aci):
    """Merkezi (cx, cy) olan çember üzerinde, saat yönünün tersine ölçülen aci (derece) noktası."""
    t = math.radians(aci)
    return cx + r * math.cos(t), cy - r * math.sin(t)


def _kesisim(a, b, r1, r2):
    """Merkezleri a ve b, yarıçapları r1 ve r2 olan çemberlerin kesişim noktaları (üstteki, alttaki)."""
    d = math.hypot(b[0] - a[0], b[1] - a[1])
    k = (d * d + r1 * r1 - r2 * r2) / (2 * d)          # a'dan AB doğrultusunda kiriş ortasına uzaklık
    h = math.sqrt(r1 * r1 - k * k)                      # kiriş ortasından kesişim noktasına dik uzaklık
    px, py = a[0] + k * (b[0] - a[0]) / d, a[1] + k * (b[1] - a[1]) / d
    ux, uy = -(b[1] - a[1]) / d, (b[0] - a[0]) / d      # AB'ye dik birim vektör
    return (px - h * ux, py - h * uy), (px + h * ux, py + h * uy)


def _cizgi(a, b, sinif, kalin=3, ek=''):
    return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="{sinif}" stroke-width="{kalin}" '
            f'stroke-linecap="round"{ek}/>')


def _cember(p, r, sinif, kalin=2.5):
    return f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r:.1f}" class="{sinif}" stroke-width="{kalin}"/>'


def _nokta(p, sinif='g-y', r=4.5):
    return f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" class="{sinif}"/>'


def _yazi(x, y, metin, boy=13, sinif='g-y', hiza='middle', kalin=''):
    k = f' font-weight="{kalin}"' if kalin else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _kutu(x, y, w, h, dolgu, cizgi, rx=10, kalin=1.8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{dolgu}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cizgi}" stroke-width="{kalin}"/>')


def _kenar_yazi(p, q, karsi, metin, sinif, uzak=22, boy=13):
    """p–q kenarının orta noktasından, karşı köşenin ters yönünde (üçgenin dışına) uzak birim ötede yazı."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    uz = math.hypot(dx, dy)
    nx, ny = -dy / uz, dx / uz
    if (karsi[0] - mx) * nx + (karsi[1] - my) * ny > 0:
        nx, ny = -nx, -ny
    return _yazi(mx + uzak * nx, my + uzak * ny + 4.5, metin, boy, sinif, 'middle', 700)


def cember_merkez_yaricap_cap():
    """Merkezi A olan çember: AK ve AL yarıçapları (r), MN çapı (2r); bütün yarıçaplar eşittir."""
    A, r = (126, 122), 88
    K, L = _nk(*A, r, 50), _nk(*A, r, 215)
    M, N = (A[0] - r, A[1]), (A[0] + r, A[1])
    ic = _cember(A, r, 'g-ms', 2.5)
    ic += _cizgi(M, N, 'g-c', 3)                                   # çap
    ic += _cizgi(A, L, 'g-ms', 2, ' stroke-dasharray="5 4"')       # ikinci yarıçap
    ic += _cizgi(A, K, 'g-ms', 3.5)                                # yarıçap
    for p in (M, N, L):
        ic += _nokta(p, 'g-y', 4)
    ic += _nokta(K, 'g-mf', 4.5) + _nokta(A, 'g-y', 4.5)
    ic += _yazi(134, 141, 'A', 14, kalin=800)
    kx, ky = _nk(*A, r + 16, 50)
    ic += _yazi(kx, ky + 5, 'K', 14, kalin=800)
    lx, ly = _nk(*A, r + 18, 215)
    ic += _yazi(lx, ly + 5, 'L', 14, kalin=800)
    ic += _yazi(M[0] - 12, M[1] + 5, 'M', 14, hiza='end', kalin=800)
    ic += _yazi(N[0] + 12, N[1] + 5, 'N', 14, hiza='start', kalin=800)
    # r yazıları: AK'nin sol üstünde, AL'nin sağ altında (kenara dik 14-16 birim)
    ic += _kenar_yazi(A, K, (A[0] + 40, A[1] + 40), 'r', 'g-mf', uzak=14, boy=14)
    ic += _kenar_yazi(A, L, (A[0] - 40, A[1] - 40), 'r', 'g-mf', uzak=16, boy=14)
    ic += _yazi(82, 112, 'çap = 2r', 13, kalin=700)
    # açıklama
    x0 = 256
    ic += _yazi(x0, 44, 'Merkezi A olan çember', 14, hiza='start', kalin=800)
    ic += _cizgi((x0, 70), (x0 + 18, 70), 'g-ms', 3.5) + _nokta((x0 + 18, 70), 'g-mf', 3.5)
    ic += _yazi(x0 + 28, 74, 'Yarıçap: |AK| = r', 13, 'g-mf', 'start', 700)
    ic += _yazi(x0, 92, 'merkezden çemberin', 12, 'g-s', 'start')
    ic += _yazi(x0, 107, 'üzerindeki bir noktaya', 12, 'g-s', 'start')
    ic += _cizgi((x0, 132), (x0 + 18, 132), 'g-c', 3)
    ic += _yazi(x0 + 28, 136, 'Çap: |MN| = 2r', 13, 'g-y', 'start', 700)
    ic += _yazi(x0, 154, 'merkezden geçer, iki ucu', 12, 'g-s', 'start')
    ic += _yazi(x0, 169, 'çemberin üzerinde', 12, 'g-s', 'start')
    ic += _kutu(x0, 186, 176, 42, 'g-ma', 'g-ms')
    ic += _yazi(x0 + 88, 204, 'Bütün yarıçaplar eşit:', 13, 'g-mf', 'middle', 700)
    ic += _yazi(x0 + 88, 221, '|AK| = |AL| = r', 13, 'g-mf', 'middle', 700)
    return svg(460, 238, ic, 'Merkezi A olan çember. A merkezinden çember üzerindeki K ve L noktalarına çizilen yarıçapların ikisi de r '
               'uzunluğundadır; merkezden geçen MN çapı 2r uzunluğundadır. Aynı çemberin bütün yarıçapları eşittir.')


def kesisen_cemberler_ucgen():
    """Yarıçapları 3 cm (96 birim) olan A ve B merkezli çemberler, |AB| = 4 cm; C ve D kesişim noktaları; ABC ikizkenar üçgeni."""
    B1 = 32                                     # 1 cm
    A, B, r = (112, 134), (240, 134), 3 * B1
    C, D = _kesisim(A, B, r, r)
    ic = _cember(A, r, 'g-ms', 2.5) + _cember(B, r, 'g-os', 2.5)
    ic += _cizgi(A, D, 'g-ms', 2, ' stroke-dasharray="6 4"') + _cizgi(B, D, 'g-os', 2, ' stroke-dasharray="6 4"')
    ic += _cizgi(A, C, 'g-ms', 3.5) + _cizgi(B, C, 'g-os', 3.5) + _cizgi(A, B, 'g-ts', 3.5)
    for p in (A, B, C, D):
        ic += _nokta(p)
    ic += _yazi(A[0] - 14, A[1] + 5, 'A', 14, hiza='end', kalin=800)
    ic += _yazi(B[0] + 14, B[1] + 5, 'B', 14, hiza='start', kalin=800)
    ic += _yazi(C[0], C[1] - 14, 'C', 14, kalin=800)
    ic += _yazi(D[0], D[1] + 24, 'D', 14, kalin=800)
    ic += _kenar_yazi(A, C, B, '3 cm', 'g-mf')
    ic += _kenar_yazi(B, C, A, '3 cm', 'g-of')
    ic += _yazi((A[0] + B[0]) / 2, A[1] + 18, '4 cm', 13, 'g-tf', kalin=700)
    ic += _yazi((A[0] + B[0]) / 2, 254, 'Kesik çizgili ABD üçgeninin kenarları da aynıdır.', 12, 'g-s')
    # açıklama
    x0 = 348
    for y, s_cizgi, s_yazi, bas, alt1, alt2 in ((52, 'g-ms', 'g-mf', '|AC| = 3 cm', 'A merkezli çemberin', 'yarıçapı'),
                                                (112, 'g-os', 'g-of', '|BC| = 3 cm', 'B merkezli çemberin', 'yarıçapı'),
                                                (172, 'g-ts', 'g-tf', '|AB| = 4 cm', 'merkezler arası', 'uzaklık')):
        ic += _cizgi((x0, y - 4), (x0 + 18, y - 4), s_cizgi, 3.5)
        ic += _yazi(x0 + 26, y, bas, 13, s_yazi, 'start', 700)
        ic += _yazi(x0, y + 17, alt1, 12, 'g-s', 'start')
        ic += _yazi(x0, y + 32, alt2, 12, 'g-s', 'start')
    ic += _yazi(x0, 232, 'ABC üçgeni:', 13, hiza='start', kalin=700)
    ic += _yazi(x0, 249, 'ikizkenar üçgen', 13, hiza='start', kalin=700)
    return svg(480, 266, ic, 'Yarıçapları 3 santimetre olan A ve B merkezli iki çember; merkezler arasındaki uzaklık 4 santimetre. '
               'Çemberler C ve D noktalarında kesişir. ABC üçgeninde AC uzunluğu 3 santimetre, BC uzunluğu 3 santimetre, '
               'AB uzunluğu 4 santimetre; üçgen ikizkenardır. Kesik çizgili ABD üçgeninin kenarları da aynıdır.')


def surukle_ve_izle():
    """Dinamik yazılımda üç durum: |AB| = 3 (eşkenar), B sürüklenince |AB| = 4 (ikizkenar), sürgüyle |BC| = 5 (çeşitkenar)."""
    B1, y0 = 12, 112                            # 1 birim = 12 uzunluk; merkezlerin bulunduğu yatay
    paneller = [dict(cx=80, r1=3, r2=3, ab=3, baslik='başlangıç: |AB| = 3', tur='eşkenar üçgen', tur_sinif='g-yf', dolgu=True),
                dict(cx=240, r1=3, r2=3, ab=4, baslik='B sürüklendi: |AB| = 4', tur='ikizkenar üçgen', tur_sinif='g-y', dolgu=False),
                dict(cx=400, r1=3, r2=5, ab=4, baslik='sürgü: |BC| = 5', tur='çeşitkenar üçgen', tur_sinif='g-y', dolgu=False)]
    ic = ''
    for p in paneller:
        cx, r1, r2, ab = p['cx'], p['r1'] * B1, p['r2'] * B1, p['ab'] * B1
        sol, sag = min(-r1, ab - r2), max(r1, ab + r2)          # çember çiftinin A'ya göre yatay sınırları
        A = (cx - (sol + sag) / 2, y0)
        B = (A[0] + ab, y0)
        C = _kesisim(A, B, r1, r2)[0]
        ic += _yazi(cx, 38, p['baslik'], 12, 'g-s')
        if p['dolgu']:
            ic += f'<path d="M{A[0]:.1f} {A[1]:.1f} L{B[0]:.1f} {B[1]:.1f} L{C[0]:.1f} {C[1]:.1f} Z" class="g-ya"/>'
        ic += _cember(A, r1, 'g-ms', 2) + _cember(B, r2, 'g-os', 2)
        ic += _cizgi(A, C, 'g-ms', 3) + _cizgi(B, C, 'g-os', 3) + _cizgi(A, B, 'g-ts', 3)
        for q in (A, B, C):
            ic += _nokta(q, 'g-y', 4)
        if B[0] - r2 < A[0] - 10:                                  # büyük B çemberi A'nın solunu kaplıyorsa A harfi aşağıya
            ic += _yazi(A[0] + 3, y0 + 20, 'A', 12.5, kalin=800)
        else:
            ic += _yazi(A[0] - 8, y0 + 4.5, 'A', 12.5, hiza='end', kalin=800)
        ic += _yazi(B[0] + 8, y0 + 4.5, 'B', 12.5, hiza='start', kalin=800)
        ic += _yazi(C[0], C[1] - 14, 'C', 12.5, kalin=800)
        # ekrandaki uzunluklar
        ic += _kutu(cx - 58, 188, 116, 66, 'g-z', 'g-c', rx=9, kalin=1.5)
        ic += _yazi(cx, 209, f'|AC| = {p["r1"]}', 13, 'g-mf', kalin=700)
        ic += _yazi(cx, 228, f'|BC| = {p["r2"]}', 13, 'g-of', kalin=700)
        ic += _yazi(cx, 247, f'|AB| = {p["ab"]}', 13, 'g-tf', kalin=700)
        ic += _yazi(cx, 276, p['tur'], 13, p['tur_sinif'], kalin=800)
    return svg(480, 292, ic, 'Dinamik matematik yazılımında üç durum. Başlangıçta yarıçaplar 3, AB uzunluğu 3: kenarlar 3, 3, 3, '
               'eşkenar üçgen. B sürüklenip AB uzunluğu 4 olunca kenarlar 3, 3, 4: ikizkenar üçgen. Sürgüyle ikinci yarıçap 5 '
               'yapılınca kenarlar 3, 5, 4: çeşitkenar üçgen. Yarıçap olan kenarlar sürüklemede değişmez, yalnız AB değişir.')


def yasam_cicegi():
    """İlk çemberin üzerinde merkezleri bulunan, aynı yarıçaplı altı çember; merkezler birleştirilince altı eşkenar üçgen."""
    A, r = (132, 140), 56
    P = [_nk(*A, r, k * 60) for k in range(6)]
    ic = ''
    for k in range(6):
        q, s = P[k], P[(k + 1) % 6]
        ic += f'<path d="M{A[0]} {A[1]} L{q[0]:.1f} {q[1]:.1f} L{s[0]:.1f} {s[1]:.1f} Z" class="g-ya" opacity=".7"/>'
    for q in P:
        ic += _cember(q, r, 'g-c', 1.6)
    ic += _cember(A, r, 'g-ms', 2.4)
    ic += '<path d="M' + ' L'.join(f'{q[0]:.1f} {q[1]:.1f}' for q in P) + ' Z" class="g-ys" stroke-width="2"/>'
    for q in P:
        ic += _cizgi(A, q, 'g-ys', 2)
    ic += _nokta(A, 'g-y', 4)
    for q in P:
        ic += _nokta(q, 'g-y', 3.5)
    # açıklama
    x0 = 262
    ic += _yazi(x0, 48, 'Yaşam çiçeği çekirdeği', 14, hiza='start', kalin=800)
    ic += _cizgi((x0, 74), (x0 + 18, 74), 'g-ms', 3)
    ic += _yazi(x0 + 26, 78, 'İlk çember, yarıçapı r', 12.5, hiza='start')
    ic += _cizgi((x0, 100), (x0 + 18, 100), 'g-c', 3)
    ic += _yazi(x0 + 26, 104, 'Altı çember daha, aynı r', 12, hiza='start')
    ic += _yazi(x0, 121, 'merkezleri ilk çemberin', 12, 'g-s', 'start')
    ic += _yazi(x0, 136, 'üzerinde', 12, 'g-s', 'start')
    ic += _cizgi((x0, 160), (x0 + 18, 160), 'g-ys', 3)
    ic += _yazi(x0 + 26, 164, 'Merkezleri birleştir:', 12.5, hiza='start')
    ic += _yazi(x0, 182, '6 eşkenar üçgen', 13, 'g-yf', 'start', 800)
    ic += _yazi(x0, 199, 'her kenar bir yarıçap: r', 12, 'g-s', 'start')
    ic += _yazi(x0, 226, 'Aynı adımlarla desen dışa', 12, 'g-s', 'start')
    ic += _yazi(x0, 241, 'doğru büyütülebilir.', 12, 'g-s', 'start')
    return svg(456, 270, ic, 'Yaşam çiçeği çekirdeği: ilk çemberin üzerinde merkezleri bulunan, aynı yarıçaplı altı çember daha '
               'çizilmiştir. Yedi merkez birleştirilince kenarları yarıçapa eşit altı eşkenar üçgen ortaya çıkar.')


def uygula(o):
    g = {'Çemberi hatırlayalım: merkez, yarıçap, çap': cember_merkez_yaricap_cap(),
         'Merkezler ve bir kesişim noktasından üçgen kuralım': kesisen_cemberler_ucgen(),
         'Dinamik matematik yazılımında inceleme': surukle_ve_izle(),
         'Bu yöntem ne işe yarar? Süslemeler, logolar ve tarih': yasam_cicegi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
