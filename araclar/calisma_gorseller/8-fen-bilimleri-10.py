"""8. sınıf Fen Bilimleri 10. hafta (3. Ünite: Basınç — Katı ve Sıvı Basıncı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def klm_ozdes_kupler():
    """Soru 2 (s[1]): K (1 küp, S), L (2 küp dikey, S), M (2 küp yatay, 2S) düzenekleri."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8)
    ic += yazi(180, 19, 'Özdeş Küplerle Kurulan K, L ve M Katı Basıncı Düzenekleri', KAHVE, boy=10.2)
    # Zemin çizgisi
    ic += f'<line x1="16" y1="68" x2="344" y2="68" stroke="{LAC}" stroke-width="1.8"/>'
    # K düzeneği: 1 küp
    ic += kutu(44, 46, 26, 22, MAVI_A, MAVI, 3)
    ic += yazi(57, 61, 'G', MAVI, boy=9.8)
    ic += yazi(57, 82, 'K (Ağırlık: G · Yüzey: S)', LAC, boy=9.2)
    # L düzeneği: 2 küp üst üste
    ic += kutu(162, 24, 26, 22, TUR_A, TUR, 3)
    ic += kutu(162, 46, 26, 22, TUR_A, TUR, 3)
    ic += yazi(175, 39, 'G', TUR, boy=9.5)
    ic += yazi(175, 61, 'G', TUR, boy=9.5)
    ic += yazi(175, 82, 'L (2G · Yüzey: S)', TUR, boy=9.2)
    # M düzeneği: 2 küp yan yana
    ic += kutu(264, 46, 26, 22, YES_A, YES, 3)
    ic += kutu(290, 46, 26, 22, YES_A, YES, 3)
    ic += yazi(277, 61, 'G', YESIL_K, boy=9.5)
    ic += yazi(303, 61, 'G', YESIL_K, boy=9.5)
    ic += yazi(290, 82, 'M (2G · Yüzey: 2S)', YESIL_K, boy=9.2)
    return svg(360, 94, ic, 'K (G, S), L (2G, S) ve M (2G, 2S) özdeş küp düzenekleri.', 15)


def dort_basinc_deney_karti():
    """Soru 3 (s[2]): 4 deneysel işlem kartı."""
    kartlar = [
        (4, 4, '1. Tuğlayı Dik Konuma Getirme', 'Yüzey: 2S -> S (Ağırlık sabit)', MAVI, MAVI_A),
        (184, 4, '2. Silindiri Dikey İkiye Kesme', 'Ağırlık: 2G -> G · Yüzey: 2S -> S', YES, YES_A),
        (4, 52, '3. Kaba Aynı Cins Su Ekleme', 'Derinlik: h -> 2h (Yoğunluk sabit)', TUR, TUR_A),
        (184, 52, '4. Su Yerine Zeytinyağı Koyma', 'Derinlik: h sabit · Yoğunluk küçülür', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.0)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.3)
    return svg(360, 100, ic, 'Katı ve sıvı basıncında dört farklı deneysel işlem kartı.', 15)


def su_deposu_xyz_musluklari():
    """Soru 6 (s[5]): X (h), Y (2h), Z (3h) musluklarından fışkıran su."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Su Dolu Depoda X, Y ve Z Musluklarının Derinlikleri', MAVI)
    ic += kutu(24, 26, 92, 58, '#bae6fd', MAVI, 4)
    ic += yazi(70, 58, 'Su (d)', MAVI)
    # X, Y, Z noktaları
    ic += f'<circle cx="116" cy="38" r="3.2" fill="{KIR}"/>'
    ic += yazi(222, 42, 'X Musluğu (Derinlik: h) -> Mesafe: x_X', LAC, ince=True, boy=9.6)
    ic += f'<circle cx="116" cy="56" r="3.2" fill="{TUR}"/>'
    ic += yazi(222, 60, 'Y Musluğu (Derinlik: 2h) -> Mesafe: x_Y', LAC, ince=True, boy=9.6)
    ic += f'<circle cx="116" cy="74" r="3.2" fill="{YESIL_K}"/>'
    ic += yazi(222, 78, 'Z Musluğu (Derinlik: 3h) -> Mesafe: x_Z', YESIL_K, boy=9.6)
    return svg(360, 94, ic, 'Yan yüzeyinde h, 2h ve 3h derinlikte X, Y, Z muslukları bulunan su deposu.', 15)


def uc_kap_klm_sivi_basinci():
    """Soru 7 (s[6]): I (2h, d, S -> K), II (2h, d, 3S -> L), III (h, d, 2S -> M)."""
    kartlar = [
        (6, 'I. Kap (K Noktası)', 'Derinlik: 2h · Su (d)', 'Taban alanı: S', MAVI, MAVI_A),
        (124, 'II. Kap (L Noktası)', 'Derinlik: 2h · Su (d)', 'Taban alanı: 3S (Geniş)', YES, YES_A),
        (242, 'III. Kap (M Noktası)', 'Derinlik: h · Su (d)', 'Taban alanı: 2S', TUR, TUR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 4, 112, 84, z, r, 8)
        ic += yazi(x + 56, 22, bas, r, boy=10.0)
        ic += yazi(x + 56, 46, s1, LAC, boy=9.5)
        ic += yazi(x + 56, 68, s2, LAC, ince=True, boy=9.3)
    return svg(360, 92, ic, 'Farklı taban alanlarına ve derinliklere sahip K, L, M kapları.', 15)


def raptiye_kuvvet_basinc_modeli():
    """Soru 8 (s[7]): Raptiyenin geniş başı (S1, F1, P1) ve sivri ucu (S2, F2, P2)."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(90, 22, 'Geniş Baş Kısmı (S₁ Büyük)', MAVI, boy=10.2)
    ic += yazi(90, 44, 'Uygulanan Kuvvet: F₁ = F', LAC, ince=True, boy=9.6)
    ic += yazi(90, 66, 'Oluşan Basınç: P₁', MAVI, boy=9.8)

    ic += kutu(184, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(270, 22, 'Sivri Uç Kısmı (S₂ Küçük)', KIR, boy=10.2)
    ic += yazi(270, 44, 'İletilen Kuvvet: F₂ = ?', LAC, ince=True, boy=9.6)
    ic += yazi(270, 66, 'Oluşan Basınç: P₂ = ?', KIR, boy=9.8)
    return svg(360, 90, ic, 'Raptiyenin geniş baş kısmı ve sivri uç kısmında kuvvet ve basınç iletimi.', 14)


def hidrolik_fren_akis():
    """Soru 9 (s[8]): Hidrolik fren sistemi 4 aşamalı çalışma şeması."""
    adimlar = [
        (4, '1. Pedal', 'Fren pedalına', 'kuvvet uygulanır', MAVI, MAVI_A),
        (93, '2. Sıvı Basıncı', 'Ana silindirde', 'basınç oluşur', TUR, TUR_A),
        (182, '3. İletim', 'Sıvı basıncı her', 'yöne eşit iletir', MOR, MOR_A),
        (271, '4. Durma', 'Balatalar diski', 'sıkıştırıp durdurur', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.0)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.3)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.3)
    return svg(360, 88, ic, 'Hidrolik fren sisteminin Pascal Prensibi ile çalışma aşamaları.', 14)


def kesik_koni_ters_cevirme():
    """Soru 10 (s[9]): Kesik koni kabın dar taban (S) üzerinden geniş taban (3S) üzerine çevrilmesi."""
    ic = kutu(4, 4, 172, 86, TUR_A, TUR, 8)
    ic += yazi(90, 21, '1. Durum (Dar Taban Yerde)', TUR, boy=10.1)
    ic += yazi(90, 43, 'Temas Yüzeyi: S (Dar)', LAC, ince=True, boy=9.6)
    ic += yazi(90, 61, 'Su Yüksekliği: h₁ (Yüksek)', LAC, ince=True, boy=9.6)
    ic += yazi(90, 79, 'Toplam Ağırlık: G', TUR, boy=9.6)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(270, 21, '2. Durum (Geniş Taban Yerde)', YESIL_K, boy=10.1)
    ic += yazi(270, 43, 'Temas Yüzeyi: 3S (Genişledi)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 61, 'Su Yüksekliği: h₂ &lt; h₁ (Azaldı)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 79, 'Toplam Ağırlık: G (Sabit)', YESIL_K, boy=9.6)
    return svg(360, 94, ic, 'Yarısına kadar su dolu kesik koni kabın geniş tabanı üzerine ters çevrilmesi.', 15)


def su_cenderesi_karti():
    """Soru 12 (s[11]): Su cenderesi küçük piston (S1, F) ve büyük piston (S2, G)."""
    ic = kutu(4, 4, 352, 82, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Su Cenderesi (Hidrolik Kaldıraç) · Pascal Prensibi Düzeneği', MAVI)
    ic += kutu(14, 28, 154, 48, '#fff', TUR, 6)
    ic += yazi(91, 46, '1. Kol (Dar Piston: S₁)', TUR, boy=9.9)
    ic += yazi(91, 66, 'Küçük F kuvveti uygulanır', LAC, ince=True, boy=9.4)

    ic += kutu(192, 28, 154, 48, '#fff', YES, 6)
    ic += yazi(269, 46, '2. Kol (Geniş Piston: S₂ > S₁)', YESIL_K, boy=9.9)
    ic += yazi(269, 66, 'Ağır otomobil (G) kaldırılır', LAC, ince=True, boy=9.4)
    return svg(360, 90, ic, 'Su cenderesinde küçük pistonla uygulanan basıncın geniş pistona iletilmesi.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = klm_ozdes_kupler()
    s[2]['gorsel'] = dort_basinc_deney_karti()
    s[5]['gorsel'] = su_deposu_xyz_musluklari()
    s[6]['gorsel'] = uc_kap_klm_sivi_basinci()
    s[7]['gorsel'] = raptiye_kuvvet_basinc_modeli()
    s[8]['gorsel'] = hidrolik_fren_akis()
    s[9]['gorsel'] = kesik_koni_ters_cevirme()
    s[11]['gorsel'] = su_cenderesi_karti()
