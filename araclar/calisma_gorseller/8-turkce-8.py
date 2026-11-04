"""8. sınıf Türkçe 8. hafta (Atatürk ve Eğitim, Anlam İlişkileri, Cümlenin Ögeleri, Vurgu ve Ara Söz) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); yalnız '·' veya '-' ayırıcı (K155/K172)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ara_soz_cdu_sema():
    """Soru 1: Ara söz ve Cümle Dışı Unsur (CDU) karşılaştırma şeması."""
    ic = kutu(4, 4, 172, 90, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, 'Ara Söz (Açıklayıcı)', MAVI)
    ic += yazi(90, 44, 'İki virgül veya çizgi arası', LAC, 'middle', True)
    ic += yazi(90, 62, 'Açıkladığı ögeye dahildir', LAC, 'middle', True)
    ic += yazi(90, 80, 'Örn: Ankara’yı, başkenti,', MAVI)

    ic += kutu(184, 4, 172, 90, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, 'Cümle Dışı Unsur (CDU)', TUR)
    ic += yazi(270, 44, 'Hitap, bağlaç ve ünlemler', LAC, 'middle', True)
    ic += yazi(270, 62, 'Hiçbir ögeye dahil olmaz', LAC, 'middle', True)
    ic += yazi(270, 80, 'Örn: Öğretmenler! · ki', TUR)
    return svg(360, 98, ic, 'Ara söz ve Cümle Dışı Unsur karşılaştırma şeması.')


def harf_inkilabi_cozumleme():
    """Soru 3: Başöğretmen Atatürk cümlesinin 5 parçalı öge çözümleme panosu."""
    ic = kutu(4, 4, 352, 90, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Cümle Çözümleme Panosu (YÖN Kuralı)', KAHVE)
    parcalar = [
        ('Atatürk', 'Kim?', MAVI, MAVI_A, 8, 62),
        ('sonbaharda', 'Ne zaman?', TUR, TUR_A, 74, 72),
        ('harfleri', 'Neyi?', YES, YES_A, 150, 66),
        ('milletimize', 'Kime?', MOR, MOR_A, 220, 72),
        ('tanıttı.', 'Yüklem', KIR, KIR_A, 296, 56),
    ]
    for s1, soru, r, z, x, w in parcalar:
        ic += kutu(x, 28, w, 56, z, r, 6, 1.2)
        ic += yazi(x + w / 2, 48, s1, LAC)
        ic += yazi(x + w / 2, 72, soru, r, 'middle', True)
    return svg(360, 98, ic, 'Başöğretmen Atatürk cümlesinin 5 bölümlü öge çözümleme panosu.')


def vurgu_dort_kart():
    """Soru 5: Yüklemden önceki vurgulu ögeleri gösteren 4 kart (3. kart okulda -> Yer T.)."""
    kartlar = [
        ('1. Kart', '… raflara özenle dizdi.', '(Nasıl? -> Zarf T.)', YES, YES_A),
        ('2. Kart', '… sabahleyin ulaştı.', '(Ne zaman? -> Zarf T.)', MAVI, MAVI_A),
        ('3. Kart', '… dün okulda tanıttı.', '(Nerede? -> Yer T.)', KIR, KIR_A),
        ('4. Kart', '… kararlılıkla yürüyor.', '(Nasıl? -> Zarf T.)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, bas, r)
        ic += yazi(x + 86, y + 36, s1, LAC, 'middle', True)
    return svg(360, 100, ic, 'Fiil cümlelerinde yüklemden önceki vurgulu sözcükleri gösteren 4 kart.')


def maarif_kongresi_karti():
    """Soru 6: Temmuz 1921 Maarif Kongresi ve Atatürk'ün eğitim vizyonu kartı."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Temmuz 1921 · Ankara Maarif Kongresi Kartı', MAVI)
    ic += kutu(14, 28, 332, 56, '#fff', MAVI, 6, 1.2)
    ic += yazi(180, 48, '“Cehaletle savaş, düşmanla savaştan', LAC, 'middle', True)
    ic += yazi(180, 68, 'daha az önemli değildir.” · M. Kemal Atatürk', MAVI)
    return svg(360, 96, ic, 'Temmuz 1921 Ankara Maarif Kongresi ve Atatürkün eğitim sözü kartı.')


def anlam_iliskileri_sema():
    """Soru 7: Amaç-sonuç, Neden-sonuç, Koşul-sonuç ve Karşılaştırma şeması."""
    kartlar = [
        ('I. Millet Mektepleri', 'artırmak üzere (Hedef)', YES, YES_A),
        ('II. Kar Yağışı', 'başladığı için (Gerekçe)', MAVI, MAVI_A),
        ('III. Bilim Rehberi', 'edinirse (Şart)', TUR, TUR_A),
        ('IV. Tarih Kitapları', 'daha çok (Kıyaslama)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, bas, r)
        ic += yazi(x + 86, y + 36, alt, LAC, 'middle', True)
    return svg(360, 100, ic, 'Dört cümledeki anlam ilişkisi ipuçları kartı.')


def yon_kurali_akis():
    """Soru 8: YÖN kuralı 4 adımlı öge bulma sırası."""
    adlar = [
        ('1. Adım', 'Yüklem bul', KIR, KIR_A),
        ('2. Adım', 'Özne bul', MAVI, MAVI_A),
        ('3. Adım', 'Nesne bul', YES, YES_A),
        ('4. Adım', 'Tamlayıcılar', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 86, '#fff', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Cümlenin Ögelerini Bulmada YÖN Kuralı Sırası', LAC)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 52, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Yüklem, Özne, Nesne ve Tamlayıcılar 4 adımlı YÖN kuralı şeması.')


def ara_soz_gorev_tablosu():
    """Soru 9: Dört cümlede iki virgül arasındaki ara sözler."""
    ic = kutu(4, 4, 352, 102, '#fff', MAVI, 9, 1.4)
    ic += yazi(180, 20, 'İki Virgül Arasındaki Ara Söz ve Ara Cümleler', MAVI)
    satirlar = [
        ('1. … büyüdüğüm şehri, Sivas’ı, ziyaret ederim.', MAVI_A, MAVI),
        ('2. … okula, Cumhuriyet İlkokuluna, kütüphane kurduk.', YES_A, YES),
        ('3. … öğretmenimiz, Ayşe Hanım, sevgi kazandırdı.', TUR_A, TUR),
        ('4. … yarışmada da, eminim, kürsüye çıkacaktır.', MOR_A, MOR),
    ]
    for i, (met, z, r) in enumerate(satirlar):
        y = 26 + i * 19
        ic += kutu(12, y, 336, 16, z, r, 4, 1.1)
        ic += yazi(180, y + 12, met, LAC, 'middle', True)
    return svg(360, 110, ic, 'Dört cümlede kullanılan ara söz ve ara cümle örnekleri.')


def disari_yon_karsilastirma():
    """Soru 12: 'dışarı çıktı' (Zarf T.) ve 'dışarıya çıktı' (Yer T.) karşılaştırma panosu."""
    ic = kutu(4, 4, 172, 90, YES_A, YES, 8, 1.4)
    ic += yazi(90, 22, '1. Cümle (Yalın Hâl)', YESIL_K)
    ic += yazi(90, 44, '“Öğrenciler teneffüste', LAC, 'middle', True)
    ic += yazi(90, 62, 'dışarı çıktı.”', YESIL_K)
    ic += yazi(90, 80, '(Hâl eki almamış)', LAC, 'middle', True)

    ic += kutu(184, 4, 172, 90, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(270, 22, '2. Cümle (-ya Ekli)', MAVI)
    ic += yazi(270, 44, '“Öğrenciler teneffüste', LAC, 'middle', True)
    ic += yazi(270, 62, 'dışarıya çıktı.”', MAVI)
    ic += yazi(270, 80, '(-ya yönelme eki almış)', LAC, 'middle', True)
    return svg(360, 98, ic, 'Dışarı çıktı ve dışarıya çıktı cümlelerinde yön sözcüğü karşılaştırması.')


def egitimdir_ki_karti():
    """Soru 13: 'Eğitimdir ki bir milleti özgür ve bağımsız yaşatır' vecize kartı."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Atatürk’ün Eğitim Özdeyişi ve Bağlaç İncelemesi', KAHVE)
    ic += kutu(14, 28, 332, 56, '#fff', ALTIN, 6, 1.2)
    ic += yazi(180, 48, '“Eğitimdir ki bir milleti özgür, bağımsız ve', LAC, 'middle', True)
    ic += yazi(180, 68, 'yüksek bir toplum hâlinde yaşatır.”', KAHVE)
    return svg(360, 96, ic, 'Eğitimdir ki bir milleti özgür ve bağımsız yaşatır özdeyiş kartı.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ara_soz_cdu_sema()
    s[2]['gorsel'] = harf_inkilabi_cozumleme()
    s[4]['gorsel'] = vurgu_dort_kart()
    s[5]['gorsel'] = maarif_kongresi_karti()
    s[6]['gorsel'] = anlam_iliskileri_sema()
    s[7]['gorsel'] = yon_kurali_akis()
    s[8]['gorsel'] = ara_soz_gorev_tablosu()
    s[11]['gorsel'] = egitimdir_ki_karti()
