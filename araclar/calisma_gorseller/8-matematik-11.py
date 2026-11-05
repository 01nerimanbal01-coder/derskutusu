"""8. sınıf Matematik 11. hafta (Veri Analizi: Çizgi, Sütun ve Daire Grafiği) görselleri.
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


def sube_sutun_grafigi():
    ic = kutu(6, 6, 185, 103, MAVI_A, MAVI)
    ic += f'<line x1="28" y1="88" x2="174" y2="88" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<rect x="40" y="48" width="26" height="40" fill="{MAVI}"/>'
    ic += f'<rect x="88" y="36" width="26" height="52" fill="{YES}"/>'
    ic += f'<rect x="136" y="58" width="26" height="30" fill="{TUR}"/>'
    ic += yazi(53, 42, '24', MAVI, kalin=True)
    ic += yazi(101, 30, '30', YES, kalin=True)
    ic += yazi(149, 52, '18', TUR, kalin=True)
    ic += yazi(53, 103, '8-A', LAC)
    ic += yazi(101, 103, '8-B', YES, kalin=True)
    ic += yazi(149, 103, '8-C', LAC)
    ic += kutu(199, 6, 155, 103, YES_A, YES)
    ic += yazi(276, 30, 'Daireye Dönüşüm', YES, kalin=True)
    ic += yazi(276, 56, 'Toplam = 24+30+18 = 72', LAC)
    ic += yazi(276, 82, '72 kişi → 360° (×5°)', MAVI, kalin=True)
    return svg(ic, '8-A (24), 8-B (30) ve 8-C (18) şubelerinin öğrenci sayısı sütun grafiği.')


def kutuphane_dagilimi():
    kartlar = [
        (6, 6, '1. Roman: 60 adet', 'Toplam: 180 kitap', MAVI, MAVI_A),
        (184, 6, '2. Hikâye: 45 adet', 'Merkez açı = ?', YES, YES_A),
        (6, 60, '3. Şiir: 30 adet', 'Oran = ?', TUR, TUR_A),
        (184, 60, '4. Bilim: 45 adet', 'Merkez açı = ?', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Kütüphanedeki 180 kitabın dört türe dağılım kartları.')


def tahil_daire_grafigi():
    ic = kutu(6, 6, 165, 103, TUR_A, TUR)
    ic += f'<circle cx="88" cy="58" r="40" fill="#fde047" stroke="{TUR}" stroke-width="1.5"/>'
    ic += f'<path d="M 88 58 L 88 18 A 40 40 0 0 1 128 58 Z" fill="#86efac" stroke="{YES}" stroke-width="1.3"/>'
    ic += f'<path d="M 88 58 L 128 58 A 40 40 0 0 1 54 78 Z" fill="#93c5fd" stroke="{MAVI}" stroke-width="1.3"/>'
    ic += yazi(106, 46, '90°', YES, kalin=True)
    ic += yazi(96, 80, '120°', MAVI, kalin=True)
    ic += yazi(64, 50, '150°', TUR, kalin=True)
    ic += kutu(179, 6, 175, 103, YES_A, YES)
    ic += yazi(266, 28, 'Tahıl Dağılımı (360°)', YES, kalin=True)
    ic += yazi(266, 52, 'Buğday: 150° · Arpa: 120°', LAC)
    ic += yazi(266, 74, 'Mısır: 90° = 54 ton', KIR, kalin=True)
    ic += yazi(266, 96, 'Buğday (150°) = ? ton', MAVI, kalin=True)
    return svg(ic, 'Buğday 150°, arpa 120° ve mısır 90° olan daire grafiği.')


def tisort_cizgi_grafigi():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Dört Günlük Tişört Satış Adedi (Çizgi Grafiği)', MAVI, kalin=True)
    ic += f'<line x1="44" y1="86" x2="324" y2="86" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<polyline points="70,64 145,52 220,74 295,36" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
    for x, y, v, g in [(70, 64, '35', 'Pzt'), (145, 52, '42', 'Sal'), (220, 74, '28', 'Çar'), (295, 36, '55', 'Per')]:
        ic += f'<circle cx="{x}" cy="{y}" r="3.5" fill="{KIR}"/>'
        ic += yazi(x, y - 7, v, KIR, kalin=True)
        ic += yazi(x, 102, g, LAC)
    return svg(ic, 'Pazartesi 35, Salı 42, Çarşamba 28 ve Perşembe 55 tişört satışını gösteren çizgi grafiği.')


def butce_yuzde_grafigi():
    ogeler = [
        (6, 'Kira', '%35', KIR, KIR_A),
        (94, 'Mutfak', '%25', MAVI, MAVI_A),
        (182, 'Eğitim', '%20', YES, YES_A),
        (270, 'Diğer', '%20', TUR, TUR_A),
    ]
    ic = ''
    for x, ad, yuzde, r, z in ogeler:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 68, yuzde, LAC, kalin=True)
        ic += yazi(x + 42, 94, '× 3,6°', r)
    return svg(ic, 'Aile bütçesi yüzde dağılımı ve daire grafiği açı dönüşümü.')


def soru_sayisi_kartlari():
    gunler = [
        (6, 'Pazartesi', '80 Soru', MAVI, MAVI_A),
        (94, 'Salı', '100 Soru', YES, YES_A),
        (182, 'Çarşamba', '60 Soru', TUR, TUR_A),
        (270, 'Perşembe', '120 Soru', MOR, MOR_A),
    ]
    ic = ''
    for x, g, s, r, z in gunler:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 34, g, r, kalin=True)
        ic += yazi(x + 42, 66, s, LAC, kalin=True)
        ic += yazi(x + 42, 94, 'Toplam: 360', r)
    return svg(ic, 'Dört günde çözülen toplam 360 sorunun günlere dağılımı.')


def uretim_degisim_sema():
    ic = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(91, 26, '1. Durum (Toplam 180)', MAVI, kalin=True)
    ic += yazi(91, 52, 'K: 40 · L: 60 · M: 80', LAC)
    ic += yazi(91, 78, 'M Açısı = (80/180)×360°', MAVI, kalin=True)
    ic += yazi(91, 98, '= 160°', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, '2. Durum (K + 20 Adet)', YES, kalin=True)
    ic += yazi(269, 52, 'K: 60 · L: 60 · M: 80', LAC)
    ic += yazi(269, 78, 'Yeni Toplam = 200 ürün', YES, kalin=True)
    ic += yazi(269, 98, 'M Yeni Açı = (80/200)×360°', KIR, kalin=True)
    return svg(ic, 'K ürünü artışı sonrası M ürününün daire grafiği merkez açısı değişimi.')


def grafik_secimi_karsilastirma():
    ic = kutu(6, 6, 170, 103, CAM_A, CAM)
    ic += yazi(91, 26, 'Araştırma 1: Meteoroloji', CAM, kalin=True)
    ic += yazi(91, 54, 'Ankara’nın 5 günlük', LAC)
    ic += yazi(91, 76, 'sıcaklık değişimi takibi', LAC)
    ic += yazi(91, 98, '→ Zamana bağlı değişim', CAM, kalin=True)
    ic += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic += yazi(269, 26, 'Araştırma 2: Ekonomi', MOR, kalin=True)
    ic += yazi(269, 54, 'Aylık gelirin harcama', LAC)
    ic += yazi(269, 76, 'kalemlerine oransal payı', LAC)
    ic += yazi(269, 98, '→ Parça - Bütün oranı', MOR, kalin=True)
    return svg(ic, 'Meteoroloji sıcaklık takibi ve ekonomi bütçe payı için uygun grafik seçimi.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sube_sutun_grafigi()
    s[2]['gorsel'] = kutuphane_dagilimi()
    s[5]['gorsel'] = tahil_daire_grafigi()
    s[6]['gorsel'] = tisort_cizgi_grafigi()
    s[7]['gorsel'] = butce_yuzde_grafigi()
    s[8]['gorsel'] = soru_sayisi_kartlari()
    s[9]['gorsel'] = uretim_degisim_sema()
    s[11]['gorsel'] = grafik_secimi_karsilastirma()
