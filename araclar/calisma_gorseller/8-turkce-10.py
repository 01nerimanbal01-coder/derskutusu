"""8. sınıf Türkçe 10. hafta (3. Tema: Erdemler — Metinde Anlam ve Fiilde Çatı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def dort_cumle_yuklem_karti():
    """Soru 2 (s[1]): 4 cümle kartı (2. kart isim cümlesi: erdemdir)."""
    kartlar = [
        (4, 4, '1. Kart · Yüklem: «dizdi»', 'Sıcak somunları tezgâha dizdi.', MAVI, MAVI_A),
        (184, 4, '2. Kart · Yüklem: «erdemdir»', 'Paylaşmak en güzel erdemdir.', KIR, KIR_A),
        (4, 52, '3. Kart · Yüklem: «hazırlandı»', 'Erzak paketleri özenle hazırlandı.', YES, YES_A),
        (184, 52, '4. Kart · Yüklem: «koştu»', 'Çocuklar çınar altında koştu.', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.4)
    return svg(360, 100, ic, 'Yüklem türlerini incelemek için verilen dört cümle kartı.', 15)


def cati_inceleme_kartlari():
    """Soru 3 (s[2]): Öznesine ve nesnesine göre 4 fiil cümlesi kartı."""
    kartlar = [
        (4, 4, '1. «Ekmeği ikiye böldü.»', 'Özne: Dedem · (Onu) böldü ✓', MAVI, MAVI_A),
        (184, 4, '2. «Sokaklar süpürüldü.»', 'Başkası tarafından · -l eki', TUR, TUR_A),
        (4, 52, '3. «Sobanın yanında uyudu.»', 'Özne: Kedi · (Onu) uyudu ✗', MOR, MOR_A),
        (184, 52, '4. «Kitapları dikkatle okudu.»', 'Özne: Öğrenciler · (Onu) okudu ✓', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.1)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.4)
    return svg(360, 100, ic, 'Dört fiil cümlesinin özne ve nesne ipuçlarını içeren kartlar.', 15)


def donuslu_edilgen_panosu():
    """Soru 6 (s[5]): I. Kardeşim sevindi (Dönüşlü) ve II. Vazo onarıldı (Edilgen)."""
    ic = kutu(4, 4, 172, 84, YES_A, YES, 8)
    ic += yazi(90, 21, 'I. Cümle («-n» Çatı Eki)', YESIL_K, boy=10.2)
    ic += yazi(90, 43, '«Kardeşim sınavı kazanınca', LAC, ince=True, boy=9.6)
    ic += yazi(90, 61, 'çok sev-in-di.»', LAC, boy=9.8)
    ic += yazi(90, 79, 'Özne işi kendi üzerinde yapar', YESIL_K, ince=True, boy=9.2)

    ic += kutu(184, 4, 172, 84, MAVI_A, MAVI, 8)
    ic += yazi(270, 21, 'II. Cümle («-l» Çatı Eki)', MAVI, boy=10.2)
    ic += yazi(270, 43, '«Kırılan vazo dikkatlice', LAC, ince=True, boy=9.6)
    ic += yazi(270, 61, 'onar-ıl-dı.»', LAC, boy=9.8)
    ic += yazi(270, 79, 'Başkası tarafından yapıldı', MAVI, ince=True, boy=9.2)
    return svg(360, 92, ic, 'Sevindi ve onarıldı fiillerinin özne-yüklem ilişkisi karşılaştırma panosu.', 15)


def nesnesiz_gecisli_kartlari():
    """Soru 7 (s[6]): 4 cümle kartı (I. kartta 'bekledi' geçişli ama nesne yazılmamış)."""
    kartlar = [
        (4, 4, 'I. Kart · Yüklem: «bekledi»', '«...sonra sessizce bekledi.»', YES, YES_A),
        (184, 4, 'II. Kart · Yüklem: «uçtu»', '«...sıcak ülkelere doğru uçtu.»', MAVI, MAVI_A),
        (4, 52, 'III. Kart · Yüklem: «sildi»', '«...bütün sandalyeleri sildi.»', TUR, TUR_A),
        (184, 52, 'IV. Kart · Yüklem: «kırıldı»', '«...ağacın kuru dalları kırıldı.»', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.1)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.4)
    return svg(360, 100, ic, 'Geçişli ve geçişsiz fiillerde nesne kullanımını gösteren dört kart.', 15)


def etken_edilgen_donusum_karti():
    """Soru 8 (s[7]): Etken cümleden edilgen cümleye dönüşüm kartı."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(90, 21, 'Etken Çatılı Cümle', MAVI, boy=10.2)
    ic += yazi(90, 43, '«Gönüllü gençler sahildeki', LAC, ince=True, boy=9.6)
    ic += yazi(90, 61, 'çöpleri topladı.»', LAC, boy=9.8)
    ic += yazi(90, 78, 'Gerçek Özne: Gönüllü gençler', MAVI, ince=True, boy=9.2)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8)
    ic += yazi(270, 21, 'Edilgen Çatılı Dönüşüm', TUR, boy=10.2)
    ic += yazi(270, 43, 'Yüklem: topla-n-dı («-n» eki)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 61, 'Yeni Cümle: ?', TUR, boy=9.8)
    ic += yazi(270, 78, 'Yeni Özne Türü: ?', LAC, ince=True, boy=9.2)
    return svg(360, 90, ic, 'Etken çatılı cümlenin edilgen çatılı cümleye dönüştürülmesi şeması.', 14)


def cati_cozumleme_akis():
    """Soru 9 (s[8]): 4 adımlı fiilde çatı çözümleme akışı."""
    adimlar = [
        (4, '1. Yüklem Türü', 'Fiil mi, isim mi', 'kontrol et', MAVI, MAVI_A),
        (93, '2. Özne İlişkisi', '-l, -n eki ve', 'özneye bak', TUR, TUR_A),
        (182, '3. Nesne Testi', 'Başına «Onu»', 'zamiri getir', MOR, MOR_A),
        (271, '4. Birleştirme', 'Özne + Nesne', 'çatısını yaz', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.0)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.3)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.3)
    return svg(360, 88, ic, 'Fiilde çatı bulunurken izlenen dört aşamalı çözümleme şeması.', 14)


def somun_ekmek_okuma_karti():
    """Soru 10 (s[9]): Bir Somun Ekmekten Alınan Ders okuma kartı."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Okuma Metni Kartı · «Bir Somun Ekmekten Alınan Ders»', KAHVE)
    ic += yazi(180, 41, '«Akşamüstü fırından çıkan sıcak somun ekmeğin kokusu sokağı sardı.', LAC, ince=True, boy=9.6)
    ic += yazi(180, 59, 'İhtiyar usta, alın teriyle kazandığı ekmeğin yarısını komşusuyla', LAC, ince=True, boy=9.6)
    ic += yazi(180, 77, 'paylaştı; çünkü gözü tok ve kanaatkâr insanın kalbi daima huzurluydu.»', YESIL_K, boy=9.5)
    return svg(360, 94, ic, 'Bir Somun Ekmekten Alınan Ders metninden öyküleyici bir kesit kartı.', 15)


def iki_cumle_karsilastirma_karti():
    """Soru 12 (s[11]): topladı (Etken-Geçişli) ve toplandı (Edilgen-Geçişsiz) kartı."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8)
    ic += yazi(90, 22, '1. Cümle («topladı»)', YESIL_K, boy=10.2)
    ic += yazi(90, 44, '«Bahçıvan kurumuş', LAC, ince=True, boy=9.6)
    ic += yazi(90, 62, 'yaprakları topladı.»', LAC, boy=9.8)

    ic += kutu(184, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(270, 22, '2. Cümle («toplandı»)', KIR, boy=10.2)
    ic += yazi(270, 44, '«Kurumuş yapraklar', LAC, ince=True, boy=9.6)
    ic += yazi(270, 62, 'toplandı.»', LAC, boy=9.8)
    return svg(360, 90, ic, 'Topladı ve toplandı yüklemli iki cümlenin çatı karşılaştırma kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_cumle_yuklem_karti()
    s[2]['gorsel'] = cati_inceleme_kartlari()
    s[5]['gorsel'] = donuslu_edilgen_panosu()
    s[6]['gorsel'] = nesnesiz_gecisli_kartlari()
    s[7]['gorsel'] = etken_edilgen_donusum_karti()
    s[8]['gorsel'] = cati_cozumleme_akis()
    s[9]['gorsel'] = somun_ekmek_okuma_karti()
    s[11]['gorsel'] = iki_cumle_karsilastirma_karti()
