"""12. sınıf İnkılap Tarihi 2. hafta (20. Yy Başı Osmanlı Devleti) çalışma kâğıdı görselleri.
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


def dort_fikir_akimi_karti():
    fikirler = [
        ('1. Osmanlıcılık', 'Eşit Haklar · Ortak Vatan', MAVI, MAVI_A),
        ('2. İslamcılık', 'Halifelik Çatısı · Ümmet', YES, YES_A),
        ('3. Türkçülük', 'Millî Dil &amp; Kültür Temeli', TUR, TUR_A),
        ('4. Batıcılık', 'Bilim &amp; Teknik Kurumlar', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(fikirler):
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
    return svg(360, 110, ic, 'Osmanlı Devleti dört fikir akımı kartı.', 34)


def trablusgarp_harita_kroki():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'TRABLUSGARP SAVAŞI HAREKÂT PLANI (1911-1912)', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, 'Derne ve Tobruk', 10.0, YES)
    ic += yazi(95, 74, 'Mustafa Kemal &amp; Enver Bey', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, KIR_A, KIR)
    ic += yazi(265, 54, 'İtalyan Donanması', 10.0, KIR)
    ic += yazi(265, 74, 'Kıyı bombardımanı &amp; 12 Ada', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Trablusgarp Savaşı harita ve cephe krokisi.', 34)


def hareket_ordusu_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, '31 MART VAKASI VE HAREKET ORDUSU (1909)', 10.6, MAVI)
    ic += yazi(180, 52, "Selanik uzerinden gelen Hareket Ordusu isyani bastirdi.", 10.0, LAC)
    ic += yazi(180, 76, 'Komutan: Mahmut Şevket Paşa · Kurmay Başkanı: Kolağası Mustafa Kemal.', 9.3, MAVI, ince=True)
    return svg(360, 110, ic, 'Hareket Ordusu ve 31 Mart Vakası panosu.', 34)


def mesrutiyet_ve_anayasa_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'İkinci Meşrutiyet (1908)', 10.2, YES)
    ic += yazi(91, 50, 'Kanun-i Esasi yürürlükte', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Çok partili ilk parlamento', 9.4, YES)

    ic += kutu(184, 6, 170, 98, TUR_A, TUR)
    ic += yazi(269, 26, 'Uşi Antlaşması (1912)', 10.2, TUR)
    ic += yazi(269, 50, "Trablusgarp Italyaya kaldi", 9.5, LAC, ince=True)
    ic += yazi(269, 50, "Trablusgarp İtalyaya kaldı", 9.5, LAC, ince=True)
    return svg(360, 110, ic, 'İkinci Meşrutiyet ve Uşi Antlaşması kartı.', 34)


def osmanli_siyasi_tarih_siralamasi():
    olaylar = [
        ('1. Meşrutiyet', '1908 İlan süreci', YES, YES_A),
        ('2. 31 Mart Olayı', '1909 İsyan bastırma', MAVI, MAVI_A),
        ('3. Trablusgarp', '1911 İtalyan işgali', TUR, TUR_A),
        ('4. Uşi Antlaşması', '1912 Barış masası', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(olaylar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, '20. yüzyıl başı Osmanlı siyasi olaylar kronolojisi.', 34)


def usi_antlasmasi_sonuc_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'UŞİ ANTLAŞMASI (1912) VE KUZEY AFRİKA', 10.6, TUR)
    ic += yazi(180, 52, "Trablusgarp ve Bingazi İtalyaya; 12 Ada gecici olarak Italyanlara birakildi.", 9.8, LAC)
    ic += yazi(180, 76, "Sonuç: Osmanlı Devleti Kuzey Afrikadaki son egemenlik toprağını kaybetti.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, 'Uşi Antlaşması sonuç panosu.', 34)


def dort_tarih_kavrami_karti():
    terimler = [
        ('Hareket Ordusu', 'İsyan bastıran birlik', MAVI, MAVI_A),
        ('M. Şevket Paşa', 'Ordu başkomutanı', YES, YES_A),
        ('Düyun-ı Umumiye', 'Mali borçlar idaresi', KIR, KIR_A),
        ('Kapitülasyon', 'Yabancı ayrıcalıkları', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(terimler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört Osmanlı siyasi ve iktisadi terimi.', 34)


def sifre_derne_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'TRABLUSGARP VE MEŞRUTİYET KAVRAM PANOSU', 10.8, CAM)
    ic += yazi(180, 50, 'DERNE · EKONOMİ · REJİM · NAMIK · EGEMENLİK', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli Trablusgarp cephesini (5 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre tarih kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_fikir_akimi_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = trablusgarp_harita_kroki()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = hareket_ordusu_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = mesrutiyet_ve_anayasa_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = osmanli_siyasi_tarih_siralamasi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = usi_antlasmasi_sonuc_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_tarih_kavrami_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_derne_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
