"""11. sınıf Matematik 9. hafta görselleri: yamuk ve dörtgen çizimleri (SVG; insan figürü yok; ölçüsüz şematik çizim)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def cizgi(p, q, renk=LAC, k=1.6, kesik=False):
    d = ' stroke-dasharray="5 4"' if kesik else ''
    return f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{renk}" stroke-width="{k}"{d}/>'


def kesis(p1, p2, p3, p4):
    d = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])
    t = ((p1[0] - p3[0]) * (p3[1] - p4[1]) - (p1[1] - p3[1]) * (p3[0] - p4[0])) / d
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))


def birim(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    u = math.hypot(dx, dy)
    return dx / u, dy / u


def dik_isaret(o, p, q, s=10, renk=KIR):
    """o köşesinde, op ve oq doğrultularında küçük dik açı kutusu."""
    a, b = birim(o, p), birim(o, q)
    k1 = (o[0] + a[0] * s, o[1] + a[1] * s)
    k2 = (k1[0] + b[0] * s, k1[1] + b[1] * s)
    k3 = (o[0] + b[0] * s, o[1] + b[1] * s)
    return f'<polyline points="{k1[0]:.1f},{k1[1]:.1f} {k2[0]:.1f},{k2[1]:.1f} {k3[0]:.1f},{k3[1]:.1f}" fill="none" stroke="{renk}" stroke-width="1.2"/>'


def sekil(nk, sira, kenar_yazi=(), ek='', en=360, boy=170, etiket='', mm=34, dolgu=MAVI_A):
    """nk: {ad: (x, y)}; sira: çokgen köşe sırası; kenar_yazi: [(P, Q, metin, renk)] dışa doğru."""
    pts = [nk[a] for a in sira]
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    ic = f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'
    ic += '<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + f'" fill="{dolgu}" stroke="{LAC}" stroke-width="1.8"/>'
    ic += ek
    for p, q, metin, renk in kenar_yazi:
        a, b = nk[p], nk[q]
        ox, oy = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        nx, ny = b[1] - a[1], a[0] - b[0]  # kenara dik, dışa doğru
        u = math.hypot(nx, ny) or 1
        nx, ny = nx / u, ny / u
        if nx * (ox - mx) + ny * (oy - my) < 0:
            nx, ny = -nx, -ny
        uz = 9 + abs(nx) * len(metin) * 3.8 + abs(ny) * 5
        ic += yazi(ox + nx * uz, oy + ny * uz + 4.5, metin, 13, renk)
    for ad, (x, y) in nk.items():
        if ad.startswith('_'):
            continue
        vx, vy = x - mx, y - my
        u = math.hypot(vx, vy) or 1
        ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4" fill="{LAC}"/>'
        ic += yazi(x + vx / u * 13, y + vy / u * 13 + 5, ad, 14)
    return svg(ic, en, boy, etiket, mm)


def s_aci():
    nk = {'A': (70, 140), 'B': (320, 140), 'C': (250, 36), 'D': (40, 36)}
    ek = yazi(84, 128, '3x + 10', 12.5, KIR, 'start') + yazi(66, 58, '2x + 20', 12.5, MOR, 'start')
    ek += yazi(195, 128, '[AB] // [DC]', 11.5, SOLUK, ince=True)
    return sekil(nk, 'ABCD', ek=ek, boy=166, etiket='ABCD yamuğunda A ve D açıları', mm=32)


def s_orta():
    A, B, C, D = (30, 140), (330, 140), (250, 36), (110, 36)
    E, F = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2), ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    K, L = kesis(A, C, E, F), kesis(B, D, E, F)
    ek = cizgi(A, C, GRI, 1.1) + cizgi(B, D, GRI, 1.1) + cizgi(E, F, TUR, 2.2)
    for ad, p in (('K', K), ('L', L)):
        ek += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.6" fill="{TUR}"/>' + yazi(p[0], p[1] - 8, ad, 13, TUR)
    nk = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F}
    return sekil(nk, 'ABCD', [('A', 'B', '18 cm', MAVI), ('D', 'C', '10 cm', MAVI)], ek,
                 boy=172, etiket='Yamukta orta taban EF ve köşegenler', mm=34)


def s_ikizkenar():
    A, B, C, D = (40, 132), (320, 132), (236, 40), (124, 40)
    H = (124, 132)
    ek = cizgi(D, H, KIR, 1.3, True) + dik_isaret(H, D, B) + yazi(132, 98, 'h', 13, KIR, 'start')
    nk = {'A': A, 'B': B, 'C': C, 'D': D, 'H': H}
    return sekil(nk, 'ABCD', [('A', 'B', '26 cm', MAVI), ('D', 'C', '8 cm', MAVI), ('A', 'D', '15 cm', MOR), ('B', 'C', '15 cm', MOR)],
                 ek, boy=168, etiket='İkizkenar yamuk ve yüksekliği', mm=33)


def s_dik():
    A, B, C, D = (60, 136), (320, 136), (205, 40), (60, 40)
    ek = dik_isaret(A, B, D) + dik_isaret(D, A, C)
    nk = {'A': A, 'B': B, 'C': C, 'D': D}
    return sekil(nk, 'ABCD', [('A', 'B', '20 cm', MAVI), ('D', 'C', '11 cm', MAVI), ('B', 'C', '15 cm', MOR)],
                 ek, boy=168, etiket='Dik yamuk', mm=33)


def s_dik_kosegen_ikiz():
    A, B, C, D = (75, 172), (285, 172), (225, 22), (135, 22)
    O = kesis(A, C, B, D)
    ek = cizgi(A, C, TUR, 1.4) + cizgi(B, D, TUR, 1.4) + dik_isaret(O, C, D, 9)
    nk = {'A': A, 'B': B, 'C': C, 'D': D}
    return sekil(nk, 'ABCD', [('A', 'B', '14 cm', MAVI), ('D', 'C', '6 cm', MAVI)], ek,
                 boy=196, etiket='Köşegenleri dik kesişen ikizkenar yamuk', mm=36)


def s_dik_kosegen_dik():
    A, B, C, D = (45, 150), (315, 150), (85, 46), (45, 46)
    O = kesis(A, C, B, D)
    ek = cizgi(A, C, TUR, 1.4) + cizgi(B, D, TUR, 1.4) + dik_isaret(O, C, B, 8) + dik_isaret(A, B, D) + dik_isaret(D, A, C)
    nk = {'A': A, 'B': B, 'C': C, 'D': D}
    return sekil(nk, 'ABCD', [('A', 'B', '18 cm', MAVI)], ek,
                 boy=180, etiket="Köşegenleri dik kesişen dik yamuk", mm=34)


def s_aciortay():
    A, B, C, D = (40, 140), (300, 150), (330, 46), (110, 24)

    def ortay(o, p, q):
        a, b = birim(o, p), birim(o, q)
        return (o[0] + (a[0] + b[0]) * 100, o[1] + (a[1] + b[1]) * 100)
    E = kesis(A, ortay(A, B, D), B, ortay(B, A, C))
    ek = cizgi(A, E, MOR, 1.4, True) + cizgi(B, E, MOR, 1.4, True)
    ek += f'<circle cx="{E[0]:.1f}" cy="{E[1]:.1f}" r="2.6" fill="{MOR}"/>' + yazi(E[0], E[1] + 20, 'E', 14, MOR)
    ek += yazi(C[0] - 30, C[1] + 16, '120°', 12.5, KIR) + yazi(D[0] + 4, D[1] + 22, '80°', 12.5, KIR)
    nk = {'A': A, 'B': B, 'C': C, 'D': D}
    return sekil(nk, 'ABCD', ek=ek, boy=172, etiket='Dörtgende A ve B açıortayları', mm=33)


def s_dik_dortgen():
    A, B, C, D = (40, 92), (160, 158), (330, 92), (160, 22)
    O = (160, 92)
    ek = cizgi(A, C, TUR, 1.2, True) + cizgi(B, D, TUR, 1.2, True) + dik_isaret(O, C, D, 9)
    nk = {'A': A, 'B': B, 'C': C, 'D': D}
    return sekil(nk, 'ABCD', [('A', 'B', '6 cm', MAVI), ('B', 'C', '9 cm', MOR), ('C', 'D', '7 cm', MAVI), ('D', 'A', 'x', MOR)],
                 ek, boy=180, etiket='Köşegenleri dik kesişen dörtgen', mm=33)


def s_varignon():
    A, B, C, D = (40, 150), (300, 160), (330, 50), (120, 22)
    K, L, M, N = [((p[0] + q[0]) / 2, (p[1] + q[1]) / 2) for p, q in ((A, B), (B, C), (C, D), (D, A))]
    ek = f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in (K, L, M, N))}" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ek += cizgi(A, C, GRI, 1.1, True) + cizgi(B, D, GRI, 1.1, True)
    nk = {'A': A, 'B': B, 'C': C, 'D': D, 'K': K, 'L': L, 'M': M, 'N': N}
    return sekil(nk, 'ABCD', ek=ek, boy=182, etiket='Dörtgenin kenar orta noktalarından oluşan KLMN', mm=34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = s_aci()
    s[2]['gorsel'] = s_orta()
    s[4]['gorsel'] = s_ikizkenar()
    s[6]['gorsel'] = s_dik()
    s[7]['gorsel'] = s_dik_kosegen_ikiz()
    s[8]['gorsel'] = s_dik_kosegen_dik()
    s[10]['gorsel'] = s_aciortay()
    s[11]['gorsel'] = s_dik_dortgen()
    s[12]['gorsel'] = s_varignon()
