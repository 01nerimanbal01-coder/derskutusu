"""8. sınıf İngilizce, 3. hafta (1 Friendship): metinde ana fikir ve kanıt, konuşmalardan ayrıntı, teklif–kabul–ret, e-posta yapısı.

Görseller yalnız MEB 8. sınıf İngilizce ders kitabındaki bilgilerle çizilir (Friendship ünitesi, PDF s11–s21).
Renk anlamı: özellik sıfatı = mavi, kanıt davranış = turuncu; kabul = yeşil, ret = turuncu; teklif = yeşil, kalıp = mor;
e-postada selam = mavi, etkinlik/gün/saat = yeşil, davet sorusu = turuncu, kapanış = mor.
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


def ozellik_kanit():
    """Davranıştan özelliğe: Lily'nin iyi yönleri ve onları gösteren davranışlar (kitap s11)."""
    ic = '<defs>' + ok_isareti('okK31', 'g-s') + '</defs>' + _baslik('Davranıştan özelliğe')
    ic += '<text x="12" y="46" font-size="12" font-weight="700" class="g-tf">Davranış (kanıt)</text>'
    ic += '<text x="306" y="46" font-size="12" font-weight="700" class="g-mf">Özellik</text>'
    satirlar = [('helps me when I need it', 'supportive'), ('cheers me up when I feel sad', 'kind'),
                ('tells me the truth', 'honest'), ('keeps my secrets', 'trustworthy'), ('we never argue', 'get on well')]
    for i, (dav, oz) in enumerate(satirlar):
        y = 56 + i * 42
        ic += _kutu(12, y, 250, 34, 'turuncu')
        ic += f'<text x="24" y="{y + 22}" font-size="12.5" font-weight="700" class="g-tf">{dav}</text>'
        ic += f'<line x1="270" y1="{y + 17}" x2="298" y2="{y + 17}" class="g-c" stroke-width="2" marker-end="url(#okK31)"/>'
        ic += _kutu(306, y, 152, 34, 'mavi')
        ic += f'<text x="382" y="{y + 22}" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">{oz}</text>'
    return svg(470, 272, ic, 'Davranıştan özelliğe: helps me when I need it supportive anlamına gelir; cheers me up when I feel sad kind; '
               'tells me the truth honest; keeps my secrets trustworthy; we never argue ise get on well ifadesini gösterir.')


def konusma_ozeti():
    """Dört kısa konuşma: kim kimi neye davet ediyor, cevap ve gerekçe (kitap s14)."""
    ic = _baslik('Dört konuşma, dört sonuç')
    kartlar = [('David → Bob · dinner', 'Cevap: “Yes, why not?”', 'Kabul'),
               ('Jamie → Tanya · cinema, weekend', 'Gerekçe: ödev · sonra başka zaman', 'Ret'),
               ('Angel → Jenny · fruit juice', 'Gerekçe: kız kardeşini eve götürmek · sonra yarın', 'Ret'),
               ('Thomas → John · concert', 'Cevap: kabul · buluşma saati 7 p.m.', 'Kabul')]
    for i, (l1, l2, durum) in enumerate(kartlar):
        y = 34 + i * 58
        renk = 'yesil' if durum == 'Kabul' else 'turuncu'
        ic += _kutu(12, y, 446, 50, renk)
        ic += f'<text x="26" y="{y + 21}" font-size="13" font-weight="700" class="g-y">{l1}</text>'
        ic += f'<text x="26" y="{y + 40}" font-size="11.5" class="g-y">{l2}</text>'
        ic += f'<rect x="384" y="{y + 13}" width="62" height="24" rx="12" class="{RENK[renk][2]}"/>'
        ic += f'<text x="415" y="{y + 29.5}" text-anchor="middle" font-size="12" font-weight="800" class="g-b">{durum}</text>'
    return svg(470, 268, ic, 'Dört kısa konuşma: David Bob’u akşam yemeğine çağırır, Bob kabul eder. Jamie Tanya’yı sinemaya çağırır, Tanya ödev nedeniyle reddeder ve başka zaman önerilir. '
               'Angel Jenny’ye meyve suyu ikram eder, Jenny kız kardeşini eve götürmesi gerektiği için reddeder ve yarın planlanır. Thomas John’u konsere çağırır, John kabul eder ve saat 7’de buluşurlar.')


def oneri_haritasi():
    """Duruma uygun öneri ve kalıbı (kitap s17–s18)."""
    ic = '<defs>' + ok_isareti('okK33', 'g-s') + '</defs>' + _baslik('Duruma uygun öneri')
    satirlar = [('Arkadaşın aç', 'What about eating something?', 'What about + fiil-ing'),
                ('Sıkılıyorsun', 'How about watching a film?', 'How about + fiil-ing'),
                ('Yorgunsun', 'Let’s have a rest!', 'Let’s + yalın fiil'),
                ('Boş öğleden sonra', 'Shall we play tennis?', 'Shall we + yalın fiil')]
    for i, (durum, oneri, kalip) in enumerate(satirlar):
        y = 34 + i * 54
        ic += _kutu(12, y, 140, 46, 'mavi')
        ic += f'<text x="82" y="{y + 28}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-mf">{durum}</text>'
        ic += f'<line x1="158" y1="{y + 23}" x2="184" y2="{y + 23}" class="g-c" stroke-width="2" marker-end="url(#okK33)"/>'
        ic += _kutu(190, y, 268, 46, 'yesil')
        ic += f'<text x="204" y="{y + 20}" font-size="13" font-weight="700" class="g-y">{oneri}</text>'
        ic += f'<text x="204" y="{y + 37}" font-size="11.5" font-weight="700" class="g-of">{kalip}</text>'
    return svg(470, 254, ic, 'Duruma uygun öneri: arkadaşın açsa What about eating something?, sıkılıyorsan How about watching a film?, yorgunsan Let’s have a rest!, '
               'boş bir öğleden sonranız varsa Shall we play tennis? denir. What about ve How about fiil-ing, Let’s ve Shall we yalın fiil alır.')


def eposta_yapisi():
    """Davet e-postasının parçaları (kitap s19)."""
    ic = _baslik('Davet e-postasının parçaları')
    parcalar = [('Hi Tim,', 'Selamlama', 'mavi'),
                ('We have a picnic on Sunday at ten.', 'Etkinlik, gün, saat', 'yesil'),
                ('Would you like to join us?', 'Davet sorusu', 'turuncu'),
                ('Love, Ela', 'Kapanış, gönderen', 'mor')]
    for i, (satir, etiket, renk) in enumerate(parcalar):
        y = 36 + i * 46
        ic += _kutu(12, y, 290, 38, renk)
        ic += f'<text x="26" y="{y + 24}" font-size="13" font-weight="700" class="{RENK[renk][2]}">{satir}</text>'
        ic += f'<text x="316" y="{y + 24}" font-size="12.5" font-weight="700" class="{RENK[renk][2]}">{etiket}</text>'
    return svg(470, 222, ic, 'Davet e-postasının parçaları: Hi Tim selamlama, We have a picnic on Sunday at ten etkinlik gün ve saat, '
               'Would you like to join us davet sorusu, Love Ela kapanış ve gönderen adıdır.')


def uygula(o):
    g = {'Metnin ana fikri ve kanıtları': ozellik_kanit(),
         'Konuşmalardan ayrıntı yakalama': konusma_ozeti(),
         'Teklif, kabul ve ret': oneri_haritasi(),
         'Davet e-postasından bilgi çıkarma': eposta_yapisi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
