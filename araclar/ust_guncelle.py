#!/usr/bin/env python3
"""Yeniden üretilmeyen sayfalara (çalışma kâğıtları, KPSS vb.) ana sayfanın üst menüsünü ve alt bilgi bağlantılarını,
sayfanın kitlesini (body data-kitle) ve öğrenci dalı konum çubuğunu uygular. Ana sayfa menüsü değişince çalıştırılır:
    python3 araclar/ust_guncelle.py
sayfa_uret.py / ozet_uret.py'nin ürettiği sayfalara da zararsızdır (aynı sonucu verir)."""
import re
from pathlib import Path
from sayfa_uret import kitle_bul, kisalt, PUBLIC, BETIK_SURUMLERI, SURUM, AGAC_CSS
from kesif_sablonlari import CSS as KESIF_CSS, RENK_CSS

ana = (PUBLIC / 'index.html').read_text(encoding='utf-8')
MENU = re.search(r'<nav class="menu" id="ana-menu"[^>]*>.*?</nav>', ana, re.S).group(0)
ALT = re.search(r'<nav aria-label="Site">.*?</nav>', ana, re.S).group(0)
ALT = re.sub(r'href="#', 'href="/#', re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', ALT))
SURUMLER = [('stil.css', SURUM), ('tahta.js', BETIK_SURUMLERI['tahta.js']), ('kutuphane.js', BETIK_SURUMLERI['kutuphane.js']),
            *((d, re.search(r'v=([\w-]+)', s).group(1)) for d, s in (('kesif.css', KESIF_CSS), ('renkler.css', RENK_CSS), ('agac.css', AGAC_CSS)))]
YOL = re.compile(r'<a href="/sinif\.html\?no=(\d+)">(\d+)\. sınıf</a><span aria-hidden="true">/</span><a href="/icerikler\.html\?sinif=(\d+)&amp;ders=([a-z-]+)">')


def guncelle(yol):
    ad = yol.relative_to(PUBLIC).as_posix()
    t = eski = yol.read_text(encoding='utf-8')
    t = re.sub(r'<nav class="menu" id="ana-menu"[^>]*>.*?</nav>', lambda m: MENU, t, count=1, flags=re.S)
    t = re.sub(r'<nav aria-label="Site">.*?</nav>', lambda m: ALT, t, count=1, flags=re.S)
    t = YOL.sub(lambda m: (f'<a href="/ogrenci.html">Öğrenci</a><span aria-hidden="true">/</span><a href="/ogrenci.html?sinif={m[1]}">{m[2]}. sınıf</a>'
                           f'<span aria-hidden="true">/</span><a href="/ogrenci.html?sinif={m[3]}&amp;ders={m[4]}">'), t)
    k = kitle_bul(ad)
    if k and 'data-kitle=' not in t:
        t = re.sub(r'<body\b', f'<body data-kitle="{k}"', t, count=1)
    t = re.sub(r'(/?ortak\.js)\?v=[\w-]+', rf'\1?v={BETIK_SURUMLERI["ortak.js"]}', t)
    for dosya, surum in SURUMLER:   # ortak stil ve betik sürümleri tek yerden (sayfa_uret / kesif_sablonlari); önbellekteki eski kopya kalmaz
        t = re.sub(rf'(/?{re.escape(dosya)})\?v=[\w-]+', rf'\1?v={surum}', t)
    # <head> sayfa_uret şablonuyla aynı olsun: description ≤160, manifest, og:type/locale/url, og:image boyutları, twitter:card
    t = re.sub(r'(<meta (?:name="description"|property="og:description") content=")([^"]*)(")', lambda m: m[1] + kisalt(m[2]) + m[3], t)
    if '<link rel="manifest"' not in t:
        t = t.replace('<link rel="apple-touch-icon" href="/apple-touch-icon.png">', '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<link rel="manifest" href="/site.webmanifest">', 1)
    if '<meta property="og:type"' not in t:
        t = t.replace('<meta property="og:site_name" content="Ders Kutusu">', '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Ders Kutusu">\n<meta property="og:locale" content="tr_TR">', 1)
    kan = re.search(r'<link rel="canonical" href="([^"]+)">', t)
    if kan and '<meta property="og:url"' not in t:
        t = t.replace('<meta property="og:title"', f'<meta property="og:url" content="{kan[1]}">\n<meta property="og:title"', 1)
    if '<meta property="og:image:width"' not in t:
        t = t.replace('<meta property="og:image" content="https://derskutusu.com/paylasim.png">',
                      '<meta property="og:image" content="https://derskutusu.com/paylasim.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">', 1)
    if t != eski:
        yol.write_text(t, encoding='utf-8')
        return 1
    return 0


if __name__ == '__main__':
    say = sum(guncelle(p) for p in PUBLIC.rglob('*.html') if p.name != 'index.html' and '<header class="ust">' in p.read_text(encoding='utf-8'))
    print(say, 'sayfa güncellendi')
