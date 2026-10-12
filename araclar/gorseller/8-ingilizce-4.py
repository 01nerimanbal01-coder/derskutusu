"""8. sınıf İngilizce, 4. hafta (2 Teen Life): etkinlik–fiil eşleşmeleri, sıklık zarfları, hoşlanma/hoşlanmama kalıpları, zaman edatları, enerji anketi puanı.

Görseller yalnız MEB 8. sınıf İngilizce ders kitabındaki bilgilerle çizilir (Teen Life ünitesi, PDF s24–s30).
Renk anlamı: go = mavi, play = yeşil, do = turuncu, diğer fiiller = mor; hoşlanma = yeşil, hoşlanmama = turuncu;
in = mavi, on = turuncu, at = yeşil; puan aralıkları 5–10 mavi, 10–20 turuncu, 20–30 yeşil (tek ölçek: 1 puan = 17 birim).
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu/yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="1.8"/>')


def _baslik(metin, genislik=470):
    return f'<text x="{genislik / 2:g}" y="21" text-anchor="middle" font-size="15" font-weight="700" class="g-y">{metin}</text>'


def _cip_genislik(metin, boy=12):
    return round(len(metin) * boy * 0.6 + 20)


def etkinlik_fiilleri():
    """go / play / do ile kurulan etkinlikler ve diğer fiiller (kitap s24)."""
    ic = _baslik('Etkinlik ve fiil eşleşmeleri')
    paneller = [(12, 'go', 'mavi', ['to a concert', 'trekking', 'bowling']),
                (163, 'play', 'yesil', ['soccer']),
                (314, 'do', 'turuncu', ['karate'])]
    for x, fiil, renk, ogeler in paneller:
        a, s, f = RENK[renk]
        ic += _kutu(x, 34, 144, 120, renk)
        ic += f'<text x="{x + 72}" y="60" text-anchor="middle" font-size="18" font-weight="800" class="{f}">{fiil}</text>'
        for i, oge in enumerate(ogeler):
            ic += f'<text x="{x + 72}" y="{88 + i * 24}" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{oge}</text>'
    ic += '<text x="12" y="180" font-size="12.5" font-weight="700" class="g-of">Başka fiillerle söylenenler</text>'
    ogeler = ['watch a film', 'read a book', 'ride a bike', 'draw pictures', 'surf the internet', 'prepare dinner', 'spend time with relatives']
    x, y = 12, 190
    for oge in ogeler:
        w = _cip_genislik(oge)
        if x + w > 458:
            x, y = 12, y + 38
        ic += _kutu(x, y, w, 30, 'mor', rx=9)
        ic += f'<text x="{x + w / 2:g}" y="{y + 19.5}" text-anchor="middle" font-size="12" font-weight="700" class="g-of">{oge}</text>'
        x += w + 8
    return svg(470, y + 40, ic, 'Etkinlik ve fiil eşleşmeleri: go ile to a concert, trekking, bowling; play ile soccer; do ile karate. '
               'Başka fiillerle watch a film, read a book, ride a bike, draw pictures, surf the internet, prepare dinner ve spend time with relatives söylenir.')


def siklik_merdiveni():
    """Sıklık zarflarının azdan çoğa sırası (kitap s26)."""
    ic = '<defs>' + ok_isareti('okK41', 'g-s') + '</defs>' + _baslik('Sıklık zarfları: azdan çoğa')
    adlar = ['never', 'rarely', 'sometimes', 'often', 'usually', 'always']
    taban = 172
    for i in range(6):
        x = 30 + i * 70
        h = 28 + i * 20
        ic += f'<rect x="{x}" y="{taban - h}" width="60" height="{h}" rx="8" class="g-mf"/>'
    for i in (2, 0, 5, 1, 4, 3):  # etiketler yer koordinatlarıyla konur; okuma sırası görsel sırayı bozmaz
        ic += f'<text x="{30 + i * 70 + 30}" y="{taban + 18}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{adlar[i]}</text>'
    ic += '<text x="30" y="64" font-size="13" font-weight="700" class="g-y">I <tspan class="g-of">always</tspan> wake up early.</text>'
    ic += '<text x="30" y="82" font-size="11.5" class="g-s">zarf ana fiilden önce gelir</text>'
    ic += f'<line x1="44" y1="208" x2="426" y2="208" class="g-c" stroke-width="2" marker-end="url(#okK41)"/>'
    ic += '<text x="30" y="228" font-size="12" font-weight="700" class="g-s">az</text>'
    ic += '<text x="440" y="228" text-anchor="end" font-size="12" font-weight="700" class="g-s">çok</text>'
    return svg(470, 236, ic, 'Sıklık zarfları azdan çoğa sıralanır: en az never, en çok always; arada rarely, sometimes, often ve usually yer alır. Zarf ana fiilden önce gelir: I always wake up early.')


def sevme_sevmeme():
    """Hoşlanma ve hoşlanmama kalıpları, görüş sıfatları (kitap s25, s28, s30)."""
    ic = _baslik('Hoşlanma ve hoşlanmama kalıpları')
    sol = ['love · like · enjoy + -ing', 'be fond of + isim / -ing', 'be keen on + isim / -ing']
    sag = ['hate · dislike + -ing', 'can’t stand + isim']
    for x, ad, renk, satirlar, ornek in ((12, 'Hoşlanma', 'yesil', sol, 'I enjoy riding my bike.'),
                                         (241, 'Hoşlanmama', 'turuncu', sag, 'I can’t stand loud music.')):
        f = RENK[renk][2]
        ic += _kutu(x, 34, 217, 128, renk)
        ic += f'<text x="{x + 108.5}" y="58" text-anchor="middle" font-size="14" font-weight="800" class="{f}">{ad}</text>'
        for i, s in enumerate(satirlar):
            ic += f'<text x="{x + 14}" y="{84 + i * 22}" font-size="12" font-weight="700" class="g-y">{s}</text>'
        ic += f'<text x="{x + 14}" y="148" font-size="12" class="g-s">{ornek}</text>'
    ic += '<text x="12" y="188" font-size="12.5" font-weight="700" class="g-y">I think … is …</text>'
    satirlar = [(204, 'yesil', ['exciting', 'trendy', 'popular', 'enjoyable']),
                (238, 'yesil', ['amazing', 'fascinating', 'terrific']),
                (272, 'turuncu', ['unbearable', 'ridiculous'])]
    for y, renk, ogeler in satirlar:
        x = 12
        for oge in ogeler:
            w = _cip_genislik(oge)
            ic += _kutu(x, y, w, 28, renk, rx=9)
            ic += f'<text x="{x + w / 2:g}" y="{y + 18.5}" text-anchor="middle" font-size="12" font-weight="700" class="{RENK[renk][2]}">{oge}</text>'
            x += w + 8
    return svg(470, 312, ic, 'Hoşlanma: love, like, enjoy fiilleri ve ardından -ing; be fond of ve be keen on ardından isim ya da -ing. '
               'Hoşlanmama: hate, dislike ve ardından -ing; can’t stand ve ardından isim. Olumlu görüş sıfatları exciting, trendy, popular, enjoyable, amazing, fascinating, terrific; '
               'olumsuz görüş sıfatları unbearable ve ridiculous.')


def edat_tablosu():
    """in / on / at ile zaman (kitap s29)."""
    ic = _baslik('Zaman edatları')
    paneller = [(12, 'in', 'mavi', ['June', 'summer', '1980', 'the morning', 'the afternoon', 'the evening']),
                (163, 'on', 'turuncu', ['Sundays', 'weekdays', '20th May', 'Saturday morning']),
                (314, 'at', 'yesil', ['7 o’clock', 'noon', 'night', 'lunchtime', 'the weekend'])]
    for x, edat, renk, ogeler in paneller:
        f = RENK[renk][2]
        ic += _kutu(x, 34, 144, 192, renk)
        ic += f'<text x="{x + 72}" y="66" text-anchor="middle" font-size="22" font-weight="800" class="{f}">{edat}</text>'
        for i, oge in enumerate(ogeler):
            ic += f'<text x="{x + 72}" y="{98 + i * 22}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{oge}</text>'
    return svg(470, 238, ic, 'Zaman edatları: in ile June, summer, 1980, the morning, the afternoon, the evening; on ile Sundays, weekdays, 20th May, Saturday morning; '
               'at ile 7 o’clock, noon, night, lunchtime, the weekend kullanılır.')


def puan_cetveli():
    """Enerji anketi: A = 5, B = 3, C = 1 puan ve sonuç aralıkları (kitap s27). Tek ölçek: 1 puan = 17 birim."""
    olcek, x0 = 17, 20

    def konum(p):
        return x0 + (p - 5) * olcek
    ic = _baslik('Enerji anketi: puan aralıkları')
    ic += '<text x="235" y="42" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">A = 5 puan · B = 3 puan · C = 1 puan</text>'
    bantlar = [(5, 10, 'mavi'), (10, 20, 'turuncu'), (20, 30, 'yesil')]
    for a, b, renk in bantlar:
        x, w = konum(a), (b - a) * olcek
        ic += f'<rect x="{x}" y="54" width="{w}" height="34" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + w / 2:g}" y="76" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{a}–{b}</text>'
    for p in (5, 10, 20, 30):
        ic += f'<line x1="{konum(p)}" y1="88" x2="{konum(p)}" y2="95" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="{konum(p)}" y="110" text-anchor="middle" font-size="11" class="g-s">{p}</text>'
    aciklamalar = [('mavi', '5–10 puan: daha enerjik olmaya çalış'),
                   ('turuncu', '10–20 puan: fena değil, daha iyi olabilir'),
                   ('yesil', '20–30 puan: çok etkileyici, gerçekten enerjik')]
    for i, (renk, metin) in enumerate(aciklamalar):
        y = 138 + i * 24
        ic += f'<circle cx="26" cy="{y - 4}" r="6" class="{RENK[renk][2]}"/><text x="40" y="{y}" font-size="12.5" class="g-y">{metin}</text>'
    return svg(470, 214, ic, 'Enerji anketinde A seçeneği 5, B seçeneği 3, C seçeneği 1 puan verir. 5–10 puan daha enerjik olmaya çalışmayı, '
               '10–20 puan fena olmadığını ama daha iyi olunabileceğini, 20–30 puan çok etkileyici ve gerçekten enerjik olmayı gösterir.')


def uygula(o):
    g = {'Boş zaman etkinlikleri ve doğru fiil': etkinlik_fiilleri(),
         'Sıklık zarfları': siklik_merdiveni(),
         'Sevdiğini ve sevmediğini söyleme': sevme_sevmeme(),
         'Günlük etkinlikleri sorma ve zamanı doğru edatla söyleme': edat_tablosu(),
         'Enerji anketi ve dinleme notları': puan_cetveli()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
