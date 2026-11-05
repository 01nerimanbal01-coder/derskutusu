"""12. sınıf Kimya 2. hafta (Elektrokimyasal Hücreler) çalışma kâğıdı görselleri.
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


def dort_hucre_bileseni_karti():
    bilesenler = [
        ('1. Anot Kutbu', 'Yükseltgenme · e⁻ verir', KIR, KIR_A),
        ('2. Katot Kutbu', 'İndirgenme · e⁻ alır', YES, YES_A),
        ('3. Tuz Köprüsü', 'Yük Denkliği · İyon Göçü', MAVI, MAVI_A),
        ('4. Voltmetre', 'Pil Gerilimi Ölçümü', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(bilesenler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:

            if ' · ' in alt:


                ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)


                ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.0, LAC, ince=True)


            elif ' &amp; ' in alt:


                ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)


                ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.0, LAC, ince=True)


            else:


                ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)

        elif ' &amp; ' in alt:

            ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)

            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.0, LAC, ince=True)

        else:

            ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel elektrokimyasal hücre bileşeni.', 34)


def daniell_pili_semasi():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'STANDART DANIELL PİLİ VE İYON GÖÇÜ ŞEMASI', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, KIR_A, KIR)
    ic += yazi(95, 54, 'Anot: Zn → Zn²⁺ + 2e⁻', 9.8, KIR)
    ic += yazi(95, 74, 'Anyonlar anoda göçer (Zn aşınır)', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, 'Katot: Cu²⁺ + 2e⁻ → Cu', 9.8, YES)
    ic += yazi(265, 74, 'Katyonlar katoda göçer (Cu artar)', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Daniell pili yarı hücreleri ve tuz köprüsü akışı.', 34)


def dis_devre_akis_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, 'DIŞ DEVRE ELEKTRON AKIŞ YÖNÜ', 10.6, MAVI)
    ic += yazi(180, 52, 'Elektronlar (e⁻): Anot elektrottan Katot elektrota doğru akar.', 10.0, LAC)
    ic += yazi(180, 76, 'Elektrik Akımı Yönü: Fiziksel kabul gereği Katottan Anoda doğrudur.', 9.3, MAVI, ince=True)
    return svg(360, 110, ic, 'Dış devre elektron akışı şeması.', 34)


def galvanik_elektrolitik_panosu():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Galvanik Hücre (Pil)', 10.2, YES)
    ic += yazi(91, 50, 'Kimyasal → Elektrik', 9.6, LAC, ince=True)
    ic += yazi(91, 76, 'İstemli tepkime (E° &gt; 0)', 9.5, YES)

    ic += kutu(184, 6, 170, 98, MOR_A, MOR)
    ic += yazi(269, 26, 'Elektrolitik Hücre', 10.2, MOR)
    ic += yazi(269, 50, 'Elektrik → Kimyasal', 9.6, LAC, ince=True)
    ic += yazi(269, 76, 'İstemsiz tepkime (E° &lt; 0)', 9.5, MOR)
    return svg(360, 110, ic, 'Galvanik ve elektrolitik hücre karşılaştırması.', 34)


def redoks_denklestirme_siralamasi():
    adımlar = [
        ('1. Yarı Tepkime', 'Anot &amp; katot ayrımı', MAVI, MAVI_A),
        ('2. Atom Denkliği', 'Ana elementleri eşitle', TUR, TUR_A),
        ('3. Yük Denkliği', 'Alınan/verilen e⁻ eşitle', YES, YES_A),
        ('4. Toplam Denklem', 'Net hücre tepkimesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Yarı tepkime denkleştirme adımları.', 34)


def pil_potansiyeli_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'STANDART PİL GERİLİMİ HESAP KARTI', 10.6, TUR)
    ic += yazi(180, 52, 'E°_pil = E°_katot - E°_anot = (+0,34 V) - (-0,76 V)', 10.0, LAC)
    ic += yazi(180, 76, 'Sonuç: E°_pil = +1,10 Volt  →  Tepkime istemlidir.', 9.8, TUR)
    return svg(360, 110, ic, 'Standart pil potansiyeli hesabı kartı.', 34)


def dort_elektrokimya_karti():
    kavramlar = [
        ('Galvanik Hücre', 'Elektrik üreten pil', MAVI, MAVI_A),
        ('Elektroliz', 'Enerji tüketen hücre', YES, YES_A),
        ('SHE Elektrot', 'E° = 0,00 V Referans', TUR, TUR_A),
        ('İstemli Süreç', 'E° &gt; 0 Pil tepkimesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kavramlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel elektrokimya terimi.', 34)


def sifre_katot_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'ELEKTROKİMYASAL HÜCRE KAVRAM PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'KATYON · ANOT · TUZ · OKSİT · TEPKİME', 9.8, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli indirgenme kutbunu (5 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre elektrokimya kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_hucre_bileseni_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = daniell_pili_semasi()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = dis_devre_akis_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = galvanik_elektrolitik_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = redoks_denklestirme_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = pil_potansiyeli_hesap_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_elektrokimya_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_katot_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
