"""7. sınıf Türkçe, 3. hafta: Gençliğin Kıymeti (ağaç ve insan, tahmin döngüsü, düşünceyi geliştirme yolları, ikilemeler, üç nokta).

Görseller yalnız MEB 7. sınıf Türkçe ders kitabındaki bilgilerle çizilir (PDF sayfaları s30-s35, s72); metin cümleleri görsele alınmaz.
Renk anlamı:
- Ağaç ve insan: yeşil = ağaç, turuncu = insan, mor = yetişkin (bahçıvan).
- Tahmin döngüsü: mavi = belirle, yeşil = ipucu bul, turuncu = tahmin et, mor = sözlükle kontrol.
- Düşünceyi geliştirme yolları: mavi = tanık gösterme, yeşil = benzetme, turuncu = örneklendirme, mor = karşılaştırma.
- İkilemeler: turuncu = yanlış yazım, yeşil = doğru yazım.
- Üç nokta: mavi, yeşil, mor = üç görev; turuncu = ünlem ve soru işaretinden sonra iki nokta uyarısı.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, yazı, koyu dolgu)
    'mavi': ('g-ma', 'g-ms', 'g-mf', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _yazi(x, y, metin, boyut=12, sinif='g-y', kalin=False, ankraj='start'):
    agirlik = ' font-weight="800"' if kalin else ''
    return f'<text x="{x:g}" y="{y:g}" text-anchor="{ankraj}" font-size="{boyut:g}"{agirlik} class="{sinif}">{metin}</text>'


def _hap(x, y, w, h, renk, metin):
    a, _, f, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h // 2}" class="{a}"/>'
            + _yazi(x + w / 2, y + h / 2 + 4.3, metin, 12, f, True, 'middle'))


def agac_insan():
    """Ağacın çiçek açıp meyve vermesi ile insanın genç ve olgun yılları; bahçıvan = gençlere destek olan yetişkin (s30-s31)."""
    ic = '<defs>' + ok_isareti('okT3a', 'g-yf') + ok_isareti('okT3b', 'g-tf') + ok_isareti('okT3c', 'g-of') + '</defs>'
    # satır 1: ağaç
    ic += _hap(6, 34, 74, 24, 'yesil', 'Ağaç')
    ic += _kutu(88, 14, 150, 64, 'yesil')
    ic += _yazi(102, 38, 'İlkbahar', 13.5, 'g-yf', True)
    ic += _yazi(102, 60, 'çiçek açar', 12)
    ic += _kutu(322, 14, 142, 64, 'yesil')
    ic += _yazi(336, 38, 'Meyve zamanı', 13.5, 'g-yf', True)
    ic += _yazi(336, 60, 'olgun şeftali', 12)
    ic += '<line x1="242" y1="46" x2="316" y2="46" class="g-ys" stroke-width="2.5" stroke-linecap="round" marker-end="url(#okT3a)"/>'
    # satır 2: insan
    ic += _hap(6, 138, 74, 24, 'turuncu', 'İnsan')
    ic += _kutu(88, 118, 150, 64, 'turuncu')
    ic += _yazi(102, 142, 'Gençlik', 13.5, 'g-tf', True)
    ic += _yazi(102, 164, 'hazırlanma dönemi', 12)
    ic += _kutu(322, 118, 142, 64, 'turuncu')
    ic += _yazi(336, 140, 'Olgun yaş', 13.5, 'g-tf', True)
    ic += _yazi(336, 158, 'kendine ve topluma', 11.5)
    ic += _yazi(336, 174, 'yararlı olma', 11.5)
    ic += '<line x1="242" y1="150" x2="316" y2="150" class="g-ts" stroke-width="2.5" stroke-linecap="round" marker-end="url(#okT3b)"/>'
    # ağaç ile insan arasındaki karşılıklar (kesikli)
    for cx in (163, 393):
        ic += f'<line x1="{cx}" y1="80" x2="{cx}" y2="116" class="g-c" stroke-width="1.8" stroke-dasharray="5 4"/>'
    ic += _yazi(172, 102, 'benzetme', 11, 'g-s')
    ic += _yazi(402, 102, 'benzetme', 11, 'g-s')
    # satır 3: bahçıvan
    ic += _hap(6, 215, 74, 24, 'mor', 'Yetişkin')
    ic += _kutu(88, 204, 376, 46, 'mor')
    ic += ('<text x="102" y="232" font-size="12.5" class="g-y"><tspan font-weight="800" class="g-of">Bahçıvan</tspan>'
           '<tspan> = gençlere destek olan yetişkin</tspan></text>')
    ic += '<line x1="163" y1="202" x2="163" y2="190" class="g-os" stroke-width="2.5" stroke-linecap="round" marker-end="url(#okT3c)"/>'
    ic += _yazi(172, 197, 'destek', 11, 'g-s')
    return svg(472, 262, ic, 'Ağaç ve insan karşılaştırması: Ağaçta ilkbaharda çiçek açar, meyve zamanında olgun şeftali oluşur. '
               'İnsanda gençlik hazırlanma dönemidir, olgun yaş kendine ve topluma yararlı olma dönemidir. Kesikli çizgiler ağaçtaki durumun insandaki karşılığını gösterir. '
               'Bahçıvan, gençlere destek olan yetişkindir ve gençliğe destek olur.')


def tahmin_dongusu():
    """Bilmediğin sözcük: belirle, ipucu bul, tahmin et, sözlükle kontrol et; uyuşmazsa tahmini düzelt (s30, s32, s72)."""
    adimlar = [
        ('mavi', 'Belirle', 'bilmediğin', 'sözcük'),
        ('yesil', 'İpucu bul', 'çevredeki', 'cümleler'),
        ('turuncu', 'Tahmin et', 'ön bilginle', 'birleştir'),
        ('mor', 'Kontrol et', 'sözlükle', 'karşılaştır'),
    ]
    ic = '<defs>' + ok_isareti('okT3d', 'g-s') + '</defs>'
    for i, (renk, baslik, s1, s2) in enumerate(adimlar):
        x = 6 + i * 122
        _, _, yaz, koyu = RENK[renk]
        ic += _kutu(x, 8, 98, 98, renk)
        ic += f'<circle cx="{x + 49}" cy="32" r="12" class="{koyu}"/>'
        ic += _yazi(x + 49, 37, str(i + 1), 13, 'g-b', True, 'middle')
        ic += _yazi(x + 49, 66, baslik, 13, yaz, True, 'middle')
        ic += _yazi(x + 49, 83, s1, 11.5, 'g-y', False, 'middle')
        ic += _yazi(x + 49, 98, s2, 11.5, 'g-y', False, 'middle')
        if i < 3:
            ic += f'<line x1="{x + 102}" y1="57" x2="{x + 118}" y2="57" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT3d)"/>'
    ic += '<path d="M421 108 V124 H299 V113" class="g-c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#okT3d)"/>'
    ic += _yazi(360, 144, 'uyuşmazsa tahmini düzelt', 11.5, 'g-s', False, 'middle')
    return svg(472, 154, ic, 'Anlam tahmini dört adımda yapılır: bir, bilmediğin sözcüğü belirle; iki, çevredeki cümlelerde ipucu bul; '
               'üç, ipuçlarını ön bilginle birleştirip tahmin et; dört, sözlükle karşılaştırarak kontrol et. Tahmin sözlükle uyuşmazsa üçüncü adıma dönüp tahmini düzelt.')


def yollar():
    """Düşünceyi geliştirme yolları ve Gençliğin Kıymeti'ndeki karşılıkları (s32)."""
    kartlar = [
        (8, 8, 'mavi', 'Tanık gösterme', 'Birinin sözüne başvurur.', 'Filozofun nehir sözü'),
        (240, 8, 'yesil', 'Benzetme', 'Başka bir şeye benzetir.', 'Ömür ve mevsimler'),
        (8, 120, 'turuncu', 'Örneklendirme', 'Somut bir örnekle açıklar.', 'Çiçekli şeftali ağacı'),
        (240, 120, 'mor', 'Karşılaştırma', 'Farkı belirginleştirir.', 'Bol ve azalan vakit'),
    ]
    ic = ''
    for x, y, renk, ad, ne, ornek in kartlar:
        _, kenar, yaz, _ = RENK[renk]
        ic += _kutu(x, y, 224, 104, renk)
        ic += _yazi(x + 14, y + 28, ad, 14, yaz, True)
        ic += f'<line x1="{x + 14}" y1="{y + 40}" x2="{x + 210}" y2="{y + 40}" class="{kenar}" stroke-width="1.4"/>'
        ic += _yazi(x + 14, y + 64, ne, 12)
        ic += (f'<text x="{x + 14}" y="{y + 88}" font-size="11.5" class="g-y"><tspan font-weight="800" class="g-s">Örnek: </tspan>'
               f'<tspan>{ornek}</tspan></text>')
    return svg(472, 232, ic, 'Düşünceyi geliştirme yolları: mavi, tanık gösterme birinin sözüne başvurur, örnek filozofun nehir sözü. '
               'Yeşil, benzetme başka bir şeye benzetir, örnek ömür ve mevsimler. Turuncu, örneklendirme somut bir örnekle açıklar, örnek çiçekli şeftali ağacı. '
               'Mor, karşılaştırma farkı belirginleştirir, örnek bol ve azalan vakit.')


def ikileme():
    """İkilemelerin yanlış ve doğru yazımı (s34): sözcükler ayrı yazılır, araya virgül ya da kısa çizgi girmez."""
    cift = [('arada, sırada', 'arada sırada'), ('iyi-kötü', 'iyi kötü'), ('çolukçocuk', 'çoluk çocuk'),
            ('omuzomuza', 'omuz omuza'), ('gündengüne', 'günden güne')]
    ic = '<defs>' + ok_isareti('okT3e', 'g-s') + '</defs>'
    ic += '<rect x="8" y="8" width="212" height="28" rx="14" class="g-ta"/>'
    ic += _yazi(114, 27, 'Yanlış yazım', 13, 'g-tf', True, 'middle')
    ic += '<rect x="252" y="8" width="212" height="28" rx="14" class="g-ya"/>'
    ic += _yazi(358, 27, 'Doğru yazım', 13, 'g-yf', True, 'middle')
    for i, (yanlis, dogru) in enumerate(cift):
        y = 44 + i * 42
        ic += _kutu(8, y, 212, 34, 'turuncu', rx=10)
        ic += _yazi(114, y + 23, yanlis, 15, 'g-y', False, 'middle')
        ic += _kutu(252, y, 212, 34, 'yesil', rx=10)
        ic += _yazi(358, y + 23, dogru, 15, 'g-y', False, 'middle')
        ic += f'<line x1="226" y1="{y + 17}" x2="247" y2="{y + 17}" class="g-c" stroke-width="2" stroke-linecap="round" marker-end="url(#okT3e)"/>'
    return svg(472, 254, ic, 'İkilemelerin yazımı: turuncu sütun yanlış, yeşil sütun doğru yazımdır. Arada, sırada yerine arada sırada; iyi-kötü yerine iyi kötü; '
               'çolukçocuk yerine çoluk çocuk; omuzomuza yerine omuz omuza; gündengüne yerine günden güne yazılır.')


def uc_nokta():
    """Üç noktanın üç görevi ve ünlem-soru uyarısı (s35)."""
    nokta = '<tspan class="g-y" font-weight="800" font-size="16">…</tspan>'
    nokta_mor = '<tspan class="g-y" font-weight="800" font-size="16">..</tspan>'
    kartlar = [
        (8, 'mavi', '1', 'Konuşmada eksik bırakılan cevap',
         f'<tspan>— Sınavda kaç soru yaptın?  — Şey</tspan>{nokta}'),
        (78, 'yesil', '2', 'Ünlemde ve seslenmede anlatımı pekiştirir',
         f'<tspan>Ah</tspan>{nokta}<tspan> keşke daha erken başlasaydım!</tspan>'),
        (148, 'mor', '3', 'Sözü keser, devamını okura bırakır',
         f'<tspan>Yağmur dindi, bulutlar açıldı ve</tspan>{nokta}'),
        (218, 'turuncu', '!', 'Ünlem ve soru sonrası: iki nokta',
         f'<tspan>Dur!</tspan>{nokta_mor}<tspan>   Nereye gidiyorsun?</tspan>{nokta_mor}'),
    ]
    ic = ''
    for y, renk, no, baslik, ornek in kartlar:
        _, _, yaz, koyu = RENK[renk]
        ic += _kutu(8, y, 456, 62, renk)
        ic += f'<circle cx="34" cy="{y + 22}" r="11" class="{koyu}"/>'
        ic += _yazi(34, y + 27, no, 13, 'g-b', True, 'middle')
        ic += _yazi(54, y + 27, baslik, 13.5, yaz, True)
        ic += f'<text x="26" y="{y + 50}" font-size="13" class="g-y">{ornek}</text>'
    return svg(472, 288, ic, 'Üç noktanın görevleri: bir, konuşmada eksik bırakılan cevap; iki, ünlemde ve seslenmede anlatımı pekiştirmek; '
               'üç, sözü keserek devamını okura bırakmak. Dördüncü kutu uyarıdır: ünlem ve soru işaretinden sonra üç nokta yerine iki nokta yazılır.')


def uygula(o):
    g = {'Ömrün ilkbaharı: bahar ve gençlik': agac_insan(),
         'Okurken anlam tahmini ve öz değerlendirme': tahmin_dongusu(),
         'Düşünceyi geliştirme yolları': yollar(),
         'İkilemelerin yazımı': ikileme(),
         'Üç noktanın görevleri': uc_nokta()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
