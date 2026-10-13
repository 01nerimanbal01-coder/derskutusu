"""7. sınıf Fen Bilimleri, 2. hafta: uzay gözlem araçlarının modeli, uzay kirliliği ve altı ayakkabı tekniği.

Görseller yalnız MEB 7. sınıf Fen Bilimleri ders kitabındaki bilgilerle çizilir (s29 model performans görevi,
s30 uzay kirliliği haberi, s31-s32 altı ayakkabı tekniği ve uzay kirliliğinin sonuçları); metin cümleleri görsele alınmaz.
Renk anlamı:
- Model adımları: mavi = hazırlık (plan, çizim), turuncu = yapım, yeşil = sunum, mor = geliştirme; gri = araç seçenekleri.
- Uzay çöpü: yeşil = çalışan uydu, turuncu = işlevsiz parçalar; gri = Uzay Gözetim Ağı.
- Sorunlar: turuncu = sorunun kaynağı, mor = sonuç, mavi = aksayabilecek alanlar.
- Altı ayakkabı: kart başındaki daire ayakkabının kendi rengidir (kitaptaki adıyla).
"""
import math

from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _gri(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _yazi(x, y, metin, boy=12.5, sinif='g-y', kalin=False, hiza='middle'):
    k = ' font-weight="800"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{boy}"{k} class="{sinif}">{metin}</text>'


def _ok(x1, y1, x2, y2, kimlik):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" '
            f'marker-end="url(#{kimlik})"/>')


def _iki(sekil, renk):
    """Aynı şekli önce açık dolguyla, sonra çerçeveyle çizer."""
    a, s, _ = RENK[renk]
    return sekil.replace('/>', f' class="{a}"/>') + sekil.replace('/>', f' class="{s}" stroke-width="1.5"/>')


def _uydu(x, y, renk, aci=0):
    ic = _iki('<rect x="-5" y="-4" width="10" height="8" rx="1.5"/>', renk)
    ic += _iki('<rect x="-16" y="-3" width="9" height="6"/>', renk)
    ic += _iki('<rect x="7" y="-3" width="9" height="6"/>', renk)
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({aci})">{ic}</g>'


def _roket(x, y, aci=0):
    ic = _iki('<polygon points="-9,-4 5,-4 9,0 5,4 -9,4"/>', 'turuncu')
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({aci})">{ic}</g>'


def _tank(x, y, aci=0):
    ic = _iki('<rect x="-8" y="-4.5" width="16" height="9" rx="4.5"/>', 'turuncu')
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({aci})">{ic}</g>'


def _parca(x, y, aci=0):
    ic = _iki('<polygon points="-6,4 0,-6 6,3"/>', 'turuncu')
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({aci})">{ic}</g>'


def model_adimlari():
    """Kitap s29, Uzay Gözlem Araçları Modeli: araç seçenekleri ve uygulama adımları."""
    ic = '<defs>' + ok_isareti('okFB72a', 'g-s') + '</defs>'
    ic += _yazi(236, 16, 'Model için bir araç seç', 12.5, 'g-s', kalin=True)
    secenek = [('Dürbün', 66), ('Teleskop', 78), ('Yapay uydu', 92), ('Ay’da gezici araç', 138)]
    x = (472 - sum(w for _, w in secenek) - 8 * 3) / 2
    for ad, w in secenek:
        ic += _gri(x, 24, w, 26, rx=13)
        ic += _yazi(x + w / 2, 41.5, ad, 12.5)
        x += w + 8
    adim = [('mavi', '1. Plan yap', 'plana göre çalış'),
            ('mavi', '2. Tasarımı çiz', 'özgün olsun'),
            ('turuncu', '3. Oluştur', 'basit, atık malzeme'),
            ('yesil', '4. Sun', 'arkadaşları dinle'),
            ('mor', '5. Karşılaştır', 'öteki modellerle'),
            ('mor', '6. Geliştir', 'kaynak araştır')]
    yer = [(6, 66), (166, 66), (326, 66), (326, 150), (166, 150), (6, 150)]
    for (renk, ad, alt), (x, y) in zip(adim, yer):
        f = RENK[renk][2]
        ic += _kutu(x, y, 140, 54, renk)
        ic += _yazi(x + 70, y + 23, ad, 13, f, kalin=True)
        ic += _yazi(x + 70, y + 41, alt, 12, f)
    ic += _ok(147, 93, 163, 93, 'okFB72a') + _ok(307, 93, 323, 93, 'okFB72a')
    ic += _ok(396, 121, 396, 147, 'okFB72a')
    ic += _ok(325, 177, 309, 177, 'okFB72a') + _ok(165, 177, 149, 177, 'okFB72a')
    ic += _yazi(236, 226, 'Değerlendirme: dereceli puanlama anahtarı · öz değerlendirme formu', 12, 'g-s')
    return svg(472, 236, ic, 'Uzay gözlem aracı modeli: dürbün, teleskop, yapay uydu ya da Ay’da gezici araç seçilir. '
               'Adımlar: 1. Plan yap, 2. Tasarımı çiz, 3. Basit ve atık malzemeyle oluştur, 4. Sun ve arkadaşlarını dinle, '
               '5. Öteki modellerle karşılaştır, 6. Kaynak araştırarak geliştir. Değerlendirme dereceli puanlama anahtarı '
               've öz değerlendirme formuyla yapılır.')


def uzay_copu():
    """Kitap s30: Dünya'nın çevresinde dolanan işlevsiz uydular, roket parçaları, yakıt tankları, sonda parçaları;
    Uzay Gözetim Ağı radar ve teleskoplarla izler, 130 milyondan fazla parça."""
    cx, cy, rx, ry = 140, 122, 122, 80
    ic = (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" class="g-c" stroke-width="1.5" '
          f'stroke-dasharray="5 5"/>')
    ic += f'<circle cx="{cx}" cy="{cy}" r="44" class="g-ma"/><circle cx="{cx}" cy="{cy}" r="44" class="g-ms" stroke-width="2"/>'
    ic += _yazi(cx, cy + 5, 'Dünya', 13, 'g-mf', kalin=True)

    def nokta(derece):
        t = math.radians(derece)
        return cx + rx * math.cos(t), cy + ry * math.sin(t)

    ic += _uydu(*nokta(-60), 'yesil', 15)
    ic += _uydu(*nokta(20), 'turuncu', 40)
    ic += _uydu(*nokta(160), 'turuncu', -25)
    ic += _roket(*nokta(-115), 30)
    ic += _roket(*nokta(95), -10)
    ic += _tank(*nokta(-165), 60)
    ic += _tank(*nokta(55), -30)
    ic += _parca(*nokta(-20), 20)
    ic += _parca(*nokta(130), 70)
    ic += _parca(*nokta(-140), -40)
    ic += _parca(*nokta(205), 15)

    sira = [(_uydu, 'yesil', 'Çalışan uydu'), (_uydu, 'turuncu', 'Görevi bitmiş uydu'),
            (_roket, None, 'Roket parçası'), (_tank, None, 'Yakıt tankı'), (_parca, None, 'Sonda parçası')]
    for k, (cizim, renk, ad) in enumerate(sira):
        y = 22 + k * 27
        ic += cizim(306, y, renk) if renk else cizim(306, y)
        ic += _yazi(328, y + 4.5, ad, 12.5, 'g-yf' if renk == 'yesil' else 'g-tf', kalin=True, hiza='start')
    ic += _gri(288, 156, 178, 82)
    ic += _yazi(377, 176, 'Uzay Gözetim Ağı', 12.5, kalin=True)
    ic += _yazi(377, 195, 'radar ve teleskopla izler', 12)
    ic += _yazi(377, 214, '130 milyondan fazla', 12)
    ic += _yazi(377, 230, 'parça dolaşıyor', 12)
    return svg(472, 246, ic, 'Uzay kirliliği: Dünya’nın çevresindeki yörüngede çalışan uydunun yanında görevi bitmiş '
               'uydular, roket parçaları, yakıt tankları ve sonda parçaları dolaşır. Uzay Gözetim Ağı bunları radar ve '
               'teleskopla izler; 130 milyondan fazla parça uzay çöpü olarak dolaşmaktadır.')


def sorunlar():
    """Kitap s32: işlevsiz parçalar + çok yüksek hız → küçük parça bile büyük zarar; önlem alınmazsa kirlilik artar,
    uzay araştırmaları, haberleşme, ulaşım ve ulusal güvenlik aksar."""
    ic = '<defs>' + ok_isareti('okFB72b', 'g-s') + '</defs>'
    ic += _kutu(6, 8, 222, 54, 'turuncu')
    ic += _yazi(117, 31, 'İşlevsiz parçalar', 13, 'g-tf', kalin=True)
    ic += _yazi(117, 49, 'Dünya’nın çevresinde kalır', 12, 'g-tf')
    ic += _kutu(244, 8, 222, 54, 'turuncu')
    ic += _yazi(355, 31, 'Çok yüksek hız', 13, 'g-tf', kalin=True)
    ic += _yazi(355, 49, 'parçalar çok hızlı dolanır', 12, 'g-tf')
    ic += _ok(117, 63, 190, 85, 'okFB72b') + _ok(355, 63, 282, 85, 'okFB72b')
    ic += _kutu(86, 88, 300, 54, 'mor')
    ic += _yazi(236, 111, 'Küçük parça bile büyük zarar', 13, 'g-of', kalin=True)
    ic += _yazi(236, 129, 'uyduya ya da uzay aracına çarpınca', 12, 'g-of')
    ic += _ok(236, 143, 236, 163, 'okFB72b')
    ic += _kutu(86, 166, 300, 38, 'mor')
    ic += _yazi(236, 190, 'Önlem alınmazsa kirlilik artar', 13, 'g-of', kalin=True)
    ic += _ok(236, 205, 236, 225, 'okFB72b')
    alan = [('Uzay araştırmaları', 138), ('Haberleşme', 98), ('Ulaşım', 68), ('Ulusal güvenlik', 118)]
    x = (472 - sum(w for _, w in alan) - 8 * 3) / 2
    for ad, w in alan:
        ic += _kutu(x, 228, w, 30, 'mavi', rx=15)
        ic += _yazi(x + w / 2, 247.5, ad, 12.5, 'g-mf', kalin=True)
        x += w + 8
    return svg(472, 266, ic, 'Uzay kirliliğinin sorunları: işlevsiz parçalar Dünya’nın çevresinde kalır ve çok yüksek '
               'hızla dolanır; bu yüzden küçük bir parça bile uyduya ya da uzay aracına çarpınca büyük zarar verir. '
               'Önlem alınmazsa kirlilik artar; uzay araştırmaları, haberleşme, ulaşım ve ulusal güvenlik aksayabilir.')


def alti_ayakkabi():
    """Kitap s31: altı ayakkabı tekniği; her ayakkabının rengi, türü ve temsil ettiği bakış açısı."""
    kart = [('#7b3fa0', 'Mor', 'binici çizmesi', 'yetki · güç'),
            ('#8a5a2b', 'Kahverengi', 'yürüyüş ayakkabısı', 'pratiklik · fayda'),
            ('#f19cbb', 'Pembe', 'ev terliği', 'sevgi · duyarlılık'),
            ('#f08a24', 'Turuncu', 'lastik çizme', 'tehlike · aciliyet'),
            ('#9aa0a6', 'Gri', 'spor ayakkabısı', 'sessiz araştırma'),
            ('#1f2f5c', 'Lacivert', 'resmî ayakkabı', 'rutin · kurallar')]
    ic = ''
    for k, (renk, ad, tur, anlam) in enumerate(kart):
        x, y = 6 + (k % 3) * 156, 8 + (k // 3) * 84
        ic += _gri(x, y, 148, 74)
        ic += (f'<circle cx="{x + 20}" cy="{y + 20}" r="9" fill="{renk}"/>'
               f'<circle cx="{x + 20}" cy="{y + 20}" r="9" fill="none" class="g-c" stroke-width="1.5"/>')
        ic += _yazi(x + 36, y + 25, ad, 13.5, kalin=True, hiza='start')
        ic += _yazi(x + 12, y + 46, tur, 12, 'g-s', hiza='start')
        ic += _yazi(x + 12, y + 64, anlam, 12.5, 'g-of', kalin=True, hiza='start')
    ic += _yazi(236, 190, 'Her öğrenci bir renk alır; çözümler raporda birleşir.', 12, 'g-s')
    return svg(472, 200, ic, 'Altı ayakkabı tekniği: mor binici çizmesi yetki ve güç, kahverengi yürüyüş ayakkabısı '
               'pratiklik ve fayda, pembe ev terliği sevgi ve duyarlılık, turuncu lastik çizme tehlike ve aciliyet, gri spor '
               'ayakkabısı sessiz araştırma, lacivert resmî ayakkabı rutin ve kurallar. Her öğrenci bir renk alır; '
               'çözümler raporda birleşir.')


def uygula(o):
    g = {'Model hazırlama adımları': model_adimlari(),
         'Uzay kirliliği nedir?': uzay_copu(),
         'Uzay kirliliğinin yol açabileceği sorunlar': sorunlar(),
         'Altı ayakkabı tekniğiyle problem çözmek': alti_ayakkabi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
