"""12. sınıf Coğrafya 2. hafta (Doğa Olaylarının Geleceği ve İklim) çalışma kâğıdı görselleri.
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


def dort_cevre_kavrami_karti():
    kavramlar = [
        ('1. Wilson Döngüsü', '300-500 Milyon Yıl · Süper Kıta', YES, YES_A),
        ('2. Sera Etkisi', 'Yer Işıması · Doğal Isınma', MAVI, MAVI_A),
        ('3. Çölleşme', 'Verim Kaybı · Kurak Alanlar', TUR, TUR_A),
        ('4. Karbon İzi', 'Emisyon Hacmi · Sera Gazı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kavramlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:

            ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)

            ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.0, LAC, ince=True)

        elif ' &amp; ' in alt:

            ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)

            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.0, LAC, ince=True)

        else:

            ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört küresel çevre kavram kartı.', 34)


def super_kita_projeksiyon_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, '250 MİLYON YIL SONRA: PANGEA ULTIMA SENARYOSU', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Manto Konveksiyonu', 10.0, YES)
    ic += yazi(95, 74, 'Yılda birkaç cm levha hareketi', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Süper Kıta İçleri', 10.0, TUR)
    ic += yazi(265, 74, 'Aşırı kurak karasal çöller', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Gelecekteki süper kıta levha tektoniği modeli.', 34)


def sera_gazi_emisyon_grafigi():
    ic = kutu(6, 6, 348, 98, KIR_A, KIR)
    ic += yazi(180, 24, 'KÜRESEL SERA GAZI SALINIM PAYLARI', 10.6, KIR)
    ic += yazi(180, 52, 'Karbondioksit (CO₂): %76  |  Metan (CH₄): %16  |  Diğer: %8', 10.0, LAC)
    ic += yazi(180, 76, 'Fosil yakıt tüketimi küresel ısınmanın ana motorudur.', 9.4, KIR, ince=True)
    return svg(360, 110, ic, 'Sera gazı salınım yüzdeleri grafiği.', 34)


def iklim_degisimi_dinamik_panosu():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Doğal Sera Dengesi', 10.4, YES)
    ic += yazi(91, 50, 'Ortalama Sıcaklık: +15 °C', 9.6, LAC, ince=True)
    ic += yazi(91, 76, 'Canlı yaşamını mümkün kılar', 9.4, YES)

    ic += kutu(184, 6, 170, 98, KIR_A, KIR)
    ic += yazi(269, 26, 'Antropojenik Isınma', 10.4, KIR)
    ic += yazi(269, 50, 'Sanayi sonrası +1,1 °C artış', 9.6, LAC, ince=True)
    ic += yazi(269, 76, 'Kritik risk eşiği: 1,5 °C', 9.4, KIR)
    return svg(360, 110, ic, 'Doğal sera dengesi ve antropojenik ısınma karşılaştırması.', 34)


def iklim_etki_zinciri_siralamasi():
    adımlar = [
        ('1. Emisyon', 'Fosil yakıt &amp; sera gazı', KIR, KIR_A),
        ('2. Isınma', 'Atmosferik ısı tutulması', TUR, TUR_A),
        ('3. Buzul Erimesi', 'Deniz seviyesi artışı', MAVI, MAVI_A),
        ('4. Kuraklık', 'Tarımsal rekolte çöküşü', YES, YES_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Küresel iklim değişikliği zincirleme etkileri.', 34)


def ipcc_risk_esigi_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'IPCC KÜRESEL ISINMA RİSK EŞİKLERİ', 10.6, TUR)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, '+1,5 °C Hedefi', 10.0, YES)
    ic += yazi(95, 74, 'Yönetilebilir risk düzeyi', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, KIR_A, KIR)
    ic += yazi(265, 54, '+2,0 °C Tehlikesi', 10.0, KIR)
    ic += yazi(265, 74, "Mercanların %99 oranı yok olur", 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'IPCC 1.5 derece ve 2.0 derece risk senaryoları panosu.', 34)


def dort_iklim_belgesi_karti():
    belgeler = [
        ('Kyoto Protokolü', 'İlk bağlayıcı anlaşma', MAVI, MAVI_A),
        ('Paris Anlaşması', '1,5 °C küresel hedef', YES, YES_A),
        ('IPCC Paneli', 'Bilimsel iklim raporları', TUR, TUR_A),
        ('Temiz Enerji', 'Güneş, rüzgâr &amp; hidro', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(belgeler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört uluslararası iklim belgesi ve hedef kartı.', 34)


def sifre_cografya_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'KÜRESEL İKLİM DEĞİŞİKLİĞİ VE GELECEK PANOSU', 10.8, CAM)
    ic += yazi(180, 50, 'İKLİMBİLİM · KUTUP · LİTOSFER · İSTASYON · METAN', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli iklim kavramını (5 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre coğrafya kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_cevre_kavrami_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = super_kita_projeksiyon_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = sera_gazi_emisyon_grafigi()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = iklim_degisimi_dinamik_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = iklim_etki_zinciri_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = ipcc_risk_esigi_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_iklim_belgesi_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_cografya_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
