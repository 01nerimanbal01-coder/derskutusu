"""7. sınıf Fen Bilimleri 9. hafta (Enerji Dönüşümleri, Enerjinin Korunumu, Hava ve Su Direnci) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def u_kaykay_pisti_svg():
    ic = kutu(6, 6, 210, 78, MAVI_A, MAVI)
    ic += f'<path d="M 24 22 Q 110 82 196 22" fill="none" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<circle cx="28" cy="24" r="7" fill="{TUR}"/><circle cx="110" cy="52" r="7" fill="{YES}"/><circle cx="192" cy="24" r="7" fill="{KIR}"/>'
    ic += yazi(28, 16, 'P (6 m)', 9.5, TUR)
    ic += yazi(110, 74, 'R (0 m)', 9.5, YES)
    ic += yazi(192, 16, 'S (6 m)', 9.5, KIR)

    ic += kutu(222, 6, 132, 78, YES_A, YES)
    ic += yazi(288, 24, 'Sürtünmesiz Pist', 10.0, YES)
    ic += yazi(288, 45, 'P’de Ep = 180 J', 9.6, LAC, ince=True)
    ic += yazi(288, 66, '3 m’de Ep=?, Ek=?', 9.6, KIR)
    return svg(360, 90, ic, 'Sürtünmesiz U kaykay pistinde P, R ve S noktaları.', 15)


def direnc_tasarim_tablo_kartlari():
    kartlar = [
        ('1. Kuş Sürüsü', 'V dizilimi uçuş', MAVI, MAVI_A),
        ('2. Fren Paraşütü', 'Geniş kubbe açma', TUR, TUR_A),
        ('3. Gemi Pruvası', 'Sivri V burun', CAM, CAM_A),
        ('4. Yüzücü Bonesi', 'Kaygan yüzey', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.3, LAC, ince=True)
    return svg(360, 82, ic, 'Hava ve su direnciyle ilgili dört uygulama kartı.', 14)


def egik_duzlem_yay_duzenegi():
    adimlar = [
        ('1. H Yüksekliği', 'Duran Küre (Ep)', MAVI, MAVI_A),
        ('2. Yatay Yol', 'Hızlı Küre (Ek)', YES, YES_A),
        ('3. Sarmal Yay', 'Maksimum Sıkışma', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 72, z, r)
        ic += yazi(x + 56, 24, bas, 10.2, r)
        ic += yazi(x + 56, 52, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, 'Eğik düzlemden inip sarmal yayı sıkıştıran küre düzeneği.', 14)


def iki_parasut_deneyi():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'X Paraşütü (Dar Kubbe)', 10.2, MAVI)
    ic += yazi(91, 44, 'Yüzey Alanı = 100 cm²', 9.6, LAC, ince=True)
    ic += yazi(91, 65, 'İniş Süresi: 4 saniye', 9.6, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'Y Paraşütü (Geniş Kubbe)', 10.2, TUR)
    ic += yazi(269, 44, 'Yüzey Alanı = 400 cm²', 9.6, LAC, ince=True)
    ic += yazi(269, 65, 'İniş Süresi: 11 saniye', 9.6, KIR)
    return svg(360, 88, ic, 'Farklı kubbe alanına sahip X ve Y paraşütlerinin iniş karşılaştırması.', 15)


def surtunmeli_sarkac_svg():
    ic = kutu(6, 6, 172, 74, YES_A, YES)
    ic += yazi(92, 22, 'Başlangıç (K Noktası)', 10.2, YES)
    ic += yazi(92, 44, 'İlk Yükseklik: h = 30 cm', 9.6, LAC, ince=True)
    ic += yazi(92, 64, 'Serbest bırakıldı', 9.5, YES)

    ic += kutu(184, 6, 170, 74, KIR_A, KIR)
    ic += yazi(269, 22, 'Karşı Uç (N Noktası)', 10.2, KIR)
    ic += yazi(269, 44, 'Son Yükseklik: h = 22 cm', 9.6, LAC, ince=True)
    ic += yazi(269, 64, '8 cm kayıp neden oluştu?', 9.5, KIR)
    return svg(360, 86, ic, 'Sürtünmeli ortamda 30 cm’den bırakılıp 22 cm’ye çıkabilen sarkaç.', 14)


def baraj_vagon_akis_seridi():
    adimlar = [
        ('1. Baraj Gölü', 'Yüksekte Su (Ep)', MAVI, MAVI_A),
        ('2. Akan Su', 'Hızlı Akış (Ek)', CAM, CAM_A),
        ('3. Çark-Vagon', 'Yatay Hareket (Ek)', YES, YES_A),
        ('4. Eğik Rampa', 'Yükselen Vagon (Ep)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += yazi(x + 41, 52, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Baraj suyundan eğik rampadaki vagona enerji dönüşüm şeridi.', 14)


def surtunmeli_enerji_sutun_grafik():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += yazi(91, 22, 'T1 Anı (Başlangıç)', 10.2, MAVI)
    ic += yazi(91, 42, 'Ek = 60 J  ·  Ep = 40 J', 9.5, LAC, ince=True)
    ic += yazi(91, 60, 'Isı Enerjisi (Eısı) = 0 J', 9.5, LAC, ince=True)
    ic += yazi(91, 76, 'Mekanik = 100 J · Toplam = 100 J', 9.3, MAVI)

    ic += kutu(184, 6, 170, 78, TUR_A, TUR)
    ic += yazi(269, 22, 'T2 Anı (Sürtünmeli Yol)', 10.2, TUR)
    ic += yazi(269, 42, 'Ek = 30 J  ·  Ep = 40 J', 9.5, LAC, ince=True)
    ic += yazi(269, 60, 'Isı Enerjisi (Eısı) = 30 J', 9.5, KIR)
    ic += yazi(269, 76, 'Mekanik = 70 J · Toplam = 100 J', 9.3, YES)
    return svg(360, 90, ic, 'Sürtünmeli yolda T1 ve T2 anlarındaki enerji değerleri kartı.', 15)


def hava_sivi_silindir_deneyi():
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI)
    ic += yazi(91, 22, 'K Silindiri · Hava Dolu', 10.2, MAVI)
    ic += yazi(91, 43, 'Tanecik yoğunluğu: Az', 9.5, LAC, ince=True)
    ic += yazi(91, 64, 'Tabana varış süresi: ?', 9.6, MAVI)

    ic += kutu(184, 6, 170, 74, CAM_A, CAM)
    ic += yazi(269, 22, 'L Silindiri · Sıvı Dolu', 10.2, CAM)
    ic += yazi(269, 43, 'Tanecik yoğunluğu: Çok fazla', 9.5, LAC, ince=True)
    ic += yazi(269, 64, 'Tabana varış süresi: ?', 9.6, KIR)
    return svg(360, 86, ic, 'Hava ve yoğun sıvı dolu K ve L silindirlerinde küre düşüşü.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = u_kaykay_pisti_svg()
    s[2]['gorsel'] = direnc_tasarim_tablo_kartlari()
    s[5]['gorsel'] = egik_duzlem_yay_duzenegi()
    s[6]['gorsel'] = iki_parasut_deneyi()
    s[7]['gorsel'] = surtunmeli_sarkac_svg()
    s[8]['gorsel'] = baraj_vagon_akis_seridi()
    s[9]['gorsel'] = surtunmeli_enerji_sutun_grafik()
    s[11]['gorsel'] = hava_sivi_silindir_deneyi()
