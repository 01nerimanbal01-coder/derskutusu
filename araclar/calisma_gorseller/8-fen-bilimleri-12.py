"""8. sınıf Fen Bilimleri 12. hafta (Periyodik Sistem: Tarihçe, Periyot-Grup ve Elementlerin Sınıflandırılması) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def periyodik_kesit_modeli():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Periyodik Tablo İlk 3 Periyot Kesiti', LAC, kalin=True)
    ic += kutu(24, 30, 56, 24, YES_A, YES, 4)
    ic += yazi(52, 46, 'X (1A)', YES, kalin=True)
    ic += kutu(280, 30, 56, 24, MOR_A, MOR, 4)
    ic += yazi(308, 46, 'Y (8A)', MOR, kalin=True)
    ic += kutu(152, 58, 56, 24, TUR_A, TUR, 4)
    ic += yazi(180, 74, 'Z (3A)', TUR, kalin=True)
    ic += kutu(88, 84, 56, 22, MAVI_A, MAVI, 4)
    ic += yazi(116, 99, 'T (2A)', MAVI, kalin=True)
    return svg(ic, 'Periyodik tablonun ilk üç periyodunda X, Y, Z ve T elementlerinin konumu.')


def dort_element_karti():
    kartlar = [
        (6, 6, '1. Hidrojen (₁H)', 'Katman: 1) · İstisna!', YES, YES_A),
        (184, 6, '2. Helyum (₂He)', 'Katman: 2) · Tam Dolu!', MOR, MOR_A),
        (6, 60, '3. Bor (₅B)', 'Katman: 2) 3) · Yarı İletken', TUR, TUR_A),
        (184, 60, '4. Magnezyum (₁₂Mg)', 'Katman: 2) 8) 2) · İletken', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Hidrojen, Helyum, Bor ve Magnezyum katman dizilimi kartları.')


def sinif_ozellik_kartlari():
    kartlar = [
        (6, 'K Sınıfı', 'Parlak · Tel/Levha', 'Isı/Elektrik İletir', MAVI, MAVI_A),
        (124, 'L Sınıfı', 'Fiziksel: Metal', 'Kimyasal: Ametal', TUR, TUR_A),
        (242, 'M Sınıfı', 'Mat · Kırılgan', 'Katı / Sıvı / Gaz', YES, YES_A),
    ]
    ic = ''
    for x, ad, o1, o2, r, z in kartlar:
        ic += kutu(x, 6, 112, 103, z, r)
        ic += yazi(x + 56, 28, ad, r, kalin=True)
        ic += yazi(x + 56, 58, o1, LAC, kalin=True)
        ic += yazi(x + 56, 86, o2, LAC)
    return svg(ic, 'Metal, yarı metal ve ametal sınıflarının özellik kartları.')


def klor_katman_modeli():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Klor Atomu (₁₇Cl)', YES, kalin=True)
    ic += yazi(92, 56, 'Katman Dizilimi: 2 ) 8 ) 7', LAC, kalin=True)
    ic += yazi(92, 86, '3 Katman · Son Katman: 7e⁻', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, 'Yer Bulma Kuralı', MAVI, kalin=True)
    ic += yazi(269, 54, 'Katman Sayısı = Periyot No', LAC)
    ic += yazi(269, 82, 'Son Katman e⁻ = A Grubu No', KIR, kalin=True)
    return svg(ic, 'Atom numarası 17 olan Klor elementinin katman-elektron dizilimi.')


def bir_a_grubu_istisnasi():
    ic = kutu(6, 6, 130, 103, MAVI_A, MAVI)
    ic += yazi(71, 24, '1A Grubu Sütunu', MAVI, kalin=True)
    ic += kutu(31, 32, 80, 22, YES_A, YES, 4)
    ic += yazi(71, 47, '₁H (Hidrojen)', YES, kalin=True)
    ic += kutu(31, 58, 80, 22, MAVI_A, MAVI, 4)
    ic += yazi(71, 73, '₃Li (Lityum)', MAVI, kalin=True)
    ic += kutu(31, 84, 80, 22, MAVI_A, MAVI, 4)
    ic += yazi(71, 99, '₁₁Na (Sodyum)', MAVI, kalin=True)
    ic += kutu(144, 6, 210, 103, TUR_A, TUR)
    ic += yazi(249, 30, 'Dikkat: 1A Grubu İstisnası!', KIR, kalin=True)
    ic += yazi(249, 58, '₃Li ve ₁₁Na → Alkali Metal', LAC, kalin=True)
    ic += yazi(249, 84, '₁H → 1A’da olmasına rağmen AMETAL!', YES, kalin=True)
    return svg(ic, '1A grubunda Hidrojenin ametal, Lityum ve Sodyumun metal olması şeması.')


def tarihce_kronoloji_kartlari():
    adimlar = [
        (6, '1829', 'Döbereiner (3’lü)', MAVI, MAVI_A),
        (94, '1864', 'Newlands (8’li)', YES, YES_A),
        (182, '1869', 'Mendeleyev (Kütle)', TUR, TUR_A),
        (270, '1913', 'Moseley (Proton)', MOR, MOR_A),
    ]
    ic = ''
    for x, yil, bilim, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, yil, r, kalin=True)
        ic += yazi(x + 42, 70, bilim, LAC, kalin=True)
    return svg(ic, 'Periyodik tablonun tarihsel gelişim basamakları.')


def periyodik_degisim_oklari():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, '1 Yönü (Soldan Sağa →)', MAVI, kalin=True)
    ic += yazi(92, 52, '• Atom numarası ARTAR', YES, kalin=True)
    ic += yazi(92, 74, '• Grup numarası ARTAR', LAC)
    ic += yazi(92, 95, '• Periyot sayısı DEĞİŞMEZ', LAC)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, '2 Yönü (Yukarıdan Aşağı ↓)', TUR, kalin=True)
    ic += yazi(269, 52, '• Atom numarası ARTAR', YES, kalin=True)
    ic += yazi(269, 74, '• Periyot sayısı ARTAR', LAC)
    ic += yazi(269, 95, '• Grup numarası DEĞİŞMEZ', LAC)
    return svg(ic, 'Periyodik tabloda soldan sağa ve yukarıdan aşağıya değişen özellikler.')


def bor_silisyum_teknoloji():
    ic = kutu(6, 6, 172, 103, TUR_A, TUR)
    ic += yazi(92, 26, 'Bor (₅B — Yarı Metal)', TUR, kalin=True)
    ic += yazi(92, 54, '• Isıya dayanıklı cam (Borcam)', LAC)
    ic += yazi(92, 78, '• Roket yakıtı ve deterjan', LAC)
    ic += yazi(92, 98, '• Türkiye dünya rezerv lideri!', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 26, 'Silisyum (₁₄Si — Yarı Metal)', CAM, kalin=True)
    ic += yazi(269, 54, '• Güneş panelleri (Fotovoltaik)', LAC)
    ic += yazi(269, 78, '• Bilgisayar mikroçipleri', LAC)
    ic += yazi(269, 98, '• Yarı iletken teknoloji!', MAVI, kalin=True)
    return svg(ic, 'Bor ve Silisyum yarı metallerinin ileri teknolojide kullanım alanları.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = periyodik_kesit_modeli()
    s[2]['gorsel'] = dort_element_karti()
    s[5]['gorsel'] = sinif_ozellik_kartlari()
    s[6]['gorsel'] = klor_katman_modeli()
    s[7]['gorsel'] = bir_a_grubu_istisnasi()
    s[8]['gorsel'] = tarihce_kronoloji_kartlari()
    s[9]['gorsel'] = periyodik_degisim_oklari()
    s[11]['gorsel'] = bor_silisyum_teknoloji()
