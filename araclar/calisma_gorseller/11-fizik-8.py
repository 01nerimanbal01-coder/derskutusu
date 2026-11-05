"""11. sınıf Fizik 8. hafta görselleri (SVG; insan figürü yok K024; beyaz bant yok K178; 24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket):
    stil = ' style="width:100%;max-height:24mm;display:block;margin:1mm auto;"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+81},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def uclu(baslik, k1, a1, k2, a2, k3, a3, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 22, baslik, 10.0, c)
    for i, (k, a, rk, dk) in enumerate([(k1, a1, MAVI, MAVI_A), (k2, a2, TUR, TUR_A), (k3, a3, YES, YES_A)]):
        x = 12 + i * 114
        ic += kutu(x, 32, 108, 70, dk, rk) + yazi(x + 54, 54, k, 9.2, rk) + yazi(x + 54, 78, a, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.2, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def g0():
    return cizelge4([('Diyagram (SCD)', 'Yalnız gerçek kuvvet', MAVI, MAVI_A), ('Paralel Bileşen', 'm·g·sinα aşağı çeker', TUR, TUR_A), ('Normal Kuvvet', 'N = m·g·cosα dik', YES, YES_A), ('Atwood Sistemi', 'Sabit makara + 2 kütle', MOR, MOR_A)], 'Newton yasaları ve serbest cisim diyagramı')
def g1():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 22, 'YATAY DÜZLEMDE İPLE BAĞLI İKİ CİSİM SİSTEMİ', 10.0, MAVI)
    ic += f'<line x1="24" y1="84" x2="336" y2="84" stroke="{LAC}" stroke-width="1.5"/>'
    ic += kutu(44, 42, 76, 42, MAVI_A, MAVI) + yazi(82, 67, 'm1 = 2 kg', 9.5, MAVI)
    ic += f'<line x1="120" y1="63" x2="184" y2="63" stroke="{TUR}" stroke-width="2.0"/>' + yazi(152, 54, 'T = 8 N', 9.0, TUR)
    ic += kutu(184, 38, 86, 46, YES_A, YES) + yazi(227, 65, 'm2 = 3 kg', 9.5, YES)
    ic += f'<line x1="270" y1="63" x2="326" y2="63" stroke="{KIR}" stroke-width="2.2"/>' + f'<polygon points="332,63 324,58 324,68" fill="{KIR}"/>' + yazi(302, 48, 'F = 20 N', 9.5, KIR)
    ic += yazi(180, 102, 'a = F / (m1 + m2) = 20 / 5 = 4 m/s^2   ·   T = m1 · a = 8 N', 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'İple bağlı iki kütle ve kuvvet diyagramı')
def g2():
    return ikili('STATİK VE KİNETİK SÜRTÜNME KUVVETİ', 'Durgun Cisim (Statik Bölge)', 'F ≤ f_s,max ise f_s = F olur', 'Hareketli Cisim (Kinetik)', 'Sabit f_k = k_k · N etki eder', MAVI, MAVI_A, TUR, TUR_A, 'Statik ve kinetik sürtünme davranışı')
def g3():
    return uclu('EĞİK DÜZLEM VE TEMEL KUVVET KAVRAMLARI', 'Normal Kuvvet (N)', 'Yüzeye dik tepki kuvveti', 'Kinetik Sürtünme', 'Harekete zıt yönlü f_k', 'Eğik Düzlem İvmesi', 'a = g · sinα bağıntısı', YES, YES_A, 'Normal kuvvet, kinetik sürtünme ve sinüs bileşeni')
def g6():
    return akis4([('1. Diyagram', 'Gerçek kuvvetleri çiz', MAVI, MAVI_A), ('2. Sürtünme', 'f = k · N hesapla', TUR, TUR_A), ('3. Ortak İvme', 'a = F_net / m_top', YES, YES_A), ('4. İp Gerilmesi', 'Tek kütleden T bul', MOR, MOR_A)], 'Bağlı cisim problemleri çözüm adımları')
def g7():
    return ikili('ATWOOD DÜZENEĞİ (m1 = 6 kg, m2 = 4 kg)', 'Net Kuvvet Hesabı', 'F_net = (6 - 4)·10 = 20 N', 'Ortak İvme Hesabı', 'a = 20 / (6 + 4) = 2 m/s^2', MOR, MOR_A, YES, YES_A, 'Atwood düzeneği net kuvvet ve ivme')
def g8():
    return kart('SERBEST CİSİM DİYAGRAMI (SCD) ALTIN KURALI', 'Diyagramda yalnız gerçek dış kuvvetler (G, N, T, F, f_s) gösterilir.', 'Net kuvvet (F_net) ve eylemsizlik (m·a) diyagrama asla çizilmez!', KIR, KIR_A, 'Serbest cisim diyagramı kuralı')
def g9():
    return ikili('SÜRTÜNMESİZ EĞİK DÜZLEM (α = 30°, g = 10 m/s^2)', 'Paralel Kuvvet Bileşeni', 'F_net = m · g · sin30°', 'Kütleden Bağımsız İvme', 'a = g · sin30° = 5 m/s^2', MAVI, MAVI_A, CAM, CAM_A, 'Eğik düzlemde ivme hesabı')

def uygula(o):
    s = o['sorular']
    for idx, fn in [(0, g0), (1, g1), (2, g2), (3, g3), (6, g6), (7, g7), (8, g8), (9, g9)]:
        s[idx]['gorsel'] = fn()
