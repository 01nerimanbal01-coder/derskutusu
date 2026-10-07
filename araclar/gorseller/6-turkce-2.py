"""6. sınıf Türkçe, 2. hafta: Bir Kelime Seyyahı (konu–ayrıntı, boy damgaları, izleme, paragraf yazma).

Görseller yalnız MEB 6. sınıf Türkçe ders kitabındaki bilgilerle çizilir (kitap s. 14-22).
Damga şekilleri kitaptaki damga tablosundan (s. 19) 0-100 kutusuna ölçeklenerek çizilmiştir.
Renk anlamı: mavi = konu / harfe benzeyen damga / yazmadan önceki seçimler,
turuncu = ayrıntı / geometrik şekilli damga, yeşil = doğadaki şekle benzeyen damga / yazarken,
mor = işaretlerinden biri yön değiştiren damga, gri = ipucu verilmeyen örnek damga.
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


def konu_ayrinti():
    """Konu: Mahmut'un kelimelere merakı; tepük, dede, aile, medrese ayrıntıdır (kitap s. 14-17)."""
    ic = '<rect x="96" y="8" width="280" height="54" rx="14" class="g-mf"/>'
    ic += '<text x="236" y="29" text-anchor="middle" font-size="12" font-weight="700" class="g-b">KONU</text>'
    ic += ('<text x="236" y="50" text-anchor="middle" font-size="15" font-weight="800" class="g-b">'
           'Mahmut\'un kelimelere merakı</text>')
    ayrinti = [('Tepük oyunu', 've adı'), ('Dedesiyle', 'sevgi bağı'),
               ('Ailesi ve', 'Karahanlılar'), ('Medrese, at,', 'ok ve kargı')]
    for i, (s1, s2) in enumerate(ayrinti):
        x = 8 + i * 116
        cx = x + 54
        ic += f'<line x1="236" y1="62" x2="{cx}" y2="104" class="g-c" stroke-width="2"/>'
        ic += _kutu(x, 104, 108, 58, 'turuncu')
        ic += f'<text x="{cx}" y="128" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="147" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s2}</text>'
    ic += ('<text x="236" y="188" text-anchor="middle" font-size="12.5" class="g-y">'
           '<tspan font-weight="800" class="g-mf">Konu</tspan> metnin bütününü kapsar; '
           '<tspan font-weight="800" class="g-tf">ayrıntılar</tspan> konuyu destekler.</text>')
    return svg(472, 200, ic, 'Konu ve ayrıntılar: Metnin konusu Mahmut\'un kelimelere merakıdır. '
               'Tepük oyunu ve adı, dedesiyle sevgi bağı, ailesi ve Karahanlılar, medrese, at, ok ve kargı konuyu destekleyen ayrıntılardır.')


# Kitap s. 19 damga tablosu (sıra kitaptaki gibi): (boy, renk, [yol, ...])
DAMGA = [
    ('Bayat', 'turuncu', ['M29 16V84', 'M41 16V84', 'M41 42L54 16', 'M70 40V84', 'M60 40L80 40L70 15Z']),
    ('Kayı', 'mavi', ['M27 18V78', 'M33 18L51 78L68 18', 'M75 18V78']),
    ('Eymür', 'turuncu', ['M53 5L71 23L53 40L36 23Z', 'M53 40V89', 'M18 45H88']),
    ('Çavuldur', 'yesil', ['M6 62L38 35Q48 27 58 34L93 62', 'M20 62L41 45Q48 39 55 44L76 62']),
    ('İğdir', 'yesil', ['M80 14L30 44H80L32 73']),
    ('Büğdüz', None, ['M29 46V25H79', 'M15 46H88L57 71H85']),
    ('Ala Yuntlu', 'turuncu', ['M32 22V47', 'M6 47H94', 'M6 56H94', 'M6 66H94']),
    ('Bayundur', 'mavi', ['M17 16H81V40H17', 'M17 16V64H81V77']),
    ('Karaeyli', 'turuncu', ['M9 47H37V60H9Z', 'M42 60Q62.5 25.5 93 61', 'M54 60Q67 42 80 60']),
    ('Döğer', 'mor', ['M19 19V75', 'M36 19L62 54C70 63 72 74 60 75C47 76 45 66 53 57L88 19']),
    ('Dodurga', 'mor', ['M13 21L35 71L57 21', 'M49 71L71 21L94 71']),
    ('Peçenek', 'mor', ['M18 39L62 56C68 58 70 55 70 52C70 49 66 48 62 50L18 65', 'M79 26V67']),
]


def damgalar():
    """On iki boyun damgası; renk, kitaptaki ipucunun türünü gösterir (kitap s. 19)."""
    ic = ''
    for i, (ad, renk, yollar) in enumerate(DAMGA):
        x = 6 + (i % 6) * 78
        y = 6 + (i // 6) * 96
        if renk:
            a, s, f = RENK[renk]
            ic += f'<rect x="{x}" y="{y}" width="70" height="66" rx="10" class="{a}"/>'
            ic += f'<rect x="{x}" y="{y}" width="70" height="66" rx="10" class="{s}" stroke-width="1.6"/>'
        else:
            s, f = 'g-c', 'g-s'
            ic += f'<rect x="{x}" y="{y}" width="70" height="66" rx="10" class="g-z"/>'
            ic += f'<rect x="{x}" y="{y}" width="70" height="66" rx="10" class="g-c" stroke-width="1.6" stroke-dasharray="4 3"/>'
        ic += (f'<g transform="translate({x + 5} {y + 3}) scale(0.6)" class="{s}" stroke-width="5.5" '
               'stroke-linecap="round" stroke-linejoin="round">')
        ic += ''.join(f'<path d="{d}"/>' for d in yollar)
        ic += '</g>'
        ic += f'<text x="{x + 35}" y="{y + 84}" text-anchor="middle" font-size="12" font-weight="800" class="{f}">{ad}</text>'
    # açıklama satırı
    lejant = [('mavi', 'harfe benzer', 76), ('turuncu', 'geometrik', 62), ('yesil', 'doğadan', 52),
              ('mor', 'yönü değişen', 80), (None, 'örnek', 40)]
    toplam = sum(w + 17 for _, _, w in lejant) + 14 * (len(lejant) - 1)
    x = (472 - toplam) / 2
    for renk, metin, w in lejant:
        if renk:
            a, s, f = RENK[renk]
            ic += f'<rect x="{x:.1f}" y="201" width="12" height="12" rx="3" class="{f}"/>'
        else:
            ic += f'<rect x="{x:.1f}" y="201" width="12" height="12" rx="3" class="g-c" stroke-width="1.6" stroke-dasharray="3 2"/>'
        ic += f'<text x="{x + 17:.1f}" y="211.5" font-size="12" class="g-y">{metin}</text>'
        x += w + 17 + 14
    return svg(472, 222, ic, 'Türk boylarının damgaları: Bayat, Kayı, Eymür, Çavuldur, İğdir, Büğdüz, Ala Yuntlu, Bayundur, '
               'Karaeyli, Döğer, Dodurga ve Peçenek. Mavi damgalar harfe, yeşil damgalar doğadaki şekillere benzer; '
               'turuncu damgalarda üçgen, dörtgen, dikdörtgen ya da paralel çizgi vardır; mor damgalarda bir işaret yön değiştirir. '
               'Büğdüz damgası ipucu verilmeyen örnektir.')


def izleme_adimlari():
    """İzlemeden önce tahmin, izlerken not, izledikten sonra değerlendirme; tahmin göstergesi (kitap s. 18-19)."""
    ic = '<defs>' + ok_isareti('okT62i', 'g-s') + '</defs>'
    sutun = [(8, 'mavi', 'İzlemeden önce', ('Başlığı ve', 'görselleri incele', 'Konuyu tahmin et', 'Gerekçeni yaz')),
             (168, 'turuncu', 'İzlerken', ('Önemli bilgileri', 'tabloya not al', 'Gerekirse', 'yeniden izle')),
             (328, 'yesil', 'İzledikten sonra', ('Tahminini ve', 'gerekçeni', 'değerlendir'))]
    for x, renk, bas, satir in sutun:
        a, s, f = RENK[renk]
        cx = x + 68
        ic += _kutu(x, 8, 136, 128, renk)
        ic += f'<rect x="{x}" y="8" width="136" height="32" rx="12" class="{f}"/>'
        ic += f'<text x="{cx}" y="29" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{bas}</text>'
        for k, t in enumerate(satir):
            ic += f'<text x="{cx}" y="{62 + k * 19}" text-anchor="middle" font-size="12.5" class="g-y">{t}</text>'
    for x in (148, 308):
        ic += f'<line x1="{x}" y1="72" x2="{x + 12}" y2="72" class="g-c" stroke-width="2" marker-end="url(#okT62i)"/>'
    ic += ('<text x="236" y="160" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">'
           'Tahminim sonuca ne kadar yaklaştı?</text>')
    gosterge = [('turuncu', 'Pek yaklaşmamışım'), ('mavi', 'Biraz yaklaşmışım'), ('yesil', 'Tam isabet!')]
    for i, (renk, t) in enumerate(gosterge):
        x = 8 + i * 154
        ic += _kutu(x, 170, 148, 30, renk, rx=15)
        ic += f'<text x="{x + 74}" y="190" text-anchor="middle" font-size="12.5" font-weight="700" class="{RENK[renk][2]}">{t}</text>'
    return svg(472, 208, ic, 'İzleme adımları: İzlemeden önce başlığı ve görselleri inceleyip konuyu tahmin et, gerekçeni yaz. '
               'İzlerken önemli bilgileri tabloya not al, gerekirse yeniden izle. İzledikten sonra tahminini ve gerekçeni değerlendir. '
               'Tahmin göstergesi: Pek yaklaşmamışım, Biraz yaklaşmışım, Tam isabet.')


def yazma_adimlari():
    """Yazmadan önce üç seçim (konu, hedef kitle, ortam); yazarken başlatma, sürdürme, sonlandırma (kitap s. 21)."""
    ic = '<defs>' + ok_isareti('okT62y', 'g-yf') + '</defs>'
    secim = [('1. Konu', 'Ne yazacağım?'), ('2. Hedef kitle', 'Kim okuyacak?'), ('3. Yazma ortamı', 'Nerede yazacağım?')]
    for i, (bas, alt) in enumerate(secim):
        x = 8 + i * 155
        cx = x + 73
        ic += _kutu(x, 8, 146, 58, 'mavi')
        ic += f'<text x="{cx}" y="32" text-anchor="middle" font-size="13.5" font-weight="800" class="g-mf">{bas}</text>'
        ic += f'<text x="{cx}" y="52" text-anchor="middle" font-size="12.5" class="g-y">{alt}</text>'
        ic += f'<line x1="{cx}" y1="68" x2="{cx}" y2="88" class="g-ys" stroke-width="2" marker-end="url(#okT62y)"/>'
    ic += _kutu(8, 96, 456, 116, 'yesil')
    satir = [('Başlatma', 'okuru konuya hazırlar'), ('Sürdürme', 'düşünceleri birbirine bağlar'),
             ('Sonlandırma', 'yazıyı toparlar')]
    for k, (bas, alt) in enumerate(satir):
        y = 106 + k * 34
        ic += f'<rect x="20" y="{y}" width="124" height="28" rx="14" class="g-yf"/>'
        ic += f'<text x="82" y="{y + 19}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{bas}</text>'
        ic += f'<text x="158" y="{y + 19}" font-size="12.5" class="g-y">ifadesi: {alt}</text>'
    return svg(472, 220, ic, 'Paragraf yazma adımları: Yazmadan önce konu, hedef kitle ve yazma ortamı seçilir. '
               'Yazarken başlatma ifadesi okuru konuya hazırlar, sürdürme ifadeleri düşünceleri birbirine bağlar, '
               'sonlandırma ifadesi yazıyı toparlar.')


def uygula(o):
    g = {'Metnin konusu ve ayrıntıları': konu_ayrinti(),
         'Türk boylarının damgaları': damgalar(),
         'Tahmin ederek izleme': izleme_adimlari(),
         'Adım adım paragraf yazma': yazma_adimlari()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
