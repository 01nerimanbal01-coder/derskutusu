"""5-turkce-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 93" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bahçedeki Hazine kitap '
    'kapağı"><rect x="4" y="3" width="342" height="23" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="19.0" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257"><tspan font-weight="700" '
    'fill="#2451d6">Kitap Kapağı Başlığı:</tspan> Bahçedeki Hazine</text><rect x="4" y="29" width="342" height="62" rx="5" fill="#fff1df" '
    'stroke="#d97706" stroke-width="0.75"/><text x="11.0" y="46.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">Kapaktaki Resim Ögeleri</text><text x="11.0" y="64.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Büyük bir ağaç, üzerinde kesik çizgili yol '
    've</text><text x="11.0" y="83.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">(X) işareti olan harita, sandık ve kürek</text></svg>',
 7: '<svg viewBox="0 0 350 140" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Metin, Dedemin Topacı: '
    'Dedem, çocukken arkadaşlarıyla en çok topaç çevirdiğini anlatır. Topacını tahtadan kendisi oymuş. İpini topaca sarar, bir hamlede '
    'yere fırlatırmış. Topaç ne kadar uzun dönerse o kadar sevinirmiş. Dedem eski topacını hâlâ saklıyor."><rect x="4" y="3" width="342" '
    'height="135" rx="5" fill="#fffdf5" stroke="#9aa6bd" stroke-width="0.75"/><text x="11.0" y="20.1" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Dedemin Topacı</text><text x="11.0" y="38.5" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Dedem, çocukken '
    'arkadaşlarıyla en çok topaç</text><text x="11.0" y="56.9" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">çevirdiğini anlatır. Topacını tahtadan kendisi</text><text x="11.0" y="75.3" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">oymuş. İpini topaca sarar, bir hamlede '
    'yere</text><text x="11.0" y="93.7" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">fırlatırmış. Topaç ne kadar uzun dönerse o</text><text x="11.0" y="112.1" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">kadar sevinirmiş. Dedem eski topacını hâlâ</text><text x="11.0" '
    'y="130.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">saklıyor.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
