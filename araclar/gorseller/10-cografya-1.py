"""10. sınıf Coğrafya, 1. hafta: Coğrafi Bakış (COĞ.10.1.1).

Görseller yalnız MEB 10. sınıf Coğrafya ders kitabındaki bilgilerle çizilir (PDF s. 16, 18-22; kitap sayfası 15, 17-21).
Renk anlamı: mor = coğrafi bakış / mekân okuryazarlığı, mavi = soru ve yer, yeşil = ölçek (boyut) ve çözüm,
turuncu = bileşenler / olay; grafikte turuncu = önceki ölçüme göre küçüldü, yeşil = büyüdü, mavi = ilk ölçüm.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu/yazı)
    'mor': ('g-oa', 'g-os', 'g-of'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _bin(n):
    """Binlik ayırıcı nokta (TDK): 5949 → 5.949."""
    return f'{n:,}'.replace(',', '.')


def cografi_bakis_haritasi():
    """Coğrafi bakış: üç soru, üç boyut, beş bileşen → mekân okuryazarlığı (kitap s. 17)."""
    ic = '<defs>' + ok_isareti('okC10a', 'g-of') + '</defs>'
    ic += _kutu(146, 8, 180, 38, 'mor', rx=19)
    ic += '<text x="236" y="32" text-anchor="middle" font-size="14.5" font-weight="800" class="g-of">COĞRAFİ BAKIŞ</text>'
    ic += '<line x1="190" y1="49" x2="124" y2="61" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    ic += '<line x1="282" y1="49" x2="348" y2="61" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    # sol üst: üç temel soru (mavi)
    ic += _kutu(12, 64, 216, 106, 'mavi')
    ic += '<text x="120" y="88" text-anchor="middle" font-size="13.5" font-weight="800" class="g-mf">Üç temel soru</text>'
    for k, s in enumerate(('Nerede?', 'Neden orada?', 'Nasıl?')):
        yy = 113 + k * 22
        ic += f'<circle cx="34" cy="{yy - 4.5}" r="4" class="g-mf"/><text x="46" y="{yy}" font-size="13" font-weight="700" class="g-y">{s}</text>'
    # sol alt: üç boyut (yeşil)
    ic += _kutu(12, 182, 216, 72, 'yesil')
    ic += '<text x="120" y="204" text-anchor="middle" font-size="13.5" font-weight="800" class="g-yf">Üç boyut</text>'
    for x, w, s in ((20, 54, 'Yerel'), (80, 70, 'Bölgesel'), (156, 64, 'Küresel')):
        ic += f'<rect x="{x}" y="217" width="{w}" height="26" rx="13" class="g-yf"/>'
        ic += f'<text x="{x + w / 2:g}" y="234.5" text-anchor="middle" font-size="12" font-weight="700" class="g-b">{s}</text>'
    # sağ: beş bileşen (turuncu)
    ic += _kutu(244, 64, 216, 190, 'turuncu')
    ic += '<text x="352" y="88" text-anchor="middle" font-size="13.5" font-weight="800" class="g-tf">Bileşenleri</text>'
    for k, s in enumerate(('Mekânsal düşünme', 'Ölçek bilinci', 'Yer ve mekân algısı',
                           'İnsan-çevre etkileşimi', 'Coğrafi bağlantılar')):
        yy = 116 + k * 28
        ic += f'<circle cx="266" cy="{yy - 4.5}" r="4" class="g-tf"/><text x="278" y="{yy}" font-size="12.5" class="g-y">{s}</text>'
    # bileşenler → mekân okuryazarlığı
    ic += '<line x1="352" y1="258" x2="352" y2="270" class="g-os" stroke-width="2" marker-end="url(#okC10a)"/>'
    ic += '<rect x="244" y="278" width="216" height="40" rx="20" class="g-of"/>'
    ic += '<text x="352" y="303" text-anchor="middle" font-size="13.5" font-weight="800" class="g-b">Mekân okuryazarlığı</text>'
    # sol alt not: mekân anlayışı
    ic += _kutu(12, 270, 216, 48, 'mor')
    ic += '<text x="120" y="290" text-anchor="middle" font-size="12" class="g-y"><tspan font-weight="800" class="g-of">Mekân:</tspan> ilişkiler, süreçler</text>'
    ic += '<text x="120" y="308" text-anchor="middle" font-size="12" class="g-y">ve örüntüler bütünü</text>'
    return svg(472, 328, ic, 'Coğrafi bakış kavram haritası. Üç temel soru: Nerede? Neden orada? Nasıl? Üç boyut: yerel, bölgesel, küresel. Bileşenleri: mekânsal düşünme, ölçek bilinci, yer ve mekân algısı, insan-çevre etkileşimi, coğrafi bağlantılar; bu bileşenler mekân okuryazarlığının temelidir. Mekân: ilişkiler, süreçler ve örüntüler bütünü.')


def soho_akisi():
    """Soho kolera salgını (1854): coğrafi bakışın soruları sırayla (kitap s. 17)."""
    ic = '<defs>' + ok_isareti('okC10b', 'g-s') + '</defs>'
    adim = [('Ne oldu?', 'turuncu', ('Bir kolera salgını 1854’te', 'can kayıplarına yol açtı.')),
            ('Nerede?', 'mavi', ('Londra’nın Soho bölgesinde kayıpların', 'yaşandığı alanlar sahada incelendi.')),
            ('Neden orada?', 'mor', ('İçme suyu kuyularındaki mikroorganizmalar', 'salgının en önemli nedeni olabilirdi.')),
            ('Nasıl önlendi?', 'yesil', ('Hastalığı bulaştıran kuyunun kullanımı', 'durduruldu; salgının yayılması önlendi.'))]
    for i, (soru, renk, satir) in enumerate(adim):
        y0 = 10 + i * 70
        _, _, f = RENK[renk]
        ic += f'<rect x="10" y="{y0}" width="124" height="48" rx="24" class="{f}"/>'
        ic += f'<text x="72" y="{y0 + 29}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{soru}</text>'
        ic += _kutu(142, y0, 320, 48, renk)
        for k, t in enumerate(satir):
            ic += f'<text x="155" y="{y0 + 20 + k * 17}" font-size="12.5" class="g-y">{t}</text>'
        if i < len(adim) - 1:
            ic += f'<line x1="72" y1="{y0 + 51}" x2="72" y2="{y0 + 64}" class="g-c" stroke-width="2" marker-end="url(#okC10b)"/>'
    ic += ('<text x="236" y="300" text-anchor="middle" font-size="12.5" class="g-y">'
           'Bu yaklaşım <tspan font-weight="800">coğrafi bakışın önemini</tspan> gösterir.</text>')
    return svg(472, 312, ic, 'Soho kolera salgını akışı. Ne oldu: Bir kolera salgını 1854’te can kayıplarına yol açtı. Nerede: Londra’nın Soho bölgesi; kayıpların yaşandığı alanlar sahada incelendi. Neden orada: İçme suyu kuyularındaki mikroorganizmalar salgının en önemli nedeni olabilirdi. Nasıl önlendi: Hastalığı bulaştıran kuyunun kullanımı durduruldu; salgının yayılması önlendi.')


def gol_alani_grafigi():
    """Marmara Gölü alanı 1975-2018 (hektar) ve 2022'de tamamen kuruma (kitap s. 20-21, Tablo 1)."""
    veri = [(1975, 5949), (1986, 5168), (1995, 4731), (2002, 5300), (2011, 5580), (2018, 3464)]
    x0, x1, taban, ust = 60, 462, 214, 44
    olcek = (taban - ust) / 6000
    ic = '<text x="14" y="18" font-size="12.5" font-weight="800" class="g-y">Göl alanı (hektar)</text>'
    for d in (0, 2000, 4000, 6000):
        y = taban - d * olcek
        cizgi = 'stroke-width="1.5"' if d == 0 else 'stroke-width="1" stroke-dasharray="3 4"'
        ic += f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" class="g-c" {cizgi}/>'
        ic += f'<text x="{x0 - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11.5" class="g-s">{_bin(d)}</text>'
    yuva = (x1 - x0) / 7
    onceki = None
    for i, (yil, alan) in enumerate(veri):
        cx = x0 + yuva * (i + 0.5)
        h = alan * olcek
        if onceki is None:
            f = RENK['mavi'][2]
            degisim = ''
        elif alan < onceki:
            f = RENK['turuncu'][2]
            degisim = '−' + _bin(onceki - alan)
        else:
            f = RENK['yesil'][2]
            degisim = '+' + _bin(alan - onceki)
        # değer çubuğun içinde yazılır: kılavuz çizgileri yazıya değmez
        ic += f'<rect x="{cx - 22:.1f}" y="{taban - h:.1f}" width="44" height="{h:.1f}" rx="5" class="{f}"/>'
        ic += f'<text x="{cx:.1f}" y="{taban - h + 18:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" class="g-b">{_bin(alan)}</text>'
        ic += f'<text x="{cx:.1f}" y="232" text-anchor="middle" font-size="12" font-weight="800" class="g-y">{yil}</text>'
        if degisim:
            ic += f'<text x="{cx:.1f}" y="250" text-anchor="middle" font-size="11.5" font-weight="800" class="{f}">{degisim}</text>'
        onceki = alan
    # 2022: göl tamamen kurudu (kitap s. 21); kitapta alan ölçümü yok, çubuk çizilmez
    cx = x0 + yuva * 6.5
    ic += f'<text x="{cx:.1f}" y="{taban - 24}" text-anchor="middle" font-size="11.5" font-weight="800" class="g-tf">tamamen</text>'
    ic += f'<text x="{cx:.1f}" y="{taban - 8}" text-anchor="middle" font-size="11.5" font-weight="800" class="g-tf">kurudu</text>'
    ic += f'<text x="{cx:.1f}" y="232" text-anchor="middle" font-size="12" font-weight="800" class="g-y">2022</text>'
    # renk açıklaması
    for x, sinif, ad in ((96, 'g-mf', 'ilk ölçüm'), (196, 'g-tf', 'önceki ölçüme göre küçüldü'), (386, 'g-yf', 'büyüdü')):
        ic += f'<rect x="{x}" y="263" width="11" height="11" rx="2" class="{sinif}"/><text x="{x + 16}" y="273" font-size="11.5" class="g-y">{ad}</text>'
    return svg(472, 284, ic, 'Marmara Gölü alanı: 1975’te 5.949, 1986’da 5.168, 1995’te 4.731, 2002’de 5.300, 2011’de 5.580, 2018’de 3.464 hektar; göl 2022’de tamamen kurudu. Göl 1975-1995 arasında küçüldü, 1995-2011 arasında büyüdü, 2011-2018 arasında 2.116 hektar küçüldü.')


def uygula(o):
    g = {'Coğrafi bakış nedir?': cografi_bakis_haritasi(),
         'Örnek olay: Soho’da kolera salgını': soho_akisi(),
         'Gölde yaşanan değişim ve etkileri': gol_alani_grafigi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
