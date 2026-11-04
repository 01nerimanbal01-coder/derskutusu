"""7. sınıf Matematik 8. hafta (Rasyonel Sayılarla Çok Adımlı İşlem Problemleri ve Cisimlerin Farklı Yönlerden Görünümleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
CAM, CAM_A = '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kesir(x, y, pay, payda, renk=LAC, boy=12):
    g = max(len(pay), len(payda)) * boy * 0.65 + 6
    ic = yazi(x, y - 4, pay, boy, renk)
    ic += f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" stroke="{renk}" stroke-width="1.5"/>'
    ic += yazi(x, y + boy + 1, payda, boy, renk)
    return ic


def dort_islem_karti_svg():
    kartlar = [
        ('1. Kart', '1', '−', '1', '3', '·', '3', '4', MAVI, MAVI_A),
        ('2. Kart', '1', 've', '2', '3', '÷', '4', '9', YES, YES_A),
        ('3. Kart', '2', '−', '1', '2', '·', '2', '5', TUR, TUR_A),
        ('4. Kart', '3', '−', '3', '4', '÷', '1', '2', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, tam, islem1, p1, q1, islem2, p2, q2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="84" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 24, bas, 12, renk)
        ic += yazi(x + 22, 60, tam, 12, LAC)
        ic += yazi(x + 40, 60, 'ekle' if islem1 == 've' else islem1, 12, renk)
        ic += kesir(x + 68, 56, p1, q1, LAC, 12)
        ic += yazi(x + 92, 60, islem2, 12, LAC)
        ic += kesir(x + 116, 56, p2, q2, LAC, 12)
    return svg(600, 96, ic, 'Dört çok adımlı rasyonel sayı işlem kartı.', 20)


def kat_plani_2x2_svg():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(140, 28, 'Üstten Kat Planı (2x2)', 12, MAVI)
    kareler = [
        (80, 38, '3', YES, YES_A),
        (136, 38, '2', TUR, TUR_A),
        (80, 68, '1', MOR, MOR_A),
        (136, 68, '4', MAVI, '#fff'),
    ]
    for x, y, s, r, a in kareler:
        ic += f'<rect x="{x}" y="{y}" width="52" height="26" rx="4" fill="{a}" stroke="{r}" stroke-width="1.5"/>'
        ic += yazi(x + 26, y + 18, s, 12, LAC)
    ic += yazi(405, 34, 'Bakış Yönleri ve Yükseklik Kuralı', 12, MAVI)
    ic += yazi(405, 58, 'Önden bakış : Her dikey sütundaki en büyük sayı', 12, LAC, ince=True)
    ic += yazi(405, 80, 'Sağdan bakış : Her yatay satırdaki en büyük sayı', 12, LAC, ince=True)
    return svg(600, 108, ic, '2x2 kodlanmış üst görünüm kat planı: üst satır 3 ve 2, alt satır 1 ve 4.', 20)


def su_deposu_problem_svg():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += f'<rect x="24" y="18" width="160" height="68" rx="8" fill="#fff" stroke="{CAM}" stroke-width="1.6"/>'
    ic += yazi(104, 42, '1. Kullanım', 12, CAM)
    ic += kesir(66, 64, '1', '3', LAC, 12)
    ic += yazi(118, 68, 'oranı', 12, LAC, ince=True)

    ic += f'<rect x="212" y="18" width="176" height="68" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 42, '2. Kullanım (Kalanın)', 12, TUR)
    ic += kesir(262, 64, '2', '5', LAC, 12)
    ic += yazi(318, 68, 'oranı', 12, LAC, ince=True)

    ic += f'<rect x="416" y="18" width="160" height="68" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(496, 44, 'Geriye Kalan Su', 12, YES)
    ic += yazi(496, 70, '36 Litre  ->  Tamamı: ?', 12, LAC)
    return svg(600, 104, ic, 'Su deposu kesir problemi aşamaları.', 20)


def onden_arkadan_simetri_svg():
    ic = f'<rect x="8" y="6" width="280" height="92" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(148, 26, 'Önden Görünüm (Soldan Sağa)', 12, MAVI)
    for k in range(3):
        ic += f'<rect x="70" y="{68 - k * 18}" width="24" height="18" fill="{MAVI}" stroke="#fff" stroke-width="1.2"/>'
    ic += f'<rect x="96" y="68" width="24" height="18" fill="{MAVI}" stroke="#fff" stroke-width="1.2"/>'
    for k in range(2):
        ic += f'<rect x="122" y="{68 - k * 18}" width="24" height="18" fill="{MAVI}" stroke="#fff" stroke-width="1.2"/>'
    ic += yazi(212, 58, 'Sütunlar: 3 - 1 - 2', 12, LAC)

    ic += f'<rect x="312" y="6" width="280" height="92" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(452, 26, 'Arkadan Görünüm (Ayna Simetriği)', 12, YES)
    ic += yazi(452, 56, 'Soldan sağa sütun sayıları:', 12, LAC, ince=True)
    ic += yazi(452, 78, '?  -  ?  -  ?', 12, KIR)
    return svg(600, 104, ic, 'Önden görünümü 3, 1, 2 olan yapının arkadan görünüm simetriği.', 20)


def tek_sira_kat_plani_svg():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(160, 30, 'Üstten Kat Planı (Tek Sıra)', 12, TUR)
    sayilar = [('Sol Sütun', '2', MAVI), ('Orta Sütun', '4', YES), ('Sağ Sütun', '1', MOR)]
    for i, (ad, s, r) in enumerate(sayilar):
        x = 40 + i * 90
        ic += f'<rect x="{x}" y="40" width="76" height="40" rx="6" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        ic += yazi(x + 38, 65, s, 12, r)
    ic += yazi(450, 44, 'Önden Bakış Yönü', 12, LAC)
    ic += yazi(450, 68, 'Sütun Yükseklikleri : 2 - 4 - 1', 12, MAVI)
    return svg(600, 98, ic, 'Soldan sağa 2, 4, 1 kat planı.', 20)


def merdivenli_islem_adim_svg():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(150, 30, 'Merdivenli Kesir İşlemi', 12, MOR)
    ic += yazi(72, 62, '2  −', 12, LAC)
    ic += yazi(132, 44, '3', 12, MAVI)
    ic += f'<line x1="104" y1="52" x2="164" y2="52" stroke="{KIR}" stroke-width="2.2"/>'
    ic += yazi(118, 72, '1 ve', 12, LAC)
    ic += kesir(150, 68, '1', '2', LAC, 12)
    ic += yazi(410, 42, '1. Adım: Paydadaki toplamı bul', 12, LAC, ince=True)
    ic += yazi(410, 64, '2. Adım: Ana çizgide bölmeyi yap', 12, LAC, ince=True)
    ic += yazi(410, 84, '3. Adım: 2 sayısından çıkar', 12, YES)
    return svg(600, 104, ic, 'Merdivenli kesir işlemi ve çözüm basamakları.', 20)


def gorunum_kurallari_pano():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'ÜÇ BOYUTLU YAPI GÖRÜNÜM İLKELERİ', 12, YES)
    ic += yazi(155, 52, 'Önden ve arkadan kare sayısı eşittir', 12, LAC, ince=True)
    ic += yazi(450, 52, 'Sağdan ve soldan görünümler simetriktir', 12, LAC, ince=True)
    ic += yazi(155, 74, 'Üstten görünüm taban planını verir', 12, LAC, ince=True)
    ic += yazi(450, 74, 'Derinlik farkı kare boyunu değiştirmez', 12, MAVI)
    return svg(600, 98, ic, 'Üç boyutlu birim küp yapılarının iki boyutlu görünüm ilkeleri.', 20)


def kup_cikarma_analiz_svg():
    ic = f'<rect x="8" y="6" width="584" height="90" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(145, 26, 'Kat Planı (Önden Bakış Alttan)', 12, TUR)
    ic += f'<rect x="76" y="34" width="56" height="24" rx="4" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(104, 51, '2 (Arka)', 12, MAVI)
    ic += f'<rect x="138" y="34" width="56" height="24" rx="4" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(166, 51, '2', 12, MAVI)
    ic += f'<rect x="76" y="62" width="56" height="24" rx="4" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(104, 79, 'K : 1', 12, KIR)
    ic += f'<rect x="138" y="62" width="56" height="24" rx="4" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(166, 79, '3', 12, YES)
    ic += yazi(418, 42, 'K : 1 küplük sütun yapıdan çıkarılıyor', 12, KIR)
    ic += yazi(418, 66, 'Arkasında 2 küplük sütun mevcuttur', 12, LAC, ince=True)
    return svg(600, 102, ic, 'Kat planından K küpünün çıkarılması analizi.', 20)


def bisiklet_parkuru_svg():
    ic = f'<rect x="8" y="6" width="584" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<rect x="22" y="18" width="166" height="64" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(88, 48, '1. Gün :', 12, MAVI)
    ic += kesir(148, 46, '2', '7', LAC, 12)

    ic += f'<rect x="210" y="18" width="166" height="64" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(276, 48, '2. Gün :', 12, TUR)
    ic += kesir(336, 46, '3', '7', LAC, 12)

    ic += f'<rect x="398" y="18" width="180" height="64" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(488, 42, 'Kalan Mesafe : 24 km', 12, YES)
    ic += yazi(488, 66, 'Toplam Parkur : ? km', 12, LAC)
    return svg(600, 100, ic, 'Bisiklet parkuru kesir problemi şeması.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_islem_karti_svg()
    s[1]['gorsel'] = kat_plani_2x2_svg()
    s[3]['gorsel'] = su_deposu_problem_svg()
    s[4]['gorsel'] = onden_arkadan_simetri_svg()
    s[6]['gorsel'] = tek_sira_kat_plani_svg()
    s[7]['gorsel'] = merdivenli_islem_adim_svg()
    s[8]['gorsel'] = gorunum_kurallari_pano()
    s[11]['gorsel'] = kup_cikarma_analiz_svg()
    s[12]['gorsel'] = bisiklet_parkuru_svg()
