"""8. sınıf Türkçe, 3. hafta: Gezici Kütüphaneler (hizmet ve donanım, ülke ve taşıt), benzetme, fiilimsi türleri.

Görseller yalnız MEB 8. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s22-s27); metin cümleleri görsele alınmaz,
fiilimsi örnekleri kurgusaldır ve özet metnindeki cümlelerle aynıdır.
Renk anlamı:
- Gezici kütüphanede neler var: mavi = hizmetler, turuncu = aracın donanımı, yeşil = kitap koleksiyonu, mor = görevli personel.
- Ülke ve taşıt: mavi = dünyadan örnekler, turuncu = Türkiye'den örnekler.
- Benzetme: mavi = anlatılan şey, turuncu = benzetilen şey, yeşil = "gibi" sözcüğü, mor = "çünkü" ile başlayan gerekçe.
- Fiilimsi türleri: turuncu = isim-fiil, mavi = sıfat-fiil, yeşil = zarf-fiil, gri = çekimli fiil.
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


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _cip(x, y, w, h, metin, renk, boyut=12):
    """Beyaz zeminli, renkli çerçeveli küçük kutu; yazı ortada."""
    s = RENK[renk][1]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{s}" stroke-width="1.6"/>'
            + _yazi(x + w / 2, y + h / 2 + 4.3, metin, boyut, 'g-y', False, 'middle'))


def hizmet_donanim():
    """Gezici kütüphanede hizmetler, donanım, kitap koleksiyonu ve görevli personel (s23)."""
    ic = ''
    # hizmetler (sol üst)
    ic += _kutu(8, 8, 222, 196, 'mavi')
    ic += _yazi(119, 30, 'Okura sunulan hizmetler', 13, 'g-mf', True, 'middle')
    for k, t in enumerate(['İnternet erişimi', 'Ödünç verme', 'Film gösterimi', 'Eğitici oyuncaklar', 'Süreli yayınlar']):
        ic += _cip(20, 42 + k * 32, 198, 26, t, 'mavi')
    # görevli personel (sol alt)
    ic += _kutu(8, 212, 222, 44, 'mor')
    ic += _yazi(119, 239, 'Görevli kütüphaneci personel', 12.5, 'g-of', True, 'middle')
    # donanım (sağ)
    ic += _kutu(242, 8, 222, 248, 'turuncu')
    ic += _yazi(353, 30, 'Aracın donanımı', 13, 'g-tf', True, 'middle')
    for k, t in enumerate(['Masaüstü bilgisayar', 'Dizüstü bilgisayar', 'Yazıcı', 'LCD TV', 'DVD oynatıcı', 'Projeksiyon cihazı', 'Oturma grubu']):
        ic += _cip(254, 42 + k * 30, 198, 24, t, 'turuncu')
    # koleksiyon (alt)
    ic += _kutu(8, 264, 456, 62, 'yesil')
    ic += _yazi(236, 288, 'Kitap koleksiyonu: ortalama 2 binden fazla kitap', 13.5, 'g-yf', True, 'middle')
    ic += _yazi(236, 309, 'Her kesime uygun · güncel · belirli aralıklarla değişir', 12, 'g-y', False, 'middle')
    return svg(472, 334, ic, 'Gezici kütüphanede neler var: mavi kutuda okura sunulan hizmetler, yani internet erişimi, ödünç verme, film gösterimi, eğitici oyuncaklar ve süreli yayınlar. '
               'Turuncu kutuda aracın donanımı, yani masaüstü bilgisayar, dizüstü bilgisayar, yazıcı, LCD TV, DVD oynatıcı, projeksiyon cihazı ve oturma grubu. '
               'Mor kutuda görevli kütüphaneci personel. Yeşil kutuda iki binden fazla, her kesime uygun, güncel ve belirli aralıklarla değişen kitap koleksiyonu.')


def ulke_tasit():
    """Gezici kütüphane hizmetinde ülkelere göre taşıtlar; Türkiye'de yük hayvanları, sonra minibüs ve otobüs (s23)."""
    ic = '<defs>' + ok_isareti('okT3s', 'g-s') + '</defs>'

    def baslik(y, renk, metin):
        _, _, f = RENK[renk]
        return (f'<rect x="8" y="{y}" width="456" height="26" rx="13" class="{f}"/>'
                + _yazi(236, y + 18, metin, 13, 'g-b', True, 'middle'))

    def satir(y, renk, sol, sag):
        s = _kutu(8, y, 170, 32, renk, rx=10) + _yazi(20, y + 21, sol, 12.5, 'g-y', True)
        s += f'<line x1="184" y1="{y + 16}" x2="210" y2="{y + 16}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT3s)"/>'
        s += _kutu(218, y, 246, 32, renk, rx=10) + _yazi(230, y + 21, sag, 12.5, 'g-y')
        return s

    ic += baslik(8, 'mavi', 'Dünyada')
    for k, (u, t) in enumerate([('İsveç', 'Gemi'), ('Fransa', 'Tren'), ('Norveç', 'Deniz ve karayolu taşıtları'), ('Sovyetler', 'Posta yolu')]):
        ic += satir(42 + k * 38, 'mavi', u, t)
    ic += baslik(198, 'turuncu', 'Türkiye’de')
    ic += satir(232, 'turuncu', '1960’lı yıllar', 'Yük hayvanları (merkep)')
    ic += satir(270, 'turuncu', '1963’ten sonra', 'Minibüs, otobüs gibi araçlar')
    return svg(472, 310, ic, 'Gezici kütüphane hizmetinde kullanılan taşıtlar. Dünyada: İsveç’te gemi, Fransa’da tren, Norveç’te deniz ve karayolu taşıtları, Sovyetler’de posta yolu. '
               'Türkiye’de: 1960’lı yıllarda Ürgüp’te yük hayvanları, yani merkep; 1963’ten sonraki yıllarda minibüs ve otobüs gibi araçlar.')


def benzetme():
    """Benzetme: anlatılan şey, benzetilen şey, 'gibi' sözcüğü ve 'çünkü' ile başlayan gerekçe (s25)."""
    ic = ''
    ic += _yazi(93, 20, 'Neyi anlatıyoruz?', 12, 'g-s', False, 'middle')
    ic += _yazi(379, 20, 'Neye benzetiyoruz?', 12, 'g-s', False, 'middle')
    for k, (sol, sag) in enumerate([('Kütüphane', 'Hazine sandığı'), ('Kitaplar', 'Anahtar')]):
        y = 30 + k * 52
        ic += _kutu(8, y, 170, 40, 'mavi') + _yazi(93, y + 25.5, sol, 14, 'g-mf', True, 'middle')
        ic += f'<rect x="206" y="{y + 8}" width="60" height="24" rx="12" class="g-yf"/>' + _yazi(236, y + 24.3, 'gibi', 13, 'g-b', True, 'middle')
        ic += _kutu(294, y, 170, 40, 'turuncu') + _yazi(379, y + 25.5, sag, 14, 'g-tf', True, 'middle')
    ic += _kutu(8, 138, 456, 52, 'mor')
    ic += _yazi(236, 160, 'Çünkü …', 14, 'g-of', True, 'middle')
    ic += _yazi(236, 179, 'Bu bölüm, iki şey arasındaki ortak özelliği açıklar.', 12, 'g-y', False, 'middle')
    return svg(472, 200, ic, 'Benzetme şeması: mavi kutuda anlatılan şeyler, turuncu kutuda benzetilen şeyler vardır; aradaki yeşil gibi sözcüğü benzetmeyi kurar. '
               'Kütüphane hazine sandığına, kitaplar anahtara benzetilmiştir. Mor kutuda çünkü ile başlayan bölüm, iki şey arasındaki ortak özelliği açıklar.')


def fiilimsi_turleri():
    """Fiilimsi türleri ve çekimli fiil; örnek cümleler kurgusaldır (s27)."""
    satirlar = [
        ('turuncu', 'İsim-fiil', 'İşin adını bildirir', [('Kitap ', 0), ('seçmek', 1), (' eğlencelidir.', 0)]),
        ('mavi', 'Sıfat-fiil', 'Bir ismi niteler', [('', 0), ('Seçilen', 1), (' kitap masada.', 0)]),
        ('yesil', 'Zarf-fiil', 'Eylemi niteler: nasıl, ne zaman, niçin', [('Kitabı ', 0), ('seçerek', 1), (' kasaya gitti.', 0)]),
    ]
    ic = ''
    for k, (renk, ad, gorev, parcalar) in enumerate(satirlar):
        y = 8 + k * 70
        _, _, f = RENK[renk]
        ic += _kutu(8, y, 456, 62, renk)
        ic += f'<rect x="16" y="{y + 8}" width="96" height="46" rx="10" class="{f}"/>'
        ic += _yazi(64, y + 36, ad, 13.5, 'g-b', True, 'middle')
        ic += _yazi(124, y + 26, gorev, 12.5, f, True)
        cumle = ''.join((f'<tspan font-weight="800" class="{f}">{m}</tspan>' if v else f'<tspan>{m}</tspan>') for m, v in parcalar)
        ic += f'<text x="124" y="{y + 48}" font-size="13" class="g-y">{cumle}</text>'
    y = 218
    ic += f'<rect x="8" y="{y}" width="456" height="62" rx="12" class="g-z"/><rect x="8" y="{y}" width="456" height="62" rx="12" class="g-c" stroke-width="2"/>'
    ic += f'<rect x="16" y="{y + 8}" width="96" height="46" rx="10" class="g-s"/>'
    ic += _yazi(64, y + 36, 'Çekimli fiil', 11.5, 'g-b', True, 'middle')
    ic += _yazi(124, y + 26, 'Kip ve kişi eki alır; fiilimsi sayılmaz', 12.5, 'g-y', True)
    ic += _yazi(124, y + 48, 'Örnek: gitti, girdi', 13, 'g-y')
    return svg(472, 288, ic, 'Fiilimsi türleri: turuncu satırda isim-fiil işin adını bildirir, örnek seçmek. Mavi satırda sıfat-fiil bir ismi niteler, örnek seçilen. '
               'Yeşil satırda zarf-fiil eylemi niteler, yani nasıl, ne zaman ve niçin yapıldığını bildirir, örnek seçerek. Gri satırda çekimli fiil kip ve kişi eki alır ve fiilimsi sayılmaz, örnek gitti ve girdi.')


def uygula(o):
    g = {'Gezici kütüphanede neler var?': hizmet_donanim(),
         'Gezici kütüphane dünyada ve ülkemizde': ulke_tasit(),
         'Benzetme ve bilgilendirici metin': benzetme(),
         'Fiilimsi türlerini ayır': fiilimsi_turleri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
