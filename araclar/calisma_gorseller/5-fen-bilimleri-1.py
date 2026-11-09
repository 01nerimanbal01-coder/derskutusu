"""5-fen-bilimleri-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 100" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Deney masasında dört '
    'eşya"><rect x="4" y="3" width="167" height="45" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.1" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">A Eşyası</text><text '
    'x="87.5" y="39.5" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Deney '
    'defteri</text><rect x="179" y="3" width="167" height="45" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" '
    'y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">B '
    'Eşyası</text><text x="262.5" y="39.5" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Meyve suyu kutusu</text><rect x="4" y="52" width="167" height="45" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="87.5" y="70.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#12a150">C Eşyası</text><text x="87.5" y="88.5" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">Deney yönergesi</text><rect x="179" y="52" width="167" height="45" rx="5" '
    'fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="70.1" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">D Eşyası</text><text x="262.5" y="88.5" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Koruyucu gözlük</text></svg>',
 9: '<svg viewBox="0 0 350 70" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="167" height="64" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Not 1</text><text '
    'x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Ellerim yıkandığı için</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">hâlâ ıslak.</text><rect x="179" y="3" width="167" height="64" rx="5" '
    'fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="262.5" y="30.6" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Not 2 · Cihazın fişini</text><text x="262.5" y="49.0" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">takmam '
    'gerekiyor.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
