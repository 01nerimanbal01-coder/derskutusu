"""7. sınıf Matematik 11. hafta (Dikdörtgenler Prizmasının Yüzey Alanı, Hacmi ve Sıvı Ölçme Birimleri) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def hediye_kutusu():
    ic = kutu(6, 6, 165, 103, MAVI_A, MAVI)
    ic += f'<polygon points="36,88 116,88 116,42 36,42" fill="#dbeafe" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="36,42 62,22 142,22 116,42" fill="#bfdbfe" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="116,42 142,22 142,68 116,88" fill="#93c5fd" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(76, 103, 'a = 5 dm', MAVI, kalin=True)
    ic += yazi(144, 84, '4 dm', KIR, kalin=True)
    ic += yazi(22, 68, '3 dm', YES, kalin=True)
    ic += kutu(179, 6, 175, 103, YES_A, YES)
    ic += yazi(266, 30, 'Kapalı Hediye Kutusu', YES, kalin=True)
    ic += yazi(266, 56, 'Ayrıtlar: 5 dm, 4 dm, 3 dm', LAC)
    ic += yazi(266, 82, 'Alan (6 yüz) ve Hacim = ?', MAVI, kalin=True)
    return svg(ic, 'Ayrıtları 5 dm, 4 dm ve 3 dm olan kapalı dikdörtgenler prizması hediye kutusu.')


def dort_kap_tablo():
    kartlar = [
        (6, 6, '1. Meyve Suyu', '10×5×20 cm', MAVI, MAVI_A),
        (184, 6, '2. Yağ Tenekesi', '20×10×25 cm', TUR, TUR_A),
        (6, 60, '3. Akvaryum', '50×30×40 cm', CAM, CAM_A),
        (184, 60, '4. Su Deposu', '100×50×60 cm', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört farklı prizmatik kap ve ayrıt ölçüleri.')


def akvaryum_su():
    ic = kutu(6, 6, 170, 103, CAM_A, CAM)
    ic += f'<rect x="28" y="32" width="116" height="60" fill="#e0f2fe" stroke="{CAM}" stroke-width="1.4"/>'
    ic += f'<rect x="28" y="47" width="116" height="45" fill="#7dd3fc" stroke="{MAVI}" stroke-width="1.1"/>'
    ic += yazi(86, 24, 'Akvaryum (3/4 Dolu)', CAM, kalin=True)
    ic += yazi(86, 105, 'a = 80 cm, b = 50 cm', LAC)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 30, 'Ölçüler ve Doluluk', MAVI, kalin=True)
    ic += yazi(269, 55, 'Taban: 80 cm × 50 cm', LAC)
    ic += yazi(269, 77, 'Yükseklik: c = 60 cm', LAC)
    ic += yazi(269, 98, '1 dm³ = 1000 cm³ = 1 L', KIR, kalin=True)
    return svg(ic, 'Taban ayrıtları 80 cm ve 50 cm, yüksekliği 60 cm olan 3/4 dolu akvaryum.')


def acik_havuz():
    ic = kutu(6, 6, 174, 103, CAM_A, CAM)
    ic += yazi(93, 28, 'Üstü Açık Yüzme Havuzu', CAM, kalin=True)
    ic += yazi(93, 55, 'Boy: 10 m · En: 6 m', LAC)
    ic += yazi(93, 78, 'Derinlik (c): 2 m', MAVI, kalin=True)
    ic += yazi(93, 98, '(Üst yüzey açıktır!)', KIR, kalin=True)
    ic += kutu(188, 6, 166, 103, TUR_A, TUR)
    ic += yazi(271, 30, 'Fayans Kaplama (5 Yüz)', TUR, kalin=True)
    ic += yazi(271, 56, '1 Taban: 10 × 6 m²', LAC)
    ic += yazi(271, 80, '4 Yan Duvar: 2·(a·c+b·c)', YES, kalin=True)
    return svg(ic, 'Boyu 10 m, eni 6 m ve derinliği 2 m olan üstü açık yüzme havuzu.')


def koli_istifleme():
    ic = kutu(6, 6, 174, 103, TUR_A, TUR)
    ic += yazi(93, 28, 'Büyük Karton Koli', TUR, kalin=True)
    ic += yazi(93, 56, '60 cm × 40 cm × 30 cm', LAC, kalin=True)
    ic += yazi(93, 84, 'V = 60 · 40 · 30 cm³', TUR)
    ic += kutu(188, 6, 166, 103, YES_A, YES)
    ic += yazi(271, 28, 'Küçük Küp Kutu', YES, kalin=True)
    ic += yazi(271, 56, '10 cm × 10 cm × 10 cm', LAC, kalin=True)
    ic += yazi(271, 84, 'Adet = V(Koli) ÷ V(Küp)', MAVI, kalin=True)
    return svg(ic, 'Büyük koli içine 10 cm ayrıtlı küp kutuların yerleştirilmesi şeması.')


def sivi_siralama_kartlari():
    ogeler = [
        (6, 'K Kabı', '450 cm³', MAVI, MAVI_A),
        (94, 'L Kabı', '1,2 dm³', YES, YES_A),
        (182, 'M Kabı', '2500 mL', TUR, TUR_A),
        (270, 'N Kabı', '0,04 m³', MOR, MOR_A),
    ]
    ic = ''
    for x, ad, deger, r, z in ogeler:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 72, deger, LAC, kalin=True)
    return svg(ic, 'Dört farklı kapta bulunan sıvı hacimlerinin karşılaştırılması.')


def kaptan_kaba_aktarma():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, '1. Kap (Tam Dolu)', MAVI, kalin=True)
    ic += yazi(91, 54, 'Taban: 20 cm × 15 cm', LAC)
    ic += yazi(91, 78, 'Su Yüksekliği: 16 cm', MAVI, kalin=True)
    ic += yazi(91, 98, 'V = 20 · 15 · 16 cm³', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, '2. Kap (Yeni Kap)', YES, kalin=True)
    ic += yazi(269, 54, 'Taban: 30 cm × 20 cm', LAC)
    ic += yazi(269, 78, 'Yeni Yükseklik: h = ?', KIR, kalin=True)
    ic += yazi(269, 98, 'Suyun hacmi değişmez!', YES, kalin=True)
    return svg(ic, '1. kaptaki suyun 2. kaba aktarılmasında yükseklik değişimi modeli.')


def iki_kup_birlestirme():
    ic = kutu(6, 6, 170, 103, MOR_A, MOR)
    ic += f'<rect x="34" y="42" width="44" height="44" fill="#ddd6fe" stroke="{MOR}" stroke-width="1.4"/>'
    ic += f'<rect x="78" y="42" width="44" height="44" fill="#c4b5fd" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(91, 26, 'İki Eş Küp (a = 4 cm)', MOR, kalin=True)
    ic += yazi(91, 102, 'Yeni ayrıtlar: 8×4×4 cm', LAC, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 30, 'Yapıştırma Etkisi', TUR, kalin=True)
    ic += yazi(269, 58, 'Hacim: 64 + 64 = 128 cm³', YES, kalin=True)
    ic += yazi(269, 84, 'Alan: 2 kare yüz içeride!', KIR, kalin=True)
    return svg(ic, 'Bir ayrıtı 4 cm olan iki eş küpün yan yana yapıştırılması modeli.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = hediye_kutusu()
    s[2]['gorsel'] = dort_kap_tablo()
    s[5]['gorsel'] = akvaryum_su()
    s[6]['gorsel'] = acik_havuz()
    s[7]['gorsel'] = koli_istifleme()
    s[8]['gorsel'] = sivi_siralama_kartlari()
    s[9]['gorsel'] = kaptan_kaba_aktarma()
    s[11]['gorsel'] = iki_kup_birlestirme()
