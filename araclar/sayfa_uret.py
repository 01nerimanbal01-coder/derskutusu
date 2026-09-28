#!/usr/bin/env python3
"""İç sayfaları (sinif.html, icerikler.html, gizlilik.html, 404.html) ana sayfanın üst ve alt bölümüyle üretir.

Ana sayfadaki simge takımı, üst menü ve alt bilgi değişince bu betik yeniden çalıştırılır:
    python3 araclar/sayfa_uret.py
Sayfaların kendi gövdeleri aşağıdaki GOVDE sözlüğündedir.
"""
import re
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / 'public'
ana = (PUBLIC / 'index.html').read_text(encoding='utf-8')
SURUM = re.search(r'stil\.css\?v=(\d+)', ana).group(1)

simgeler = ana[ana.index('<!-- Simge takımı'):ana.index('</svg>\n\n<header') + len('</svg>')]
ust = ana[ana.index('<header class="ust">'):ana.index('</header>') + len('</header>')]
alt = ana[ana.index('<footer class="alt">'):ana.index('</footer>') + len('</footer>')]
# İç sayfalarda bölüm bağlantıları ana sayfaya gider
ust = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'href="#', 'href="/#', ust))
alt = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'href="#', 'href="/#', alt))


def sayfa(ad, baslik, aciklama, govde, betikler=(), kanonik=True):
    kan = f'<link rel="canonical" href="https://derskutusu.com/{ad}">\n' if kanonik else '<meta name="robots" content="noindex">\n'
    js = ''.join(f'<script src="/{b}?v={SURUM}"></script>\n' for b in ('ortak.js', *betikler, 'arama.js'))
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{baslik} · Ders Kutusu</title>
<meta name="description" content="{aciklama}">
{kan}<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#2451d6">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:site_name" content="Ders Kutusu">
<meta property="og:title" content="{baslik} · Ders Kutusu">
<meta property="og:description" content="{aciklama}">
<meta property="og:image" content="https://derskutusu.com/paylasim.png">
<link rel="stylesheet" href="/stil.css?v={SURUM}">
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>

{simgeler}

{ust}

<main id="icerik">
{govde}
</main>

{alt}

{js}</body>
</html>
'''


YAKINDA = '''      <div class="yakinda" id="icerik-yakinda" hidden>
        <div class="yakinda-simge" aria-hidden="true"><svg><use href="#s-kitap"/></svg></div>
        <div>
          <h3>Bu seçimde henüz içerik yok</h3>
          <p>İçerikler eklendikçe burada listelenecek. Yeni içeriklerden haberdar olmak için bizi takip edin.</p>
        </div>
        <a class="dugme ana" data-sosyal="youtube" target="_blank" rel="noopener" hidden><svg><use href="#s-youtube"/></svg>Abone ol</a>
      </div>'''

GOVDE = {
    'sinif.html': ('Sınıf', '5-12. sınıf dersleri için konu anlatımları, soru çözümleri ve öğretmen dosyaları.', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/#siniflar">Sınıflar</a><span aria-hidden="true">/</span><span id="yol-sinif"></span></nav>
      <h1 id="baslik">Sınıf</h1>
      <p id="aciklama"></p>
      <nav class="sinif-gecis" id="sinif-gecis" aria-label="Sınıflar"></nav>
    </div>
  </section>
  <section class="bolum">
    <div class="kap">
      <div class="bolum-bas">
        <div><p class="ust-baslik">Dersler</p><h2>Dersini seç</h2></div>
        <a class="tumu" id="tum-icerik" href="/icerikler.html">Bu sınıfın bütün içerikleri<svg><use href="#s-ok"/></svg></a>
      </div>
      <div class="ders-izgara" id="ders-listesi"></div>
    </div>
  </section>
  <section class="bolum koyu-zemin" id="secmeli-bolum" hidden>
    <div class="kap">
      <div class="bolum-bas">
        <div><p class="ust-baslik">Seçmeli dersler</p><h2>Seçmeli ve imam hatip dersleri</h2></div>
      </div>
      <div class="ders-izgara" id="secmeli-listesi"></div>
    </div>
  </section>''', ('kutuphane.js',)),
    'icerikler.html': ('İçerikler', 'Sınıfa, derse ve türe göre konu anlatımları, soru çözümleri, videolar, yıllık planlar ve yazılı soruları.', f'''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>İçerikler</span></nav>
      <h1>İçerikler</h1>
      <p>Sınıfa, derse ve türe göre arayın: konu anlatımları, soru çözümleri, videolar; öğretmenler için yıllık planlar, yazılı soruları ve çalışma kâğıtları.</p>
    </div>
  </section>
  <section class="bolum">
    <div class="kap">
      <form class="suzgec-cubugu" role="search" onsubmit="return false">
        <label>Sınıf<select id="s-sinif"><option value="">Bütün sınıflar</option></select></label>
        <label>Ders<select id="s-ders"></select></label>
        <label>Kimin için<select id="s-kitle"><option value="">Herkes</option><option value="ogrenci">Öğrenci</option><option value="ogretmen">Öğretmen</option></select></label>
        <label>Tür<select id="s-tur"></select></label>
        <label class="arama">Ara<input id="s-ara" type="search" placeholder="Konu, başlık…" autocomplete="off"></label>
      </form>
      <p class="sonuc-bilgi"><span id="sonuc-sayi"></span><button type="button" id="temizle" hidden>Seçimleri temizle</button></p>
      <div class="kartlar" id="kartlar"></div>
{YAKINDA}
    </div>
  </section>''', ('kutuphane.js',)),
    'belgeler.html': ('Resmî belgeler', 'MEB, ÖDSGM, DÖGM ve ÖSYM resmî belgeleri: öğretim programları, kılavuzlar, ortak yazılı tabloları, LGS ve YKS.', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Resmî belgeler</span></nav>
      <h1>Resmî belgeler</h1>
      <p>MEB, ÖDSGM, DÖGM ve ÖSYM’nin yayımladığı belgeler tek yerde. Bağlantılar doğrudan resmî kaynaklara gider; dosyalar her zaman güncel sürümüyle açılır.</p>
      <nav class="sinif-gecis" id="grup-gecis" aria-label="Belge grupları"></nav>
    </div>
  </section>
  <div id="belge-gruplari"></div>''', ('belgeler.js',)),
    'ara.html': ('Arama', 'Ders Kutusu içinde akıllı arama: sınıf, ders, plan, öğretim programı ve resmî belgeler.', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Arama</span></nav>
      <h1>Arama</h1>
      <p>Yazdığınızı anlar: sınıfı, dersi ve aradığınız türü kendisi bulur; yazım hatalarını düzeltir.</p>
      <form class="arama-buyuk" id="arama-form" role="search">
        <svg aria-hidden="true"><use href="#s-mercek"/></svg>
        <input id="arama-kutu" type="search" name="q" placeholder="Ör. 8. sınıf matematik yıllık plan" aria-label="Sitede ara" autocomplete="off" spellcheck="false" enterkeyhint="search">
        <button class="dugme ana" type="submit">Ara</button>
      </form>
      <div class="anlasilan" id="anlasilan"></div>
      <div class="arama-not" id="arama-not" aria-live="polite"></div>
    </div>
  </section>
  <section class="bolum">
    <div class="kap">
      <p class="sonuc-bilgi"><span id="arama-sayi" aria-live="polite"></span></p>
      <div class="kartlar" id="arama-sonuclari"></div>
      <p class="orta"><button class="dugme" id="daha-fazla" type="button" hidden>Daha fazla göster</button></p>
      <div class="yakinda" id="arama-bos" hidden>
        <div class="yakinda-simge" aria-hidden="true"><svg><use href="#s-mercek"/></svg></div>
        <div>
          <h3>Ne aramak istersiniz?</h3>
          <p>Sınıf, ders ve tür yazmanız yeterli. Örnekler:</p>
          <div class="ornekler">
            <a href="?q=8.+sınıf+matematik+yıllık+plan" data-ornek="8. sınıf matematik yıllık plan">8. sınıf matematik yıllık plan</a>
            <a href="?q=5+fen+günlük+plan" data-ornek="5 fen günlük plan">5 fen günlük plan</a>
            <a href="?q=tde+öğretim+programı" data-ornek="tde öğretim programı">tde öğretim programı</a>
            <a href="?q=ortak+yazılı+matematik" data-ornek="ortak yazılı matematik">ortak yazılı matematik</a>
            <a href="?q=lgs" data-ornek="lgs">lgs</a>
            <a href="?q=ara+tatil" data-ornek="ara tatil">ara tatil</a>
          </div>
        </div>
      </div>
    </div>
  </section>''', ()),
}

for ad, (baslik, aciklama, govde, betikler) in GOVDE.items():
    (PUBLIC / ad).write_text(sayfa(ad, baslik, aciklama, govde, betikler), encoding='utf-8')

# Gizlilik ve 404: mevcut gövdeleri korunur, üst/alt yenilenir
for ad, baslik, aciklama, kanonik in [('gizlilik.html', 'Gizlilik ve çerezler', 'Ders Kutusu gizlilik ve çerez bilgilendirmesi.', True),
                                      ('404.html', 'Sayfa bulunamadı', 'Aradığınız sayfa bulunamadı.', False)]:
    eski = (PUBLIC / ad).read_text(encoding='utf-8')
    govde = eski[eski.index('<main'):eski.index('</main>')]
    govde = govde[govde.index('>') + 1:].strip('\n')
    if 'class="metin-sayfa"' not in govde:
        govde = f'<div class="metin-sayfa">\n{govde}\n</div>'
    betik = ''
    if '<script>' in eski:
        betik = eski[eski.index('<script>'):eski.index('</script>') + len('</script>')]
    html = sayfa(ad, baslik, aciklama, govde, kanonik=kanonik).replace('</body>', (betik + '\n' if betik else '') + '</body>')
    (PUBLIC / ad).write_text(html, encoding='utf-8')

print('üretildi:', ', '.join([*GOVDE, 'gizlilik.html', '404.html']))
