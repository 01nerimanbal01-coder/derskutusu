"""5. sınıf Fen Bilimleri, 4. hafta: Ay'ın özellikleri, dönme ve dolanma hareketleri.

Görseller yalnız MEB 5. sınıf Fen Bilimleri ders kitabındaki bilgilerle çizilir (kitap PDF s. 29-35).
Renk anlamı: Güneş ve Güneş ışığı = turuncu, Dünya = mavi, Ay = gri, Ay'ın Dünya'ya bakan yüzü = turuncu nokta,
yüzeyin parçalanma zinciri = mor; gündüz = turuncu, gece = mavi. Boyutlar ve uzaklıklar ölçekli değildir (görselde de yazılır).
"""
import math
from ozet_gorsel import svg, ok_isareti

RENK = {  # (dolgu, çerçeve, yazı)
    'turuncu': ('g-ta', 'g-ts', 'g-tf'),
    'mavi': ('g-ma', 'g-ms', 'g-mf'),
    'mor': ('g-oa', 'g-os', 'g-of'),
}


def _kutu(x, y, w, h, renk, rx=12):
    a, s, _ = RENK[renk]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{a}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{s}" stroke-width="2"/>')


def ay_isigi():
    """Ay ışık kaynağı değildir: Güneş'ten gelen ışığı yansıtır ve Dünya'dan görülür."""
    ic = '<defs>' + ok_isareti('okF4a', 'g-tf') + '</defs>'
    ic += '<circle cx="52" cy="62" r="36" class="g-tf"/>'
    ic += '<text x="52" y="67" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Güneş</text>'
    ic += '<circle cx="250" cy="52" r="20" class="g-s"/>'
    ic += '<text x="250" y="94" text-anchor="middle" font-size="13" font-weight="800" class="g-y">Ay</text>'
    ic += '<circle cx="388" cy="150" r="32" class="g-mf"/>'
    ic += '<text x="388" y="155" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Dünya</text>'
    ic += '<line x1="98" y1="58" x2="220" y2="53" class="g-ts" stroke-width="2.4" marker-end="url(#okF4a)"/>'
    ic += '<text x="160" y="40" text-anchor="middle" font-size="12.5" class="g-y">Güneş’ten gelen ışık</text>'
    ic += '<line x1="270" y1="70" x2="352" y2="126" class="g-ts" stroke-width="2.4" stroke-dasharray="6 5" marker-end="url(#okF4a)"/>'
    ic += '<text x="318" y="82" font-size="12.5" class="g-y">Ay’dan yansıyan</text>'
    ic += '<text x="318" y="98" font-size="12.5" class="g-y">ışık</text>'
    ic += '<text x="20" y="150" font-size="13" font-weight="800" class="g-y">Ay ışık kaynağı değildir;</text>'
    ic += '<text x="20" y="168" font-size="13" font-weight="800" class="g-y">Güneş’ten gelen ışığı yansıtır.</text>'
    ic += '<text x="340" y="190" text-anchor="end" font-size="12" class="g-s">Ölçekli değildir.</text>'
    return svg(460, 198, ic, 'Güneş, Ay ve Dünya: Güneş’ten gelen ışık Ay’a ulaşır, Ay bu ışığı yansıtır ve yansıyan ışık Dünya’ya gelir. '
               'Ay ışık kaynağı değildir, Güneş’ten gelen ışığı yansıtır. Boyutlar ve uzaklıklar ölçekli değildir.')


def parcalanma():
    """Gündüz ile gece arasındaki büyük sıcaklık farkı yüzeyi parçalar: kaya, taş, kum, toz."""
    ic = '<defs>' + ok_isareti('okF4b', 'g-s') + '</defs>'
    ic += _kutu(8, 8, 150, 58, 'turuncu')
    ic += '<text x="83" y="30" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">Gündüz</text>'
    ic += '<text x="83" y="52" text-anchor="middle" font-size="14" font-weight="700" class="g-y">125 °C’ye kadar</text>'
    ic += _kutu(174, 8, 150, 58, 'mavi')
    ic += '<text x="249" y="30" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">Gece</text>'
    ic += '<text x="249" y="52" text-anchor="middle" font-size="14" font-weight="700" class="g-y">−174 °C’ye kadar</text>'
    ic += '<text x="342" y="32" font-size="12.5" class="g-y">çok büyük</text>'
    ic += '<text x="342" y="50" font-size="12.5" class="g-y">sıcaklık farkı</text>'
    ic += '<text x="240" y="98" text-anchor="middle" font-size="12.5" class="g-y">Bu fark yüzeyin parçalanmasını hızlandırır.</text>'
    for i, ad in enumerate(['Kaya', 'Taş', 'Kum', 'Toz']):
        x = 8 + i * 118
        ic += _kutu(x, 114, 92, 44, 'mor')
        ic += f'<text x="{x + 46}" y="142" text-anchor="middle" font-size="14" font-weight="800" class="g-of">{ad}</text>'
        if i < 3:
            ic += f'<line x1="{x + 96}" y1="136" x2="{x + 114}" y2="136" class="g-c" stroke-width="2" marker-end="url(#okF4b)"/>'
    ic += '<text x="8" y="186" font-size="13" font-weight="800" class="g-y">Yüzeyin büyük bölümü tozdur.</text>'
    return svg(480, 196, ic, 'Ay’da sıcaklık gündüz 125 °C’ye, gece eksi 174 °C’ye kadar ulaşır. Bu büyük sıcaklık farkı yüzeyin parçalanmasını '
               'hızlandırır: kayalar taşlara, taşlar kuma, kum toza dönüşür. Yüzeyin büyük bölümü tozdur.')


def donme_dolanma():
    """Ay, Dünya'nın etrafında saatin dönme yönünün tersine dolanırken Dünya'ya hep aynı yüzünü gösterir."""
    cx, cy, R, r = 230, 150, 100, 14
    ic = '<defs>' + ok_isareti('okF4c', 'g-mf') + '</defs>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="{R}" class="g-c" stroke-width="1.6" stroke-dasharray="6 6"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="34" class="g-mf"/>'
    ic += f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="14" font-weight="800" class="g-b">Dünya</text>'
    for aci in (0, 90, 180, 270):
        rad = math.radians(aci)
        mx, my = cx + R * math.cos(rad), cy - R * math.sin(rad)
        # Dünya'ya doğru birim vektör
        ux, uy = (cx - mx) / R, (cy - my) / R
        ic += f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{r}" class="g-s"/>'
        ic += f'<circle cx="{mx + ux * 8:.1f}" cy="{my + uy * 8:.1f}" r="3.6" class="g-yf"/>'
    a1, a2 = math.radians(22), math.radians(68)
    x1, y1 = cx + R * math.cos(a1), cy - R * math.sin(a1)
    x2, y2 = cx + R * math.cos(a2), cy - R * math.sin(a2)
    ic += f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 0 {x2:.1f} {y2:.1f}" class="g-ms" stroke-width="2.6" marker-end="url(#okF4c)"/>'
    ic += '<text x="344" y="62" font-size="12.5" font-weight="700" class="g-mf">dolanma yönü:</text>'
    ic += '<text x="344" y="79" font-size="12.5" class="g-y">saatin dönme</text>'
    ic += '<text x="344" y="95" font-size="12.5" class="g-y">yönünün tersi</text>'
    ic += f'<text x="{cx + R}" y="{cy + 34}" text-anchor="middle" font-size="13" font-weight="800" class="g-y">Ay</text>'
    ic += '<circle cx="20" cy="284" r="4.5" class="g-yf"/><text x="32" y="289" font-size="12.5" class="g-y">Ay’ın Dünya’ya bakan yüzü</text>'
    ic += '<text x="452" y="289" text-anchor="end" font-size="12" class="g-s">Ölçekli değildir.</text>'
    return svg(460, 300, ic, 'Ay’ın Dünya etrafındaki dolanması: Ay dört farklı konumda gösterilir ve her konumda Dünya’ya bakan yüzü yeşil noktayla işaretlidir; '
               'bu yüz her konumda aynıdır, bu yüzden Dünya’dan Ay’ın hep aynı yüzü görünür. Dolanma yönü saatin dönme yönünün tersidir. '
               'Boyutlar ve uzaklıklar ölçekli değildir.')


def uygula(o):
    g = {'Ay’ın ışığı': ay_isigi(),
         'Ay’ın yüzeyi ve sıcaklık': parcalanma(),
         'Dönme ve dolanma hareketleri': donme_dolanma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
