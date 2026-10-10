"""5. sınıf Fen Bilimleri, 3. hafta: Güneş hakkında bilgi toplama, gözlem verisini yorumlama ve doğrulama.

Görseller yalnız MEB 5. sınıf Fen Bilimleri ders kitabındaki bilgilerle çizilir (kitap PDF s. 23-26).
Renk anlamı: Güneş ve doğrulama = turuncu, koyu bölge (Güneş lekesi) = mor, küçük top = mavi;
bilgi toplama adımları mavi, doğrulama turuncu, kayıt yeşil.
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
    return (_kutu(x, y, w, 26, renk, rx=13)
            + f'<text x="{x + w / 2:g}" y="{y + 18}" text-anchor="middle" font-size="12.5" font-weight="700" '
              f'class="{RENK[renk][2]}">{metin}</text>')


def bilgi_adimlari():
    """Bilgiye ulaşmanın dört adımı: araç belirle, bilgiyi bul, doğrula, kaydet ve düzelt."""
    ic = '<defs>' + ok_isareti('okF3a', 'g-s') + '</defs>'
    adim = [('mavi', 'Araç', 'belirle'), ('mavi', 'Bilgiyi', 'bul'), ('turuncu', 'Bilgiyi', 'doğrula'),
            ('yesil', 'Kaydet', 've düzelt')]
    for i, (renk, s1, s2) in enumerate(adim):
        x = 8 + i * 124
        cx = x + 50
        ic += _kutu(x, 10, 100, 86, renk)
        ic += f'<circle cx="{cx}" cy="32" r="12" class="{RENK[renk][2]}"/>'
        ic += f'<text x="{cx}" y="37" text-anchor="middle" font-size="13" font-weight="800" class="g-b">{i + 1}</text>'
        ic += f'<text x="{cx}" y="62" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{s1}</text>'
        ic += f'<text x="{cx}" y="80" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{s2}</text>'
        if i < 3:
            ic += f'<line x1="{x + 104}" y1="53" x2="{x + 120}" y2="53" class="g-c" stroke-width="2" marker-end="url(#okF3a)"/>'
    for k, (renk, t, w) in enumerate([('mavi', 'Toplama', 84), ('turuncu', 'Doğrulama', 96), ('yesil', 'Kayıt', 66)]):
        ic += _hap(8 + [0, 92, 196][k], 112, w, t, renk)
    ic += '<text x="480" y="130" text-anchor="end" font-size="12" class="g-s">Kayıt çalışma boyunca sürer.</text>'
    return svg(488, 150, ic, 'Bilgiye ulaşmanın dört adımı: 1 araç belirle, 2 bilgiyi bul, 3 bilgiyi doğrula, 4 kaydet ve düzelt. '
               'İlk iki adım bilgi toplamadır, üçüncü adım doğrulamadır, dördüncü adım kayıttır; kayıt çalışma boyunca sürer.')


def leke_cizimleri():
    """Ayşe'nin 1., 3. ve 5. gözlem çizimleri alt alta: A, B ve C bölgeleri soldan sağa kayar."""
    ic = '<defs>' + ok_isareti('okF3b', 'g-tf') + '</defs>'
    R = 40
    sat = [('1. gözlem', [(-26, -9), (-18, 1), (-27, 13)], 'sol tarafta'),
           ('3. gözlem', [(-10, -9), (-2, 0), (-11, 11)], 'ortaya yakın'),
           ('5. gözlem', [(14, -9), (22, 1), (14, 12)], 'sağ tarafta')]
    cx = 190
    ic += '<text x="262" y="16" font-size="12.5" font-weight="800" class="g-y">A, B ve C bölgeleri</text>'
    for k, (ad, noktalar, yer) in enumerate(sat):
        cy = 58 + k * 88
        ic += f'<circle cx="{cx}" cy="{cy}" r="{R}" class="g-ta"/><circle cx="{cx}" cy="{cy}" r="{R}" class="g-ts" stroke-width="2"/>'
        for (dx, dy), harf in zip(noktalar, 'ABC'):
            ic += f'<circle cx="{cx + dx}" cy="{cy + dy}" r="3.6" class="g-of"/>'
            ic += f'<text x="{cx + dx + 6}" y="{cy + dy + 4}" font-size="11" font-weight="800" class="g-y">{harf}</text>'
        ic += f'<text x="20" y="{cy + 5}" font-size="13" font-weight="700" class="g-y">{ad}</text>'
        ic += f'<text x="262" y="{cy + 5}" font-size="12.5" class="g-y">{yer}</text>'
    ic += '<circle cx="26" cy="292" r="4" class="g-of"/><text x="36" y="296" font-size="12" class="g-s">koyu bölge</text>'
    ic += '<line x1="150" y1="292" x2="226" y2="292" class="g-ts" stroke-width="2.2" marker-end="url(#okF3b)"/>'
    ic += '<text x="238" y="296" font-size="12" class="g-s">kayma yönü</text>'
    return svg(440, 308, ic, 'Üç gözlem çizimi alt alta: 1. gözlemde A, B ve C koyu bölgeleri Güneş’in sol tarafında, 3. gözlemde ortaya yakın, '
               '5. gözlemde sağ tarafında. Üç bölge de soldan sağa kayar; bu, Güneş’in kendi ekseni etrafında döndüğünü gösterir.')


def gorunen_boyut():
    """Görünen boyut etkinliği: aynı doğrultuda bir adım uzaktaki küçük top ve en uzaktaki büyük top; gözlemcinin gördüğü."""
    ic = ''
    ic += '<line x1="24" y1="66" x2="36" y2="78" class="g-c" stroke-width="2.2" stroke-linecap="round"/>'
    ic += '<line x1="36" y1="66" x2="24" y2="78" class="g-c" stroke-width="2.2" stroke-linecap="round"/>'
    ic += '<text x="30" y="52" text-anchor="middle" font-size="14" font-weight="800" class="g-y">X</text>'
    ic += '<text x="30" y="98" text-anchor="middle" font-size="12" class="g-s">gözlemci</text>'
    ic += '<line x1="46" y1="72" x2="104" y2="72" class="g-c" stroke-width="1.6" stroke-dasharray="4 4"/>'
    ic += '<text x="75" y="62" text-anchor="middle" font-size="11.5" class="g-s">bir adım</text>'
    ic += '<circle cx="120" cy="72" r="10" class="g-mf"/>'
    ic += '<text x="120" y="100" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">küçük top</text>'
    ic += '<line x1="136" y1="72" x2="334" y2="72" class="g-c" stroke-width="1.6" stroke-dasharray="4 4"/>'
    ic += '<text x="235" y="62" text-anchor="middle" font-size="11.5" class="g-s">aynı doğrultu</text>'
    ic += '<circle cx="370" cy="72" r="28" class="g-tf"/>'
    ic += '<text x="370" y="120" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">büyük top (en uzak)</text>'
    ic += '<text x="20" y="152" font-size="13" font-weight="800" class="g-y">Gözlemcinin gördüğü</text>'
    ic += '<circle cx="110" cy="196" r="21" class="g-mf"/><circle cx="214" cy="196" r="13" class="g-tf"/>'
    ic += '<text x="110" y="236" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">küçük top</text>'
    ic += '<text x="214" y="236" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">büyük top</text>'
    ic += '<text x="270" y="190" font-size="12.5" class="g-y">Uzaktaki büyük top,</text>'
    ic += '<text x="270" y="207" font-size="12.5" class="g-y">yakındaki küçük topa</text>'
    ic += '<text x="270" y="224" font-size="12.5" class="g-y">göre daha küçük görünür.</text>'
    ic += '<text x="452" y="246" text-anchor="end" font-size="11.5" class="g-s">Şematiktir.</text>'
    return svg(460, 254, ic, 'Görünen boyut etkinliği: gözlemci X noktasında; küçük top bir adım uzakta, büyük top aynı doğrultuda en uzakta. '
               'Gözlemci uzaktaki büyük topu yakındaki küçük topa göre daha küçük görür. Şematik çizimdir.')


def uygula(o):
    g = {'Bilgiye ulaşmanın dört adımı': bilgi_adimlari(),
         'Ayşe’nin Güneş gözlemi': leke_cizimleri(),
         'Görünen boyut etkinliği': gorunen_boyut()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
