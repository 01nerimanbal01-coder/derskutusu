"""12. sınıf Fizik 1. hafta (Düzgün Çembersel Hareket) çalışma kâğıdı görselleri.
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


def dort_fiziksel_buyukluk_karti():
    buyuklukler = [
        ('1. Periyot (T)', '1 Tam Tur Süresi (s)', MAVI, MAVI_A),
        ('2. Frekans (f)', 'Saniyedeki Tur (Hz)', YES, YES_A),
        ('3. Çizgisel Hız', 'Yörüngeye Teğet (v)', TUR, TUR_A),
        ('4. Açısal Hız', 'Birim Zamanda Açı (ω)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(buyuklukler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, '(' + alt.split(' (')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Düzgün çembersel hareket dört temel büyüklük kartı.', 34)


def k_noktasi_vektor_modeli():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ÇEMBERSEL YÖRÜNGEDE VEKTÖRLER (K NOKTASI)', 10.6, MAVI)
    # Şematik çember ve vektör gösterimi
    ic += kutu(20, 36, 150, 58, TUR_A, TUR)
    ic += yazi(95, 54, 'Çizgisel Hız (v): Teğet', 9.8, TUR)
    ic += yazi(95, 74, 'Yönü sürekli değişir', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, 'Merkezcil Kuvvet &amp; İvme', 9.8, YES)
    ic += yazi(265, 74, 'Daima merkeze yöneliktir', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dairesel yörüngede çizgisel hız, ivme ve kuvvet vektör yönleri.', 34)


def periyot_frekans_iliski_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Periyot (T = 4 s)', 10.4, YES)
    ic += yazi(91, 50, 'Bir tam tur süresi = 4 s', 9.6, LAC, ince=True)
    ic += yazi(91, 76, 'Formül: T · f = 1', 9.6, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Frekans (f = ?)', 10.4, TUR)
    ic += yazi(269, 50, 'f = 1 / T = 1 / 4 s⁻¹', 9.6, LAC, ince=True)
    ic += yazi(269, 76, 'Sonuç: f = 0,25 Hertz', 9.6, TUR)
    return svg(360, 110, ic, 'Periyot ve frekans matematiksel bağıntısı.', 34)


def hiz_ivme_diklik_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'HIZ VE İVME VEKTÖRLERİNİN GEOMETRİK İLİŞKİSİ', 10.5, MOR)
    ic += yazi(180, 52, 'v vektörü (Teğet) ⊥ a vektörü (Merkezcil) → Açı: 90°', 10.0, LAC)
    ic += yazi(180, 76, 'Hızın büyüklüğü sabit kalırken yön değişimini merkezcil ivme sağlar.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'Hız ve ivme vektörlerinin diklik ilişkisi şeması.', 34)


def dort_cisim_kuvvet_siralamasi():
    cisimler = [
        ('K: ω, 4r', 'F = 4 m·ω²·r', KIR, KIR_A),
        ('L: 2ω, r', 'F = 4 m·ω²·r', TUR, TUR_A),
        ('M: ω, 2r', 'F = 2 m·ω²·r', MAVI, MAVI_A),
        ('N: ω, r', 'F = 1 m·ω²·r', YES, YES_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(cisimler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' = ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' = ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Farklı yarıçap ve açısal hızlardaki cisimlerin merkezcil kuvvetleri.', 34)


def virajda_arac_dinamik_semasi():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'YATAY VİRAJDA DÖNEN ARACIN DİNAMİK MODELİ', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Sürtünme Kuvveti (Fs)', 10.0, YES)
    ic += yazi(95, 74, 'Tekerlek ile yol arasında', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Merkezcil Görev', 10.0, TUR)
    ic += yazi(265, 74, 'Fs = m·v² / r dengesi', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Yatay virajda dönen araca etki eden sürtünme ve merkezcil kuvvet.', 34)


def dort_formul_karti():
    formuller = [
        ('Çizgisel Hız', 'v = 2πr / T', MAVI, MAVI_A),
        ('Açısal Hız', 'ω = 2π / T', TUR, TUR_A),
        ('Merkezcil İvme', 'a = v² / r', YES, YES_A),
        ('Kuvvet', 'F = m·ω²·r', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(formuller):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' = ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' = ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel çembersel hareket bağıntı kartı.', 34)


def sifre_fizik_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'DÜZGÜN ÇEMBERSEL HAREKET KAVRAM PANOSU', 10.8, MAVI)
    ic += yazi(180, 50, 'KONUM · TUR · VİRAJ · İVME · PERİYOT · TEĞET', 9.8, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli dinamik terimini (6 harf) bulunuz.', 9.4, MAVI, ince=True)
    return svg(360, 110, ic, 'Şifre fizik kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_fiziksel_buyukluk_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = k_noktasi_vektor_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = periyot_frekans_iliski_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = hiz_ivme_diklik_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = dort_cisim_kuvvet_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = virajda_arac_dinamik_semasi()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_formul_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_fizik_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
