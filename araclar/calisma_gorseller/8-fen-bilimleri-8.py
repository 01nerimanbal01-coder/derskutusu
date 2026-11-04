"""8. sınıf Fen Bilimleri 8. hafta (Mutasyon, Modifikasyon ve Adaptasyon) çalışma kâğıdı görselleri.
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


def uc_kavram_karsilastirma():
    """Soru 1: Mutasyon, Modifikasyon ve Adaptasyon karşılaştırma kartları."""
    kartlar = [
        ('MUTASYON', 'DNA yapısı değişir', 'Eşeyde kalıtsaldır', KIR, KIR_A, 6),
        ('MODİFİKASYON', 'Gen işleyişi değişir', 'Kalıtsal değildir', MAVI, MAVI_A, 124),
        ('ADAPTASYON', 'Çevreye uyum sağlar', 'Daima kalıtsaldır', YES, YES_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC, 'middle', True)
        ic += yazi(x + 56, 70, s2, r)
    return svg(360, 94, ic, 'Mutasyon, Modifikasyon ve Adaptasyon temel özellik kartları.')


def cuha_cicegi_deneyi():
    """Soru 3: Çuha çiçeği sıcaklığa bağlı modifikasyon şeması."""
    ic = kutu(4, 4, 352, 94, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 21, 'Çuha Çiçeğinde Sıcaklığa Bağlı Çiçek Rengi Deneyi', KAHVE)
    ic += kutu(12, 28, 158, 62, KIR_A, KIR, 7, 1.3)
    ic += yazi(91, 46, '1. Ortam: 15 - 20 °C', KIR)
    ic += yazi(91, 66, 'Kırmızı Çiçek Açar', LAC)
    ic += yazi(91, 82, '(Genotip aynı)', LAC, 'middle', True)

    ic += kutu(190, 28, 158, 62, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(269, 46, '2. Ortam: 30 - 35 °C', MAVI)
    ic += yazi(269, 66, 'Beyaz Çiçek Açar', LAC)
    ic += yazi(269, 82, '(Tohumu 18 °C’de kırmızı)', MAVI, 'middle', True)
    return svg(360, 102, ic, 'Çuha çiçeğinin 15-20 derecede kırmızı, 30-35 derecede beyaz çiçek açması şeması.')


def hucre_mutasyon_sema():
    """Soru 5: Vücut hücresi ve üreme hücresinde mutasyon karşılaştırma şeması."""
    ic = kutu(4, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += yazi(90, 22, 'Vücut (Deri) Hücresi', TUR)
    ic += yazi(90, 44, 'Etken: X Işınları', LAC, 'middle', True)
    ic += yazi(90, 62, 'DNA dizilimi bozulur', LAC, 'middle', True)
    ic += yazi(90, 80, 'Kalıtsal DEĞİLDİR', TUR)

    ic += kutu(184, 4, 172, 92, MOR_A, MOR, 8, 1.4)
    ic += yazi(270, 22, 'Üreme Ana Hücresi', MOR)
    ic += yazi(270, 44, 'Etken: X Işınları', LAC, 'middle', True)
    ic += yazi(270, 62, 'DNA dizilimi bozulur', LAC, 'middle', True)
    ic += yazi(270, 80, 'Yavrulara AKTARILIR', MOR)
    return svg(360, 100, ic, 'Deri hücresi ve üreme ana hücresinde gerçekleşen mutasyonların kalıtsallık şeması.')


def himalaya_tavsani_sema():
    """Soru 6: Himalaya tavşanı buz yastığı deneyi 3 adımlı şema."""
    adlar = [
        ('1. Adım', 'Beyaz sırt tüyü', 'kazınır', MAVI, MAVI_A, 8),
        ('2. Adım', 'Sırt bölgesine', 'buz bağlanır', TUR, TUR_A, 126),
        ('3. Adım', 'Soğuk bölgede', 'siyah kıl çıkar', YES, YES_A, 244),
    ]
    ic = kutu(4, 4, 352, 92, '#fff', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Himalaya Tavşanında Kıl Rengi Değişimi Deneyi', LAC)
    for bas, s1, s2, r, z, x in adlar:
        ic += kutu(x, 28, 108, 60, z, r, 7, 1.3)
        ic += yazi(x + 54, 45, bas, r)
        ic += yazi(x + 54, 63, s1, LAC, 'middle', True)
        ic += yazi(x + 54, 80, s2, LAC)
    return svg(360, 100, ic, 'Himalaya tavşanı sırtına buz konulduğunda siyah kıl çıkması deney şeması.')


def kutup_col_ekosistem_kartlari():
    """Soru 7: Kutup ayısı, kutup tilkisi ve çöl tilkisi adaptasyon kartları."""
    kartlar = [
        ('Kutup Ayısı', 'Beyaz post · Kutup', 'Küçük kulak · Kalın yağ', MAVI, MAVI_A, 6),
        ('Kutup Tilkisi', 'Beyaz post · Kutup', 'Küçük kulak · Kısa burun', YES, YES_A, 124),
        ('Çöl Tilkisi', 'Kum rengi · Çöl', 'Geniş kulak · Uzun kuyruk', TUR, TUR_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC)
        ic += yazi(x + 56, 70, s2, LAC, 'middle', True)
    return svg(360, 94, ic, 'Kutup ayısı, kutup tilkisi ve çöl tilkisi ekosistem uyum kartları.')


def bal_arisi_beslenme_akis():
    """Soru 8: Bal arısı larvalarında beslenmeye bağlı modifikasyon şeması."""
    ic = kutu(4, 4, 352, 92, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 20, 'Bal Arısı Larvalarında Beslenmeye Bağlı Gelişim', KAHVE)
    ic += kutu(12, 30, 98, 56, MOR_A, MOR, 7, 1.3)
    ic += yazi(61, 52, 'Arı Larvası', MOR)
    ic += yazi(61, 72, '(Aynı genotip)', LAC, 'middle', True)

    ic += kutu(126, 28, 220, 28, TUR_A, TUR, 6, 1.2)
    ic += yazi(236, 46, 'Arı sütü -> Kraliçe Arı (Verimli)', TUR)
    ic += kutu(126, 60, 220, 28, YES_A, YES, 6, 1.2)
    ic += yazi(236, 78, 'Polen -> İşçi Arı (Kısır)', YESIL_K)
    return svg(360, 100, ic, 'Bal arısı larvalarının arı sütüyle kraliçe arı, polenle işçi arı olması şeması.')


def kaktus_nilufer_adaptasyon():
    """Soru 9: Kaktüs (çöl) ve Nilüfer (su) bitki adaptasyonları karşılaştırması."""
    ic = kutu(4, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += yazi(90, 22, 'Kaktüs (Çöl Bitkisi)', TUR)
    ic += yazi(90, 44, 'İğne (diken) yapraklar', LAC, 'middle', True)
    ic += yazi(90, 62, 'Su depolayan gövde', LAC, 'middle', True)
    ic += yazi(90, 80, 'Su kaybını AZALTIR', TUR)

    ic += kutu(184, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(270, 22, 'Nilüfer (Su Bitkisi)', MAVI)
    ic += yazi(270, 44, 'Geniş yüzeyli yapraklar', LAC, 'middle', True)
    ic += yazi(270, 62, 'Hava boşluklu gövde', LAC, 'middle', True)
    ic += yazi(270, 80, 'Terlemeyi ARTIRIR', MAVI)
    return svg(360, 100, ic, 'Kaktüs ve nilüfer bitkilerinin yaprak ve gövde adaptasyonları karşılaştırması.')


def dort_ornek_kalitsallik_karti():
    """Soru 12: I Bronzlaşma, II Van kedisi göz rengi, III Kas gelişimi, IV Ördek perdeli ayak."""
    kartlar = [
        ('I. Güneşte tenin', 'bronzlaşması', MAVI, MAVI_A),
        ('II. Van kedisinin', 'farklı göz rengi', MOR, MOR_A),
        ('III. Sporcunun kol', 'kasının gelişmesi', TUR, TUR_A),
        ('IV. Ördeğin ayak', 'perdeli yapısı', YES, YES_A),
    ]
    ic = ''
    for i, (s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, s1, r)
        ic += yazi(x + 86, y + 36, s2, LAC, 'middle', True)
    return svg(360, 100, ic, 'Dört özellik kartı: I Bronzlaşma, II Van kedisi, III Kas gelişimi, IV Ördek perdeli ayak.')


def tek_yumurta_ikizleri_karti():
    """Soru 13: Tek yumurta ikizlerinde modifikasyon ve sabit kalıtsal özellikler."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Tek Yumurta İkizleri Araştırma Gözlem Kartı', MAVI)
    ic += kutu(14, 28, 160, 56, '#fff', TUR, 6, 1.2)
    ic += yazi(94, 46, 'Değişen Özellikler:', TUR)
    ic += yazi(94, 68, 'Boy ve kütle (Modifikasyon)', LAC, 'middle', True)
    ic += kutu(186, 28, 160, 56, '#fff', YES, 6, 1.2)
    ic += yazi(266, 46, 'Aynı Kalan Özellikler:', YESIL_K)
    ic += yazi(266, 68, 'Kan grubu · Göz rengi', LAC, 'middle', True)
    return svg(360, 96, ic, 'Tek yumurta ikizlerinde boy-kilo değişimi ve kan grubu-göz rengi sabitliği kartı.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = uc_kavram_karsilastirma()
    s[2]['gorsel'] = cuha_cicegi_deneyi()
    s[4]['gorsel'] = hucre_mutasyon_sema()
    s[5]['gorsel'] = himalaya_tavsani_sema()
    s[6]['gorsel'] = kutup_col_ekosistem_kartlari()
    s[7]['gorsel'] = bal_arisi_beslenme_akis()
    s[8]['gorsel'] = kaktus_nilufer_adaptasyon()
    s[11]['gorsel'] = tek_yumurta_ikizleri_karti()
