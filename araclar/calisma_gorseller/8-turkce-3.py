"""8. sınıf Türkçe 3. hafta (Gezici Kütüphaneler: Dijital Uçurum, Benzetme ve Fiilimsi Türleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def hizmet_donanim_semasi():
    """Gezici kütüphanede hizmetler ve donanım ayrım şeması."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Okura Sunulan Hizmetler', 11, MAVI)
    ic += yazi(90, 38, '· Kitap ödünç verme', 10.5, LAC, 'middle', True)
    ic += yazi(90, 53, '· Ücretsiz internet erişimi', 10.5, LAC, 'middle', True)
    ic += yazi(90, 68, '· Film gösterimi ve yayınlar', 10.5, MAVI)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Araçtaki Donanımlar', 11, TUR)
    ic += yazi(270, 38, '· Bilgisayarlar ve yazıcı', 10.5, LAC, 'middle', True)
    ic += yazi(270, 53, '· Projeksiyon, LCD TV, DVD', 10.5, LAC, 'middle', True)
    ic += yazi(270, 68, '· Okur oturma grubu', 10.5, TUR)
    return svg(360, 90, ic, 'Gezici kütüphanede okura sunulan hizmetler ve araçtaki donanımlar.', 18)


def gibi_kullanim_kartlari():
    """Dört kartta gibi edatının benzetme ve örnekleme kullanımları."""
    kartlar = [
        ('I. Kart · Deniz feneri gibi', 'Benzetme (aydınlatma yönü)', MAVI, MAVI_A),
        ('II. Kart · Roman, dergi gibi', 'Örnek sıralama (teşbih yok)', KIR, KIR_A),
        ('III. Kart · Birer kanat gibi', 'Benzetme (ufuk açma yönü)', YES, YES_A),
        ('IV. Kart · Bahçıvan gibi', 'Benzetme (özenle yetiştirme)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört kartta gibi sözcüğünün benzetme ve örnek verme işlevleri.', 18)


def ulke_tasit_panosu():
    """Dünyada ve Türkiye'de gezici kütüphane taşıtları panosu."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'DÜNYADA VE TÜRKİYE’DE GEZİCİ KÜTÜPHANE TAŞITLARI', 10.5, '#fff')
    adimlar = [
        ('İsveç & Fransa', 'Gemi · Tren', MAVI, MAVI_A, 10),
        ('Norveç & Sovyet', 'Deniz-kara · Posta', TUR, TUR_A, 126),
        ('Türkiye (Ürgüp)', 'Merkep → Otobüs', YES, YES_A, 242),
    ]
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 32, 108, 56, z, r, 7, 1.2)
        ic += yazi(x + 54, 50, bas, 10.5, r)
        ic += yazi(x + 54, 70, alt, 10.5, LAC, 'middle', True)
    return svg(360, 100, ic, 'Dünyada ve Türkiye de kullanılan gezici kütüphane taşıtları panosu.', 19)


def bilgilendirici_metin_rehberi():
    """Giriş, gelişme, sonuç ve kontrol aşamalı yazma şeması."""
    asamalar = [
        ('1. Giriş Bölümü', ['Konu seçilir ve', 'kısaca tanıtılır.'], MAVI, MAVI_A, 4),
        ('2. Gelişme Bölümü', ['Açıklayıcı anlatım', 've kanıt sunulur.'], TUR, TUR_A, 122),
        ('3. Sonuç & Denetim', ['Sonuca bağlanır,', 'yazım denetlenir.'], YES, YES_A, 240),
    ]
    ic = ''
    for bas, sat, r, z, x in asamalar:
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        ic += yazi(x + 58, 20, bas, 10.5, r)
        ic += yazi(x + 58, 42, sat[0], 10.5, LAC, 'middle', True)
        ic += yazi(x + 58, 60, sat[1], 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Bilgilendirici metin yazma basamakları: Giriş, Gelişme, Sonuç ve Denetim.', 18)


def fiilimsi_ayrim_semasi():
    """İsim-fiil, sıfat-fiil ve zarf-fiil görev şeması."""
    kartlar = [
        ('İsim-fiil', 'İşin adını bildirir', 'incelemek', TUR, TUR_A, 4),
        ('Sıfat-fiil', 'İsmi niteler', 'gelen / düzenlenen', MAVI, MAVI_A, 122),
        ('Zarf-fiil', 'Nasıl / zaman', 'gülümseyerek', YES, YES_A, 240),
    ]
    ic = ''
    for bas, g, ornek, r, z, x in kartlar:
        ic += kutu(x, 4, 116, 74, z, r, 8, 1.3)
        ic += yazi(x + 58, 22, bas, 11, r)
        ic += yazi(x + 58, 44, g, 10.5, LAC, 'middle', True)
        ic += yazi(x + 58, 64, ornek, 10.5, r)
    return svg(360, 82, ic, 'Fiilimsi türleri: İsim-fiil incelemek, sıfat-fiil gelen ve düzenlenen, zarf-fiil gülümseyerek.', 18)


def benzetme_ogeleri_karti():
    """Bilginin meşaleye benzetildiği teşbih şeması."""
    ic = kutu(4, 4, 352, 76, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 20, 'Benzetme (Teşbih) Çözümleme Şeması', 11, MOR)
    ic += kutu(12, 28, 96, 44, '#fff', MAVI, 6, 1.2)
    ic += yazi(60, 46, 'Anlatılan:', 10.5, SOLUK, 'middle', True)
    ic += yazi(60, 62, 'Bilgi', 11, MAVI)
    ic += kutu(116, 36, 48, 28, YES_A, YES, 14, 1.2)
    ic += yazi(140, 54, 'gibi', 11, YES)
    ic += kutu(172, 28, 172, 44, '#fff', TUR, 6, 1.2)
    ic += yazi(258, 46, 'Benzetilen: Meşale', 10.5, TUR)
    ic += yazi(258, 62, 'Yönü: Doğru yolu aydınlatır', 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Benzetme şeması: Bilgi meşaleye benzetilmiştir, ortak özellik doğru yönü aydınlatmasıdır.', 18)


def gez_koku_fisleri():
    """gez- kökünden türetilen dört sözcük fişi (4. fiş çekimli fiil)."""
    fisler = [
        ('1. fiş · gezmek', 'İsim-fiil (işin adı)', TUR, TUR_A),
        ('2. fiş · gezerek', 'Zarf-fiil (nasıl ulaştırdı)', YES, YES_A),
        ('3. fiş · gezilen', 'Sıfat-fiil (bölümleri niteler)', MAVI, MAVI_A),
        ('4. fiş · gezdik', 'Kip ve kişi ekli çekimli fiil', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 10.8, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'gez- kökünden dört fiş: 1 gezmek, 2 gezerek, 3 gezilen, 4 gezdik.', 18)


def soru_turu_karti():
    """Metin içi ve metin dışı (çıkarım) soru karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 76, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'A Sorusu (Metin İçi)', 10.8, MAVI)
    ic += yazi(90, 40, '“Gezici kütüphanede kaç kitap', 10.5, LAC, 'middle', True)
    ic += yazi(90, 55, 've hangi cihazlar bulunur?”', 10.5, LAC, 'middle', True)
    ic += yazi(90, 71, '→ Yanıtı metinde doğrudan var', 10.5, MAVI)

    ic += kutu(184, 4, 172, 76, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'B Sorusu (Çıkarım / Öneri)', 10.8, TUR)
    ic += yazi(270, 40, '“Gelecekte bu araçlara hangi', 10.5, LAC, 'middle', True)
    ic += yazi(270, 55, 'yeni hizmetler eklenebilir?”', 10.5, LAC, 'middle', True)
    ic += yazi(270, 71, '→ Çıkarım yapılarak yanıtlanır', 10.5, TUR)
    return svg(360, 84, ic, 'Metin içi A sorusu ile metin dışı çıkarım gerektiren B sorusunun karşılaştırılması.', 18)


def gecmis_gunumuz_karti():
    """1960'lar Eşekli Kütüphaneci ile günümüz gezici kütüphane karşılaştırması."""
    ic = kutu(4, 4, 172, 74, TUR_A, TUR, 8, 1.3)
    ic += yazi(90, 20, '1960’lı Yıllar · Ürgüp', 10.8, TUR)
    ic += yazi(90, 40, 'Mustafa Güzelgöz · 35 köy', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, 'Taşıt: Yük hayvanı (merkep)', 10.5, TUR)

    ic += kutu(184, 4, 172, 74, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, 'Günümüz · Modern Araçlar', 10.8, YES)
    ic += yazi(270, 40, 'Otobüs · Bilgisayar · İnternet', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, 'Film gösterimi · 2000+ kitap', 10.5, YES)
    return svg(360, 82, ic, '1960 lı yıllarda Ürgüp te yük hayvanlarıyla taşınan kütüphane ile günümüz modern gezici kütüphane otobüsü.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = hizmet_donanim_semasi()
    s[1]['gorsel'] = gibi_kullanim_kartlari()
    s[5]['gorsel'] = ulke_tasit_panosu()
    s[6]['gorsel'] = bilgilendirici_metin_rehberi()
    s[7]['gorsel'] = fiilimsi_ayrim_semasi()
    s[8]['gorsel'] = benzetme_ogeleri_karti()
    s[9]['gorsel'] = gez_koku_fisleri()
    s[10]['gorsel'] = soru_turu_karti()
    s[13]['gorsel'] = gecmis_gunumuz_karti()
