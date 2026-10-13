"""6. sınıf İngilizce, 7. hafta (Theme 1: School Life): Daily Routines, School Rules and Republic Day; Do / Does soruları,
sıklık zarfları ve How often, emir cümlesiyle okul kuralları, günlük rutin posteri.

Görseller yalnız özet metnindeki (araclar/ozetler/6-ingilizce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: soru şemasında turuncu = yardımcı fiil (Do / Does), mavi = özne, yeşil = yalın fiil, mor = soru sözcüğü;
sıklık ölçeğinde mavi = sıklık zarfı (dairenin dolu parçası yalnız sırayı gösterir, ölçüsüz), turuncu = sayılı sıklık ifadesi;
kural kartlarında yeşil = olumlu kural (Do this), turuncu = olumsuz kural (Don't), mavi = izin isteme kalıbı;
rutin şeridinde mavi = saati söylenen durak (saat yüzü, akrep ve yelkovan doğru açıda), mor = saati söylenmeyen durak,
gri ok = sıra. Şerit ölçeksizdir (duraklar arası uzaklık süre göstermez).
"""
import math

from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu / yazı)
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _cip(x, y, metin, renk, yuk=32, boy=13):
    """Açık dolgulu, çerçeveli sözcük kutusu; (genişlik, svg) döner."""
    w = round(len(metin) * boy * 0.6 + 22)
    a, s, f = RENK[renk]
    ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{a}"/>'
          f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{s}" stroke-width="2"/>'
          f'<text x="{x + w / 2:g}" y="{y + yuk / 2 + 4.5:g}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{f}">{metin}</text>')
    return w, ic


def _sira(x, y, parcalar, bosluk=8):
    """Kutuları soldan sağa dizer; (son x, svg) döner."""
    ic = ''
    for metin, renk in parcalar:
        w, c = _cip(x, y, metin, renk)
        ic += c
        x += w + bosluk
    return x - bosluk, ic


def _kutu(x, y, w, h, renk, rx=12, kalinlik=1.8):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="{kalinlik}"/>')


def do_does_semasi():
    """Evet/hayır sorusu Do / Does + özne + yalın fiil, kısa cevaplar; ayrıntı sorusu soru sözcüğü + do/does + özne + yalın fiil."""
    ic = '<text x="12" y="17" font-size="12.5" font-weight="700" class="g-s">Evet / hayır sorusu</text>'
    satirlar = [(25, [('Do', 'turuncu'), ('I, you, we, they', 'mavi'), ('yalın fiil', 'yesil')], ('Yes, I do.', "No, I don't.")),
                (88, [('Does', 'turuncu'), ('he, she, it', 'mavi'), ('yalın fiil', 'yesil')], ('Yes, she does.', "No, he doesn't."))]
    for y, parcalar, (evet, hayir) in satirlar:
        son, c = _sira(12, y, parcalar)
        ic += c
        ic += f'<text x="{son + 5}" y="{y + 22}" font-size="16" font-weight="800" class="g-y">?</text>'
        ic += f'<text x="332" y="{y + 13}" font-size="12" font-weight="700" class="g-y">{evet}</text>'
        ic += f'<text x="332" y="{y + 28}" font-size="12" font-weight="700" class="g-y">{hayir}</text>'
    ic += '<text x="12" y="78" font-size="13" font-weight="700" class="g-y">Do you walk to school?</text>'
    ic += '<text x="196" y="78" font-size="12" class="g-s">— No, I don\'t. I take the school bus.</text>'
    ic += '<text x="12" y="141" font-size="13" font-weight="700" class="g-y">Does she go to school by bus?</text>'
    ic += '<text x="252" y="141" font-size="12" font-weight="700" class="g-tf">go yalın kalır, goes değil</text>'
    ic += '<text x="12" y="170" font-size="12.5" font-weight="700" class="g-s">Ayrıntı sorusu</text>'
    son, c = _sira(12, 178, [('Soru sözcüğü', 'mor'), ('do / does', 'turuncu'), ('özne', 'mavi'), ('yalın fiil', 'yesil')])
    ic += c
    ic += f'<text x="{son + 5}" y="200" font-size="16" font-weight="800" class="g-y">?</text>'
    ic += '<text x="12" y="231" font-size="13" font-weight="700" class="g-y">What time do you get up?</text>'
    ic += '<text x="212" y="231" font-size="12" class="g-s">— I get up at half past six.</text>'
    ic += '<text x="12" y="253" font-size="13" font-weight="700" class="g-y">How does Mert go to school?</text>'
    ic += '<text x="236" y="253" font-size="12" class="g-s">— By bus.</text>'
    for x, ad, renk in ((20, 'Yardımcı fiil', 'turuncu'), (142, 'Özne', 'mavi'), (212, 'Yalın fiil', 'yesil'), (312, 'Soru sözcüğü', 'mor')):
        ic += f'<circle cx="{x}" cy="280" r="6" class="{RENK[renk][2]}"/><text x="{x + 11}" y="284" font-size="12" class="g-y">{ad}</text>'
    return svg(470, 294, ic, 'Soru kalıbı şeması: evet/hayır sorusu Do artı I, you, we, they artı yalın fiil; Does artı he, she, it artı yalın fiil. '
               'Kısa cevaplar Yes, I do. No, I don\'t. Yes, she does. No, he doesn\'t. Örnek: Do you walk to school? No, I don\'t. '
               'I take the school bus. Does she go to school by bus? Burada go yalın kalır, goes değil. Ayrıntı sorusu: soru sözcüğü artı '
               'do ya da does artı özne artı yalın fiil: What time do you get up? I get up at half past six. How does Mert go to school? By bus. '
               'Turuncu yardımcı fiil, mavi özne, yeşil yalın fiil, mor soru sözcüğü.')


def _dilim(cx, cy, r, oran):
    """Dairenin saat 12'den başlayıp saat yönünde dolan parçası (oran 0–1)."""
    if oran <= 0:
        return ''
    if oran >= 1:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-mf"/>'
    aci = 2 * math.pi * oran
    x, y = cx + r * math.sin(aci), cy - r * math.cos(aci)
    buyuk = 1 if oran > 0.5 else 0
    return f'<path d="M{cx} {cy}L{cx} {cy - r}A{r} {r} 0 {buyuk} 1 {x:.1f} {y:.1f}Z" class="g-mf"/>'


def siklik_olcegi():
    """always → never: beş daire; dolu parça yalnız sırayı gösterir. Altında How often sorusu ve sayılı sıklık ifadeleri."""
    ic = '<defs>' + ok_isareti('ok6ing7b', 'g-c') + '</defs>'
    ic += '<text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" class="g-y">Sıklık zarfları: en sıktan en seyreğe</text>'
    zarf = [('always', 'her zaman', 1), ('usually', 'genellikle', 0.75), ('often', 'sık sık', 0.5), ('sometimes', 'bazen', 0.25),
            ('never', 'hiçbir zaman', 0)]
    cy, r = 72, 24
    for i, (en, tr, oran) in enumerate(zarf):
        cx = 55 + i * 90
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-ma"/>'
        ic += _dilim(cx, cy, r, oran)
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-ms" stroke-width="2"/>'
        ic += f'<text x="{cx}" y="118" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{en}</text>'
        ic += f'<text x="{cx}" y="134" text-anchor="middle" font-size="11.5" class="g-s">{tr}</text>'
    ic += '<text x="12" y="156" font-size="12" font-weight="700" class="g-s">en sık</text>'
    ic += '<line x1="62" y1="152" x2="380" y2="152" class="g-c" stroke-width="2" marker-end="url(#ok6ing7b)"/>'
    ic += '<text x="392" y="156" font-size="12" font-weight="700" class="g-s">en seyrek</text>'
    ic += '<text x="12" y="186" font-size="13" font-weight="700" class="g-y">How often do you have P.E.?</text>'
    ic += '<text x="236" y="186" font-size="13" font-weight="700" class="g-tf">— Twice a week.</text>'
    x = 12
    for ifade in ('every day', 'once a week', 'twice a week', 'three times a week'):
        w = round(len(ifade) * 12 * 0.6 + 16)
        ic += _kutu(x, 198, w, 30, 'turuncu', rx=9, kalinlik=2)
        ic += f'<text x="{x + w / 2:g}" y="217.5" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">{ifade}</text>'
        x += w + 8
    ic += '<text x="12" y="250" font-size="12" class="g-s">Cevap: zarf (mavi) ya da sayılı ifade (turuncu).</text>'
    ic += '<text x="12" y="267" font-size="12" class="g-s">Dolu parça yalnız sırayı gösterir (ölçüsüz).</text>'
    return svg(470, 278, ic, 'Sıklık zarfları en sıktan en seyreğe beş daireyle: always her zaman (dairenin tamamı dolu), usually genellikle, '
               'often sık sık, sometimes bazen, never hiçbir zaman (boş daire); dolu parça yalnız sırayı gösterir, ölçüsüz. '
               'How often do you have P.E.? sorusunun cevabı Twice a week. Sayılı sıklık ifadeleri turuncu kutularda: every day, '
               'once a week, twice a week, three times a week. Cevap bir zarf ya da sayılı bir ifade olur.')


def kural_kartlari():
    """Do this / Don't do that kural kartları (emir cümlesi fiille başlar) ve izin isteme kalıbı."""
    ic = ''
    kartlar = [(10, 'Do this', 'yesil', [('Enter', 'the classroom quietly.'), ('Greet', 'your teachers.'), ('Be', 'on time.'),
                                         ('Keep', 'the classroom clean.')]),
               (248, "Don't do that", 'turuncu', [("Don't", 'run in the corridors.'), ("Don't", 'eat in the classroom.'),
                                                 ("Don't", 'be late.'), ("Don't", 'shout.')])]
    for x, bas, renk, kurallar in kartlar:
        a, s, f = RENK[renk]
        ic += _kutu(x, 10, 222, 150, renk)
        ic += f'<rect x="{x + 10}" y="18" width="202" height="28" rx="9" class="{f}"/>'
        ic += f'<text x="{x + 111}" y="37" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{bas}</text>'
        for i, (fiil, devam) in enumerate(kurallar):
            ic += (f'<text x="{x + 12}" y="{72 + i * 24}" font-size="12.5" class="g-y">'
                   f'<tspan font-weight="800" class="{f}">{fiil}</tspan> {devam}</text>')
    ic += '<text x="240" y="181" text-anchor="middle" font-size="12" class="g-s">Fiille başlar, özne yok; olumsuz: Don\'t + fiil.</text>'
    ic += _kutu(10, 192, 460, 76, 'mavi')
    ic += '<text x="22" y="212" font-size="12.5" font-weight="800" class="g-mf">İzin isterken</text>'
    ic += '<text x="22" y="233" font-size="12.5" font-weight="700" class="g-y">Can I go to the toilet, please?</text>'
    ic += '<text x="268" y="233" font-size="12.5" class="g-s">— Yes, you can.</text>'
    ic += '<text x="22" y="254" font-size="12.5" font-weight="700" class="g-y">May I come in?</text>'
    ic += '<text x="268" y="254" font-size="12.5" class="g-s">— Not now, please wait.</text>'
    return svg(480, 280, ic, 'Okul kuralları kartları. Yeşil Do this kartı: Enter the classroom quietly. Greet your teachers. Be on time. '
               'Keep the classroom clean. Turuncu Don\'t do that kartı: Don\'t run in the corridors. Don\'t eat in the classroom. '
               'Don\'t be late. Don\'t shout. Emir cümlesi fiille başlar, özne yazılmaz; olumsuzu Don\'t artı fiil. '
               'Mavi kutu izin isteme: Can I go to the toilet, please? Yes, you can. May I come in? Not now, please wait.')


def _saat(cx, cy, saat, dakika, r=18):
    """Saat yüzü: akrep ve yelkovan verilen saate göre doğru açıda."""
    ic = f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-z"/><circle cx="{cx}" cy="{cy}" r="{r}" class="g-ms" stroke-width="2"/>'
    for a in (0, 90, 180, 270):
        rad = math.radians(a)
        ic += (f'<line x1="{cx + (r - 4) * math.sin(rad):.1f}" y1="{cy - (r - 4) * math.cos(rad):.1f}" '
               f'x2="{cx + (r - 1.5) * math.sin(rad):.1f}" y2="{cy - (r - 1.5) * math.cos(rad):.1f}" class="g-c" stroke-width="1.5"/>')
    akrep = math.radians((saat % 12 + dakika / 60) * 30)
    yelkovan = math.radians(dakika * 6)
    ic += (f'<line x1="{cx}" y1="{cy}" x2="{cx + r * 0.5 * math.sin(akrep):.1f}" y2="{cy - r * 0.5 * math.cos(akrep):.1f}" '
           f'class="g-ms" stroke-width="2.5" stroke-linecap="round"/>')
    ic += (f'<line x1="{cx}" y1="{cy}" x2="{cx + r * 0.75 * math.sin(yelkovan):.1f}" y2="{cy - r * 0.75 * math.cos(yelkovan):.1f}" '
           f'class="g-ms" stroke-width="2" stroke-linecap="round"/>')
    ic += f'<circle cx="{cx}" cy="{cy}" r="2" class="g-mf"/>'
    return ic


def rutin_seridi():
    """Selin'in model metnindeki okul günü: saati söylenen dört durak saat yüzüyle, okul sonrası ve yatmadan önce mor düğümle."""
    ic = '<defs>' + ok_isareti('ok6ing7d', 'g-c') + '</defs>'
    ic += '<text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" class="g-y">My School Day (Selin): rutinin sırası</text>'
    duraklar = [('7:00', "seven o'clock", ['get up,', 'have breakfast'], (7, 0)),
                ('8:00', 'at eight', ['go to school', 'by bus'], (8, 0)),
                ('9:00', 'at nine', ['first lesson', 'starts'], (9, 0)),
                ('12:30', 'half past twelve', ['lunch in', 'the canteen'], (12, 30)),
                ('after school', '', ['do homework,', 'play basketball'], None),
                ('before bed', '', ['pack my bag'], None)]
    cy, r = 168, 21
    xler = [55 + i * 72 for i in range(len(duraklar))]
    for i, (x, (bas, ifade, isler, saat)) in enumerate(zip(xler, duraklar)):
        if saat:
            ic += _saat(x, cy, *saat, r=r)
        else:
            ic += f'<circle cx="{x}" cy="{cy}" r="{r}" class="g-oa"/><circle cx="{x}" cy="{cy}" r="{r}" class="g-os" stroke-width="2"/>'
            ic += f'<circle cx="{x}" cy="{cy}" r="5" class="g-of"/>'
        if i + 1 < len(xler):
            ic += f'<line x1="{x + r + 5}" y1="{cy}" x2="{xler[i + 1] - r - 5}" y2="{cy}" class="g-c" stroke-width="2" marker-end="url(#ok6ing7d)"/>'
        satirlar = [(bas, 14, '800', 'g-mf' if saat else 'g-of')]
        if ifade:
            satirlar.append((ifade, 12, '400', 'g-s'))
        satirlar += [(s, 12, '400', 'g-y') for s in isler]
        n = len(satirlar)
        for j, (metin, boy, agirlik, sinif) in enumerate(satirlar):
            y = (124 - 16 * (n - 1 - j)) if i % 2 == 0 else (210 + 16 * j)
            ic += f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{boy}" font-weight="{agirlik}" class="{sinif}">{metin}</text>'
    ic += '<text x="235" y="284" text-anchor="middle" font-size="12" class="g-s">Sunarken: first → then → after that → finally</text>'
    return svg(470, 296, ic, 'Selin\'in okul günü sıra şeridi, ölçeksiz. Saat yüzleri: 7:00 seven o\'clock get up, have breakfast; '
               '8:00 at eight go to school by bus; 9:00 at nine first lesson starts; 12:30 half past twelve lunch in the canteen. '
               'Mor duraklar: after school do homework, play basketball; before bed pack my bag. Gri oklar sırayı gösterir. '
               'Sunarken first, then, after that, finally sözcükleri kullanılır.')


def uygula(o):
    g = {'Asking about routines: Do you …? What time …?': do_does_semasi(),
         'How often? Frequency adverbs and the class survey': siklik_olcegi(),
         "School rules: Do this, don't do that": kural_kartlari(),
         'Writing and speaking: my daily routine poster': rutin_seridi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
