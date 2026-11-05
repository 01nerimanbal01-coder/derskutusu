"""5. sınıf Matematik 13. hafta (Dört İşlem Problemleri ve Dikdörtgenin Çevre-Alan İlişkisi) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115, mm=20):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ikili_kart(b1, s1a, s1b, r1, z1, b2, s2a, s2b, r2, z2, etiket, ar1=False, ar2=False):
    ic = kutu(6, 6, 170, 103, z1, r1)
    ic += yazi(91, 28, b1, r1, kalin=True)
    ic += (ar_yazi(91, 60, s1a, LAC) if ar1 else yazi(91, 58, s1a, LAC, kalin=True))
    ic += yazi(91, 90, s1b, r1)
    ic += kutu(184, 6, 170, 103, z2, r2)
    ic += yazi(269, 28, b2, r2, kalin=True)
    ic += (ar_yazi(269, 60, s2a, LAC) if ar2 else yazi(269, 58, s2a, LAC, kalin=True))
    ic += yazi(269, 90, s2b, r2)
    return svg(ic, etiket)


def dortlu_kart(kartlar, etiket, ar=False):
    konum = [(6, 6), (184, 6), (6, 60), (184, 60)]
    ic = ''
    for (x, y), (b1, b2, r, z) in zip(konum, kartlar):
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += (ar_yazi(x + 85, y + 41, b2, LAC) if ar else yazi(x + 85, y + 39, b2, LAC))
    return svg(ic, etiket)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ikili_kart(
        'Kat Modeli (Toplam = 120)', 'Silgi: [1 Kutu] · Kalem: [3 Kutu + 8]', 'Toplam = 4 Kutu + 8 = 120', MAVI, MAVI_A,
        'Çözüm Adımları', '1) Fazlalığı çıkar: 120 − 8 = 112', '2) 4’e böl: 112 ÷ 4 = ?', YES, YES_A,
        'Kat modeliyle kalem ve silgi problemi çözüm şeması.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Dikdörtgen (1 cm × 9 cm)', 'Çevre = 20 cm · Alan = 9 br²', KIR, KIR_A),
        ('2. Dikdörtgen (2 cm × 8 cm)', 'Çevre = 20 cm · Alan = ? br²', TUR, TUR_A),
        ('3. Dikdörtgen (3 cm × 7 cm)', 'Çevre = 20 cm · Alan = ? br²', MAVI, MAVI_A),
        ('4. Dikdörtgen (4 cm × 6 cm)', 'Çevre = 20 cm · Alan = 24 br²', YES, YES_A),
    ], 'Çevresi 20 cm olan dört farklı dikdörtgenin kenar ve alanları.')
    s[5]['gorsel'] = ikili_kart(
        'İleriye Doğru İşlem', '[Sayı] → (× 4) → (− 18) = 82', '4 katının 18 eksiği 82', TUR, TUR_A,
        'Tersinden Çalışma Çözümü', '1) 82 + 18 = 100', '2) 100 ÷ 4 = ?', CAM, CAM_A,
        'Tersinden çalışma stratejisiyle başlangıç sayısını bulma.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('K Dikdörtgeni (3 cm ve 11 cm)', 'Yarı çevre: 3 + 11 = 14 cm', YES, YES_A),
        ('L Dikdörtgeni (5 cm ve 9 cm)', 'Yarı çevre: 5 + 9 = 14 cm', MAVI, MAVI_A),
        ('M Dikdörtgeni (6 cm ve 8 cm)', 'Yarı çevre: 6 + 8 = 14 cm', MOR, MOR_A),
        ('N Dikdörtgeni (4 cm ve 12 cm)', 'Yarı çevre: 4 + 12 = 16 cm (!)', KIR, KIR_A),
    ], 'Dört dikdörtgenin yarı çevre ve çevre uzunluğu kontrolü.')
    s[7]['gorsel'] = ikili_kart(
        'Bahçe Teli Uzunluğu', 'Çevre = 24 m → Yarı Çevre = 12 m', 'Kısa + Uzun = 12 m', YES, YES_A,
        'Olası Kenar Çiftleri', '(1,11) (2,10) (3,9) (4,8)', 'En yakın: (5,7 → 35) ve (6,6 → 36)', MAVI, MAVI_A,
        '24 m çevreli bahçede en büyük alanı veren kenar seçimi.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1 cm × 11 cm (Çevre = 24 cm)', 'Alan = 1 × 11 = 11 br²', KIR, KIR_A),
        ('2 cm × 10 cm (Çevre = 24 cm)', 'Alan = 2 × 10 = 20 br²', TUR, TUR_A),
        ('4 cm × 8 cm (Çevre = 24 cm)', 'Alan = 4 × 8 = 32 br²', MAVI, MAVI_A),
        ('5 cm × 7 cm (Çevre = 24 cm)', 'Alan = 5 × 7 = 35 br²', YES, YES_A),
    ], 'Sabit 24 cm çevreli dört dikdörtgenin alan karşılaştırması.')
    s[9]['gorsel'] = ikili_kart(
        'A Paketi (20 GB Kullanım)', 'Sabit: 350 TL + (20 × 20 TL)', 'Toplam = 350 + 400 = 750 TL', TUR, TUR_A,
        'B Paketi (20 GB Kullanım)', 'Sabit: 500 TL + (20 × 10 TL)', 'Toplam = 500 + 200 = 700 TL', YES, YES_A,
        'A ve B internet paketlerinin 20 GB için maliyet karşılaştırması.'
    )
    s[11]['gorsel'] = ikili_kart(
        'P Dikdörtgeni (Uzak Kenarlar)', 'Kısa: 2 cm · Uzun: 9 cm', 'Çevre = 22 cm · Alan = 18 br²', MOR, MOR_A,
        'R Dikdörtgeni (Yakın Kenarlar)', 'Kısa: 5 cm · Uzun: 6 cm', 'Çevre = 22 cm · Alan = 30 br²', YES, YES_A,
        'Eşit çevreli (22 cm) P ve R dikdörtgenlerinin alan karşılaştırması.'
    )
