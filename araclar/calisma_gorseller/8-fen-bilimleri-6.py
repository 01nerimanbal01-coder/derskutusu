"""8. sınıf Fen Bilimleri 6. hafta (Kalıtım ve Tek Karakter Çaprazlamaları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def caprazlama_kartlari():
    """Soru 1: Mor (M) ve Beyaz (m) çiçek rengi 4 çaprazlama kartı."""
    kartlar = [
        ('1. Çaprazlama', 'MM × mm', 'Mor × Beyaz', MOR, MOR_A),
        ('2. Çaprazlama', 'Mm × Mm', 'Melez × Melez', MAVI, MAVI_A),
        ('3. Çaprazlama', 'Mm × mm', 'Melez × Saf Çekinik', TUR, TUR_A),
        ('4. Çaprazlama', 'mm × mm', 'Beyaz × Beyaz', YES, YES_A),
    ]
    ic = ''
    for i, (bas, cap, acik, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 76, z, r, 8, 1.5)
        ic += yazi(x + 70, 26, bas, r)
        ic += yazi(x + 70, 50, cap, LAC)
        ic += yazi(x + 70, 70, acik, LAC, 'middle', True)
    return svg(600, 88, ic, 'Bezelye çiçek rengi dört çaprazlama kartı.', 12)


def mendel_bezelye_sema():
    """Soru 2: Mendel'in bezelye bitkisini seçme gerekçeleri şeması."""
    ic = kutu(4, 4, 352, 92, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Mendel Neden Bezelye Bitkisini Seçti?', KAHVE)
    kartlar = [
        ('Hızlı Üreme', 'Yılda birkaç döl', YES, YES_A, 10),
        ('Kapalı Çiçek', 'Yabancı tozlaşma yok', MAVI, MAVI_A, 126),
        ('Zıt Karakter', 'Mor-beyaz, sarı-yeşil', MOR, MOR_A, 242),
    ]
    for bas, alt, r, z, x in kartlar:
        ic += kutu(x, 28, 108, 60, z, r, 7, 1.3)
        ic += yazi(x + 54, 50, bas, r)
        ic += yazi(x + 54, 72, alt, LAC, 'middle', True)
    return svg(360, 100, ic, 'Mendel’in bezelye bitkisini tercih etme nedenleri şeması.', 12)


def kalitim_bilgi_panosu():
    """Soru 4: Baskın-çekinik alel ve bezelye karakterleri bilgi panosu."""
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Bezelyelerde Baskın ve Çekinik Karakter Panosu', MAVI)
    ic += kutu(12, 28, 162, 60, MOR_A, MOR, 7, 1.3)
    ic += yazi(93, 46, 'Baskın Alel (A, M, S)', MOR)
    ic += yazi(93, 66, 'Mor çiçek · Sarı tohum', LAC, 'middle', True)
    ic += yazi(93, 82, 'AA ve Aa’da etkisini gösterir', MOR, 'middle', True)
    ic += kutu(186, 28, 162, 60, YES_A, YES, 7, 1.3)
    ic += yazi(267, 46, 'Çekinik Alel (a, m, s)', YESIL_K)
    ic += yazi(267, 66, 'Beyaz çiçek · Yeşil tohum', LAC, 'middle', True)
    ic += yazi(267, 82, 'Yalnız aa’da ortaya çıkar', YESIL_K, 'middle', True)
    return svg(360, 100, ic, 'Bezelyelerde baskın ve çekinik karakterler bilgi panosu.', 12)


def sari_yesil_tohum_caprazlama():
    """Soru 6: Sarı tohumlu iki ata bezelyeden yeşil tohumlu bezelye elde edilmesi."""
    ic = kutu(4, 4, 352, 92, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Tohum Rengi Çaprazlama Gözlemi (S: Sarı, s: Yeşil)', KAHVE)
    ic += kutu(12, 30, 102, 56, TUR_A, TUR, 7, 1.3)
    ic += yazi(63, 52, '1. Ata Bezelye', TUR)
    ic += yazi(63, 73, 'Sarı Tohum (?)', LAC)
    ic += yazi(124, 62, '×', LAC)
    ic += kutu(134, 30, 102, 56, TUR_A, TUR, 7, 1.3)
    ic += yazi(185, 52, '2. Ata Bezelye', TUR)
    ic += yazi(185, 73, 'Sarı Tohum (?)', LAC)
    ic += yazi(246, 62, '→', LAC)
    ic += kutu(256, 30, 92, 56, YES_A, YES, 7, 1.4)
    ic += yazi(302, 52, 'Yavru Döl', YESIL_K)
    ic += yazi(302, 73, 'Yeşil (ss)', YESIL_K)
    return svg(360, 100, ic, 'İki sarı tohumlu ata bezelyeden yeşil tohumlu bezelye oluşumu şeması.', 12)


def punnett_karesi_kilavuzu():
    """Soru 7: Mm × Mm çaprazlaması Punnett karesi şeması."""
    ic = kutu(4, 4, 352, 94, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Punnett Karesi Kılavuzu (Mm × Mm)', MAVI)
    hucreler = [
        (16, 28, 'Aleller', 'M', 'm', MAVI_A, MAVI),
        (126, 28, 'M', 'MM (Saf)', 'Mm (Melez)', MOR_A, MOR),
        (236, 28, 'm', 'Mm (Melez)', 'mm (Saf)', YES_A, YES),
    ]
    for x, y, b, s1, s2, z, r in hucreler:
        ic += kutu(x, y, 104, 62, z, r, 6, 1.3)
        ic += yazi(x + 52, y + 18, b, r)
        ic += yazi(x + 52, y + 38, s1, LAC)
        ic += yazi(x + 52, y + 55, s2, LAC, 'middle', True)
    return svg(360, 102, ic, 'İki melez bezelyenin Punnett karesi eşleştirme kılavuzu.', 12)


def uzun_kisa_kontrol_caprazlama():
    """Soru 8: Uzun boylu bezelyenin genotipini (UU veya Uu) bulma şeması."""
    ic = kutu(4, 4, 352, 90, YES_A, YES, 8, 1.4)
    ic += yazi(180, 21, 'Bahçedeki Bezelyenin Genotipini Belirleme Deneyi', YESIL_K)
    ic += kutu(14, 28, 158, 56, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(93, 48, 'İncelenen Bezelye', MAVI)
    ic += yazi(93, 70, 'Uzun Boylu (UU veya Uu?)', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 56, TUR_A, TUR, 7, 1.3)
    ic += yazi(267, 48, 'Kontrol Bezelyesi', TUR)
    ic += yazi(267, 70, 'Kısa Boylu: uu (Saf çekinik)', LAC, 'middle', True)
    return svg(360, 98, ic, 'Uzun boylu bezelyenin UU mu Uu mu olduğunu anlamak için kontrol çaprazlaması.', 12)


def tohum_sekli_sutun_grafigi():
    """Soru 9: K × L çaprazlaması sonucu %50 düzgün, %50 buruşuk tohum grafiği."""
    ic = kutu(4, 4, 352, 94, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'K × L Çaprazlaması Fenotip Oranı Grafiği', LAC)
    ic += f'<line x1="48" y1="80" x2="320" y2="80" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<line x1="48" y1="28" x2="48" y2="80" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(32, 46, '%50', MAVI)
    ic += f'<line x1="48" y1="42" x2="310" y2="42" stroke="{GRI}" stroke-width="1" stroke-dasharray="4 3"/>'
    ic += kutu(88, 42, 76, 38, MAVI_A, MAVI, 4, 1.4)
    ic += yazi(126, 65, '%50 Düzgün', MAVI)
    ic += kutu(204, 42, 76, 38, TUR_A, TUR, 4, 1.4)
    ic += yazi(242, 65, '%50 Buruşuk', TUR)
    return svg(360, 102, ic, 'K ve L bezelyelerinin çaprazlanmasında yüzde 50 düzgün, yüzde 50 buruşuk tohum grafiği.', 12)


def esey_kromozomu_aktarimi():
    """Soru 10: İnsanda eşey kromozomları (44+XX × 44+XY) aktarımı şeması."""
    ic = kutu(4, 4, 352, 92, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 21, 'Eşey Kromozomlarının Yavru Döllere Aktarımı', MOR)
    ic += kutu(12, 28, 158, 26, KIR_A, KIR, 6, 1.2)
    ic += yazi(91, 45, 'Dişi (44+XX) → Yumurta: X', KIR)
    ic += kutu(190, 28, 158, 26, MAVI_A, MAVI, 6, 1.2)
    ic += yazi(269, 45, 'Erkek (44+XY) → Sperm: X, Y', MAVI)
    ic += kutu(12, 60, 336, 28, YES_A, YES, 6, 1.2)
    ic += yazi(180, 78, 'Yavrular: %50 Kız (44+XX) · %50 Erkek (44+XY)', YESIL_K)
    return svg(360, 100, ic, 'İnsanda 44+XX ve 44+XY eşey kromozomlarının aktarımı modeli.', 12)


def dorduncu_cocuk_olasilik_karti():
    """Soru 13: Üç erkek çocuktan sonra 4. çocuğun kız olma olasılığı kartı."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Bağımsız Olasılık ve Cinsiyet Kalıtımı Kartı', MAVI)
    kutular = [
        ('1. Çocuk', 'XY (Erkek)', MAVI, '#fff', 12),
        ('2. Çocuk', 'XY (Erkek)', MAVI, '#fff', 96),
        ('3. Çocuk', 'XY (Erkek)', MAVI, '#fff', 180),
        ('4. Çocuk', 'XX Olasılığı: ?', KIR, KIR_A, 264),
    ]
    for bas, alt, r, z, x in kutular:
        ic += kutu(x, 28, 78, 54, z, r, 6, 1.3)
        ic += yazi(x + 39, 48, bas, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 96, ic, 'Üç erkek çocuktan sonra dördüncü çocuğun kız olma olasılığı kartı.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = caprazlama_kartlari()
    s[1]['gorsel'] = mendel_bezelye_sema()
    s[3]['gorsel'] = kalitim_bilgi_panosu()
    s[5]['gorsel'] = sari_yesil_tohum_caprazlama()
    s[6]['gorsel'] = punnett_karesi_kilavuzu()
    s[7]['gorsel'] = uzun_kisa_kontrol_caprazlama()
    s[8]['gorsel'] = tohum_sekli_sutun_grafigi()
    s[9]['gorsel'] = esey_kromozomu_aktarimi()
    s[12]['gorsel'] = dorduncu_cocuk_olasilik_karti()
