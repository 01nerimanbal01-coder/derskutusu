"""7. sınıf Din Kültürü ve Ahlak Bilgisi, 4. hafta: baastan cennet ve cehenneme ahiret aşamaları ve aralarındaki bağ.

Görseller yalnız MEB 7. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap s. 27-30).
Renk anlamı: mizan çiziminde yeşil = sevap ve mükâfat, turuncu = günah ve ceza; cennet adlarında yeşil = cennet;
bağlantı zincirinde mavi = ahiret yolunun aşamaları, yeşil = mükâfat yeri (cennet), turuncu = ceza yeri (cehennem).
Çizimlerde ölçü yoktur; terazideki ağır basan kefe aşağıda durur, başka bir büyüklük ilişkisi gösterilmez.
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


def _terazi(cx, agir, baslik, renk, sonuc):
    """İki kefeli terazi: agir='sol' ise sevap kefesi, 'sag' ise günah kefesi aşağıdadır (kitap s. 27)."""
    s = _kutu(cx - 100, 6, 200, 28, renk, 14) + _yazi(cx, 25, baslik, 13, True, RENK[renk][2])
    s += f'<line x1="{cx}" y1="76" x2="{cx}" y2="160" class="g-c" stroke-width="3" stroke-linecap="round"/>'
    s += f'<rect x="{cx - 26}" y="160" width="52" height="8" rx="4" class="g-s"/>'
    yl, yr = (93, 59) if agir == 'sol' else (59, 93)
    s += f'<line x1="{cx - 70}" y1="{yl}" x2="{cx + 70}" y2="{yr}" class="g-c" stroke-width="4" stroke-linecap="round"/>'
    s += f'<circle cx="{cx}" cy="76" r="5" class="g-s"/>'
    for x, yb, ad, r in ((cx - 70, yl, 'sevap', 'yesil'), (cx + 70, yr, 'günah', 'turuncu')):
        s += f'<line x1="{x}" y1="{yb}" x2="{x}" y2="{yb + 24}" class="g-c" stroke-width="2"/>'
        s += _kutu(x - 40, yb + 24, 80, 26, r, 8) + _yazi(x, yb + 42, ad, 12.5, True, RENK[r][2])
    s += _kutu(cx - 60, 180, 120, 32, renk) + _yazi(cx, 201, sonuc, 14, True, RENK[renk][2])
    return s


def mizan():
    """Mizanda ağır basan taraf sonucu belirler: sevap ağırsa mükâfat, günah ağırsa ceza (kitap s. 27)."""
    ic = _terazi(120, 'sol', 'Sevap ağır basarsa', 'yesil', 'Mükâfat')
    ic += _terazi(360, 'sag', 'Günah ağır basarsa', 'turuncu', 'Ceza')
    ic += _yazi(240, 232, 'Tartıda ağır basan taraf, sonucu belirler.', 12.5, True)
    return svg(480, 244, ic, 'Mizan, sevap ve günahların tartıldığı manevi adalet terazisidir. Birinci teraziyi sevap kefesi aşağıda gösterir: '
               'sevap ağır basarsa mükâfat vardır. İkinci teraziyi günah kefesi aşağıda gösterir: günah ağır basarsa ceza vardır.')


def cennet_adlari():
    """Cennet için Kur'an-ı Kerim'de geçen yedi ad (kitap s. 28)."""
    ic = _yazi(240, 24, 'Cennetin Kur’an-ı Kerim’de geçen adları', 14, True, 'g-yf')
    for k, ad in enumerate(['Adn', 'Naim', 'Firdevs', 'Meva']):
        x = 9 + k * 118
        ic += _kutu(x, 44, 108, 32, 'yesil', 16) + _yazi(x + 54, 65, ad, 13, True, 'g-yf')
    for k, ad in enumerate(['Hüsna', 'Darüsselam', 'Darülmukame']):
        x = 68 + k * 118
        ic += _kutu(x, 88, 108, 32, 'yesil', 16) + _yazi(x + 54, 109, ad, 13, True, 'g-yf')
    ic += _yazi(240, 148, 'Bu adların hepsi cenneti anlatır.', 12.5, True)
    return svg(480, 160, ic, 'Cennetin Kur’an-ı Kerim’de geçen yedi adı: Adn, Naim, Firdevs, Meva, Hüsna, Darüsselam ve Darülmukame.')


def baglanti_zinciri():
    """Aşamaların bağlantısı: ikinci sûr, diriliş, toplanma ve defterler, tartı, cennet ya da cehennem (kitap s. 27-29)."""
    ic = '<defs>' + ok_isareti('okDK74z', 'g-s') + '</defs>'
    kutu_y = {'Kıyamet': 12, 'Baas': 86, 'Mahşer': 160, 'Mizan': 234}
    for ad, y in kutu_y.items():
        ic += _kutu(24, y, 190, 38, 'mavi') + _yazi(119, y + 25, ad, 15, True, 'g-mf')
    etiket = ['İsrafil sûra ikinci kez üfler', 'Dirilenler bir araya gelir', 'Defterler verildikten sonra']
    for k, t in enumerate(etiket):
        ys = 12 + 74 * k + 42
        ic += f'<line x1="119" y1="{ys}" x2="119" y2="{ys + 26}" class="g-c" stroke-width="2" marker-end="url(#okDK74z)"/>'
        ic += _yazi(136, ys + 17, t, 12.5, False, 'g-y', 'start')
    ic += '<line x1="119" y1="276" x2="69" y2="298" class="g-c" stroke-width="2" marker-end="url(#okDK74z)"/>'
    ic += '<line x1="119" y1="276" x2="169" y2="298" class="g-c" stroke-width="2" marker-end="url(#okDK74z)"/>'
    ic += _yazi(196, 292, 'Hesap görüldükten sonra', 12.5, False, 'g-y', 'start')
    ic += _kutu(24, 304, 90, 38, 'yesil') + _yazi(69, 329, 'Cennet', 14, True, 'g-yf')
    ic += _kutu(124, 304, 90, 38, 'turuncu') + _yazi(169, 329, 'Cehennem', 14, True, 'g-tf')
    for k, (renk, t) in enumerate([('mavi', 'ahiret yolunun aşamaları'), ('yesil', 'mükâfat yeri'), ('turuncu', 'ceza yeri')]):
        y = 14 + k * 16
        ic += f'<circle cx="270" cy="{y - 4}" r="6" class="{RENK[renk][2]}"/>' + _yazi(282, y, t, 12, False, 'g-y', 'start')
    return svg(480, 352, ic, 'Ahiret aşamalarının bağlantısı: İsrafil sûra ikinci kez üfleyince kıyametten sonra baas gerçekleşir; '
               'dirilenler bir araya gelerek mahşerde toplanır; defterler verildikten sonra mizan kurulur; hesap görüldükten sonra '
               'insanlar cennete ya da cehenneme gider. Mavi aşamaları, yeşil mükâfat yeri olan cenneti, turuncu ceza yeri olan cehennemi gösterir.')


def uygula(o):
    g = {'Mizan: adalet terazisi': mizan(),
         'Cennet ve cehennem': cennet_adlari(),
         'Aşamalar birbirine nasıl bağlanır?': baglanti_zinciri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
