"""6. sınıf Sosyal Bilgiler, 2. hafta: gelecekteki roller, söyleşi tablosu, etkinlik akışı.

Görseller yalnız MEB 6. sınıf Sosyal Bilgiler ders kitabındaki bilgilerle çizilir (kitap s. 16-22).
Renk anlamı: mavi = eğitim grupları / günümüz, turuncu = spor ve sanat grupları / geçmiş,
yeşil = toplum ve aile grupları / değerlendirme adımları. Söyleşi tablosundaki örnek kurgusaldır
(alıştırma örneği), kitaptaki tablo başlıkları (yer aldığı grup, rol, hak, sorumluluk) aynen kullanılır.
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


def gelecek_kartlari():
    """Kitaptaki altı gelecek kartı (s. 16): eğitim mavi, spor ve sanat turuncu, toplum ve aile yeşil."""
    kart = [('mavi', 'Kart 1', ('TÜBİTAK proje', 'takımında çalışkan', 'bir öğrenci')),
            ('mavi', 'Kart 2', ('Başarılı bir', 'üniversite', 'öğrencisi')),
            ('turuncu', 'Kart 3', ('Ülkesini temsil eden', 'disiplin sahibi', 'millî sporcu')),
            ('turuncu', 'Kart 4', ('Başarılı bir müzik', 'grubunda enstrüman', 'çalan müzisyen')),
            ('yesil', 'Kart 5', ('Topluma duyarlı bir', 'sivil toplum', 'kuruluşuna üye')),
            ('yesil', 'Kart 6', ('Evlatları ve torunları', 'tarafından sevilen', 'bir aile büyüğü'))]
    ic = ''
    for i, (renk, bas, satir) in enumerate(kart):
        x = 8 + (i % 3) * 154
        y = 8 + (i // 3) * 104
        cx = x + 74
        ic += _kutu(x, y, 148, 94, renk)
        ic += (f'<path d="M{x + 12},{y} h124 a12,12 0 0 1 12,12 v14 h-148 v-14 a12,12 0 0 1 12,-12 z" '
               f'class="{RENK[renk][2]}"/>')
        ic += f'<text x="{cx}" y="{y + 18}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{bas}</text>'
        for k, t in enumerate(satir):
            ic += f'<text x="{cx}" y="{y + 48 + k * 17}" text-anchor="middle" font-size="12" class="g-y">{t}</text>'
    gosterge = [('mavi', 'Eğitim'), ('turuncu', 'Spor ve sanat'), ('yesil', 'Toplum ve aile')]
    for k, (renk, t) in enumerate(gosterge):
        x = 8 + k * 154
        ic += f'<circle cx="{x + 8}" cy="226" r="6" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{x + 20}" y="230" font-size="12" class="g-y">{t}</text>'
    return svg(472, 240, ic, 'Gelecek kartları: TÜBİTAK proje takımında çalışkan bir öğrenci, başarılı bir üniversite öğrencisi, '
               'ülkesini temsil eden disiplin sahibi millî sporcu, başarılı bir müzik grubunda enstrüman çalan müzisyen, '
               'topluma duyarlı bir sivil toplum kuruluşuna üye, evlatları ve torunları tarafından sevilen bir aile büyüğü.')


def soylesi_tablosu():
    """Geçmiş–günümüz karşılaştırma tablosu (s. 19) kurgusal bir söyleşi örneğiyle."""
    ic = '<rect x="122" y="8" width="168" height="30" rx="8" class="g-tf"/>'
    ic += '<text x="206" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">GEÇMİŞ</text>'
    ic += '<rect x="296" y="8" width="168" height="30" rx="8" class="g-mf"/>'
    ic += '<text x="380" y="28" text-anchor="middle" font-size="13" font-weight="800" class="g-b">GÜNÜMÜZ</text>'
    satir = [('Yer aldığı grup', 'Köy okulu (okul grubu)', 'Aile ve akraba grubu'),
             ('Rol', 'Öğrenci', 'Anneanne'),
             ('Hak', 'Eğitim alma', 'Sevgi ve saygı görme'),
             ('Sorumluluk', 'Derslerine çalışma', 'Torunlarına yol gösterme')]
    for k, (ad, g, a) in enumerate(satir):
        y = 46 + k * 32
        ic += f'<rect x="8" y="{y}" width="108" height="26" rx="6" class="g-z"/>'
        ic += f'<rect x="8" y="{y}" width="108" height="26" rx="6" class="g-c" stroke-width="1.5"/>'
        ic += f'<text x="16" y="{y + 18}" font-size="12.5" font-weight="800" class="g-y">{ad}</text>'
        ic += f'<rect x="122" y="{y}" width="168" height="26" rx="6" class="g-ta"/>'
        ic += f'<text x="206" y="{y + 18}" text-anchor="middle" font-size="12.5" class="g-y">{g}</text>'
        ic += f'<rect x="296" y="{y}" width="168" height="26" rx="6" class="g-ma"/>'
        ic += f'<text x="380" y="{y + 18}" text-anchor="middle" font-size="12.5" class="g-y">{a}</text>'
    ic += '<text x="8" y="196" font-size="12" class="g-s">Örnek söyleşi: Elif\'in anneannesi. Rol değişince hak ve sorumluluk da değişir.</text>'
    return svg(472, 206, ic, 'Geçmiş–günümüz karşılaştırma tablosu: satırlar yer aldığı grup, rol, hak, sorumluluk. '
               'Örnek söyleşi: geçmişte köy okulunda öğrenci, eğitim alma hakkı, derslerine çalışma sorumluluğu; '
               'günümüzde aile ve akraba grubunda anneanne, sevgi ve saygı görme hakkı, torunlarına yol gösterme sorumluluğu.')


def etkinlik_akisi():
    """'Gelecekte dâhil olacağım gruplar ve rollerim' etkinliğinin adımları (s. 20-21), yılan düzeninde."""
    ic = '<defs>' + ok_isareti('okS62e', 'g-s') + '</defs>'
    adim = [('mavi', 'Mesleğini', 'hayal et'), ('mavi', 'Grup ve', 'rollerini söyle'),
            ('mavi', 'Grup, rol, hak,', 'sorumluluk tablosu'),
            ('turuncu', 'Grupla ortak tablo', '(kartona çiz)'), ('turuncu', 'Tabloyu panoya', 'as'),
            ('yesil', 'İncele, yapışkan', 'notla geri bildir')]
    yer = [(8, 8), (166, 8), (324, 8), (324, 100), (166, 100), (8, 100)]
    for i, ((renk, s1, s2), (x, y)) in enumerate(zip(adim, yer)):
        cx = x + 70
        ic += _kutu(x, y, 140, 74, renk, rx=10)
        ic += f'<circle cx="{cx}" cy="{y + 18}" r="11" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{cx}" y="{y + 23}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="{cx}" y="{y + 46}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="{y + 63}" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{s2}</text>'
    for x in (150, 308):  # üst sıra: sağa
        ic += f'<line x1="{x}" y1="45" x2="{x + 10}" y2="45" class="g-c" stroke-width="2" marker-end="url(#okS62e)"/>'
    ic += '<line x1="394" y1="84" x2="394" y2="94" class="g-c" stroke-width="2" marker-end="url(#okS62e)"/>'
    for x in (322, 164):  # alt sıra: sola
        ic += f'<line x1="{x}" y1="137" x2="{x - 10}" y2="137" class="g-c" stroke-width="2" marker-end="url(#okS62e)"/>'
    ic += _kutu(8, 190, 456, 96, 'yesil')
    ic += '<text x="236" y="212" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">Panoyu incelerken üç soru</text>'
    soru = ['Öğrenciler hangi gruplara dâhil olmayı hayal etmiş?',
            'Benim tahmin etmediğim roller var mı?',
            'Hak ve sorumluluklarda hangi benzerlik ve farklılıklar var?']
    for k, t in enumerate(soru):
        y = 234 + k * 20
        ic += f'<circle cx="26" cy="{y - 4}" r="4" class="g-yf"/>'
        ic += f'<text x="38" y="{y}" font-size="12" class="g-y">{t}</text>'
    return svg(472, 294, ic, 'Etkinlik akışı: 1 mesleğini hayal et, 2 grup ve rollerini söyle, 3 grup, rol, hak, sorumluluk tablosunu doldur, '
               '4 grupla ortak tabloyu kartona çiz, 5 tabloyu panoya as, 6 incele ve yapışkan notla geri bildirim ver. '
               'Panoyu incelerken üç soru: hangi gruplar hayal edilmiş, tahmin etmediğim roller var mı, '
               'hak ve sorumluluklarda hangi benzerlik ve farklılıklar var.')


def uygula(o):
    g = {'Gelecekte üstlenebileceğimiz roller': gelecek_kartlari(),
         'Geçmişten günümüze roller: söyleşi': soylesi_tablosu(),
         'Gelecekteki grup ve rollerimizi tahmin etme': etkinlik_akisi()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
