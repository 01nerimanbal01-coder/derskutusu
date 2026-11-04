"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 8. hafta (Kuvâ-yı Millîye, Cemiyetler ve Samsun'a Çıkış) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); yalnız '·' veya '-' ayırıcı (K155/K172)."""

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


def cemiyet_siniflandirma_sema():
    """Soru 1: Mondros sonrası kurulan 3 cemiyet grubu şeması."""
    gruplar = [
        ('Millî Cemiyetler', 'Kilikyalılar · Trakya', 'Tam bağımsızlık', YES, YES_A, 6),
        ('Azınlık Cemiyetleri', 'Mavri Mira · Pontus', 'Toprak parçalama', KIR, KIR_A, 124),
        ('Millî Varlığa Düşman', 'Wilson · İngiliz Muh.', 'Manda ve himaye', TUR, TUR_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in gruplar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC, 'middle', True)
        ic += yazi(x + 56, 70, s2, r)
    return svg(360, 94, ic, 'Mondros sonrası kurulan üç cemiyet grubu sınıflandırma şeması.')


def kuvayi_milliye_ozellik_sema():
    """Soru 3: Kuvâ-yı Millîye oluşum nedenleri ve katkıları şeması."""
    ic = kutu(4, 4, 172, 92, KIR_A, KIR, 8, 1.4)
    ic += yazi(90, 22, 'Doğuş Nedenleri', KIR)
    ic += yazi(90, 44, 'Anadolu’nun işgali', LAC, 'middle', True)
    ic += yazi(90, 62, 'Ordunun terhis edilmesi', LAC, 'middle', True)
    ic += yazi(90, 80, 'Hükûmetin sessizliği', KIR)

    ic += kutu(184, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(270, 22, 'Yapısı ve Katkıları', MAVI)
    ic += yazi(270, 44, 'Bölgesel · Düzensiz güç', LAC, 'middle', True)
    ic += yazi(270, 62, 'Düşmanı yavaşlattı', LAC, 'middle', True)
    ic += yazi(270, 80, 'İsyanları bastırdı', MAVI)
    return svg(360, 100, ic, 'Kuvâ-yı Millîyenin doğuş nedenleri, bölgesel yapısı ve katkıları şeması.')


def anadolu_savunma_panosu():
    """Soru 5: Dört millî cemiyetin savunduğu bölgeler panosu."""
    kartlar = [
        ('Batı · Ege Bölgesi', 'İzmir Redd-i İlhak', MAVI, MAVI_A),
        ('Doğu Karadeniz', 'Trabzon Muhafaza-i H.', YES, YES_A),
        ('Doğu Anadolu', 'Şark Vilayetleri M. H.', TUR, TUR_A),
        ('Çukurova · Adana', 'Kilikyalılar Cemiyeti', MOR, MOR_A),
    ]
    ic = ''
    for i, (bolge, cem, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, bolge, r)
        ic += yazi(x + 86, y + 36, cem, LAC, 'middle', True)
    return svg(360, 100, ic, 'Dört millî cemiyetin savunduğu Anadolu bölgeleri panosu.')


def milli_kongre_karsilastirma():
    """Soru 6: Bölgesel cemiyetler ile Millî Kongre Cemiyeti karşılaştırması."""
    ic = kutu(4, 4, 172, 90, YES_A, YES, 8, 1.4)
    ic += yazi(90, 22, 'Diğer Millî Cemiyetler', YESIL_K)
    ic += yazi(90, 46, 'Bölgesel kurtuluş amacı', LAC, 'middle', True)
    ic += yazi(90, 66, 'Kendi ilini savunma', LAC, 'middle', True)

    ic += kutu(184, 4, 172, 90, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(270, 22, 'Millî Kongre Cemiyeti', MAVI)
    ic += yazi(270, 44, 'Dr. Esat Işık · Ulusal çap', LAC, 'middle', True)
    ic += yazi(270, 62, 'Basın ve yayın yolu', LAC, 'middle', True)
    ic += yazi(270, 80, 'İlk “Kuvâ-yı Millîye” adı', MAVI)
    return svg(360, 98, ic, 'Diğer millî cemiyetler ile ulusal nitelikli Millî Kongre Cemiyeti karşılaştırması.')


def mufettislik_gorev_sema():
    """Soru 7: 9. Ordu Müfettişliği görünürdeki görev ve gerçek amaç şeması."""
    ic = kutu(4, 4, 352, 94, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 21, '9. Ordu Müfettişliği · Yetki ve Amaç Karşılaştırması', KAHVE)
    ic += kutu(12, 28, 162, 62, TUR_A, TUR, 7, 1.3)
    ic += yazi(93, 45, 'Görünürdeki Görev:', TUR)
    ic += yazi(93, 64, 'Silahları toplamak ve', LAC, 'middle', True)
    ic += yazi(93, 80, 'asayişi sağlamak', LAC, 'middle', True)

    ic += kutu(186, 28, 162, 62, YES_A, YES, 7, 1.3)
    ic += yazi(267, 45, 'Mustafa Kemal’in Amacı:', YESIL_K)
    ic += yazi(267, 64, 'Askerî-sivil emir yetkisiyle', LAC, 'middle', True)
    ic += yazi(267, 80, 'ulusu örgütleyip kurtarmak', YESIL_K)
    return svg(360, 102, ic, '9. Ordu Müfettişliği görünürdeki görev ve Mustafa Kemalin gerçek amacı şeması.')


def samsun_kronoloji_akis():
    """Soru 8: Samsun'a çıkış ve Samsun Raporu 4 adımlı kronoloji şeması."""
    adlar = [
        ('1. Adım', 'İngiliz notası', KIR, KIR_A),
        ('2. Adım', 'Müfettiş ataması', TUR, TUR_A),
        ('3. Adım', '19 Mayıs Samsun', MAVI, MAVI_A),
        ('4. Adım', 'Samsun Raporu', YES, YES_A),
    ]
    ic = kutu(4, 4, 352, 86, '#fff', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Samsun’a Çıkış Süreci Kronolojik Akışı (Mayıs 1919)', LAC)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 52, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'İngiliz notası, 9. Ordu Müfettişliği, 19 Mayıs Samsun ve Samsun Raporu akışı.')


def samsun_raporu_belge_karti():
    """Soru 9: 22 Mayıs 1919 Samsun Raporu maddeleri belge kartı."""
    ic = kutu(4, 4, 352, 98, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(180, 20, 'Tarihî Belge · Samsun Raporu (22 Mayıs 1919)', MAVI)
    maddeler = [
        ('1. Karadeniz’deki olaylardan Rum çeteleri sorumludur.', '#fff', MAVI),
        ('2. İzmir’in Yunanlılarca işgali haksızdır, kabul edilemez.', '#fff', TUR),
        ('3. Millet yabancı manda ve kontrolüne karşı tam bağımsızdır.', '#fff', YES),
    ]
    for i, (met, z, r) in enumerate(maddeler):
        y = 28 + i * 22
        ic += kutu(12, y, 336, 19, z, r, 5, 1.2)
        ic += yazi(180, y + 14, met, LAC, 'middle', True)
    return svg(360, 106, ic, '22 Mayıs 1919 Samsun Raporu temel maddeleri belge kartı.')


def zararli_cemiyetler_karsilastirma():
    """Soru 12: Azınlık cemiyetleri ve Millî varlığa düşman cemiyetlerin ortak paydası."""
    ic = kutu(4, 4, 352, 94, KIR_A, KIR, 9, 1.4)
    ic += yazi(180, 20, 'Zararlı Cemiyetlerin Karşılaştırması ve Ortak Paydası', KIR)
    ic += kutu(12, 28, 160, 40, '#fff', KIR, 6, 1.2)
    ic += yazi(92, 44, 'Azınlık Cemiyetleri:', KIR)
    ic += yazi(92, 61, 'Bağımsız devlet kurmak', LAC, 'middle', True)

    ic += kutu(188, 28, 160, 40, '#fff', TUR, 6, 1.2)
    ic += yazi(268, 44, 'Millî Varlığa Düşman:', TUR)
    ic += yazi(268, 61, 'Manda ve teslimiyet', LAC, 'middle', True)

    ic += kutu(12, 72, 336, 20, '#fff', MOR, 5, 1.2)
    ic += yazi(180, 86, 'Ortak Yön: İtilaf desteğiyle Millî Mücadele’ye karşı çıkma', MOR)
    return svg(360, 102, ic, 'Azınlık cemiyetleri ile millî varlığa düşman cemiyetlerin ortak yönü şeması.')


def sivas_birlesme_sema():
    """Soru 13: Bölgesel yararlı cemiyetlerin Sivas Kongresi'nde tek çatıda birleşmesi."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Sivas Kongresi · Millî Cemiyetlerin Birleştirilmesi', YESIL_K)
    ic += kutu(12, 28, 138, 54, '#fff', MAVI, 6, 1.2)
    ic += yazi(81, 48, 'Bölgesel Cemiyetler', MAVI)
    ic += yazi(81, 68, '(Dağınık savunma)', LAC, 'middle', True)
    ic += yazi(164, 56, '->', YESIL_K)
    ic += kutu(178, 28, 170, 54, '#fff', YES, 6, 1.4)
    ic += yazi(263, 48, 'A-R Müdafaa-i Hukuk', YESIL_K)
    ic += yazi(263, 68, '(Tek merkezden yönetim)', LAC, 'middle', True)
    return svg(360, 96, ic, 'Bölgesel millî cemiyetlerin Sivas Kongresinde tek çatıda birleşmesi şeması.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = cemiyet_siniflandirma_sema()
    s[2]['gorsel'] = kuvayi_milliye_ozellik_sema()
    s[4]['gorsel'] = anadolu_savunma_panosu()
    s[5]['gorsel'] = milli_kongre_karsilastirma()
    s[6]['gorsel'] = mufettislik_gorev_sema()
    s[7]['gorsel'] = samsun_kronoloji_akis()
    s[8]['gorsel'] = samsun_raporu_belge_karti()
    s[11]['gorsel'] = sivas_birlesme_sema()
