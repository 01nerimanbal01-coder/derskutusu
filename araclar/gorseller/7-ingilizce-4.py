"""7. sınıf İngilizce, 4. hafta: Sports teması; sıklık zarflarının sırası, zarfın cümledeki yeri, sıklık ifadeleri.

Görseller yalnız MEB 7. sınıf İngilizce ders kitabındaki bilgilerle çizilir (Sports ünitesi, PDF s23-s26, s28, s32; zarfın be fiilindeki yeri
için plandaki konu satırı).
Renk anlamı: sıklık ölçeğinde mavi dolu uzunluk = sıklığın sırası (ölçüsüz); cümle yapısında özne mavi, sıklık zarfı turuncu, fiil/be yeşil,
cümlenin devamı mor; hafta şeritlerinde three times a week turuncu, twice a week mavi.
"""
from ozet_gorsel import svg

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def siklik_olcegi():
    """always → never: yedi basamak (kitap s26); çubuk uzunluğu yalnız sırayı gösterir."""
    ic = ''
    zarf = [('always', 'her zaman', 300), ('usually', 'genellikle', 250), ('often', 'sık sık', 200), ('sometimes', 'bazen', 150),
            ('rarely / seldom', 'nadiren', 100), ('hardly ever', 'neredeyse hiç', 50), ('never', 'hiçbir zaman', 0)]
    for i, (en, tr, uz) in enumerate(zarf):
        y = 8 + i * 38
        ic += f'<text x="14" y="{y + 15}" font-size="14" font-weight="800" class="g-y">{en}</text>'
        ic += f'<text x="14" y="{y + 30}" font-size="11.5" class="g-s">{tr}</text>'
        ic += f'<rect x="160" y="{y + 7}" width="290" height="22" rx="8" class="g-ma"/>'
        if uz:
            ic += f'<rect x="160" y="{y + 7}" width="{uz * 290 / 300:g}" height="22" rx="8" class="g-mf"/>'
        ic += f'<rect x="160" y="{y + 7}" width="290" height="22" rx="8" class="g-ms" stroke-width="1.5"/>'
    ic += '<text x="235" y="296" text-anchor="middle" font-size="12" class="g-s">Uzunluk yalnız sıklığın sırasını gösterir.</text>'
    return svg(470, 306, ic, 'Sıklık zarflarının sırası en sıktan en seyreğe: always her zaman, usually genellikle, often sık sık, sometimes bazen, '
               'rarely veya seldom nadiren, hardly ever neredeyse hiç, never hiçbir zaman. Mavi uzunluk yalnız sıralamayı gösterir.')


def _cip(x, y, metin, renk, yuk=30, boy=13):
    w = round(len(metin) * boy * 0.6 + 22)
    a, s, f = RENK[renk]
    ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{a}"/>'
          f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{s}" stroke-width="2"/>'
          f'<text x="{x + w / 2:g}" y="{y + yuk / 2 + 4.5:g}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{f}">{metin}</text>')
    return w, ic


def _sira(y, parcalar):
    gen = [round(len(m) * 13 * 0.6 + 22) for m, _ in parcalar]
    bosluk = 8
    x = (470 - (sum(gen) + bosluk * (len(gen) - 1))) / 2
    ic = ''
    for (m, r), w in zip(parcalar, gen):
        _, c = _cip(round(x, 1), y, m, r)
        ic += c
        x += w + bosluk
    return ic


def zarfin_yeri():
    """Zarf ana fiilden önce, be fiilinden sonra (kitap s26 örnekleri; be fiili için plandaki konu satırı)."""
    ic = '<text x="12" y="16" font-size="12" font-weight="700" class="g-s">Ana fiil varsa</text>'
    ic += _sira(24, [('Mert', 'mavi'), ('always', 'turuncu'), ('goes', 'yesil'), ('jogging after school', 'mor')])
    ic += '<text x="235" y="72" text-anchor="middle" font-size="12" class="g-y">Zarf, ana fiilden önce gelir.</text>'
    ic += '<text x="12" y="104" font-size="12" font-weight="700" class="g-s">Be fiili varsa</text>'
    ic += _sira(112, [('Our coach', 'mavi'), ('is', 'yesil'), ('always', 'turuncu'), ('on time', 'mor')])
    ic += '<text x="235" y="160" text-anchor="middle" font-size="12" class="g-y">Zarf, be fiilinden sonra gelir.</text>'
    for x, ad, renk in ((20, 'Özne', 'mavi'), (110, 'Sıklık zarfı', 'turuncu'), (240, 'Fiil / be', 'yesil'), (340, 'Cümlenin devamı', 'mor')):
        ic += f'<circle cx="{x}" cy="190" r="6" class="{RENK[renk][2]}"/><text x="{x + 12}" y="194" font-size="12" class="g-y">{ad}</text>'
    return svg(470, 204, ic, 'Zarfın yeri: Mert always goes jogging after school; ana fiil goes olduğu için always ondan önce gelir. '
               'Our coach is always on time; be fiili is olduğu için always ondan sonra gelir. Mavi özne, turuncu sıklık zarfı, '
               'yeşil fiil veya be, mor cümlenin devamı.')


def hafta_seritleri():
    """Üç gün = three times a week (Mon, Thu, Sat); iki gün = twice a week (Tue, Fri) (kitap s32, etkinlik 4)."""
    gunler = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ic = ''
    seritler = [(8, 'three times a week', 'turuncu', {0, 3, 5}, 'Monday, Thursday, Saturday'),
                (96, 'twice a week', 'mavi', {1, 4}, 'Tuesday, Friday')]
    for y, ad, renk, dolu, alt in seritler:
        a, s, f = RENK[renk]
        ic += f'<text x="24" y="{y + 14}" font-size="14" font-weight="800" class="{f}">{ad}</text>'
        for i, g in enumerate(gunler):
            x = 24 + i * 60
            if i in dolu:
                ic += f'<rect x="{x}" y="{y + 24}" width="56" height="36" rx="8" class="{f}"/>'
                ic += f'<text x="{x + 28}" y="{y + 47}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{g}</text>'
            else:
                ic += f'<rect x="{x}" y="{y + 24}" width="56" height="36" rx="8" class="g-z"/>'
                ic += f'<rect x="{x}" y="{y + 24}" width="56" height="36" rx="8" class="g-c" stroke-width="1.5"/>'
                ic += f'<text x="{x + 28}" y="{y + 47}" text-anchor="middle" font-size="13" class="g-s">{g}</text>'
        ic += f'<text x="24" y="{y + 78}" font-size="12" class="g-y">{alt}</text>'
    return svg(470, 186, ic, 'İki hafta şeridi: Monday, Thursday ve Saturday günleri renkli, antrenman haftada üç gün: three times a week. '
               'Tuesday ve Friday günleri renkli, antrenman haftada iki gün: twice a week.')


def uygula(o):
    g = {'Sıklık zarflarının sırası': siklik_olcegi(),
         'Sıklık zarfının cümledeki yeri': zarfin_yeri(),
         'Sıklık ifadeleri: kaç kez, ne kadar sürede': hafta_seritleri()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
