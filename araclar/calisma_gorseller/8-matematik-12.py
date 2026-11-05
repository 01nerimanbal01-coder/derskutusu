"""8. sınıf Matematik 12. hafta (Grafikler Arası Dönüşümler ve Basit Olayların Olma Olasılığına Giriş) görselleri.
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


def spor_kursu_sutun():
    ic = kutu(6, 6, 178, 103, MAVI_A, MAVI)
    ic += yazi(95, 22, 'Spor Kursu Öğrenci Sayısı', MAVI, kalin=True)
    barlar = [(22, 52, 36, 'Yüzme:18', CAM), (76, 64, 24, 'Tenis:12', YES), (130, 48, 40, 'Okçuluk:18', TUR)]
    for x, y, h, et, r in barlar:
        ic += f'<rect x="{x}" y="{y}" width="38" height="{h}" rx="3" fill="{r}"/>'
        ic += yazi(x + 19, 102, et, LAC, kalin=True)
    ic += kutu(192, 6, 162, 103, YES_A, YES)
    ic += yazi(273, 28, 'Daire Grafiğine Dönüşüm', YES, kalin=True)
    ic += yazi(273, 54, 'Toplam = 18 + 12 + 18 = 48 kişi', LAC)
    ic += yazi(273, 78, '48 kişi → 360° ise', LAC, kalin=True)
    ic += yazi(273, 98, 'Yüzme (18 kişi) → ?°', KIR, kalin=True)
    return svg(ic, 'Spor kursu sütun grafiğinin daire grafiğine dönüştürülmesi.')


def tahil_ebob_daire():
    ic = kutu(6, 6, 166, 103, TUR_A, TUR)
    ic += f'<circle cx="89" cy="56" r="36" fill="#fef3c7" stroke="{TUR}" stroke-width="1.5"/>'
    ic += f'<line x1="89" y1="56" x2="89" y2="20" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="89" y1="56" x2="125" y2="56" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="89" y1="56" x2="62" y2="80" stroke="{LAC}" stroke-width="1.3"/>'
    ic += yazi(89, 103, 'Toplam: 720 Ton Tahıl', TUR, kalin=True)
    ic += kutu(180, 6, 174, 103, YES_A, YES)
    ic += yazi(267, 26, 'EBOB(90°,120°,150°) = 30°', YES, kalin=True)
    ic += yazi(267, 50, 'Arpa: 90° → 3k', LAC)
    ic += yazi(267, 72, 'Mısır: 120° → 4k', LAC)
    ic += yazi(267, 94, 'Buğday: 150° → 5k (12k=720)', MAVI, kalin=True)
    return svg(ic, 'Tahıl üretimi daire grafiğinde EBOB kat yöntemi şeması.')


def coklu_grafik_galeri():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, '1. Grafik: 120 Aracın Türü', MAVI, kalin=True)
    ic += yazi(92, 52, 'Otomobil Merkez Açısı: 216°', LAC, kalin=True)
    ic += yazi(92, 76, 'Kamyonet: 144°', LAC)
    ic += yazi(92, 98, 'Otomobil = 120 × (216/360) = 72', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 24, '2. Grafik: Otomobil Yakıtı', YES, kalin=True)
    ic += yazi(269, 52, 'Elektrikli Merkez Açısı: 120°', KIR, kalin=True)
    ic += yazi(269, 76, 'Hibrit: 150° · Benzin: 90°', LAC)
    ic += yazi(269, 98, 'Elektrikli = 72 × (120/360) = ?', YES, kalin=True)
    return svg(ic, '120 araçlık galeride iki daire grafiğiyle elektrikli otomobil hesabı.')


def on_iki_top_kutusu():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 24, 'Olasılık Deneyi: 1’den 12’ye Kadar Numaralanmış Özdeş Toplar', MOR, kalin=True)
    for i in range(1, 13):
        x = 12 + (i - 1) * 28
        ic += f'<circle cx="{x + 12}" cy="56" r="11" fill="#ffffff" stroke="{MOR}" stroke-width="1.3"/>'
        ic += yazi(x + 12, 60, str(i), LAC, kalin=True)
    ic += yazi(180, 96, 'Olası Durumlar: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} (12 Çıktı)', MAVI, kalin=True)
    return svg(ic, '1’den 12’ye kadar numaralanmış 12 özdeş top modeli.')


def fidan_boyu_cizgi():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 22, 'Bir Fidanın 4 Aylık Boy Değişimi Çizgi Grafiği (cm)', YES, kalin=True)
    ic += f'<polyline points="42,84 110,72 180,60 250,48 318,36" fill="none" stroke="{YES}" stroke-width="2.2"/>'
    noktalar = [(42, 84, 'Dikim: 20'), (110, 72, '1.Ay: 27'), (180, 60, '2.Ay: 34'), (250, 48, '3.Ay: 41'), (318, 36, '4.Ay: 48')]
    for x, y, et in noktalar:
        ic += f'<circle cx="{x}" cy="{y}" r="4" fill="{KIR}"/>'
        ic += yazi(x, 102, et, LAC, kalin=True)
    return svg(ic, 'Dikildiğinde 20 cm olan fidanın 4 aylık boy uzama çizgi grafiği.')


def renkli_top_torbasi():
    kartlar = [
        (6, 'Sarı Top', '1 Adet (En Az)', TUR, TUR_A),
        (94, 'Yeşil Top', '3 Adet', YES, YES_A),
        (182, 'Kırmızı Top', '5 Adet', KIR, KIR_A),
        (270, 'Mavi Top', '8 Adet (En Çok)', MAVI, MAVI_A),
    ]
    ic = ''
    for x, ad, sayi, r, z in kartlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 70, sayi, LAC, kalin=True)
    return svg(ic, 'Torbadaki farklı renkli top sayıları ve olasılık karşılaştırması.')


def esit_olasilik_torbasi():
    ic = kutu(6, 6, 172, 103, CAM_A, CAM)
    ic += yazi(92, 26, 'Torbadaki Mevcut Bilyeler', CAM, kalin=True)
    ic += yazi(92, 52, '• Kırmızı: 6 bilye', KIR, kalin=True)
    ic += yazi(92, 74, '• Mavi: 10 bilye (En çok)', MAVI, kalin=True)
    ic += yazi(92, 95, '• Siyah: 4 bilye', LAC, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Hedef: Eşit Olasılıklı!', TUR, kalin=True)
    ic += yazi(269, 54, 'Her renkten 10’ar bilye', LAC, kalin=True)
    ic += yazi(269, 78, 'olması için kaç kırmızı ve', LAC)
    ic += yazi(269, 96, 'kaç siyah eklenmelidir?', KIR, kalin=True)
    return svg(ic, 'Torbadaki bilyelerin eşit olasılıklı duruma getirilmesi modeli.')


def iki_okul_daire_karsilastirma():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'A Okulu Daire Grafiği', MAVI, kalin=True)
    ic += yazi(92, 54, 'Kız Öğrenci: 180° (%50)', LAC, kalin=True)
    ic += yazi(92, 84, 'Toplam Mevcudu: 400 Öğrenci', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic += yazi(269, 26, 'B Okulu Daire Grafiği', MOR, kalin=True)
    ic += yazi(269, 54, 'Kız Öğrenci: 180° (%50)', LAC, kalin=True)
    ic += yazi(269, 84, 'Toplam Mevcudu: 600 Öğrenci', MOR, kalin=True)
    return svg(ic, 'A ve B okullarının daire grafiklerinde oran ve gerçek sayı farkı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = spor_kursu_sutun()
    s[2]['gorsel'] = tahil_ebob_daire()
    s[5]['gorsel'] = coklu_grafik_galeri()
    s[6]['gorsel'] = on_iki_top_kutusu()
    s[7]['gorsel'] = fidan_boyu_cizgi()
    s[8]['gorsel'] = renkli_top_torbasi()
    s[9]['gorsel'] = esit_olasilik_torbasi()
    s[11]['gorsel'] = iki_okul_daire_karsilastirma()
