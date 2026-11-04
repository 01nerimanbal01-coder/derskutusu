"""12. sınıf Matematik 1. hafta (Üstel Fonksiyon) çalışma kâğıdı görselleri.
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


def dort_ustel_kavram_karti():
    kavramlar = [
        ('f(x) = 3ˣ', 'a &gt; 1 · Artan Fonksiyon', YES, YES_A),
        ('g(x) = (½)ˣ', '0 &lt; a &lt; 1 · Azalan Fonksiyon', TUR, TUR_A),
        ('y = 0 Asimptot', 'x eksenine yaklaşır', MAVI, MAVI_A),
        ('(0, 1) Noktası', 'Ortak y ekseni kesişimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kavramlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
        if ' · ' in alt:
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel üstel fonksiyon kavram kartı.', 34)


def iki_uzeri_x_grafik_modeli():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'f(x) = 2ˣ FONKSİYON GRAFİĞİ VE DEĞERLERİ', 10.6, MAVI)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'x = 3  →  f(3) = 8', 10.0, YES)
    ic += yazi(95, 74, 'x = 0  →  f(0) = 1', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'x = -1  →  f(-1) = 1/2', 10.0, TUR)
    ic += yazi(265, 74, 'f(3) - f(-1) = 8 - 0,5 = 7,5', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'f(x) = 2^x fonksiyonunun grafik ve değer modeli.', 34)


def taban_kosullari_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Geçerli Taban Koşulu', 10.4, YES)
    ic += yazi(91, 50, 'a &gt; 0  ve  a ≠ 1', 10.0, LAC)
    ic += yazi(91, 76, 'f: ℝ → ℝ⁺ tanımlıdır', 9.4, YES)

    ic += kutu(184, 6, 170, 98, KIR_A, KIR)
    ic += yazi(269, 26, 'Tanımsız Durumlar', 10.4, KIR)
    ic += yazi(269, 50, 'a ≤ 0  veya  a = 1', 10.0, LAC)
    ic += yazi(269, 76, 'Üstel fonksiyon belirtmez', 9.4, KIR)
    return svg(360, 110, ic, 'Üstel fonksiyon taban koşulları karşılaştırma kartı.', 34)


def birebir_ortenlik_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'BİRE BİRLİK VE ÖRTENLİK ANALİZİ', 10.6, CAM)
    ic += yazi(180, 52, 'Yatay Doğru Testi: Her y &gt; 0 için grafik tek noktada kesilir.', 10.0, LAC)
    ic += yazi(180, 76, 'Bu nedenle f(x) = aˣ fonksiyonu bire bir ve örtendir (tersi logaritmadır).', 9.3, CAM, ince=True)
    return svg(360, 110, ic, 'Üstel fonksiyonlarda bire birlik ve örtenlik analizi.', 34)


def uslu_siralamasi_karti():
    ifadeler = [
        ('2⁻² = 1/4', 'En küçük değer (0,25)', MAVI, MAVI_A),
        ('2⁻¹ = 1/2', 'İkinci basamak (0,50)', YES, YES_A),
        ('2⁰ = 1', 'Kesim değeri (1,00)', TUR, TUR_A),
        ('2² = 4', 'En büyük değer (4,00)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(ifadeler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Üslü kuvvetlerin değer sıralaması kartı.', 34)


def iki_egri_karsilastirma():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'TABANIN GRAFİK EĞRİSİNE ETKİSİ', 10.6, MOR)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'f(x) = aˣ (a &gt; 1)', 10.0, YES)
    ic += yazi(95, 74, 'Soldan sağa ARTAN eğri', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'g(x) = bˣ (0 &lt; b &lt; 1)', 10.0, TUR)
    ic += yazi(265, 74, 'Soldan sağa AZALAN eğri', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Taban değerine göre artan ve azalan üstel fonksiyon grafikleri.', 34)


def dort_kume_ozelligi_karti():
    ozellikler = [
        ('Tanım Kümesi', 'Gerçek Sayılar (ℝ)', MAVI, MAVI_A),
        ('Görüntü Kümesi', 'Pozitif Reel (ℝ⁺)', YES, YES_A),
        ('Bire Birlik', 'Farklı girdiye farklı çıktı', TUR, TUR_A),
        ('Örtenlik', 'Değer kümesi açıkta kalmaz', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(ozellikler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Üstel fonksiyonun küme ve eşleşme özellikleri.', 34)


def sifre_matematik_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'ÜSTEL FONKSİYON KAVRAM PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'TEK · ASİMPTOT · BİREBİR · ARTAN · NOKTA', 9.8, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli matematik terimini (5 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre matematik kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_ustel_kavram_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = iki_uzeri_x_grafik_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = taban_kosullari_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = birebir_ortenlik_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = uslu_siralamasi_karti()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = iki_egri_karsilastirma()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_kume_ozelligi_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_matematik_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
