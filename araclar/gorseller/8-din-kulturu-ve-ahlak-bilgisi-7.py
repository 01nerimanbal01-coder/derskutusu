"""8. sınıf Din Kültürü ve Ahlak Bilgisi, 7. hafta: Bir Ayet Tanıyorum: Ayetelkürsi ve Anlamı (ünite: Kader İnancı).

Görseller yalnız özet metnindeki (araclar/ozetler/8-din-kulturu-ve-ahlak-bilgisi-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: birinci görselde gri = Kur’an çerçevesi, mavi = Bakara suresi, turuncu = Ayetelkürsi (255. ayet); ikinci görselde
mavi = sözcüğün insan dilindeki anlamları (sözlük, Türkçe kullanım, simge), yeşil = ayetteki anlam (yorumcuların açıklaması),
turuncu = yanlış anlayış (koltuk ya da taht gibi düşünmek); üçüncü görselde mavi = ayetin Allah hakkında bildirdikleri (tevhit, Hay,
Kayyum, kesilmeyen gözetim), yeşil = Kayyum’un gözetimiyle süren düzen örnekleri, turuncu = insanın durumu (yorulur, uyur);
dördüncü görselde mavi = ayetin okunduğu ortamlar ve ortak nokta (sığınma, güven), turuncu = uyarı (tılsım değil, önlem de gerekir);
beşinci görselde mavi = ayette anlatılan Allah’ın sıfatları ve O’na güvenmek, yeşil = kader inancının kavramları ve insanın payına
düşen, gri = terazi (denge).
Ölçek: birinci görseldeki ayet şeridi Bakara suresinin 286 ayetini ölçekli gösterir (1 ayet ≈ 1,44 birim); 255. ayetin turuncu işareti
görünürlük için genişletilmiştir. Öteki çizimler ölçeksizdir; kutu boyutları önem ya da büyüklük göstermez.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çizgi, koyu dolgu / vurgulu yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _zemin(x, y, w, h, rx=10, cerceve='g-c'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cerceve}" stroke-width="1.5"/>')


def _yazi(x, y, metin, boyut=12, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik, sinif='g-c', kalinlik=2):
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="{sinif}" stroke-width="{kalinlik}" '
            f'stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def kuran_konum():
    """Kur’an → Bakara suresi (2. sure, 286 ayet, Medine) → 255. ayet: Ayetelkürsi. Ayet şeridi ölçekli: 412 birim = 286 ayet."""
    ic = '<defs>' + ok_isareti('okDK87a', 'g-tf') + '</defs>'
    ic += _zemin(6, 6, 468, 238, 12)
    ic += _yazi(20, 28, 'Kur’an-ı Kerim', 14, True, 'g-y', 'start')
    ic += _yazi(460, 28, 'Kur’an → sure → ayet', 12, False, 'g-s', 'end')
    ic += _kutu(20, 40, 440, 166, 'mavi', 10)
    ic += _yazi(34, 62, 'Bakara suresi', 14, True, 'g-mf', 'start')
    ic += _yazi(446, 62, '2. sure · en uzun sure · 286 ayet', 12, False, 'g-y', 'end')
    ic += _yazi(34, 80, 'Medine döneminde inmiştir', 12, False, 'g-s', 'start')
    # ayet şeridi: 286 ayet, soldan sağa; ölçek 412 / 286
    ic += _zemin(34, 94, 412, 24, 4)
    s = 412 / 286
    for n, etiket in ((0, '1'), (100, '100'), (200, '200'), (286, '286')):
        x = 34 + n * s
        ic += f'<line x1="{x:.1f}" y1="118" x2="{x:.1f}" y2="124" class="g-c" stroke-width="1.5"/>'
        ic += _yazi(round(x, 1), 137, etiket, 12, False, 'g-s')
    x255 = 34 + 254 * s   # 255. ayetin sol kenarı (≈ 399,9); işaret görünürlük için 7 birim
    ic += f'<rect x="{x255 - 2.5:.1f}" y="94" width="7" height="24" class="g-tf"/>'
    ic += _ok(round(x255 + 1, 1), 119, round(x255 + 1, 1), 150, 'okDK87a', 'g-ts')
    ic += _kutu(34, 154, 412, 42, 'turuncu', 8)
    ic += _yazi(240, 171, '255. ayet = Ayetelkürsi', 13, True, 'g-tf')
    ic += _yazi(240, 188, 'tek bir ayettir, sure değildir', 12)
    ic += _yazi(240, 228, 'Adı “kürsî” sözcüğünden gelir: “kürsü ayeti”', 12)
    return svg(480, 250, ic, 'Ayetelkürsi’nin Kur’an’daki yeri: Kur’an-ı Kerim içinde Bakara suresi, Bakara suresi içinde 255. ayet. '
               'Bakara suresi Kur’an’ın ikinci ve en uzun suresidir, 286 ayettir ve Medine döneminde inmiştir. 286 ayetlik şeritte 255. ayet '
               'sona yakın bir yerde işaretlidir: Ayetelkürsi tek bir ayettir, sure değildir. Adı ayette geçen kürsî sözcüğünden gelir, kürsü ayeti demektir.')


def kursu_anlam():
    """Kürsü sözcüğünün anlam katmanları: sözlük anlamı → Türkçedeki kullanımı → simge; ayette ilim, kudret, hükümranlık."""
    ic = '<defs>' + ok_isareti('okDK87b', 'g-s') + '</defs>'
    ust = [(6, 150, 'Sözlük anlamı', 'Arapça “kürsî”:', 'oturulan yer, koltuk, taht'),
           (174, 150, 'Türkçede kürsü', 'öğretmen, hatip kürsüsü:', 'söz sahibinin saygın yeri'),
           (342, 132, 'Simge', 'yetki ve egemenlik', 'simgesi')]
    for x, w, baslik, s1, s2 in ust:
        cx = x + w / 2
        ic += _kutu(x, 6, w, 70, 'mavi', 10) + _yazi(cx, 28, baslik, 12.5, True, 'g-mf') + _yazi(cx, 47, s1) + _yazi(cx, 65, s2)
    ic += _ok(159, 41, 170, 41, 'okDK87b') + _ok(327, 41, 338, 41, 'okDK87b')
    ic += _ok(240, 80, 240, 104, 'okDK87b')
    ic += _kutu(6, 110, 468, 138, 'yesil')
    ic += _yazi(240, 132, 'Ayette: Allah’ın kürsüsü gökleri ve yeri kaplar', 13.5, True, 'g-yf')
    ic += _yazi(240, 150, 'Kur’an yorumcularına göre bu söz şunu anlatır:', 12, False, 'g-s')
    for x, (ad, s1, s2) in zip((20, 169, 318), (('İlim', 'bilgisinin ulaşmadığı', 'yer yoktur'),
                                               ('Kudret', 'gücünün yetmediği', 'yer yoktur'),
                                               ('Hükümranlık', 'egemenliğinin dışında', 'kalan yer yoktur'))):
        cx = x + 71
        ic += _zemin(x, 162, 142, 74, 10, 'g-ys') + _yazi(cx, 184, ad, 13, True, 'g-yf') + _yazi(cx, 204, s1) + _yazi(cx, 220, s2)
    ic += _kutu(6, 260, 468, 52, 'turuncu')
    ic += _yazi(240, 282, 'Koltuk ya da taht gibi düşünülmez', 13, True, 'g-tf')
    ic += _yazi(240, 301, 'Allah, yarattığı hiçbir şeye benzemez.', 12)
    return svg(480, 318, ic, 'Kürsü sözcüğünün anlam katmanları: sözlük anlamı Arapça kürsî, oturulan yer, koltuk, taht; Türkçede öğretmen '
               'ya da hatip kürsüsü, söz sahibinin saygın yeri; buradan yetki ve egemenlik simgesi. Ayette Allah’ın kürsüsünün gökleri ve yeri '
               'kaplaması, Kur’an yorumcularına göre ilmini, kudretini ve hükümranlığını anlatır: bilgisinin ulaşmadığı, gücünün yetmediği, '
               'egemenliğinin dışında kalan yer yoktur. Kürsü, koltuk ya da taht gibi düşünülmez; Allah yarattığı hiçbir şeye benzemez.')


def hay_kayyum():
    """Ayetin ilk mesajları: tevhit, Hay, Kayyum (ve gözetimiyle süren düzen), uyuklama ve uykunun O’nu tutmaması."""
    ic = '<defs>' + ok_isareti('okDK87c', 'g-s') + '</defs>'
    ic += _kutu(6, 6, 232, 70, 'mavi') + _yazi(122, 28, 'Tevhit', 13.5, True, 'g-mf')
    ic += _yazi(122, 47, 'Allah’tan başka ilah yoktur') + _yazi(122, 65, 'kelimeitevhit: Lâ ilâhe illallah')
    ic += _kutu(250, 6, 224, 70, 'mavi') + _yazi(362, 28, 'Hay', 13.5, True, 'g-mf')
    ic += _yazi(362, 47, 'Allah diridir; hayatının') + _yazi(362, 65, 'başlangıcı ve sonu yoktur')
    ic += _kutu(6, 88, 468, 70, 'mavi') + _yazi(240, 110, 'Kayyum', 13.5, True, 'g-mf')
    ic += _yazi(240, 128, 'kendi varlığı için hiçbir şeye muhtaç değildir;') + _yazi(240, 146, 'bütün varlıkları var eder, yönetir, ayakta tutar')
    ic += _ok(240, 162, 240, 174, 'okDK87c')
    ic += _kutu(6, 178, 468, 84, 'yesil') + _yazi(240, 198, 'Allah’ın evreni her an gözetmesiyle sürer:', 12.5, True, 'g-yf')
    for x, (ad, s1) in zip((18, 169, 320), (('Gezegenler', 'yörüngesinde kalır'), ('Mevsimler', 'düzenli döner'), ('Kalbin', 'sen uyurken bile atar'))):
        cx = x + 71
        ic += _zemin(x, 206, 142, 46, 10, 'g-ys') + _yazi(cx, 225, ad, 12, True, 'g-yf') + _yazi(cx, 243, s1)
    ic += _kutu(6, 274, 228, 70, 'turuncu') + _yazi(120, 296, 'İnsan', 13, True, 'g-tf')
    ic += _yazi(120, 314, 'yorulur, dalgınlaşır, uyur;') + _yazi(120, 332, 'çevresinden habersiz kalır')
    ic += _kutu(246, 274, 228, 70, 'mavi') + _yazi(360, 296, 'Allah', 13, True, 'g-mf')
    ic += _yazi(360, 314, 'uyuklama ve uyku O’nu tutmaz;') + _yazi(360, 332, 'gözetimi bir an bile kesilmez')
    return svg(480, 350, ic, 'Ayetin ilk mesajları kutu şemasında: Tevhit, Allah’tan başka ilah yoktur; ayetin ilk cümlesi kelimeitevhidin, '
               'Lâ ilâhe illallah sözünün anlamını taşır. Hay: Allah diridir, hayatının başlangıcı ve sonu yoktur. Kayyum: kendi varlığı için '
               'hiçbir şeye muhtaç değildir; bütün varlıkları var eder, yönetir ve ayakta tutar. Gezegenlerin yörüngesinde kalması, mevsimlerin '
               'düzenli dönmesi ve kalbin sen uyurken bile atması Allah’ın evreni her an gözetmesiyle sürer. İnsan yorulur, dalgınlaşır, uyur '
               've çevresinden habersiz kalır; Allah’ı ise uyuklama ve uyku tutmaz, gözetimi bir an bile kesilmez.')


def nerede_okunur():
    """Ayetelkürsi’nin okunduğu ortamlar ve ortak nokta: Allah’a sığınma ve güven; tılsım değildir, önlem de gerekir."""
    ic = '<defs>' + ok_isareti('okDK87d', 'g-mf') + '</defs>'
    sol = [('Namazların sonunda', 'selam verdikten sonra'), ('Yatmadan önce', 'sabaha kadar koruma'), ('Kur’an okurken', 'Bakara suresi içinde')]
    sag = [('Hatim, mevlit', 'cenaze, taziye'), ('Yola çıkarken', 'bir işe başlarken'), ('Korku ve sıkıntı', 'anlarında')]
    for i, ((b1, a1), (b2, a2)) in enumerate(zip(sol, sag)):
        y = 6 + i * 66
        ic += _kutu(6, y, 142, 56, 'mavi', 10) + _yazi(77, y + 24, b1, 12, True, 'g-mf') + _yazi(77, y + 42, a1)
        ic += _kutu(332, y, 142, 56, 'mavi', 10) + _yazi(403, y + 24, b2, 12, True, 'g-mf') + _yazi(403, y + 42, a2)
        ic += _ok(152, y + 28, 176, 100, 'okDK87d', 'g-ms') + _ok(328, y + 28, 304, 100, 'okDK87d', 'g-ms')
    ic += '<rect x="182" y="70" width="116" height="60" rx="14" class="g-mf"/>'
    ic += _yazi(240, 91, 'Ortak nokta', 12.5, True, 'g-b') + _yazi(240, 108, 'Allah’a sığınma', 12, False, 'g-b') + _yazi(240, 124, 've O’na güvenme', 12, False, 'g-b')
    ic += _kutu(6, 206, 468, 70, 'turuncu') + _yazi(240, 228, 'Tılsım ya da muska değildir', 13, True, 'g-tf')
    ic += _yazi(240, 246, 'anlamını bilerek, dua niyetiyle okunur;') + _yazi(240, 264, 'korunmak: önlem almak + Allah’a tevekkül etmek')
    return svg(480, 282, ic, 'Ayetelkürsi’nin okunduğu ortamlar: namazların sonunda selam verdikten sonra, yatmadan önce (sabaha kadar '
               'koruma), Kur’an okurken Bakara suresi içinde, hatim ve mevlitte, cenaze ve taziyede, yola çıkarken ve bir işe başlarken, korku '
               've sıkıntı anlarında. Bütün okların gösterdiği ortak nokta Allah’a sığınma ve O’na güvenmedir. Ayet tılsım ya da muska değildir; '
               'anlamını bilerek, dua niyetiyle okunur; korunmak için önlem almak ve Allah’a tevekkül etmek gerekir.')


def kader_bagi():
    """Ayette anlatılan sıfatlar (ilim, kudret, hükümranlık, Kayyum) kader inancının kavramlarına temel olur; doğru kader inancı dengedir."""
    ic = '<defs>' + ok_isareti('okDK87e', 'g-s') + '</defs>'
    ic += _kutu(6, 6, 200, 194, 'mavi') + _yazi(20, 30, 'Ayetelkürsi’de Allah', 13.5, True, 'g-mf', 'start')
    for i, (ad, s1) in enumerate((('İlim', 'her şeyi bilir'), ('Kudret', 'gücü her şeye yeter'), ('Hükümranlık', 'her şey O’nundur'),
                                  ('Kayyum', 'her şeyi ayakta tutar, gözetir'))):
        y = 58 + i * 38
        ic += _yazi(20, y, ad, 12.5, True, 'g-mf', 'start') + _yazi(20, y + 16, s1, 12, False, 'g-y', 'start')
    for i, (ad, s1) in enumerate((('Kader', 'ölçüyle bilme ve takdir etme'), ('Sünnetullah (düzen)', 'evrenin yasaları bozulmadan sürer'),
                                  ('Tevekkül', 'görevini yap, sonucu O’na bırak'), ('Sorumluluk', 'seçimi insan yapar ve sorumludur'))):
        y = 6 + i * 50
        ic += _kutu(250, y, 224, 44, 'yesil', 10) + _yazi(262, y + 19, ad, 12.5, True, 'g-yf', 'start') + _yazi(262, y + 36, s1, 12, False, 'g-y', 'start')
        ic += _ok(226, y + 22, 244, y + 22, 'okDK87e')
    ic += '<line x1="210" y1="103" x2="226" y2="103" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    ic += '<line x1="226" y1="28" x2="226" y2="178" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    # terazi: iki kefe dengede
    ic += _yazi(240, 232, 'Doğru kader inancı bir dengedir', 13, True)
    ic += '<line x1="110" y1="262" x2="370" y2="262" class="g-c" stroke-width="3" stroke-linecap="round"/>'
    ic += '<line x1="120" y1="262" x2="120" y2="284" class="g-c" stroke-width="2"/><line x1="360" y1="262" x2="360" y2="284" class="g-c" stroke-width="2"/>'
    ic += '<rect x="236" y="262" width="8" height="70" class="g-mf"/><rect x="214" y="330" width="52" height="6" rx="3" class="g-mf"/>'
    ic += '<circle cx="240" cy="262" r="6" class="g-mf"/>'
    ic += _kutu(24, 284, 192, 42, 'mavi', 10) + _yazi(120, 302, 'Allah’ın ilmine ve') + _yazi(120, 320, 'kudretine güvenmek')
    ic += _kutu(264, 284, 192, 42, 'yesil', 10) + _yazi(360, 302, 'kendi payına düşeni') + _yazi(360, 320, 'yapmak, önlem almak')
    return svg(480, 340, ic, 'Ayetelkürsi ile kader inancının bağı: ayette anlatılan Allah her şeyi bilir (ilim), gücü her şeye yeter (kudret), '
               'her şey O’nundur (hükümranlık), her şeyi ayakta tutar ve gözetir (Kayyum). Bu sıfatlar kader inancının kavramlarına temel olur: '
               'kader, ölçüyle bilme ve takdir etme; sünnetullah, evrenin yasalarının bozulmadan sürmesi; tevekkül, görevini yapıp sonucu Allah’a '
               'bırakmak; sorumluluk, seçimi insanın yapması. Altta dengede duran terazi: bir kefede Allah’ın ilmine ve kudretine güvenmek, '
               'öteki kefede kendi payına düşeni yapmak ve önlem almak; doğru kader inancı bu dengedir.')


def uygula(o):
    g = {'Ayetelkürsi Kur’an’ın neresinde?': kuran_konum(),
         'Kürsü sözcüğü ne anlatır?': kursu_anlam(),
         'Ayetin mesajları: Allah birdir, diridir, her şeyi ayakta tutar': hay_kayyum(),
         'Ayetelkürsi nerelerde okunur?': nerede_okunur(),
         'Ayetelkürsi ve kader inancı': kader_bagi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
