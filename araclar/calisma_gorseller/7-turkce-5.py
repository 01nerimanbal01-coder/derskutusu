"""7. sınıf Türkçe 5. hafta (Sen Sor O Yanıtlasın — Sporda ve Yaşamda Hedefe Odaklan, Mülakat ve Anlam İlişkileri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def mulakat_roportaj_karsilastirma():
    """Soru 1: Mülakat ve röportaj tür karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, 'Mülakat (Görüşme)', MAVI)
    ic += yazi(90, 44, '• Uzman konukla soru-cevap', LAC, 'middle', True)
    ic += yazi(90, 63, '• Yorum katmadan aktarım', LAC, 'middle', True)
    ic += yazi(90, 81, '• Nesnel ve doğrudan bilgi', MAVI)

    ic += kutu(184, 4, 172, 88, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, 'Röportaj', TUR)
    ic += yazi(270, 44, '• Soru-cevap + Araştırma', LAC, 'middle', True)
    ic += yazi(270, 63, '• Yazarın gözlem ve izlenimi', LAC, 'middle', True)
    ic += yazi(270, 81, '• Mekân betimlemesi ve fotoğraf', TUR)
    return svg(360, 96, ic, 'Mülakat ile röportaj türlerinin özelliklerini karşılaştıran kartlar.', 12)


def anlam_iliskileri_kartlari():
    """Soru 2: Amaç-sonuç, sebep-sonuç ve koşul-sonuç kartları."""
    kartlar = [
        ('1. Kart · Hedef', '«...finale yükselmek için...»', MAVI, MAVI_A),
        ('2. Kart · Gerekçe', '«...doğru yaptığı için vurdu.»', YES, YES_A),
        ('3. Kart · Şart', '«...uzaklaştırırsan odaklanırsın.»', TUR, TUR_A),
        ('4. Kart · Hedef', '«...artırmak üzere görüştü.»', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Amaç, sebep ve koşul ilişkisi içeren dört cümle kartı.', 12)


def ortulu_anlam_haber_panosu():
    """Soru 4: Örtülü anlam içeren ve içermeyen 4 spor haberi."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Spor Bülteni · Örtülü Anlam İnceleme Panosu', KAHVE)
    haberler = [
        ('1. Haber', '«...bu sezon DA kupayı kaldırdı.»', MAVI, MAVI_A, 10, 28),
        ('2. Haber', '«...ARTIK odaklanma egzersizi yapıyor.»', TUR, TUR_A, 184, 28),
        ('3. Haber', '«...çizelgeyi sabahleyin panoya astı.»', YES, YES_A, 10, 58),
        ('4. Haber', '«...YALNIZCA Kaan tam puan aldı.»', MOR, MOR_A, 184, 58),
    ]
    for bas, alt, r, z, x, y in haberler:
        ic += kutu(x, y, 166, 26, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 17, f'{bas}: {alt}', LAC, 'middle', True)
    return svg(360, 96, ic, 'Dört spor haberinde örtülü anlam ipuçlarını gösteren pano.', 12)


def acik_ve_kapali_uclu_soru_karti():
    """Soru 5: Kapalı uçlu ve açık uçlu mülakat sorusu karşılaştırması."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Mülakat Sorusu Hazırlık Kartı · Konuk: Milli Okçu', MAVI)
    ic += kutu(12, 28, 162, 52, KIR_A, KIR, 6, 1.2)
    ic += yazi(93, 46, '1. Soru (Kapalı Uçlu)', KIR)
    ic += yazi(93, 66, '«Okçuluk sporunu seviyor musunuz?»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, YES_A, YES, 6, 1.2)
    ic += yazi(267, 46, '2. Soru (Açık Uçlu)', YESIL_K)
    ic += yazi(267, 66, '«Atış anında nasıl odaklanıyorsunuz?»', LAC, 'middle', True)
    return svg(360, 94, ic, 'Kapalı uçlu ve açık uçlu mülakat sorularının karşılaştırması.', 12)


def soylesi_ana_dusunce_karti():
    """Soru 7: Sen Sor O Yanıtlasın söyleşi parçası."""
    ic = kutu(4, 4, 352, 88, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, '«Sen Sor O Yanıtlasın» · Milli Sporcunun Yanıtı', KIR)
    ic += kutu(14, 28, 332, 54, '#fff', KIR, 6, 1.2)
    ic += yazi(180, 47, '«Yetenek tek başına yetmez; gerçek başarı net bir hedefe', LAC, 'middle', True)
    ic += yazi(180, 67, 'kilitlenmek, disiplinle çalışmak ve pes etmemekle gelir.»', KIR)
    return svg(360, 96, ic, 'Milli sporcunun başarıda odaklanma ve disiplin vurgusu yaptığı söyleşi kartı.', 12)


def mulakat_sureci_adimlari():
    """Soru 8: 4 aşamalı mülakat uygulama kılavuzu."""
    adimlar = [
        ('1. Hazırlık', 'Araştır & soru yaz', MAVI, MAVI_A, 6),
        ('2. Randevu', 'Zamanında buluş', TUR, TUR_A, 94),
        ('3. Görüşme', 'Dinle & kaydet', MOR, MOR_A, 182),
        ('4. Yayım', 'Yorumsuz aktar', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Mülakat öncesinden yayımına kadar dört aşamalı süreç şeması.', 12)


def soz_varligi_anlam_kartlari():
    """Soru 9: Deyim, gerçek ve terim anlam kartları."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Metindeki Söz Varlığı · Deyim, Gerçek ve Terim Anlam', YESIL_K)
    satirlar = [
        ('1. Cümle: «Madalya için aylarca ter döktü.» (Deyim / Mecaz)', MAVI, 28),
        ('2. Cümle: «Yayını gerip 70 metredeki hedef tahtasına baktı.» (Gerçek)', TUR, 56),
    ]
    for metin, r, y in satirlar:
        ic += kutu(14, y, 332, 24, '#fff', r, 5, 1.2)
        ic += yazi(180, y + 16, metin, LAC, 'middle', True)
    return svg(360, 96, ic, 'Ter dökmek deyimi ile hedef tahtası kullanımını gösteren cümle kartı.', 12)


def somut_hedef_karsilastirma():
    """Soru 12: Belirsiz dilek ile somut ve ölçülebilir hedef karşılaştırması."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Hedefe Odaklanmada Somut Planlama İlkeleri', MOR)
    ic += kutu(12, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(93, 46, 'Belirsiz Dilek (✗)', KIR)
    ic += yazi(93, 66, '«Başarılı olmak istiyorum.»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Somut ve Ölçülebilir Hedef (✓)', YESIL_K)
    ic += yazi(267, 66, '«Her gün 40 dk düzenli çalışma»', LAC, 'middle', True)
    return svg(360, 94, ic, 'Belirsiz dilek ile somut ve ölçülebilir hedef arasındaki fark kartı.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = mulakat_roportaj_karsilastirma()
    s[1]['gorsel'] = anlam_iliskileri_kartlari()
    s[3]['gorsel'] = ortulu_anlam_haber_panosu()
    s[4]['gorsel'] = acik_ve_kapali_uclu_soru_karti()
    s[6]['gorsel'] = soylesi_ana_dusunce_karti()
    s[7]['gorsel'] = mulakat_sureci_adimlari()
    s[8]['gorsel'] = soz_varligi_anlam_kartlari()
    s[11]['gorsel'] = somut_hedef_karsilastirma()
