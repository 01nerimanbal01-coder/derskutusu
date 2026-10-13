"""7. sınıf Sosyal Bilgiler, 7. hafta: küreselleşmenin insan ve toplum hayatına etkisi (ünite: Evimiz Dünya).

Kaynak: Görseller yalnız özet metnindeki (araclar/ozetler/7-sosyal-bilgiler-7.json) bilgilerle çizilir;
ders kitabı sayfası kullanılmamıştır.
Renk anlamı: mavi = küreselleşmenin bağları ve nedenleri (ulaşım, iletişim, ticaret, teknoloji), günümüz ve dünyaya açılma;
mor = ana kavram (küreselleşme), ülke/toplum düğümleri ve etki alanları; yeşil = olumlu yön ve korunan değerler (kökler, Türkçe);
turuncu = olumsuz yön; gri = eskiden / yansız çerçeve ve terazi-gövde çizgileri.
Ağ şeması ve ağaç şeması ölçeksizdir, harita değildir; insan figürü, logo, marka ve bayrak çizilmez.
"""
import math

from ozet_gorsel import svg, ok_isareti

RENK = {'mavi': ('g-ma', 'g-ms', 'g-mf'), 'turuncu': ('g-ta', 'g-ts', 'g-tf'),
        'yesil': ('g-ya', 'g-ys', 'g-yf'), 'mor': ('g-oa', 'g-os', 'g-of'), 'gri': ('g-z', 'g-c', 'g-s')}


def _kutu(x, y, w, h, renk, rx=10, kalinlik=1.5):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def _m(x, y, t, boyut=12.5, agirlik=None, sinif='g-y', ankor=None):
    a = f' text-anchor="{ankor}"' if ankor else ''
    g = f' font-weight="{agirlik}"' if agirlik else ''
    return f'<text x="{x}" y="{y}"{a} font-size="{boyut}"{g} class="{sinif}">{t}</text>'


def _cizgi(x1, y1, x2, y2, sinif='g-c', kalinlik=2, ek=''):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{sinif}" stroke-width="{kalinlik}" stroke-linecap="round"{ek}/>'


def _bag(a, b, r, sinif, kalinlik, ek=''):
    # iki düğümü, dairelere değmeden birleştir
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    return _cizgi(a[0] + ux * (r + 3), a[1] + uy * (r + 3), b[0] - ux * (r + 3), b[1] - uy * (r + 3), sinif, kalinlik, ek)


def ag():
    """Dünya neden küçüldü: seyrek bağlar (eskiden) ile sık bağlar (günümüzde) ağ şeması; ölçeksiz, harita değil."""
    R, r = 56, 11
    ic = ''
    paneller = [(8, 'Eskiden: seyrek ve yavaş bağlar', 'İpek Yolu, coğrafi keşifler', [(0, 1), (3, 4), (5, 2)], 1.5, ' stroke-dasharray="5 4"'),
                (244, 'Günümüzde: sık ve hızlı bağlar', 'internet, hızlı ulaşım', [(i, j) for i in range(6) for j in range(i + 1, 6)], 2, '')]
    for px, baslik, altyazi, kenarlar, kalin, ek in paneller:
        cx, cy = px + 110, 114
        ic += _m(cx, 22, baslik, 13, 800, 'g-y', 'middle')
        ic += _kutu(px, 32, 220, 180, 'gri', 12)
        dugumler = [(cx + R * math.cos(math.radians(-90 + 60 * k)), cy + R * math.sin(math.radians(-90 + 60 * k))) for k in range(6)]
        for i, j in kenarlar:
            ic += _bag(dugumler[i], dugumler[j], r, 'g-ms', kalin, ek)
        for x, y in dugumler:
            ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="g-of"/>'
        ic += _m(cx, 203, altyazi, 12, None, 'g-s', 'middle')
    # açıklama satırı
    ic += '<circle cx="16" cy="228" r="6" class="g-of"/>' + _m(28, 232, 'bir ülke ya da toplum', 12)
    ic += _cizgi(166, 228, 192, 228, 'g-ms', 2) + _m(200, 232, 'ulaşım, iletişim, ticaret bağı', 12)
    ic += _m(370, 232, '(ölçeksiz)', 12, None, 'g-s')
    # sınırları aşanlar
    ic += _m(8, 267, 'Sınırları aşanlar:', 12.5, 700)
    x = 118
    for t, w in [('insanlar', 74), ('mallar', 62), ('para', 52), ('bilgi', 50)]:
        ic += _kutu(x, 250, w, 24, 'mavi', 12)
        ic += _m(x + w / 2, 267, t, 12.5, 700, 'g-mf', 'middle')
        x += w + 8
    ic += _m(236, 298, 'Dünya fiziksel olarak küçülmedi; bağlar arttı.', 12, None, 'g-y', 'middle')
    ic += _m(236, 317, 'Mesafeler engel olmaktan çıktı → “küresel köy”.', 12.5, 700, 'g-y', 'middle')
    return svg(472, 326, ic, 'Ölçeksiz ağ şeması, harita değil: altı ülke ya da toplum dairesi iki panelde gösterilir. Eskiden, İpek Yolu ve coğrafi '
               'keşifler döneminde, daireler arasında yalnız üç seyrek ve kesikli bağ vardır; günümüzde internet ve hızlı ulaşımla her daire '
               'diğer hepsine sık ve kalın bağlarla bağlıdır. Bu ulaşım, iletişim ve ticaret bağlarından insanlar, mallar, para ve bilgi sınırları '
               'aşar. Dünya fiziksel olarak küçülmedi; bağlar arttığı için mesafeler engel olmaktan çıktı, bu yüzden dünyaya küresel köy denir.')


def gunluk():
    """Günlük hayatta eskiden–günümüzde karşılaştırma kutuları ve dil örneği."""
    ic = '<defs>' + ok_isareti('okSB77a', 'g-s') + '</defs>'
    ic += _kutu(67, 8, 100, 22, 'gri', 11) + _m(117, 23, 'Eskiden', 13, 800, 'g-y', 'middle')
    ic += '<rect x="308" y="8" width="110" height="22" rx="11" class="g-mf"/>' + _m(363, 23, 'Günümüzde', 13, 800, 'g-b', 'middle')
    satirlar = [('Bilgiye erişim', ['Kütüphaneye gitmek,', 'ansiklopedi karıştırmak'],
                 ['Saniyede yanıt, sanal müze gezisi,', 'alt yazıyla yabancı dilde ders']),
                ('Eğitim ve çalışma', ['Okulda ders,', 'iş yerinde çalışma'],
                 ['Evden ekran başında ders,', 'başka ülkedeki şirkete uzaktan iş']),
                ('Alışveriş, sofra ve eğlence', ['Yakın çevreden, çoğu yerel', 'üretim ürünler'],
                 ['Farklı kıtalardan ürün, çevrim içi', 'sipariş; farklı dilde şarkı, aynı dizi'])]
    for i, (baslik, sol, sag) in enumerate(satirlar):
        ty = 52 + i * 68
        ic += _m(8, ty, baslik, 12.5, 800)
        y0 = ty + 6
        ic += _kutu(8, y0, 218, 44, 'gri', 10) + _kutu(254, y0, 218, 44, 'mavi', 10)
        for k, t in enumerate(sol):
            ic += _m(18, y0 + 18 + k * 16, t, 12)
        for k, t in enumerate(sag):
            ic += _m(264, y0 + 18 + k * 16, t, 12)
        ic += _cizgi(231, y0 + 22, 247, y0 + 22, 'g-c', 2, ' marker-end="url(#okSB77a)"')
    ic += _kutu(8, 252, 464, 30, 'yesil', 15)
    ic += _m(22, 271, 'Dil:', 12.5, 800, 'g-yf') + _m(52, 271, 'selfie → özçekim', 12.5, 700)
    ic += _m(172, 271, 'e-mail → e-posta', 12.5, 700) + _m(292, 271, '(TDK’nin önerdiği karşılık)', 12, None, 'g-s')
    return svg(472, 292, ic, 'Eskiden ve günümüzde karşılaştırma kutuları. Bilgiye erişim: eskiden kütüphaneye gitmek ve ansiklopedi karıştırmak; '
               'günümüzde saniyede yanıt, sanal müze gezisi, alt yazıyla yabancı dilde ders. Eğitim ve çalışma: eskiden okulda ders, iş yerinde '
               'çalışma; günümüzde evden ekran başında ders, başka ülkedeki şirkete uzaktan iş. Alışveriş, sofra ve eğlence: eskiden yakın '
               'çevreden, çoğu yerel üretim ürünler; günümüzde farklı kıtalardan ürün, çevrim içi sipariş, farklı dilde şarkılar ve aynı diziler. '
               'Dil: selfie yerine özçekim, e-mail yerine e-posta; bunlar TDK’nin önerdiği Türkçe karşılıklardır.')


def terazi():
    """Olumlu ve olumsuz yönler terazi benzetmesiyle; altta değerlendirme soruları."""
    ic = _cizgi(118, 36, 354, 36, 'g-c', 3)
    ic += '<polygon points="236,38 226,54 246,54" class="g-s"/>'
    ic += _cizgi(236, 54, 236, 196, 'g-c', 3) + '<rect x="200" y="196" width="72" height="6" rx="3" class="g-s"/>'
    ic += _cizgi(118, 38, 118, 58, 'g-c', 2) + _cizgi(354, 38, 354, 58, 'g-c', 2)
    kartlar = [(8, 'yesil', 'Olumlu yönler', ['Bilgi ve bilim hızla paylaşılır', 'Farklı kültürleri tanıma, hoşgörü',
                                              'Ürün çeşitliliği, yeni iş alanları', 'Afetlerde küresel dayanışma']),
               (244, 'turuncu', 'Olumsuz yönler', ['Kültürel tekdüzeleşme', 'Yerel kültür ve diller unutulur',
                                                  'Aşırı tüketim, dijital bağımlılık', 'Dijital uçurum: eşitsizlik'])]
    for x, renk, baslik, ogeler in kartlar:
        ic += _kutu(x, 58, 220, 124, renk, 12)
        ic += _m(x + 14, 80, baslik, 13.5, 800, RENK[renk][2])
        for k, t in enumerate(ogeler):
            y = 102 + k * 20
            ic += f'<circle cx="{x + 20}" cy="{y - 4}" r="3" class="{RENK[renk][2]}"/>'
            ic += _m(x + 30, y, t, 12)
    ic += _m(236, 222, 'Yalnız “iyi” ya da “kötü” demek yetmez:', 12.5, 700, 'g-y', 'middle')
    ic += _kutu(112, 232, 248, 26, 'gri', 13) + _m(236, 250, 'Kimin için? · Hangi alanda? · Nasıl?', 13, 800, 'g-y', 'middle')
    return svg(472, 268, ic, 'Terazi benzetmesi: iki kefede küreselleşmenin yönleri. Olumlu yönler: bilgi ve bilim hızla paylaşılır; farklı '
               'kültürleri tanıma ve hoşgörü; ürün çeşitliliği ve yeni iş alanları; afetlerde küresel dayanışma. Olumsuz yönler: kültürel '
               'tekdüzeleşme; yerel kültür ve dillerin unutulması; aşırı tüketim ve dijital bağımlılık; dijital uçurum, yani eşitsizlik. '
               'Terazi dengede durur: yalnız iyi ya da kötü demek yetmez; kimin için, hangi alanda ve nasıl soruları sorulur.')


def agac():
    """Köklerine bağlı kalarak dünyaya açılmak: dalları dünyaya uzanan, kökleri değerlerde kalan ağaç şeması."""
    ic = '<ellipse cx="236" cy="92" rx="226" ry="84" class="g-ma"/><ellipse cx="236" cy="92" rx="226" ry="84" class="g-ms" stroke-width="1.5"/>'
    ic += _m(236, 30, 'Dallar: dünyaya açılmak', 13, 800, 'g-mf', 'middle')
    ic += '<rect x="0" y="206" width="472" height="138" class="g-ya"/>' + _cizgi(0, 206, 472, 206, 'g-ys', 2)
    ic += '<rect x="226" y="118" width="20" height="88" rx="4" class="g-s"/>'
    dallar = [(145, 46, 182, 'Kültürünü dünyayla paylaş', (236, 76)),
              (18, 84, 124, 'Dünyadan öğren', (144, 98)),
              (268, 84, 186, 'Küresel sorunlarda iş birliği', (266, 98))]
    for x, y, w, t, (ux, uy) in dallar:
        ic += _cizgi(236, 120, ux, uy, 'g-ms', 2.5)
    for x, y, w, t, _ in dallar:
        ic += _kutu(x, y, w, 28, 'mavi', 14)
        ic += _m(x + w / 2, y + 19, t, 12, 700, 'g-mf', 'middle')
    kokler = [(10, 232, 166, 'Türkçeyi doğru kullanmak', (178, 246)),
              (252, 232, 206, 'Bayramları, gelenekleri yaşatmak', (250, 246)),
              (44, 280, 172, 'Yerel üreticiyi desteklemek', (218, 294)),
              (256, 280, 102, 'Tarihini bilmek', (254, 294))]
    for x, y, w, t, (ux, uy) in kokler:
        ic += _cizgi(236, 208, ux, uy, 'g-ys', 2.5)
    for x, y, w, t, _ in kokler:
        ic += _kutu(x, y, w, 28, 'yesil', 14)
        ic += _m(x + w / 2, y + 19, t, 12, 700, 'g-yf', 'middle')
    ic += _m(236, 332, 'Kökler: millî ve manevi değerleri korumak', 13, 800, 'g-yf', 'middle')
    return svg(472, 344, ic, 'Ağaç benzetmesi, ölçeksiz şema: gövdenin üstündeki mavi dallar dünyaya açılmayı gösterir: dünyadan öğren, '
               'kültürünü dünyayla paylaş, küresel sorunlarda iş birliği. Toprağın altındaki yeşil kökler millî ve manevi değerleri korumayı '
               'gösterir: Türkçeyi doğru kullanmak, bayramları ve gelenekleri yaşatmak, yerel üreticiyi desteklemek, tarihini bilmek. '
               'Ağaç köklerini kaybetmeden dallarını uzatır: dünyadan öğren, kendi değerlerinle katıl.')


def kavram():
    """Kavram haritası örneği: nedenler, merkezde küreselleşme, etki alanları ve artı/eksi örnek satırları."""
    ic = '<defs>' + ok_isareti('okSB77b', 'g-s') + '</defs>'
    ic += _m(8, 18, 'Nedenler', 12.5, 800, 'g-mf')
    nedenler = ['Ulaşım', 'İletişim', 'Ticaret', 'Teknoloji']
    hedef = [186, 220, 252, 286]
    for k, t in enumerate(nedenler):
        x = 8 + k * 114
        ic += _kutu(x, 26, 106, 28, 'mavi', 14) + _m(x + 53, 45, t, 12.5, 700, 'g-mf', 'middle')
        ic += _cizgi(x + 53, 58, hedef[k], 92, 'g-c', 1.5, ' marker-end="url(#okSB77b)"')
    ic += '<rect x="156" y="96" width="160" height="40" rx="20" class="g-of"/>' + _m(236, 121, 'KÜRESELLEŞME', 15, 800, 'g-b', 'middle')
    ic += _m(8, 172, 'Etkiler', 12.5, 800, 'g-of')
    etkiler = [('Ekonomi', 84, '+ yeni iş alanı', '− kriz yayılır'), ('Kültür', 84, '+ hoşgörü', '− tekdüzeleşme'),
               ('Sağlık', 84, '+ aşı iş birliği', '− hızlı salgın'), ('Çevre', 84, '+ iklim iş birliği', '− kirlilik yayılır'),
               ('Günlük hayat', 104, '+ bilgiye erişim', '− dijital bağımlılık')]
    x = 8
    kaynak = [196, 216, 236, 256, 276]
    for k, (t, w, arti, eksi) in enumerate(etkiler):
        cx = x + w / 2
        ic += _cizgi(kaynak[k], 138, cx, 177, 'g-c', 1.5, ' marker-end="url(#okSB77b)"')
        ic += _kutu(x, 180, w, 28, 'mor', 14) + _m(cx, 199, t, 12.5, 700, 'g-of', 'middle')
        ic += _m(cx, 226, arti, 11.5, None, 'g-yf', 'middle') + _m(cx, 242, eksi, 11.5, None, 'g-tf', 'middle')
        x += w + 4
    ic += _m(236, 270, 'Her etkiye bir olumlu (+), bir olumsuz (−) örnek.', 12, None, 'g-s', 'middle')
    return svg(472, 282, ic, 'Kavram haritası örneği. Üstte dört neden: ulaşım, iletişim, ticaret, teknoloji; oklar ortadaki küreselleşme '
               'kavramına gider. Küreselleşmeden beş etki alanına oklar çıkar: ekonomi, kültür, sağlık, çevre, günlük hayat. Her alanın altında '
               'bir olumlu artı örnek ve bir olumsuz eksi örnek vardır: ekonomi, artı yeni iş alanı, eksi kriz yayılır; kültür, artı hoşgörü, '
               'eksi tekdüzeleşme; sağlık, artı aşı iş birliği, eksi hızlı salgın; çevre, artı iklim iş birliği, eksi kirlilik yayılır; '
               'günlük hayat, artı bilgiye erişim, eksi dijital bağımlılık.')


def uygula(o):
    g = {'Küreselleşme: dünya neden “küçüldü”?': ag(),
         'Günlük hayatındaki değişimler': gunluk(),
         'Olumlu ve olumsuz yönler': terazi(),
         'Köklerine bağlı kalarak dünyaya açılmak': agac(),
         'Değişimi ifade etmek: kavram haritası': kavram()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
