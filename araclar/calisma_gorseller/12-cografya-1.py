"""12. sınıf Coğrafya 1. hafta (Ekstrem Doğa Olayları ve Etkileri) çalışma kâğıdı görselleri.
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


def dort_ekstrem_olay_karti():
    kartlar = [
        ('1. Tsunami', 'Okyanus Kırığı · Dev Dalga', MAVI, MAVI_A),
        ('2. Kuraklık', 'Yağış Azlığı · Geniş Alan', TUR, TUR_A),
        ('3. Heyelan', 'Eğimli Yamaç · Kütle Kayması', YES, YES_A),
        ('4. Kasırga', 'Sıcak Okyanus · Dönen Rüzgâr', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.3, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört ekstrem doğa olayı bilgi kartları.', 34)


def denizalti_deprem_harita():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'OKYANUS TABANI TEKTONİK KIRILMA MODELİ', 10.8, CAM)
    # Fay çizgisi ve dalga hareketi
    ic += kutu(20, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(95, 54, 'Odak Noktası: 8,2 Büyüklük', 9.8, MAVI)
    ic += yazi(95, 74, 'Fay hattında 4 m düşey atım', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Kıyı Yerleşim Hattı', 9.8, TUR)
    ic += yazi(265, 74, 'Tsunami alarm seviyesi: 1', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Okyanus tabanında meydana gelen 8.2 büyüklüğünde deprem modeli.', 34)


def buyukluk_siddet_karti():
    ic = kutu(6, 6, 170, 98, MAVI_A, MAVI)
    ic += yazi(91, 26, 'Büyüklük (Magnitüd)', 10.4, MAVI)
    ic += yazi(91, 48, 'Açığa çıkan toplam enerji', 9.6, LAC, ince=True)
    ic += yazi(91, 66, 'Sismografla ölçülür (Aletsel)', 9.4, LAC, ince=True)
    ic += yazi(91, 84, 'Merkezden uzaklaşsa da DEĞİŞMEZ', 9.2, MAVI)

    ic += kutu(184, 6, 170, 98, KIR_A, KIR)
    ic += yazi(269, 26, 'Şiddet (Mercalli)', 10.4, KIR)
    ic += yazi(269, 48, 'Yeryüzündeki hasar ve yıkım', 9.6, LAC, ince=True)
    ic += yazi(269, 66, 'Yapı ve insan etkisiyle ölçülür', 9.4, LAC, ince=True)
    ic += yazi(269, 84, 'Uzaklaştıkça genellikle AZALIR', 9.2, KIR)
    return svg(360, 110, ic, 'Deprem büyüklüğü ve deprem şiddeti karşılaştırma kartı.', 34)


def ekstrem_siniflandirma_diyagram():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 24, 'Jeolojik &amp; Jeomorfolojik', 10.2, YES)
    ic += yazi(91, 46, 'Depremler · Tsunamiler', 9.6, LAC, ince=True)
    ic += yazi(91, 64, 'Volkanik Patlamalar', 9.6, LAC, ince=True)
    ic += yazi(91, 82, 'Heyelan &amp; Kaya Düşmesi', 9.6, LAC, ince=True)

    ic += kutu(184, 6, 170, 98, MOR_A, MOR)
    ic += yazi(269, 24, 'Klimatolojik &amp; Hidrolojik', 10.2, MOR)
    ic += yazi(269, 46, 'Aşırı Sıcaklık &amp; Soğukluk', 9.6, LAC, ince=True)
    ic += yazi(269, 64, 'Şiddetli Rüzgârlar (Kasırga)', 9.6, LAC, ince=True)
    ic += yazi(269, 82, 'Aşırı Yağış, Sel &amp; Kuraklık', 9.6, LAC, ince=True)
    return svg(360, 110, ic, 'Ekstrem doğa olayları iki ana grup sınıflandırma şeması.', 34)


def volkan_patlama_akisi():
    adımlar = [
        ('1. Püskürme', 'Gaz &amp; kül çıkışı', KIR, KIR_A),
        ('2. Stratosfer', 'Kül güneşi keser', TUR, TUR_A),
        ('3. Soğuma', 'Küresel sıcaklık düşer', MAVI, MAVI_A),
        ('4. Kıtlık', 'Tarım rekoltesi çöker', YES, YES_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if '&amp;' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Volkanik patlamanın iklim ve tarım üzerindeki aşamalı etkileri.', 34)


def sicaklik_dalgalanma_grafigi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'EKSTREM SICAK HAVA DALGASI GRAFİĞİ', 10.5, TUR)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Mevsim Normalleri: 28 °C', 9.8, YES)
    ic += yazi(95, 74, 'Olağan buharlaşma dengesi', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, KIR_A, KIR)
    ic += yazi(265, 54, 'Ekstrem Değer: 44 °C', 9.8, KIR)
    ic += yazi(265, 74, 'Yüksek orman yangını riski', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Mevsim normalleri ile ekstrem sıcaklık dalgası karşılaştırma grafiği.', 34)


def dort_meteorolojik_afet_karti():
    afetler = [
        ('Sıcak Dalgası', 'Mevsim Üstü Isı', KIR, KIR_A),
        ('Soğuk Dalgası', 'Ani Don Olayı', MAVI, MAVI_A),
        ('Ani Taşkın', 'Dere Yatağı Taşması', CAM, CAM_A),
        ('Kütle Kayması', 'Suya Doygun Zemin', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(afetler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört meteorolojik afet türü kartı.', 34)


def sifre_ipucu_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'JEOLOJİK SÜREÇLER &amp; AFET ARAŞTIRMA KARTI', 10.8, CAM)
    ic += yazi(180, 50, 'LAV · OBRUK · HEYELAN · KRATER · MAGMA · TSUNAMİ', 9.8, LAC)
    ic += yazi(180, 76, 'Anahtar kutuları birleştirerek şifreyi (6 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre ipucu panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_ekstrem_olay_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = denizalti_deprem_harita()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = buyukluk_siddet_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = ekstrem_siniflandirma_diyagram()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = volkan_patlama_akisi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = sicaklik_dalgalanma_grafigi()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_meteorolojik_afet_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_ipucu_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
