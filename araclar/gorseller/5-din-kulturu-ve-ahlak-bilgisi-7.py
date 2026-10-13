"""5. sınıf Din Kültürü ve Ahlak Bilgisi, 7. hafta: Bir Sure Öğreniyorum: İhlas Suresi (Allah İnancı ünitesi).

Görseller yalnız özet metnindeki (araclar/ozetler/5-din-kulturu-ve-ahlak-bilgisi-7.json) bilgilerle çizilir;
ders kitabı sayfası kullanılmamıştır. Dinî sembol, hat yazısı ve Arapça harf çizilmez; yalnız kavram ve ilişki şemaları.
Renk anlamı (görsel görsel):
- İhlas kavramı: mavi = sözcüğün anlamı, yeşil = dinde ihlas (doğru tutum), turuncu = surenin adını alma nedeni.
- Ana mesajlar: mavi = Allah ve O’na ait nitelikler (koyu: ayet/mesaj etiketi, açık daire: Allah),
  turuncu = yaratılmışlar (O’na muhtaç olan, O’na benzemeyen), yeşil = çıkarım (tevhit, dua, güzel isimler).
- Nerede okunur: mavi = namaz (en çok okunduğu yer), yeşil = Kur’an okuma, dua ve günlük hayat, turuncu = dinî törenler,
  mor = surenin değeri (üçte bir çubuğu), nötr yüzey = surenin kendisi.
- Hayata taşıma: mavi = surenin verdiği bilgi (neden), turuncu = davranışa yansıması (sonuç), yeşil = anlamı koruyan özet.
Çizimler ölçeksizdir; yalnız ilişkiler gösterilir. "Üçte bir" çubuğu metindeki oranı gösterir; uzunluk değil değer anlamındadır.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _koyu(x, y, w, h, renk, rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{RENK[renk][2]}"/>'


def _nötr(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boyut=12, kalin=False, sinif='g-y', hiza='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{hiza}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def _satirlar(cx, ilk_y, aralik, satirlar, boyut=12, kalin=False, sinif='g-y'):
    return ''.join(_yazi(cx, ilk_y + i * aralik, t, boyut, kalin, sinif) for i, t in enumerate(satirlar))


def _ok(x1, y1, x2, y2, kimlik, kalinlik=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="{kalinlik}" marker-end="url(#{kimlik})"/>'


def ihlas_kavrami():
    """İhlas sözcüğü → anlamları → dinde ihlas; altta surenin bu adı alma nedeni (metin: 1. bölüm)."""
    ok = 'okD7ihl'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'
    ic += _koyu(165, 8, 150, 34, 'mavi', 17) + _yazi(240, 30, 'İhlas (Arapça)', 14, True, 'g-b')
    ic += _ok(212, 44, 150, 62, ok) + _ok(268, 44, 330, 62, ok)
    ic += _kutu(14, 66, 216, 46, 'mavi') + _yazi(122, 94, 'Samimiyet, içtenlik', 13)
    ic += _kutu(250, 66, 216, 46, 'mavi') + _satirlar(358, 86, 17, ['Katışıksız,', 'saf hâle getirme'], 13)
    ic += _ok(122, 114, 190, 134, ok) + _ok(358, 114, 290, 134, ok)
    ic += _kutu(40, 138, 400, 66, 'yesil')
    ic += _yazi(240, 158, 'Dinde ihlas', 13, True, 'g-yf')
    ic += _satirlar(240, 176, 16, ['İbadet ve iyilikleri gösteriş için değil,', 'yalnızca Allah’ın rızasını kazanmak için yapmak'])
    ic += _yazi(10, 226, 'Sure bu adı neden aldı?', 12, True, 'g-s', 'start')
    ic += _kutu(10, 234, 140, 62, 'turuncu', 10) + _satirlar(80, 254, 16, ['Allah’ın birliğini', 'en saf ve en açık', 'biçimde anlatır'])
    ic += _kutu(170, 234, 140, 62, 'turuncu', 10) + _satirlar(240, 254, 16, ['İnancı yanlış', 'düşüncelerden', 'arındırır'])
    ic += _kutu(330, 234, 140, 62, 'turuncu', 10) + _yazi(400, 254, 'İhlas suresi', 12, True, 'g-tf')
    ic += _satirlar(400, 270, 16, ['Tevhit suresi', 'olarak da anılır'])
    ic += _ok(152, 265, 166, 265, ok) + _ok(312, 265, 326, 265, ok)
    return svg(480, 304, ic, 'İhlas sözcüğü Arapçadır; samimiyet, içtenlik ve bir şeyi katışıksız, saf hâle getirme anlamlarına gelir. '
               'Dinde ihlas, ibadet ve iyilikleri gösteriş için değil, yalnızca Allah’ın rızasını kazanmak için yapmaktır. '
               'Sure bu adı, Allah’ın birliğini en saf ve en açık biçimde anlattığı ve okuyanın inancını yanlış düşüncelerden '
               'arındırdığı için almıştır; Tevhit suresi olarak da anılır.')


def ana_mesajlar():
    """Bir – Samed – eşsiz ilişki şeması: her satırda ayet etiketi, küçük çizim ve mesaj (metin: 4. bölüm)."""
    ok = 'okD7mes'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'
    satirlar = [
        ('1. ayet', 'BİR', ['Allah birdir, tektir.', 'O’ndan başka', 'ilah yoktur.'], ['Tevhit: Allah’ın var ve', 'bir olduğuna inanmak']),
        ('2. ayet', 'SAMED', ['Her şey O’na muhtaçtır;', 'O ise hiçbir şeye', 'muhtaç değildir.'], ['İhtiyaçlarımızı O’ndan', 'ister, O’na dua ederiz.']),
        ('3.–4. ayet', 'EŞSİZ', ['Doğmamış, doğurmamıştır;', 'eşi, benzeri, dengi yok.', 'Ezelî ve ebedîdir.'], ['O’nu güzel isimleriyle', 'tanırız.']),
    ]
    for i, (ayet, ad, mesaj, sonuc) in enumerate(satirlar):
        y0 = 8 + i * 108
        cy = y0 + 42
        ic += _nötr(8, y0, 464, 98, 12)
        ic += _koyu(14, y0 + 6, 86, 86, 'mavi', 10) + _yazi(57, y0 + 36, ayet, 12, False, 'g-b') + _yazi(57, y0 + 66, ad, 16, True, 'g-b')
        if i == 0:
            ic += _yazi(160, cy + 4, 'ehad: bir, tek', 12, False, 'g-s')
        elif i == 1:
            ic += _kutu(108, y0 + 18, 80, 48, 'turuncu', 10) + _satirlar(148, y0 + 38, 16, ['Bütün', 'varlıklar'])
            ic += _yazi(215, y0 + 31, 'muhtaç', 11.5, False, 'g-s') + _ok(192, cy, 238, cy, ok)
        else:
            ic += _kutu(108, y0 + 18, 80, 48, 'turuncu', 10) + _satirlar(148, y0 + 38, 16, ['Hiçbir', 'varlık'])
            ic += _yazi(215, cy + 8, '≠', 22, True, 'g-y')
        ic += f'<circle cx="266" cy="{cy}" r="24" class="g-ma"/><circle cx="266" cy="{cy}" r="24" class="g-ms" stroke-width="2"/>'
        ic += _yazi(266, cy + 5, 'Allah', 13, True, 'g-mf')
        if i == 0:
            ic += _yazi(266, y0 + 86, 'tek ilah', 11.5, False, 'g-s')
        ic += _satirlar(384, y0 + 18, 15, mesaj)
        ic += _kutu(300, y0 + 56, 168, 36, 'yesil', 8) + _satirlar(384, y0 + 70, 15, sonuc, 12, False, 'g-yf')
    return svg(480, 330, ic, 'Surenin üç ana mesajı. Birinci ayet, ehad: Allah birdir, tektir; O’ndan başka ilah yoktur; buna inanmak tevhittir. '
               'İkinci ayet, Samed: bütün varlıklar Allah’a muhtaçtır, O ise hiçbir şeye muhtaç değildir; ihtiyaçlarımızı O’ndan ister, '
               'O’na dua ederiz. Üçüncü ve dördüncü ayetler: Allah doğmamış ve doğurmamıştır, eşi, benzeri ve dengi yoktur, ezelî ve '
               'ebedîdir; hiçbir varlık O’na benzemez, O’nu güzel isimleriyle tanırız.')


def nerede_okunur():
    """Merkezde İhlas suresi, çevresinde okunduğu yerler; altta Kur’an’ın üçte birine denk değer çubuğu (metin: 5. bölüm)."""
    ok = 'okD7yer'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'
    ic += _kutu(8, 8, 170, 50, 'mavi') + _yazi(93, 29, 'Namazda (en çok)', 13, True, 'g-mf') + _yazi(93, 47, 'Fatiha suresinden sonra')
    ic += _kutu(302, 8, 170, 50, 'yesil') + _yazi(387, 29, 'Kur’an-ı Kerim okurken', 12.5, True, 'g-yf') + _yazi(387, 47, 'hatim yaparken')
    ic += _kutu(8, 85, 132, 50, 'yesil') + _yazi(74, 115, 'Dua ederken', 13, True, 'g-yf')
    ic += _nötr(180, 84, 120, 52, 14) + _yazi(240, 106, 'İhlas suresi', 14, True) + _yazi(240, 124, 'kolay ezberlenir', 11.5, False, 'g-s')
    ic += _kutu(340, 85, 132, 50, 'turuncu') + _yazi(406, 106, 'Dinî törenlerde', 13, True, 'g-tf') + _yazi(406, 124, 'mevlit, cenaze')
    ic += _kutu(150, 162, 180, 78, 'yesil') + _yazi(240, 184, 'Yatmadan önce', 13, True, 'g-yf')
    for x, ad in [(156, 'İhlas'), (214, 'Felak'), (272, 'Nas')]:
        ic += _nötr(x, 196, 52, 22, 6) + _yazi(x + 26, 211, ad)
    ic += _yazi(240, 232, 'üçü art arda okunur', 11.5, False, 'g-s')
    ic += _ok(212, 82, 172, 61, ok) + _ok(268, 82, 308, 61, ok)
    ic += _ok(176, 110, 146, 110, ok) + _ok(304, 110, 334, 110, ok) + _ok(240, 140, 240, 156, ok)
    # değer çubuğu: Kur’an’ın üçte biri
    ic += '<rect x="8" y="262" width="222" height="28" rx="6" class="g-oa"/>'
    ic += '<path d="M14 262h68v28h-68a6 6 0 0 1-6-6v-16a6 6 0 0 1 6-6z" class="g-of"/>'
    ic += '<rect x="8" y="262" width="222" height="28" rx="6" class="g-os" stroke-width="1.5"/>'
    ic += '<line x1="82" y1="262" x2="82" y2="290" class="g-os" stroke-width="1.5"/>'
    ic += '<line x1="156" y1="262" x2="156" y2="290" class="g-os" stroke-width="1.5"/>'
    ic += _yazi(45, 280, 'İhlas', 12, True, 'g-b')
    ic += _yazi(242, 268, 'Kur’an’ın üçte birine denk', 12.5, True, 'g-of', 'start')
    ic += _yazi(242, 283, 'Hz. Peygamber (sav) bildirmiştir;', 11.5, False, 'g-s', 'start')
    ic += _yazi(242, 298, 'çünkü tevhidi özetler.', 11.5, False, 'g-s', 'start')
    return svg(480, 310, ic, 'İhlas suresinin okunduğu yerler: en çok namazda, Fatiha suresinden sonra; Kur’an-ı Kerim okurken ve hatim yaparken; '
               'dua ederken; yatmadan önce İhlas, Felak ve Nas sureleri art arda; mevlit ve cenaze gibi dinî törenlerde. '
               'Altta üç parçalı çubuk: Hz. Peygamber, surenin Kur’an’ın üçte birine denk olduğunu bildirmiştir, çünkü sure tevhidi özetler.')


def hayata_tasi():
    """Surenin verdiği bilgi → davranış; altta özet kuralı: sözcükler değişir, anlam aynı kalır (metin: 6. bölüm)."""
    ok = 'okD7hay'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'
    ic += _yazi(88, 18, 'Surenin verdiği bilgi', 12, True, 'g-s') + _yazi(338, 18, 'Hayatına yansıması', 12, True, 'g-s')
    satirlar = [
        (['Allah birdir,', 'tektir'], ['Yalnız O’na ibadet edersin,', 'yalnız O’ndan yardım istersin.']),
        (['Allah', 'Samed’dir'], ['Güven duyarsın: seni yaratan,', 'yaşatan, ihtiyacını karşılayan O’dur.']),
        (['Eşi ve benzeri', 'yoktur'], ['O’nu yarattıklarına benzetmezsin;', 'güzel isimleriyle tanır, dua edersin.']),
        (['Surenin adı:', 'ihlas'], ['İyilik ve ibadetlerini gösteriş için', 'değil, Allah’ın rızası için yaparsın.']),
    ]
    for i, (bilgi, davranis) in enumerate(satirlar):
        y = 28 + i * 54
        ic += _kutu(8, y, 160, 46, 'mavi', 10) + _satirlar(88, y + 19, 16, bilgi, 12.5, True, 'g-mf')
        ic += _ok(172, y + 23, 196, y + 23, ok)
        ic += _kutu(204, y, 268, 46, 'turuncu', 10) + _satirlar(338, y + 19, 16, davranis)
    ic += _yazi(240, 258, 'sözcükler değişebilir,', 11.5, False, 'g-s')
    ic += _kutu(8, 266, 190, 48, 'mavi') + _yazi(103, 295, 'Ayetlerin anlamı', 12.5, True, 'g-mf')
    ic += _yazi(240, 299, '=', 24, True)
    ic += _kutu(282, 266, 190, 48, 'yesil') + _satirlar(377, 287, 16, ['Kendi cümlelerinle', 'yazdığın özet'], 12.5, True, 'g-yf')
    ic += _yazi(240, 332, 'anlam aynı kalır', 12, True, 'g-yf')
    return svg(480, 340, ic, 'Surenin verdiği bilgi ve hayata yansıması: Allah birdir, tektir, bu yüzden yalnız O’na ibadet eder, yalnız O’ndan '
               'yardım istersin. Allah Samed’dir, bu sana güven verir: seni yaratan, yaşatan ve ihtiyacını karşılayan O’dur. Eşi ve benzeri '
               'yoktur, O’nu yarattıklarına benzetmez, güzel isimleriyle tanır ve dua edersin. Surenin adı ihlas: iyilik ve ibadetlerini '
               'gösteriş için değil, Allah’ın rızası için yaparsın. Özet kuralı: ayetlerin anlamı ile kendi cümlelerinle yazdığın özet '
               'eşittir; sözcükler değişebilir ama anlam aynı kalır.')


def uygula(o):
    g = {'İhlas ne demek, sure bu adı neden aldı?': ihlas_kavrami(),
         'Surenin ana mesajları: bir, Samed, eşsiz': ana_mesajlar(),
         'İhlas suresini nerelerde okuruz?': nerede_okunur(),
         'Surenin anlamını hayatına taşı': hayata_tasi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
