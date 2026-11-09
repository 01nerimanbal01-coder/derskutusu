"""6-fen-bilimleri-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {3: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gezegen kimlik kartı: '
    'yapısı gazsal, Güneş’e yakınlık sırası 7, uydusu var, halkası var."><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" '
    'stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#2451d6">GEZEGEN KİMLİK KARTI</text><text x="11.0" y="38.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Yapısı: Gazsal · Güneş’e yakınlık sırası: '
    '7.</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Uydusu: Var · Halkası: Var</text></svg>',
 6: '<svg viewBox="0 0 350 156" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Uydusu ve halkası olma '
    'durumuna göre gezegen gruplama şeması."><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">K Bölgesi</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">Yalnız uydusu olan ·</text><text x="87.5" y="58.0" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">(halkası olmayan)</text><text x="87.5" '
    'y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">gezegenler</text><rect x="179" y="3" width="167" height="82" rx="5" fill="#fff1df" stroke="#d97706" '
    'stroke-width="0.75"/><text x="262.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#d97706">L Bölgesi (Kesişim)</text><text x="262.5" y="39.6" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Hem uydusu hem</text><text x="262.5" y="58.0" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">halkası olan</text><text x="262.5" y="76.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">gezegenler</text><rect '
    'x="4" y="89" width="167" height="64" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="87.5" y="107.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">M Bölgesi</text><text '
    'x="87.5" y="125.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Yalnız halkası olan</text><text x="87.5" y="144.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">gezegenler</text><rect x="179" y="89" width="167" height="64" rx="5" '
    'fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="107.4" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">N Bölgesi (Dış Alan)</text><text x="262.5" y="125.8" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Uydusu ve '
    'halkası</text><text x="262.5" y="144.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">olmayan gezegenler</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
