"""Keşif sayfalarının ortak görünümü; içerik kaynaklarını değiştirmez."""
import re

CSS = '<link rel="stylesheet" href="/kesif.css?v=20261004-duzen1">'
JS = '<script src="/kesif.js?v=20261004-duzen1"></script>'
RENK_CSS = '<link rel="stylesheet" href="/renkler.css?v=20261004-duzen1" media="screen">'


def renkli_sayfa(html, ad):
    """Yalnız site çerçevesi: ders içeriği, şekiller ve baskı stilleri korunur."""
    renk = {
        'icerikler.html': 'mor', 'planlar.html': 'turuncu',
        'yazili.html': 'pembe', 'sinav.html': 'pembe',
        'belgeler.html': 'turkuaz', 'kelime.html': 'lacivert',
        'arapca.html': 'lacivert', 'kpss.html': 'sari',
        'tahta.html': 'yesil', 'goruntule.html': 'yesil',
    }.get(ad, 'mor' if ad.startswith('ozet/') else 'yesil' if ad.startswith('calisma/') else 'mavi')
    html = re.sub(r'(<body\b[^>]*?)\sdata-site-renk="[^"]*"', r'\1', html, count=1)
    html = re.sub(r'<body\b', f'<body data-site-renk="{renk}"', html, count=1)
    if 'href="/renkler.css?' not in html:
        html = html.replace('</head>', RENK_CSS + '\n</head>')
    return html


def kutuphane_govde(govde):
    if 'kesif-library' in govde:
        return govde
    govde = govde.replace('<h1>İçerikler</h1>', '<h1>Kaynak kütüphanesi</h1>')
    govde = govde.replace('Sınıfa, derse, haftaya ve türe göre arayın: konu anlatımları, soru çözümleri, videolar; öğretmenler için yıllık planlar, yazılı soruları ve çalışma kâğıtları.', 'Öğrenmek, pekiştirmek veya derse hazırlanmak için ihtiyacın olan kaynağı bul.')
    govde = govde.replace('<form class="suzgec-cubugu"', '''<div class="kesif-library">
      <aside class="kesif-sidebar" aria-label="Kaynak kategorileri"><h2>Kategoriler</h2><div id="kategori-secimleri"></div></aside>
      <div class="kesif-results">
      <form class="suzgec-cubugu"''')
    govde = govde.replace('<p class="sonuc-bilgi">', '<div class="kesif-result-toolbar"><p class="sonuc-bilgi">')
    govde = govde.replace('Seçimleri temizle</button></p>', '''Seçimleri temizle</button></p>
      <label class="kesif-sort">Sıralama<select id="s-sirala"><option value="yeni">Son eklenen</option><option value="baslik">Başlık A–Z</option><option value="sinif">Sınıf sırası</option></select></label></div>''')
    govde = govde.replace('<div class="kartlar" id="kartlar"></div>', '''<div class="kartlar" id="kartlar"></div>
      <div class="kesif-more" id="daha-alani" hidden><p id="gosterilen-sayi" role="status"></p><button class="dugme" type="button" id="daha-goster">Daha fazla kaynak göster ↓</button></div>''')
    left, sep, right = govde.rpartition('    </div>\n  </section>')
    if not sep:
        raise ValueError('Kütüphane kapanış yapısı değişmiş')
    return left + '      </div>\n      </div>\n' + sep + right


def kesif_sayfa(html, ad):
    if ad not in ('index.html', 'sinif.html', 'icerikler.html'):
        return renkli_sayfa(html, ad)
    if 'kesif.css?' not in html:
        html = html.replace('</head>', CSS + '\n</head>')
    html = html.replace('<body>', '<body class="kesif-page">')
    if 'src="/kesif.js?' not in html:
        import re
        html = re.sub(r'(<script src="/?ortak\.js[^>]*></script>)', r'\1\n' + JS, html, count=1)
    return renkli_sayfa(html, ad)
