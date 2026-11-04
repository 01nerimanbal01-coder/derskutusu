"""6. sınıf Din Kültürü ve Ahlak Bilgisi 6. hafta (Kur'an-ı Kerim'in Özellikleri ve İlahi Kitapların Ortak Mesajı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def ilk_vahiy_karti():
    ic = kutu(8, 8, 584, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 584, 26, YES, YES, 9, 1)
    ic += yazi(300, 25, 'İLK VAHİY KİMLİK KARTI · 610 YILI', 12, '#fff')
    ic += yazi(300, 52, 'Yer: Mekke - Hira Mağarası · Zaman: Ramazan Ayı - Kadir Gecesi', 12, LAC)
    ic += yazi(300, 76, 'İlk Ayetler: Alak suresi 1-5 (“Yaratan Rabbinin adıyla oku!”) · Melek: Cebrail', 12, YES, ince=True)
    return svg(600, 100, ic, 'İlk vahyin yeri, zamanı ve Alak suresinin ilk beş ayeti bilgi kartı.', 22)


def ayet_ozellik_kartlari():
    kartlar = [
        ('Ahzâb suresi 40. ayet', 'Nebîlerin sonuncusu → Son kitap', MAVI, MAVI_A),
        ('Kadir suresi 1. ayet', 'Kadir Gecesi’nde indirilmeye başlandı', TUR, TUR_A),
        ('Hicr suresi 9. ayet', '“Onun koruyucusu elbette biziz.”', YES, YES_A),
        ('Sebe suresi 28. ayet', 'Bütün insanlara müjdeleyici - Evrensel', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Kur’an-ı Kerim’in özelliklerini bildiren dört ayet kartı.', 22)


def ana_konular_kartlari():
    kartlar = [
        ('1. Kart: Tevhit İlkesi', '“Allah birdir, O’ndan başka ilah yoktur.”', MAVI, MAVI_A),
        ('2. Kart: Kulluk Görevi', '“Namazı dosdoğru kılın, zekâtı verin.”', YES, YES_A),
        ('3. Kart: Güzel Davranış', '“Anne babaya iyilik edin, doğru söyleyin.”', TUR, TUR_A),
        ('4. Kart: Toplumsal Düzen', '“Ölçüyü ve tartıyı adaletle tam yapın.”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Kur’an’ın ana konularına örnek dört ayet mesajı kartı.', 22)


def korunma_zaman_semasi():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, 'Hz. Ebu Bekir Dönemi', 12, '#fff')
    ic += yazi(150, 52, 'Yazılı ayet parçaları bir araya getirildi', 12, LAC)
    ic += yazi(150, 74, '→ İki kapak arasında MUSHAF oldu', 12, MAVI, ince=True)

    ic += kutu(308, 8, 284, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(450, 25, 'Hz. Osman Dönemi', 12, '#fff')
    ic += yazi(450, 52, 'Mushaf nüshaları çoğaltıldı', 12, LAC)
    ic += yazi(450, 74, '→ Büyük İslam şehirlerine gönderildi', 12, TUR, ince=True)
    return svg(600, 100, ic, 'Hz. Ebu Bekir ve Hz. Osman dönemlerinde mushaf çalışmaları şeması.', 22)


def indirilme_sureci_zinciri():
    adimlar = [
        ('1. İlk Vahiy', '610 · Hira Mağarası', YES, YES_A),
        ('2. Ezber ve Yazı', 'Hafız · Vahiy Kâtibi', MAVI, MAVI_A),
        ('3. Mushaf', 'Hz. Ebu Bekir devri', TUR, TUR_A),
        ('4. Çoğaltılma', 'Hz. Osman devri', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Kur’an-ı Kerim’in indiriliş ve korunma aşamaları şeması.', 22)


def mekke_medine_panosu():
    ic = kutu(8, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, 'Mekke Dönemi (610 - 622)', 12, '#fff')
    ic += yazi(150, 52, 'İnanç, tevhit, ahiret ve güzel ahlak', 12, LAC)
    ic += yazi(150, 74, 'Sorulara ve olaylara göre adım adım', 12, YES, ince=True)

    ic += kutu(308, 8, 284, 84, CAM_A, CAM, 9, 1.6)
    ic += kutu(308, 8, 284, 26, CAM, CAM, 9, 1)
    ic += yazi(450, 25, 'Medine Dönemi (622 - 632)', 12, '#fff')
    ic += yazi(450, 52, 'İbadet, hukuk ve toplumsal kurallar', 12, LAC)
    ic += yazi(450, 74, 'Toplam 23 yılda kolayca öğrenilip yaşandı', 12, CAM, ince=True)
    return svg(600, 100, ic, 'Mekke ve Medine dönemlerinde 23 yıllık tedrici vahiy süreci panosu.', 22)


def ortak_mesaj_semasi():
    ilkeler = [
        ('Tevhit İnancı', 'Yalnız Allah’a kulluk', YES, YES_A),
        ('Peygamberlik', 'Elçilere iman ve itaat', MAVI, MAVI_A),
        ('Ahiret Günü', 'Diriliş ve hesap bilinci', TUR, TUR_A),
        ('Güzel Ahlak', 'Adalet, doğruluk ve iyilik', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(ilkeler):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Dört ilahi kitabın ortak mesajlarını gösteren dört sütunlu şema.', 22)


def meal_tefsir_karti():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, 'MEAL (Yaklaşık Anlam)', 12, '#fff')
    ic += yazi(150, 52, 'Ayetlerin başka bir dile', 12, LAC)
    ic += yazi(150, 74, 'kısa ve yaklaşık aktarımıdır', 12, MAVI, ince=True)

    ic += kutu(308, 8, 284, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, MOR, MOR, 9, 1)
    ic += yazi(450, 25, 'TEFSİR (Ayrıntılı Açıklama)', 12, '#fff')
    ic += yazi(450, 52, 'Ayetlerin iniş sebebini, bağlamını', 12, LAC)
    ic += yazi(450, 74, 've hikmetlerini genişçe açıklar', 12, MOR, ince=True)
    return svg(600, 100, ic, 'Meal ve tefsir kavramlarının kapsam karşılaştırması.', 22)


def bakara_136_karti():
    ic = kutu(8, 8, 584, 84, TUR_A, TUR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, TUR, TUR, 9, 1)
    ic += yazi(300, 25, 'BAKARA SURESİ 136. AYET MEALİ · İLAHİ KİTAPLAR ZİNCİRİ', 12, '#fff')
    ic += yazi(300, 52, '“… Mûsâ ve İsa’ya verilen ile bütün diğer peygamberlere Rab’lerinden verilene', 12, LAC)
    ic += yazi(300, 76, 'iman ettik. Onlardan hiçbirini diğerinden ayırt etmeyiz…”', 12, TUR, ince=True)
    return svg(600, 100, ic, 'Bakara suresi 136. ayet meali ve peygamberler arasında ayrım yapmama ilkesi.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ilk_vahiy_karti()
    s[4]['gorsel'] = ayet_ozellik_kartlari()
    s[5]['gorsel'] = ana_konular_kartlari()
    s[6]['gorsel'] = korunma_zaman_semasi()
    s[7]['gorsel'] = indirilme_sureci_zinciri()
    s[8]['gorsel'] = mekke_medine_panosu()
    s[9]['gorsel'] = ortak_mesaj_semasi()
    s[11]['gorsel'] = meal_tefsir_karti()
    if len(s) > 12:
        s[12]['gorsel'] = bakara_136_karti()
