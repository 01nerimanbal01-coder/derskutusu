"""5-ingilizce-4 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {3: '<svg viewBox="0 0 350 138" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Okul kat planı"><rect '
    'x="4" y="3" width="167" height="64" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Library</text><text '
    'x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Bookshelves and</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">reading desks</text><rect x="179" y="3" width="167" height="64" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" y="21.4" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Canteen</text><text x="262.5" y="39.8" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Food trays and</text><text x="262.5" y="58.2" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">lunch tables</text><rect '
    'x="4" y="71" width="167" height="64" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="87.5" y="89.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Sports field</text><text '
    'x="87.5" y="107.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">The '
    'coach (with</text><text x="87.5" y="126.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">whistle and ball)</text><rect x="179" y="71" width="167" height="64" rx="5" fill="#f0e9fe" '
    'stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="89.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#7c3aed">Science lab</text><text x="262.5" y="107.8" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Microscope and test</text><text x="262.5" '
    'y="126.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">tubes</text></svg>',
 5: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Okul kulübü konuşma '
    'kartı"><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.2" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Ela:</text><text '
    'x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">What '
    'is your</text><text x="87.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">favourite school</text><text x="87.5" y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">club?</text><rect x="179" y="3" width="167" height="82" rx="5" fill="#e3f6ea" '
    'stroke="#12a150" stroke-width="0.75"/><text x="262.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#12a150">Can:</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">— ? —</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
