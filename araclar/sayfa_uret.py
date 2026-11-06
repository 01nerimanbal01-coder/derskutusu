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
BETIK_SURUMLERI = {'goruntule.js': '20261106-1', 'belgeler.js': '20261104-3', 'planlar.js': '20261105-1', 'agac.js': '20261104-3', 'yazili.js': '20261010-1', 'ortak.js': '20261106-3', 'tahta.js': '20261106-1', 'etkinlik.js': '20261017-9', 'arama.js': '20261104-2', 'kutuphane.js': '20261104-2', 'kelime.js': '20261104-2', 'arapca.js': '20261104-2', 'yazili-cikti.js': '79d67c33e4', 'yazili-duzen.js': '20261104-3', 'asds.js': '20261104-7'}

simgeler = ana[ana.index('<!-- Simge takımı'):ana.index('</svg>\n\n<header') + len('</svg>')]
ust = ana[ana.index('<header class="ust">'):ana.index('</header>') + len('</header>')]
alt = ana[ana.index('<footer class="alt">'):ana.index('</footer>') + len('</footer>')]
# İç sayfalarda bölüm bağlantıları ana sayfaya gider
ust = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'(<a\b[^>]*\bhref=")#', r'\1/#', ust))
alt = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', re.sub(r'(<a\b[^>]*\bhref=")#', r'\1/#', alt))


# Çerezsiz ziyaret sayacı (Cloudflare Web Analytics; kişisel veri toplamaz, gizlilik.html'de açıklanır)
SAYAC = '''<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "fffb5e8a709947ee9ba14ea753d96275"}'></script><!-- End Cloudflare Web Analytics -->'''


# Site ağacı (kullanıcı 11.10.2026): her sayfa kendi dalının kitlesini taşır (üst menü vurgusu, kayan şerit süzgeci).
SINIF_DIZIN_SAYFALARI = tuple(f'sinif-{s}.html' for s in range(5, 13))
KITLE_OGRENCI = ('ogrenci.html', 'kelime.html', 'arapca.html', 'sinav.html', *SINIF_DIZIN_SAYFALARI)
KITLE_OGRETMEN = ('ogretmen.html', 'planlar.html', 'yazili.html', 'belgeler.html', 'kpss.html', 'ders-dagitim.html')
AGAC_CSS = '<link rel="stylesheet" href="/agac.css?v=20261106-2">'


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
REKLAM_SAYFALARI = {'index.html': 'ana', 'ogrenci.html': 'ana', 'ogretmen.html': 'ana', 'icerikler.html': 'ana',
                    **{ad: 'ana' for ad in SINIF_DIZIN_SAYFALARI}}
# Etkileşimli araç, indirme, arama, yasal bildirim, iletişim ve dış resmî belge sayfalarına AdSense betiği konmaz;
# yalnız özgün konu anlatımları, çalışma kâğıtları ve akademik dizin sayfalarında yer alır.
ADSENSE_HARIC = {
    'tahta.html', 'goruntule.html', 'ders-dagitim.html', 'ders-dagitim-uygulama.html',
    'planlar.html', 'yazili.html', 'kelime.html', 'arapca.html',
    'belgeler.html', 'gizlilik.html', 'telif.html', 'iletisim.html', 'katki.html',
    '404.html', 'okul-bildir.html', 'ara.html', 'sinif.html',
}
ADSENSE_UST_KOD = (
    '<script>(window.adsbygoogle=window.adsbygoogle||[]).requestNonPersonalizedAds=1;</script>\n'
    f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={REKLAM_MUSTERI}" crossorigin="anonymous"></script>\n'
)


def reklam_yeri(ad):
    """Sayfanın reklam alanı (alt bilginin hemen üstü); reklam konmayan sayfada ya da slot kimliği yokken boş."""
    yer = 'ozet' if ad.startswith('ozet/') else REKLAM_SAYFALARI.get(ad)
    if not yer:
        return ''
    slot = REKLAM_SLOTLAR.get(yer, '')
    if not slot:
        return ''
    birim = (f'<ins class="adsbygoogle" style="display:block" data-ad-client="{REKLAM_MUSTERI}" data-ad-slot="{slot}" data-ad-format="auto" '
             'data-full-width-responsive="true" data-tag-for-age-treatment="1"></ins>')
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
    adsense_ust = ADSENSE_UST_KOD if (kanonik and ad not in ADSENSE_HARIC) else ''
    js = ''.join(f'<script src="/{b}?v={BETIK_SURUMLERI.get(b, SURUM)}"></script>\n' for b in ('ortak.js', *betikler, 'arama.js', 'tahta.js'))
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
{adsense_ust}<link rel="icon" href="/favicon.ico" sizes="any">
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

def _metin_bicimle(metin):
    """JSON başlık/açıklamalarındaki {us:..}, {alt:..}, {ar:..}, {koyu:..} sembollerini güvenli HTML'e çevirir."""
    import html as _h
    s = _h.escape(str(metin or ''))
    s = re.sub(r'\{us:([^{}|]*)\|([^{}]+)\}', lambda m: f'{m[1]}<sup>{m[2]}</sup>', s)
    s = re.sub(r'\{alt:([^{}|]*)\|([^{}]+)\}', lambda m: f'{m[1]}<sub>{m[2]}</sub>' if m[2] else f'<sub>{m[1]}</sub>', s)
    s = re.sub(r'\{ar:([^{}]+)\}', r'<bdi lang="ar" dir="rtl">\1</bdi>', s)
    s = re.sub(r'\{koyu:([^{}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\{(?:vurgu|egik|i):([^{}]+)\}', r'<em>\1</em>', s)
    return s


def _sinif_dizin_seridi(aktif=None):
    etiketler = {
        5: '5. Sınıf Konu Dizini', 6: '6. Sınıf Konu Dizini',
        7: '7. Sınıf Konu Dizini', 8: '8. Sınıf · LGS Konu Dizini',
        9: '9. Sınıf Konu Dizini', 10: '10. Sınıf Konu Dizini',
        11: '11. Sınıf Konu Dizini', 12: '12. Sınıf · YKS Konu Dizini',
    }
    baglar = ''.join(
        f'<a href="/sinif-{s}.html"' + (' aria-current="page"' if s == aktif else '') + f'>{etiketler[s]}</a>'
        for s in range(5, 13)
    )
    return f'<nav class="sinif-dizin-serit" aria-label="Sınıf ders ve konu dizinleri"><strong>Sınıf Konu ve Çalışma Kâğıdı Dizinleri:</strong>{baglar}</nav>'


def _kutuphane_onizleme_kartlari():
    import html as _h
    import json as _j
    ic = _j.loads((PUBLIC / 'veri' / 'icerikler.json').read_text(encoding='utf-8')).get('icerikler', [])
    secilen = []
    for s in range(5, 13):
        ozetler = [x for x in ic if x.get('sinif') == s and x.get('tur') == 'Konu anlatımı' and x.get('goruntule')]
        calismalar = [x for x in ic if x.get('sinif') == s and x.get('tur') == 'Çalışma kâğıdı' and x.get('goruntule')]
        secilen.extend(ozetler[:2])
        secilen.extend(calismalar[:1])
    kartlar = []
    for x in secilen:
        adres = '/' + str(x['goruntule']).lstrip('/')
        kartlar.append(
            f'<article class="kart">'
            f'<p class="ust-baslik">{_h.escape(str(x.get("tur", "")))} · {x.get("sinif")}. Sınıf</p>'
            f'<h3><a href="{_h.escape(adres, quote=True)}">{_metin_bicimle(x.get("baslik", ""))}</a></h3>'
            f'<p>{_metin_bicimle(x.get("aciklama", ""))}</p>'
            f'</article>'
        )
    return '\n        '.join(kartlar)


def _belgeler_govde():
    import html as _h
    import json as _j
    veri = _j.loads((PUBLIC / 'veri' / 'belgeler.json').read_text(encoding='utf-8'))
    gruplar = veri.get('gruplar', [])
    gecis = ''.join(f'<a href="#{_h.escape(g["kimlik"], quote=True)}">{_h.escape(g["ad"])}</a>' for g in gruplar)
    bolumler = []
    for idx, g in enumerate(gruplar):
        kartlar = []
        for b in g.get('belgeler', []):
            hedef = b.get('goruntule') or b.get('dosya') or b.get('baglanti') or ''
            if hedef and not hedef.startswith(('http://', 'https://', '/')):
                hedef = '/' + hedef
            dis = hedef.startswith(('http://', 'https://'))
            ek_attr = ' target="_blank" rel="noopener"' if dis else ''
            kaynak = _h.escape(b.get('kaynak', 'MEB'))
            kartlar.append(
                f'<article class="kart">'
                f'<p class="ust-baslik">{kaynak}</p>'
                f'<h3><a href="{_h.escape(hedef, quote=True)}"{ek_attr}>{_metin_bicimle(b.get("baslik", ""))}</a></h3>'
                f'<p>{_metin_bicimle(b.get("aciklama", ""))}</p>'
                f'</article>'
            )
        zemin = ' koyu-zemin' if idx % 2 else ''
        bolumler.append(
            f'  <section class="bolum{zemin}" id="{_h.escape(g["kimlik"], quote=True)}">\n'
            f'    <div class="kap">\n'
            f'      <div class="bolum-bas"><div><h2>{_h.escape(g["ad"])}</h2><p>{_h.escape(g.get("aciklama", ""))}</p></div></div>\n'
            f'      <div class="kartlar">{"".join(kartlar)}</div>\n'
            f'    </div>\n'
            f'  </section>'
        )
    rehber = (
        '  <section class="bolum">\n'
        '    <div class="kap">\n'
        '      <div class="statik-rehber">\n'
        '        <h2>Resmî Eğitim Belgeleri Nasıl Kullanılır?</h2>\n'
        '        <p>Millî Eğitim Bakanlığı (MEB), Talim ve Terbiye Kurulu Başkanlığı, Ölçme, Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü (ÖDSGM), Din Öğretimi Genel Müdürlüğü (DÖGM) ve ÖSYM tarafından yayımlanan öğretim programları, çerçeve yıllık planlar, ders kitapları ve ortak yazılı konu-soru dağılım tabloları okul içi akademik planlamanın temel dayanağıdır. Ders Kutusu bu sayfada öğretmenlerin, zümre başkanlarının ve öğrencilerin ihtiyaç duyduğu güncel mevzuat ve program belgelerini tek bir düzenli dizinde bir araya getirir.</p>\n'
        '        <p>Türkiye Yüzyılı Maarif Modeli kapsamında güncellenen ders öğretim programlarını incelerken öğrenme çıktıları, süreç bileşenleri, içerik çerçevesi ve ölçme-değerlendirme açıklamaları birlikte değerlendirilmelidir. Zümre toplantılarında ortak yazılı senaryosu seçerken ilgili dönemin ÖDSGM konu-soru dağılım tablosu esas alınır; günlük ve yıllık ders planları ise çerçeve planlardaki hafta dağılımıyla eşleştirilir. Doğrudan sınıf ve ders bazlı özgün konu anlatımlarımıza ulaşmak için aşağıdaki sınıf dizinlerini kullanabilirsiniz.</p>\n'
        '      </div>\n'
        f'      {_sinif_dizin_seridi()}\n'
        '    </div>\n'
        '  </section>'
    )
    return (
        '  <section class="sayfa-bas">\n'
        '    <div class="kap">\n'
        '      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><span>Resmî belgeler</span></nav>\n'
        '      <h1>Resmî belgeler ve öğretim programları</h1>\n'
        '      <p>MEB, ÖDSGM, DÖGM ve ÖSYM’nin yayımladığı öğretim programları, kılavuzlar, ortak yazılı tabloları ve ders kitapları tek yerde. Bağlantılar resmî kaynaklarıyla birlikte güncel sürümüyle sunulur.</p>\n'
        f'      <nav class="sinif-gecis" id="grup-gecis" aria-label="Belge grupları">{gecis}</nav>\n'
        '    </div>\n'
        '  </section>\n'
        f'  <div id="belge-gruplari">\n{chr(10).join(bolumler)}\n  </div>\n'
        f'{rehber}'
    )


SINIF_REHBER_METINLERI = {
    5: (
        '5. Sınıf Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '5. sınıf Türkçe, Matematik, Fen Bilimleri, Sosyal Bilgiler, İngilizce, Din Kültürü ve seçmeli dersler için hafta hafta özgün konu anlatımları ve PDF çalışma kâğıtları.',
        'Ortaokula geçişin ilk basamağı olan 5. sınıf, Türkiye Yüzyılı Maarif Modeli (TYMM) kapsamında öğrencilerin temel kavramları görsel modellerle, günlük yaşam bağlamlarıyla ve sorgulayıcı etkinliklerle öğrendiği kritik bir dönemdir. Türkçe dersinde dinleme ve okuma stratejileri ile bağlamdan söz varlığı geliştirme; Matematik dersinde temel geometrik çizimler, açılar, doğal sayılar ve kesir modelleri; Fen Bilimleri dersinde Güneş, Dünya ve Ay sistemi, kuvvetin ölçülmesi ve canlılar dünyası; Sosyal Bilgiler dersinde ise birlikte yaşama kültürü, hak-sorumluluk bilinci ve coğrafi farkındalık öne çıkar. Aşağıdaki dizinde 5. sınıfa ait tüm zorunlu ve seçmeli derslerin 37 haftalık konu anlatımlarını ve yazdırılabilir PDF çalışma kâğıtlarını hafta sırasıyla doğrudan açabilirsiniz.',
    ),
    6: (
        '6. Sınıf Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '6. sınıf tüm dersler için MEB yıllık plan sırasıyla hazırlanmış haftalık konu özetleri, çözümlü örnekler, etkileşimli etkinlikler ve PDF çalışma kâğıtları.',
        '6. sınıf programı, ortaokulun temel akademik becerilerini soyut düşünme ve analitik problem çözme basamağına taşır. Matematikte çarpanlar-katlar, bölünebilme kuralları, kesirlerle işlemler, ondalık gösterim ve cebirsel ifadelerin temeli atılırken; Fen Bilimleri dersinde Güneş sistemi ve tutulmalar, insan vücudundaki sistemler, kuvvet-hareket ve madde-ısı konuları deneysel gözlemlerle işlenir. Türkçe dersinde metin türleri, anlam ilişkileri ve dil yapıları derinleşir; Sosyal Bilgiler ve İngilizce derslerinde ise tarihsel süreklilik ile günlük iletişim kalıpları pekiştirilir. Bu sayfada 6. sınıf derslerinin tamamı için hazırlanan özgün haftalık konu anlatımlarına ve cevaplı/cevapsız çalışma kâğıtlarına tek tıklamayla ulaşabilirsiniz.',
    ),
    7: (
        '7. Sınıf Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '7. sınıf Türkçe, Matematik, Fen Bilimleri, Sosyal Bilgiler, İngilizce ve Din Kültürü haftalık konu anlatımları, çözümlü sorular ve PDF çalışma kâğıtları.',
        '7. sınıf, hem ortaokul müfredatının en yoğun kavramsal konularını barındıran hem de 8. sınıftaki LGS hazırlığının sağlam temelini oluşturan kilit bir öğretim yılıdır. Matematik dersinde tam sayılarla işlemler, rasyonel sayılar, doğrusal denklemler, oran-orantı, yüzdeler ve çember-daire konuları doğrudan üst kademe sayısal muhakemenin omurgasını kurar. Fen Bilimleri dersinde uzay araştırmaları, hücre ve bölünmeler, kuvvet-iş-enerji ilişkisi, saf maddeler ve ışık üniteleri; Türkçe dersinde fiiller, zarflar, paragraf yorumu ve anlatım bozuklukları; Sosyal Bilgiler dersinde ise iletişim, Osmanlı kültür mirası, nüfus ve ekonomi konuları ayrıntılı olarak ele alınır. Aşağıdaki ders listelerinden her haftanın ders özetini ve çalışma föyünü doğrudan inceleyebilirsiniz.',
    ),
    8: (
        '8. Sınıf · LGS Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '8. sınıf ve LGS hazırlık için Matematik, Türkçe, Fen Bilimleri, T.C. İnkılap Tarihi, İngilizce ve Din Kültürü haftalık konu anlatımları ile PDF çalışma kâğıtları.',
        '8. sınıf, ortaokul öğreniminin tamamlandığı ve Liselere Geçiş Sistemi (LGS) merkezî sınavına hazırlığın sistemli biçimde yürütüldüğü dönüm noktasıdır. Sınavda ve okul yazılılarında başarı; ezberlenmiş formüller yerine kavramların neden-sonuç ilişkisiyle anlaşılmasına, grafik-tablo okuma becerisine ve bağlam temelli soruların doğru analiz edilmesine dayanır. Matematikte çarpanlar-katlar, üslü ve kareköklü ifadeler, veri analizi, olasılık, cebirsel ifadeler, doğrusal denklemler ve eşitsizlikler; Fen Bilimlerinde mevsimler-iklim, DNA ve genetik kod, basınç, madde ve endüstri ile basit makineler; Türkçede fiilimsiler, cümlenin ögeleri ve sözel mantık; T.C. İnkılap Tarihi, İngilizce ve Din Kültüründe ise ünite kazanımlarının tamamı aşağıdaki hafta hafta konu özetleri ve çalışma kâğıtlarıyla eksiksiz kapsanır.',
    ),
    9: (
        '9. Sınıf Lise Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '9. sınıf Türk Dili ve Edebiyatı, Matematik, Fizik, Kimya, Biyoloji, Tarih, Coğrafya, İngilizce ve Din Kültürü haftalık konu anlatımları dizini.',
        'Liseye başlangıç yılı olan 9. sınıf, Türkiye Yüzyılı Maarif Modeli ortaöğretim programlarıyla disiplinler arası bilimsel düşünme, akademik okuryazarlık ve TYT temelinin kurulduğu evredir. Ortaokul fen bilimleri bu sınıfta Fizik, Kimya ve Biyoloji olarak üç bağımsız laboratuvar bilimine ayrılır; Sosyal Bilgiler birikimi ise Tarih ve Coğrafya derslerinde birincil kaynak analizi ve mekânsal sentez becerisine dönüşür. Türk Dili ve Edebiyatı dersinde edebî metin çözümlemesi ve yazma süreci; Matematik dersinde gerçek sayılar, nicelikler ve değişimler, algoritmik düşünme ve üçgen geometrisi öne çıkar. Aşağıdaki tam dizinden 9. sınıfın bütün ortak ve seçmeli ders özetlerine doğrudan erişebilirsiniz.',
    ),
    10: (
        '10. Sınıf Lise Konu Anlatımları ve Çalışma Kâğıtları Dizini',
        '10. sınıf tüm lise dersleri için MEB yıllık planına uyumlu haftalık konu anlatımları, çözümlü örnekler ve etkileşimli etkinlikler dizini.',
        '10. sınıf, lise müfredatının derinleştiği ve Yükseköğretim Kurumları Sınavı (YKS) Temel Yeterlilik Testi (TYT) konularının büyük bölümünün tamamlandığı kritik bir yıldır. Bu sınıfta programa ilk kez katılan Felsefe dersi öğrencilere kavram analizi, argüman kurma ve eleştirel sorgulama perspektifi kazandırır. Matematikte sayma-olasılık, fonksiyonlar, polinomlar, ikinci dereceden denklemler ve dörtgenler-katı cisimler; Fizikte elektrik-manyetizma, basınç-kaldırma kuvveti, dalgalar ve optik; Kimyada kimyanın temel kanunları, mol kavramı, karışımlar ve asitler-bazlar; Biyolojide hücre bölünmeleri, kalıtım ve ekosistem ekolojisi; Edebiyat, Tarih ve Coğrafyada ise dönem ve mekân analizleri hafta hafta özgün anlatımlarla sunulur.',
    ),
    11: (
        '11. Sınıf AYT ve Lise Konu Anlatımları Dizini',
        '11. sınıf Matematik, Fizik, Kimya, Biyoloji, Türk Dili ve Edebiyatı, Tarih, Coğrafya, Felsefe ve seçmeli dersler haftalık konu anlatımları.',
        '11. sınıf, öğrencilerin ilgi ve hedefledikleri yükseköğretim alanlarına göre akademik uzmanlaşmaya geçtiği ve YKS Alan Yeterlilik Testleri (AYT) konularının omurgasını oluşturan öğretim yılıdır. Matematikte trigonometri, analitik geometri, fonksiyonlarda uygulamalar, denklem sistemleri ve çember-daire; Fizikte vektörler, bağıl hareket, Newton’un hareket yasaları, iş-güç-enerji, itme-momentum ve elektrik-manyetizma; Kimyada modern atom teorisi, gazlar, sıvı çözeltiler, kimyasal tepkimelerde enerji-hız-denge; Biyolojide insan fizyolojisi ve komünite-popülasyon ekolojisi; Türk Dili ve Edebiyatı, Tarih, Coğrafya ve Felsefede ise analitik dönem incelemeleri aşağıdaki haftalık konu anlatımlarında adım adım çözümlü örneklerle işlenir.',
    ),
    12: (
        '12. Sınıf · YKS (TYT · AYT) Konu Anlatımları Dizini',
        '12. sınıf ve YKS hazırlık için Matematik, Fizik, Kimya, Biyoloji, Edebiyat, T.C. İnkılap Tarihi, Coğrafya, İngilizce ve Din Kültürü haftalık konu anlatımları.',
        '12. sınıf, ortaöğretim sürecinin tamamlandığı ve üniversiteye geçiş sınavı YKS (TYT, AYT ve YDT) hazırlığının ileri düzey konularla bütünleştiği son kademedir. Matematikte üstel ve logaritmik fonksiyonlar, diziler, trigonometri dönüşümleri, limit-süreklilik, türev ve integral; Fizikte çembersel hareket, basit harmonik hareket, dalga mekaniği, atom fiziği ve modern fizik; Kimyada kimya ve elektrik, karbon kimyasına giriş ve organik bileşikler; Biyolojide genden proteine, canlılarda enerji dönüşümleri ve bitki biyolojisi; Türk Dili ve Edebiyatı, T.C. İnkılap Tarihi ve Atatürkçülük ile Coğrafya derslerinde ise cumhuriyet dönemi birikimi ve küresel ortam konuları aşağıdaki dizinde hafta sırasıyla yer alır.',
    ),
}


def _sinif_dizin_govde(sinif_no):
    import html as _h
    import json as _j
    ders_veri = _j.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))
    ic_veri = _j.loads((PUBLIC / 'veri' / 'icerikler.json').read_text(encoding='utf-8')).get('icerikler', [])
    ders_adlari = ders_veri.get('dersler', {})
    ortak_kodlar = list(ders_veri.get('siniflar', {}).get(str(sinif_no), []))
    secmeli_kodlar = list(ders_veri.get('secmeli', {}).get(str(sinif_no), []))
    sirali_kodlar = []
    for k in ortak_kodlar + secmeli_kodlar:
        if k not in sirali_kodlar:
            sirali_kodlar.append(k)
    for x in ic_veri:
        if x.get('sinif') == sinif_no and x.get('ders') and x['ders'] not in sirali_kodlar:
            sirali_kodlar.append(x['ders'])

    baslik, _, rehber_p = SINIF_REHBER_METINLERI[sinif_no]
    ders_kartlari = []
    gecis_baglari = []
    toplam_ozet = 0
    toplam_calisma = 0

    for dk in sirali_kodlar:
        ozetler = sorted(
            [x for x in ic_veri if x.get('sinif') == sinif_no and x.get('ders') == dk and x.get('tur') == 'Konu anlatımı' and x.get('goruntule')],
            key=lambda i: (int(i.get('hafta') or 999), str(i.get('baslik') or '')),
        )
        calismalar = sorted(
            [x for x in ic_veri if x.get('sinif') == sinif_no and x.get('ders') == dk and x.get('tur') == 'Çalışma kâğıdı' and x.get('goruntule')],
            key=lambda i: (int(i.get('hafta') or 999), str(i.get('baslik') or '')),
        )
        if not ozetler and not calismalar:
            continue
        toplam_ozet += len(ozetler)
        toplam_calisma += len(calismalar)
        ad = _h.escape(ders_adlari.get(dk, dk))
        bolum_id = f'dizin-{dk}'
        gecis_baglari.append(f'<a href="#{_h.escape(bolum_id, quote=True)}">{ad}</a>')

        ozet_li = ''.join(
            f'<li><a href="/{_h.escape(str(x["goruntule"]).lstrip("/"), quote=True)}">{_metin_bicimle(x.get("baslik", ""))}</a></li>'
            for x in ozetler
        )
        calisma_blok = ''
        if calismalar:
            cal_li = ''.join(
                f'<li><a href="/{_h.escape(str(x["goruntule"]).lstrip("/"), quote=True)}">{_metin_bicimle(x.get("baslik", ""))}</a></li>'
                for x in calismalar
            )
            calisma_blok = f'<p class="sinif-dizin-altgrup">{ad} Çalışma Kâğıtları (PDF ve Çözümlü Föy)</p><ul class="sinif-dizin-liste">{cal_li}</ul>'

        sayac_metin = f'{len(ozetler)} haftalık konu anlatımı' + (f' · {len(calismalar)} çalışma kâğıdı' if calismalar else '')
        ders_kartlari.append(
            f'        <article class="sinif-dizin-ders" id="{_h.escape(bolum_id, quote=True)}">\n'
            f'          <h2>{sinif_no}. Sınıf {ad}</h2>\n'
            f'          <p>{sayac_metin} · <a href="/ogrenci.html?sinif={sinif_no}&amp;ders={_h.escape(dk, quote=True)}">Ünite ağacında aç</a> · <a href="/planlar.html?sinif={sinif_no}">Günlük/yıllık plan</a></p>\n'
            f'          <ul class="sinif-dizin-liste">{ozet_li}</ul>\n'
            f'          {calisma_blok}\n'
            f'        </article>'
        )

    return (
        '  <section class="sayfa-bas">\n'
        '    <div class="kap">\n'
        f'      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/ogrenci.html">Öğrenci</a><span aria-hidden="true">/</span><span>{sinif_no}. Sınıf Konu Dizini</span></nav>\n'
        f'      <h1>{_h.escape(baslik)}</h1>\n'
        f'      <p>{_h.escape(rehber_p)}</p>\n'
        f'      <p><strong>Toplam içerik:</strong> {toplam_ozet} özgün haftalık konu anlatımı ve etkileşimli etkinlik sayfası'
        + (f', {toplam_calisma} yazdırılabilir çalışma kâğıdı.' if toplam_calisma else '.')
        + f' Ayrıca <a href="/ogrenci.html?sinif={sinif_no}">{sinif_no}. sınıf etkileşimli ünite gezgini</a>, <a href="/yazili.html?sinif={sinif_no}">{sinif_no}. sınıf ortak yazılı senaryoları</a> ve <a href="/planlar.html?sinif={sinif_no}">{sinif_no}. sınıf günlük ders planları</a> sayfalarını kullanabilirsiniz.</p>\n'
        f'      {_sinif_dizin_seridi(aktif=sinif_no)}\n'
        f'      <nav class="sinif-gecis" aria-label="{sinif_no}. sınıf dersleri">{"".join(gecis_baglari)}</nav>\n'
        '    </div>\n'
        '  </section>\n'
        '  <section class="bolum">\n'
        '    <div class="kap">\n'
        f'      <div class="sinif-dizin-grid">\n{chr(10).join(ders_kartlari)}\n      </div>\n'
        '    </div>\n'
        '  </section>\n' + SOSYAL_DAVET
    )


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
      <div class="kartlar" id="kartlar">
        {_kutuphane_onizleme_kartlari()}
      </div><!-- KARTLAR_SONU -->
      <div class="yakinda" id="icerik-yakinda" hidden>
        <div class="yakinda-simge" aria-hidden="true"><svg><use href="#s-kitap"/></svg></div>
        <div>
          <h3 id="sonucsuz-baslik">Filtrelere uygun kaynak seçimi</h3>
          <p id="sonucsuz-aciklama">Başka bir sınıf, ders veya tür seçebilirsiniz.</p>
          <div class="sonucsuz-eylemler">
            <button class="dugme ana" type="button" id="aramayi-temizle" hidden>Yalnız aramayı temizle</button>
            <button class="dugme" type="button" id="sonucsuz-temizle" hidden>Tüm içerikleri göster</button>
          </div>
        </div>
      </div>
      <!-- KUTUPHANE_BOLUM_SONU -->
    </div>
  </section>
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>Ders Kutusu Kaynak Kütüphanesi Nasıl Düzenlenmiştir?</h2>
        <p>Kaynak kütüphanemiz; 5, 6, 7 ve 8. sınıf ortaokul kademesi ile 9, 10, 11 ve 12. sınıf lise kademesindeki tüm zorunlu ve seçmeli dersleri tek bir arama çatısı altında toplar. Kütüphanede yer alan 2.800’ü aşkın eğitim materyali; Türkiye Yüzyılı Maarif Modeli (TYMM) öğretim programlarına ve Millî Eğitim Bakanlığı çerçeve yıllık planlarına göre hafta hafta sınıflandırılmıştır. Öğrenciler okulda işledikleri haftanın konu anlatımını sesli özet, görsel şema, çözümlü örnek ve anında dönüt veren etkileşimli etkinliklerle tekrar edebilir; ardından aynı konunun cevapsız ve cevaplı PDF çalışma kâğıdını indirerek yazılıya ve merkezî sınavlara hazırlanabilir.</p>
        <p>Öğretmenler ise kütüphane süzgeçlerinden hedef kitleyi “Öğretmen” olarak seçerek okul ve yönetici adlarıyla kişiselleştirilebilen günlük ders planlarına, yıllık çerçeve planlara, ÖDSGM ortak yazılı konu-soru dağılım senaryolarına ve resmî öğretim programlarına doğrudan ulaşabilir. Aşağıdaki sınıf dizinlerinden dilediğiniz sınıfın tüm ders ve hafta bağlantılarını tek sayfada görüntüleyebilirsiniz.</p>
      </div>
      {_sinif_dizin_seridi()}
    </div>
  </section>''', ('kutuphane.js',)),
    'belgeler.html': ('Resmî belgeler', 'MEB, ÖDSGM, DÖGM ve ÖSYM resmî belgeleri: öğretim programları, kılavuzlar, ortak yazılı tabloları, LGS ve YKS.', _belgeler_govde(), ('belgeler.js',)),
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
  </section>
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>Ortak Yazılı Senaryoları ve Açık Uçlu Sınav Uygulama Rehberi</h2>
        <p>Millî Eğitim Bakanlığı Ölçme, Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü (ÖDSGM) tarafından yayımlanan konu-soru dağılım tabloları, ortaokul ve lise derslerinde dönem içi ortak yazılı sınavların hangi öğrenme çıktılarından ve kaç açık uçlu sorudan oluşacağını belirler. Okul zümre öğretmenler kurulu dönem başında yayımlanan senaryolardan öğrenci profiline ve işlenen hafta takvimine uygun olan bir senaryoyu seçerek tutanak altına alır. Ders Kutusu’ndaki senaryo seçici, her senaryodaki öğrenme çıktılarını ve soru sayılarını doğrudan tablolaştırır; aynı senaryoya tam uyumlu hazır yazılı kâğıdını ve puanlama anahtarlı cevap kâğıdını PDF biçiminde sunar.</p>
        <h3>Senaryo Yazılısı ile Öğrenme Çıktısı Yazılısı Arasındaki Fark Nedir?</h3>
        <ul>
          <li><strong>Senaryoya göre yazılı kâğıtları:</strong> ÖDSGM’nin yayımladığı 1. ve 2. yazılı senaryo tablolarındaki soru dağılımını birebir takip eden, doğrudan dönem ortak sınavında veya sınav provasında kullanılmaya hazır açık uçlu sınav kâğıtlarıdır.</li>
          <li><strong>Öğrenme çıktısına göre yazılı kâğıtları:</strong> Türkiye Yüzyılı Maarif Modeli’ndeki her bir öğrenme çıktısını tek başına derinlemesine yoklayan, süreç odaklı izleme ve konu tarama yazılılarıdır.</li>
          <li><strong>Puanlama ve cevap anahtarı güvenliği:</strong> Cevaplı öğretmen kâğıtları her sorunun adım adım çözüm basamaklarını ve tam puan/kısmi puan ölçütlerini içerir; öğrenci sayfalarında ise yalnızca cevapsız çalışma kâğıtları listelenir.</li>
        </ul>
        <h3>Açık Uçlu Yazılı Sınavlarda Dereceli Puanlama ve Kısmi Puan İlkeleri</h3>
        <p>Açık uçlu ve kısa cevaplı yazılı sınavlarda değerlendirme yalnızca sonuca göre değil, öğrencinin kurduğu çözüm stratejisine, kullandığı bilimsel veya matematiksel kavramlara ve ara işlem basamaklarına göre yapılır. Ders Kutusu cevap anahtarlarında her soru için tam puanın yanı sıra ara adımların puan karşılıkları da ayrıntılı olarak gösterilir; böylece aynı zümredeki öğretmenlerin farklı şubelerde ortak ve nesnel bir puanlama standardı yakalaması kolaylaşır. Öğrenciler ise sınav öncesinde cevapsız öğrenci kâğıtlarını süre tutarak çözebilir, eksik kaldıkları öğrenme çıktıları için aşağıdaki sınıf konu dizinlerinden ilgili haftanın konu özetine ve çalışma kâğıdına doğrudan dönebilir.</p>
        <p>Birinci ve ikinci dönem ortak yazılı sınavları öncesinde yayınlanan bu çalışma kâğıtları, öğrencilerin çoktan seçmeli test alışkanlığından çıkarak düşüncelerini tam cümlelerle ifade etme, matematiksel ve bilimsel işlem basamaklarını düzenli yazma, tablo ve grafik verilerini yorumlayarak çıkarımda bulunma becerilerini geliştirir. Öğretmenlerimiz sınıf seviyesine göre farklı senaryoları indirip zümre sınav havuzu oluşturabilir ya da yazılı öncesi son ders saatinde akıllı tahtada örnek çözüm provası yapabilir.</p>
      </div>
      ''' + _sinif_dizin_seridi() + '''
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
      <button class="dugme" type="button" id="t-ig-kart" title="Haftalık Instagram konu kartı aç ya da tahtaya ekle">📸 IG Kartı</button>
      <button class="dugme" type="button" id="t-video" title="Ekran, tahta ve ses kaydı al">● Ders Kaydı</button>
      <button class="dugme" type="button" id="t-paylas" title="Tahtayı WhatsApp veya bağlantıyla paylaş">🟢 Paylaş</button>
      <a class="dugme ig-takip-mini" href="https://www.instagram.com/derskutusuinfo/" target="_blank" rel="noopener" title="@derskutusuinfo Instagram sayfasını ziyaret et"><svg viewBox="0 0 24 24" aria-hidden="true" style="width:14px;height:14px;vertical-align:-2px;margin-right:3px;fill:currentColor;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>@derskutusuinfo</a>
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
        <div class="katki-sosyal">
          <button class="dugme ana" type="button" id="katki-paylas">Bağlantıyı paylaş</button>
          <a class="dugme" href="https://api.whatsapp.com/send?text=Ders%20Kutusu%20%E2%80%94%201%E2%80%9312.%20s%C4%B1n%C4%B1f%20g%C3%BCnl%C3%BCk%20ve%20y%C4%B1ll%C4%B1k%20planlar%2C%20konu%20%C3%B6zetleri%2C%20ortak%20yaz%C4%B1l%C4%B1lar%20ve%20ASDS%20denemeleri%20(%40derskutusuinfo)%3A%20https%3A%2F%2Fderskutusu.com%2F" target="_blank" rel="noopener">🟢 WhatsApp’ta Paylaş</a>
        </div>
        <p class="katki-not" id="katki-durum" aria-live="polite"></p>
      </article>
      <article class="kart katki-kart">
        <h2>Takip edin</h2>
        <p>Yeni içerikleri ilk siz görün. Takip etmek ve videolara yorum bırakmak da bize destek olur.</p>
        <div class="katki-sosyal">
          <a class="dugme ana" href="https://www.instagram.com/derskutusuinfo/" data-sosyal="instagram" target="_blank" rel="noopener"><svg><use href="#s-instagram"/></svg>@derskutusuinfo · Instagram</a>
          <a class="dugme" href="https://www.youtube.com/@derskutusuinfo" data-sosyal="youtube" target="_blank" rel="noopener"><svg><use href="#s-youtube"/></svg>YouTube</a>
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
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>İçerik İnceleme, Doğrulama ve Yayın Sürecimiz</h2>
        <p>Ders Kutusu’na iletilen her hata bildirimi, içerik önerisi ve öğretmen materyali yayın ekibimiz tarafından dört aşamalı kalite kontrol sürecinden geçirilir. İlk aşamada içeriğin güncel Türkiye Yüzyılı Maarif Modeli (TYMM) öğretim programı ve ilgili sınıfın Millî Eğitim Bakanlığı ders kitabındaki kavram sınırlarıyla tam uyumu denetlenir; müfredat dışı terim veya kazanım üstü işlem basamakları ayıklanır. İkinci aşamada tüm metinler, matematiksel semboller, kesir ve karekök gösterimleri ile Türk Dil Kurumu yazım kuralları satır satır incelenir.</p>
        <p>Üçüncü aşamada çoktan seçmeli ve açık uçlu sorular bağımsız çözüm kontrolünden geçirilir; soru kökünün netliği, görsel-metin tutarlılığı ve tek doğru cevabın tartışmasız biçimde sağlandığı doğrulanır. Son aşamada ise içerik masaüstü bilgisayarlarda, tabletlerde, telefonlarda ve sınıf içi etkileşimli akıllı tahtalarda erişilebilirlik testinden geçirilerek yayına alınır. Öğretmenlerimizin kendi sınıflarında uygulayıp verim aldığı özgün çalışma kâğıtları ve etkinlik önerileri, Türkiye’nin dört bir yanındaki öğrencilerin nitelikli eğitim kaynaklarına ücretsiz ulaşmasına doğrudan katkı sağlar.</p>
        <h3>Hata Bildirimlerinde ve Önerilerde Hangi Bilgiler Yer Almalı?</h3>
        <p>Bildiriminizin aynı gün içinde sonuçlandırılabilmesi için ilgili sayfanın tam bağlantısını (örneğin 8. sınıf Matematik 4. hafta konu özeti veya 6. sınıf Fen Bilimleri 1. dönem 1. yazılı senaryo kâğıdı), fark ettiğiniz durumu ve varsa önerdiğiniz düzeltmeyi kısaca yazmanız yeterlidir. Gönderilen her e-posta doğrudan ilgili branş editörümüz tarafından kaynak ders kitabıyla karşılaştırılır, doğrulanan güncellemeler hem web sayfasına hem de indirilebilir PDF ve Word belgelerine eş zamanlı olarak yansıtılır. Açık erişimli eğitim kütüphanemizi büyütmek için katkıda bulunan tüm öğretmen ve öğrencilerimize teşekkür ederiz.</p>
        <p>Yeni içerik veya araç önerilerinizde okul türü (ortaokul, Anadolu lisesi, fen lisesi veya imam hatip lisesi), sınıf düzeyi ve ilgili ünite başlığını paylaşmanız üretim sıramızı planlamamıza doğrudan yardımcı olur. Öğretmenlerimizin zümre toplantılarında veya sınıf içi uygulamalarda ihtiyaç duyduğu yeni çizelge, çalışma yaprağı ve akıllı tahta özellikleri öncelikli olarak geliştirilerek tüm eğitim camiasının ücretsiz kullanımına sunulmaktadır.</p>
      </div>
      ''' + _sinif_dizin_seridi() + '''
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
            hazirlik = ('<li><a href="/sinif-8.html">8. sınıf LGS konu anlatımları ve çalışma kâğıtları tam dizini</a></li>'
                        '<li><a href="/ogrenci.html?sinif=8">8. sınıfın bütün dersleri ve üniteleri</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=Konu%20anlat%C4%B1m%C4%B1">8. sınıf konu özetleri ve etkinlikler</a></li>'
                        '<li><a href="/icerikler.html?sinif=8&amp;tur=%C3%87al%C4%B1%C5%9Fma%20k%C3%A2%C4%9F%C4%B1d%C4%B1">8. sınıf çalışma kâğıtları (PDF)</a></li>'
                        '<li><a href="/yazili.html?sinif=8">8. sınıf ortak yazılı senaryoları ve kâğıtları</a></li>')
        else:
            hazirlik = ''.join(f'<li><a href="/sinif-{k}.html">{k}. sınıf konu anlatımları ve ders dizini</a></li>' for k in x['siniflar'])
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
    asds_veri = _j.loads((PUBLIC / 'veri' / 'asds.json').read_text(encoding='utf-8'))
    asds_statik = []
    for blok in asds_veri.get('siniflar', []):
        sno = blok['sinif']
        sinav_kartlari = []
        for s in blok.get('sinavlar', []):
            dos = s.get('dosyalar', {})
            baglar = []
            for anahtar, etiket in (('a_cevapsiz', 'A Kitapçığı (Cevapsız)'), ('b_cevapsiz', 'B Kitapçığı (Cevapsız)'),
                                    ('a_cevapli', 'A Kitapçığı (Cevaplı)'), ('b_cevapli', 'B Kitapçığı (Cevaplı)'),
                                    ('anahtar', 'Cevap Anahtarı')):
                if dos.get(anahtar):
                    baglar.append(f'<a href="{e(dos[anahtar])}">{etiket}</a>')
            sinav_kartlari.append(
                f'<article class="kart" id="{e(s["kimlik"])}">'
                f'<h4>{sno}. Sınıf {e(s["ad"])}</h4>'
                f'<p>{e(s.get("olculen_hafta", ""))} · {s.get("soru_sayisi", 0)} soru, {s.get("sure", 0)} dk</p>'
                f'<p>{" · ".join(baglar)}</p>'
                f'</article>'
            )
        asds_statik.append(
            f'<div id="asds-sinif-{sno}">'
            f'<h3>{e(blok["baslik"])}</h3>'
            f'<p>{blok.get("soru_sayisi", 0)} soru · {blok.get("sure", 0)} dakika · {e(blok.get("puanlama", ""))}</p>'
            f'<div class="kartlar">{"".join(sinav_kartlari)}</div>'
            f'</div>'
        )
    asds_bolumu = f'''  <section class="bolum asds-ana-bolum" id="asds-bolum-kapsayici" aria-labelledby="asds-ana-baslik">
    <div class="kap">
      <div class="bolum-bas">
        <div>
          <p class="ust-baslik">5, 6, 7 ve 8. Sınıf Haftalık Deneme Sınavları · A &amp; B Kitapçığı</p>
          <h2 id="asds-ana-baslik">Akademik Süreç Değerlendirme Sınavları (ASDS)</h2>
          <p>Her bir sınıf için ayrı başlık altında; sınav uygulaması için <b>Cevapsız A ve B Kitapçıkları</b> ile öğretmen ve çözüm kontrolü için <b>Cevaplı A ve B Kitapçıkları + Cevap Anahtarı (PDF)</b> yer alır.</p>
        </div>
      </div>
      <div id="asds-bolum" class="asds-bolum-kutu">
        {"".join(asds_statik)}
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


GOVDE['planlar.html'] = ('Günlük planlar', '1-12. sınıf günlük ders planları: Okul, öğretmen, müdür yardımcısı ve müdür adları her sayfaya yazılır. Plan tüm yıl ya da ay ay, Word veya PDF olarak indirilir.', '''  <section class="sayfa-bas plan-bas">
    <div class="kap">
      <nav class="yol" aria-label="Konum"><a href="/">Ana sayfa</a><span aria-hidden="true">/</span><a href="/#ogretmen">Öğretmen</a><span aria-hidden="true">/</span><span>Günlük planlar</span></nav>
      <h1>Günlük ders planları</h1>
      <p>İlkokuldan liseye bütün sınıfların planları burada. Okulun adını, kendi adınızı, müdür yardımcısının ve müdürün adını bir kez yazın. İndirdiğiniz planın her sayfasına bu bilgiler kendiliğinden yerleşir. Planı tüm yıl ya da ay ay, Word veya PDF olarak alın.</p>
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
  </section>
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>Türkiye Yüzyılı Maarif Modeli Günlük ve Yıllık Ders Planı Rehberi</h2>
        <p>İlkokul 1–4, ortaokul 5–8 ve lise 9–12. sınıf kademelerindeki tüm dersler için hazırlanan günlük ders planları; Millî Eğitim Bakanlığı Talim ve Terbiye Kurulu Başkanlığı öğretim programları ile 37 haftalık çerçeve yıllık plan takvimine tam uyumlu olarak düzenlenmiştir. Her haftanın günlük ders planı; ilgili öğrenme alanı ve temayı, süreç bileşenlerini, öğrenme-öğretme yaşantılarını, farklılaştırma (zenginleştirme ve destekleme) etkinliklerini, okul dışı öğrenme önerilerini ve süreç odaklı ölçme-değerlendirme araçlarını eksiksiz içerir.</p>
        <p>Öğretmenlerimiz okul adını, kendi ad ve soyadını, müdür yardımcısı ve okul müdürü bilgilerini yalnızca bir kez girdiğinde sistem bu bilgileri tarayıcı belleğinde (sunucuya hiçbir kişisel veri göndermeden) tüm sayfalardaki imza bloklarına otomatik yerleştirir. Dilerseniz tüm eğitim öğretim yılını tek bir düzenlenebilir Word (.docx) ya da yazdırmaya hazır PDF dosyası olarak indirebilir, dilerseniz ay ay bölünmüş ZIP arşivini zümre klasörünüze kaydedebilirsiniz.</p>
        <h3>Günlük Ders Planlarında Bulunan Bölümler ve Uygulama Esnekliği</h3>
        <p>Hazırlanan her haftalık ders planı sayfasında dersin adı, sınıf düzeyi, ünite veya tema başlığı, önerilen ders saati, ilgili haftanın öğrenme çıktıları, derse giriş ve merak uyandırma soruları, adım adım konu işlenişi, kavram yanılgılarına karşı uyarılar ve ders sonu değerlendirme soruları standart bir tablo düzeninde yer alır. Word (.docx) biçiminde indirilen planlarda okulunuzun zümre kararlarına, bölgesel etkinlik takvimine veya sınıfınızın hazırbulunuşluk düzeyine göre dilediğiniz satırı düzenleyebilir; PDF biçimini ise doğrudan yazdırarak ders defteri ve zümre dosyası eki olarak kullanabilirsiniz.</p>
        <p>Planlarda yer alan haftalık tarih aralıkları Millî Eğitim Bakanlığı iş günü takvimine göre birinci ve ikinci dönem ara tatilleri, yarıyıl tatili ve ortak sınav haftaları dikkate alınarak yapılandırılmıştır. İlgili haftanın günlük planını indirdikten sonra aynı haftanın etkileşimli konu özetini ve çalışma kâğıdını aşağıdaki sınıf dizinlerinden açarak ders hazırlığınızı birkaç dakika içinde tamamlayabilirsiniz.</p>
      </div>
      ''' + _sinif_dizin_seridi() + '''
    </div>
  </section>\n''' + SOSYAL_DAVET, ('planlar.js',))

# Ders dağıtım programı (kullanıcı 22.10.2026): uygulama ders-dagitim-uygulama.html'de tek dosya, kendi stilleriyle;
# site stilleriyle çakışmasın diye bu sayfada çerçeve içinde açılır. Veriler yalnız ziyaretçinin tarayıcısında (localStorage).
GOVDE['ders-dagitim.html'] = ('Ders dağıtım programı', 'Okullar için ücretsiz ders dağıtım programı: öğretmen, sınıf ve ders bilgilerinden haftalık program üretir, yerleşmeyen dersin nedenini gösterir; PDF ve Excel çıktı verir. Veriler yalnız tarayıcınızda kalır.', '''<style>
.ddp-bas { padding-bottom: 28px; }
.ddp-kap { padding: 20px 0 8px; }
.sayfa-bas .dd-sayac { font-size: 16px; margin-top: 8px; }
.dd-sayac strong { color: var(--metin); font-variant-numeric: tabular-nums; }
.ddp-cerceve { display: block; width: 100%; height: calc(100vh - 96px); min-height: 560px; border: 0; border-radius: var(--kose); background: var(--zemin-2); box-shadow: var(--golge); }
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
      <div class="g-dugmeler y-ust"><a class="dugme ana" href="/ders-dagitim-uygulama.html">Tam ekranda aç</a> <a class="dugme" href="#ddp-nasil">Nasıl kullanılır?</a> <a class="dugme" href="https://api.whatsapp.com/send?text=Okullar%20i%C3%A7in%20%C3%BCcretsiz%20Ders%20Da%C4%9F%C4%B1t%C4%B1m%20Program%C4%B1%20(PDF%20ve%20Excel%20%C3%A7%C4%B1kt%C4%B1l%C4%B1)%3A%20https%3A%2F%2Fderskutusu.com%2Fders-dagitim.html" target="_blank" rel="noopener">🟢 Okul Yönetimiyle Paylaş</a> <a class="dugme" href="https://www.instagram.com/derskutusuinfo/" target="_blank" rel="noopener"><svg><use href="#s-instagram"/></svg>@derskutusuinfo</a></div>
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
      <h2>Okul Yönetimleri İçin Çizelge Planlama İpuçları</h2>
      <p>Haftalık ders dağıtım çizelgesi hazırlanırken önce laboratuvar, bilişim teknolojileri sınıfı, müzik atölyesi ve spor salonu gibi ortak kullanılan özel dersliklerin saatleri ile iki öğretmenin birlikte girdiği uygulamalı dersler tanımlanmalıdır. Ardından nöbet günleri, zümre toplantı saatleri ve öğretmenlerin mazeretli olduğu zaman dilimleri girildiğinde yerleştirme motoru dar boğazları öncelik sırasıyla çözer. Herhangi bir sınıfın haftalık toplam ders saati ile atanmış branş derslerinin toplamı uyuşmadığında sistem uyarı vererek eksik veya fazla saati anında bildirir; böylece dönem başında el ile yapılan saat kaydırma hataları tamamen önlenir.</p>
      <h2>Blok Ders Dağılımı, Çakışma Çözümü ve Resmî Çıktı Biçimleri</h2>
      <p>Dağıtım algoritması, dört veya beş saatlik ana branş derslerini (Matematik, Türkçe, Türk Dili ve Edebiyatı, Fen Bilimleri, Fizik, Kimya, Biyoloji ve Yabancı Dil) haftanın günlerine dengeli biçimde örneğin 2+2 veya 2+2+1 blok yapısıyla yerleştirir; aynı sınıfa aynı günde aşırı yüklenmeyi engeller. Yerleşmeyen bir ders saati kaldığında program yalnızca hata vermekle kalmaz, hangi öğretmenin hangi gündeki kapalı saati açılırsa veya hangi iki sınıfın dersi takas edilirse çizelgenin %100 tamamlanacağını adım adım listeler. Tamamlanan haftalık ders programını sınıf el programı, öğretmen el programı ve okul genel çarşaf çizelgesi olarak PDF veya Excel (.xlsx) biçiminde indirip okul panolarında ve öğretmenler kurulunda doğrudan paylaşabilirsiniz.</p>
      <p>Dönem içinde öğretmen değişikliği, seçmeli ders güncellemesi veya derslik tadilatı gibi durumlarda mevcut çizelgenizi sıfırlamanıza gerek yoktur; yalnızca ilgili öğretmenin veya sınıfın kısıtlarını güncelleyip yeniden dağıtım çalıştırarak en az değişiklikle yeni haftalık programı oluşturabilirsiniz.</p>
    </div>
  </div>\n''' + SOSYAL_DAVET, ())

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
      <h2 class="kelime-baslik" id="k-tema-baslik">Temel İngilizce Kelime Kartları</h2>
      <div id="k-alan" class="kelime-alan" aria-live="polite">
        <p>5 ve 6. sınıf İngilizce ders kitaplarının ünite sözlüklerinden derlenen kelimeleri sesli telaffuz, anlam kartı, çoktan seçmeli test, yazma ve eşleştirme adımlarıyla çalışabilirsiniz.</p>
      </div>
      <p class="kelime-not">İlerlemen yalnız bu tarayıcıda tutulur, hiçbir yere gönderilmez. Sesler tarayıcının kendi okuma özelliğiyle çıkar.</p>
      <div class="statik-rehber">
        <h2>İngilizce Kelime Öğrenme Yöntemi ve Ünite Temaları</h2>
        <p>Yabancı dil öğreniminde kalıcı söz varlığı geliştirmek, kelimeleri tek başına ezberlemek yerine bağlam içinde görmek, doğru telaffuzu dinlemek ve aralıklı tekrar (spaced repetition) yöntemiyle aktif olarak geri çağırmakla mümkündür. Ders Kutusu İngilizce kelime çalışma aracı, Millî Eğitim Bakanlığı 5. ve 6. sınıf İngilizce ders kitaplarının sözlük bölümlerindeki 800’ü aşkın hedef kelimeyi ünite temalarına göre gruplandırır. Öğrenciler “Classroom Life”, “Family &amp; Friends”, “Daily Routines”, “Health”, “Festivals” ve “Nature” gibi her temada önce çift yönlü bilgi kartlarıyla kelimenin Türkçe karşılığını ve örnek kullanımını inceler; ardından dinleme ve klavyeyle yazma alıştırmalarıyla hem işitsel hem görsel hafızayı birlikte çalıştırır.</p>
        <p>Kelime alıştırmalarını tamamladıktan sonra ilgili haftanın dil bilgisi yapılarını ve diyalog örneklerini pekiştirmek için <a href="/sinif-5.html">5. sınıf İngilizce konu anlatımları</a>, <a href="/sinif-6.html">6. sınıf İngilizce konu anlatımları</a>, <a href="/sinif-7.html">7. sınıf</a> ve <a href="/sinif-8.html">8. sınıf LGS İngilizce</a> dizinlerimizdeki haftalık ders özetlerine ve çalışma kâğıtlarına geçebilirsiniz.</p>
        <h3>Dört Çalışma Kipini Verimli Kullanma Sırası</h3>
        <p>Yeni bir temaya başlarken önce <strong>Kartlar</strong> kipinde kelimenin yazılışını ve anlamını inceleyip ses simgesiyle doğru okunuşu yüksek sesle tekrar edin. Ardından <strong>Eşleştir</strong> kipiyle hızlı görsel çağrışım kurun, <strong>Test</strong> kipiyle çeldiriciler arasından doğru anlamı seçme hızınızı ölçün ve son aşamada <strong>Yaz</strong> kipiyle sessiz harfleri veya çift ünsüzleri hatasız kodladığınızdan emin olun. Düzenli olarak günde on beş dakika yapılan bu dört adımlı tekrar, okul yazılılarında ve okuma parçalarında karşılaşılan kelimelerin kalıcı hafızaya yerleşmesini sağlar.</p>
        <h3>Sınıf Düzeyine Göre Kapsanan Temalar ve Yazılıya Hazırlık</h3>
        <p>5. sınıf İngilizce kelime listeleri okul ortamı, ders araç gereçleri, tanışma ve selamlaşma kalıpları, ülkeler ve uluslar, saatler, günlük alışkanlıklar, hastalıklar ve sağlık önerileri, film türleri, doğum günü partisi hazırlıkları, spor etkinlikleri ve hayvan barınağı temalarını eksiksiz içerir. 6. sınıf kelime grupları ise okul sonrası etkinlikler, kahvaltı ve beslenme alışkanlıkları, şehir ve kasaba yaşamı, hava durumu ve duygular, lunapark araçları, meslekler, tatil etkinlikleri, kitap kurdu okuma terimleri, çevre koruma ve demokratik seçim kavramlarını kapsar. Her temadaki kelimeleri öğrendikten sonra ilgili haftanın açık uçlu yazılı sorularını ve çalışma kâğıtlarını çözerek okuma-yazma bütünlüğünü sağlayabilirsiniz.</p>
        <p>Öğretmenlerimiz sınıf içi akıllı tahtada temayı seçip tam ekran kart görünümüyle ders başında beş dakikalık kelime ısınma etkinliği yapabilir; öğrenciler ise yanlış yanıtladıkları kelimeleri tekrar listesinde toplayarak kendi bireysel sözlüklerini adım adım tamamlayabilir. Tüm kelime verileri ve seslendirmeler hiçbir üyelik gerektirmeden her cihazda doğrudan çalışır.</p>
      </div>
      ''' + _sinif_dizin_seridi() + '''
    </div>
  </section>''', ('kelime.js',))

GOVDE['arapca.html'] = ('Arapça harf ve kelime çalışması', '28 harf ve 48 kelime/ifade: harf biçimleri, harekeler, kartlar, test, Arapça klavyeyle yazma ve eşleştirme.', f'''<link rel="stylesheet" href="/arapca.css?v={SURUM}">
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
<div id="a-alan" class="kelime-alan"><p>28 Arapça harfin başta, ortada ve sonda yazılış biçimleri ile üstün, esre, ötre ve cezm harekelerini etkileşimli kartlarla inceleyebilirsiniz.</p></div>
<p id="a-ses-durum" class="kelime-not" role="status"></p>
<p class="kelime-not">İlerlemen yalnız bu tarayıcıda tutulur. Kelime ve ifade kapsamı MEB 5–6. sınıf Arapça kitapları ve yıllık planlarına göre hazırlanmıştır. Alfabe bölümü genel tekrar içindir.</p>
<div class="k-dugmeler sol"><a class="dugme" href="/ozet/5-arapca-hafta-1.html">5. sınıf konu anlatımı</a><a class="dugme" href="/ozet/6-arapca-hafta-1.html">6. sınıf konu anlatımı</a><a class="dugme" href="/kelime.html">İngilizce kelime çalışması</a></div>
<div class="statik-rehber">
  <h2>Arapça Harf Biçimleri, Harekeler ve Kelime Çalışma Rehberi</h2>
  <p>Arapça okuma ve yazma becerisinin temeli, sağdan sola yazım yönünü kavramak ve 28 harfin kelime başındaki, ortasındaki ve sonundaki bitişme biçimlerini ayırt edebilmektir. Kendinden sonraki harfle birleşmeyen <em>elif, dal, zel, ra, ze ve vav</em> harflerinin tanınması, öğrencilerin kelime köklerini ve eklerini okurken hata yapmasını önler. Bu sayfadaki çalışma modülü; harf tanıma aşamasından başlayarak fetha (üstün), kesra (esre), damme (ötre), sükûn (cezm) ve şedde işaretlerinin sese etkisini adım adım uygulamalı olarak gösterir.</p>
  <p>Harf ve hareke tekrarının ardından selamlaşma, tanışma, aile bireyleri, okul eşyaları ve günlük ifadeler temalarındaki kelimeleri ekran içi Arapça klavyeyle yazarak, sesli dinleyerek ve anlam eşleştirmesi yaparak pekiştirebilirsiniz. Ortaokul ve imam hatip lisesi düzeyindeki tüm haftalık Arapça ders özetleri için <a href="/sinif-5.html">5. sınıf</a>, <a href="/sinif-6.html">6. sınıf</a>, <a href="/sinif-7.html">7. sınıf</a>, <a href="/sinif-8.html">8. sınıf</a>, <a href="/sinif-9.html">9. sınıf</a> ve <a href="/sinif-10.html">10. sınıf</a> konu dizinlerimizi inceleyebilirsiniz.</p>
  <p>Çalışırken önce <strong>Harfler</strong> ve <strong>Harekeler</strong> sekmelerinde mahreç ve kısa-uzun ünlü farklarını kavrayıp ardından kelime kartlarına geçmeniz önerilir. Sağdan sola birleşen harflerin kuyruklarının satır çizgisine göre nasıl kısaldığını gözlemlemek ve ekran klavyesiyle kelimeyi harekeli biçimde yeniden yazmak, hem ders kitabındaki diyalog metinlerini akıcı okumayı hem de açık uçlu yazılı sınavlarda doğru yazım yapmayı doğrudan kolaylaştırır.</p>
  <h3>Uzatma Harfleri (Med), Tenvin ve Günlük İletişim Kalıpları</h3>
  <p>Arapçada kelimelerin doğru okunması ve anlamlandırılması için kısa ünlü görevindeki harekelerin yanı sıra <em>elif, vav ve ye</em> uzatma (med) harflerinin, kelime sonunda belirsizlik bildiren iki üstün, iki esre ve iki ötre (tenvin) işaretlerinin ve harfi iki kez okutan şeddenin işlevi iyi kavranmalıdır. Modüldeki kelime kartları yalnızca tekil sözcükleri değil; sabah ve akşam selamlaşmalarını, kendini ve ailesini tanıtma cümlelerini, sınıf içi yönergeleri, soru edatlarını ve temel nezaket ifadelerini de harekeli yazılışları ve Türkçe anlamlarıyla birlikte sunar. Böylece öğrenciler hem dinleme-konuşma etkinliklerine hem de dönem içi yazılı sınavlarına sağlam bir temelle hazırlanır.</p>
  <p>Ayrıca müzekker (eril) ve müennes (dişil) kelimelerin sonundaki kapalı te (tâ-i merbûta) işareti, işaret zamirleri (hâzâ / hâzihî) ve iyelik ekleri (benim, senin, onun) ünite örnekleriyle birlikte gösterilir. Öğrenciler her kartta kelimenin Arapça yazılışını inceledikten sonra ekran klavyesinde harfleri tek tek seçerek birleşme kurallarını bizzat uygulayabilir ve kendi ilerleme yüzdelerini takip edebilir.</p>
</div>
''' + _sinif_dizin_seridi() + '''
<noscript>Alıştırmalar için JavaScript’i etkinleştirin. Konu anlatımlarını yukarıdaki bağlantılardan okuyabilirsiniz.</noscript>
</div></section>''', ('arapca.js',))

GOVDE['ogrenci.html'] = ('Öğrenci', 'Ders Kutusu öğrenci sayfası: sınıfını seç; ünite ünite konu anlatımları, etkinlikler, çalışma kâğıtları ve ders kitapları.', f'''  <div id="agac" class="agac"><section class="agac-bas"><div class="kap">
      <h1>Öğrenci Çalışma Merkezi (5–12. Sınıf)</h1>
      <p>Sınıfını seç; Türkiye Yüzyılı Maarif Modeli (TYMM) ve güncel Millî Eğitim Bakanlığı yıllık plan sırasına göre hazırlanan haftalık konu özetlerine, görsel modellere, çözümlü örneklere, etkileşimli etkinliklere ve PDF çalışma kâğıtlarına hiçbir üyelik gerekmeden doğrudan ulaş.</p>
      <ul>
        <li><a href="/sinif-5.html">5. sınıf konu anlatımları ve çalışma kâğıtları dizini</a> (<a href="/ogrenci.html?sinif=5">Ünite gezgini</a>)</li>
        <li><a href="/sinif-6.html">6. sınıf konu anlatımları ve çalışma kâğıtları dizini</a> (<a href="/ogrenci.html?sinif=6">Ünite gezgini</a>)</li>
        <li><a href="/sinif-7.html">7. sınıf konu anlatımları ve çalışma kâğıtları dizini</a> (<a href="/ogrenci.html?sinif=7">Ünite gezgini</a>)</li>
        <li><a href="/sinif-8.html">8. sınıf · LGS konu anlatımları ve çalışma kâğıtları dizini</a> (<a href="/ogrenci.html?sinif=8">Ünite gezgini</a>)</li>
        <li><a href="/sinif-9.html">9. sınıf lise konu anlatımları dizini</a> (<a href="/ogrenci.html?sinif=9">Ünite gezgini</a>)</li>
        <li><a href="/sinif-10.html">10. sınıf lise konu anlatımları dizini</a> (<a href="/ogrenci.html?sinif=10">Ünite gezgini</a>)</li>
        <li><a href="/sinif-11.html">11. sınıf AYT ve lise konu anlatımları dizini</a> (<a href="/ogrenci.html?sinif=11">Ünite gezgini</a>)</li>
        <li><a href="/sinif-12.html">12. sınıf · YKS (TYT · AYT) konu anlatımları dizini</a> (<a href="/ogrenci.html?sinif=12">Ünite gezgini</a>)</li>
      </ul>
      <p>Etkileşimli çalışma araçları: <a href="/kelime.html">İngilizce kelime kartları</a> · <a href="/arapca.html">Arapça harf ve kelime çalışması</a> · <a href="/sinav.html">ASDS Deneme Sınavları, LGS ve YKS Rehberi</a> · <a href="/kpss.html">KPSS Genel Yetenek Modülleri</a> (<a href="/kpss/turkce-paragrafta-anlam.html">Paragrafta Anlam</a> · <a href="/kpss/matematik-temel-kavramlar.html">Temel Kavramlar</a>)</p>
    </div></section></div>
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>Ders Kutusu ile Haftalık Ders Tekrarı ve Sınava Hazırlık Nasıl Yapılır?</h2>
        <p>Kalıcı akademik başarı, okulda işlenen konunun aynı hafta içinde sade bir özetle tekrar edilmesine ve farklı soru tipleriyle sınanmasına dayanır. Ders Kutusu’ndaki 1.600’ü aşkın haftalık konu anlatımı sayfası dört temel öğrenme adımını tek ekranda birleştirir: Önce renkli vektörel şemalar, bilgi ve dikkat kutularıyla konunun özü kavranır; ardından adım adım açılır çözümlü örneklerle işlem ve yorumlama stratejisi görülür; üçüncü adımda çoktan seçmeli, doğru-yanlış, eşleştirme ve boşluk doldurma sorularından oluşan etkileşimli etkinliklerle anında geri bildirim alınır; son adımda ise iki sayfalık PDF çalışma kâğıdı indirilerek kâğıt-kalem pratiği tamamlanır.</p>
        <p>Ortaokul 5, 6, 7 ve 8. sınıf öğrencileri ayrıca her ay uygulanan A ve B kitapçıklı Akademik Süreç Değerlendirme Sınavları (ASDS) ile sarmal kazanım eksiklerini ölçebilir; lise 9, 10, 11 ve 12. sınıf öğrencileri ise hem okul yazılılarına hem de TYT ve AYT oturumlarına ünite sırasını bozmadan hazırlanabilir. Aşağıdaki sınıf bağlantılarından kendi sınıfınızın tüm ders ve hafta listesine tek tıkla geçebilirsiniz.</p>
        <div id="yaziliya-hazirlik">
          <h3>Yazılıya Hazırlık, Açık Uçlu Çalışma Kâğıtları ve Kişisel İlerleme Takibi</h3>
          <p>Üstteki sınıf ve ders gezgininden dersinizi seçtiğinizde ilgili dersin ünite ve hafta ağacının altında o dönemin ortak yazılı senaryolarına ve öğrenme çıktılarına uygun açık uçlu öğrenci çalışma kâğıtları doğrudan listelenir. Öğrenci sayfalarında sınav heyecanını ve öz değerlendirmeyi desteklemek amacıyla yalnızca cevapsız çalışma kâğıtları yer alır; ayrıntılı puanlama anahtarları ise öğretmen bölümünde sunulur. Ayrıca okuduğunuz her konu özetini “Bu konuyu tamamladım” düğmesiyle işaretleyerek hangi ünitede yüzde kaç ilerlediğinizi kendi cihazınızda adım adım takip edebilirsiniz.</p>
        </div>
        <h3>Ortaokul ve Lise Kademelerinde Kapsanan Dersler</h3>
        <p>Ortaokul kademesinde (5, 6, 7 ve 8. sınıflar) Türkçe, Matematik, Fen Bilimleri, Sosyal Bilgiler, T.C. İnkılap Tarihi ve Atatürkçülük, İngilizce, Din Kültürü ve Ahlak Bilgisi, Arapça, Kur’an-ı Kerim, Peygamberimizin Hayatı ve Temel Dini Bilgiler derslerinin tamamı hafta hafta yer alır. Lise kademesinde (9, 10, 11 ve 12. sınıflar) ise Türk Dili ve Edebiyatı, Matematik, Fizik, Kimya, Biyoloji, Tarih, Coğrafya, Felsefe, İngilizce, Din Kültürü ve Ahlak Bilgisi ile imam hatip meslek derslerinin tüm ünite özetleri, kavram haritaları ve çalışma yaprakları açık erişimli olarak sunulmaktadır.</p>
        <h3>Adım Adım Bireysel Çalışma ve Tekrar Planı</h3>
        <p>Haftalık çalışmanıza başlarken önce okulda o hafta işlenen ünite ve konuyu seçip özetin başındaki öğrenme çıktılarını okuyun. Konu anlatımı içindeki renkli şemaları, formül kutularını ve kavram karşılaştırma tablolarını inceledikten sonra çözümlü örneklerin cevabını açmadan önce kendi başınıza çözmeyi deneyin. Ardından sayfa sonundaki etkileşimli çoktan seçmeli, doğru-yanlış, eşleştirme ve boşluk doldurma sorularını tamamlayarak anında doğruluk kontrolü yapın. Hafta sonunda ise aynı konunun iki sayfalık PDF çalışma kâğıdını indirip çözerek öğrendiklerinizi kalıcı hafızaya taşıyın; sınav haftalarında ise ortak yazılı senaryo kâğıtları ve ASDS deneme sınavlarıyla genel tekrarınızı tamamlayın.</p>
      </div>
      {_sinif_dizin_seridi()}
    </div>
  </section>''', ('agac.js',))
GOVDE['ogretmen.html'] = ('Öğretmen Köşesi', 'Öğretmen Köşesi: günlük ve yıllık planlar, ortak yazılı senaryoları ve kâğıtları, öğretim programları, çalışma kâğıtları ve resmî belgeler.', f'''  <div id="agac" class="agac"><section class="agac-bas"><div class="kap">
      <h1>Öğretmen Köşesi · Plan, Ölçme ve Akıllı Tahta Merkezi</h1>
      <p>1’den 12. sınıfa kadar derse hazırlık, sınıf içi sunum ve süreç odaklı ölçme-değerlendirme için hazırlanan tüm belgeler aşağıda kategorilere ayrılmıştır.</p>
      <ul>
        <li><a href="/planlar.html">Günlük ders planları (1–12. sınıf)</a>: Okul, öğretmen ve yönetici adları her sayfaya otomatik yerleşir; tüm yıl ya da ay ay Word (.docx) veya PDF olarak indirilir.</li>
        <li><a href="/ders-dagitim.html">Okul haftalık ders dağıtım programı</a>: Öğretmen, sınıf, branş ve derslik kısıtlarından otomatik haftalık çizelge kurar; PDF ve Excel çıktısı verir.</li>
        <li><a href="/ogretmen.html?kategori=yillik-plan">Çerçeve yıllık planlar</a>: Güncel Türkiye Yüzyılı Maarif Modeli ve MEB öğretim programlarına uyumlu 37 haftalık yıllık planlar.</li>
        <li><a href="/yazili.html">Ortak yazılı senaryoları ve cevaplı yazılı kâğıtları</a>: ÖDSGM konu-soru dağılım tabloları, senaryoya göre ve öğrenme çıktısına göre açık uçlu sınav kâğıtları.</li>
        <li><a href="/ogretmen.html?kategori=ogretim-programi">Ders öğretim programları</a>: Öğrenme çıktıları, süreç bileşenleri, içerik çerçevesi ve uygulama açıklamaları.</li>
        <li><a href="/ogretmen.html?kategori=calisma-kagidi">Sınıf içi çalışma kâğıtları</a>: Derste veya ödevlendirmede kullanmak üzere cevapsız öğrenci ve cevaplı öğretmen PDF föyleri.</li>
        <li><a href="/belgeler.html">Resmî mevzuat ve kılavuz belgeleri</a>: MEB, TTKB, ÖDSGM, DÖGM ve ÖSYM tarafından yayımlanan kılavuz ve tablolar.</li>
        <li><a href="/tahta.html">Dijital akıllı tahta</a>: Kareli, çizgili, noktalı ve koordinat düzlemli zeminlerde kalem, şekil tanıma ve ders kaydı aracı.</li>
        <li><a href="/kpss.html">KPSS Genel Yetenek çalışma merkezi</a>: Öğretmen adayları için özgün konu özetleri, çözümlü örnekler ve PDF testler.</li>
      </ul>
    </div></section></div>
  <section class="bolum koyu-zemin">
    <div class="kap">
      <div class="statik-rehber">
        <h2>Sınıf İçi Ders İşlenişi ve Ölçme-Değerlendirme Araçlarımız</h2>
        <p>Ders Kutusu Öğretmen Köşesi, öğretmenlerin evrak yükünü azaltmak ve sınıf içi öğretim süresini nitelikli içerikle zenginleştirmek amacıyla tasarlanmıştır. Sitedeki bütün haftalık konu özetleri akıllı tahta uyumlu tam ekran sunum kipine ve sayfa üzerine doğrudan kalemle yazma özelliğine sahiptir; böylece sınıfta ek bir yazılım kurmaya gerek kalmadan tarayıcı üzerinden konu anlatımı ve örnek soru çözümü yapılabilir. Günlük plan oluşturucu ve ders dağıtım programı gibi yönetim araçlarında girilen kurum ve öğretmen adları hiçbir sunucuya aktarılmaz; tüm belge üretimi doğrudan cihazınızın tarayıcısında gerçekleşir.</p>
        <p>Zümre çalışmalarında dönem içi yazılı hazırlarken <a href="/yazili.html">Ortak Yazılılar</a> bölümünden ilgili sınıf ve dersin ÖDSGM senaryolarını karşılaştırabilir, öğrencilerinizin bireysel konu tekrarı için de aşağıdaki sınıf konu dizinlerini doğrudan paylaşabilirsiniz.</p>
        <h3>Türkiye Yüzyılı Maarif Modeli Süreç Odaklı Ölçme ve Zümre Hazırlığı</h3>
        <p>Güncel öğretim programlarında ölçme ve değerlendirme yalnızca dönem sonu notu vermeye değil, öğrencinin öğrenme çıktılarındaki gelişimini süreç boyunca izlemeye ve geri bildirimle desteklemeye odaklanır. Öğretmen Köşesi’nde yer alan haftalık çalışma kâğıtları; kavrama, uygulama, analiz ve bağlam temelli muhakeme basamaklarını dengeli biçimde tarayacak şekilde iki sayfalık kompakt föyler hâlinde hazırlanmıştır. Her çalışma kâğıdının hem sınıf içinde öğrencilere dağıtılabilecek cevapsız baskı sürümü hem de akıllı tahtada veya öğretmen kontrolünde kullanılabilecek tam çözümlü cevap anahtarı sürümü ayrı ayrı indirilebilir.</p>
        <p>Dönem başı ve dönem sonu zümre toplantılarında ihtiyaç duyulan çerçeve yıllık planlara, ders öğretim programlarına, MEB çalışma takvimine ve ortak sınav uygulama kılavuzlarına üstteki kategori düğmelerinden veya <a href="/belgeler.html">Resmî Belgeler</a> arşivinden saniyeler içinde ulaşabilirsiniz.</p>
        <h3>Akıllı Tahta Sunum Kipi, Kalem Aracı ve Sınıf İçi Etkileşim</h3>
        <p>Sınıf içi etkileşimli tahtalarda herhangi bir konu özetini açtığınızda üst araç çubuğundaki “Sunum modu” düğmesiyle menüleri gizleyip metin ve şemaları tam ekran büyütebilir, “Kalemle yaz” düğmesiyle de doğrudan paragrafların, grafiklerin ve çözümlü örneklerin üzerine renkli kalem ve fosforlu vurgulayıcıyla not alabilirsiniz. Ders sonunda öğrencilerinize ödev veya tekrar bağlantısı göndermek istediğinizde sayfadaki paylaşım düğmesiyle ilgili haftanın konu özetini, çalışma kâğıdını veya yazılı senaryosunu tek tıkla sınıf gruplarında paylaşabilirsiniz. Bütün öğretmen araçlarımız reklamsız çalışma tuvallerine, hızlı yüklenen vektörel grafiklere ve sıfır üyelik ilkesine sahiptir.</p>
        <h3>Kademe ve Branşlara Göre Hazır Zümre Kaynakları</h3>
        <p>İlkokul, ortaokul ve lise öğretmenlerimiz için hazırlanan yıllık ve günlük plan arşivi; Türkçe, Matematik, Fen Bilimleri, Sosyal Bilgiler, T.C. İnkılap Tarihi ve Atatürkçülük, İngilizce, Din Kültürü ve Ahlak Bilgisi, Türk Dili ve Edebiyatı, Fizik, Kimya, Biyoloji, Tarih, Coğrafya, Felsefe, Arapça ve meslek derslerinin tamamını kapsar. Ayrıca dönem ortasında ve dönem sonunda yapılan ortak yazılı sınavlar için ÖDSGM senaryo tablolarına birebir uyumlu açık uçlu sorular, puanlama cetvelleri ve kazanım eşleştirme listeleri düzenli olarak güncellenir. Öğretmen adaylarımız da KPSS Genel Yetenek bölümündeki özgün konu anlatımları, çözümlü örnekler ve PDF deneme yapraklarıyla sınava ücretsiz hazırlanabilir.</p>
      </div>
      {_sinif_dizin_seridi()}
    </div>
  </section>''', ('agac.js',))
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

    <h2>Kapsam ve yayın standartlarımız</h2>
    <p>Ders Kutusu’nda yayımlanan 1.600’den fazla haftalık konu anlatımı, 720’yi aşkın çalışma kâğıdı, ortak yazılı senaryoları ve ASDS deneme kitapçıkları; eğitimde fırsat eşitliğini desteklemek amacıyla hiçbir abonelik duvarı olmadan açık erişimli sunulur. Matematiksel ifadelerde kesirler ve karekökler ders kitaplarındaki akademik dizgi kurallarına uygun biçimde gösterilir; fen, sosyal bilimler ve dil derslerindeki tüm şemalar ekran okuyucu uyumlu vektörel çizimlerle hazırlanır. Güncel müfredat değişiklikleri yayımlandıkça ilgili sınıf ve hafta içerikleri aynı eğitim dönemi içinde güncellenir.</p>
    <p>Yayın kurulumuz her eğitim öğretim yılı başında Millî Eğitim Bakanlığı Talim ve Terbiye Kurulu Başkanlığı tarafından yayımlanan çerçeve öğretim programlarını, ders kitaplarını ve Ölçme, Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğü (ÖDSGM) konu-soru dağılım tablolarını ayrıntılı olarak inceler. Ortaokul 5–8. sınıf ve lise 9–12. sınıf kademelerindeki tüm derslerde öğrencilerin kavram yanılgısına düşebileceği noktalar “Dikkat” ve “İpucu” kutularıyla vurgulanır; öğretmenlerimizin sınıf içinde doğrudan akıllı tahtada kullanabileceği yüksek kontrastlı sunum görünümü ve yazdırılabilir PDF föyleri bir arada sunulur.</p>
  </div>
</div>''', ())
GOVDE['iletisim.html'] = ('İletişim', 'Ders Kutusu ile iletişim: soru, öneri, hata bildirimi ve telif başvuruları için e-posta.', '''<div class="metin-sayfa">
  <div class="kap">
    <h1>İletişim</h1>
    <p>Ders Kutusu yayın ekibiyle soru, içerik önerisi, akademik hata bildirimi, okul erişim desteği ve telif başvuruları için doğrudan e-posta üzerinden iletişime geçebilirsiniz. Ziyaretçi gizliliğini korumak amacıyla sitede kişisel veri toplayan bir üyelik ya da iletişim formu bulundurulmaz; gönderdiğiniz e-postalar yalnızca başvurunuzu yanıtlamak ve ilgili içeriği iyileştirmek için kullanılır.</p>

    <h2>Kurumsal E-posta Adresimiz</h2>
    <p><a href="mailto:info@derskutusu.com">info@derskutusu.com</a></p>

    <h2>Hangi Konularda Başvurabilirsiniz?</h2>
    <ul>
      <li><strong>Akademik ve dizgisel hata bildirimi:</strong> Konu özetinde, çözümlü örnekte, etkileşimli etkinlikte, PDF çalışma kâğıdında ya da günlük plan dosyasında fark ettiğiniz yazım veya işlem hatasını ilgili sayfanın tam adresiyle birlikte iletebilirsiniz. Bildirilen maddi hatalar öncelikli olarak incelenir ve düzeltilmiş sürüm kısa sürede yayına alınır. <a href="mailto:info@derskutusu.com?subject=Hata%20bildirimi">Hata bildir</a></li>
      <li><strong>Yeni ders ve materyal önerisi:</strong> Okulunuzda veya sınıfınızda ihtiyaç duyduğunuz ünite özetlerini, çalışma kâğıtlarını, yazılı senaryolarını ya da akıllı tahta araçlarını sınıf ve ders belirterek önerebilirsiniz. Üretim takvimimizi öğretmen ve öğrencilerden gelen taleplere göre şekillendiriyoruz. <a href="mailto:info@derskutusu.com?subject=%C4%B0%C3%A7erik%20%C3%B6nerisi">Öneri gönder</a></li>
      <li><strong>Telif hakları ve kaynak bildirimleri:</strong> Sitedeki özgün içeriklerin kullanım izinleri veya telif bildirimleri için sayfa bağlantısı ve açıklamanızla birlikte başvurabilirsiniz. Başvurular en geç 72 saat içinde değerlendirilir. Ayrıntılı bilgi için <a href="/telif.html">Telif hakları ve kullanım koşulları</a> sayfasını inceleyebilirsiniz.</li>
      <li><strong>Okul ağı ve akıllı tahta erişim desteği:</strong> Sitenin bir sayfası veya PDF belgesi okul ağınızda ya da sınıf içi etkileşimli tahtada açılmıyorsa tarayıcı bilgisini ve ekranda görünen uyarıyı yazmanız yeterlidir.</li>
    </ul>

    <h2>Sosyal Medya ve Duyuru Kanallarımız</h2>
    <p>Yeni eklenen haftalık ders özetlerini, yazılı hazırlık serilerini ve ASDS deneme duyurularını resmi sosyal medya hesaplarımızdan da takip edebilirsiniz: <a href="https://www.instagram.com/derskutusuinfo/" target="_blank" rel="noopener">Instagram (@derskutusuinfo)</a> · <a href="https://www.youtube.com/@derskutusuinfo" target="_blank" rel="noopener">YouTube (@derskutusuinfo)</a> · <a href="https://www.facebook.com/derskutusuinfo" target="_blank" rel="noopener">Facebook (@derskutusuinfo)</a>.</p>

    <h2>Değerlendirme ve Yanıt Sürecimiz</h2>
    <p>Öğretmen, öğrenci ve velilerden gelen her e-posta doğrudan içerik ve yazılım geliştirme ekibimiz tarafından okunur. Konu anlatımları, çalışma kâğıtları veya sınav anahtarlarıyla ilgili maddi hata bildirimleri en yüksek öncelikle ele alınarak kaynak ders kitabıyla karşılaştırılır ve doğrulanan düzeltmeler aynı gün içinde yayına yansıtılır. Kurumsal iş birliği, açık kaynak eğitim projeleri ve gizlilik politikamızla ilgili sorularınız da gizlilik ilkelerimiz çerçevesinde titizlikle yanıtlanır.</p>
    <p>E-posta gönderirken bildiriminizin daha hızlı incelenebilmesi için konu satırında sınıf düzeyini, ders adını ve hafta numarasını (örneğin “7. Sınıf Fen Bilimleri 5. Hafta Çalışma Kâğıdı Soru 4”) belirtmeniz süreci hızlandırır. Okul zümrelerinizde kullandığınız yıllık ve günlük planlarla veya haftalık ders dağıtım programıyla ilgili teknik destek taleplerinizde ise kullandığınız cihaz türünü (masaüstü bilgisayar, tablet veya etkileşimli tahta) eklemeniz çözüm üretmemizi kolaylaştıracaktır.</p>
    <p>Yayın ekibimiz hafta içi ve hafta sonu gelen tüm akademik bildirimleri düzenli olarak tarar; özellikle yazılı sınav haftalarında ve deneme sınavı dönemlerinde öğretmen ve öğrencilerimizin acil belge veya cevap anahtarı sorularına öncelik verilir. Sitedeki bütün ders içeriklerine <a href="/icerikler.html">Kaynak Kütüphanesi</a> üzerinden veya sınıf dizinlerinden doğrudan ulaşabilirsiniz.</p>
    <p>Okul yönetimleri, il ve ilçe zümre başkanlıkları veya eğitim fakültesi öğretim elemanları tarafından iletilen açık erişimli materyal paylaşımı, ortak çalışma yaprağı geliştirme ve müfredat uyumu görüşleri de doğrudan akademik koordinasyon ekibimizce değerlendirilir. Ders Kutusu, Türkiye’nin her bölgesindeki öğrenci ve öğretmenlerin reklama boğulmayan, hızlı, güvenilir ve ücretsiz eğitim kaynaklarına ulaşması için kesintisiz olarak geliştirilmektedir.</p>

    <p>Siteye içerik veya paylaşım yoluyla destek olmak için <a href="/katki.html">Katkıda bulun</a> sayfasına, yayın ilkelerimiz için <a href="/hakkimizda.html">Hakkımızda</a> ve <a href="/gizlilik.html">Gizlilik ve çerezler</a> sayfalarına göz atabilirsiniz.</p>
  </div>
</div>''', ())

for _s in range(5, 13):
    _b, _a, _ = SINIF_REHBER_METINLERI[_s]
    GOVDE[f'sinif-{_s}.html'] = (_b, _a, _sinif_dizin_govde(_s), ())

# Arama dizinine girmeyecek araç/yönlendirme sayfaları (içerik değil, araç)
NOINDEX = {'sinif.html', 'ara.html', 'tahta.html', 'goruntule.html', 'okul-bildir.html', 'ders-dagitim-uygulama.html'}


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
        alt_kisim = eski[eski.index('</main>'):]
        if '<script>' in alt_kisim:
            aday = alt_kisim[alt_kisim.index('<script>'):alt_kisim.index('</script>') + len('</script>')]
            if 'requestNonPersonalizedAds' not in aday:
                betik = aday
        html = sayfa(ad, baslik, aciklama, govde, kanonik=kanonik).replace('</body>', (betik + '\n' if betik else '') + '</body>')
        (PUBLIC / ad).write_text(html, encoding='utf-8')

    # Ana sayfa (gövdesi elle bakılır): reklam alanı alt bilginin üstünde; slot kimliği değişince burası da yenilenir
    yol = PUBLIC / 'index.html'
    eski = yol.read_text(encoding='utf-8')
    yeni = re.sub(r'<aside class="reklam"[^\n]*</aside>\n', '', eski).replace('<footer class="alt">', reklam_yeri('index.html') + '<footer class="alt">', 1)
    if yeni != eski:
        yol.write_text(yeni, encoding='utf-8')

    # Sitemap senkronizasyonu: 8 sınıf dizini ve yazili.html dahil edilir, NOINDEX sayfaları dışarıda tutulur
    harita_yol = PUBLIC / 'sitemap.xml'
    if harita_yol.exists():
        harita = harita_yol.read_text(encoding='utf-8')
        eklenecek = [f'https://derskutusu.com/{ad}' for ad in (*SINIF_DIZIN_SAYFALARI, 'yazili.html')]
        eksikler = [u for u in eklenecek if f'<loc>{u}</loc>' not in harita]
        if eksikler:
            blok = ''.join(f'  <url><loc>{u}</loc><lastmod>2026-11-06</lastmod></url>\n' for u in eksikler)
            anker = '  <url><loc>https://derskutusu.com/ogretmen.html</loc></url>\n'
            if anker in harita:
                harita = harita.replace(anker, anker + blok, 1)
            else:
                harita = harita.replace('</urlset>', blok + '</urlset>')
            harita_yol.write_text(harita, encoding='utf-8')

    print('üretildi:', ', '.join([*GOVDE, 'gizlilik.html', 'telif.html', '404.html', 'index.html (reklam alanı)']))


if __name__ == '__main__':
    main()
