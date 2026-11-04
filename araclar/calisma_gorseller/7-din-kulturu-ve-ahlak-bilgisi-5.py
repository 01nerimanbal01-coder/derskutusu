"""7. sınıf Din Kültürü ve Ahlak Bilgisi 5. hafta (Melek İnancının İnsana Kazandırdıkları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def inanc_dusunce_davranis_zinciri():
    """Soru 1: İnanç -> Düşünce -> Davranış 3 halkalı analitik zincir şeması."""
    halkalar = [
        ('1. İnanç', 'Kirâmen Kâtibîn yazar', YES, YES_A, 6),
        ('2. Düşünce', '? (İçsel farkındalık)', MAVI, MAVI_A, 126),
        ('3. Davranış', '? (Ahlaki tutum)', TUR, TUR_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Melek İnancında Akıl Yürütme Zinciri', KAHVE)
    for bas, alt, r, z, x in halkalar:
        ic += kutu(x, 28, 108, 54, z, r, 7, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 68, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'İnanç, düşünce ve davranış arasındaki üç halkalı analitik bağ şeması.', 16)


def melek_gorev_ve_erdem_kartlari():
    """Soru 2: Dört melek inancı yönü ve kazandırdığı erdem kartları."""
    kartlar = [
        ('1. Yazıcı Melekler', 'Amelleri eksiksiz kaydeder', MAVI, MAVI_A),
        ('2. Hafaza Melekleri', 'Allah’ın izniyle korur', YES, YES_A),
        ('3. Dua Eden Melekler', 'Müminler için hayır diler', TUR, TUR_A),
        ('4. İtaatkâr Melekler', 'Kibre kapılmadan kulluk eder', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Melek inancının dört yönünü özetleyen bilgi kartları.', 16)


def infitar_ayet_levhasi():
    """Soru 4: İnfitar suresi 10-12. ayetler levhası."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 22, 'Kur’an-ı Kerim · İnfitâr Suresi 10–12. Ayetler', YESIL_K)
    ic += kutu(14, 30, 332, 52, '#fff', ALTIN, 6, 1.2)
    ic += yazi(180, 50, '«Şüphesiz üzerinizde bekçiler, değerli yazıcılar vardır;', LAC, 'middle', True)
    ic += yazi(180, 70, 'onlar yapmakta olduğunuz her şeyi bilirler.»', YESIL_K)
    return svg(360, 94, ic, 'İnfitâr suresi 10-12. ayetlerin mealini içeren levha.', 16)


def gayb_bilgi_kaynagi_karti():
    """Soru 5: Gayb bilgisi ve doğru kaynak kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Gayb Âlemi ve Doğru Bilgi Kaynağı', MAVI)
    ic += kutu(12, 28, 162, 52, KIR_A, KIR, 6, 1.2)
    ic += yazi(93, 46, 'Mert’in İddiası (!)', KIR)
    ic += yazi(93, 66, '«Her efsaneye inanabiliriz»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, YES_A, YES, 6, 1.2)
    ic += yazi(267, 46, 'İslam’da Ölçü', YESIL_K)
    ic += yazi(267, 66, 'Yalnız Kur’an ve Sahih Sünnet', LAC, 'middle', True)
    return svg(360, 94, ic, 'Gayb bilgisinde hurafeler ile vahiy kaynağının karşılaştırması.', 16)


def kutuphane_tutum_karsilastirma():
    """Soru 7: Kütüphane kitabında iki farklı tutum kartı."""
    ic = kutu(4, 4, 172, 88, KIR_A, KIR, 8, 1.4)
    ic += yazi(90, 22, '1. Öğrenci Tutumu', KIR)
    ic += yazi(90, 46, 'Yırtık sayfayı gizleyip', LAC, 'middle', True)
    ic += yazi(90, 66, '«Kimse görmedi» diyerek', LAC, 'middle', True)
    ic += yazi(90, 82, 'rafa sessizce bırakır.', KIR)

    ic += kutu(184, 4, 172, 88, YES_A, YES, 8, 1.4)
    ic += yazi(270, 22, '2. Öğrenci Tutumu', YESIL_K)
    ic += yazi(270, 46, 'Kimse görmemiş olsa bile', LAC, 'middle', True)
    ic += yazi(270, 66, 'görevliye durumu anlatıp', LAC, 'middle', True)
    ic += yazi(270, 82, 'sayfayı onarmayı üstlenir.', YESIL_K)
    return svg(360, 96, ic, 'Kütüphanede yırtılan kitap karşısında iki farklı öğrenci tutumu.', 16)


def tedbir_ve_yardim_adimlari():
    """Soru 8: 4 adımlı tedbir, gayret ve ilahi yardım akışı."""
    adimlar = [
        ('1. Hazırlık', 'Planlı çalış', MAVI, MAVI_A, 6),
        ('2. Cesaret', 'Yalnız değilsin', YES, YES_A, 94),
        ('3. Dürüstlük', 'Hilesiz emek ver', TUR, TUR_A, 182),
        ('4. Dua & Güven', 'Sonucu Allah’tan bil', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Melek inancında tedbir, cesaret, dürüstlük ve dua basamakları.', 15)


def iki_melek_duasi_karti():
    """Soru 9: İnfak eden ve cimrilik eden için iki meleğin duası hadisi."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Hadis-i Şerif · Her Sabah İnen İki Meleğin Duası', KAHVE)
    ic += kutu(12, 28, 162, 54, YES_A, YES, 6, 1.2)
    ic += yazi(93, 46, '1. Meleğin Duası', YESIL_K)
    ic += yazi(93, 68, '«İnfak edene bereket ver!»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 54, TUR_A, TUR, 6, 1.2)
    ic += yazi(267, 46, '2. Meleğin Uyarısı', TUR)
    ic += yazi(267, 68, 'Cimrilikten sakındırma', LAC, 'middle', True)
    return svg(360, 96, ic, 'Paylaşan ve cimrilik eden hakkında iki meleğin duasını gösteren kart.', 16)


def dis_ve_ic_denetim_karti():
    """Soru 12: Dış denetim ile iç denetim (öz denetim) karşılaştırması."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Denetim Türlerinin Toplumsal Güvene Etkisi', MAVI)
    ic += kutu(12, 28, 162, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(93, 46, 'Dış Denetim (Kamera)', TUR)
    ic += yazi(93, 66, 'Yalnız görülen yerde etkili', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Öz Denetim (Kirâmen Kâtibîn)', YESIL_K)
    ic += yazi(267, 66, 'Her zaman ve her yerde etkili', LAC, 'middle', True)
    return svg(360, 94, ic, 'Kamera denetimi ile yazıcı melek inancına dayalı öz denetim karşılaştırması.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = inanc_dusunce_davranis_zinciri()
    s[1]['gorsel'] = melek_gorev_ve_erdem_kartlari()
    s[3]['gorsel'] = infitar_ayet_levhasi()
    s[4]['gorsel'] = gayb_bilgi_kaynagi_karti()
    s[6]['gorsel'] = kutuphane_tutum_karsilastirma()
    s[7]['gorsel'] = tedbir_ve_yardim_adimlari()
    s[8]['gorsel'] = iki_melek_duasi_karti()
    s[11]['gorsel'] = dis_ve_ic_denetim_karti()
