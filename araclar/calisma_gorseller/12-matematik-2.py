"""12. sınıf Matematik 2. hafta (Logaritma Fonksiyonu) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_logaritma_turu_karti():
    turler = [
        ('1. logₐ x = y', 'aʸ = x üstel dönüşümü', YES, YES_A),
        ('2. Bayağı Log', 'log x (10 Tabanı)', MAVI, MAVI_A),
        ('3. Doğal Log', 'ln x (e Tabanı ≈ 2,718)', TUR, TUR_A),
        ('4. (1, 0) Noktası', 'Ortak x ekseni kesişimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(turler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        if ' (' in alt:
            ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel logaritma türü bilgi kartı.', 34)


def log2_grafik_modeli():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'f(x) = log₂ x GRAFİK VE DEĞER ANALİZİ', 10.6, MAVI)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'x = 8  →  log₂ 8 = 3', 10.0, YES)
    ic += yazi(95, 74, 'x = 1  →  log₂ 1 = 0', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'x = 1/4  →  log₂ (1/4) = -2', 9.8, TUR)
    ic += yazi(265, 74, 'f(8) + f(1/4) = 3 + (-2) = 1', 9.6, LAC)
    return svg(360, 110, ic, 'f(x) = log2 x grafik ve değer modeli.', 34)


def tanim_kumesi_kurali_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'LOGARİTMA EN GENİŞ TANIM KÜMESİ KOŞULLARI', 10.6, CAM)
    ic += kutu(16, 38, 98, 56, YES_A, YES)
    ic += yazi(65, 56, 'İç Kısım', 10.0, YES)
    ic += yazi(65, 74, 'h(x) &gt; 0 olmalı', 9.2, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, TUR_A, TUR)
    ic += yazi(180, 56, 'Taban &gt; 0', 10.0, TUR)
    ic += yazi(180, 74, 'g(x) &gt; 0 olmalı', 9.2, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, KIR_A, KIR)
    ic += yazi(295, 56, 'Taban ≠ 1', 10.0, KIR)
    ic += yazi(295, 74, 'g(x) ≠ 1 olmalı', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Logaritma en geniş tanım kümesi 3 kuralı.', 34)


def log_ustel_simetri_karti():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'y = x DOĞRUSUNA GÖRE TERS FONKSİYON SİMETRİSİ', 10.6, MOR)
    ic += yazi(180, 52, 'f(x) = aˣ (Üstel)  ← Simetri: y = x →  f⁻¹(x) = logₐ x (Logaritma)', 10.0, LAC)
    ic += yazi(180, 76, "Üstel eğri (0, 1) noktasından geçerken logaritma (1, 0) noktasından geçer.", 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Üstel ve logaritma fonksiyonlarının y=x simetrisi.', 34)


def log_deger_siralamasi():
    degerler = [
        ('log₂ (1/8)', 'Değer: -3 (En küçük)', MAVI, MAVI_A),
        ('log₂ (1/2)', 'Değer: -1 (Negatif)', YES, YES_A),
        ('log₂ 1', 'Değer: 0 (Kesişim)', TUR, TUR_A),
        ('log₂ 4', 'Değer: 2 (En büyük)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(degerler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        if ' (' in alt:
            ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Logaritmik değerlerin büyüklük sıralaması.', 34)


def taban_degisimi_grafik_karti():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'TABAN BÜYÜKLÜĞÜNE GÖRE LOGARİTMA EĞRİSİ', 10.6, TUR)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'a &gt; 1 (Örnek: log₂ x)', 10.0, YES)
    ic += yazi(95, 74, 'Soldan sağa ARTAN grafik', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, KIR_A, KIR)
    ic += yazi(265, 54, '0 &lt; a &lt; 1 (Örnek: log_½ x)', 9.8, KIR)
    ic += yazi(265, 74, 'Soldan sağa AZALAN grafik', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Taban değerine göre artan ve azalan logaritma grafikleri.', 34)


def dort_log_ozellik_karti():
    ozellikler = [
        ('Bayağı Log', 'log 100 = 2', MAVI, MAVI_A),
        ('Doğal Log', 'ln e⁴ = 4', YES, YES_A),
        ('Düşey Asimptot', 'x = 0 (y ekseni)', TUR, TUR_A),
        ('Uygulama Alanı', 'pH, Desibel, Richter', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(ozellikler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel logaritma özelliği ve uygulama alanı.', 34)


def sifre_dogal_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'LOGARİTMA VE FONKSİYON KAVRAM PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'DÜŞEY · ONLUK · EĞRİ · ASİMPTOT · LOGARİTMA', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli matematiksel kavramı (5 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre matematik kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_logaritma_turu_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = log2_grafik_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = tanim_kumesi_kurali_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = log_ustel_simetri_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = log_deger_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = taban_degisimi_grafik_karti()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_log_ozellik_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_dogal_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
