"""9. sınıf Tarih, 1. hafta: Tarih Öğrenmenin Faydaları (TAR.9.1.1).

Görseller yalnız MEB 9. sınıf Tarih ders kitabındaki bilgilerle çizilir (kitap s. 11, 13, 15-17).
Renk anlamı: mor = geçmiş ve tarih, turuncu = şimdi / tarihini bilmeyen toplum,
mavi = gelecek / bireye faydalar, yeşil = tarihini bilen toplum / topluma faydalar.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'mor': ('g-oa', 'g-os', 'g-of'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def zaman_oku():
    """Geçmiş, şimdi, gelecek: biten her an geçmişe dönüşür; öngörüde bulunmak için geçmişi bilmek gerekir (kitap s. 15)."""
    # kalın zaman çizgisinin ok ucu küçük tutulur (işaret çizgi kalınlığıyla büyür)
    ic = ('<defs><marker id="okT9a" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto">'
          '<path d="M0 0L10 5L0 10z" class="g-mf"/></marker>' + ok_isareti('okT9b', 'g-of') + '</defs>')
    # üstte geçmişten geleceğe uzanan yay: öngörü (kitap: öngörü için geçmişi bilmek "gerekir"; "sağlar" denmez)
    ic += ('<text x="236" y="20" text-anchor="middle" font-size="12.5" font-weight="700" class="g-of">'
           'Öngörüde bulunmak için geçmişi bilmek gerekir.</text>')
    ic += '<path d="M100 76 Q236 -4 368 74" class="g-os" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#okT9b)"/>'
    # zaman çizgisi: geçmiş (mor) · şimdi (turuncu nokta) · gelecek (mavi, oklu)
    ic += '<line x1="24" y1="90" x2="224" y2="90" class="g-os" stroke-width="4" stroke-linecap="round"/>'
    ic += '<line x1="248" y1="90" x2="440" y2="90" class="g-ms" stroke-width="4" stroke-linecap="round" marker-end="url(#okT9a)"/>'
    ic += '<circle cx="236" cy="90" r="9" class="g-tf"/>'
    etiket = [(100, 'Geçmiş', 'g-of', ('yaşanmış olaylar',)),
              (236, 'Şimdi', 'g-tf', ('biten her an', 'geçmişe dönüşür')),
              (372, 'Gelecek', 'g-mf', ('yaşanabilecek', 'olaylar'))]
    for x, ad, sinif, alt in etiket:
        ic += f'<text x="{x}" y="120" text-anchor="middle" font-size="14" font-weight="800" class="{sinif}">{ad}</text>'
        for k, t in enumerate(alt):
            ic += f'<text x="{x}" y="{139 + k * 16}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
    ic += ('<text x="236" y="186" text-anchor="middle" font-size="12.5" class="g-y">'
           'İnsan, <tspan font-weight="800">geçmiş ile gelecek arasında</tspan> yaşar.</text>')
    return svg(472, 198, ic, 'Zaman şeridi: geçmiş, şimdi ve gelecek. Biten her an geçmişe dönüşür. Gelecek hakkında öngörüde bulunmak için geçmişi bilmek gerekir. İnsan, geçmiş ile gelecek arasında yaşar.')


def ortak_kimlik_zinciri():
    """Tarihi bilmek → ortak değerler → ortak kimlik → toplumun devamlılığı; karşıt yol turuncu (kitap s. 15)."""
    ic = '<defs>' + ok_isareti('okT9y', 'g-yf') + ok_isareti('okT9t', 'g-tf') + '</defs>'
    kolon = [(12, 'yesil', 'Tarihini bilen toplum', 'okT9y',
              ('Ortak değerleri benimser', 'Ortak kimlikte birleşir', 'Varlığını sürdürür')),
             (240, 'turuncu', 'Tarihini bilmeyen toplum', 'okT9t',
              ('Ortak değerleri benimseyemez', 'Ortak kimlik oluşmaz', 'Devamlılık gösteremez'))]
    W = 220
    for x, renk, bas, ok, adimlar in kolon:
        a, s, f = RENK[renk]
        cx = x + W // 2
        ic += f'<rect x="{x}" y="8" width="{W}" height="36" rx="18" class="{f}"/>'
        ic += f'<text x="{cx}" y="31" text-anchor="middle" font-size="13.5" font-weight="800" class="g-b">{bas}</text>'
        y = 66
        ic += f'<line x1="{cx}" y1="47" x2="{cx}" y2="{y - 7}" class="{s}" stroke-width="2.5" marker-end="url(#{ok})"/>'
        for i, t in enumerate(adimlar):
            ic += _kutu(x, y, W, 38, renk)
            ic += f'<text x="{cx}" y="{y + 24}" text-anchor="middle" font-size="12.5" font-weight="700" class="{f}">{t}</text>'
            if i < len(adimlar) - 1:
                ic += f'<line x1="{cx}" y1="{y + 41}" x2="{cx}" y2="{y + 52}" class="{s}" stroke-width="2.5" marker-end="url(#{ok})"/>'
            y += 60
    # kitap s. 15: "toplumsal ve millî kimliğin oluşumunda tarih öğrenmenin payı büyüktür" (tek satıra sığmaz, iki satır)
    ic += ('<text x="236" y="250" text-anchor="middle" font-size="12.5" class="g-y">'
           'Toplumsal ve millî kimliğin oluşmasında</text>'
           '<text x="236" y="268" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">'
           'tarih öğrenmenin payı büyüktür.</text>')
    return svg(472, 280, ic, 'Tarihini bilen toplum ortak değerleri benimser, ortak kimlikte birleşir ve varlığını sürdürür. Tarihini bilmeyen toplum ortak değerleri benimseyemez, ortak kimlik oluşmaz ve devamlılık gösteremez.')


def faydalar_haritasi():
    """Tarih öğrenmenin bireye ve topluma faydaları (kitap s. 11, 13, 15-17)."""
    ic = _kutu(161, 8, 150, 36, 'mor', rx=18)
    ic += '<text x="236" y="31" text-anchor="middle" font-size="14" font-weight="800" class="g-of">TARİH ÖĞRENMEK</text>'
    # her madde kitaptaki bir cümleye dayanır; satır ≤ 26 karakter (12 pt × 0,55 × 26 ≈ 172 px < 184 px kutu içi)
    kol = [(12, 'mavi', 'Bireye faydaları',
            ('Kimlik kazandırır', 'Aile ve kökeni tanıtır', 'Bugünü anlamlandırır',
             'Öngörüye yardım eder', 'Bakış açısını genişletir', 'Sorgulamayı geliştirir',
             'Empati kurmayı geliştirir')),
           (244, 'yesil', 'Topluma faydaları',
            ('Ortak değerleri benimsetir', 'Ortak kimlik oluşturur', 'Millî bilinci güçlendirir',
             'Aidiyeti canlı tutar', 'Mücadeleleri öğretir', 'Kültürel mirası benimsetir',
             'Toplumun devamını sağlar'))]
    W = 216
    for x, renk, ad, maddeler in kol:
        _, s, f = RENK[renk]
        cx = x + W // 2
        ic += f'<line x1="{236 + (-40 if x < 236 else 40)}" y1="46" x2="{cx}" y2="62" class="g-c" stroke-width="2"/>'
        ic += _kutu(x, 64, W, 50 + len(maddeler) * 21, renk)
        ic += f'<text x="{cx}" y="89" text-anchor="middle" font-size="14" font-weight="800" class="{f}">{ad}</text>'
        for k, m in enumerate(maddeler):
            yy = 114 + k * 21
            ic += f'<circle cx="{x + 16}" cy="{yy - 4}" r="3.5" class="{f}"/><text x="{x + 26}" y="{yy}" font-size="12" class="g-y">{m}</text>'
    return svg(472, 270, ic, 'Tarih öğrenmenin faydaları. Bireye: kimlik kazandırır, aile ve kökeni tanıtır, bugünü anlamlandırır, öngörüye yardım eder, bakış açısını genişletir, sorgulamayı geliştirir, empati kurmayı geliştirir. Topluma: ortak değerleri benimsetir, ortak kimlik oluşturur, millî bilinci güçlendirir, aidiyeti canlı tutar, mücadeleleri öğretir, kültürel mirası benimsetir, toplumun devamını sağlar.')


def uygula(o):
    g = {'Tarih nedir, geçmişi neden bilmeliyiz?': zaman_oku(),
         'Ortak kimlik ve millî bilinç': ortak_kimlik_zinciri(),
         'Tarih bakış açısını genişletir': faydalar_haritasi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
