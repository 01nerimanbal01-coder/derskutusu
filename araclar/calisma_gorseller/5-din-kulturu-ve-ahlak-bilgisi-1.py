"""5-din-kulturu-ve-ahlak-bilgisi-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {3: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Yeryüzünde yağmur '
    'yağması ve susayan insanın su içmesi"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">1. Durum · Yeryüzünde Su Döngüsü</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Yağmur bulutundan kurumuş toprağa ve</text><text x="11.0" '
    'y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">filize yağmur '
    'yağması</text><rect x="4" y="68" width="342" height="62" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="11.0" '
    'y="85.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">2. Durum · İnsan '
    'Vücudunda Su İhtiyacı</text><text x="11.0" y="103.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Susayan bir kişinin su şişesinden bardağa su</text><text x="11.0" y="122.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">doldurup içmesi</text></svg>',
 5: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Aynı çiçeğin insana ve '
    'arıya görünümü"><rect x="4" y="3" width="342" height="62" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">İnsanın Gördüğü '
    'Çiçek</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Yalnızca sarı taç yapraklar ve turuncu orta</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">kısım görünür.</text><rect x="4" y="68" width="342" height="62" '
    'rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="11.0" y="85.4" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Arının Gördüğü Çiçek</text><text x="11.0" y="103.8" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Yapraklarda insan gözünün '
    'göremediği mor</text><text x="11.0" y="122.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">balözü izleri görünür.</text></svg>',
 7: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tohumun meyve veren '
    'ağaca dönüşüm aşamaları"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. '
    'Tohum → 2. Fidan</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Toprağa ekilen tohum su ve minerallerle</text><text x="11.0" y="57.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">filizlenip fidana dönüşür.</text><rect x="4" '
    'y="68" width="342" height="62" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="11.0" y="85.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">3. Ağaç → 4. Meyve Veren '
    'Ağaç</text><text x="11.0" y="103.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Toprakta kök salıp büyüyen ağaç</text><text x="11.0" y="122.2" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">olgunlaşarak meyve verir.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
