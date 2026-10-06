#!/usr/bin/env python3
"""KPSS derslerini, testlerini ve modül dizinini aynı kaynaktan üretir."""
import json, re
from pathlib import Path
from ozet_uret import e
from sayfa_uret import sayfa, BETIK_SURUMLERI
R=Path(__file__).resolve().parents[1]; P=R/'public'; V='202610060640'
GUIDES={
 'ortaogretim':'https://osym.gov.tr/2026-kpss-ortaogretim-kilavuz-ve-basvuru-bilgileri',
 'on-lisans':'https://osym.gov.tr/2026-kpss-on-lisans-kilavuz-ve-basvuru-bilgileri',
 'lisans':'https://www.osym.gov.tr/2026kpss-lisans-kilavuz-ve-basvuru-bilgileri'}
modules=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((R/'araclar/kpss').glob('*.json'))]
modules.sort(key=lambda m: m['ders']!='Türkçe')
for m in modules:  # veri denetimi: yanlış "dogru" sessizce sayfaya yazılmasın
 assert re.fullmatch(r'[a-z0-9-]+',m['id']),m['id']
 assert len({q['id'] for q in m['sorular']})==len(m['sorular']),m['id']+': soru kimliği yineleniyor'
 for q in m['sorular']:
  assert type(q['dogru']) is int and 0<=q['dogru']<len(q['secenekler'])<=5,q['id']+': "dogru" 0 tabanlı ve seçenek aralığında olmalı'
(P/'kpss').mkdir(exist_ok=True)
def wrap(path,title,desc,body):
 s=sayfa(path,title,desc,body,betikler=('kpss.js',))
 s=s.replace('</head>',f'<link rel="stylesheet" href="/kpss.css?v={V}">\n</head>')
 s=re.sub(r'(kpss\.js\?v=)\d+',lambda m:m[1]+V,s)
 (P/path).write_text(s,encoding='utf-8')
def sources():
 return '<section class="kp-sources"><h2>Kaynak ve kapsam</h2><p>Genel Yetenek kapsamı için ÖSYM’nin 2026 kılavuzları esas alınmıştır. Konu anlatımları ve sorular Ders Kutusu tarafından özgün hazırlanmıştır. Bu modül ortak temel çalışmasıdır; tam sınav denemesi değildir.</p><div class="kp-links">'+''.join(f'<a href="{url}" target="_blank" rel="noopener">ÖSYM · {label}</a>' for label,url in zip(['Ortaöğretim','Ön lisans','Lisans'],GUIDES.values()))+'</div><p class="kp-small">Kapsam kontrolü: 2 Ekim 2026. Sınav koşullarında kendi düzeyinizin güncel kılavuzunu izleyin.</p></section>'
warning='<p id="kp-storage-warning" class="kp-warning" role="status" hidden>Tarayıcı bu oturumda ilerlemeyi kaydedemiyor. Testi çözebilirsiniz; sayfadan ayrılınca yeni sonuçlarınız hatırlanmayabilir.</p>'
for m in modules:
 mid=m['id']; title=m['konu']; lesson=''; examples=''; questions=''
 for i,b in enumerate(m['bolumler'],1):
  lesson+=f'<section class="kp-section" id="konu-{i}"><span class="kp-number">{i:02}</span><h3>{e(b["baslik"])}</h3>'+''.join(f'<p>{e(p)}</p>' for p in b['metin'])+'</section>'
 for i,o in enumerate(m['ornekler'],1):
  examples+=f'<article class="kp-example"><span class="kp-eyebrow">Çözümlü örnek {i:02}</span><p>{e(o["soru"])}</p><details><summary>Çözümü göster</summary><p>{e(o["cevap"])}</p></details></article>'
 for i,q in enumerate(m['sorular'],1):
  choices=''.join(f'<label class="kp-option"><input type="radio" name="soru-{i}" value="{j}"><b>{"ABCDE"[j]}</b><span>{e(t)}</span></label>' for j,t in enumerate(q['secenekler']))
  questions+=f'<fieldset class="kp-question" data-id="{q["id"]}" data-topic="{e(q["alt_konu"])}" data-answer="{q["dogru"]}"><legend><span class="kp-eyebrow">Soru {i:02} · {e(q["alt_konu"])} · {e(q["seviye"])}</span><span class="kp-stem">{e(q["soru"])}</span></legend>{choices}<div class="kp-explanation" hidden><strong class="kp-verdict"></strong><p>{e(q["aciklama"])}</p></div></fieldset>'
 body=f'''<div class="kap kp-page" data-kp-module="{mid}" data-version="{m['surum']}">
 <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><a href="/kpss.html">KPSS</a><span>/</span><span>{e(m['ders'])}</span></nav>
 <header class="kp-hero"><span class="kp-eyebrow">KPSS · {e(m['ders'])} · Ortak temel</span><h1>{e(title)}</h1><p>{e(m['aciklama'])}</p><div class="kp-tags"><span>6 çözümlü örnek</span><span>10 özgün soru</span><span>Çözümlü geri bildirim</span></div><div class="kp-actions"><a class="dugme ana" href="#kp-lesson">Konuya başla</a><a class="dugme" href="#kp-test">Teste geç</a></div></header>
 {warning}
 <div class="kp-layout"><div class="kp-main"><section id="kp-lesson"><div class="kp-heading"><span class="kp-eyebrow">01 · ÖĞREN</span><h2>Konu anlatımı</h2></div>{lesson}
 <div class="kp-learn"><button class="dugme" id="kp-learned" type="button" aria-pressed="false">Konuyu çalıştım</button><span id="kp-learn-status" class="kp-small"></span></div></section>
 <section class="kp-block"><div class="kp-heading"><span class="kp-eyebrow">02 · UYGULA</span><h2>Çözümlü örnekler</h2><p>Önce kendin yanıtla, sonra çözümle karşılaştır.</p></div>{examples}</section>
 <section class="kp-block" id="kp-test"><div class="kp-heading"><span class="kp-eyebrow">03 · KENDİNİ DENE</span><h2>10 soruluk konu testi</h2><p>Her sorunun bir doğru cevabı var. Testi bitirince doğru, yanlış ve boş cevaplarını açıklamalarıyla görebilirsin.</p></div>
 <div class="kp-test-toolbar"><label for="kp-duration">Çalışma süresi <select id="kp-duration"><option value="0">Süresiz</option><option value="600">10 dakika</option><option value="900">15 dakika</option><option value="1200">20 dakika</option></select></label><button class="dugme ana" type="button" id="kp-start">Testi başlat</button><output id="kp-timer" aria-live="off" aria-label="Kalan süre">Süresiz</output><span id="kp-answered" aria-live="polite">0 / 10 yanıtlandı</span></div>
 <p class="kp-small">Süreli çalışmada sayaç bitince test değerlendirilir. Bu süre seçimi alıştırma içindir.</p><noscript><p>Çevrim içi test için JavaScript gerekir. Aşağıdaki PDF’lerle çalışabilirsiniz.</p></noscript>
 <form id="kp-quiz"><fieldset id="kp-question-set" disabled><legend class="kp-sr">Test soruları</legend>{questions}</fieldset><div class="kp-actions"><button class="dugme ana" id="kp-finish" type="submit" disabled>Testi bitir ve değerlendir</button><button class="dugme" id="kp-retry" type="button" hidden>Yanlış ve boşları tekrar çöz</button><button class="dugme" id="kp-reset" type="button" hidden>Tüm testi yeniden çöz</button></div></form><div id="kp-result" class="kp-result" tabindex="-1" role="status" hidden></div>
 </section></div>
 <aside class="kp-sidebar"><div class="kp-side-card"><span class="kp-eyebrow">ÇALIŞMA ROTASI</span><h2>Adım adım ilerle</h2><ol><li><a href="#kp-lesson">Konuyu oku</a></li><li>Örnekleri kendin çöz</li><li><a href="#kp-test">Testle kontrol et</a></li><li>Yanlış ve boşlara dön</li></ol><p class="kp-small">İlerlemen bu tarayıcıda saklanır. Başka cihazlara aktarılmaz; tarayıcı verilerini silersen sıfırlanır.</p></div><div class="kp-side-card"><h2>Yazdırarak çalış</h2><p>10 soruluk testi PDF olarak indir.</p><div class="kp-downloads"><a class="dugme" href="/kpss/pdf/{mid}.pdf" download>Test PDF · Cevapsız</a><a class="dugme" href="/kpss/pdf/{mid}-cevapli.pdf" download>Test PDF · Cevaplı</a></div></div></aside></div>{sources()}</div>'''
 wrap(f'kpss/{mid}.html',f'KPSS {m["ders"]}: {title}',m['aciklama'],body)
cards=''
for m in modules:
 cards+=f'''<article class="kp-module-card" data-module="{m['id']}"><span class="kp-eyebrow">{e(m['ders'])} · 01</span><h2>{e(m['konu'])}</h2><p>{e(m['aciklama'])}</p><div class="kp-tags"><span>6 çözümlü örnek</span><span>10 soruluk test</span><span>2 PDF</span></div><p class="kp-progress">Henüz çalışılmadı</p><a class="dugme ana" href="/kpss/{m['id']}.html">Çalışmaya başla <span aria-hidden="true">→</span></a></article>'''
body=f'''<div class="kap kp-page" id="kp-home"><nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span>/</span><span>KPSS</span></nav><header class="kp-hero"><span class="kp-eyebrow">KPSS HAZIRLIK · GENEL YETENEK</span><h1>Küçük adımlarla,<br>sağlam bir temel.</h1><p>Konuyu öğren, çözümlü örneklerle pekiştir, testte kendini dene. Türkçe ve matematik için ilk iki çalışma modülü hazır.</p><div class="kp-tags"><span>2 konu anlatımı</span><span>12 çözümlü örnek</span><span>20 özgün soru</span><span>Tamamen ücretsiz</span></div><a class="dugme ana" href="#kp-modules">Konuları keşfet <span aria-hidden="true">↓</span></a></header>{warning}
<section class="kp-preferences"><div><label for="kp-level">Hazırlandığın düzey</label><select id="kp-level"><option value="ortaogretim">Ortaöğretim</option><option value="on-lisans">Ön lisans</option><option value="lisans">Lisans</option></select><a id="kp-guide" href="{GUIDES['ortaogretim']}" target="_blank" rel="noopener">ÖSYM 2026 kılavuzunu aç ↗</a></div><div><strong id="kp-total">0 / 2 test tamamlandı</strong><p class="kp-small">İlerlemen yalnız bu tarayıcıda saklanır.</p></div><p class="kp-level-note">İlk iki modül üç düzey için ortak temel konuları içerir. Düzey seçimi kılavuz bağlantısını ve tercihini değiştirir; bu modüllerin soruları aynıdır.</p></section>
<section id="kp-modules" class="kp-block"><div class="kp-heading"><span class="kp-eyebrow">BUGÜN NE ÇALIŞACAKSIN?</span><h2>Hazır çalışma modülleri</h2><p>Konu anlatımı, çözümlü örnekler, çevrim içi test ve cevaplı/cevapsız PDF bir arada.</p></div><div class="kp-module-grid">{cards}</div></section>
<section class="kp-next"><h2>Sıradaki içerikler</h2><p>Türkçe ve matematikte yeni konularla devam edilecek. Tarih, coğrafya ve vatandaşlık içerikleri henüz yayımlanmadı. AGS ve ÖABT bu başlangıç paketinin kapsamında değildir.</p></section>{sources()}</div>'''
wrap('kpss.html','KPSS Hazırlık','KPSS Türkçe ve matematik konu anlatımları, çözümlü örnekler, özgün testler ve ücretsiz PDF dosyaları.',body)
(P/'veri/kpss.json').write_text(json.dumps({'guncelleme':'2026-10-02','moduller':[{k:m[k] for k in ('id','ders','konu','aciklama','duzeyler','surum')} for m in modules]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Ana sayfa ortak başlığın kaynağıdır. Mevcut içeriklerin gövdelerine dokunulmaz.
for p in P.rglob('*.html'):
 s=p.read_text(encoding='utf-8'); old=s
 def nav_kpss(match):
  nav=match[0]
  if 'href="/kpss.html"' not in nav:
   nav=re.sub(r'(<a href="/?sinav\.html">Sınavlar</a>)',r'\1\n      <a href="/kpss.html">KPSS</a>',nav,count=1)
  return nav
 s=re.sub(r'<nav[^>]*id="ana-menu"[^>]*>.*?</nav>',nav_kpss,s,flags=re.S)
 # arama.js sürümünün tek kaynağı sayfa_uret.BETIK_SURUMLERI'dir (harfli sürümler de olabilir).
 s=re.sub(r'(arama\.js\?v=)[^"\'&]+',lambda m:m[1]+BETIK_SURUMLERI['arama.js'],s)
 if s!=old:p.write_text(s,encoding='utf-8')
p=P/'sitemap.xml'; s=p.read_text(encoding='utf-8')
for slug in ['kpss.html',*[f'kpss/{m["id"]}.html' for m in modules]]:
 url='https://derskutusu.com/'+slug
 if url not in s:s=s.replace('</urlset>',f'  <url><loc>{url}</loc><lastmod>2026-10-02</lastmod></url>\n</urlset>')
p.write_text(s,encoding='utf-8')
print(f'KPSS: {len(modules)} modül, {sum(len(m["ornekler"]) for m in modules)} örnek, {sum(len(m["sorular"]) for m in modules)} soru üretildi.')
