"""5. sınıf İngilizce, 7. hafta: School Life teması; okul kulüpleri, Do you like …ing?, mustn't ve can't, who ve what, ülkeler, Republic Day.

Görseller yalnız özet metnindeki (araclar/ozetler/5-ingilizce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı: soru-cevap şemasında mavi = soru başındaki Do/Does, gri çerçeve = özne, yeşil = olumlu (like, love, Yes), turuncu = olumsuz
(don't like, hate, No), mor = -ing alan fiil; who/what şemasında mavi = who (kişi), turuncu = what (şey, eylem), yeşil = yardımcı fiil
(is/are, do/does), gri = cümlenin devamı; kulüp fuarı konuşma sırasında gri = kendini tanıtma (to be), yeşil = sevdiğin şey,
turuncu = sevmediğin şey, mor = kural (mustn't/can't), mavi = arkadaşına soru; okuma görselinde mor = okuma adımları,
mavi = düşen ton (olumlu cümle), turuncu = yükselen ton (evet/hayır sorusu). Çizimler ölçeksizdir.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu / yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
    'gri': ('g-z', 'g-c', 'g-y'),
}


def _gen(metin, boy=13):
    return round(len(metin) * boy * 0.6 + 22)


def _cip(x, y, metin, renk, yuk=30, boy=13, w=None):
    """Açık dolgu + aynı renk çerçeve + koyu yazı; gri çipte yüzey dolgusu, gri çerçeve ve normal yazı."""
    w = w or _gen(metin, boy)
    a, s, f = RENK[renk]
    ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{a}"/>'
          f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{s}" stroke-width="2"/>'
          f'<text x="{x + w / 2:g}" y="{y + yuk / 2 + 4.5:g}" text-anchor="middle" font-size="{boy}" font-weight="700" class="{f}">{metin}</text>')
    return w, ic


def _sira(y, parcalar, orta=235, bosluk=8):
    """Çipleri yan yana dizer, orta noktaya göre ortalar."""
    gen = [_gen(m) for m, _ in parcalar]
    x = orta - (sum(gen) + bosluk * (len(gen) - 1)) / 2
    ic = ''
    for (m, r), w in zip(parcalar, gen):
        ic += _cip(round(x, 1), y, m, r)[1]
        x += w + bosluk
    return ic


def _nokta(x, y, renk, r=6):
    if renk == 'gri':
        return f'<circle cx="{x}" cy="{y}" r="{r}" class="g-z"/><circle cx="{x}" cy="{y}" r="{r}" class="g-c" stroke-width="2"/>'
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{RENK[renk][2]}"/>'


def soru_cevap():
    """Do you like …ing? → Yes, I do. / No, I don't.; Does Mert like acting? → Yes, he does. / No, he doesn't.; love–like–don't like–hate ölçeği."""
    ic = '<defs>' + ok_isareti('ok5ing7a', 'g-s') + '</defs>'
    bloklar = [(8, [('Do', 'mavi'), ('you', 'gri'), ('like', 'yesil'), ('playing chess?', 'mor')],
                [('Yes, I do.', 'yesil'), ("No, I don't.", 'turuncu')]),
               (116, [('Does', 'mavi'), ('Mert', 'gri'), ('like', 'yesil'), ('acting?', 'mor')],
                [('Yes, he does.', 'yesil'), ("No, he doesn't.", 'turuncu')])]
    for y, soru, cevaplar in bloklar:
        ic += _sira(y, soru)
        for cx, (m, r) in zip((140, 330), cevaplar):
            w = _gen(m)
            ic += _cip(round(cx - w / 2, 1), y + 58, m, r)[1]
        ic += f'<line x1="214" y1="{y + 35}" x2="160" y2="{y + 54}" class="g-c" stroke-width="2" marker-end="url(#ok5ing7a)"/>'
        ic += f'<line x1="256" y1="{y + 35}" x2="310" y2="{y + 54}" class="g-c" stroke-width="2" marker-end="url(#ok5ing7a)"/>'
    x = 22
    for ad, renk in (('Do / Does', 'mavi'), ('özne', 'gri'), ('olumlu', 'yesil'), ('olumsuz', 'turuncu'), ('fiil + -ing', 'mor')):
        ic += _nokta(x, 228, renk) + f'<text x="{x + 11}" y="232" font-size="12" class="g-y">{ad}</text>'
        x += 11 + round(len(ad) * 7.2) + 18
    ic += '<text x="24" y="258" font-size="12" font-weight="700" class="g-s">çok sever</text>'
    ic += '<text x="446" y="258" text-anchor="end" font-size="12" font-weight="700" class="g-s">hiç sevmez</text>'
    ic += '<line x1="106" y1="254" x2="352" y2="254" class="g-c" stroke-width="2" marker-end="url(#ok5ing7a)"/>'
    olcek = (('love', 'yesil', 'dancing'), ('like', 'yesil', 'drawing'), ("don't like", 'turuncu', 'getting up early'), ('hate', 'turuncu', 'losing'))
    for cx, (m, r, ek) in zip((62, 162, 282, 402), olcek):
        w = _gen(m)
        ic += _cip(round(cx - w / 2, 1), 268, m, r)[1]
        ic += f'<text x="{cx}" y="322" text-anchor="middle" font-size="12" font-weight="700" class="g-of">{ek}</text>'
    return svg(470, 334, ic, 'Soru-cevap şeması: Do you like playing chess? sorusuna Yes, I do. ya da No, I don\'t. diye cevap verilir; '
               'Does Mert like acting? sorusuna Yes, he does. ya da No, he doesn\'t. Soru Do ya da Does ile başlar, like sözcüğünden sonra '
               'gelen fiil -ing alır. Altta tercih ölçeği çok severden hiç sevmeze: love dancing, like drawing, don\'t like getting up early, '
               'hate losing.')


def kim_ne():
    """who → bir kişi, what → bir şey ya da eylem; soru yapısı who/what + is/are ya da who/what + do/does + özne + fiil."""
    ic = ''
    kartlar = [(8, 'mavi', 'who', 'bir kişi: kim?',
                [('Who is he?', '', 'He is my coach.'), ('Who is the coach', 'of the sports club?', 'Mr. Aydın is.')]),
               (242, 'turuncu', 'what', 'bir şey ya da eylem: ne?',
                [('What is this?', '', 'It is our club poster.'), ('What do you do', 'in the drama club?', 'We act in short plays.')])]
    for x, renk, bas, aciklama, ciftler in kartlar:
        a, s, f = RENK[renk]
        ic += f'<rect x="{x}" y="8" width="220" height="186" rx="12" class="{a}"/>'
        ic += f'<rect x="{x}" y="8" width="220" height="186" rx="12" class="{s}" stroke-width="2"/>'
        ic += f'<rect x="{x + 75}" y="18" width="70" height="30" rx="10" class="{f}"/>'
        ic += f'<text x="{x + 110}" y="39" text-anchor="middle" font-size="16" font-weight="800" class="g-b">{bas}</text>'
        ic += f'<text x="{x + 110}" y="68" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{aciklama}</text>'
        y = 94
        for s1, s2, cevap in ciftler:
            ic += f'<text x="{x + 14}" y="{y}" font-size="13" font-weight="700" class="g-y">{s1}</text>'
            if s2:
                y += 17
                ic += f'<text x="{x + 14}" y="{y}" font-size="13" font-weight="700" class="g-y">{s2}</text>'
            y += 18
            ic += f'<text x="{x + 14}" y="{y}" font-size="12" class="g-s">→ {cevap}</text>'
            y += 30
    for y, yardimci, devam, ornek in ((206, 'is / are', '…', 'Who is she? · What are the rules of your club?'),
                                      (268, 'do / does', 'özne + fiil', 'What does the environment club do on Fridays?')):
        ic += _cip(12, y, 'Who', 'mavi')[1]
        ic += f'<text x="64" y="{y + 19.5:g}" font-size="13" font-weight="700" class="g-s">/</text>'
        ic += _cip(74, y, 'What', 'turuncu')[1]
        ic += f'<text x="134" y="{y + 19.5:g}" font-size="13" font-weight="700" class="g-s">+</text>'
        w, c = _cip(148, y, yardimci, 'yesil')
        ic += c
        ic += f'<text x="{148 + w + 8}" y="{y + 19.5:g}" font-size="13" font-weight="700" class="g-s">+</text>'
        ic += _cip(148 + w + 22, y, devam, 'gri')[1]
        ic += f'<text x="12" y="{y + 48}" font-size="12" class="g-s">{ornek}</text>'
    ic += '<text x="12" y="338" font-size="12" font-weight="700" class="g-y">Who özne ise fiil -s alır: Who organises the fair?</text>'
    return svg(470, 350, ic, 'who ve what şeması: who bir kişiyi sorar: Who is he? He is my coach. Who is the coach of the sports club? '
               'Mr. Aydın is. what bir şeyi ya da eylemi sorar: What is this? It is our club poster. What do you do in the drama club? '
               'We act in short plays. Yapı: who ya da what artı is/are; who ya da what artı do/does artı özne ve fiil. '
               'Who özne ise fiil -s alır: Who organises the fair?')


def fuar_sirasi():
    """Kulüp fuarında konuşma sırası: tanıt → sevdiğin şey → sevmediğin şey → kural → arkadaşına soru (Deniz'in konuşmasından örnekler)."""
    ic = '<defs>' + ok_isareti('ok5ing7b', 'g-s') + '</defs>'
    adimlar = [('gri', "I'm … / I'm in the …", 'adın ve kulübün', "I'm Deniz. I'm a member of the drama club."),
               ('yesil', 'I like …ing', 'sevdiğin şey', 'I love acting.'),
               ('turuncu', "I don't like …ing", 'sevmediğin şey', "I don't like strict rules."),
               ('mor', "You mustn't … / You can't …", 'bir kural', "In our club, you mustn't be late for rehearsals."),
               ('mavi', 'Do you like …ing?', 'arkadaşına bir soru', 'Do you like acting? — Yes, I do!')]
    for i, (renk, kalip, etiket, ornek) in enumerate(adimlar):
        y = 8 + i * 64
        ic += f'<rect x="48" y="{y}" width="414" height="54" rx="12" class="g-z"/>'
        ic += f'<rect x="48" y="{y}" width="414" height="54" rx="12" class="g-c" stroke-width="1.5"/>'
        if renk == 'gri':
            ic += (f'<circle cx="26" cy="{y + 27}" r="14" class="g-z"/><circle cx="26" cy="{y + 27}" r="14" class="g-c" stroke-width="2"/>'
                   f'<text x="26" y="{y + 32}" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{i + 1}</text>')
        else:
            ic += (f'<circle cx="26" cy="{y + 27}" r="14" class="{RENK[renk][2]}"/>'
                   f'<text x="26" y="{y + 32}" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{i + 1}</text>')
        ic += _cip(58, y + 7, kalip, renk, yuk=28)[1]
        ic += f'<text x="452" y="{y + 25}" text-anchor="end" font-size="12" class="g-s">{etiket}</text>'
        ic += f'<text x="60" y="{y + 48}" font-size="12" class="g-y">{ornek}</text>'
        if i < 4:
            ic += f'<line x1="26" y1="{y + 45}" x2="26" y2="{y + 73}" class="g-c" stroke-width="2" marker-end="url(#ok5ing7b)"/>'
    ic += '<text x="60" y="338" font-size="12" class="g-s">Neden ekle: because I want to be free on the stage.</text>'
    return svg(470, 348, ic, 'Kulüp fuarında konuşma sırası beş adım: bir, adın ve kulübün: I\'m Deniz. I\'m a member of the drama club. '
               'İki, sevdiğin şey: I love acting. Üç, sevmediğin şey: I don\'t like strict rules. Dört, bir kural: In our club, you mustn\'t '
               'be late for rehearsals. Beş, arkadaşına bir soru: Do you like acting? Yes, I do! Neden eklemek için because kullanılır.')


def okuma_ve_ton():
    """Okuma sırası (tara → soruyu oku → cevap cümlesini oku) ve cümle sonunda ses: olumlu cümlede düşer, evet/hayır sorusunda yükselir."""
    ic = '<defs>' + ok_isareti('ok5ing7c', 'g-s') + ok_isareti('ok5ing7d', 'g-mf') + ok_isareti('ok5ing7e', 'g-tf') + '</defs>'
    adimlar = ['Hızlıca tara', 'Soruyu oku', 'Cevap cümlesini oku']
    gen = [_gen(a, 12) for a in adimlar]
    x = (470 - (sum(gen) + 60)) / 2
    for i, (a, w) in enumerate(zip(adimlar, gen)):
        ic += _cip(round(x, 1), 8, a, 'mor', boy=12)[1]
        if i < 2:
            ic += f'<line x1="{x + w + 6:g}" y1="23" x2="{x + w + 24:g}" y2="23" class="g-c" stroke-width="2" marker-end="url(#ok5ing7c)"/>'
        x += w + 30
    ic += '<text x="26" y="56" font-size="11.5" class="g-s">skimming: kulüp adlarını bul</text>'
    ic += '<text x="444" y="56" text-anchor="end" font-size="11.5" class="g-s">cevabı veren cümle</text>'
    ic += '<text x="24" y="77" font-size="12" font-weight="700" class="g-s">Cümle sonunda ses</text>'
    cumleler = [(126, 'We are proud and happy today.', 'dusen', 160, 214, 'Olumlu cümle ↘', 'ses sonda alçalır (falling)'),
                (186, 'The art club decorates the hall.', 'dusen', 180, 236, 'Olumlu cümle ↘', 'ses sonda alçalır (falling)'),
                (246, 'Do you like dancing?', 'yukselen', 100, 154, 'Evet/hayır sorusu ↗', 'ses sonda yükselir (rising)')]
    for T, cumle, ton, x1, x2, bas, aciklama in cumleler:
        if ton == 'dusen':
            ic += f'<path d="M24 {T - 38}L{x1} {T - 38}L{x2} {T - 22}" class="g-ms" stroke-width="2.5" stroke-linejoin="round" marker-end="url(#ok5ing7d)"/>'
            renk = 'g-mf'
        else:
            ic += f'<path d="M24 {T - 24}L{x1} {T - 24}L{x2} {T - 40}" class="g-ts" stroke-width="2.5" stroke-linejoin="round" marker-end="url(#ok5ing7e)"/>'
            renk = 'g-tf'
        ic += f'<text x="24" y="{T}" font-size="14" font-weight="700" class="g-y">{cumle}</text>'
        ic += f'<text x="272" y="{T - 8}" font-size="12.5" font-weight="700" class="{renk}">{bas}</text>'
        ic += f'<text x="272" y="{T + 10}" font-size="12" class="g-s">{aciklama}</text>'
    return svg(470, 266, ic, 'Okuma sırası: önce metni hızlıca tara (skimming) ve kulüp adlarını bul, sonra soruyu oku, sonra cevabı veren '
               'cümleyi dikkatle oku. Cümle sonunda ses: olumlu cümlede ses sonda alçalır: We are proud and happy today. The art club '
               'decorates the hall. Evet/hayır sorusunda ses sonda yükselir: Do you like dancing?')


def uygula(o):
    g = {'Likes and dislikes: Do you like …ing?': soru_cevap(),
         'Who and what: asking about people and things': kim_ne(),
         'At the School Clubs Fair': fuar_sirasi(),
         'Republic Day at school: reading': okuma_ve_ton()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
