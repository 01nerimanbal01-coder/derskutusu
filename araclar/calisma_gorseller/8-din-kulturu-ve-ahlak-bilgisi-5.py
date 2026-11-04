"""8. sınıf Din Kültürü ve Ahlak Bilgisi 5. hafta (Kaderle İlgili Kavramlar: Ömür, Ecel, Rızık, Tevekkül, Başarı ve Sağlık) çalışma kâğıdı görselleri.
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


def ciftci_tevekkul_semasi():
    """Soru 1: Önce tedbir sonra takdir çiftçi tevekkül şeması."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'İslam’da Doğru Tevekkül Denklemi: Tedbir + Takdir', YESIL_K)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, '1. Aşama: Maddi Tedbir', MAVI)
    ic += yazi(93, 66, 'Tarlayı sür · Tohum ek · Sula', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, '2. Aşama: Dua ve Güven', YESIL_K)
    ic += yazi(267, 66, 'Bereketi Allah’tan bekle', LAC, 'middle', True)
    return svg(360, 94, ic, 'Çiftçinin tarlayı ekip suladıktan sonra Allah’a tevekkül etmesi şeması.', 12)


def ayet_hadis_kavram_panosu():
    """Soru 2: 4 ayet ve hadis kavram kartı."""
    kartlar = [
        ('Necm Suresi, 39. Ayet', '«Çalıştığının karşılığı vardır»', MAVI, MAVI_A),
        ('Hadis-i Şerif (Deve)', '«Önce bağla, sonra tevekkül et»', YES, YES_A),
        ('Hadis-i Şerif (Şifa)', '«Ey kullar, tedavi olunuz!»', TUR, TUR_A),
        ('Ankebût Suresi, 57. Ayet', '«Her can ölümü tadacaktır»', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Emek, tevekkül, sağlık ve ecel ile ilgili dört ayet-hadis kartı.', 12)


def dort_kisi_kader_soylemi():
    """Soru 4: 4 kişinin kader söylemi kartları."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Toplumdaki Kader Söylemleri · Doğru ve Yanlış Yorumlar', KAHVE)
    kisiler = [
        ('1. Kişi (Tedbirsiz)', '«Kış lastiği takmadım, alın yazım»', KIR, KIR_A, 10, 28),
        ('2. Kişi (Çalışmadan)', '«Çalışmadım, kısmette varsa olur»', KIR, KIR_A, 184, 28),
        ('3. Kişi (Bilinçli)', '«Sağlam bina yaptık, dua ettik»', YES, YES_A, 10, 58),
        ('4. Kişi (Suçlu)', '«Hata yaptım, kader mahkûmuyum»', KIR, KIR_A, 184, 58),
    ]
    for bas, alt, r, z, x, y in kisiler:
        ic += kutu(x, y, 166, 26, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 17, f'{bas}: {alt}', LAC, 'middle', True)
    return svg(360, 96, ic, 'Dört farklı kader söyleminin karşılaştırıldığı pano.', 12)


def hz_omer_sam_karantina_karti():
    """Soru 5: Hz. Ömer'in Şam veba salgınında tedbir kararı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Tarihî Örnek · Hz. Ömer ve Şam’daki Veba Salgını', MAVI)
    ic += kutu(12, 28, 162, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(93, 46, 'Alınan Tedbir Kararı', TUR)
    ic += yazi(93, 66, 'Salgın olan şehre girmemek', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Kader İlkemiz', YESIL_K)
    ic += yazi(267, 66, 'Biyolojik yasalara uyum', LAC, 'middle', True)
    return svg(360, 94, ic, 'Hz. Ömer’in veba salgınında aldığı karantina tedbiri kartı.', 12)


def kuslarin_rizik_arayisi_karti():
    """Soru 7: Kuşların sabah aç çıkıp çabalayarak tok dönmesi."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Rızık ve Gayret Dengesi · Kuşların Rızık Arayışı', KAHVE)
    adimlar = [
        ('1. İlahi Takdir', 'er-Rezzâk rızkı yaratır', YES, YES_A, 10),
        ('2. Canlının Çabası', 'Sabah yuvadan çıkıp arar', MAVI, MAVI_A, 126),
        ('3. Sonuç', 'Emekle rızka kavuşur', TUR, TUR_A, 242),
    ]
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Rızkın yaratılması ile canlının çabası arasındaki bağı gösteren şema.', 12)


def basari_tevekkul_adimlari():
    """Soru 8: Sınav başarısında 4 adımlı tevekkül kılavuzu."""
    adimlar = [
        ('1. Hedef & Plan', 'Program hazırla', MAVI, MAVI_A, 6),
        ('2. Düzenli Emek', 'Çalış & soru çöz', TUR, TUR_A, 94),
        ('3. Sağlık Tedbiri', 'Uyku & beslenme', MOR, MOR_A, 182),
        ('4. Tevekkül', 'Dua et & güven', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Sınava hazırlanırken doğru tevekkülün dört aşaması.', 12)


def ali_imran_159_levhasi():
    """Soru 9: Âl-i İmrân suresi 159. ayet levhası."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 21, 'Kur’an-ı Kerim · Âl-i İmrân Suresi 159. Ayet', YESIL_K)
    ic += kutu(14, 29, 332, 52, '#fff', ALTIN, 6, 1.2)
    ic += yazi(180, 49, '«...Bir işe karar verip azmettiğin (hazırlandığın) zaman', LAC, 'middle', True)
    ic += yazi(180, 69, 'artık Allah’a tevekkül et! Allah tevekkül edenleri sever.»', YESIL_K)
    return svg(360, 94, ic, 'Âl-i İmrân suresi 159. ayet mealini içeren levha.', 12)


def irade_ve_yanlis_kader_terazisi():
    """Soru 12: Cüzi irade sorumluluğu ile yanlış kader söylemleri karşılaştırması."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Sorumluluk Bilinci ve Yanlış Kader Söylemleri', MOR)
    ic += kutu(12, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(93, 46, 'Yanlış Söylem (Kaçış)', KIR)
    ic += yazi(93, 66, '«Alın yazım · Kader utansın»', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'İslam’ın İlkesi (Sorumluluk)', YESIL_K)
    ic += yazi(267, 66, 'Akıl + Cüzi İrade = Hesap Verme', LAC, 'middle', True)
    return svg(360, 94, ic, 'Yanlış kader söylemleri ile İslam’daki irade sorumluluğunun karşılaştırması.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ciftci_tevekkul_semasi()
    s[1]['gorsel'] = ayet_hadis_kavram_panosu()
    s[3]['gorsel'] = dort_kisi_kader_soylemi()
    s[4]['gorsel'] = hz_omer_sam_karantina_karti()
    s[6]['gorsel'] = kuslarin_rizik_arayisi_karti()
    s[7]['gorsel'] = basari_tevekkul_adimlari()
    s[8]['gorsel'] = ali_imran_159_levhasi()
    s[11]['gorsel'] = irade_ve_yanlis_kader_terazisi()
