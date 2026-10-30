#!/usr/bin/env python3
"""İç sayfaları (sinif.html, icerikler.html, gizlilik.html, 404.html) ana sayfanın üst ve alt bölümüyle üretir.

Ana sayfadaki simge takımı, üst menü ve alt bilgi değişince bu betik yeniden çalıştırılır:
    python3 araclar/sayfa_uret.py
Sayfaların kendi gövdeleri aşağıdaki GOVDE sözlüğündedir.
"""
import re
from pathlib import Path
from kesif_sablonlari import kesif_sayfa, kutuphane_govde

PUBLIC = Path(__file__).resolve().parent.parent / 'public'
ana = (PUBLIC / 'index.html').read_text(encoding='utf-8')
SURUM = re.search(r'stil\.css\?v=(\d+)', ana).group(1)
BETIK_SURUMLERI = {'goruntule.js': '20261012-1', 'belgeler.js': '20261012-1', 'agac.js': '20261029-3', 'yazili.js': '20261010-1', 'ortak.js': '20261031-3', 'tahta.js': '20261018-5', 'etkinlik.js': '20261017-9', 'arama.js': '20261004-duzen1', 'kutuphane.js': '20261029-3', 'arapca.js': '202610061430', 'yazili-cikti.js': '79d67c33e4', 'yazili-duzen.js': '20261013-1', 'asds.js': '20261029-1'}

simgeler = ana[ana.index('<!-- Simge takımı'):ana.index('</svg>\n\n<header') + len('</svg>')]
ust = ana[ana.index('<header class="ust">'):ana.index('</header>') + len('</header>')]
alt = ana[ana.index('<footer class="alt">'):ana.index('</footer>') + len('</footer>')]
# İç sayfalarda bölüm bağlantıları ana sayfaya gider
ust = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'(<a\b[^>]*\bhref=")#', r'\1/#', ust))
alt = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'(<a\b[^>]*\bhref=")#', r'\1/#', alt))


# Çerezsiz ziyaret sayacı (Cloudflare Web Analytics; kişisel veri toplamaz, gizlilik.html'de açıklanır)
SAYAC = '''<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "fffb5e8a709947ee9ba14ea753d96275"}'></script><!-- End Cloudflare Web Analytics -->'''


# Site ağacı (kullanıcı 11.10.2026): her sayfa kendi dalının kitlesini taşır (üst menü vurgusu, kayan şerit süzgeci).
KITLE_OGRENCI = ('ogrenci.html', 'kelime.html', 'arapca.html', 'sinav.html')
KITLE_OGRETMEN = ('ogretmen.html', 'planlar.html', 'yazili.html', 'belgeler.html', 'kpss.html', 'ders-dagitim.html')
AGAC_CSS = '<link rel="stylesheet" href="/agac.css?v=20261029-2">'


def kitle_bul(ad):
    if ad.startswith(('ozet/', 'calisma/')) or ad in KITLE_OGRENCI:
        return 'ogrenci'
    return 'ogretmen' if ad in KITLE_OGRETMEN else ''


def kitle_ekle(html, ad):
    k = kitle_bul(ad)
    if k and 'data-kitle=' not in html:
        html = re.sub(r'<body\b', f'<body data-kitle="{k}"', html, count=1)
    if ad in ('ogrenci.html', 'ogretmen.html') and 'agac.css?' not in html:
        html = html.replace('</head>', AGAC_CSS + '\n</head>', 1)
    return html


# Reklam birimi yerleri (kullanıcı 29.09 "adsense de kurabiliriz", 17.10; AGENTS-TAM 46): yalnız ana/ağaç sayfaları ve konu özetleri,
# alt bilginin üstünde tek alan. Etkinlik, kalem/tahta, kitap görüntüleyici, yazılı/plan indirme ve kelime/Arapça çalışma sayfalarına konmaz.
# Alan HTML'de gizli (hidden) durur; ortak.js yalnız ziyaretçi izin verip betik yüklenince açar ve doldurur (izin yoksa yer kaplamaz).
# Slot kimliklerini kullanıcı AdSense'ten verir (Reklamlar → Reklama göre → Görüntülü reklam, duyarlı); kimlik yokken <ins> yazılmaz,
# alan boş ve gizli kalır. Kimlik gelince buraya yazılır, ozet_uret.py + ust_guncelle.py yeniden çalıştırılır.
REKLAM_MUSTERI = 'ca-pub-6660544937586858'
REKLAM_SLOTLAR = {'ana': '', 'ozet': ''}   # 'ana': "Ders Kutusu – sayfa altı" (index, öğrenci, öğretmen, içerikler); 'ozet': "Ders Kutusu – özet altı"
REKLAM_SAYFALARI = {'index.html': 'ana', 'ogrenci.html': 'ana', 'ogretmen.html': 'ana', 'icerikler.html': 'ana'}


def reklam_yeri(ad):
    """Sayfanın reklam alanı (alt bilginin hemen üstü); reklam konmayan sayfada boş."""
    yer = 'ozet' if ad.startswith('ozet/') else REKLAM_SAYFALARI.get(ad)
    if not yer:
        return ''
    slot = REKLAM_SLOTLAR.get(yer, '')
    birim = (f'<ins class="adsbygoogle" style="display:block" data-ad-client="{REKLAM_MUSTERI}" data-ad-slot="{slot}" data-ad-format="auto" '
             'data-full-width-responsive="true" data-tag-for-age-treatment="1"></ins>') if slot else ''
    return f'<aside class="reklam" data-reklam="{yer}" aria-label="Reklam" hidden><div class="kap"><span class="reklam-etiket">Reklam</span>{birim}</div></aside>\n'


SOSYAL_DAVET = '''  <div class="kap"><aside class="sosyal-davet" aria-label="Sosyal medya takip çağrısı">
    <div class="sd-sol">
      <span class="sd-simge" aria-hidden="true"><svg><use href="#s-instagram"/></svg></span>
      <div>
        <strong>Günlük bilgi kartları ve yazılı serileri için Instagram'dayız!</strong>
        <p>5–12. sınıf konu özeti kartlarını, yazılıya hazırlık karusellerini ve yeni çalışma kâğıtlarını kaçırmamak için <b>@derskutusuinfo</b> hesabımızı takip edin.</p>
      </div>
    </div>
    <div class="sd-eylemler">
      <a class="dugme sd-ig" href="https://www.instagram.com/derskutusuinfo/" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#s-instagram"/></svg><span>@derskutusuinfo · Takip et</span></a>
      <a class="dugme sd-fb" href="https://www.facebook.com/derskutusuinfo" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#s-facebook"/></svg><span>Facebook</span></a>
    </div>
  </aside></div>'''


def sema_olustur(ad, baslik, aciklama, sema_ek=None):
    import json as _j
    kurum = {
        '@type': 'EducationalOrganization',
        '@id': 'https://derskutusu.com/#kurum',
        'name': 'Ders Kutusu',
        'url': 'https://derskutusu.com/',
        'logo': 'https://derskutusu.com/simge-512.png',
        'email': 'info@derskutusu.com',
        'sameAs': [
            'https://www.instagram.com/derskutusuinfo/',
            'https://www.facebook.com/derskutusuinfo',
            'https://www.youtube.com/@derskutusuinfo',
        ],
    }
    graf = [kurum]
    if sema_ek:
        graf.extend(sema_ek if isinstance(sema_ek, list) else [sema_ek])
    else:
        graf.append({
            '@type': 'WebPage',
            '@id': f'https://derskutusu.com/{ad}#sayfa',
            'url': f'https://derskutusu.com/{ad}',
            'name': f'{baslik} · Ders Kutusu',
            'description': aciklama,
            'inLanguage': 'tr-TR',
            'isPartOf': {'@type': 'WebSite', '@id': 'https://derskutusu.com/#site', 'name': 'Ders Kutusu', 'url': 'https://derskutusu.com/'},
            'publisher': {'@id': 'https://derskutusu.com/#kurum'},
        })
    veri = _j.dumps({'@context': 'https://schema.org', '@graph': graf}, ensure_ascii=False)
    return f'<script type="application/ld+json">{veri}</script>\n'


def sayfa(ad, baslik, aciklama, govde, betikler=(), kanonik=True, sema_ek=None):
    kan = (f'<link rel="canonical" href="https://derskutusu.com/{ad}">\n'
           f'<meta property="og:url" content="https://derskutusu.com/{ad}">\n') if kanonik else '<meta name="robots" content="noindex">\n'
    og_tip = 'article' if ad.startswith('ozet/') else 'website'
    sema = sema_olustur(ad, baslik, aciklama, sema_ek) if kanonik else ''
    js =''.join(f'<script src="/{b}?v={BETIK_SURUMLERI.get(b, SURUM)}"></script>\n' for b in ('ortak.js', *betikler, 'arama.js', 'tahta.js'))
    if ad == 'icerikler.html':
        govde = kutuphane_govde(govde)
    html = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{baslik} · Ders Kutusu</title>
<meta name="description" content="{aciklama}">
{kan}<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#2451d6">
<meta name="google-adsense-account" content="ca-pub-6660544937586858">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="{og_tip}">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Ders Kutusu">
<meta property="og:title" content="{baslik} · Ders Kutusu">
<meta property="og:description" content="{aciklama}">
<meta property="og:image" content="https://derskutusu.com/paylasim.png">
<meta name="twitter:card" content="summary_large_image">
{sema}<link rel="stylesheet" href="/stil.css?v={SURUM}">
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>

{simgeler}

{ust}

<main id="icerik">
{govde}
</main>

{reklam_yeri(ad)}{alt}

{js}{SAYAC}
</body>
</html>
'''
    return kitle_ekle(kesif_sayfa(html, ad), ad)


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
      <nav class="hizli-baglanti" id="ogretmen-hizli" aria-label="Öğretmen dosyaları" hidden></nav>
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
      <p>Sınıfa, derse, haftaya ve türe göre arayın: konu anlatımları, soru çözümleri, videolar; öğretmenler için yıllık planlar, yazılı soruları ve çalışma kâğıtları.</p>
    </div>
  </section>
  <section class="bolum">
    <div class="kap">
      <form class="suzgec-cubugu" role="search" onsubmit="return false">
        <label>Sınıf<select id="s-sinif"><option value="">Bütün sınıflar</option></select></label>
        <label>Ders<select id="s-ders"></select></label>
        <label>Kimin için<select id="s-kitle"><option value="">Herkes</option><option value="ogrenci">Öğrenci</option><option value="ogretmen">Öğretmen</option></select></label>
        <label>Hafta<select id="s-hafta"><option value="">Bütün haftalar</option></select></label>
        <label>Tür<select id="s-tur"></select></label>
        <label class="arama">Ara<input id="s-ara" type="search" placeholder="Konu, başlık…" autocomplete="off"></label>
      </form>
      <div class="secili-suzgecler" id="secili-suzgecler" role="group" aria-label="Seçili süzgeçler" hidden></div>
      <p class="sonuc-bilgi"><span id="sonuc-sayi" role="status" aria-live="polite" aria-atomic="true"></span><button type="button" id="temizle" hidden>Seçimleri temizle</button></p>
      <div class="kartlar" id="kartlar"></div>
      <div class="yakinda" id="icerik-yakinda" hidden>
        <div class="yakinda-simge" aria-hidden="true"><svg><use href="#s-kitap"/></svg></div>
        <div>
          <h3 id="sonucsuz-baslik">Bu seçimde henüz içerik yok</h3>
          <p id="sonucsuz-aciklama">Başka bir sınıf, ders veya tür seçebilirsiniz.</p>
          <div class="sonucsuz-eylemler">
            <button class="dugme ana" type="button" id="aramayi-temizle" hidden>Yalnız aramayı temizle</button>
            <button class="dugme" type="button" id="sonucsuz-temizle" hidden>Tüm içerikleri göster</button>
          </div>
        </div>
      </div>
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
    'goruntule.html': ('Belge', 'Resmî belgeyi Ders Kutusu içinde görüntüleyin.', '''  <section class="g-bas">
    <div class="kap g-bas-ic">
      <div>
        <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/belgeler.html">Resmî belgeler</a></nav>
        <h1 id="g-baslik">Belge yükleniyor…</h1>
        <p id="g-bilgi"></p>
      </div>
      <div class="g-dugmeler" id="g-dugmeler"></div>
    </div>
  </section>
  <div class="g-alan" id="g-alan"></div>''', ('goruntule.js',)),
    'yazili.html': ('Ortak yazılılar: senaryo ve öğrenme çıktısı', 'Ortak yazılı senaryoları ve öğrenme çıktısına göre yazılı kâğıtları: sınıf ve dersi seçin; senaryo tablosu, öğrenci kâğıdı ve cevap anahtarı (PDF).', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a id="y-yol-sinif" href="/ogretmen.html">Öğretmen Köşesi</a><span aria-hidden="true">/</span><span>Yazılılar</span></nav>
      <h1 id="y-baslik">Yazılılar</h1>
      <p id="yd-giris">1. dönem, 2026-2027. Sınıfınızı ve dersinizi seçin; o ders için iki tür yazılı açılır: senaryoya göre ve öğrenme çıktısına göre. Cevap anahtarları yalnız bu sayfadadır; öğrenciler kâğıtları <a href="/ogrenci.html">Öğrenci</a> bölümünde yalnızca öğrenci kâğıdı olarak bulur.</p>
      <div class="yd-secim" id="yd-secim"></div>
      <nav class="sinif-gecis" id="y-siniflar" aria-label="Aynı dersin öteki sınıfları"></nav>
      <nav class="yd-gecis" id="yd-gecis" aria-label="Bu sayfadaki bölümler" hidden></nav>
    </div>
  </section>
  <section class="bolum y-bolum" id="senaryo-yazilisi" aria-labelledby="yd-s1-baslik">
    <div class="kap">
      <h2 class="yd-baslik" id="yd-s1-baslik">1 · Senaryoya göre yazılı</h2>
      <p class="yd-aciklama">Okulun zümresi ÖDSGM ortak yazılı senaryolarından birini seçer; tablo her öğrenme çıktısından kaç soru çıkacağını gösterir, hazır kâğıt da o senaryonun tam yazılısıdır.</p>
      <div class="g-dugmeler y-ust" id="y-dugmeler"></div>
      <div class="y-secim">
        <div class="sekmeler" id="y-yazililar" role="group" aria-label="Yazılı"></div>
        <div class="cipler" id="y-senaryolar" role="group" aria-label="Senaryo"></div>
        <label class="y-yalniz"><input type="checkbox" id="y-yalniz" checked> Yalnız soru çıkan öğrenme çıktıları</label>
      </div>
      <div class="y-kaydir" id="y-tablo"></div>
    </div>
  </section>\n''' + SOSYAL_DAVET, ('yazili.js', 'yazili-cikti.js', 'yazili-duzen.js')),
    'tahta.html': ('Akıllı tahta', 'Tarayıcıda çalışan akıllı tahta: hassas kalem, ekran ve ses kaydı, akıllı şekil tanıma, seç-taşı, soru görseli yapıştırma, süre ölçer, cevap perdesi, koordinat ekseni ve çoklu sayfa.', '''  <section class="tahta-sayfa">
    <div class="kap tahta-ustbar">
      <h1>Akıllı tahta</h1>
      <label class="gizli" for="t-zemin">Zemin</label>
      <select id="t-zemin" aria-label="Zemin"><option value="kareli">Kareli</option><option value="cizgili">Çizgili</option><option value="noktali">Noktalı</option><option value="izometrik">İzometrik noktalı</option><option value="koordinat">Koordinat düzlemi</option><option value="birim-cember">Birim çember</option><option value="sayidogrusu">Sayı doğrusu</option><option value="muzik">Müzik dizeği (Porte)</option><option value="koyu">Koyu tahta</option><option value="">Düz beyaz</option></select>
      <button class="dugme" type="button" id="t-onceki" title="Önceki sayfa" aria-label="Önceki sayfa">‹</button>
      <span id="t-sayfa" aria-live="polite">1 / 1</span>
      <button class="dugme" type="button" id="t-sonraki" title="Sonraki ya da yeni sayfa" aria-label="Sonraki ya da yeni sayfa">›</button>
      <button class="dugme" type="button" id="t-cogalt" title="Bu sayfayı çoğalt">Çoğalt</button>
      <button class="dugme" type="button" id="t-sil" title="Bu sayfayı sil">Sayfayı sil</button>
      <button class="dugme" type="button" id="t-video" title="Ekran, tahta ve ses kaydı al">● Ders Kaydı</button>
      <button class="dugme" type="button" id="t-kaydet"><svg><use href="#s-indir"/></svg>PNG</button>
      <button class="dugme ana" type="button" id="t-tam"><svg><use href="#s-buyut"/></svg>Tam ekran</button>
    </div>
    <div class="tahta-alan" id="tahta-alan"><div id="tahta"></div></div>
  </section>''', ()),
    'katki.html': ('Katkıda bulun', 'Ders Kutusu’na katkıda bulunun: hata bildirin, içerik önerin, paylaşın.', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Katkıda bulun</span></nav>
      <h1>Katkıda bulun</h1>
      <p>Ders Kutusu ücretsizdir. Siteyi daha doğru, daha güncel ve daha kullanışlı yapmak için birkaç dakikanızı ayırmanız bile büyük destek olur.</p>
    </div>
  </section>
  <section class="bolum">
    <div class="kap katki-izgara">
      <article class="kart katki-kart">
        <h2>Hata bildirin</h2>
        <p>Bir plan dosyasında, özette ya da cevapta yanlış mı gördünüz? Sayfanın adresini ve hatayı yazmanız yeterli; en kısa sürede düzeltiriz.</p>
        <a class="dugme ana" data-katki="hata" href="mailto:info@derskutusu.com?subject=Hata%20bildirimi">Hata bildir</a>
      </article>
      <article class="kart katki-kart">
        <h2>İçerik önerin</h2>
        <p>Hangi sınıf ve ders için hangi konu özetini, çalışma kâğıdını ya da planı görmek istersiniz? Önerileriniz sıramızı belirler.</p>
        <a class="dugme" data-katki="oneri" href="mailto:info@derskutusu.com?subject=%C4%B0%C3%A7erik%20%C3%B6nerisi">Öneri gönder</a>
      </article>
      <article class="kart katki-kart">
        <h2>Paylaşın</h2>
        <p>Siteyi zümrenizle, öğrencilerinizle ve velilerle paylaşın. Ne kadar çok kişi kullanırsa o kadar çok içerik hazırlayabiliriz.</p>
        <button class="dugme" type="button" id="katki-paylas">Bağlantıyı paylaş</button>
        <p class="katki-not" id="katki-durum" aria-live="polite"></p>
      </article>
      <article class="kart katki-kart">
        <h2>Takip edin</h2>
        <p>Yeni içerikleri ilk siz görün. Takip etmek ve videolara yorum bırakmak da bize destek olur.</p>
        <div class="katki-sosyal">
          <a class="dugme" href="https://www.youtube.com/@derskutusuinfo" data-sosyal="youtube" target="_blank" rel="noopener"><svg><use href="#s-youtube"/></svg>YouTube</a>
          <a class="dugme" href="https://www.instagram.com/derskutusuinfo/" data-sosyal="instagram" target="_blank" rel="noopener"><svg><use href="#s-instagram"/></svg>Instagram</a>
          <a class="dugme" href="https://www.facebook.com/derskutusuinfo" data-sosyal="facebook" target="_blank" rel="noopener"><svg><use href="#s-facebook"/></svg>Facebook</a>
        </div>
      </article>
      <article class="kart katki-kart genis">
        <h2>Öğretmenler: kendi materyalinizi gönderin</h2>
        <p>Kendi hazırladığınız çalışma kâğıdı, yazılı sorusu ya da etkinliği sitede adınızla yayımlayabiliriz. Yalnız size ait olan, başka bir kitaptan ya da siteden alınmamış içerikleri kabul ediyoruz; gönderdiğiniz dosyada adınızı ve yayımlanmasına izin verdiğinizi belirtmeniz yeterli.</p>
        <a class="dugme" href="mailto:info@derskutusu.com?subject=Materyal%20g%C3%B6nderimi">Materyal gönder</a>
      </article>
    </div>
  </section>
  <script>
    (function () {
      var d = document.getElementById('katki-paylas'), durum = document.getElementById('katki-durum');
      d.addEventListener('click', function () {
        var veri = { title: 'Ders Kutusu', text: '5–12. sınıf planlar, konu özetleri, resmî belgeler ve akıllı tahta', url: 'https://derskutusu.com/' };
        if (navigator.share) { navigator.share(veri).catch(function () {}); return; }
        (navigator.clipboard ? navigator.clipboard.writeText(veri.url) : Promise.reject()).then(function () { durum.textContent = 'Bağlantı kopyalandı.'; }, function () { durum.textContent = veri.url; });
      });
    })();
  </script>''', ()),
}


def _sinav_govde():
    """Sınavlar sayfası (LGS, YKS): veri/sinavlar.json + veri/belgeler.json'dan durağan HTML + canlı sayaç ve net hesaplayıcı."""
    import html as _h
    import json as _j
    sv = _j.loads((PUBLIC / 'veri' / 'sinavlar.json').read_text(encoding='utf-8'))
    bl = {b['kimlik']: b for g in _j.loads((PUBLIC / 'veri' / 'belgeler.json').read_text(encoding='utf-8'))['gruplar'] for b in g['belgeler']}
    e = _h.escape
    gecis = (
        '<a href="#asds-bolum-kapsayici">Haftalık Denemeler (ASDS)</a>'
        '<a href="#asds-sinif-5">5. Sınıf Denemeleri</a>'
        '<a href="#asds-sinif-6">6. Sınıf Denemeleri</a>'
        '<a href="#asds-sinif-7">7. Sınıf Denemeleri</a>'
        '<a href="#asds-sinif-8">8. Sınıf (LGS) Denemeleri</a>'
    )
    gecis += ''.join(f'<a href="#{x["kimlik"]}">{e(x["ad"])} Rehberi</a>' for x in sv['sinavlar'])
    gecis += '<a href="#net-hesaplayici">Net ve Başarı Hesaplayıcı</a>'
    bolumler = ''
    for n, x in enumerate(sv['sinavlar']):
        lgs = x['kimlik'] == 'lgs'
        hedef_sinif = '8' if lgs else '12'
        kartlar = ''
        for o in x['oturumlar']:
            satir = ''
            for t in o['testler']:
                dk = e(t[2])
                ozet_url = f'/ogrenci.html?sinif={hedef_sinif}&amp;ders={dk}'
                calisma_url = f'/icerikler.html?{"sinif=8&amp;" if lgs else ""}ders={dk}&amp;tur=%C3%87al%C4%B1%C5%9Fma%20k%C3%A2%C4%9F%C4%B1d%C4%B1'
                yazili_url = f'/ogrenci.html?sinif={hedef_sinif}&amp;ders={dk}#yaziliya-hazirlik'
                satir += (f'<tr><td><a class="sinav-ders-ad" href="{ozet_url}">{e(t[0])}</a>'
                          f'<span class="sinav-hizli"><a href="{ozet_url}">Konu Özeti</a><a href="{calisma_url}">Çalışma Kâğıdı</a><a href="{yazili_url}">Yazılı PDF</a></span></td>'
                          f'<td class="sayi">{t[1]}</td></tr>')
            kartlar += (f'<article class="kart sinav-oturum"><h3>{e(o["ad"])}</h3>'
                        f'<p class="sinav-ozet"><b>{o["toplam"]}</b> soru · <b>{o["sure"]}</b> dakika</p>'
                        f'<table class="sinav-tablo"><thead><tr><th>Test ve hızlı çalışma</th><th class="sayi">Soru</th></tr></thead><tbody>{satir}</tbody></table></article>')
        belge = ''.join(
            f'<li><a href="/goruntule.html?b={k}">{e(bl[k]["baslik"])}</a><span>{e(bl[k].get("kaynak", ""))}</span></li>'
            for k in x['belgeler'] if k in bl)
        if lgs:
            hazirlik = ('<li><a href="/ogrenci.html?sinif=8">8. sınıfın bütün dersleri ve üniteleri</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=Konu%20anlat%C4%B1m%C4%B1">8. sınıf konu özetleri ve etkinlikler</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=%C3%87al%C4%B1%C5%9Fma%20k%C3%A2%C4%9F%C4%B1d%C4%B1">8. sınıf çalışma kâğıtları (PDF)</a></li>'
                        '<li><a href="/yazili.html?sinif=8">8. sınıf ortak yazılı senaryoları ve kâğıtları</a></li>')
        else:
            hazirlik = ''.join(f'<li><a href="/ogrenci.html?sinif={k}">{k}. sınıfın bütün dersleri ve üniteleri</a></li>' for k in x['siniflar'])
            hazirlik += '<li><a href="/icerikler.html?tur=Ders%20kitab%C4%B1">Lise MEB ders kitapları</a></li>'
        bolumler += f'''  <section class="bolum{' koyu-zemin' if n % 2 else ''}" id="{x['kimlik']}">
    <div class="kap">
      <div class="bolum-bas"><div><p class="ust-baslik">{e(x['kurum'])} · {e(x['kim'])}</p><h2>{e(x['ad'])}: {e(x['uzun_ad'])}</h2><p>{e(x['not'])}</p></div></div>
      <div class="sinav-oturumlar">{kartlar}</div>
      <div class="sinav-alt">
        <div><h3>Resmî belgeler ve çıkmış sorular</h3><ul class="sinav-liste">{belge}</ul></div>
        <div><h3>Sitede hazırlık</h3><ul class="sinav-liste">{hazirlik}</ul></div>
      </div>
    </div>
  </section>
'''
    sayac_ve_hesap = '''  <section class="bolum sinav-kokpit-bolum" aria-label="Sınav geri sayım panosu">
    <div class="kap">
      <div class="sinav-sayac-pano" id="sinav-sayac-pano">
        <article class="sinav-sayac-kart lgs-kart">
          <div class="ssk-ust"><span class="ssk-etiket">MEB · 8. Sınıf Merkezî Sınav</span><strong>LGS Hazırlık Takvimi</strong></div>
          <div class="ssk-zaman" data-sinav-sayac="lgs"><b>Haziran 2027</b><span>50 Sözel (75 dk) + 40 Sayısal (80 dk) · Toplam 90 Soru</span></div>
          <div class="ssk-cubuk" aria-hidden="true"><i data-sinav-cubuk="lgs" style="width:22%"></i></div>
          <div class="ssk-eylemler">
            <a class="dugme ana" href="/ogrenci.html?sinif=8">8. Sınıf Dersleri</a>
            <a class="dugme" href="#net-hesaplayici" data-hesap-sec="lgs">LGS Net Hesapla ↓</a>
          </div>
        </article>
        <article class="sinav-sayac-kart yks-kart">
          <div class="ssk-ust"><span class="ssk-etiket">ÖSYM · 12. Sınıf &amp; Mezun</span><strong>YKS (TYT · AYT · YDT) Takvimi</strong></div>
          <div class="ssk-zaman" data-sinav-sayac="yks"><b>Haziran 2027</b><span>TYT 120 Soru (165 dk) · AYT 160 Soru (180 dk)</span></div>
          <div class="ssk-cubuk" aria-hidden="true"><i data-sinav-cubuk="yks" style="width:22%"></i></div>
          <div class="ssk-eylemler">
            <a class="dugme ana" href="/ogrenci.html?sinif=12">12. Sınıf Dersleri</a>
            <a class="dugme" href="#net-hesaplayici" data-hesap-sec="tyt">TYT Net Hesapla ↓</a>
          </div>
        </article>
      </div>
    </div>
  </section>
'''
    hesaplayici = '''  <section class="bolum koyu-zemin" id="net-hesaplayici" aria-labelledby="nh-baslik">
    <div class="kap">
      <div class="bolum-bas">
        <div>
          <p class="ust-baslik">Deneme analizi ve çalışma rehberi</p>
          <h2 id="nh-baslik">LGS ve YKS (TYT) Net &amp; Başarı Hesaplayıcı</h2>
          <p>Deneme sınavındaki doğru ve yanlış sayılarını gir; branş netlerin, başarı yüzdelerin ve öncelikli çalışman gereken ders anında hesaplansın.</p>
        </div>
        <div class="nh-sekmeler" role="tablist" aria-label="Sınav türü">
          <button type="button" role="tab" class="nh-sekme" data-nh-tur="lgs" aria-selected="true">LGS (8. Sınıf · 3Y=1D)</button>
          <button type="button" role="tab" class="nh-sekme" data-nh-tur="tyt" aria-selected="false">YKS – TYT (4Y=1D)</button>
        </div>
      </div>
      <div class="nh-duzen" id="nh-duzen">
        <div class="nh-tablo-kutu" id="nh-tablo-kutu"></div>
        <aside class="nh-ozet-kutu" id="nh-ozet-kutu" aria-live="polite"></aside>
      </div>
    </div>
  </section>
'''
    asds_bolumu = '''  <section class="bolum asds-ana-bolum" id="asds-bolum-kapsayici" aria-labelledby="asds-ana-baslik">
    <div class="kap">
      <div class="bolum-bas">
        <div>
          <p class="ust-baslik">5, 6, 7 ve 8. Sınıf Haftalık Deneme Sınavları · A &amp; B Kitapçığı</p>
          <h2 id="asds-ana-baslik">Akademik Süreç Değerlendirme Sınavları (ASDS)</h2>
          <p>Her bir sınıf için ayrı başlık altında; sınav uygulaması için <b>Cevapsız A ve B Kitapçıkları</b> ile öğretmen ve çözüm kontrolü için <b>Cevaplı A ve B Kitapçıkları + Cevap Anahtarı (PDF)</b> yer alır.</p>
        </div>
      </div>
      <div id="asds-bolum" class="asds-bolum-kutu">
        <p role="status">Deneme sınavları ve kitapçıklar yükleniyor…</p>
      </div>
    </div>
  </section>
'''
    return f'''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Sınavlar ve Denemeler</span></nav>
      <h1>Sınavlar ve Haftalık Deneme Sınavları (ASDS · LGS · YKS)</h1>
      <p>5, 6, 7 ve 8. sınıf haftalık Akademik Süreç Değerlendirme Sınavları (Cevapsız &amp; Cevaplı A ve B kitapçıkları), LGS/YKS oturum dağılımları ve etkileşimli net hesaplayıcı.</p>
      <nav class="sinif-gecis" aria-label="Sınavlar">{gecis}</nav>
    </div>
  </section>
{asds_bolumu}{sayac_ve_hesap}{bolumler}{hesaplayici}'''


GOVDE['planlar.html'] = ('Günlük planlar', 'Günlük ders planları: Okul, öğretmen, müdür yardımcısı ve müdür adları her sayfaya yazılır. Plan tüm yıl ya da ay ay, Word veya PDF olarak indirilir.', '''  <section class="sayfa-bas plan-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/#ogretmen">Öğretmen</a><span aria-hidden="true">/</span><span>Günlük planlar</span></nav>
      <h1>Günlük ders planları</h1>
      <p>Okulun adını, kendi adınızı, müdür yardımcısının ve müdürün adını bir kez yazın. İndirdiğiniz planın her sayfasına bu bilgiler kendiliğinden yerleşir. Planı tüm yıl ya da ay ay, Word veya PDF olarak alın.</p>
      <ol class="plan-adimlar" aria-label="Adımlar">
        <li><span>1</span>Bilgileri yazın</li>
        <li><span>2</span>Sınıfı ve dersi seçin</li>
        <li><span>3</span>Ayı ve biçimi seçip indirin</li>
      </ol>
    </div>
  </section>
  <section class="bolum plan-bolum">
    <div class="kap plan-duzen">
      <aside class="plan-yan">
        <form class="plan-bilgi" id="p-bilgi" onsubmit="return false" aria-labelledby="p-bilgi-baslik">
          <h2 id="p-bilgi-baslik"><span class="adim-no">1</span>Plan bilgileri</h2>
          <label>Okulun adı<input id="p-okul" maxlength="90" placeholder="Örnek: Atatürk Ortaokulu" autocomplete="organization" spellcheck="false"></label>
          <label>Ders öğretmeni<input id="p-ogretmen" maxlength="60" placeholder="Adınız ve soyadınız" autocomplete="name" spellcheck="false"></label>
          <label>Müdür yardımcısı<input id="p-mudur-yrd" maxlength="60" placeholder="Adı ve soyadı" autocomplete="off" spellcheck="false"></label>
          <label>Okul müdürü<input id="p-mudur" maxlength="60" placeholder="Adı ve soyadı" autocomplete="off" spellcheck="false"></label>
          <label class="plan-secenek"><input type="checkbox" id="p-tarih" checked> Onay tarihine haftanın ilk iş gününü yaz</label>
          <label class="plan-secenek"><input type="checkbox" id="p-hatirla" checked> Bilgileri bu cihazda hatırla</label>
          <p class="plan-not">Bilgiler yalnız sizin tarayıcınızda kalır, hiçbir yere gönderilmez. Boş bıraktığınız alan belgede noktalı kalır.</p>
        </form>
        <figure class="plan-onizleme" aria-label="Sayfa önizlemesi">
          <div class="kagit" id="p-kagit" aria-hidden="true">
            <div class="k-ust"><img src="/simge-192.png" alt="" width="18" height="18"><b>DERS KUTUSU</b><span id="k-ust-sag">Günlük plan · 2026-2027</span></div>
            <p class="k-okul" id="k-okul"></p>
            <p class="k-baslik" id="k-baslik">5. SINIF MATEMATİK DERSİ GÜNLÜK PLANI</p>
            <p class="k-hafta" id="k-hafta">2026-2027 Eğitim Öğretim Yılı · 1. Hafta: 14-18 Eylül</p>
            <div class="k-tablo"><i></i><i></i><i></i><i></i><i></i><i></i></div>
            <div class="k-imza">
              <div><b>Ders Öğretmeni</b><span class="k-bos"></span><span id="k-ogretmen"></span></div>
              <div><b>Müdür Yardımcısı</b><span class="k-bos"></span><span id="k-mudur-yrd"></span></div>
              <div><b>Uygundur</b><span id="k-tarih">14.09.2026</span><span id="k-mudur"></span><span>Okul Müdürü</span></div>
            </div>
          </div>
          <figcaption>Bilgiler planın her sayfasında bu yerlere yazılır.</figcaption>
        </figure>
      </aside>
      <div class="plan-ana">
        <div class="plan-kutu">
          <h2><span class="adim-no">2</span>Sınıf ve ders</h2>
          <div class="sekmeler plan-siniflar" id="p-siniflar" role="group" aria-label="Sınıf"></div>
          <label class="plan-ara"><svg aria-hidden="true"><use href="#s-mercek"/></svg><span class="gizli">Ders ara</span><input id="p-ara" type="search" placeholder="Ders ara (ör. matematik)" autocomplete="off"></label>
          <div id="p-dersler" class="plan-gruplar"></div>
          <p id="p-sonuc" class="gizli" role="status" aria-live="polite"></p>
        </div>
        <div class="plan-kutu plan-indir" id="p-indir" hidden tabindex="-1">
          <h2><span class="adim-no">3</span><span id="p-secili-ad">İndir</span></h2>
          <p class="plan-ozet" id="p-secili-bilgi"></p>
          <div class="plan-bicim" role="radiogroup" aria-label="Dosya biçimi">
            <label><input type="radio" name="p-bicim" value="docx" checked><span><b>Word</b><small>Düzenlenebilir .docx</small></span></label>
            <label><input type="radio" name="p-bicim" value="pdf"><span><b>PDF</b><small>Yazdırmaya hazır</small></span></label>
          </div>
          <h3 class="plan-alt-baslik">Hangi dönem?</h3>
          <div class="plan-aylar" id="p-aylar"></div>
          <button type="button" class="dugme plan-zip" id="p-zip"><svg aria-hidden="true"><use href="#s-indir"/></svg><span>Bütün ayları ayrı dosyalar hâlinde indir (ZIP)</span></button>
          <p class="plan-durum" id="p-durum" role="status" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>\n''' + SOSYAL_DAVET, ('planlar.js',))

# Ders dağıtım programı (kullanıcı 22.10.2026): uygulama ders-dagitim-uygulama.html'de tek dosya, kendi stilleriyle;
# site stilleriyle çakışmasın diye bu sayfada çerçeve içinde açılır. Veriler yalnız ziyaretçinin tarayıcısında (localStorage).
GOVDE['ders-dagitim.html'] = ('Ders dağıtım programı', 'Okullar için ücretsiz ders dağıtım programı: öğretmen, sınıf ve ders bilgilerinden haftalık program üretir, yerleşmeyen dersin nedenini gösterir; PDF ve Excel çıktı verir. Veriler yalnız tarayıcınızda kalır.', '''<style>
.ddp-bas { padding-bottom: 28px; }
.ddp-kap { padding: 20px 0 8px; }
.sayfa-bas .dd-sayac { font-size: 16px; margin-top: 8px; }
.dd-sayac strong { color: var(--metin); font-variant-numeric: tabular-nums; }
.ddp-cerceve { display: block; width: 100%; height: calc(100vh - 96px); min-height: 560px; border: 1px solid var(--cizgi); border-radius: var(--kose); background: var(--zemin-2); }
</style>
  <section class="sayfa-bas ddp-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/ogretmen.html">Öğretmen Köşesi</a><span aria-hidden="true">/</span><span>Ders dağıtım programı</span></nav>
      <h1>Ders dağıtım programı</h1>
      <p>Okul ayarlarını, öğretmenleri, sınıfları ve dersleri girin; program haftalık ders çizelgesini kendisi kurar. Yerleşmeyen bir ders kalırsa nedenini ve en az değişiklikle çözüm önerisini gösterir. Program bilgileri yalnız bu tarayıcıda saklanır.</p>
      <p class="dd-sayac" hidden>Programı kullanan okul sayısı: <strong class="dd-sayac-sayi">0</strong></p>
      <script>
      (function () {
        var p = document.querySelector('.dd-sayac'); if (!p || !window.fetch) return;
        var el = p.querySelector('.dd-sayac-sayi');
        fetch('/veri/ders-dagitim-sayac.json', { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (j) {
          var n = j ? Math.max(0, Math.floor(+j.sayi || 0)) : 0; if (!n) return;
          p.hidden = false;
          if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = n; return; }
          var i = 0, adim = Math.max(1, Math.ceil(n / 40));
          (function say() { i = Math.min(n, i + adim); el.textContent = i; if (i < n) setTimeout(say, 40); })();
        }, function () { });
      })();
      </script>
      <p><a class="dugme ana" href="/ders-dagitim-uygulama.html">Tam ekranda aç</a> <a class="dugme" href="#ddp-nasil">Nasıl kullanılır?</a></p>
    </div>
  </section>
  <div class="kap ddp-kap">
    <iframe class="ddp-cerceve" src="/ders-dagitim-uygulama.html" title="Ders dağıtım programı uygulaması"></iframe>
  </div>
  <div class="metin-sayfa" id="ddp-nasil">
    <div class="kap">
      <h2>Nasıl kullanılır?</h2>
      <ol>
        <li><strong>Okul ve ayarlar:</strong> Okul adını, öğretim yılını, günlük ders saati sayısını ve öğle arasını girin.</li>
        <li><strong>Öğretmenler:</strong> Öğretmenleri ve branşlarını ekleyin; ders veremeyecekleri saatleri “Yok” olarak işaretleyin, günlük ders sınırı gibi isteklerini yazın.</li>
        <li><strong>Sınıflar ve dersler:</strong> Her sınıfın derslerini, haftalık ders saatlerini ve dersi okutacak öğretmeni seçin.</li>
        <li><strong>Ortak dersler ve derslikler:</strong> Birlikte işlenen dersleri ve spor salonu, laboratuvar, BT sınıfı gibi aynı anda az sayıda sınıfın kullanabildiği derslikleri tanımlayın.</li>
        <li><strong>Program oluştur:</strong> Program bütün kurallara uyan yerleşimi arar. Yerleşmeyen ders kalırsa nedeni ve en az zararlı “Yok” esnetme önerisi gösterilir.</li>
        <li><strong>Programlar ve çıktı:</strong> Sınıf ve öğretmen programlarını, genel tabloyu ve dağıtım çizelgesini PDF, Excel ya da yazdırılabilir sayfa olarak indirin.</li>
      </ol>
      <h2>Verileriniz</h2>
      <p>Öğretmen, ders ve program bilgileri yalnız bu cihazdaki tarayıcıda saklanır, Ders Kutusu sunucusuna gönderilmez. Okul bilgilerindeki “kullanan okullar listesine eklensin” işareti açıksa programı ilk oluşturduğunuzda yalnız okul adı, ilçe ve öğretmen/sınıf sayısı bildirilir; sitede yalnız kullanan okul sayısı görünür, okul adı Ders Kutusu’nun herkese açık GitHub deposundaki listede görünebilir. İşareti kaldırırsanız hiçbir bilgi gönderilmez. Başka bir bilgisayarda devam etmek için “Yedek indir” ile aldığınız dosyayı orada “Yedek yükle” ile açabilirsiniz. Ayrıntı: <a href="/gizlilik.html">Gizlilik ve çerezler</a>.</p>
    </div>
  </div>''', ())

GOVDE['kelime.html'] = ('İngilizce kelime çalışması', '5 ve 6. sınıf İngilizce kelimeleri: kartlar, sesli dinleme, test, yazma ve eşleştirme. Kelimeler MEB ders kitaplarının sözlük bölümünden.', '''  <section class="sayfa-bas kelime-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/icerikler.html">İçerikler</a><span aria-hidden="true">/</span><span>İngilizce kelimeler</span></nav>
      <h1>İngilizce kelime çalışması</h1>
      <p>Ders kitabındaki kelimeleri kartlarla öğren, sesli dinle, test çöz, yazarak pekiştir ve eşleştir. Kelimeler MEB İngilizce ders kitaplarının sözlük bölümünden alınmıştır.</p>
      <p><a class="dugme" href="/arapca.html">Arapça harf ve kelime çalışması</a></p>
      <nav class="sekmeler" id="k-sinif" aria-label="Sınıf"></nav>
    </div>
  </section>
  <section class="bolum kelime-bolum">
    <div class="kap">
      <div class="kelime-ust">
        <label class="kelime-tema">Tema<select id="k-tema"></select></label>
        <div class="kelime-ilerleme" aria-label="Bu temada öğrendiğin kelimeler">
          <span>Öğrendiğin: <b id="k-ilerleme-sayi">0 / 0</b></span>
          <span class="kelime-cubuk" aria-hidden="true"><i id="k-ilerleme-cubuk"></i></span>
          <button type="button" class="cip-dugme" id="k-sifirla">Sıfırla</button>
        </div>
      </div>
      <nav class="sekmeler kelime-kipler" id="k-kipler" aria-label="Çalışma biçimi"></nav>
      <h2 class="kelime-baslik" id="k-tema-baslik"></h2>
      <div id="k-alan" class="kelime-alan" aria-live="polite"></div>
      <p class="kelime-not">İlerlemen yalnız bu tarayıcıda tutulur, hiçbir yere gönderilmez. Sesler tarayıcının kendi okuma özelliğiyle çıkar.</p>
    </div>
  </section>''', ('kelime.js',))

GOVDE['arapca.html'] = ('Arapça harf ve kelime çalışması', '28 harf ve 48 kelime/ifade: harf biçimleri, harekeler, kartlar, test, Arapça klavyeyle yazma ve eşleştirme.', '''<link rel="stylesheet" href="/arapca.css?v=202610022030">
<section class="sayfa-bas kelime-bas"><div class="kap">
<nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/icerikler.html?ders=arapca">Arapça</a><span>/</span><span>Harf ve kelime çalışması</span></nav>
<p class="ust-baslik">Gör · Oku · Yaz · Eşleştir</p><h1>Arapça harf ve kelime çalışması</h1>
<p>Harfleri ve harekeleri tanı; kelimeleri kartlarla öğren, test çöz ve Arapça klavyeyle yaz. İlk içerikler: 5. sınıf Merhaba, 6. sınıf Akrabalarım.</p>
<nav class="sekmeler" id="a-sinif" aria-label="Sınıf"></nav></div></section>
<section class="bolum kelime-bolum"><div class="kap">
<div class="kelime-ust"><label class="kelime-tema">Kelime grubu<select id="a-konu"></select></label>
<div class="kelime-ilerleme"><span>Öğrendiğin: <b id="a-ilerleme">0 / 0</b></span><span class="kelime-cubuk" aria-hidden="true"><i id="a-cubuk"></i></span><button type="button" class="cip-dugme" id="a-sifirla">Sıfırla</button></div></div>
<nav class="sekmeler kelime-kipler" id="a-modlar" aria-label="Çalışma biçimi"></nav>
<h2 id="a-baslik" class="kelime-baslik">Alfabe ve yazıya hazırlık</h2>
<div id="a-alan" class="kelime-alan"><p>Harf ve kelimeler yükleniyor…</p></div>
<p id="a-ses-durum" class="kelime-not" role="status"></p>
<p class="kelime-not">İlerlemen yalnız bu tarayıcıda tutulur. Kelime ve ifade kapsamı MEB 5–6. sınıf Arapça kitapları ve yıllık planlarına göre hazırlanmıştır. Alfabe bölümü genel tekrar içindir.</p>
<div class="k-dugmeler sol"><a class="dugme" href="/ozet/5-arapca-hafta-1.html">5. sınıf konu anlatımı</a><a class="dugme" href="/ozet/6-arapca-hafta-1.html">6. sınıf konu anlatımı</a><a class="dugme" href="/kelime.html">İngilizce kelime çalışması</a></div>
<noscript>Alıştırmalar için JavaScript’i etkinleştirin. Konu anlatımlarını yukarıdaki bağlantılardan okuyabilirsiniz.</noscript>
</div></section>''', ('arapca.js',))

GOVDE['ogrenci.html'] = ('Öğrenci', 'Ders Kutusu öğrenci sayfası: sınıfını seç; ünite ünite konu anlatımları, etkinlikler, çalışma kâğıtları ve ders kitapları.', '''  <div id="agac" class="agac" aria-busy="true"><section class="agac-bas"><div class="kap">
      <h1>Öğrenci</h1>
      <p>Sınıfını seç; derslerin ünite ve konularına, haftalık konu özetlerine, çözümlü örneklere, etkileşimli etkinliklere ve çalışma kâğıtlarına ulaş. Konular MEB yıllık planındaki hafta sırasıyla eklenir.</p>
      <ul>
        <li><a href="/ogrenci.html?sinif=5">5. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=6">6. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=7">7. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=8">8. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=9">9. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=10">10. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=11">11. sınıf dersleri</a></li>
        <li><a href="/ogrenci.html?sinif=12">12. sınıf dersleri</a></li>
      </ul>
      <p>Ayrıca: <a href="/kelime.html">İngilizce kelime çalışması</a> · <a href="/arapca.html">Arapça harf ve kelime çalışması</a> · <a href="/sinav.html">Sınavlar (LGS, YKS)</a></p>
      <p role="status">Yükleniyor…</p>
    </div></section></div>''', ('agac.js',))
GOVDE['ogretmen.html'] = ('Öğretmen Köşesi', 'Öğretmen Köşesi: günlük ve yıllık planlar, ortak yazılı senaryoları ve kâğıtları, öğretim programları, çalışma kâğıtları ve resmî belgeler.', '''  <div id="agac" class="agac" aria-busy="true"><section class="agac-bas"><div class="kap">
      <h1>Öğretmen Köşesi</h1>
      <p>Derse hazırlık ve ölçme için ihtiyaç duyulan dosyalar kategorilere ayrılmıştır. Kategoriyi, ardından sınıfı seçin.</p>
      <ul>
        <li><a href="/planlar.html">Günlük planlar</a>: Okul ve yönetici adları her sayfaya yazılır; tüm yıl ya da ay ay, Word veya PDF.</li>
        <li><a href="/ders-dagitim.html">Ders dağıtım programı</a>: Öğretmen, sınıf ve derslerden haftalık ders programı; PDF ve Excel çıktı, veriler tarayıcıda.</li>
        <li><a href="/ogretmen.html?kategori=yillik-plan">Yıllık planlar</a>: Güncel öğretim programına göre haftalık yıllık planlar.</li>
        <li><a href="/yazili.html">Yazılı senaryoları ve kâğıtları</a>: Ortak yazılı konu-soru dağılımları ve cevaplı yazılı kâğıtları.</li>
        <li><a href="/ogretmen.html?kategori=ogretim-programi">Öğretim programları</a>: Öğrenme çıktıları, süreç bileşenleri ve açıklamalar.</li>
        <li><a href="/ogretmen.html?kategori=calisma-kagidi">Çalışma kâğıtları</a>: Derste kullanmak için cevaplı ve cevapsız PDF.</li>
        <li><a href="/belgeler.html">Resmî belgeler</a>: MEB, ÖDSGM, DÖGM ve ÖSYM kılavuzları ve tabloları.</li>
        <li><a href="/tahta.html">Akıllı tahta</a>: Kalem, renkler, kareli zemin; tarayıcıda çalışır.</li>
        <li><a href="/kpss.html">KPSS hazırlık</a>: Öğretmen adayları için konu anlatımı ve testler.</li>
      </ul>
      <p role="status">Yükleniyor…</p>
    </div></section></div>''', ('agac.js',))
GOVDE['sinav.html'] = ('Sınavlar ve Deneme Sınavları (ASDS · LGS · YKS)', '5, 6, 7 ve 8. sınıf haftalık Akademik Süreç Değerlendirme Sınavları (ASDS — Cevapsız ve Cevaplı A & B kitapçıkları), LGS ve YKS hazırlık kaynakları.', _sinav_govde(), ('asds.js',))

# Hakkımızda ve İletişim (14.10.2026, AdSense 'düşük değerli içerik' düzeltmesi)
GOVDE['hakkimizda.html'] = ('Hakkımızda', 'Ders Kutusu nedir, kimler için hazırlanır, içerikler nasıl hazırlanır ve denetlenir?', '''<div class="metin-sayfa">
  <div class="kap">
    <h1>Hakkımızda</h1>
    <p>Ders Kutusu, 5–12. sınıf öğrencileri ve öğretmenleri için hazırlanan ücretsiz bir eğitim sitesidir. Okulda o hafta işlenen konuyu aynı sırayla, sade bir dille tekrar etmeyi ve derse hazırlanmayı kolaylaştırmak için kuruldu.</p>

    <h2>Öğrenciler için</h2>
    <ul>
      <li><strong>Haftalık konu özetleri:</strong> her ders için MEB yıllık planındaki hafta sırasıyla; renkli görseller, bilgi ve dikkat kutuları, çözümlü örnekler.</li>
      <li><strong>Etkileşimli etkinlikler:</strong> her özetin sonunda çoktan seçmeli, doğru-yanlış, eşleştirme ve boşluk doldurma soruları; cevap anında denetlenir.</li>
      <li><strong>Çalışma kâğıtları:</strong> haftanın konusunu baştan sona yoklayan iki sayfalık kâğıtlar; cevaplı ve cevapsız PDF.</li>
      <li><strong>Kelime çalışmaları:</strong> İngilizce ve Arapça kelime kartları; dinleme, yazma ve eşleştirme alıştırmaları.</li>
      <li><strong>Sınav bilgileri:</strong> LGS ve YKS için takvim, kapsam ve resmî kaynaklar.</li>
    </ul>

    <h2>Öğretmenler için</h2>
    <ul>
      <li><strong>Yıllık ve günlük planlar:</strong> güncel öğretim programına göre; okul, öğretmen ve yönetici adları her sayfaya yazılır, plan tüm yıl ya da ay ay Word veya PDF olarak indirilir.</li>
      <li><strong>Ortak yazılılar:</strong> senaryo tabloları, öğrenme çıktısına göre hazırlanmış yazılı kâğıtları ve cevap anahtarları.</li>
      <li><strong>Öğretim programları ve resmî belgeler:</strong> MEB, ÖDSGM, DÖGM ve ÖSYM yayınları tek yerde.</li>
      <li><strong>Akıllı tahta:</strong> tarayıcıda çalışan kalem, renkler, kareli ve çizgili zemin.</li>
      <li><strong>KPSS hazırlık:</strong> öğretmen adayları için konu anlatımı ve testler.</li>
    </ul>

    <h2>İçerikleri nasıl hazırlıyoruz?</h2>
    <p>Konu özetleri, o sınıf ve dersin güncel MEB ders kitabında yer alan bilgilere dayanır; kitapta olmayan bilgi eklenmez. Anlatımlar, örnekler ve sorular özgün olarak yazılır; ders kitabından metin kopyalanmaz.</p>
    <p>Her içerik yayımlanmadan önce denetlenir: bilgiler kaynak kitapla karşılaştırılır, matematik sembolleri öğretim programındaki gösterimle yazılır, soruların tek doğru cevabı olduğu ve daha önce yayımlanan sorulardan farklı olduğu kontrol edilir.</p>
    <p>Öğretim programları ve kılavuzlar gibi resmî yayınlar kaynağı belirtilerek sunulur. Ders kitapları ve sınav kitapçıkları kopyalanmaz, resmî adreslerinden açılır. Ayrıntılar için <a href="/telif.html">Telif hakları ve kullanım</a> sayfasına bakabilirsiniz.</p>

    <h2>İlkelerimiz</h2>
    <ul>
      <li>Bütün içerikler ücretsizdir; üyelik gerekmez.</li>
      <li>Ziyaretçilerden kişisel bilgi istenmez. Günlük planlara yazılan adlar yalnız tarayıcıda kalır, sunucuya gönderilmez (<a href="/gizlilik.html">Gizlilik ve çerezler</a>).</li>
      <li>Site telefonda, tablette ve bilgisayarda çalışır.</li>
      <li>Bildirilen hatalar en kısa sürede düzeltilir.</li>
    </ul>

    <h2>Bize ulaşın</h2>
    <p>Soru, öneri ve hata bildirimleriniz için <a href="/iletisim.html">İletişim</a> sayfasını kullanabilir, <a href="/katki.html">Katkıda bulun</a> sayfasından da siteye destek olabilirsiniz.</p>
  </div>
</div>''', ())
GOVDE['iletisim.html'] = ('İletişim', 'Ders Kutusu ile iletişim: soru, öneri, hata bildirimi ve telif başvuruları için e-posta.', '''<div class="metin-sayfa">
  <div class="kap">
    <h1>İletişim</h1>
    <p>Ders Kutusu ile ilgili soru, öneri ve bildirimlerinizi e-postayla iletebilirsiniz. Sitede iletişim formu yoktur; e-posta adresiniz yalnız size yanıt vermek için kullanılır.</p>

    <h2>E-posta</h2>
    <p><a href="mailto:info@derskutusu.com">info@derskutusu.com</a></p>

    <h2>Ne için yazabilirsiniz?</h2>
    <ul>
      <li><strong>Hata bildirimi:</strong> konu özetinde, soruda, cevapta ya da plan dosyasında gördüğünüz yanlışı sayfanın adresiyle birlikte yazın. <a href="mailto:info@derskutusu.com?subject=Hata%20bildirimi">Hata bildir</a></li>
      <li><strong>İçerik önerisi:</strong> eklenmesini istediğiniz ders, konu ya da öğretmen dosyasını yazın. <a href="mailto:info@derskutusu.com?subject=%C4%B0%C3%A7erik%20%C3%B6nerisi">Öneri gönder</a></li>
      <li><strong>Telif:</strong> bir içeriğin size ait olduğunu düşünüyorsanız sayfa adresini ve gerekçenizi yazın; inceleyip gereğini yaparız. Ayrıntı: <a href="/telif.html">Telif hakları ve kullanım</a>.</li>
      <li><strong>Okul ağında erişim:</strong> site okulunuzun ağında ya da akıllı tahtada açılmıyorsa okulunuzun adını ve ekranda görünen uyarıyı yazın.</li>
    </ul>

    <p>Siteye başka yollarla destek olmak için <a href="/katki.html">Katkıda bulun</a> sayfasına, sitenin amacı ve içeriklerin nasıl hazırlandığı için <a href="/hakkimizda.html">Hakkımızda</a> sayfasına bakabilirsiniz.</p>
  </div>
</div>''', ())

# Arama dizinine girmeyecek araç/yönlendirme sayfaları (içerik değil, araç)
NOINDEX = {'sinif.html', 'ara.html', 'tahta.html', 'goruntule.html'}


def main():
    """Sabit iç sayfaları yazar. Yalnız doğrudan çalıştırılınca ya da ozet_uret.main() çağırınca; içe aktarma dosya yazmaz."""
    for ad, (baslik, aciklama, govde, betikler) in GOVDE.items():
        (PUBLIC / ad).write_text(sayfa(ad, baslik, aciklama, govde, betikler, kanonik=ad not in NOINDEX), encoding='utf-8')

    # Gizlilik ve 404: mevcut gövdeleri korunur, üst/alt yenilenir
    for ad, baslik, aciklama, kanonik in [('gizlilik.html', 'Gizlilik ve çerezler', 'Ders Kutusu gizlilik ve çerez bilgilendirmesi.', True),
                                          ('telif.html', 'Telif hakları ve kullanım koşulları', 'Ders Kutusu içeriklerinin telif hakları ve kullanım koşulları.', True),
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

    # Ana sayfa (gövdesi elle bakılır): reklam alanı alt bilginin üstünde; slot kimliği değişince burası da yenilenir
    yol = PUBLIC / 'index.html'
    eski = yol.read_text(encoding='utf-8')
    yeni = re.sub(r'<aside class="reklam"[^\n]*</aside>\n', '', eski).replace('<footer class="alt">', reklam_yeri('index.html') + '<footer class="alt">', 1)
    if yeni != eski:
        yol.write_text(yeni, encoding='utf-8')

    print('üretildi:', ', '.join([*GOVDE, 'gizlilik.html', 'telif.html', '404.html', 'index.html (reklam alanı)']))


if __name__ == '__main__':
    main()
