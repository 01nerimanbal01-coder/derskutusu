"""6. sınıf Fen Bilimleri, 2. hafta: model oluşturma adımları, Güneş ve Ay tutulmaları.

Görseller yalnız MEB 6. sınıf Fen Bilimleri ders kitabındaki bilgilerle çizilir (kitap s. 15, 29, 33-41).
Renk anlamı: turuncu = Güneş tutulması (ve Güneş), mavi = Ay tutulması (ve Dünya),
model adımlarında mavi = hazırlık, turuncu = model ve test, yeşil = sunum; gri = Ay.
Boyutlar ve uzaklıklar ölçekli değildir (görselde de yazılır).
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


def _hap(x, y, w, metin, renk):
    """Bilgi hapı: açık zemin, renkli çerçeve ve yazı (yükseklik 28)."""
    return (_kutu(x, y, w, 28, renk, rx=14)
            + f'<text x="{x + w / 2:g}" y="{y + 19}" text-anchor="middle" font-size="12.5" font-weight="700" '
              f'class="{RENK[renk][2]}">{metin}</text>')


def model_adimlari():
    """Model oluşturma adımları (kitap s. 15): yedi adım, yılan düzeninde."""
    ic = '<defs>' + ok_isareti('okF62m', 'g-s') + '</defs>'
    adim = [('mavi', 'Problemi', 'tanımla'), ('mavi', 'Araştır,', 'veri topla'),
            ('mavi', 'Çözüm yolları', 'geliştir'), ('turuncu', 'En uygununu', 'seç, oluştur'),
            ('turuncu', 'Modeli', 'test et'), ('turuncu', 'Sorun varsa', 'geliştir'),
            ('yesil', 'Sunumunu', 'yap')]
    yer = [(8, 8), (126, 8), (244, 8), (362, 8), (362, 112), (244, 112), (126, 112)]
    for i, ((renk, s1, s2), (x, y)) in enumerate(zip(adim, yer)):
        cx = x + 50
        ic += _kutu(x, y, 100, 76, renk)
        ic += f'<circle cx="{cx}" cy="{y + 20}" r="12" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{cx}" y="{y + 25}" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="{cx}" y="{y + 48}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="{y + 66}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s2}</text>'
    for x in (110, 228, 346):  # üst sıra: sağa
        ic += f'<line x1="{x}" y1="46" x2="{x + 10}" y2="46" class="g-c" stroke-width="2" marker-end="url(#okF62m)"/>'
    ic += '<line x1="412" y1="86" x2="412" y2="104" class="g-c" stroke-width="2" marker-end="url(#okF62m)"/>'
    for x in (360, 242):  # alt sıra: sola
        ic += f'<line x1="{x}" y1="150" x2="{x - 10}" y2="150" class="g-c" stroke-width="2" marker-end="url(#okF62m)"/>'
    gosterge = [('mavi', 'Hazırlık'), ('turuncu', 'Model ve test'), ('yesil', 'Sunum')]
    for k, (renk, t) in enumerate(gosterge):
        y = 124 + k * 22
        ic += f'<circle cx="16" cy="{y}" r="6" class="{RENK[renk][2]}"/>'
        ic += f'<text x="28" y="{y + 4}" font-size="12" class="g-y">{t}</text>'
    return svg(472, 196, ic, 'Model oluşturma adımları: 1 problemi tanımla, 2 araştır ve veri topla, 3 çözüm yolları geliştir, '
               '4 en uygununu seç ve modeli oluştur, 5 modeli test et, 6 sorun varsa yeni kanıtlara göre geliştir, 7 sunumunu yap.')


def gunes_tutulmasi():
    """Güneş tutulması: Ay, Güneş ile Dünya arasında; Ay'ın gölgesi Dünya'da bir bölgeye düşer (kitap s. 36)."""
    ic = '<polygon points="250,82 364,89 364,95 250,102" class="g-y" opacity=".28"/>'
    ic += '<circle cx="52" cy="92" r="42" class="g-tf"/>'
    ic += '<text x="52" y="97" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Güneş</text>'
    ic += '<circle cx="250" cy="92" r="10" class="g-s"/>'
    ic += '<text x="250" y="68" text-anchor="middle" font-size="13" font-weight="800" class="g-y">Ay</text>'
    ic += '<circle cx="402" cy="92" r="38" class="g-mf"/>'
    ic += '<circle cx="368" cy="92" r="5" class="g-y" opacity=".7"/>'
    ic += '<text x="414" y="97" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Dünya</text>'
    ic += '<text x="306" y="122" text-anchor="middle" font-size="12" class="g-y">Ay\'ın gölgesi</text>'
    ic += '<text x="402" y="148" text-anchor="middle" font-size="12" class="g-y">Gölgenin düştüğü</text>'
    ic += '<text x="402" y="164" text-anchor="middle" font-size="12" class="g-y">bölgeden görülür</text>'
    ic += _hap(8, 136, 140, 'Yeni ay evresi', 'turuncu')
    ic += _hap(156, 136, 140, 'Gündüz gözlenir', 'turuncu')
    ic += _hap(8, 172, 288, 'Ay tutulmasından dar alanda görülür', 'turuncu')
    ic += '<text x="464" y="194" text-anchor="end" font-size="12" class="g-s">Ölçekli değildir.</text>'
    return svg(472, 208, ic, 'Güneş tutulması: Güneş, Ay ve Dünya aynı hizada; Ay ortada. Ay\'ın gölgesi Dünya\'da bir bölgeye düşer, '
               'tutulma yalnız o bölgeden görülür. Yeni ay evresinde, gündüz gözlenir; Ay tutulmasından daha dar alanda görülür. '
               'Boyutlar ve uzaklıklar ölçekli değildir.')


def ay_tutulmasi():
    """Ay tutulması: Dünya, Güneş ile Ay arasında; Ay, Dünya'nın gölgesinde kalır (kitap s. 36)."""
    ic = '<polygon points="252,60 462,80 462,104 252,124" class="g-y" opacity=".28"/>'
    ic += '<circle cx="52" cy="92" r="42" class="g-tf"/>'
    ic += '<text x="52" y="97" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Güneş</text>'
    ic += '<circle cx="252" cy="92" r="32" class="g-mf"/>'
    ic += '<text x="252" y="97" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Dünya</text>'
    ic += '<circle cx="420" cy="92" r="11" class="g-s" opacity=".55"/>'
    ic += '<text x="420" y="64" text-anchor="middle" font-size="13" font-weight="800" class="g-y">Ay</text>'
    ic += '<text x="350" y="134" text-anchor="middle" font-size="12" class="g-y">Dünya\'nın gölgesi</text>'
    hap = [(8, 'Dolunay evresi'), (124, 'Gece gözlenir'), (240, 'Geniş alanda'), (356, 'Daha uzun sürer')]
    for x, t in hap:
        ic += _hap(x, 150, 108, t, 'mavi')
    ic += ('<text x="8" y="202" font-size="12" class="g-y">Ay, Dünya\'nın gölgesinde kalır ve bir süre parlak görünmez.</text>')
    ic += '<text x="464" y="202" text-anchor="end" font-size="12" class="g-s">Ölçekli değildir.</text>'
    return svg(472, 212, ic, 'Ay tutulması: Güneş, Dünya ve Ay aynı hizada; Dünya ortada. Ay, Dünya\'nın gölgesinde kalır ve bir süre '
               'parlak görünmez. Dolunay evresinde, gece gözlenir; daha geniş alanda görülür ve daha uzun sürer. '
               'Boyutlar ve uzaklıklar ölçekli değildir.')


def karsilastirma():
    """Güneş tutulması ile Ay tutulmasının karşılaştırılması (kitap s. 36-37, 39)."""
    ic = ''
    ic += '<rect x="122" y="8" width="168" height="30" rx="8" class="g-tf"/>'
    ic += '<text x="206" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Güneş tutulması</text>'
    ic += '<rect x="296" y="8" width="168" height="30" rx="8" class="g-mf"/>'
    ic += '<text x="380" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">Ay tutulması</text>'
    satir = [('Sıralama', 'Güneş – Ay – Dünya', 'Güneş – Dünya – Ay'),
             ('Ortadaki', 'Ay', 'Dünya'),
             ('Gölge', 'Ay\'ın gölgesi Dünya\'ya', 'Ay, Dünya\'nın gölgesinde'),
             ('Ay\'ın evresi', 'Yeni ay', 'Dolunay'),
             ('Zaman', 'Gündüz', 'Gece'),
             ('Gözlem alanı', 'Daha dar', 'Daha geniş'),
             ('Süre', 'Daha kısa', 'Daha uzun')]
    for k, (ad, g, a) in enumerate(satir):
        y = 44 + k * 30
        ic += f'<rect x="8" y="{y}" width="108" height="26" rx="6" class="g-z"/>'
        ic += f'<rect x="8" y="{y}" width="108" height="26" rx="6" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="16" y="{y + 18}" font-size="12.5" font-weight="800" class="g-y">{ad}</text>'
        ic += f'<rect x="122" y="{y}" width="168" height="26" rx="6" class="g-ta"/>'
        ic += f'<text x="206" y="{y + 18}" text-anchor="middle" font-size="12.5" class="g-y">{g}</text>'
        ic += f'<rect x="296" y="{y}" width="168" height="26" rx="6" class="g-ma"/>'
        ic += f'<text x="380" y="{y + 18}" text-anchor="middle" font-size="12.5" class="g-y">{a}</text>'
    return svg(472, 258, ic, 'Karşılaştırma: Güneş tutulmasında sıralama Güneş, Ay, Dünya; ortada Ay; Ay\'ın gölgesi Dünya\'ya düşer; '
               'yeni ay evresinde, gündüz; daha dar alanda, daha kısa. Ay tutulmasında sıralama Güneş, Dünya, Ay; ortada Dünya; '
               'Ay Dünya\'nın gölgesinde kalır; dolunay evresinde, gece; daha geniş alanda, daha uzun.')


def uygula(o):
    g = {'Bilimsel model nasıl oluşturulur?': model_adimlari(),
         'Güneş tutulması': gunes_tutulmasi(),
         'Ay tutulması': ay_tutulmasi(),
         'Güneş ve Ay tutulmasını karşılaştırma': karsilastirma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
