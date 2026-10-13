"""5. sınıf Türkçe, 7. hafta: Mustafa (dinleme stratejisi, hikâye unsurları ve metnin bölümleri, söz varlığı, şiirin biçimi
ve söz sanatları, konuşmayı başlatma-sürdürme-bitirme, ekleme bildiren bağlantı ifadeleri, büyük harf ve kesme işareti).

Görseller yalnız özet metnindeki (araclar/ozetler/5-turkce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı:
- Dinleme akışı: mavi = hazırlık soruları ve materyal seçimi, yeşil = etkileşimli dinleme, turuncu = etkileşimsiz dinleme,
  mor = tahmin basamakları.
- Yüzey anlam: mavi = soru ve kelime çözme adımları, yeşil = yüzey anlam (cevap metinde doğrudan var), turuncu = yorum
  (ipucu + kendi bilgin), gri zemin = bağlamdan tahmin örnekleri.
- Şiirin biçimi: mavi = a kafiyesi (1. ve 3. dize), turuncu = b kafiyesi (2. ve 4. dize), gri kareler = heceler,
  mor = söz sanatları.
- Konuşma: mavi = başlat, turuncu = sürdür, yeşil = bitir, mor = ekleme ifadeleriyle bağlanan düşünceler,
  gri = konuşmadan önce belirlenenler.
Bütün şemalar ölçeksizdir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _zemin(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _hap(x, y, w, h, metin, renk, boyut=13):
    return (_kutu(x, y, w, h, renk, rx=h // 2)
            + f'<text x="{x + w / 2:g}" y="{y + h / 2 + 4.5:g}" text-anchor="middle" font-size="{boyut}" '
              f'font-weight="800" class="{RENK[renk][2]}">{metin}</text>')


def _yazi(x, y, metin, boyut=12.5, sinif='g-y', hiza='middle', kalin=''):
    k = f' font-weight="{kalin}"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{hiza}" font-size="{boyut}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik, kalinlik=2):
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="g-c" stroke-width="{kalinlik}" '
            f'stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def dinleme_akisi():
    """Dinlemeye hazırlık akışı: üç soru → materyal seçimi → etkileşimli / etkileşimsiz dinleme → tahmin basamakları."""
    ic = '<defs>' + ok_isareti('ok5tr7a', 'g-s') + '</defs>'
    for x, ust, alt in [(8, 'Ne için', 'dinliyorum?'), (166, 'Ne kadar', 'zamanım var?'), (324, 'Elimde hangi', 'kaynaklar var?')]:
        cx = x + 74
        ic += _kutu(x, 8, 148, 44, 'mavi', rx=10)
        ic += _yazi(cx, 27, ust) + _yazi(cx, 44, alt)
        ic += _ok(cx, 56, cx, 69, 'ok5tr7a')
    ic += _kutu(8, 74, 464, 44, 'mavi', rx=10)
    ic += _yazi(240, 93, 'Amaca, süreye ve olanaklara göre materyali seç', 13, 'g-mf', kalin='800')
    ic += _yazi(240, 110, 'belgesel, sesli öykü, şiir kaydı ya da kitap')
    ic += _ok(120, 122, 120, 135, 'ok5tr7a') + _ok(360, 122, 360, 135, 'ok5tr7a')
    ic += _kutu(8, 140, 224, 92, 'yesil', rx=10)
    ic += _yazi(120, 160, 'Etkileşimli dinleme', 13.5, 'g-yf', kalin='800')
    ic += _yazi(120, 182, 'Karşındakiyle konuşursun,')
    ic += _yazi(120, 200, 'anlamadığını hemen sorarsın.')
    ic += _yazi(120, 220, 'Örnek: büyükannenin anısı', 12, 'g-s')
    ic += _kutu(248, 140, 224, 92, 'turuncu', rx=10)
    ic += _yazi(360, 160, 'Etkileşimsiz dinleme', 13.5, 'g-tf', kalin='800')
    ic += _yazi(360, 182, 'Kayıt ya da video izlersin,')
    ic += _yazi(360, 200, 'soru soramazsın: not al,')
    ic += _yazi(360, 218, 'işaretle, gerekirse başa sar.')
    adimlar = [(8, 'Dinlemeden önce', ['Başlık ve temadan', 'gerekçeli bir', 'tahmin yap']),
               (170, 'Dinlerken', ['Kişi, yer adlarını', 've tarihleri', 'kısa not al']),
               (332, 'Dinledikten sonra', ['Tahminin tuttu mu', 'diye kontrol et', ''])]
    for x, bas, satir in adimlar:
        cx = x + 70
        ic += _kutu(x, 246, 140, 76, 'mor', rx=10)
        ic += _yazi(cx, 264, bas, 12, 'g-of', kalin='800')
        for k, s in enumerate(satir):
            if s:
                ic += _yazi(cx, 282 + k * 16, s)
    ic += _ok(151, 284, 167, 284, 'ok5tr7a') + _ok(313, 284, 329, 284, 'ok5tr7a')
    ic += _yazi(240, 342, 'Tutmayan tahmin hata değil, dikkat için ipucudur.', 12.5, 'g-s')
    return svg(480, 350, ic, 'Dinlemeye hazırlık akışı: önce üç soru sorarsın: Ne için dinliyorum, ne kadar zamanım var, elimde hangi '
               'kaynaklar var. Amaca, süreye ve olanaklara göre materyali seçersin: belgesel, sesli öykü, şiir kaydı ya da kitap. '
               'Etkileşimli dinlemede karşındakiyle konuşur, anlamadığını hemen sorarsın; örnek, büyükannenin anısı. '
               'Etkileşimsiz dinlemede kayıt ya da video izlersin, soru soramazsın: not alır, işaretler, gerekirse başa sararsın. '
               'Dinlemeden önce başlık ve temadan gerekçeli bir tahmin yaparsın, dinlerken kişi ve yer adlarını, tarihleri kısa '
               'not alırsın, dinledikten sonra tahminin tuttu mu diye kontrol edersin. Tutmayan tahmin hata değil, dikkat için ipucudur.')


def yuzey_anlam():
    """Yüzey anlam mı, yorum mu karar şeması; bilinmeyen kelimeyi bağlamdan çözme adımları ve iki örnek."""
    ic = '<defs>' + ok_isareti('ok5tr7b', 'g-s') + '</defs>'
    ic += _kutu(116, 8, 240, 46, 'mavi', rx=10)
    ic += _yazi(236, 27, 'Sorunun cevabı metinde', 13) + _yazi(236, 45, 'cümle olarak geçiyor mu?', 13)
    ic += _ok(176, 58, 122, 86, 'ok5tr7b') + _ok(296, 58, 350, 86, 'ok5tr7b')
    ic += _yazi(128, 74, 'Evet', 13, 'g-yf', 'end', '800') + _yazi(344, 74, 'Hayır', 13, 'g-tf', 'start', '800')
    ic += _kutu(8, 92, 220, 70, 'yesil', rx=10)
    ic += _yazi(118, 114, 'Yüzey anlam', 14, 'g-yf', kalin='800')
    ic += _yazi(118, 136, 'Cevap metinde doğrudan') + _yazi(118, 154, 'söylenir; aynen alırsın.')
    ic += _kutu(244, 92, 220, 70, 'turuncu', rx=10)
    ic += _yazi(354, 114, 'Yorum', 14, 'g-tf', kalin='800')
    ic += _yazi(354, 136, 'İpuçlarını kendi bilginle') + _yazi(354, 154, 'birleştirip sonuca varırsın.')
    ic += _yazi(8, 192, 'Bilinmeyen kelimede dinlemeyi kesme; adımlar:', 13, 'g-y', 'start', '800')
    adimlar = [('Çevresindeki', 'cümlelere bak'), ('Anlamını', 'tahmin et'), ('Sözlükte', 'kontrol et'), ('Doğru anlamı', 'not al')]
    for k, (ust, alt) in enumerate(adimlar):
        x = 8 + k * 120
        ic += _kutu(x, 202, 96, 50, 'mavi', rx=10)
        ic += _yazi(x + 48, 222, ust) + _yazi(x + 48, 239, alt)
        if k < 3:
            ic += _ok(x + 99, 227, x + 115, 227, 'ok5tr7b')
    ic += _zemin(8, 268, 456, 64, rx=10)
    ornek = [(286, 'hür', 'ipucu: yanındaki “bağımsız”', 'anlam: bağımsız, özgür'),
             (316, 'nutuk', 'ipucu: törende okunur', 'anlam: konuşma, söylev')]
    for cy, kelime, ipucu, anlam in ornek:
        ic += _hap(20, cy - 12, 62, 24, kelime, 'mavi', 12.5)
        ic += _yazi(96, cy + 4.5, ipucu, 12.5, 'g-y', 'start') + _yazi(300, cy + 4.5, anlam, 12.5, 'g-y', 'start')
    return svg(472, 340, ic, 'Yüzey anlam mı, yorum mu: Sorunun cevabı metinde cümle olarak geçiyorsa yüzey anlamdır, cevap metinde '
               'doğrudan söylenir ve aynen alınır. Geçmiyorsa yorum yaparsın: ipuçlarını kendi bilginle birleştirip sonuca varırsın. '
               'Bilinmeyen kelimede dinlemeyi kesmezsin; adımlar: çevresindeki cümlelere bak, anlamını tahmin et, sözlükte kontrol et, '
               'doğru anlamı not al. Örnekler: hür kelimesinde ipucu yanındaki bağımsız kelimesidir, anlamı bağımsız, özgür; '
               'nutuk kelimesinde ipucu törende okunmasıdır, anlamı konuşma, söylev.')


def siir_bicimi():
    """Dörtlük şeması: dört dize, her dizede 11 hece, abab çapraz kafiye; altta üç söz sanatı."""
    ic = _zemin(8, 8, 456, 182, rx=12)
    ic += _yazi(22, 30, 'Dörtlük', 13, 'g-y', 'start', '800')
    ic += _yazi(151, 30, '11 hece', 12, 'g-s', kalin='800')
    ic += _yazi(297, 30, 'Kafiyeli kelime', 12, 'g-s', kalin='800')
    ic += _yazi(376, 30, 'Düzen', 12, 'g-s', kalin='800')
    dizeler = [(56, 'dalgalanır', 'mavi', 'a'), (90, 'ışıldar', 'turuncu', 'b'), (124, 'boyanır', 'mavi', 'a'), (158, 'parıldar', 'turuncu', 'b')]
    for k, (cy, kelime, renk, harf) in enumerate(dizeler, 1):
        ic += _yazi(22, cy + 4.5, f'{k}. dize', 12.5, 'g-y', 'start')
        for j in range(11):
            ic += f'<rect x="{76 + 14 * j}" y="{cy - 6}" width="11" height="11" rx="2" class="g-c" stroke-width="1.5"/>'
        ic += _hap(244, cy - 12, 106, 24, kelime, renk, 12.5)
        ic += f'<circle cx="376" cy="{cy}" r="11" class="{RENK[renk][2]}"/>'
        ic += _yazi(376, cy + 4.5, harf, 13, 'g-b', kalin='800')
    ic += '<path d="M389 56 Q436 90 389 124" class="g-ms" stroke-width="2"/>'
    ic += '<path d="M389 90 Q436 124 389 158" class="g-ts" stroke-width="2"/>'
    ic += _yazi(236, 209, 'Çapraz kafiye (abab): 1. ile 3., 2. ile 4. dize.', 12.5)
    sanatlar = [(8, 'Benzetme', '“gibi, kadar” ile başka', 'bir varlığa benzetme'),
                (163, 'Kişileştirme', 'insan olmayan varlığa', 'insan özelliği verme'),
                (318, 'Abartma', 'olduğundan çok büyük', 'ya da küçük gösterme')]
    for x, bas, s1, s2 in sanatlar:
        cx = x + 73
        ic += _kutu(x, 222, 146, 76, 'mor', rx=10)
        ic += _yazi(cx, 242, bas, 13, 'g-of', kalin='800')
        ic += _yazi(cx, 262, s1, 12) + _yazi(cx, 278, s2, 12)
    return svg(472, 306, ic, 'Dörtlük şeması: dört dize vardır, her dize on bir hecelidir; birinci dize dalgalanır, üçüncü dize boyanır '
               'kelimeleriyle biter ve a kafiyesidir; ikinci dize ışıldar, dördüncü dize parıldar kelimeleriyle biter ve b kafiyesidir. '
               'Birinci ile üçüncü, ikinci ile dördüncü dize kafiyelidir; bu düzene çapraz kafiye, abab, denir. '
               'Üç söz sanatı: benzetme, gibi ve kadar ile başka bir varlığa benzetme; kişileştirme, insan olmayan varlığa insan '
               'özelliği verme; abartma, olduğundan çok büyük ya da küçük gösterme.')


def konusma_sirasi():
    """Konuşmanın sırası: başlat → sürdür → bitir; ekleme bildiren bağlantı ifadeleriyle düşünceleri bağlama."""
    ic = '<defs>' + ok_isareti('ok5tr7c', 'g-s') + '</defs>'
    ic += _yazi(8, 27, 'Başlamadan önce belirle:', 12.5, 'g-y', 'start', '800')
    for x, w, t in [(196, 50, 'amaç'), (252, 48, 'konu'), (306, 38, 'tür'), (350, 114, 'anlatım biçimi')]:
        ic += _zemin(x, 8, w, 28, rx=14)
        ic += _yazi(x + w / 2, 27, t)
    adimlar = [(8, 'mavi', '1. Başlat', ['Selamla, hitap et,', 'ne anlatacağını', 'kısaca söyle.']),
               (168, 'turuncu', '2. Sürdür', ['Dinleyenlere bak,', 'geçiş cümlesi kur,', 'söz sırasına uy.']),
               (328, 'yesil', '3. Bitir', ['Teşekkür et,', 'soru var mı, sor;', 'sözü başkasına ver.'])]
    for x, renk, bas, satir in adimlar:
        cx = x + 68
        ic += _kutu(x, 50, 136, 98, renk, rx=10)
        ic += _yazi(cx, 74, bas, 14, RENK[renk][2], kalin='800')
        for k, s in enumerate(satir):
            ic += _yazi(cx, 96 + k * 18, s)
    ic += _ok(147, 99, 163, 99, 'ok5tr7c') + _ok(307, 99, 323, 99, 'ok5tr7c')
    ic += _yazi(8, 178, 'Ekleme ifadeleri cümleye yeni düşünce ekler:', 13, 'g-y', 'start', '800')
    dusunce = [(8, 'Törende şiir', 'okuyacağım'), (180, 'koroda marş', 'söyleyeceğim'), (352, 'sınıf panosunu', 'ben hazırladım')]
    for x, ust, alt in dusunce:
        ic += _kutu(x, 190, 112, 48, 'mor', rx=10)
        ic += _yazi(x + 56, 209, ust) + _yazi(x + 56, 226, alt)
    for x1, x2, bag in [(123, 176, 'ayrıca'), (295, 348, 'üstelik')]:
        ic += _ok(x1, 214, x2, 214, 'ok5tr7c')
        ic += _yazi((x1 + x2) / 2 + 1, 205, bag, 13, 'g-of', kalin='800')
    return svg(472, 246, ic, 'Konuşmanın sırası: Başlamadan önce amacını, konunu, türünü ve anlatım biçimini belirlersin. '
               'Bir, başlat: selamla, hitap et, ne anlatacağını kısaca söyle. İki, sürdür: dinleyenlere bak, geçiş cümlesi kur, '
               'söz sırasına uy. Üç, bitir: teşekkür et, soru var mı diye sor, sözü başkasına ver. Ekleme bildiren bağlantı '
               'ifadeleri cümleye yeni düşünce ekler: Törende şiir okuyacağım, ayrıca koroda marş söyleyeceğim, üstelik sınıf '
               'panosunu ben hazırladım.')


def uygula(o):
    g = {'Dinlemeye hazırlan: materyal, strateji ve tahmin': dinleme_akisi(),
         'Yüzey anlam ve bilinmeyen kelimeler': yuzey_anlam(),
         'Şiirin biçimi ve söz sanatları': siir_bicimi(),
         'Konuş: başlat, sürdür, bitir; ekleme bildiren bağlantı ifadeleri': konusma_sirasi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
