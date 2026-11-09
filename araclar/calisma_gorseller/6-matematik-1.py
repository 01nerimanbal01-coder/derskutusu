"""6-matematik-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {3: '<svg viewBox="0 0 350 85" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="0’dan başlayıp altışar '
    'birim ilerleyen eşit atlamalar."><rect x="4" y="3" width="342" height="80" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Sayı Doğrusunda 0’dan Başlayan Eşit ·</text><text x="11.0" y="38.6" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Atlamalar</text><text x="11.0" y="57.0" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Başlangıç: 0 → 1. atlama: '
    '6 → 2. atlama: 12 → 3.</text><text x="11.0" y="75.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">atlama: ... → 5. atlama: ?</text></svg>',
 7: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sekiz çarpan kartı: 1, 2, '
    '3, 4, ?, 8, 12, 24."><rect x="4" y="3" width="342" height="62" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text '
    'x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Bir '
    'Doğal Sayının Küçükten Büyüğe Bütün</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">Çarpanları</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">1 · 2 · 3 · 4 · [ ? ] · 8 · 12 · 24</text></svg>',
 10: '<svg viewBox="0 0 350 85" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="1’den 30’a kadar '
     'numaralı raflarda 4 ve 6’nın katı olan etiketler."><rect x="4" y="3" width="342" height="80" rx="5" fill="#e8eefe" stroke="#2451d6" '
     'stroke-width="0.75"/><text x="11.0" y="20.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#2451d6">Kütüphane Rafları (1’den 30’a Kadar ·</text><text x="11.0" y="38.6" text-anchor="start" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Numaralı)</text><text x="11.0" y="57.0" '
     'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Kırmızı etiket: 4, 8, '
     '... (her 4. raf) · Mavi etiket:</text><text x="11.0" y="75.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="500" fill="#0b2257">6, 12, ... (her 6. raf)</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
