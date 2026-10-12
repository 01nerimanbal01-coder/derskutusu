"""7. sınıf İngilizce, 3. hafta: metinden bilgi çıkarma (T/F/NI), sayılarla karşılaştırma, because ve so.

Görseller yalnız MEB 7. sınıf İngilizce ders kitabındaki bilgilerle çizilir (Appearance and Personality ünitesi, PDF s15-s20).
Renk anlamı: T = yeşil, F = turuncu, NI = mavi; kilo çubuklarında kişi başına bir renk (baba turuncu, anne mavi, öğrenci yeşil);
neden = mavi, sonuç = turuncu, bağlaç = mor.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _soru_kutusu(x, y, w, h, metin):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="g-c" stroke-width="1.8"/>'
            f'<text x="{x + w / 2:g}" y="{y + h / 2 + 5:g}" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{metin}</text>')


def karar_semasi():
    """Bir ifade için T, F ya da NI kararı (kitap s16, etkinlik 12)."""
    ic = '<defs>' + ok_isareti('okK3', 'g-s') + '</defs>'
    ic += _soru_kutusu(105, 8, 260, 38, 'Özellik metinde geçiyor mu?')
    ic += '<line x1="150" y1="46" x2="150" y2="92" class="g-c" stroke-width="2" marker-end="url(#okK3)"/>'
    ic += '<text x="160" y="76" font-size="12" font-weight="700" class="g-y">Hayır</text>'
    ic += '<line x1="320" y1="46" x2="320" y2="92" class="g-c" stroke-width="2" marker-end="url(#okK3)"/>'
    ic += '<text x="330" y="76" font-size="12" font-weight="700" class="g-y">Evet</text>'
    # NI
    ic += '<rect x="20" y="96" width="190" height="112" rx="12" class="g-mf"/>'
    ic += '<text x="115" y="142" text-anchor="middle" font-size="30" font-weight="800" class="g-b">NI</text>'
    ic += '<text x="115" y="166" text-anchor="middle" font-size="14" font-weight="700" class="g-b">Bilgi yok</text>'
    ic += '<text x="115" y="186" text-anchor="middle" font-size="12" class="g-b">Metin söz etmiyor</text>'
    # ikinci soru
    ic += _soru_kutusu(250, 96, 210, 38, 'Metindekiyle aynı mı?')
    ic += '<line x1="298" y1="134" x2="298" y2="160" class="g-c" stroke-width="2" marker-end="url(#okK3)"/>'
    ic += '<text x="308" y="154" font-size="12" font-weight="700" class="g-y">Evet</text>'
    ic += '<line x1="408" y1="134" x2="408" y2="160" class="g-c" stroke-width="2" marker-end="url(#okK3)"/>'
    ic += '<text x="418" y="154" font-size="12" font-weight="700" class="g-y">Hayır</text>'
    ic += '<rect x="246" y="164" width="104" height="44" rx="10" class="g-yf"/>'
    ic += '<text x="298" y="192" text-anchor="middle" font-size="14" font-weight="800" class="g-b">T · Doğru</text>'
    ic += '<rect x="356" y="164" width="104" height="44" rx="10" class="g-tf"/>'
    ic += '<text x="408" y="192" text-anchor="middle" font-size="14" font-weight="800" class="g-b">F · Yanlış</text>'
    return svg(470, 216, ic, 'T, F, NI karar şeması: özellik metinde geçmiyorsa NI, bilgi yok. Geçiyorsa ve metindekiyle aynıysa T, doğru; '
               'metindekinden farklıysa F, yanlış.')


def kilo_cubuklari():
    """Baba 95 kg, anne 55 kg, öğrenci 42 kg; tek ölçek: 1 kg = 3 birim (kitap s17, etkinlik 14-15)."""
    x0, olcek = 100, 3
    ic = ''
    veri = [('dad', 95, 'g-tf', 16), ('mum', 55, 'g-mf', 60), ('student', 42, 'g-yf', 104)]
    for ad, kg, sinif, y in veri:
        w = kg * olcek
        ic += f'<text x="{x0 - 8}" y="{y + 20}" text-anchor="end" font-size="13" font-weight="700" class="g-y">{ad}</text>'
        ic += f'<rect x="{x0}" y="{y}" width="{w}" height="30" rx="6" class="{sinif}"/>'
        ic += f'<text x="{x0 + w + 8}" y="{y + 20}" font-size="13" font-weight="800" class="{sinif}">{kg} kg</text>'
    ic += f'<line x1="{x0}" y1="146" x2="{x0 + 100 * olcek}" y2="146" class="g-c" stroke-width="1.5"/>'
    for kg in (0, 25, 50, 75, 100):
        x = x0 + kg * olcek
        ic += f'<line x1="{x}" y1="146" x2="{x}" y2="152" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="{x}" y="167" text-anchor="middle" font-size="11" class="g-s">{kg}</text>'
    ic += f'<text x="{x0 + 100 * olcek + 22}" y="167" font-size="11" class="g-s">kg</text>'
    ic += ('<text x="235" y="194" text-anchor="middle" font-size="13" font-weight="700" class="g-y">The <tspan class="g-tf">dad</tspan> is heavier than the '
           '<tspan class="g-mf">mum</tspan>.</text>')
    ic += ('<text x="235" y="216" text-anchor="middle" font-size="13" font-weight="700" class="g-y">The <tspan class="g-mf">mum</tspan> is heavier than the '
           '<tspan class="g-yf">student</tspan>.</text>')
    return svg(470, 228, ic, 'Kilo çubukları tek ölçekle: dad 95 kg, mum 55 kg, student 42 kg. The dad is heavier than the mum. '
               'The mum is heavier than the student.')


def _cip(x, y, metin, renk, yuk=30, boy=13):
    w = round(len(metin) * boy * 0.6 + 22)
    a, s, f = RENK[renk]
    ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{a}"/>'
          f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{s}" stroke-width="2"/>'
          f'<text x="{x + w / 2:g}" y="{y + yuk / 2 + 4.5:g}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{f}">{metin}</text>')
    return w, ic


def _sira(y, parcalar):
    """Yan yana çipleri ortalar; (başlangıç x'leri ve genişlikleri) döndürür."""
    gen = [round(len(m) * 13 * 0.6 + 22) for m, _ in parcalar]
    bosluk = 8
    toplam = sum(gen) + bosluk * (len(gen) - 1)
    x = (470 - toplam) / 2
    ic, yer = '', []
    for (m, r), w in zip(parcalar, gen):
        _, c = _cip(round(x, 1), y, m, r)
        ic += c
        yer.append((round(x, 1), w))
        x += w + bosluk
    return ic, yer


def _neden_oku(yer, kaynak, hedef, y_alt, ok):
    """Nedenin altından sonucun altına dirsekli ok."""
    xa = yer[kaynak][0] + yer[kaynak][1] / 2
    xb = yer[hedef][0] + yer[hedef][1] / 2
    return (f'<path d="M{xa:g} {y_alt + 4} V{y_alt + 22} H{xb:g} V{y_alt + 9}" fill="none" class="g-c" stroke-width="2" '
            f'stroke-linejoin="round" marker-end="url(#{ok})"/>')


def because_so():
    """Aynı neden–sonuç ilişkisi: because ve so ile (kitap s15, s18)."""
    ic = '<defs>' + ok_isareti('okN3', 'g-s') + '</defs>'
    ic += '<text x="12" y="16" font-size="12" font-weight="700" class="g-s">because ile</text>'
    s1, y1 = _sira(24, [('Ali has many friends', 'turuncu'), ('because', 'mor'), ('he is outgoing', 'mavi')])
    ic += s1 + _neden_oku(y1, 2, 0, 54, 'okN3')
    ic += '<text x="12" y="100" font-size="12" font-weight="700" class="g-s">so ile</text>'
    s2, y2 = _sira(108, [('Ali is outgoing', 'mavi'), (', so', 'mor'), ('he has many friends', 'turuncu')])
    ic += s2 + _neden_oku(y2, 0, 2, 138, 'okN3')
    for x, ad, renk in ((110, 'Neden', 'mavi'), (210, 'Sonuç', 'turuncu'), (310, 'Bağlaç', 'mor')):
        ic += f'<circle cx="{x}" cy="190" r="6" class="{RENK[renk][2]}"/><text x="{x + 12}" y="194" font-size="12" class="g-y">{ad}</text>'
    return svg(470, 204, ic, 'Aynı ilişki iki cümleyle: Ali has many friends because he is outgoing; Ali is outgoing, so he has many friends. '
               'Ok iki cümlede de nedenden sonuca gider. Mavi neden, turuncu sonuç, mor bağlaç.')


def uygula(o):
    g = {'Doğru, yanlış, bilgi yok': karar_semasi(),
         'Sayılara bakarak karşılaştırma': kilo_cubuklari(),
         'Because ve so: neden ve sonuç': because_so()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
