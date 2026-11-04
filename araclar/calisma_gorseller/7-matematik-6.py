"""7. sınıf Matematik 6. hafta (Rasyonel Sayılarla İşlemler ve Problem Çözme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); eğik kesir yok (K155); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dikey_kesir(cx, cy, isaret, pay, payda, renk=LAC):
    """Dikey kesir çizer (K155 uyumlu, eğik çizgi yok)."""
    ic = ''
    dx = 0
    if isaret:
        ic += yazi(cx - 14, cy + 4, isaret, renk)
        dx = 6
    ic += yazi(cx + dx, cy - 5, str(pay), renk)
    ic += f'<line x1="{cx + dx - 10}" y1="{cy - 1}" x2="{cx + dx + 10}" y2="{cy - 1}" stroke="{renk}" stroke-width="1.5"/>'
    ic += yazi(cx + dx, cy + 13, str(payda), renk)
    return ic


def islem_agaci_sema():
    """Soru 1: Rasyonel sayılarla işlem ağacı şeması: A = (-1/2) + (3/4) = 1/4, B = -4/3, C = A . B = -1/3 -> wait: dogru=2 (+1/3) so let's make B = +4/3."""
    ic = kutu(4, 4, 352, 92, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Rasyonel Sayılar İşlem Şeması', MAVI)
    ic += kutu(12, 28, 154, 60, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(89, 44, 'A Kutusu (Toplama)', MAVI)
    ic += dikey_kesir(48, 68, '−', 1, 2, LAC)
    ic += yazi(76, 72, '+', LAC)
    ic += dikey_kesir(102, 68, '+', 3, 4, LAC)
    ic += yazi(138, 72, '= A', MAVI)

    ic += kutu(194, 28, 154, 60, YES_A, YES, 7, 1.3)
    ic += yazi(271, 44, 'C Kutusu (Çarpma)', YESIL_K)
    ic += yazi(222, 72, 'A · (', LAC)
    ic += dikey_kesir(258, 68, '+', 4, 3, LAC)
    ic += yazi(298, 72, ') = C', YESIL_K)
    return svg(360, 100, ic, 'Rasyonel sayılarla toplama ve çarpma işlem şeması.', 20)


def ters_eleman_kartlari():
    """Soru 2: Toplamaya ve çarpmaya göre ters kartları."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Toplamaya ve Çarpmaya Göre Ters Kuralları', KAHVE)
    ic += kutu(12, 28, 162, 54, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(93, 47, 'Toplamaya Göre Ters', MAVI)
    ic += yazi(93, 69, 'Yalnız İŞARET değişir', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 54, MOR_A, MOR, 7, 1.3)
    ic += yazi(267, 47, 'Çarpmaya Göre Ters', MOR)
    ic += yazi(267, 69, 'Pay ile payda yer değiştirir', LAC, 'middle', True)
    return svg(360, 96, ic, 'Toplamaya ve çarpmaya göre ters kuralları bilgi kartı.', 19)


def kuvvet_kartlari():
    """Soru 4: K = (-1/2)^2 ve L = (-1/2)^3 kuvvet kartları."""
    ic = kutu(4, 4, 352, 88, '#f8fafc', GRI, 8, 1.3)
    ic += kutu(12, 12, 160, 72, MAVI_A, MAVI, 7, 1.4)
    ic += yazi(92, 30, 'K Kartı (Karesi)', MAVI)
    ic += yazi(60, 60, 'K = (', LAC)
    ic += dikey_kesir(92, 56, '−', 1, 2, LAC)
    ic += yazi(124, 52, ')²', MAVI)

    ic += kutu(188, 12, 160, 72, TUR_A, TUR, 7, 1.4)
    ic += yazi(268, 30, 'L Kartı (Küpü)', TUR)
    ic += yazi(236, 60, 'L = (', LAC)
    ic += dikey_kesir(268, 56, '−', 1, 2, LAC)
    ic += yazi(300, 52, ')³', TUR)
    return svg(360, 96, ic, 'Eksi bir bölü ikinin karesi ve küpü kartları.', 19)


def merdivenli_kesir_kartlari():
    """Soru 5: Ana kesir çizgisi karşılaştırma kartları."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 8, 1.4)
    ic += yazi(180, 21, 'Ana Kesir Çizgisinin Konumu', YESIL_K)
    ic += kutu(14, 28, 158, 54, '#fff', MAVI, 6, 1.2)
    ic += yazi(62, 58, 'A =', MAVI)
    ic += dikey_kesir(104, 54, '', 4, 3, LAC)
    ic += yazi(138, 58, '÷ 2', LAC)

    ic += kutu(188, 28, 158, 54, '#fff', TUR, 6, 1.2)
    ic += yazi(234, 58, 'B = 4 ÷', TUR)
    ic += dikey_kesir(292, 54, '', 3, 2, LAC)
    return svg(360, 96, ic, 'Ana kesir çizgisine göre iki farklı bölme işlemi kartı.', 19)


def zeytinyagi_bidonu_sema():
    """Soru 7: Kalanın kesri zeytinyağı bidonu problemi şeması."""
    adimlar = [
        ('1. Dolum', 'Bütünün çeyreği', MAVI, MAVI_A, 8),
        ('2. Dolum', 'Kalanın üçte biri', TUR, TUR_A, 126),
        ('Kalan Miktar', '18 litre zeytinyağı', YES, YES_A, 244),
    ]
    ic = kutu(4, 4, 352, 90, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Zeytinyağı Bidonu Dolum Aşamaları', KAHVE)
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 28, 108, 56, z, r, 7, 1.3)
        ic += yazi(x + 54, 48, bas, r)
        ic += yazi(x + 54, 70, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Zeytinyağı bidonunun aşamalı dolum ve kalan miktar şeması.', 19)


def islem_onceligi_kilavuzu():
    """Soru 8: İşlem önceliği 4 basamaklı kılavuz şeması."""
    basamaklar = [
        ('1. Adım', 'Üslü İfadeler', MOR, MOR_A, 6),
        ('2. Adım', 'Parantez İçi', MAVI, MAVI_A, 94),
        ('3. Adım', 'Çarpma · Bölme', TUR, TUR_A, 182),
        ('4. Adım', 'Toplama · Çıkarma', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in basamaklar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Çok adımlı işlemlerde dört basamaklı işlem önceliği kılavuzu.', 18)


def dikdortgen_bahce_sema():
    """Soru 9: Kısa kenarı 6/5 dam, uzun kenarı 15/4 dam olan dikdörtgen bahçe."""
    ic = kutu(4, 4, 352, 92, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Dikdörtgen Bahçe Alan Hesabı (Alan = Kısa × Uzun)', YESIL_K)
    ic += kutu(44, 28, 190, 56, '#fff', YES, 6, 1.5)
    ic += yazi(139, 54, 'Bahçe Alanı = ?', YESIL_K)
    ic += yazi(139, 73, 'Uzun kenar: 15 ÷ 4 dam', LAC, 'middle', True)
    ic += kutu(246, 28, 98, 56, MAVI_A, MAVI, 6, 1.3)
    ic += yazi(295, 48, 'Kısa Kenar', MAVI)
    ic += dikey_kesir(295, 68, '', 6, 5, LAC)
    return svg(360, 100, ic, 'Kenar uzunlukları rasyonel sayı olan dikdörtgen bahçe şeması.', 20)


def parkur_mesafe_karti():
    """Soru 12: 135 km parkur 1. gün ve 2. gün ilerleme şeması."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, '135 Kilometrelik Doğa Parkuru İlerleme Şeması', MAVI)
    bolumler = [
        ('1. Gün', '9 parçada 2’si', MAVI, '#fff', 12),
        ('2. Gün', '9 parçada 4’ü', TUR, TUR_A, 128),
        ('Kalan Yol', '? kilometre', YES, YES_A, 244),
    ]
    for bas, alt, r, z, x in bolumler:
        ic += kutu(x, 28, 104, 52, z, r, 6, 1.3)
        ic += yazi(x + 52, 47, bas, r)
        ic += yazi(x + 52, 68, alt, LAC, 'middle', True)
    return svg(360, 96, ic, '135 kilometrelik parkurun birinci ve ikinci gün ilerleme şeması.', 19)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = islem_agaci_sema()
    s[1]['gorsel'] = ters_eleman_kartlari()
    s[3]['gorsel'] = kuvvet_kartlari()
    s[4]['gorsel'] = merdivenli_kesir_kartlari()
    s[6]['gorsel'] = zeytinyagi_bidonu_sema()
    s[7]['gorsel'] = islem_onceligi_kilavuzu()
    s[8]['gorsel'] = dikdortgen_bahce_sema()
    s[11]['gorsel'] = parkur_mesafe_karti()
