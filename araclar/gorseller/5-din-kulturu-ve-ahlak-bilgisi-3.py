"""5. sınıf Din Kültürü ve Ahlak Bilgisi, 3. hafta: gökteki ahenk, mevsimlerdeki bağlantılar, tevhidin dört yönü.

Görseller yalnız MEB 5. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir (kitap PDF s. 22-23, 26-27).
Renk anlamı: mavi = Dünya’nın hareketleri ve kış (gece-gündüz, mevsimler, kar), turuncu = Dünya’nın Güneş’e uzaklığı,
yaz ve tevhit kavramı, yeşil = ilkbahar; tevhidin dört yönü mavi kutularla gösterilir.
Çizimlerde ölçü ve uzaklık yoktur; yalnız neden-sonuç ilişkileri gösterilir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def _satirlar(cx, ilk_y, aralik, satirlar, boyut=12.5, kalin=False, sinif='g-y', anchor='middle'):
    """Ortalanmış çok satırlı yazı; ilk satırın taban çizgisi ilk_y."""
    agirlik = ' font-weight="700"' if kalin else ''
    return ''.join(f'<text x="{cx:g}" y="{ilk_y + i * aralik:g}" text-anchor="{anchor}" font-size="{boyut}"{agirlik} class="{sinif}">{t}</text>'
                   for i, t in enumerate(satirlar))


def gokteki_ahenk():
    """Neden-sonuç: Dünya’nın hareketleri → gece-gündüz, mevsimler; Dünya’nın Güneş’e uzaklığı → hayat (kitap s. 22)."""
    ic = '<defs>' + ok_isareti('okD3gok', 'g-s') + '</defs>'
    ic += '<text x="86" y="16" text-anchor="middle" font-size="12" font-weight="700" class="g-s">Neden</text>'
    ic += '<text x="337" y="16" text-anchor="middle" font-size="12" font-weight="700" class="g-s">Sonuç</text>'
    # 1. satır: mavi
    ic += _kutu(8, 26, 156, 66, 'mavi')
    ic += _satirlar(86, 54, 18, ['Dünya’nın', 'hareketleri'], 13, True, 'g-mf')
    ic += '<line x1="170" y1="59" x2="204" y2="59" class="g-c" stroke-width="2" marker-end="url(#okD3gok)"/>'
    ic += _kutu(210, 26, 254, 30, 'mavi', rx=15)
    ic += '<text x="337" y="46" text-anchor="middle" font-size="12.5" class="g-y">Gece ile gündüz art arda gelir</text>'
    ic += _kutu(210, 62, 254, 30, 'mavi', rx=15)
    ic += '<text x="337" y="82" text-anchor="middle" font-size="12.5" class="g-y">Mevsimler oluşur</text>'
    # 2. satır: turuncu
    ic += _kutu(8, 110, 156, 66, 'turuncu')
    ic += _satirlar(86, 138, 18, ['Dünya’nın Güneş’e', 'uzaklığı'], 12.5, True, 'g-tf')
    ic += '<line x1="170" y1="143" x2="204" y2="143" class="g-c" stroke-width="2" marker-end="url(#okD3gok)"/>'
    ic += _kutu(210, 116, 254, 54, 'turuncu', rx=15)
    ic += _satirlar(337, 139, 18, ['Yeryüzündeki varlıklar', 'hayat bulur'], 12.5)
    return svg(472, 190, ic, 'Neden-sonuç: Dünya’nın hareketleri sayesinde gece ile gündüz art arda gelir ve mevsimler oluşur. '
               'Dünya’nın Güneş’e uzaklığı sayesinde yeryüzündeki varlıklar hayat bulur.')


def mevsim_zinciri():
    """Kış, ilkbahar ve yaz: kar → yer altı suları → baharın su ihtiyacı; yaz sıcaklığı → olgunlaşma (kitap s. 23)."""
    ic = '<defs>' + ok_isareti('okD3mev', 'g-mf') + '</defs>'
    kol = [(10, 'mavi', 'Kış'), (180, 'yesil', 'Bahar'), (350, 'turuncu', 'Yaz')]
    for x, renk, ad in kol:
        ic += f'<rect x="{x}" y="10" width="140" height="30" rx="15" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + 70}" y="30" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{ad}</text>'
    # kış
    ic += _kutu(10, 50, 140, 34, 'mavi', 10) + _satirlar(80, 72, 17, ['Kar yağar'])
    ic += _kutu(10, 92, 140, 34, 'mavi', 10) + _satirlar(80, 114, 17, ['Toprak korunur'])
    ic += _kutu(10, 134, 140, 48, 'mavi', 10) + _satirlar(80, 154, 17, ['Yer altı suları', 'artar'])
    # ilkbahar
    ic += _kutu(180, 50, 140, 132, 'yesil', 10) + _satirlar(250, 103, 18, ['Ekin, bitki ve', 'ağaçlar suyunu', 'bulur'])
    # yaz
    ic += _kutu(350, 50, 140, 34, 'turuncu', 10) + _satirlar(420, 72, 17, ['Sıcaklık artar'])
    ic += _kutu(350, 92, 140, 90, 'turuncu', 10) + _satirlar(420, 124, 18, ['Ekin ve', 'diğer bitkiler', 'olgun hâle gelir'])
    # neden-sonuç oku: yer altı suları → baharın su ihtiyacı
    ic += '<line x1="154" y1="158" x2="174" y2="158" class="g-ms" stroke-width="2.5" marker-end="url(#okD3mev)"/>'
    ic += '<text x="250" y="206" text-anchor="middle" font-size="12.5" class="g-y">Kışın yağan kar, baharın su ihtiyacını karşılar.</text>'
    return svg(500, 218, ic, 'Mevsimler: Kışın kar yağar, toprak korunur, yer altı suları artar. Baharda ekin, bitki ve ağaçlar suyunu bulur. '
               'Yazın sıcaklık artar, ekin ve diğer bitkiler olgun hâle gelir. '
               'Kışın yağan kar, baharın su ihtiyacını karşılar.')


def tevhit_dort_yon():
    """Tevhidin dört yönü (kitap s. 27, Bilgi Görseli 1.2): merkezde tevhit, çevrede dört ifade."""
    ic = ''
    kutular = [(8, 8, ['Bir ve ibadete layık', 'tek ilah']), (272, 8, ['Eşi, benzeri ve', 'ortağı yok']),
               (8, 124, ['Her şeyi yoktan yaratan,', 'bütün varlıkların sahibi']), (272, 124, ['Hiçbir varlığa', 'benzemez'])]
    for x, y, satir in kutular:
        ic += _kutu(x, y, 200, 56, 'mavi')
        ic += _satirlar(x + 100, y + 24, 18, satir)
    for x1, y1, x2, y2 in [(206, 78, 190, 68), (274, 78, 290, 68), (206, 110, 190, 120), (274, 110, 290, 120)]:
        ic += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="g-c" stroke-width="2" stroke-linecap="round"/>'
    ic += '<rect x="200" y="78" width="80" height="32" rx="16" class="g-tf"/>'
    ic += '<text x="240" y="99" text-anchor="middle" font-size="15" font-weight="800" class="g-b">Tevhit</text>'
    return svg(480, 188, ic, 'Tevhit: Allah bir ve ibadete layık tek ilahtır; eşi, benzeri ve ortağı yoktur; her şeyi yoktan yaratandır ve '
               'bütün varlıkların sahibidir; hiçbir varlığa benzemez.')


def uygula(o):
    g = {'Gökteki ahenk: gece, gündüz ve mevsimler': gokteki_ahenk(),
         'Her varlığa kendi ortamına uygun özellikler': mevsim_zinciri(),
         'Düzen ve tevhit: Allah’ın birliği': tevhit_dort_yon()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
