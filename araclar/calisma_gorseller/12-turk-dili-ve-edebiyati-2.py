"""12. sınıf Edebiyat 2. hafta (Dilin Değişimi ve Edebiyatın İlişkileri) çalışma kâğıdı görselleri.
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


def dort_edebi_eser_karti():
    eserler = [
        ('1. Dokuzuncu Hariciye', 'Peyami Safa · Hasta Çocuk Psikolojisi', MAVI, MAVI_A),
        ('2. Yıllarca Aradım', 'Âşık Veysel · Felsefi Arayış', YES, YES_A),
        ('3. Kürk Mantolu', 'Sabahattin Ali · İç Çatışma', TUR, TUR_A),
        ('4. Dil-Millet Bağı', 'T. Gülensoy · Dilin Evrimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(eserler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
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
    return svg(360, 110, ic, 'Dört edebî eser ve tematik odağı kartı.', 34)


def edebi_felsefi_dil_karsilastirma():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'EDEBÎ DİL İLE FELSEFİ DİLİN FARKI', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Edebî Dil (Üst Dil)', 10.0, YES)
    ic += yazi(95, 74, 'İmge, mecaz &amp; estetik çağrışım', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, 'Felsefi Dil', 10.0, TUR)
    ic += yazi(265, 74, 'Kavramsal netlik &amp; doğrudan anlatım', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Edebî dil ve felsefi dil karşılaştırması.', 34)


def ic_konusma_bilinc_akisi_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'DOKUZUNCU HARİCİYE KOĞUŞU VE ANLATIM TEKNİKLERİ', 10.6, MOR)
    ic += yazi(180, 52, 'İç Konuşma &amp; Bilinç Akışı: Karakterin ruhsal dünyasını dışa vurur.', 10.0, LAC)
    ic += yazi(180, 76, 'Peyami Safa hasta bir gencin psikolojik buhranlarını ustalıkla yansıtır.', 9.3, MOR, ince=True)
    return svg(360, 110, ic, 'İç konuşma ve bilinç akışı anlatım teknikleri panosu.', 34)


def dil_degisimi_etken_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'İç Etkenler', 10.4, YES)
    ic += yazi(91, 50, 'Dilin kendi ses yapısı', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Anlam daralması / genişlemesi', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Dış Etkenler', 10.4, TUR)
    ic += yazi(269, 50, 'Göçler, din &amp; coğrafya', 9.5, LAC, ince=True)
    ic += yazi(269, 76, 'Teknoloji &amp; kültürel temas', 9.4, TUR)
    return svg(360, 110, ic, 'Dildeki iç ve dış değişim faktörleri.', 34)


def yazma_sureci_siralamasi():
    asamalar = [
        ('1. Hazırlık', 'Konu &amp; hedef kitle seçimi', MAVI, MAVI_A),
        ('2. Planlama', 'Düşünceleri taslağa dökme', YES, YES_A),
        ('3. Yazma', 'Paragrafları kaleme alma', TUR, TUR_A),
        ('4. Düzeltme', 'Yazım &amp; anlatım kontrolü', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(asamalar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Yazma sürecinin dört temel aşaması.', 34)


def dil_millet_baglantisi_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'DİL-MİLLET BAĞLANTISI (TUNCER GÜLENSOY)', 10.6, TUR)
    ic += yazi(180, 52, '“Dil canlı bir varlıktır; toplumun tarihiyle birlikte nefes alır.”', 10.0, LAC)
    ic += yazi(180, 76, 'Göçler, din değişiklikleri ve teknoloji dildeki kelime hazinesini dönüştürür.', 9.3, TUR, ince=True)
    return svg(360, 110, ic, 'Dil millet bağlantısı ve canlı dil tahlili panosu.', 34)


def dort_anlatim_teknigi_karti():
    teknikler = [
        ('İç Konuşma', 'Düzenli zihin akışı', MAVI, MAVI_A),
        ('Bilinç Akışı', 'Serbest çağrışımlar', YES, YES_A),
        ('İç Çözümleme', 'Anlatıcının analizi', TUR, TUR_A),
        ('Monolog', 'Sesli tekli konuşma', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(teknikler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört edebî anlatım tekniği bilgi kartı.', 34)


def sifre_bilinc_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'EDEBİYAT VE PSİKOLOJİ KAVRAM PANOSU', 10.8, YES)
    ic += yazi(180, 50, 'BİLİM · İÇSEL · LİSAN · İMGE · NOKTA · ÇATIŞMA', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli zihinsel kavramı (6 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre edebiyat kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_edebi_eser_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = edebi_felsefi_dil_karsilastirma()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = ic_konusma_bilinc_akisi_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = dil_degisimi_etken_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = yazma_sureci_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = dil_millet_baglantisi_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_anlatim_teknigi_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_bilinc_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
