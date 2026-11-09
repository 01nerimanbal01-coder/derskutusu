"""5-matematik-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A noktasından başlayıp B '
    'noktasından geçerek uzanan ışın"><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Başlangıç Ucu</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">A noktası kapalı</text><text x="87.5" y="58.0" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">uçtur (başlangıç</text><text x="87.5" '
    'y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">noktası '
    'sabittir).</text><rect x="179" y="3" width="167" height="82" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text '
    'x="262.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#12a150">Uzanış Yönü</text><text x="262.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Çizgi B noktasından</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">geçerek B yönünde</text><text x="262.5" y="76.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">ok ile sınırsız uzanır.</text></svg>',
 5: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Köşesi B, kolları BA ve '
    'BC ışınları olan açı"><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Açının '
    'Köşesi</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">İki ışının ortak</text><text x="87.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">başlangıç noktası: B</text><text x="87.5" y="76.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">noktası</text><rect x="179" y="3" width="167" '
    'height="82" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="262.5" y="30.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Açının Kolları</text><text x="262.5" y="48.8" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">1. kol: [BA ışını · '
    '2.</text><text x="262.5" y="67.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">kol: [BC ışını</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
