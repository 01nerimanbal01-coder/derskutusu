"""9-matematik-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="İşaret kartları: P = '
    '(-3)^4 ve R = -3^4"><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="87.5" y="30.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">P '
    'Kartı: (−3)⁴</text><text x="87.5" y="48.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Parantez içi negatif</text><text x="87.5" y="67.2" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">tabanın çift kuvveti</text><rect x="179" y="3" width="167" '
    'height="82" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="262.5" y="21.2" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">R Kartı: −3⁴</text><text x="262.5" y="39.6" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Parantezsiz '
    'üslü</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">ifadenin negatif</text><text x="262.5" y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">işareti</text></svg>',
 3: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="İki işlem yolu"><rect '
    'x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="30.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">I. İşlem Yolu: '
    '(2³)³</text><text x="87.5" y="48.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Üssün üssü kuralı</text><text x="87.5" y="67.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">uygulanır.</text><rect x="179" y="3" width="167" height="82" rx="5" '
    'fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="262.5" y="21.2" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">II. İşlem Yolu: 2⁴ · 2⁵</text><text x="262.5" y="39.6" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Tabanları aynı '
    'olan</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">üslü ifadelerin</text><text x="262.5" y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">çarpımı</text></svg>',
 14: '<svg viewBox="0 0 350 51" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Depolama şeması"><rect '
     'x="4" y="3" width="167" height="45" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.1" '
     'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Depodaki '
     'Kutu</text><text x="87.5" y="39.5" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
     'fill="#2451d6">Sayısı: 2³</text><rect x="179" y="3" width="167" height="45" rx="5" fill="#e3f6ea" stroke="#12a150" '
     'stroke-width="0.75"/><text x="262.5" y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#12a150">Her Kutudaki Kart</text><text x="262.5" y="39.5" text-anchor="middle" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Sayısı: 2⁴</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
