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


# Çerezsiz ziyaret sayacı (Cloudflare Web Analytics; kişisel veri toplamaz, gizlilik.html'de açıklanır)
SAYAC = '''<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "fffb5e8a709947ee9ba14ea753d96275"}'></script><!-- End Cloudflare Web Analytics -->'''


def sayfa(ad, baslik, aciklama, govde, betikler=(), kanonik=True):
    kan = f'<link rel="canonical" href="https://derskutusu.com/{ad}">\n' if kanonik else '<meta name="robots" content="noindex">\n'
    js = ''.join(f'<script src="/{b}?v={SURUM}"></script>\n' for b in ('ortak.js', *betikler, 'arama.js', 'tahta.js'))
    return f'''<!doctype html>
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

{js}{SAYAC}
</body>
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
    'yazili.html': ('Ortak yazılı senaryoları', 'ÖDSGM 1. dönem ortak yazılı konu-soru dağılım senaryoları: hangi öğrenme çıktısından kaç soru çıkacak.', '''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a id="y-yol-sinif" href="/#siniflar">Sınıf</a><span aria-hidden="true">/</span><span>Ortak yazılı</span></nav>
      <h1 id="y-baslik">Ortak yazılı senaryoları</h1>
      <p>1. dönem, 2026-2027. Okulun zümresi senaryolardan birini seçer; tabloda her öğrenme çıktısından kaç soru çıkacağı yazar.</p>
      <div class="g-dugmeler y-ust" id="y-dugmeler"></div>
      <nav class="sinif-gecis" id="y-siniflar" aria-label="Sınıflar"></nav>
    </div>
  </section>
  <section class="bolum y-bolum">
    <div class="kap">
      <div class="y-secim">
        <div class="sekmeler" id="y-yazililar" role="group" aria-label="Yazılı"></div>
        <div class="cipler" id="y-senaryolar" role="group" aria-label="Senaryo"></div>
        <label class="y-yalniz"><input type="checkbox" id="y-yalniz" checked> Yalnız soru çıkan öğrenme çıktıları</label>
      </div>
      <div class="y-kaydir" id="y-tablo"></div>
    </div>
  </section>''', ('yazili.js',)),
    'tahta.html': ('Akıllı tahta', 'Tarayıcıda çalışan akıllı tahta: kalem, fosforlu kalem, silgi, renkler, kareli ve çizgili zemin, sayfalar.', '''  <section class="tahta-sayfa">
    <div class="kap tahta-ustbar">
      <h1>Akıllı tahta</h1>
      <label class="gizli" for="t-zemin">Zemin</label>
      <select id="t-zemin" aria-label="Zemin"><option value="kareli">Kareli</option><option value="cizgili">Çizgili</option><option value="noktali">Noktalı</option><option value="">Düz</option></select>
      <button class="dugme" type="button" id="t-onceki" aria-label="Önceki sayfa">‹</button>
      <span id="t-sayfa" aria-live="polite">1 / 1</span>
      <button class="dugme" type="button" id="t-sonraki" aria-label="Sonraki ya da yeni sayfa">›</button>
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
          <a class="dugme" data-sosyal="youtube" target="_blank" rel="noopener" hidden><svg><use href="#s-youtube"/></svg>YouTube</a>
          <a class="dugme" data-sosyal="instagram" target="_blank" rel="noopener" hidden><svg><use href="#s-instagram"/></svg>Instagram</a>
          <a class="dugme" data-sosyal="facebook" target="_blank" rel="noopener" hidden><svg><use href="#s-facebook"/></svg>Facebook</a>
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
    """Sınavlar sayfası (LGS, YKS): veri/sinavlar.json + veri/belgeler.json'dan durağan HTML."""
    import html as _h
    import json as _j
    sv = _j.loads((PUBLIC / 'veri' / 'sinavlar.json').read_text(encoding='utf-8'))
    bl = {b['kimlik']: b for g in _j.loads((PUBLIC / 'veri' / 'belgeler.json').read_text(encoding='utf-8'))['gruplar'] for b in g['belgeler']}
    e = _h.escape
    gecis = ''.join(f'<a href="#{x["kimlik"]}">{e(x["ad"])}</a>' for x in sv['sinavlar'])
    bolumler = ''
    for n, x in enumerate(sv['sinavlar']):
        lgs = x['kimlik'] == 'lgs'
        kartlar = ''
        for o in x['oturumlar']:
            satir = ''.join(
                f'<tr><td><a href="/icerikler.html?{"sinif=8&amp;" if lgs else ""}ders={t[2]}">{e(t[0])}</a></td><td class="sayi">{t[1]}</td></tr>'
                for t in o['testler'])
            kartlar += (f'<article class="kart sinav-oturum"><h3>{e(o["ad"])}</h3>'
                        f'<p class="sinav-ozet"><b>{o["toplam"]}</b> soru · <b>{o["sure"]}</b> dakika</p>'
                        f'<table class="sinav-tablo"><thead><tr><th>Test</th><th class="sayi">Soru</th></tr></thead><tbody>{satir}</tbody></table></article>')
        belge = ''.join(
            f'<li><a href="/goruntule.html?b={k}">{e(bl[k]["baslik"])}</a><span>{e(bl[k].get("kaynak", ""))}</span></li>'
            for k in x['belgeler'] if k in bl)
        if lgs:
            hazirlik = ('<li><a href="/sinif.html?no=8">8. sınıfın bütün dersleri</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=Konu%20anlat%C4%B1m%C4%B1">8. sınıf konu özetleri</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=Yaz%C4%B1l%C4%B1%20senaryosu">8. sınıf ortak yazılı senaryoları</a></li>')
        else:
            hazirlik = ''.join(f'<li><a href="/sinif.html?no={k}">{k}. sınıfın bütün dersleri</a></li>' for k in x['siniflar'])
            hazirlik += '<li><a href="/icerikler.html?tur=Ders%20kitab%C4%B1">Lise ders kitapları</a></li>'
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
    return f'''  <section class="sayfa-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Sınavlar</span></nav>
      <h1>Sınavlar</h1>
      <p>LGS ve YKS'nin oturumları, testleri ve soru sayıları; çıkmış sorular, kılavuzlar ve sitedeki hazırlık kaynakları. Bilgiler resmî belgelerden alınmıştır; yeni yılın belgeleri yayımlanınca güncellenir.</p>
      <nav class="sinif-gecis" aria-label="Sınavlar">{gecis}</nav>
    </div>
  </section>
{bolumler}'''


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
  </section>''', ('planlar.js',))

GOVDE['sinav.html'] = ('Sınavlar: LGS ve YKS', 'LGS ve YKS: oturumlar, testler, soru sayıları ve süreler; çıkmış sorular, kılavuzlar ve hazırlık kaynakları.', _sinav_govde(), ())

for ad, (baslik, aciklama, govde, betikler) in GOVDE.items():
    (PUBLIC / ad).write_text(sayfa(ad, baslik, aciklama, govde, betikler), encoding='utf-8')

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

print('üretildi:', ', '.join([*GOVDE, 'gizlilik.html', 'telif.html', '404.html']))
