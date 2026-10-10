"""5. sınıf Türkçe, 4. hafta: Bir İp Bul, Oyuna Başla! (konuşma, akıcı okuma, isim ve fiil, nokta, kısa çizgi, e-posta).

Görseller yalnız MEB 5. sınıf Türkçe ders kitabındaki bilgilerle çizilir (kitap s. 33-45; PDF sayfaları s34-s45).
Renk anlamı:
- Beden dili: mavi = göz teması, turuncu = hareketler, yeşil = yüz ifadesi.
- İp oyunları: mavi = takımların yarıştığı oyunlar, turuncu = takımdan söz edilmeyen oyunlar.
- İsim ve fiil: mavi = isim, turuncu = fiil.
- Nokta ve kısa çizgi: mavi = noktanın görevleri, yeşil = doğru bölme, turuncu = yanlış bölme.
- E-posta: mavi = üst bilgi alanları, yeşil = selam-hitap ve kapanış-imza, turuncu = ileti, mor = ek.
"""
from ozet_gorsel import svg

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


def beden_dili():
    """Konuşurken beden dili: göz teması, hareketler, yüz ifadesi (kitap s. 43)."""
    ic = ''
    satir = [('mavi', 'Göz teması', 'Farklı arkadaşlarına dönerek bak.'),
             ('turuncu', 'Hareketler', 'El, kol ve beden anlatıma uysun.'),
             ('yesil', 'Yüz ifadesi', 'Heyecan, sevinç, şaşkınlık, merak.')]
    for k, (renk, etiket, aciklama) in enumerate(satir):
        y = 8 + k * 58
        ic += _hap(8, y, 130, 44, etiket, renk, 13.5)
        ic += _zemin(146, y, 318, 44)
        ic += f'<text x="160" y="{y + 27}" font-size="13" class="g-y">{aciklama}</text>'
    return svg(472, 184, ic, 'Konuşurken beden dili: göz teması kurarken farklı arkadaşlarına dönerek bak; el, kol ve beden hareketleri '
               'anlatıma uysun; yüz ifadesiyle heyecan, sevinç, şaşkınlık ve merak gösterilir.')


def ip_oyunlari():
    """Metindeki beş ip oyunu (kitap s. 35-37)."""
    ic = ''
    for x, w, t in [(8, 120, 'Oyun'), (134, 124, 'Kimler oynar'), (264, 200, 'Amaç ya da sonuç')]:
        ic += _zemin(x, 8, w, 30, rx=15)
        ic += f'<text x="{x + w / 2:g}" y="28" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">{t}</text>'
    satir = [
        ('mavi', ['Halat çekme'], ['İki takım'], ['Rakip takımı', 'çizgiden geçirmek']),
        ('turuncu', ['İp çevirme'], ['En az 5 oyuncu', '(önerilir)'], ['İpe değen oyuncu', 'ip çevirici olur']),
        ('mavi', ['İp atlamalı', 'bayrak koşusu'], ['Eşit oyunculu', 'takımlar'], ['İlk bitiren', 'takım kazanır']),
        ('turuncu', ['Lazer oyunu'], ['Bir arkadaşla', '(süre tutulur)'], ['İplere değmeden', 'hedefe ulaşmak']),
        ('turuncu', ['Kedi beşiği'], ['İki kişi'], ['İp düğüm olunca', 'oyun biter']),
    ]
    for k, (renk, c1, c2, c3) in enumerate(satir):
        y = 44 + k * 48
        for (x, w), hucre in zip([(8, 120), (134, 124), (264, 200)], [c1, c2, c3]):
            ic += _kutu(x, y, w, 42, renk, rx=10)
            if len(hucre) == 1:
                ic += f'<text x="{x + 10}" y="{y + 26}" font-size="12.5" class="g-y">{hucre[0]}</text>'
            else:
                ic += f'<text x="{x + 10}" y="{y + 18}" font-size="12.5" class="g-y">{hucre[0]}</text>'
                ic += f'<text x="{x + 10}" y="{y + 34}" font-size="12.5" class="g-y">{hucre[1]}</text>'
    ic += '<rect x="8" y="292" width="14" height="14" rx="3" class="g-mf"/>'
    ic += '<text x="28" y="304" font-size="12.5" class="g-y">Takımlar yarışır</text>'
    ic += '<rect x="168" y="292" width="14" height="14" rx="3" class="g-tf"/>'
    ic += '<text x="188" y="304" font-size="12.5" class="g-y">Takımdan söz edilmez</text>'
    return svg(472, 316, ic, 'İp oyunları: halat çekme iki takımla, rakip takımı çizgiden geçirmek için; ip çevirme en az 5 oyuncuyla, '
               'ipe değen oyuncu ip çevirici olur; ip atlamalı bayrak koşusu eşit oyunculu takımlarla, ilk bitiren takım kazanır; '
               'lazer oyunu bir arkadaşla, süre tutularak iplere değmeden hedefe ulaşmak; kedi beşiği iki kişiyle, ip düğüm olunca biter. '
               'Halat çekme ve bayrak koşusunda takımlar yarışır; diğer oyunlarda takımdan söz edilmez.')


def isim_fiil():
    """İsim (varlığa ad olan) ve fiil (iş ya da durum bildiren) kelimeler (kitap s. 34)."""
    ic = _hap(8, 8, 224, 32, 'İsim: varlığa ad olur', 'mavi')
    ic += _hap(240, 8, 224, 32, 'Fiil: iş ya da durum', 'turuncu')
    for k, t in enumerate(['Atatürk', 'sandalye', 'boyası', 'perdeler', 'halının']):
        y = 50 + k * 38
        ic += _kutu(8, y, 224, 30, 'mavi', rx=10)
        ic += f'<text x="22" y="{y + 20}" font-size="13.5" class="g-y">{t}</text>'
    for k, t in enumerate(['onarıldı', 'konulmuş', 'değişmiş', 'açıldı', 'duruyor']):
        y = 50 + k * 38
        ic += _kutu(240, y, 224, 30, 'turuncu', rx=10)
        ic += f'<text x="254" y="{y + 20}" font-size="13.5" class="g-y">{t}</text>'
    ic += '<text x="236" y="258" text-anchor="middle" font-size="12.5" class="g-s">Ek alsa da varlığa ad olan kelime isimdir.</text>'
    return svg(472, 270, ic, 'İsim, bir varlığa ad olan kelimedir: Atatürk, sandalye, boyası, perdeler, halının. '
               'Fiil, iş ya da durum bildiren kelimedir: onarıldı, konulmuş, değişmiş, açıldı, duruyor. '
               'Ek alsa da varlığa ad olan kelime isimdir.')


def nokta_cizgi():
    """Noktanın saat, binlik, adres, çarpma görevleri; satır sonunda hece sınırından bölme (kitap s. 41-42)."""
    ic = ''
    kart = [('Saat ile dakika arası', '21.30'), ('Binlik basamaklar', '2.500'),
            ('İnternet adresi', 'www.eba.gov.tr'), ('Çarpma işlemi', '9.3')]
    nokta = '<tspan font-size="19" font-weight="800" class="g-mf">.</tspan>'
    for k, (etiket, ornek) in enumerate(kart):
        x = 8 + (k % 2) * 232
        y = 8 + (k // 2) * 60
        ic += _kutu(x, y, 224, 52, 'mavi', rx=10)
        ic += f'<text x="{x + 12}" y="{y + 20}" font-size="12.5" font-weight="800" class="g-mf">{etiket}</text>'
        ic += f'<text x="{x + 12}" y="{y + 42}" font-size="14" class="g-y">{ornek.replace(".", nokta)}</text>'
    ic += '<text x="8" y="150" font-size="13" font-weight="800" class="g-y">Satır sonunda kısa çizgi: hece sınırından böl</text>'
    ornek = [(8, 'yesil', 'Doğru: oyun-cak', 'oyun-', 'cak'), (240, 'turuncu', 'Yanlış: oy-uncak', 'oy-', 'uncak')]
    for x, renk, baslik, ust, alt in ornek:
        ic += _kutu(x, 162, 224, 100, renk, rx=10)
        ic += f'<text x="{x + 12}" y="184" font-size="13" font-weight="800" class="{RENK[renk][2]}">{baslik}</text>'
        ic += _zemin(x + 12, 194, 200, 26, rx=6)
        ic += f'<text x="{x + 202}" y="212" text-anchor="end" font-size="13.5" class="g-y">{ust}</text>'
        ic += _zemin(x + 12, 226, 200, 26, rx=6)
        ic += f'<text x="{x + 22}" y="244" font-size="13.5" class="g-y">{alt}</text>'
    return svg(472, 272, ic, 'Noktanın görevleri: saat ile dakika arasında, örnek 21.30; binlik basamaklarda, örnek 2.500; internet adresinde, '
               'örnek www.eba.gov.tr; çarpma işleminde, örnek 9.3. Satır sonunda kelime hece sınırından kısa çizgiyle bölünür: '
               'oyun-cak doğru, oy-uncak yanlıştır.')


def eposta():
    """E-postanın bölümleri (kitap s. 43-44)."""
    ic = _zemin(8, 8, 456, 306, rx=12)
    satir = [
        (20, 'mavi', 'Kimden', 'gönderenin adresi'),
        (58, 'mavi', 'Kime', 'alıcının adresi'),
        (96, 'mavi', 'Konu', 'iletinin neyle ilgili olduğu'),
        (150, 'yesil', 'Selam ve hitap', 'uygun bir selam ve hitap'),
        (188, 'turuncu', 'İleti', 'nazik dille yazılmış asıl metin'),
        (226, 'yesil', 'Kapanış ve imza', 'uygun kapanış ve imza'),
        (270, 'mor', 'Ek', 'iletiyle giden dosya ya da görsel'),
    ]
    for y, renk, etiket, aciklama in satir:
        ic += _hap(20, y, 130, 30, etiket, renk, 12.5)
        ic += f'<text x="162" y="{y + 20}" font-size="12.5" class="g-y">{aciklama}</text>'
    ic += '<line x1="20" y1="138" x2="452" y2="138" class="g-c" stroke-width="1.5"/>'
    ic += '<line x1="20" y1="262" x2="452" y2="262" class="g-c" stroke-width="1.5"/>'
    return svg(472, 322, ic, 'E-postanın bölümleri: Kimden gönderenin adresi, Kime alıcının adresi, Konu iletinin neyle ilgili olduğu; '
               'uygun selam ve hitap; nazik dille yazılmış ileti; uygun kapanış ve imza; Ek satırında iletiyle giden dosya ya da görsel.')


def uygula(o):
    g = {'Konuşmanı hazırla ve beden dilini kullan': beden_dili(),
         'Akıcı okuma ve ip oyunları': ip_oyunlari(),
         'İsim ve fiil': isim_fiil(),
         'Noktanın diğer görevleri ve satır sonunda kısa çizgi': nokta_cizgi(),
         'Yaz: kısa cümleler ve e-posta': eposta()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
