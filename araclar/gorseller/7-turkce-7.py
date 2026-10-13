"""7. sınıf Türkçe, 7. hafta: Bir Hilal Uğruna — Bayrağımızın Altında (başlıktan tahmin ve görselden anlam, metin yapısı ve
anahtar kelimeler, derin anlam çıkarımları, medya içeriğini değerlendirme).

Kaynak: Görseller yalnız özet metnindeki (araclar/ozetler/7-turkce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Metin ve şiir cümleleri görsele alınmaz; tarihler (23 Nisan 1920, 30 Ağustos 1922, 29 Ekim 1923) özet metnindendir.
Renk anlamı:
- Tahmin ve görsel okuma: mavi = görülen/okunan (ipucu, unsur, doğrudan mesaj), turuncu = ön bilgi,
  yeşil = senin vardığın sonuç (tahmin, yargı, örtük mesaj); tepki gri zemin.
- Metin yapısı ve anahtar kelimeler: mavi = metindeki önemli bilgi ve anahtar kelime, yeşil = eş anlamlı, turuncu = zıt anlamlı,
  mor = çağrıştırdığı kelime; kesik çizgili gri kutu = anahtar olmayan kelimeler. Zaman şeridi ölçeksizdir.
- Derin anlam: mavi = metindeki kanıt (yüzey anlam), turuncu = ön bilgi, yeşil = çıkarım (derin anlam).
- Medya değerlendirme: mavi = norm (ölçütler), yeşil = ölçütü karşılayan bulgu, turuncu = karşılamayan bulgu, mor = yargı;
  2. ve 3. adım gri zemin.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı / koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12, kalinlik=2):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def _dolu(x, y, w, h, renk, rx=12):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="{RENK[renk][2]}"/>'


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _panel(x, y, w, h, rx=12, kesik=False):
    kesik_c = ' stroke-dasharray="5 4"' if kesik else ''
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" class="g-c" stroke-width="1.5"{kesik_c}/>')


def _ok(x1, y1, x2, y2, kimlik, kalinlik=2):
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" class="g-c" stroke-width="{kalinlik}" '
            f'stroke-linecap="round" marker-end="url(#{kimlik})"/>')


def tahmin_ve_gorsel():
    """Sol: ipucu + ön bilgi → tahmin → okurken denetim döngüsü → yargı. Sağ: unsur + ön bilgi → doğrudan / örtük mesaj → tepki."""
    k = 'ok7tr7a'
    ic = '<defs>' + ok_isareti(k, 'g-s') + '</defs>'
    sutunlar = [
        (8, 'Başlıktan tahmin', 'İpuçları', 'başlık, görsel, ilk bölüm', ['Çanakkale, Millî Mücadele,', 'Cumhuriyet']),
        (242, 'Görselden anlam', 'Unsurlar', 'kim/ne, nerede, renkler, nesneler', ['bayrak: vatan, bağımsızlık,', 'bir arada olmak']),
    ]
    for x0, baslik, b1, s1, s2 in sutunlar:
        cx = x0 + 111
        ic += _yazi(x0, 22, baslik, 13.5, 'g-y', True)
        ic += _kutu(x0, 32, 222, 44, 'mavi')
        ic += _yazi(x0 + 12, 51, b1, 12.5, 'g-mf', True)
        ic += _yazi(x0 + 12, 68, s1, 11.5)
        ic += _yazi(cx, 92, '+', 16, 'g-s', True, 'middle')
        ic += _kutu(x0, 98, 222, 54, 'turuncu')
        ic += _yazi(x0 + 12, 117, 'Ön bilgin', 12.5, 'g-tf', True)
        ic += _yazi(x0 + 12, 133, s2[0], 11.5)
        ic += _yazi(x0 + 12, 147, s2[1], 11.5)
        ic += _ok(cx, 156, cx, 170, k)
    # sol sütun: tahmin → okurken döngü → yargı
    x0, cx = 8, 119
    ic += _kutu(x0, 176, 222, 46, 'yesil')
    ic += _yazi(x0 + 12, 195, 'Tahmin', 12.5, 'g-yf', True)
    ic += _yazi(x0 + 12, 212, 'mantıklı bir tahmin yaz', 11.5)
    # döngü: okurken her bölüm sonunda denetlenir, gerekirse tahmine dönülüp güncellenir
    ic += (f'<path d="M{x0 + 14} 224 V266 H{x0 + 208} V228" class="g-c" stroke-width="2" stroke-linecap="round" '
           f'stroke-linejoin="round" stroke-dasharray="5 4" marker-end="url(#{k})"/>')
    ic += _yazi(cx, 244, 'okurken her bölüm sonunda:', 11.5, 'g-s', False, 'middle')
    ic += _yazi(cx, 259, 'tutuyor mu? gerekirse güncelle', 11.5, 'g-s', False, 'middle')
    ic += _ok(cx, 272, cx, 286, k)
    ic += _kutu(x0, 290, 222, 54, 'yesil')
    ic += _yazi(x0 + 12, 309, 'Yargı', 12.5, 'g-yf', True)
    ic += _yazi(x0 + 12, 325, 'metinle karşılaştır: tutan ve', 11.5)
    ic += _yazi(x0 + 12, 339, 'tutmayan yönleri belirle', 11.5)
    # sağ sütun: doğrudan mesaj, örtük mesaj → tepki
    x0, cx = 242, 353
    ic += _kutu(x0, 176, 222, 44, 'mavi')
    ic += _yazi(x0 + 12, 195, 'Doğrudan mesaj', 12.5, 'g-mf', True)
    ic += _yazi(x0 + 12, 212, 'açıkça görünen: bir tören', 11.5)
    ic += _kutu(x0, 228, 222, 44, 'yesil')
    ic += _yazi(x0 + 12, 247, 'Örtük mesaj', 12.5, 'g-yf', True)
    ic += _yazi(x0 + 12, 264, 'sezdirilen: bayrağa saygı, birlik', 11.5)
    ic += _ok(cx, 276, cx, 288, k)
    ic += _panel(x0, 292, 222, 52)
    ic += _yazi(x0 + 12, 311, 'Tepki', 12.5, 'g-y', True)
    ic += _yazi(x0 + 12, 328, 'törene katıl, duyguyu paylaş', 11.5)
    return svg(472, 352, ic, 'İki akış şeması. Başlıktan tahmin: ipuçları (başlık, görsel, ilk bölüm) artı ön bilgin (Çanakkale, Millî Mücadele, '
               'Cumhuriyet) mantıklı bir tahmine götürür; okurken her bölüm sonunda tahminin tutup tutmadığına bakılır, gerekirse güncellenir; '
               'metin bitince tahmin metinle karşılaştırılır, tutan ve tutmayan yönler belirlenip yargıya varılır. Görselden anlam: '
               'unsurlar (kim ya da ne, nerede, renkler, nesneler) artı ön bilgin (bayrak vatanı, bağımsızlığı, bir arada olmayı çağrıştırır) '
               'doğrudan mesaja (açıkça görünen, örneğin bir tören) ve örtük mesaja (sezdirilen, örneğin bayrağa saygı ve birlik) götürür; '
               'sonra tepki verilir: törene katılmak, duyguyu paylaşmak. Mavi görülen ve okunan, turuncu ön bilgi, yeşil vardığın sonuçtur.')


def yapi_ve_anahtar():
    """Üst: sıralı-kronolojik yapı zaman şeridi (üç olay, üç tarih, zaman ifadeleri, bilgiler arası ilişki).
    Alt: anahtar kelime haritası (bayrak → bağımsızlık, vatan, zafer, şehit; eş anlam, zıt anlam, çağrışım) ve anahtar olmayan kelimeler."""
    k = 'ok7tr7b'
    ic = '<defs>' + ok_isareti(k, 'g-s') + '</defs>'
    # üst: zaman şeridi (ölçeksiz)
    ic += _yazi(8, 20, 'Sıralı-kronolojik yapı', 13.5, 'g-mf', True)
    ic += _yazi(472, 20, 'önemli bilgiler: olaylar ve tarihler', 11.5, 'g-s', False, 'end')
    ic += _ok(14, 66, 468, 66, k, 2.5)
    olaylar = [(84, '23 Nisan 1920', ['Meclis açıldı'], 'Mücadelenin merkezi', 'önce'),
               (240, '30 Ağustos 1922', ['Büyük Taarruz', 'kazanıldı'], 'savaş sona erer', 'ardından'),
               (396, '29 Ekim 1923', ['Cumhuriyet', 'ilan edildi'], 'yeni yönetim biçimi', 'ertesi yıl')]
    for i, (x, tarih, olay, iliski, zaman) in enumerate(olaylar):
        ic += f'<circle cx="{x}" cy="66" r="7" class="g-mf"/>'
        ic += _yazi(x, 52, tarih, 12.5, 'g-y', True, 'middle')
        zx = x if i == 0 else (olaylar[i - 1][0] + x) / 2
        ic += _yazi(zx, 86, zaman, 11.5, 'g-s', False, 'middle')
        for j, s in enumerate(olay):
            ic += _yazi(x, 104 + j * 16, s, 12.5, 'g-mf', True, 'middle')
        ic += _yazi(x, 140, iliski, 11.5, 'g-s', False, 'middle')
    ic += '<line x1="8" y1="156" x2="472" y2="156" class="g-c" stroke-width="1" stroke-dasharray="4 4"/>'
    # alt: anahtar kelime haritası
    ic += _yazi(8, 178, 'Anahtar kelime haritası', 13.5, 'g-y', True)
    ic += _yazi(472, 178, 'başlıkta geçer, tekrar eder, anlamı taşır', 11.5, 'g-s', False, 'end')
    ic += _panel(8, 184, 186, 34, 10, kesik=True)
    ic += _yazi(16, 198, 'oldukça, ayrıca: sık geçer,', 11.5, 'g-s')
    ic += _yazi(16, 212, 'konuyu taşımaz: anahtar değil', 11.5, 'g-s')
    kx = 252
    ic += _dolu(kx - 40, 186, 80, 28, 'mavi', 14)
    ic += _yazi(kx, 205, 'bayrak', 13, 'g-b', True, 'middle')
    for x, ad, w in [(100, 'bağımsızlık', 92), (225, 'vatan', 58), (325, 'zafer', 56), (420, 'şehit', 56)]:
        ic += f'<line x1="{kx}" y1="214" x2="{x}" y2="240" class="g-c" stroke-width="2"/>'
        ic += _dolu(x - w / 2, 240, w, 28, 'mavi', 14)
        ic += _yazi(x, 259, ad, 13, 'g-b', True, 'middle')
    iliskili = [(100, 52, 'özgürlük', 74, 'mor'), (100, 146, 'egemenlik', 84, 'mor'),
                (225, 225, 'yurt', 50, 'yesil'), (325, 325, 'yenilgi', 62, 'turuncu')]
    for px, x, ad, w, renk in iliskili:
        ic += f'<line x1="{px}" y1="268" x2="{x}" y2="296" class="g-c" stroke-width="2"/>'
        ic += _kutu(x - w / 2, 296, w, 26, renk, 13, 1.5)
        ic += _yazi(x, 314, ad, 12.5, RENK[renk][2], True, 'middle')
    for x, metin, sinif in [(99, 'çağrıştırır', 'g-of'), (225, 'eş anlamlı', 'g-yf'), (325, 'zıt anlamlı', 'g-tf')]:
        ic += _yazi(x, 342, metin, 11.5, sinif, True, 'middle')
    return svg(480, 352, ic, 'Üstte sıralı-kronolojik yapının ölçeksiz zaman şeridi: önce 23 Nisan 1920, Meclis açıldı, Millî Mücadele’nin merkezi; '
               'ardından 30 Ağustos 1922, Büyük Taarruz kazanıldı, savaş sona erer; ertesi yıl 29 Ekim 1923, Cumhuriyet ilan edildi, yeni yönetim '
               'biçimi. Önemli bilgiler olaylar ve tarihlerdir. Altta anahtar kelime haritası: başlıktaki bayrak kelimesi bağımsızlık, vatan, '
               'zafer ve şehit anahtar kelimelerine bağlanır; bağımsızlık özgürlük ve egemenliği çağrıştırır (mor), vatan ile yurt eş anlamlıdır '
               '(yeşil), zafer ile yenilgi zıt anlamlıdır (turuncu). Kesik çizgili kutu: oldukça ve ayrıca sık geçer ama konuyu taşımaz, anahtar değildir.')


def derin_anlam():
    """Çıkarım formülü (kanıt + ön bilgi = çıkarım) ve basit çıkarım ile üst düzey çıkarımın karşılaştırması."""
    k = 'ok7tr7c'
    ic = '<defs>' + ok_isareti(k, 'g-s') + '</defs>'
    kutular = [(6, 'mavi', 'Metindeki kanıt', ['metnin açıkça', 'söylediği (yüzey anlam)']),
               (170, 'turuncu', 'Ön bilgin', ['metinde yazmayan,', 'senin bildiğin']),
               (334, 'yesil', 'Çıkarım', ['satır arasındaki', 'derin anlam'])]
    for x, renk, baslik, satirlar in kutular:
        ic += _kutu(x, 8, 140, 62, renk)
        ic += _yazi(x + 10, 30, baslik, 12.5, RENK[renk][2], True)
        for j, s in enumerate(satirlar):
            ic += _yazi(x + 10, 47 + j * 14, s, 11.5)
    ic += _yazi(158, 46, '+', 18, 'g-s', True, 'middle')
    ic += _yazi(322, 46, '=', 18, 'g-s', True, 'middle')
    paneller = [
        (8, 'Basit çıkarım', 'kanıt: sınırlı bölüm, tek cümle',
         [('mavi', 'her sabah direğin önünde durur'), ('mavi', 'kasketini çıkarır'), ('turuncu', 'şapka çıkarmak saygı belirtir')],
         32, ('Belli ki', 'bayrağa saygı duyuyor'), 'kanıt + ön bilgi → çıkarım'),
        (244, 'Üst düzey çıkarım', 'kanıt: metnin bütünü ve görseller',
         [('mavi', 'kasketini çıkarır'), ('mavi', 'göğsünde eski bir madalya'), ('mavi', 'torununa Çanakkale anıları'),
          ('mavi', 'köy meydanındaki anıt')],
         26, ('Demek ki', 'gazi ya da gazi yakını'), 'ne kadar çok kanıt, o kadar sağlam'),
    ]
    for x0, baslik, alt, cipler, adim, (c1, c2), notu in paneller:
        cx = x0 + 114
        ic += _panel(x0, 84, 228, 240)
        ic += _yazi(x0 + 12, 106, baslik, 13.5, 'g-y', True)
        ic += _yazi(x0 + 12, 122, alt, 11.5, 'g-s')
        y = 132
        for renk, metin in cipler:
            ic += _kutu(x0 + 12, y, 204, 22, renk, 11, 1.5)
            ic += _yazi(cx, y + 15, metin, 11.5, 'g-y', False, 'middle')
            y += adim
        y_son = y - adim + 22
        ic += _ok(cx, y_son + 4, cx, y_son + 18, k)
        yb = y_son + 22
        ic += _kutu(x0 + 12, yb, 204, 44, 'yesil', 10)
        ic += _yazi(cx, yb + 18, c1, 12.5, 'g-yf', True, 'middle')
        ic += _yazi(cx, yb + 35, c2, 12.5, 'g-yf', True, 'middle')
        ic += _yazi(cx, 314, notu, 11.5, 'g-s', False, 'middle')
    return svg(480, 332, ic, 'Çıkarım formülü: metindeki kanıt (metnin açıkça söylediği, yüzey anlam) artı ön bilgin (metinde yazmayan, senin '
               'bildiğin) eşittir çıkarım (satır arasındaki derin anlam). Altta iki panel. Basit çıkarım, kanıtı sınırlı bir bölümden, tek '
               'cümleden alır: adam her sabah direğin önünde durur ve kasketini çıkarır (mavi kanıt); şapka çıkarmak saygı belirtir (turuncu ön '
               'bilgi); çıkarım: belli ki bayrağa saygı duyuyor (yeşil). Üst düzey çıkarım, kanıtı metnin bütününden ve görsellerden toplar: '
               'kasketini çıkarır, göğsünde eski bir madalya, torununa Çanakkale anıları, köy meydanındaki anıt; çıkarım: demek ki gazi ya da '
               'gazi yakını. Ne kadar çok kanıt, o kadar sağlam çıkarım.')


def medya():
    """Dört adım (norm belirle, norma göre incele, sonuçları karşılaştır, gerekçeli yargı) ve örnek kutlama videosunun değerlendirmesi."""
    k = 'ok7tr7d'
    ic = '<defs>' + ok_isareti(k, 'g-s') + '</defs>'
    adimlar = [('mavi', '1. Norm', 'belirle'), (None, '2. Norma göre', 'incele'),
               (None, '3. Sonuçları', 'karşılaştır'), ('mor', '4. Gerekçeli', 'yargı')]
    for i, (renk, s1, s2) in enumerate(adimlar):
        x = 8 + i * 120
        if renk:
            ic += _kutu(x, 8, 98, 44, renk, 10)
            sinif = RENK[renk][2]
        else:
            ic += _panel(x, 8, 98, 44, 10)
            sinif = 'g-y'
        ic += _yazi(x + 49, 26, s1, 12, sinif, True, 'middle')
        ic += _yazi(x + 49, 42, s2, 12, sinif, True, 'middle')
        if i < 3:
            ic += _ok(x + 101, 30, x + 116, 30, k)
    # 1. norm: ölçütler
    ic += _kutu(8, 66, 200, 130, 'mavi')
    ic += _yazi(20, 88, '1. Norm (ölçütler)', 12.5, 'g-mf', True)
    for j, m in enumerate(['Görseller konuya uygun', 'Dil hedef kitleye uygun', 'Bilgiler doğru, kaynağı belli', 'Abartı ve yanlıştan uzak']):
        y = 110 + j * 20
        ic += f'<circle cx="26" cy="{y - 4}" r="3" class="g-mf"/>'
        ic += _yazi(34, y, m, 11.5)
    # 2. inceleme: örnek kutlama videosu
    ic += _panel(224, 66, 248, 130)
    ic += _yazi(236, 88, '2. İnceleme: kutlama videosu', 12.5, 'g-y', True)
    bulgular = [(True, 'görseller: bayrak ve tören sahneleri'), (True, 'dil: öğrencilere uygun'), (False, 'bilgi: ilan tarihi 1922 yazılmış')]
    for j, (uygun, m) in enumerate(bulgular):
        y = 110 + j * 20
        cx, cy = 246, y - 4
        if uygun:
            ic += f'<circle cx="{cx}" cy="{cy}" r="7" class="g-ya"/><circle cx="{cx}" cy="{cy}" r="7" class="g-ys" stroke-width="1.5"/>'
            ic += (f'<path d="M{cx - 3.5} {cy} l2.5 2.5 l4.5 -5" class="g-ys" stroke-width="2" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            ic += f'<circle cx="{cx}" cy="{cy}" r="7" class="g-ta"/><circle cx="{cx}" cy="{cy}" r="7" class="g-ts" stroke-width="1.5"/>'
            ic += f'<path d="M{cx - 3} {cy - 3} l6 6 M{cx + 3} {cy - 3} l-6 6" class="g-ts" stroke-width="2" stroke-linecap="round"/>'
        ic += _yazi(258, y, m, 11.5, 'g-y' if uygun else 'g-tf')
    ic += _yazi(258, 170, 'doğrusu 29 Ekim 1923', 11.5, 'g-tf')
    # 3. karşılaştır → 4. yargı
    ic += _ok(108, 200, 108, 214, k)
    ic += _ok(348, 200, 348, 214, k)
    ic += _yazi(228, 211, '3. normla karşılaştır', 11.5, 'g-s', False, 'middle')
    ic += _kutu(8, 218, 464, 50, 'mor')
    ic += _yazi(20, 247, '4. Yargı (gerekçeli)', 12.5, 'g-of', True)
    ic += _yazi(180, 240, 'Görsel ve dil uygun; tarih hatası', 11.5)
    ic += _yazi(180, 256, 'düzeltilmeden paylaşılmamalı.', 11.5)
    return svg(480, 276, ic, 'Medya içeriğini değerlendirmenin dört adımı: bir, norm belirle; iki, norma göre incele; üç, sonuçları normla '
               'karşılaştır; dört, gerekçeli yargıya var. Norm kutusunda (mavi) dört ölçüt: görseller konuya uygun, dil hedef kitleye uygun, '
               'bilgiler doğru ve kaynağı belli, abartı ve yanlıştan uzak. İnceleme kutusunda örnek kutlama videosunun bulguları: görseller '
               'bayrak ve tören sahneleri, uygun (yeşil onay); dil öğrencilere uygun (yeşil onay); bilgi: ilan tarihi 1922 yazılmış, doğrusu '
               '29 Ekim 1923 (turuncu çarpı). İki kutudan oklar yargı kutusuna (mor) iner: görsel ve dil uygun; tarih hatası düzeltilmeden '
               'paylaşılmamalı.')


def uygula(o):
    g = {'Başlıktan tahmin, görselden anlam': tahmin_ve_gorsel(),
         'Metin yapısı, önemli bilgiler ve anahtar kelimeler': yapi_ve_anahtar(),
         'Derin anlam: satır arasını okumak': derin_anlam(),
         'Medya içeriğini değerlendirmek': medya()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
