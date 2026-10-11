"""6. sınıf Fen Bilimleri, 3. hafta: tutulma modelleri (kayıt diyagramı, iki düzenek, model hataları).

Görseller yalnız haftanın metnindeki bilgilerle çizilir (kayıt diyagramı, malzemelerin konumlanma sırası, model kontrolü).
Renk anlamı: turuncu = Güneş tutulması kaydı ve el feneri (Güneş), mavi = büyük top (Dünya) ve Ay tutulması düzeneği,
gri = küçük top (Ay); model hataları görselinde mor = hatalı model, yeşil = düzeltilmiş model.
Boyutlar ve uzaklıklar ölçekli değildir; ölçü yazan öğe yoktur.
"""
from ozet_gorsel import svg, ok_isareti


def _rozet(x, y, w, metin, f, a, s):
    """Yuvarlak uçlu etiket (yükseklik 22): açık zemin, renkli çerçeve ve yazı."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" class="{s}" stroke-width="1.8"/>'
            f'<text x="{x + w / 2:g}" y="{y + 15}" text-anchor="middle" font-size="12" font-weight="700" class="{f}">{metin}</text>')


def _fener(x, cy):
    """El feneri (Güneş'i temsil eder): gövde ve baş; x gövdenin sol kenarı."""
    return (f'<rect x="{x}" y="{cy - 13}" width="44" height="26" rx="5" class="g-ta"/>'
            f'<rect x="{x}" y="{cy - 13}" width="44" height="26" rx="5" class="g-ts" stroke-width="2"/>'
            f'<rect x="{x + 44}" y="{cy - 17}" width="10" height="34" rx="3" class="g-tf"/>')


def _isiklar(x, cy):
    """El fenerinin ışığı: üç kısa ışın."""
    return (f'<line x1="{x}" y1="{cy}" x2="{x + 20}" y2="{cy}" class="g-ts" stroke-width="2" stroke-linecap="round"/>'
            f'<line x1="{x}" y1="{cy - 10}" x2="{x + 18}" y2="{cy - 17}" class="g-ts" stroke-width="2" stroke-linecap="round"/>'
            f'<line x1="{x}" y1="{cy + 10}" x2="{x + 18}" y2="{cy + 17}" class="g-ts" stroke-width="2" stroke-linecap="round"/>')


def kayit_diyagrami():
    """Güneş tutulması için doldurulmuş kayıt diyagramı: merkez soru ve dört bölüm."""
    ic = '<rect x="50" y="8" width="360" height="42" rx="21" class="g-tf"/>'
    ic += ('<text x="230" y="34" text-anchor="middle" font-size="14" font-weight="800" class="g-b">'
           'Güneş tutulması nasıl gerçekleşir?</text>')
    satir = [('Önceden bilinenler', 'Ay, Dünya\'nın çevresinde dolanır.'),
             ('Malzemeler', 'El feneri, büyük top, küçük top'),
             ('Konumlanma sırası', 'El feneri, küçük top, büyük top'),
             ('Öğrenilenler', 'Gölge, büyük topa düştü.')]
    for k, (ad, icerik) in enumerate(satir):
        y = 74 + k * 56
        ic += f'<rect x="16" y="{y}" width="156" height="44" rx="10" class="g-tf"/>'
        ic += f'<text x="94" y="{y + 27}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-b">{ad}</text>'
        ic += f'<rect x="180" y="{y}" width="264" height="44" rx="10" class="g-ta"/>'
        ic += f'<rect x="180" y="{y}" width="264" height="44" rx="10" class="g-ts" stroke-width="2"/>'
        ic += f'<text x="194" y="{y + 27}" font-size="12.5" class="g-y">{icerik}</text>'
    return svg(460, 300, ic, 'Güneş tutulması için doldurulmuş kayıt diyagramı: merkez soru Güneş tutulması nasıl gerçekleşir. '
               'Önceden bilinenler: Ay, Dünya\'nın çevresinde dolanır. Malzemeler: el feneri, büyük top, küçük top. '
               'Konumlanma sırası: el feneri, küçük top, büyük top. Öğrenilenler: gölge, büyük topa düştü.')


def _duzenek(cy, orta_buyuk):
    """Üç malzemeli düzenek. orta_buyuk=False: el feneri, küçük top, büyük top (Güneş tutulması);
    True: el feneri, büyük top, küçük top (Ay tutulması)."""
    ic = _fener(18, cy) + _isiklar(80, cy)
    if not orta_buyuk:
        # gölge: ortadaki küçük toptan büyük topa
        ic += f'<polygon points="200,{cy - 12} 358,{cy - 24} 358,{cy + 24} 200,{cy + 12}" class="g-y" opacity=".22"/>'
        ic += f'<circle cx="200" cy="{cy}" r="12" class="g-s"/>'
        ic += f'<circle cx="380" cy="{cy}" r="30" class="g-mf"/>'
        ic += f'<circle cx="367" cy="{cy}" r="15" class="g-y" opacity=".42"/>'
        orta_ust = cy - 12
        ad = [(45, 'El feneri', '(Güneş)'), (200, 'Küçük top', '(Ay)'), (380, 'Büyük top', '(Dünya)')]
        gol = (276, cy - 40)
    else:
        # gölge: ortadaki büyük toptan küçük topa
        ic += f'<polygon points="200,{cy - 30} 392,{cy - 40} 392,{cy + 40} 200,{cy + 30}" class="g-y" opacity=".22"/>'
        ic += f'<circle cx="200" cy="{cy}" r="30" class="g-mf"/>'
        ic += f'<circle cx="380" cy="{cy}" r="12" class="g-s"/>'
        ic += f'<circle cx="380" cy="{cy}" r="12" class="g-y" opacity=".42"/>'
        orta_ust = cy - 30
        ad = [(45, 'El feneri', '(Güneş)'), (200, 'Büyük top', '(Dünya)'), (380, 'Küçük top', '(Ay)')]
        gol = (296, cy - 48)
    ic += _rozet(171, orta_ust - 32, 58, 'ortada', 'g-of', 'g-oa', 'g-os')
    ic += f'<text x="{gol[0]}" y="{gol[1]}" text-anchor="middle" font-size="12" class="g-y">Gölge</text>'
    for x, a, b in ad:
        ic += f'<text x="{x}" y="{cy + 52}" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">{a}</text>'
        ic += f'<text x="{x}" y="{cy + 68}" text-anchor="middle" font-size="12" class="g-s">{b}</text>'
    return ic


def iki_duzenek():
    """Güneş tutulması ve Ay tutulması düzenekleri: el feneri yerinde kalır, iki top yer değiştirir."""
    ic = '<text x="16" y="22" font-size="13.5" font-weight="800" class="g-tf">Güneş tutulması düzeneği</text>'
    ic += _duzenek(98, False)
    ic += '<text x="16" y="198" font-size="13.5" font-weight="800" class="g-mf">Ay tutulması düzeneği</text>'
    ic += _duzenek(282, True)
    return svg(460, 366, ic, 'İki düzenek. Güneş tutulması düzeneğinde sıra el feneri, küçük top, büyük toptur; ortadaki küçük topun gölgesi '
               'büyük topa düşer. Ay tutulması düzeneğinde sıra el feneri, büyük top, küçük toptur; ortadaki büyük topun gölgesinde küçük top kalır. '
               'El feneri yerinde durur, iki top yer değiştirir. Boyutlar ve uzaklıklar ölçekli değildir.')


def _mini(ox, cy, tur, hatali):
    """Küçük model çizimi. tur: 'ortadaki' (Ay tutulması, ortadaki malzeme yanlış), 'hiza' (Güneş tutulması, hiza bozuk),
    'boyut' (Ay tutulması, toplar yanlış büyüklükte). hatali=False: düzeltilmiş hâl."""
    ic = (f'<rect x="{ox}" y="{cy - 8}" width="26" height="16" rx="4" class="g-ta"/>'
          f'<rect x="{ox}" y="{cy - 8}" width="26" height="16" rx="4" class="g-ts" stroke-width="1.8"/>'
          f'<rect x="{ox + 26}" y="{cy - 11}" width="6" height="22" rx="2" class="g-tf"/>')
    x1, x2 = ox + 84, ox + 170
    ad1 = ad2 = ''
    if tur == 'ortadaki':
        # Ay tutulması: doğru sıra el feneri, Dünya (büyük, mavi), Ay (küçük, gri)
        if hatali:
            ic += f'<polygon points="{x1},{cy - 8} {x2 - 22},{cy - 16} {x2 - 22},{cy + 16} {x1},{cy + 8}" class="g-y" opacity=".22"/>'
            ic += f'<circle cx="{x1}" cy="{cy}" r="8" class="g-s"/><circle cx="{x2}" cy="{cy}" r="18" class="g-mf"/>'
            ad1, ad2 = 'Ay', 'Dünya'
        else:
            ic += f'<polygon points="{x1},{cy - 18} {x2 + 8},{cy - 22} {x2 + 8},{cy + 22} {x1},{cy + 18}" class="g-y" opacity=".22"/>'
            ic += f'<circle cx="{x1}" cy="{cy}" r="18" class="g-mf"/><circle cx="{x2}" cy="{cy}" r="8" class="g-s"/>'
            ic += f'<circle cx="{x2}" cy="{cy}" r="8" class="g-y" opacity=".42"/>'
            ad1, ad2 = 'Dünya', 'Ay'
    elif tur == 'hiza':
        # Güneş tutulması: el feneri, Ay (küçük, gri), Dünya (büyük, mavi); hatalıda Ay yukarı kaymış
        gy = cy - 28 if hatali else cy
        son = x2 - 30 if hatali else x2 - 22
        ic += f'<polygon points="{x1},{gy - 8} {son},{gy - 12} {son},{gy + 12} {x1},{gy + 8}" class="g-y" opacity=".22"/>'
        ic += f'<circle cx="{x1}" cy="{gy}" r="8" class="g-s"/><circle cx="{x2}" cy="{cy}" r="18" class="g-mf"/>'
        if not hatali:
            ic += f'<circle cx="{x2 - 8}" cy="{cy}" r="9" class="g-y" opacity=".42"/>'
        ad1, ad2 = 'Ay', 'Dünya'
    else:
        # Ay tutulması: büyüklükler. Hatalıda Dünya'yı temsil eden top küçük, Ay'ı temsil eden top büyük
        if hatali:
            ic += f'<polygon points="{x1},{cy - 8} {x2 - 22},{cy - 14} {x2 - 22},{cy + 14} {x1},{cy + 8}" class="g-y" opacity=".22"/>'
            ic += f'<circle cx="{x1}" cy="{cy}" r="8" class="g-mf"/><circle cx="{x2}" cy="{cy}" r="18" class="g-s"/>'
            ic += f'<circle cx="{x2}" cy="{cy}" r="18" class="g-y" opacity=".3"/>'
        else:
            ic += f'<polygon points="{x1},{cy - 18} {x2 + 8},{cy - 22} {x2 + 8},{cy + 22} {x1},{cy + 18}" class="g-y" opacity=".22"/>'
            ic += f'<circle cx="{x1}" cy="{cy}" r="18" class="g-mf"/><circle cx="{x2}" cy="{cy}" r="8" class="g-s"/>'
            ic += f'<circle cx="{x2}" cy="{cy}" r="8" class="g-y" opacity=".42"/>'
        ad1, ad2 = 'Dünya', 'Ay'
    ic += f'<text x="{x1}" y="{cy + 40}" text-anchor="middle" font-size="12" class="g-y">{ad1}</text>'
    ic += f'<text x="{x2}" y="{cy + 40}" text-anchor="middle" font-size="12" class="g-y">{ad2}</text>'
    return ic


def model_hatalari():
    """Model kontrolünde bulunan üç hata ve düzeltilmiş hâlleri (hatalı = mor, düzeltilmiş = yeşil)."""
    ic = '<defs>' + ok_isareti('okK3h', 'g-yf') + '</defs>'
    ic += _rozet(34, 8, 150, 'Hatalı model', 'g-of', 'g-oa', 'g-os')
    ic += _rozet(264, 8, 150, 'Düzeltilmiş model', 'g-yf', 'g-ya', 'g-ys')
    bas = [('1. Ay tutulması: ortadaki malzeme yanlış', 'ortadaki'),
           ('2. Güneş tutulması: malzemeler aynı hizada değil', 'hiza'),
           ('3. Ay tutulması: Dünya\'nın topu, Ay\'ın topundan küçük', 'boyut')]
    for k, (ad, tur) in enumerate(bas):
        y0 = 44 + k * 106
        ic += f'<text x="16" y="{y0 + 8}" font-size="12.5" font-weight="800" class="g-y">{ad}</text>'
        cy = y0 + 58
        ic += _mini(12, cy, tur, True)
        ic += f'<line x1="208" y1="{cy}" x2="{244 - 5.4:g}" y2="{cy}" class="g-ys" stroke-width="3" marker-end="url(#okK3h)"/>'
        ic += _mini(252, cy, tur, False)
    return svg(460, 368, ic, 'Model kontrolünde bulunan üç hata ve düzeltilmiş hâlleri. 1: Ay tutulması modelinde ortadaki malzeme yanlışsa '
               'ilgili iki malzemenin yeri değiştirilir. 2: Güneş tutulması modelinde malzemeler aynı hizada değilse hizalama düzeltilir. '
               '3: Ay tutulması modelinde Dünya\'yı temsil eden top Ay\'ı temsil eden toptan küçükse toplar değiştirilir. '
               'Boyutlar ve uzaklıklar ölçekli değildir.')


def uygula(o):
    g = {'Güneş tutulması modeli ve kayıt diyagramı': kayit_diyagrami(),
         'Ay tutulması modeli ve iki düzenek': iki_duzenek(),
         'Modeli değerlendirme ve düzeltme': model_hatalari()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
