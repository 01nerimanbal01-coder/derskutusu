#!/usr/bin/env python3
"""Yeniden üretilmeyen sayfalara (çalışma kâğıtları, KPSS vb.) ana sayfanın üst menüsünü ve alt bilgi bağlantılarını,
sayfanın kitlesini (body data-kitle) ve öğrenci dalı konum çubuğunu uygular. Ana sayfa menüsü değişince çalıştırılır:
    python3 araclar/ust_guncelle.py
sayfa_uret.py / ozet_uret.py'nin ürettiği sayfalara da zararsızdır (aynı sonucu verir)."""
import re
from pathlib import Path
from sayfa_uret import kitle_bul, PUBLIC, BETIK_SURUMLERI, SURUM, AGAC_CSS, ADSENSE_HARIC, ADSENSE_UST_KOD
from kesif_sablonlari import CSS as KESIF_CSS, RENK_CSS

ana = (PUBLIC / 'index.html').read_text(encoding='utf-8')
MENU = re.search(r'<nav class="menu" id="ana-menu"[^>]*>.*?</nav>', ana, re.S).group(0)
ALT = re.search(r'<nav aria-label="Site">.*?</nav>', ana, re.S).group(0)
ALT = re.sub(r'href="#', 'href="/#', re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', ALT))
ALT_BILGI = re.search(r'<nav aria-label="Bilgi">.*?</nav>', ana, re.S).group(0)
ALT_BILGI = re.sub(r'href="#', 'href="/#', re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', ALT_BILGI))
ALT_SOSYAL = re.search(r'<div class="alt-sosyal">.*?</div>', ana, re.S).group(0)
SURUMLER = [('stil.css', SURUM), ('kpss.css', SURUM), ('arapca.css', SURUM), ('tahta.js', BETIK_SURUMLERI['tahta.js']), ('kutuphane.js', BETIK_SURUMLERI['kutuphane.js']), ('asds.js', BETIK_SURUMLERI['asds.js']),
            *((d, re.search(r'v=([\w-]+)', s).group(1)) for d, s in (('kesif.css', KESIF_CSS), ('renkler.css', RENK_CSS), ('agac.css', AGAC_CSS)))]
NPA_ETIKETI = re.compile(r'<script>\(window\.adsbygoogle=window\.adsbygoogle\|\|\[\]\)\.requestNonPersonalizedAds=1;</script>\n?')
REKLAM_ETIKETI = re.compile(r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=[\w-]+" crossorigin="anonymous"></script>\n?')
ADSENSE_META = '<meta name="google-adsense-account" content="ca-pub-6660544937586858">\n'
YOL = re.compile(r'<a href="/sinif\.html\?no=(\d+)">(\d+)\. sınıf</a><span aria-hidden="true">/</span><a href="/icerikler\.html\?sinif=(\d+)&amp;ders=([a-z-]+)">')


def guncelle(yol):
    ad = yol.relative_to(PUBLIC).as_posix()
    t = eski = yol.read_text(encoding='utf-8')
    t = re.sub(r'<nav class="menu" id="ana-menu"[^>]*>.*?</nav>', lambda m: MENU, t, count=1, flags=re.S)
    t = re.sub(r'<nav aria-label="Site">.*?</nav>', lambda m: ALT, t, count=1, flags=re.S)
    t = re.sub(r'<nav aria-label="Bilgi">.*?</nav>', lambda m: ALT_BILGI, t, count=1, flags=re.S)
    t = re.sub(r'<div class="alt-sosyal">.*?</div>', lambda m: ALT_SOSYAL, t, count=1, flags=re.S)
    t = YOL.sub(lambda m: (f'<a href="/ogrenci.html">Öğrenci</a><span aria-hidden="true">/</span><a href="/ogrenci.html?sinif={m[1]}">{m[2]}. sınıf</a>'
                           f'<span aria-hidden="true">/</span><a href="/ogrenci.html?sinif={m[3]}&amp;ders={m[4]}">'), t)
    k = kitle_bul(ad)
    if k and 'data-kitle=' not in t:
        t = re.sub(r'<body\b', f'<body data-kitle="{k}"', t, count=1)
    # 06.11.2026: Standart AdSense doğrulama ve Google sertifikalı TCF v2.2 CMP uyumu (araç/noindex sayfaları hariç)
    t = NPA_ETIKETI.sub('', t)
    t = REKLAM_ETIKETI.sub('', t)
    if ad not in ADSENSE_HARIC and 'content="noindex"' not in t:
        if ADSENSE_META in t:
            t = t.replace(ADSENSE_META, ADSENSE_META + ADSENSE_UST_KOD, 1)
        elif '</head>' in t:
            t = t.replace('</head>', ADSENSE_META + ADSENSE_UST_KOD + '</head>', 1)
    t = re.sub(r'(/?ortak\.js)\?v=[\w-]+', rf'\1?v={BETIK_SURUMLERI["ortak.js"]}', t)
    for dosya, surum in SURUMLER:   # ortak stil ve betik sürümleri tek yerden (sayfa_uret / kesif_sablonlari); önbellekteki eski kopya kalmaz
        t = re.sub(rf'(/?{re.escape(dosya)})\?v=[\w-]+', rf'\1?v={surum}', t)
    if t != eski:
        yol.write_text(t, encoding='utf-8')
        return 1
    return 0


if __name__ == '__main__':
    say = sum(guncelle(p) for p in PUBLIC.rglob('*.html') if p.name != 'index.html' and '<header class="ust">' in p.read_text(encoding='utf-8'))
    print(say, 'sayfa güncellendi')
