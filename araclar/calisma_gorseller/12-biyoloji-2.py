"""12. sınıf Biyoloji 2. hafta (Nükleik Asitler ve DNA Modeli) çalışma kâğıdı görselleri.
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


def dort_nukleotit_bilesen_karti():
    kartlar = [
        ('1. Azotlu Baz', 'Pürin &amp; Pirimidin', MAVI, MAVI_A),
        ('2. Pentoz', 'Deoksiriboz &amp; Riboz', YES, YES_A),
        ('3. Fosfat Grubu', 'İnorganik Fosfor (H₃PO₄)', TUR, TUR_A),
        ('4. Bağlar', 'Glikozit &amp; Ester bağı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört nükleotit bileşeni bilgi kartı.', 34)


def dna_cift_sarmal_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'WATSON-CRICK DNA ÇİFT SARMAL MODELİ', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'A = T (2 Hidrojen Bağı)', 10.0, YES)
    ic += yazi(95, 74, 'İkili zayıf bağ ile eşleşme', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(265, 54, 'G ≡ C (3 Hidrojen Bağı)', 10.0, MAVI)
    ic += yazi(265, 74, 'Üçlü zayıf bağ ile eşleşme', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'DNA çift sarmal baz eşleşme modeli.', 34)


def nukleotit_bag_yapisi_karti():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'BİR NÜKLEOTİTİN İÇ KİMYASAL BAĞLARI', 10.6, MAVI)
    ic += kutu(16, 38, 98, 56, TUR_A, TUR)
    ic += yazi(65, 56, 'Azotlu Baz', 10.0, TUR)
    ic += yazi(65, 74, 'A, T, G, C, U', 9.2, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, YES_A, YES)
    ic += yazi(180, 56, 'Glikozit Bağı', 10.0, YES)
    ic += yazi(180, 74, 'Baz - Şeker arası', 9.2, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, MOR_A, MOR)
    ic += yazi(295, 56, 'Ester Bağı', 10.0, MOR)
    ic += yazi(295, 74, 'Şeker - Fosfat arası', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Nükleotit içi glikozit ve ester bağları şeması.', 34)


def dna_rna_karsilastirma_panosu():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'DNA Özellikleri', 10.4, YES)
    ic += yazi(91, 48, 'Deoksiriboz · Timin', 9.5, LAC, ince=True)
    ic += yazi(91, 66, 'Çift zincirli sarmal', 9.5, LAC, ince=True)
    ic += yazi(91, 84, 'Kendini eşler (Replikasyon)', 9.4, YES)

    ic += kutu(184, 6, 170, 98, MOR_A, MOR)
    ic += yazi(269, 26, 'RNA Özellikleri', 10.4, MOR)
    ic += yazi(269, 48, 'Riboz · Urasil', 9.5, LAC, ince=True)
    ic += yazi(269, 66, 'Tek polinükleotit zincir', 9.5, LAC, ince=True)
    ic += yazi(269, 84, 'DNA üzerinden sentezlenir', 9.4, MOR)
    return svg(360, 110, ic, 'DNA ve RNA molekülleri karşılaştırma panosu.', 34)


def genetik_organizasyon_siralamasi():
    basamaklar = [
        ('1. Nükleotit', 'En küçük yapı birimi', MAVI, MAVI_A),
        ('2. Gen Bölgesi', 'Protein şifresi taşıyan', YES, YES_A),
        ('3. DNA Sarmalı', 'Tüm genleri içeren', TUR, TUR_A),
        ('4. Kromozom', 'Histonla paketli yapı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(basamaklar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Genetik materyalin parça bütün organizasyonu.', 34)


def dna_oranti_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, '1000 NÜKLEOTİTLİK DNA DENEY HESAP KARTI', 10.6, TUR)
    ic += yazi(180, 52, 'C = 300  →  G = 300  |  C + G = 600 Nükleotit', 10.0, LAC)
    ic += yazi(180, 76, 'Kalan: 1000 - 600 = 400 (A + T)  →  Adenin = 200, Timin = 200', 9.5, TUR)
    return svg(360, 110, ic, 'DNA nükleotit hesaplama kartı.', 34)


def dort_baz_grubu_karti():
    gruplar = [
        ('Pürin Bazları', 'A &amp; G (Çift halkalı)', MAVI, MAVI_A),
        ('Pirimidinler', 'T, C, U (Tek halkalı)', YES, YES_A),
        ('Nükleozit', 'Baz + Pentoz şekeri', TUR, TUR_A),
        ('Heliks Sarmalı', 'Sağa dönümlü burgu', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(gruplar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' (')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört azotlu baz ve yapı grubu kartı.', 34)


def sifre_biyoloji_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'MOLEKÜLER BİYOLOJİ VE GENETİK KAVRAM PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'HİDROJEN · ENZİM · LİGAZ · İPLİK · KROMATİN · SARMAL', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli genetik kavramı (6 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre biyoloji kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_nukleotit_bilesen_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = dna_cift_sarmal_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = nukleotit_bag_yapisi_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = dna_rna_karsilastirma_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = genetik_organizasyon_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = dna_oranti_hesap_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_baz_grubu_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_biyoloji_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
