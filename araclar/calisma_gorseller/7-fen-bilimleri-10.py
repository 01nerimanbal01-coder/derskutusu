"""7. sınıf Fen Bilimleri 10. hafta (Sindirim Sistemi: Fiziksel ve Kimyasal Sindirim, Sindirim Kanalı ve Yardımcı Organlar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def fiziksel_kimyasal_pano():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Fiziksel (Mekanik) Sindirim', 10.0, MAVI)
    ic += yazi(91, 44, '• Enzim KULLANILMAZ', 9.5, LAC, ince=True)
    ic += yazi(91, 64, '• Diş, mide kası, safra sıvısı', 9.4, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Kimyasal Sindirim', 10.0, YES)
    ic += yazi(269, 44, '• Su ve ENZİM kullanılır', 9.5, LAC, ince=True)
    ic += yazi(269, 64, '• Ağız, mide ve ince bağırsak', 9.4, YES)
    return svg(360, 88, ic, 'Fiziksel ve kimyasal sindirim karşılaştırma panosu.', 15)


def besin_sindirim_kartlari():
    kartlar = [
        ('1. Karbonhidrat', 'Ağız -> İnce B.', MAVI, MAVI_A),
        ('2. Protein', '? -> İnce B.', KIR, KIR_A),
        ('3. Yağlar', '? -> ?', TUR, TUR_A),
        ('4. Su / Vitamin', 'Sindirilmez', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.8"/>'
        ic += yazi(x + 41, 54, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Dört besin grubunun kimyasal sindirim kartları.', 14)


def sindirim_kanali_klmn():
    organlar = [
        ('K · Yemek B.', 'İletim (Sindirim yok)', MAVI, MAVI_A),
        ('L · Mide', 'Protein başlar', TUR, TUR_A),
        ('M · İnce B.', 'Sindirim biter + Villus', YES, YES_A),
        ('N · Kalın B.', 'Su/Mineral emilimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(organlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += yazi(x + 41, 52, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Sindirim kanalında K, L, M ve N organlarının görevleri.', 14)


def yardimci_organlar_xy():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'Karaciğer → X Salgısı', 10.0, TUR)
    ic += yazi(91, 44, 'Enzim içermez, yağları', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'damlacıklara ayırır (Fiziksel)', 9.3, TUR)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'Pankreas → Y Salgısı', 10.0, MOR)
    ic += yazi(269, 44, 'Enzim içerir; karbonhidrat,', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'protein ve yağı kimyasal sindirir', 9.3, MOR)
    return svg(360, 88, ic, 'Karaciğerin X (safra) ve pankreasın Y (pankreas öz suyu) salgıları.', 15)


def zeytinyagi_tup_deneyi():
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Deney Tüpü', 10.0, MAVI)
    ic += yazi(91, 43, '10 mL Zeytinyağı', 9.4, LAC, ince=True)
    ic += yazi(91, 63, '+ Yalnız Pankreas Öz Suyu', 9.3, MAVI)

    ic += kutu(184, 6, 170, 74, YES_A, YES)
    ic += yazi(269, 22, '2. Deney Tüpü', 10.0, YES)
    ic += yazi(269, 43, '10 mL Zeytinyağı + Safra', 9.4, LAC, ince=True)
    ic += yazi(269, 63, '+ Pankreas Öz Suyu', 9.3, YES)
    return svg(360, 86, ic, 'Zeytinyağı üzerine safra ve pankreas öz suyu etki deneyi.', 14)


def sindirim_yolculuk_seridi():
    adimlar = [
        ('1. Ağız-Yutak', 'Çiğneme + Tükürük', MAVI, MAVI_A),
        ('2. Yemek Borusu', 'Kaslarla İletim', CAM, CAM_A),
        ('3. Mide', 'Mide Öz Suyu', TUR, TUR_A),
        ('4. Bağırsaklar', 'Emilim ve Atım', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += yazi(x + 41, 52, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'Sindirim kanalında besinlerin izlediği dört aşamalı yol.', 14)


def besin_degisim_grafik():
    kartlar = [
        (6, 'X Besini', 'Ağızda azalmaya başlar', 'İnce bağırsakta biter', MAVI, MAVI_A),
        (124, 'Y Besini', 'Midede azalmaya başlar', 'İnce bağırsakta biter', KIR, KIR_A),
        (242, 'Z Besini', 'İnce bağırsakta başlar', 'İnce bağırsakta biter', TUR, TUR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 22, bas, 10.0, r)
        ic += yazi(x + 56, 44, s1, 9.1, LAC, ince=True)
        ic += yazi(x + 56, 64, s2, 9.1, r)
    return svg(360, 88, ic, 'X, Y ve Z besinlerinin kimyasal sindirim başlangıç ve bitiş kartları.', 15)


def ince_kalin_emilim_karti():
    ic = kutu(6, 6, 170, 74, YES_A, YES)
    ic += yazi(91, 22, 'İnce Bağırsakta Emilim', 10.0, YES)
    ic += yazi(91, 43, '• Villus (tümür) çıkıntıları VAR', 9.3, LAC, ince=True)
    ic += yazi(91, 63, '• Sindirilmiş besinler kana geçer', 9.2, YES)

    ic += kutu(184, 6, 170, 74, MOR_A, MOR)
    ic += yazi(269, 22, 'Kalın Bağırsakta Emilim', 10.0, MOR)
    ic += yazi(269, 43, '• Villus çıkıntıları YOK (Sindirim yok)', 9.3, LAC, ince=True)
    ic += yazi(269, 63, '• Kalan su, vitamin ve mineral emilir', 9.2, MOR)
    return svg(360, 86, ic, 'İnce bağırsak ve kalın bağırsakta gerçekleşen emilim karşılaştırması.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = fiziksel_kimyasal_pano()
    s[2]['gorsel'] = besin_sindirim_kartlari()
    s[5]['gorsel'] = sindirim_kanali_klmn()
    s[6]['gorsel'] = yardimci_organlar_xy()
    s[7]['gorsel'] = zeytinyagi_tup_deneyi()
    s[8]['gorsel'] = sindirim_yolculuk_seridi()
    s[9]['gorsel'] = besin_degisim_grafik()
    s[11]['gorsel'] = ince_kalin_emilim_karti()
