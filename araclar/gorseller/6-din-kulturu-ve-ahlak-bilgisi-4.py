"""6. sınıf Din Kültürü ve Ahlak Bilgisi, 4. hafta: balık kılçığı diyagramı, değerlendirme pusulası,
vahyin gönderiliş amacını anlatan kavramların ilişkisi.

Görseller yalnız MEB 6. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap PDF s. 26-28).
Renk anlamı: balık kılçığında mavi = ana soru, yeşil = sınıflama başlıkları, mor = ana fikir; pusulada her yön kendi
rengindedir (mavi kuzey, turuncu doğu, mor güney, yeşil batı); kavram ilişkisinde mavi = akıl yolu, turuncu = vahiy yolu,
yeşil = insanın rehberlikten yararlanması. Çizimlerde ölçü yoktur; yalnız ilişkiler gösterilir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    agirlik = ' font-weight="700"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{metin}</text>'


def balik_kilcigi():
    """Balık kılçığı diyagramı: ana soru (baş), altı başlık (kılçıklar), ana fikir (kuyruk) (kitap s. 26)."""
    ic = ''
    # omurga
    ic += '<line x1="94" y1="116" x2="364" y2="116" class="g-c" stroke-width="4" stroke-linecap="round"/>'
    # baş: ana soru
    ic += '<rect x="366" y="84" width="106" height="64" rx="14" class="g-mf"/>'
    for k, t in enumerate(['Vahyin', 'getirdikleri', 'nelerdir?']):
        ic += _yazi(419, 106 + k * 16, t, 12.5, True, 'g-b')
    # kuyruk: ana fikir
    ic += '<rect x="8" y="98" width="84" height="36" rx="12" class="g-of"/>' + _yazi(50, 121, 'Ana fikir', 12.5, True, 'g-b')
    # kılçıklar: üstte ve altta üçer başlık
    ust = [('Ahlak', ['Ahlak']), ('Bilim', ['Bilim']), ('İnanç', ['İnanç'])]
    alt = [('Aile', ['Aile']), ('Toplumsal düzen', ['Toplumsal', 'düzen']), ('Hukuk', ['Hukuk'])]
    for k, ((_, satir_u), (_, satir_a)) in enumerate(zip(ust, alt)):
        cx = 146 + k * 96
        for y, satir, yukari in [(14, satir_u, True), (178, satir_a, False)]:
            ic += _kutu(cx - 42, y, 84, 40, 'yesil', 10)
            if len(satir) == 1:
                ic += _yazi(cx, y + 25, satir[0], 12.5, True)
            else:
                ic += _yazi(cx, y + 17, satir[0], 12, True) + _yazi(cx, y + 32, satir[1], 12, True)
            if yukari:
                ic += f'<line x1="{cx}" y1="58" x2="{cx + 22}" y2="112" class="g-c" stroke-width="2" stroke-linecap="round"/>'
            else:
                ic += f'<line x1="{cx}" y1="174" x2="{cx + 22}" y2="120" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    return svg(480, 232, ic, 'Balık kılçığı diyagramı: baştaki soru Vahyin getirdikleri nelerdir. Altı başlık: ahlak, aile, bilim, toplumsal düzen, inanç ve hukuk. '
               'Kuyruktaki alana çıkarımdan ulaşılan ana fikir yazılır.')


def degerlendirme_pusulasi():
    """Değerlendirme pusulası: ortada Vahyin, dört yönde dört soru (kitap s. 27)."""
    ic = ''
    # yön kolları
    ic += '<path d="M240 66 L228 118 L252 118 Z" class="g-mf"/>'
    ic += '<path d="M292 118 L240 106 L240 130 Z" class="g-tf"/>'
    ic += '<path d="M240 170 L228 118 L252 118 Z" class="g-of"/>'
    ic += '<path d="M188 118 L240 106 L240 130 Z" class="g-yf"/>'
    ic += '<circle cx="240" cy="118" r="26" class="g-z"/><circle cx="240" cy="118" r="26" class="g-c" stroke-width="2"/>'
    ic += _yazi(240, 122, 'Vahyin', 12, True)
    # dört yön kutusu: (x, y, w, renk, harf, metin)
    yonler = [(122, 6, 236, 'mavi', 'K', 'Hayatıma yön veren olay'),
              (302, 98, 176, 'turuncu', 'D', 'Öğrendiğim bilgi'),
              (122, 190, 236, 'mor', 'G', 'Güzelleştirdiğim davranış'),
              (2, 98, 176, 'yesil', 'B', 'Oluşturduğum hedef')]
    for x, y, w, renk, harf, metin in yonler:
        a, s, f = RENK[renk]
        ic += _kutu(x, y, w, 40, renk, 12)
        ic += f'<circle cx="{x + 22}" cy="{y + 20}" r="11" class="{f}"/>' + _yazi(x + 22, y + 25, harf, 12.5, True, 'g-b')
        ic += _yazi(x + 36 + (w - 42) / 2, y + 25, metin, 12.5, True)
    return svg(480, 238, ic, 'Değerlendirme pusulası: ortada Vahyin ifadesi vardır. Kuzey (K) hayata yön veren olayı, doğu (D) öğrenilen bilgiyi, '
               'güney (G) güzelleştirilen davranışı, batı (B) oluşturulan hedefi sorgular.')


def _satir(x0, y, ogeler, renk):
    """Kavram satırı: kutucuklar ok (->) ya da artı (+) ile bağlanır; sağ kenarı döndürür."""
    a, s, f = RENK[renk]
    ic, x = '', x0
    for o in ogeler:
        if o == '->':
            ic += f'<line x1="{x + 3}" y1="{y + 14}" x2="{x + 19}" y2="{y + 14}" class="g-c" stroke-width="2" marker-end="url(#okDK64k)"/>'
            x += 28
        elif o == '+':
            ic += _yazi(x + 9, y + 20, '+', 16, True, f)
            x += 18
        else:
            w = round(len(o) * 7.4 + 14)
            ic += (f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="14" class="g-z"/>'
                   f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="14" class="{s}" stroke-width="1.8"/>')
            ic += _yazi(x + w / 2, y + 19, o, 12.5, True)
            x += w
    return ic, x


def kavram_iliskisi():
    """Dokuz kavramın ilişkisi: akıl yolu, vahiy yolu, insanın rehberlikten yararlanması (kitap s. 28)."""
    ic = '<defs>' + ok_isareti('okDK64k', 'g-s') + '</defs>'
    kartlar = [('mavi', 'Allah → akıl → iyi-kötü', ['Allah', '->', 'akıl', '->', 'iyi-kötü'],
                'Akıl, doğru ile yanlışı ayırt etmeyi sağlar.'),
               ('turuncu', 'Allah → vahiy → peygamber → insan', ['Allah', '->', 'vahiy', '->', 'peygamber', '->', 'insan'],
                'Vahiy, peygamberler aracılığıyla insanlara ulaşır.'),
               ('yesil', 'rehberlik + yol göstericilik → insan → ibadet', ['rehberlik', '+', 'yol göstericilik', '->', 'insan', '->', 'ibadet'],
                'İnsan, bu rehberlikle ibadetini ve görevlerini öğrenir.')]
    for k, (renk, _, ogeler, alt) in enumerate(kartlar):
        y = 8 + k * 82
        ic += _kutu(8, y, 464, 72, renk)
        ic += f'<circle cx="28" cy="{y + 26}" r="11" class="{RENK[renk][2]}"/>' + _yazi(28, y + 31, str(k + 1), 12.5, True, 'g-b')
        satir, son = _satir(48, y + 12, ogeler, renk)
        assert son <= 458, (k, son)
        ic += satir
        ic += _yazi(48, y + 62, alt, 12, False, 'g-y', 'start')
    return svg(480, 252, ic, 'Kavramların ilişkisi: 1 Allah akıl verir, akıl iyi ile kötüyü ayırt ettirir. 2 Allah vahiy gönderir, vahiy peygamberler aracılığıyla insana ulaşır. '
               '3 Rehberlik ve yol göstericilik sayesinde insan ibadetini ve görevlerini öğrenir.')


def uygula(o):
    g = {'Pusulamız Vahiy: vahyin getirdiklerini sınıflamak': balik_kilcigi(),
         'Değerlendirme pusulası: vahyin hayata etkisi': degerlendirme_pusulasi(),
         'Kavramlarla toparlama: vahyin gönderiliş amacı': kavram_iliskisi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
