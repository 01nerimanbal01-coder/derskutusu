"""6. sınıf Din Kültürü ve Ahlak Bilgisi, 2. hafta: Hz. İbrahim kıssası, bilgi toplama adımları,
ayetlerin doğruladığı bilgiler, 3-2-1 kartı.

Görseller yalnız MEB 6. sınıf Din Kültürü ve Ahlak Bilgisi ders kitabındaki bilgilerle çizilir
(kitap s. 13, 16-23). Renk anlamı: mavi = bulma / görevler, turuncu = doğrulama / özellikler,
yeşil = kaydetme. Ayet–bilgi eşlemesi, kitaptaki Bilgi Görseli 1.3 (özellikler) ve 1.4 (görevler)
başlıklarına göre yapılmıştır.
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


def kissa_akisi():
    """Hz. İbrahim kıssasının dört adımı (kitap s. 13), yılan düzeninde."""
    ic = '<defs>' + ok_isareti('okD62k', 'g-s') + '</defs>'
    adim = [('mavi', 'Bayram günü şehir boşalır;', 'Hz. İbrahim geri döner.'),
            ('mavi', 'Putları kırar, baltayı', 'en büyük putun boynuna asar.'),
            ('turuncu', 'Halk sorunca: “Ona sorun,', 'belki o yapmıştır.”'),
            ('yesil', '“Hiçbir şey yapamıyorsa', 'niçin ona inanıyorsunuz?”')]
    yer = [(8, 8), (248, 8), (248, 96), (8, 96)]
    for i, ((renk, s1, s2), (x, y)) in enumerate(zip(adim, yer)):
        cx = x + 108
        ic += _kutu(x, y, 216, 72, renk, rx=10)
        ic += f'<circle cx="{x + 20}" cy="{y + 20}" r="11" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + 20}" y="{y + 25}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="{cx}" y="{y + 46}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="{y + 63}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s2}</text>'
    ic += '<line x1="226" y1="44" x2="238" y2="44" class="g-c" stroke-width="2" marker-end="url(#okD62k)"/>'
    ic += '<line x1="356" y1="82" x2="356" y2="90" class="g-c" stroke-width="2" marker-end="url(#okD62k)"/>'
    ic += '<line x1="246" y1="132" x2="234" y2="132" class="g-c" stroke-width="2" marker-end="url(#okD62k)"/>'
    return svg(472, 176, ic, 'Hz. İbrahim kıssasının akışı: 1 bayram günü şehir boşalır, Hz. İbrahim geri döner; '
               '2 putları kırar, baltayı en büyük putun boynuna asar; 3 halk sorunca “Ona sorun, belki o yapmıştır.” der; '
               '4 “Hiçbir şey yapamıyorsa niçin ona inanıyorsunuz?” diye sorarak insanları düşünmeye yöneltir.')


def bilgi_adimlari():
    """Bilgi toplamanın üç adımı: bul, doğrula, kaydet (kitap s. 16-23 etkinlik amaçları)."""
    ic = '<defs>' + ok_isareti('okD62b', 'g-s') + '</defs>'
    adim = [('mavi', 'BUL', ('Kur’an-ı Kerim', 'Güvenilir kaynaklar', 'Kaynağı deftere yaz')),
            ('turuncu', 'DOĞRULA', ('Ayet ve hadislerle', 'Öğretmen rehberliği', 'Doğrulananı yaz')),
            ('yesil', 'KAYDET', ('“Yazalım” şeması', '3-2-1 kartı', 'Öğrenme günlüğü'))]
    for i, (renk, bas, satir) in enumerate(adim):
        x = 8 + i * 160
        cx = x + 72
        ic += _kutu(x, 8, 144, 110, renk)
        ic += (f'<path d="M{x + 12},8 h120 a12,12 0 0 1 12,12 v16 h-144 v-16 a12,12 0 0 1 12,-12 z" '
               f'class="{RENK[renk][2]}"/>')
        ic += f'<text x="{cx}" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{i + 1}. {bas}</text>'
        for k, t in enumerate(satir):
            ic += f'<text x="{cx}" y="{58 + k * 20}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
    for x in (154, 314):
        ic += f'<line x1="{x}" y1="64" x2="{x + 10}" y2="64" class="g-c" stroke-width="2" marker-end="url(#okD62b)"/>'
    return svg(472, 126, ic, 'Bilgi toplamanın üç adımı: 1 bul (Kur’an-ı Kerim temel kaynak, TDV İslâm Ansiklopedisi gibi '
               'güvenilir kaynaklar, kaynağı da deftere yazma); 2 doğrula (ayet ve hadislerle, öğretmen rehberliğinde, '
               'doğrulananı alana yazma); 3 kaydet (“Yazalım” şeması, 3-2-1 kartı, öğrenme günlüğü).')


def ayet_tablosu():
    """Etkinlikteki ayetler ve doğruladıkları bilgi (kitap s. 20-21); görev mavi, özellik turuncu."""
    ic = '<rect x="8" y="8" width="150" height="30" rx="8" class="g-s"/>'
    ic += '<text x="83" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Ayet</text>'
    ic += '<rect x="166" y="8" width="298" height="30" rx="8" class="g-s"/>'
    ic += '<text x="315" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Doğruladığı bilgi</text>'
    satir = [('mavi', 'Maide 67 ve 92', 'Tebliğ: indirileni apaçık duyurma'),
             ('mavi', 'Ahzab 21', 'Örneklik: Resul’de güzel bir örnek'),
             ('mavi', 'Nisa 165', 'Müjdeleme ve uyarma'),
             ('mavi', 'İbrahim 4', 'Kavminin diliyle iyice açıklama'),
             ('turuncu', 'Meryem 56', 'Sıdk: Hz. İdris pek doğru bir insandı'),
             ('turuncu', 'Şuara 143', 'Emanet: güvenilir bir elçi'),
             ('turuncu', 'Enbiya 62-63', 'Fetanet: Hz. İbrahim düşündürür'),
             ('turuncu', 'Nisa 113', 'İsmet: Allah’ın koruması')]
    for k, (renk, a, b) in enumerate(satir):
        y = 44 + k * 30
        ic += f'<rect x="8" y="{y}" width="150" height="26" rx="6" class="{RENK[renk][0]}"/>'
        ic += f'<text x="16" y="{y + 18}" font-size="12.5" font-weight="800" class="g-y">{a}</text>'
        ic += f'<rect x="166" y="{y}" width="298" height="26" rx="6" class="{RENK[renk][0]}"/>'
        ic += f'<text x="176" y="{y + 18}" font-size="12.5" class="g-y">{b}</text>'
    gosterge = [('mavi', 'Görev (Bilgi Görseli 1.4)'), ('turuncu', 'Özellik (Bilgi Görseli 1.3)')]
    for k, (renk, t) in enumerate(gosterge):
        x = 8 + k * 230
        ic += f'<circle cx="{x + 8}" cy="300" r="6" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + 20}" y="304" font-size="12" class="g-y">{t}</text>'
    return svg(472, 314, ic, 'Ayetler ve doğruladıkları bilgi: Maide 67 ve 92 tebliğ; Ahzab 21 örneklik; Nisa 165 müjdeleme ve '
               'uyarma; İbrahim 4 kavminin diliyle açıklama (görevler). Meryem 56 sıdk; Şuara 143 emanet; Enbiya 62-63 fetanet; '
               'Nisa 113 ismet (özellikler).')


def kayit_karti():
    """3-2-1 kartı (kitap s. 22): üç bilgi, iki kavram, bir kavram."""
    ic = ''
    kart = [('mavi', '3', 'Bu konuda öğrendiğim üç bilgi', 3),
            ('turuncu', '2', 'Bu konuda çalışmam gereken iki kavram', 2),
            ('yesil', '1', 'Bu konuda dikkatimi çeken bir kavram', 1)]
    y = 8
    for renk, sayi, bas, n in kart:
        h = 34 + n * 18
        ic += _kutu(8, y, 456, h, renk)
        ic += f'<circle cx="34" cy="{y + 24}" r="14" class="{RENK[renk][2]}"/>'
        ic += f'<text x="34" y="{y + 29}" text-anchor="middle" font-size="14" font-weight="800" class="g-b">{sayi}</text>'
        ic += f'<text x="58" y="{y + 29}" font-size="12.5" font-weight="800" class="g-y">{bas}</text>'
        for k in range(n):
            ly = y + 46 + k * 18
            ic += f'<text x="58" y="{ly + 4}" font-size="12" class="g-s">{k + 1}.</text>'
            ic += f'<line x1="74" y1="{ly + 2}" x2="452" y2="{ly + 2}" class="g-c" stroke-width="1.5" stroke-dasharray="2 3"/>'
        y += h + 8
    return svg(472, y, ic, '3-2-1 kartı: bu konuda öğrendiğim üç bilgi (üç satır), bu konuda çalışmam gereken iki kavram '
               '(iki satır), bu konuda dikkatimi çeken bir kavram (bir satır).')


def uygula(o):
    g = {'Hz. İbrahim kıssası: düşündürerek yol göstermek': kissa_akisi(),
         'Bilgi toplamanın üç adımı: bul, doğrula, kaydet': bilgi_adimlari(),
         'Ayetler hangi bilgiyi doğrular?': ayet_tablosu(),
         'Öğrendiklerini kaydetmek: şema, 3-2-1 kartı ve öğrenme günlüğü': kayit_karti()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
