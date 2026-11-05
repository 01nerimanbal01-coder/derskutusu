"""6. sınıf Fen Bilimleri 10. hafta (Hayvanlarda ve İnsanda Üreme, Büyüme ve Gelişme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def omurgali_gruplari_kartlari():
    kartlar = [
        ('1. Kart · Memeliler', 'Yunus, Yarasa, Sincap', YES, YES_A),
        ('2. Kart · Kuşlar', 'Penguen, Deve Kuşu, Kartal', MAVI, MAVI_A),
        ('3. Kart · Sürüngenler', 'Timsah, Kaplumbağa', TUR, TUR_A),
        ('4. Kart · Su Canlıları', 'Semender, Kurbağa, Alabalık', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Dört omurgalı hayvan grubu örnek kartları.', 16)


def omurgali_karsilastirma_panosu():
    kartlar = [
        ('1. Güvercin', 'Yumurtlar · Bakım var', MAVI, MAVI_A),
        ('2. Kurbağa', 'Yumurtlar · Başkalaşım (?)', YES, YES_A),
        ('3. Balina', 'Doğurur (?) · Süt verir', TUR, TUR_A),
        ('4. Kertenkele', 'Yumurtlar · Bakım yok (?)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 8.8, LAC, ince=True)
    return svg(360, 84, ic, 'Güvercin, kurbağa, balina ve kertenkelenin üreme özellikleri.', 15)


def disi_ureme_yapilari_sema():
    kartlar = [
        ('K · Yumurtalık', 'Yumurta hücresini üretir', MAVI, MAVI_A),
        ('L · Yumurta Kanalı', 'Döllenme burada olur', YES, YES_A),
        ('M · Döl Yatağı', 'Embriyo burada gelişir', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 104}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 56, 56, alt, 9.1, LAC, ince=True)
    return svg(360, 86, ic, 'Dişi üreme sistemindeki K, L ve M yapılarının görev şeması.', 15)


def baskalasim_evreleri_panosu():
    ic = kutu(6, 6, 348, 38, CAM_A, CAM)
    ic += yazi(180, 20, '1. Kurbağada Başkalaşım Sırası:', 9.8, CAM)
    ic += yazi(180, 36, 'Yumurta  →  [ (1) ? ]  →  Bacaklı İribaş  →  Genç ve Ergin Kurbağa', 9.2, LAC)

    ic += kutu(6, 50, 348, 38, MOR_A, MOR)
    ic += yazi(180, 64, '2. Kelebekte Başkalaşım Sırası:', 9.8, MOR)
    ic += yazi(180, 80, 'Yumurta  →  Larva (Tırtıl)  →  [ (2) ? ]  →  Ergin Kelebek', 9.2, LAC)
    return svg(360, 94, ic, 'Kurbağa ve kelebekte başkalaşım evreleri şeması.', 16)


def sperm_yumurta_karti():
    ic = kutu(6, 6, 170, 76, MOR_A, MOR)
    ic += yazi(91, 22, 'Dişi Üreme Hücresi: Yumurta', 9.8, MOR)
    ic += yazi(91, 44, '• Büyük ve bol sitoplazmalı', 9.3, LAC, ince=True)
    ic += yazi(91, 64, '• Kamçısız ve hareketsiz', 9.3, MOR)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'Erkek Üreme Hücresi: Sperm', 9.8, MAVI)
    ic += yazi(269, 44, '• Küçük ve az sitoplazmalı', 9.3, LAC, ince=True)
    ic += yazi(269, 64, '• Kuyruklu (kamçılı) ve hareketli', 9.3, MAVI)
    return svg(360, 88, ic, 'Yumurta ve sperm hücrelerinin yapısal karşılaştırma kartı.', 15)


def embriyo_gelisim_zinciri():
    adimlar = [
        ('1. Hücreler', 'Sperm + Yumurta', MAVI, MAVI_A),
        ('2. Döllenme', 'Zigot (İlk hücre)', YES, YES_A),
        ('3. Tutunma', 'Embriyo (Rahim)', TUR, TUR_A),
        ('4. Gelişim', 'Fetüs → Bebek', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += yazi(x + 41, 54, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Üreme hücrelerinden bebeğe gelişim sırası.', 15)


def kus_memeli_venn_karti():
    ic = kutu(6, 6, 110, 76, MAVI_A, MAVI)
    ic += yazi(61, 24, 'Kuşlar', 10.2, MAVI)
    ic += yazi(61, 46, '• Yumurta ile ürer', 9.0, LAC, ince=True)
    ic += yazi(61, 64, '• Kuluçkaya yatar', 9.0, LAC, ince=True)

    ic += kutu(125, 6, 110, 76, YES_A, YES)
    ic += yazi(180, 24, 'Ortak Bölge (X)', 10.2, YESIL_K)
    ic += yazi(180, 46, '• Omurgalı olma', 9.0, LAC)
    ic += yazi(180, 64, '• Yavru bakımı', 9.0, YESIL_K)

    ic += kutu(244, 6, 110, 76, TUR_A, TUR)
    ic += yazi(299, 24, 'Memeliler', 10.2, TUR)
    ic += yazi(299, 46, '• Doğurarak ürer', 9.0, LAC, ince=True)
    ic += yazi(299, 64, '• Sütle besler', 9.0, LAC, ince=True)
    return svg(360, 88, ic, 'Kuşlar ve memelilerin özelliklerini karşılaştıran şema.', 15)


def kurbaga_solunum_degisimi():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, '1. Evre: İribaş (Suda)', 10.1, CAM)
    ic += yazi(91, 44, 'Yumurtadaki besin az olduğu için', 9.1, LAC, ince=True)
    ic += yazi(91, 64, 'balık gibi solungaç solunumu yapar.', 9.2, CAM)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Evre: Ergin Kurbağa', 10.1, YESIL_K)
    ic += yazi(269, 44, 'Kuyruk kaybolur, bacaklar çıkar;', 9.1, LAC, ince=True)
    ic += yazi(269, 64, 'akciğer ve deri solunumu yapar.', 9.2, YESIL_K)
    return svg(360, 88, ic, 'İribaş ve ergin kurbağanın başkalaşım ve solunum farkı kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = omurgali_gruplari_kartlari()
    s[2]['gorsel'] = omurgali_karsilastirma_panosu()
    s[5]['gorsel'] = disi_ureme_yapilari_sema()
    s[6]['gorsel'] = baskalasim_evreleri_panosu()
    s[7]['gorsel'] = sperm_yumurta_karti()
    s[8]['gorsel'] = embriyo_gelisim_zinciri()
    s[9]['gorsel'] = kus_memeli_venn_karti()
    s[11]['gorsel'] = kurbaga_solunum_degisimi()
