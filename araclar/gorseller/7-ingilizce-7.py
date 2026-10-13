"""7. sınıf İngilizce, 7. hafta (Sports ünitesinin son haftası): How often / Why soru-cevap kalıpları, because ile neden açıklama,
bir sporcunun rutinini anlatan paragrafın planı.

Görseller yalnız özet metnindeki (araclar/ozetler/7-ingilizce-7.json) bilgilerle çizilir; ders kitabı sayfası kullanılmamıştır.
Renk anlamı (üç görselde aynı): turuncu = sıklık zarfı (always, usually …), yeşil = sıklık ifadesi (three times a week …),
mor = neden (because + özne + fiil), mavi = yapılan iş / sonuç (so ile başlayan bölüm); gri çerçeveli kutu = soru ya da nötr adım.
Tüm çizimler şematiktir, ölçek yoktur.
"""
from ozet_gorsel import svg, ok_isareti

RENK = {  # (açık dolgu, çerçeve, koyu dolgu / yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'yesil': ('g-ya', 'g-ys', 'g-yf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}
W = 470


def _gen(metin, boy=12):
    return round(len(metin) * boy * 0.6 + 22)


def _cip(x, y, metin, renk, dolu=False, yuk=30, boy=12):
    """Yuvarlak köşeli sözcük öbeği; dolu=True ise koyu dolgu üstünde beyaz yazı."""
    w = _gen(metin, boy)
    a, s, f = RENK[renk]
    if dolu:
        ic = f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{f}"/>'
        yazi = 'g-b'
    else:
        ic = (f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{a}"/>'
              f'<rect x="{x}" y="{y}" width="{w}" height="{yuk}" rx="9" class="{s}" stroke-width="2"/>')
        yazi = f
    ic += (f'<text x="{x + w / 2:g}" y="{y + yuk / 2 + 4.5:g}" text-anchor="middle" font-size="{boy}" font-weight="700" '
           f'class="{yazi}">{metin}</text>')
    return w, ic


def _sira(y, parcalar, bosluk=8):
    """Öbekleri yan yana ortalar; (çizim, [(x, w), …]) döndürür."""
    gen = [_gen(m) for m, _, _ in parcalar]
    x = (W - (sum(gen) + bosluk * (len(gen) - 1))) / 2
    ic, yerler = '', []
    for (m, r, d), w in zip(parcalar, gen):
        _, c = _cip(round(x, 1), y, m, r, d)
        ic += c
        yerler.append((round(x, 1), w))
        x += w + bosluk
    return ic, yerler


def _notr_kutu(x, y, w, h, rx=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-z"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="g-c" stroke-width="1.5"/>')


def _renkli_kutu(x, y, w, h, renk, rx=10):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="1.5"/>')


def soru_cevap():
    """Üç soru, cevap türleri: Do you often …? → Yes/No + zarf; How often …? → zarf ya da ifade; Why …? → Because …"""
    ok = 'ok7ing7a'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'

    def soru(y, h, satirlar):
        s = _notr_kutu(10, y, 170, h)
        n = len(satirlar)
        for i, t in enumerate(satirlar):
            by = y + h / 2 + (i - (n - 1) / 2) * 17 + 4.5
            s += f'<text x="95" y="{by:g}" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{t}</text>'
        return s

    def cevap(y, h, renk, baslik, satirlar):
        s = _renkli_kutu(206, y, 254, h, renk)
        s += f'<text x="218" y="{y + 20}" font-size="12" font-weight="700" class="{RENK[renk][2]}">{baslik}</text>'
        for i, t in enumerate(satirlar):
            s += f'<text x="218" y="{y + 39 + i * 18}" font-size="12.5" class="g-y">{t}</text>'
        return s

    # 1) evet/hayır sorusu
    ic += soru(12, 50, ['Do you often', 'go on a diet?'])
    ic += f'<line x1="186" y1="37" x2="198" y2="37" class="g-c" stroke-width="2" marker-end="url(#{ok})"/>'
    ic += cevap(12, 50, 'turuncu', 'Yes / No + sıklık zarfı', ['No, I never go on a diet.'])
    # 2) How often: iki cevap türü
    ic += soru(74, 112, ['How often', 'do you train?'])
    for hedef in (99, 161):
        ic += (f'<path d="M186 130 H192 V{hedef} H198" class="g-c" stroke-width="2" stroke-linejoin="round" '
               f'marker-end="url(#{ok})"/>')
    ic += cevap(74, 50, 'turuncu', 'sıklık zarfı', ['I usually train after school.'])
    ic += cevap(136, 50, 'yesil', 'sıklık ifadesi: … times a week', ['I train three times a week.'])
    # 3) Why: neden
    ic += soru(198, 68, ['Why does Ece', 'go swimming', 'twice a week?'])
    ic += f'<line x1="186" y1="232" x2="198" y2="232" class="g-c" stroke-width="2" marker-end="url(#{ok})"/>'
    ic += cevap(198, 68, 'mor', 'Because + neden (özne + fiil)', ['Because she wants', 'to win a medal.'])
    return svg(W, 278, ic, 'Üç soru ve cevap türleri. Do you often go on a diet? sorusuna Yes ya da No ve bir sıklık zarfıyla cevap verilir: '
               'No, I never go on a diet. How often do you train? sorusunun iki tür cevabı vardır: sıklık zarfı, I usually train after '
               'school; ya da sıklık ifadesi, I train three times a week. Why does Ece go swimming twice a week? sorusunun cevabı because '
               'ile başlar: Because she wants to win a medal. Turuncu sıklık zarfı, yeşil sıklık ifadesi, mor neden.')


def because_semasi():
    """iş + because + neden; neden başa alınınca virgül; because nedeni, so sonucu başlatır."""
    ok = 'ok7ing7b'
    ic = '<defs>' + ok_isareti(ok + 'm', 'g-of') + ok_isareti(ok + 'v', 'g-mf') + '</defs>'
    # 1) temel kalıp
    ic += '<text x="12" y="20" font-size="12" font-weight="700" class="g-s">1) Neden sonda: iş + because + neden</text>'
    s, yer = _sira(28, [('She eats healthy food', 'mavi', False), ('because', 'mor', True), ('she wants to be strong.', 'mor', False)])
    ic += s
    ic += f'<text x="{yer[0][0] + yer[0][1] / 2:g}" y="76" text-anchor="middle" font-size="12" class="g-s">iş: ne yapılıyor?</text>'
    ic += f'<text x="{yer[2][0] + yer[2][1] / 2:g}" y="76" text-anchor="middle" font-size="12" class="g-s">neden: özne + fiil</text>'
    # 2) neden başta → virgül
    ic += '<text x="12" y="104" font-size="12" font-weight="700" class="g-s">2) Neden başta: araya virgül gelir</text>'
    s, yer = _sira(112, [('Because she wants to be strong,', 'mor', False), ('she eats healthy food.', 'mavi', False)])
    ic += s
    vx = yer[0][0] + yer[0][1] - 26
    ic += f'<line x1="{vx:g}" y1="146" x2="{vx:g}" y2="156" class="g-c" stroke-width="2"/>'
    ic += f'<text x="{vx:g}" y="171" text-anchor="middle" font-size="12" class="g-s">virgül</text>'
    # 3) because ↔ so
    ic += '<text x="12" y="200" font-size="12" font-weight="700" class="g-s">3) because nedeni, so sonucu başlatır</text>'
    y = 212
    ic += _renkli_kutu(14, y, 160, 48, 'mavi')
    ic += f'<text x="94" y="{y + 19}" text-anchor="middle" font-size="12" class="g-s">iş / sonuç</text>'
    ic += f'<text x="94" y="{y + 38}" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">she trains hard</text>'
    ic += _renkli_kutu(296, y, 160, 48, 'mor')
    ic += f'<text x="376" y="{y + 19}" text-anchor="middle" font-size="12" class="g-s">neden</text>'
    ic += f'<text x="376" y="{y + 38}" text-anchor="middle" font-size="13" font-weight="700" class="g-of">she wants to win</text>'
    # because oku: işten nedene (sağa)
    ic += f'<line x1="182" y1="{y + 14}" x2="204" y2="{y + 14}" class="g-os" stroke-width="2"/>'
    ic += f'<text x="235" y="{y + 18.5}" text-anchor="middle" font-size="12" font-weight="700" class="g-of">because</text>'
    ic += f'<line x1="266" y1="{y + 14}" x2="288" y2="{y + 14}" class="g-os" stroke-width="2" marker-end="url(#{ok}m)"/>'
    # so oku: nedenden sonuca (sola)
    ic += f'<line x1="288" y1="{y + 36}" x2="250" y2="{y + 36}" class="g-ms" stroke-width="2"/>'
    ic += f'<text x="235" y="{y + 40.5}" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">so</text>'
    ic += f'<line x1="220" y1="{y + 36}" x2="182" y2="{y + 36}" class="g-ms" stroke-width="2" marker-end="url(#{ok}v)"/>'
    ic += ('<text x="235" y="284" text-anchor="middle" font-size="12.5" class="g-y">She trains hard '
           '<tspan font-weight="700" class="g-of">because</tspan> she wants to win.</text>')
    ic += ('<text x="235" y="304" text-anchor="middle" font-size="12.5" class="g-y">She wants to win, '
           '<tspan font-weight="700" class="g-mf">so</tspan> she trains hard.</text>')
    return svg(W, 316, ic, 'Because ile neden açıklama şeması. Kalıp: iş artı because artı neden: She eats healthy food because she wants '
               'to be strong; because’dan sonra özne ve fiil gelir. Neden başa alınırsa araya virgül konur: Because she wants to be '
               'strong, she eats healthy food. Because nedeni, so sonucu başlatır: She trains hard because she wants to win; She wants '
               'to win, so she trains hard. Mavi iş ya da sonuç, mor neden.')


def paragraf_plani():
    """Sporcu rutini paragrafının beş adımı; yeşil sıklık ifadesi, turuncu zarflar, mor because."""
    ok = 'ok7ing7c'
    ic = '<defs>' + ok_isareti(ok, 'g-s') + '</defs>'
    adimlar = [
        ('1', 'Sporcuyu tanıt: adı, yaşı, sporu', '___ is a ___ (swimmer / archer).', None),
        ('2', 'Antrenman sıklığı: how often', 'S/he trains three times a week / every day.', 'yesil'),
        ('3', 'Alışkanlıklar: sıklık zarfları', 'S/he always / usually / sometimes / never ___.', 'turuncu'),
        ('4', 'Neden: because + özne + fiil', 'S/he ___ because s/he wants to ___.', 'mor'),
        ('5', 'Kısa kapanış cümlesi', 'He wants to be a champion.', None),
    ]
    for i, (no, ad, kalip, renk) in enumerate(adimlar):
        y = 10 + i * 60
        if renk:
            a, s, f = RENK[renk]
            ic += f'<circle cx="32" cy="{y + 25}" r="14" class="{f}"/>'
            ic += f'<text x="32" y="{y + 30}" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{no}</text>'
            ic += _renkli_kutu(56, y, 402, 50, renk)
            ic += f'<text x="68" y="{y + 20}" font-size="13" font-weight="700" class="{f}">{ad}</text>'
        else:
            ic += f'<circle cx="32" cy="{y + 25}" r="14" class="g-z"/><circle cx="32" cy="{y + 25}" r="14" class="g-c" stroke-width="1.5"/>'
            ic += f'<text x="32" y="{y + 30}" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{no}</text>'
            ic += _notr_kutu(56, y, 402, 50)
            ic += f'<text x="68" y="{y + 20}" font-size="13" font-weight="700" class="g-y">{ad}</text>'
        ic += f'<text x="68" y="{y + 39}" font-size="12" class="g-y">{kalip}</text>'
        if i < len(adimlar) - 1:
            ic += f'<line x1="32" y1="{y + 43}" x2="32" y2="{y + 66}" class="g-c" stroke-width="2" marker-end="url(#{ok})"/>'
    ic += '<text x="257" y="322" text-anchor="middle" font-size="12" class="g-s">Her adım 1–2 cümle · toplam 60–80 kelime</text>'
    return svg(W, 332, ic, 'Sporcu rutini paragrafının beş adımı sırayla: bir, sporcuyu tanıt: adı, yaşı, sporu; iki, antrenman sıklığını '
               'söyle: S/he trains three times a week, yeşil sıklık ifadesi; üç, alışkanlıkları sıklık zarflarıyla ver: always, usually, '
               'sometimes, never, turuncu; dört, because ile neden açıkla: özne artı fiil, mor; beş, kısa kapanış cümlesi: He wants to '
               'be a champion. Her adım bir iki cümle, toplam 60 ile 80 kelime.')


def uygula(o):
    g = {'Hızlı tekrar: How often? sorusu ve iki tür cevap': soru_cevap(),
         'Because ile neden açıklama': because_semasi(),
         'Yazma: bir sporcunun rutinini anlatan paragraf': paragraf_plani()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
