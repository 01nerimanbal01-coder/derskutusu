"""6. sınıf Fen Bilimleri 9. hafta (Tohumun Çimlenmesine Etki Eden Faktörlere İlişkin Hipotez Oluşturma ve Hayvanlarda Üreme, Büyüme ve Gelişme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def sicaklik_hipotez_deneyi():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'P Düzeneği (Oda Sıcaklığı)', 10.2, YESIL_K)
    ic += yazi(91, 44, 'Nemli pamuk · Hava var', 9.7, LAC, ince=True)
    ic += yazi(91, 65, 'Sıcaklık: 25 °C → Çimlendi', 9.9, YESIL_K)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'R Düzeneği (Soğuk Ortam)', 10.2, MAVI)
    ic += yazi(269, 44, 'Nemli pamuk · Hava var', 9.7, LAC, ince=True)
    ic += yazi(269, 65, 'Sıcaklık: 2 °C → Çimlenmedi', 9.9, MAVI)
    return svg(360, 88, ic, '25 derece ve 2 derecede kurulan P ve R kontrollü çimlenme düzenekleri.', 15)


def dort_omurgali_karti():
    canlilar = [
        ('1. Alabalık', 'Su · Solungaç', MAVI, MAVI_A),
        ('2. Kırlangıç', 'Tüylü · Kanatlı', TUR, TUR_A),
        ('3. Yunus', 'Suda yaşayan memeli', YES, YES_A),
        ('4. Kertenkele', 'Karasal · Pullu deri', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, ozellik, r, z) in enumerate(canlilar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, ozellik, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Alabalık, kırlangıç, yunus ve kertenkele omurgalı canlı kartları.', 15)


def dort_mercimek_kabi():
    kaplar = [
        ('I. Kap (Karanlık)', 'Nemli · 24 °C · Hava var', YES, YES_A),
        ('II. Kap (Aydınlık)', 'Nemli · 24 °C · Hava var', MAVI, MAVI_A),
        ('III. Kap (Aydınlık)', 'Kuru pamuk · 24 °C', TUR, TUR_A),
        ('IV. Kap (Karanlık)', 'Nemli · 0 °C (Buzluk)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, kosul, r, z) in enumerate(kaplar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, kosul, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Farklı koşullardaki dört mercimek tohumu kabı.', 16)


def baskalasim_karsilastirma_semasi():
    ic = kutu(6, 6, 348, 38, YES_A, YES)
    ic += yazi(180, 19, 'Kurbağada Başkalaşım Evreleri:', 10.1, YESIL_K)
    ic += yazi(180, 35, 'Yumurta → [ X = ? ] → Genç Kurbağa → Ergin Kurbağa', 9.6, LAC)

    ic += kutu(6, 50, 348, 38, MOR_A, MOR)
    ic += yazi(180, 63, 'Kelebekte Başkalaşım Evreleri:', 10.1, MOR)
    ic += yazi(180, 79, 'Yumurta → Tırtıl (Larva) → [ Y = ? ] → Ergin Kelebek', 9.6, LAC)
    return svg(360, 94, ic, 'Kurbağa (X) ve kelebek (Y) başkalaşım döngüsü karşılaştırma şeması.', 16)


def oksijen_zeytinyagi_deneyi():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'A Kabı (Ağzı Açık)', 10.2, YESIL_K)
    ic += yazi(91, 44, 'Nemli pamuk · 25 °C', 9.7, LAC, ince=True)
    ic += yazi(91, 65, 'Oksijen girer → Çimlendi', 9.8, YESIL_K)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'B Kabı (Üstü Zeytinyağlı)', 10.2, KIR)
    ic += yazi(269, 44, 'Kaynatılmış-soğutulmuş su · 25 °C', 9.4, LAC, ince=True)
    ic += yazi(269, 65, 'Sonuç: Çimlenme olmadı!', 9.8, KIR)
    return svg(360, 88, ic, 'Oksijenin çimlenmeye etkisini gösteren zeytinyağı tabakalı deney.', 15)


def ipek_bocegi_dongusu():
    evreler = [
        ('Evre A', 'Yumurta (Yaprakta)', MAVI, MAVI_A),
        ('Evre B', 'Tırtıl (Larva)', YES, YES_A),
        ('Evre C', 'İpek Koza (Pupa)', TUR, TUR_A),
        ('Evre D', 'Ergin Kelebek', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(evreler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.3, r)
        ic += yazi(x + 41, 54, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'İpek böceğinin dört gelişim evresi.', 15)


def sazan_guvercin_venn():
    ic = kutu(6, 6, 112, 76, MAVI_A, MAVI)
    ic += yazi(62, 24, 'K Bölgesi', 10.3, MAVI)
    ic += yazi(62, 46, 'Yalnız Sazan', 9.7, LAC)
    ic += yazi(62, 65, '(Balık özelliği)', 9.3, LAC, ince=True)

    ic += kutu(124, 6, 112, 76, YES_A, YES)
    ic += yazi(180, 24, 'L Bölgesi', 10.3, YESIL_K)
    ic += yazi(180, 46, 'Ortak Özellik', 9.7, LAC)
    ic += yazi(180, 65, '(Sazan ve Güvercin)', 9.3, LAC, ince=True)

    ic += kutu(242, 6, 112, 76, TUR_A, TUR)
    ic += yazi(298, 24, 'M Bölgesi', 10.3, TUR)
    ic += yazi(298, 46, 'Yalnız Güvercin', 9.7, LAC)
    ic += yazi(298, 65, '(Kuş özelliği)', 9.3, LAC, ince=True)
    return svg(360, 88, ic, 'Sazan balığı ve güvercin karşılaştırma şeması.', 15)


def toprak_etkisi_tasarim_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'DENEY TASARIM KARTI · ARAŞTIRMA SORUSU', 10.3, CAM)
    ic += yazi(180, 44, '“Tohumun çimlenmesi için toprak zorunlu mudur?”', 10.0, LAC)
    ic += yazi(180, 66, 'Sabit tutulanlar = ?   |   Bağımsız değişken (Farklı) = ?', 9.6, CAM, ince=True)
    return svg(360, 88, ic, 'Toprağın çimlenmeye etkisini araştıran deney tasarım kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sicaklik_hipotez_deneyi()
    s[2]['gorsel'] = dort_omurgali_karti()
    s[5]['gorsel'] = dort_mercimek_kabi()
    s[6]['gorsel'] = baskalasim_karsilastirma_semasi()
    s[7]['gorsel'] = oksijen_zeytinyagi_deneyi()
    s[8]['gorsel'] = ipek_bocegi_dongusu()
    s[9]['gorsel'] = sazan_guvercin_venn()
    s[11]['gorsel'] = toprak_etkisi_tasarim_karti()
