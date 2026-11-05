"""11. sınıf Fizik 2. hafta görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def grafik_ozellik_kartlari():
    kartlar = [
        ('1. v-t Eğimi', 'Sabit İvme (g)', MAVI, MAVI_A),
        ('2. v-t Alanı', 'Toplam Yol (h)', YES, YES_A),
        ('3. x-t Eğrisi', 'Parabolik Hızlanma', TUR, TUR_A),
        ('4. a-t Alanı', 'Hız Değişimi (Δv)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Serbest düşme grafik özellikleri kartı.', 34)

def vt_grafik_alan_hesabi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'v-t GRAFİĞİ: 0-3 s TOPLAM YOL VE 4. s YOLU', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'İlk 3 Saniye Toplam Yol', 9.4, MAVI)
    ic += yazi(92, 76, 'h(0-3s) = (3 · 30) / 2', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'h = 45 metre', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Yalnız 4. Saniyede Alınan Yol', 9.4, YESIL_K)
    ic += yazi(267, 76, 'h(4.s) = 7h = 7 · 5 m', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'h = 35 metre', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'v-t grafiği alan ve yol hesabı şeması.', 34)

def h80_metre_dusus_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'h = 80 METRE YÜKSEKTEN SERBEST DÜŞÜŞ MODELİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Formül Bağıntısı', 9.6, YESIL_K)
    ic += yazi(92, 76, 'h = (1/2) · g · t²', 8.8, LAC, ince=True)
    ic += yazi(92, 92, '80 = 5 · t² → t² = 16', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Uçuş Süresi ve Çarpma Hızı', 9.6, TUR)
    ic += yazi(267, 76, 'Düşüş Süresi: t = 4 saniye', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Çarpma Hızı: v = 40 m/s', 8.8, TUR, ince=True)
    return svg(360, 125, ic, '80 metre serbest düşüş modeli şeması.', 34)

def grafik_trio_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'SERBEST DÜŞME HAREKETİNİN ÜÇ TEMEL GRAFİĞİ', 10.3, CAM)
    ic += kutu(20, 38, 95, 68, '#ffffff', CAM)
    ic += yazi(67, 58, 'Konum (x-t)', 9.4, CAM)
    ic += yazi(67, 78, 'Parabolik eğri', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Hızlanan yol', 8.8, CAM, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', MAVI)
    ic += yazi(179, 58, 'Hız (v-t)', 9.4, MAVI)
    ic += yazi(179, 78, 'Doğrusal artış', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Eğim = g sabiti', 8.8, MAVI, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(292, 58, 'İvme (a-t)', 9.4, TUR)
    ic += yazi(292, 78, 'Sabit paralel doğru', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'a = 10 m/s²', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Konum, hız ve ivme grafikleri özeti.', 34)

def saniye_aralik_yol_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 20, 'HER SANİYEDE TEK BAŞINA ALINAN YOLLAR', 10.2, TUR)
    adımlar = [
        ('1. sn (h)', '5 metre', 16),
        ('2. sn (3h)', '15 metre', 102),
        ('3. sn (5h)', '25 metre', 188),
        ('4. sn (7h)', '35 metre', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 56, b, 9.3, TUR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Saniyelerde alınan ardışık yollar şeması.', 34)

def ivme_zaman_alani_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'İVME-ZAMAN GRAFİĞİNDE ALAN = HIZ DEĞİŞİMİ', 10.3, MOR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MOR)
    ic += yazi(92, 56, 'Sabit İvme Değeri', 9.6, MOR)
    ic += yazi(92, 76, 'a = g = 10 m/s²', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Zaman: Δt = 5 saniye', 8.8, MOR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Toplam Hız Artışı (Δv)', 9.6, YESIL_K)
    ic += yazi(267, 76, 'Alan = a · Δt = 10 · 5', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Δv = 50 m/s', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'İvme zaman alanı hız değişimi modeli.', 34)

def sure_mesafe_eslestirme_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'DÜŞÜŞ SÜRESİ VE TOPLAM MESAFE EŞLEŞTİRMESİ', 10.1, YESIL_K)
    kartlar = [
        ('1 saniye', '5 m yol', 16),
        ('2 saniye', '20 m yol', 102),
        ('3 saniye', '45 m yol', 188),
        ('4 saniye', '80 m yol', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Süre ve toplam mesafe kartı.', 34)

def grafik_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['G', 'R', 'A', 'F', 'İ', 'K']
    for i, h in enumerate(harfler):
        x = 42 + i * 46
        ic += kutu(x, 42, 40, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 20, 74, h, 16.0, MAVI)
        ic += yazi(x + 20, 36, f'{i + 1}. Harf', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Grafik kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = grafik_ozellik_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = vt_grafik_alan_hesabi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = h80_metre_dusus_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = grafik_trio_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = saniye_aralik_yol_kesiti()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = ivme_zaman_alani_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = sure_mesafe_eslestirme_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = grafik_sifre_kutulari()
    s[10]['en_fazla'] = 34
