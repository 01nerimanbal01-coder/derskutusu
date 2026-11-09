"""8-matematik-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {3: '<svg viewBox="0 0 350 95" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="İçine giren 2, 3, 3 ve 7 '
    'asal sayılarını çarpan sayı makinesi."><rect x="4" y="3" width="342" height="25" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Makineye Giren Asal Sayılar · 2 · 3 · 3 · 7</text><rect x="4" y="31" width="342" height="62" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" y="48.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">Makinenin Kuralı ve Çıkan Sayı</text><text x="11.0" y="66.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Giren asal sayıların tamamını çarpar → '
    'Çıkan</text><text x="11.0" y="85.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Sayı: ?</text></svg>',
 10: '<svg viewBox="0 0 350 82" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dört öğrencinin 48 '
     'sayısını üslü ifadelerin çarpımı biçiminde yazılışı."><rect x="4" y="3" width="167" height="36" rx="5" fill="#e8eefe" '
     'stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="700" fill="#2451d6">Ali · 48\xa0=\xa02⁴ · 3</text><rect x="179" y="3" width="167" height="36" rx="5" '
     'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" y="25.8" text-anchor="middle" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Can · 48\xa0=\xa02³ · 6</text><rect x="4" y="43" width="167" '
     'height="36" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="87.5" y="65.8" text-anchor="middle" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Efe · 48\xa0=\xa04² · 3</text><rect x="179" '
     'y="43" width="167" height="36" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="65.8" '
     'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Naz · 48\xa0=\xa02 · '
     '24</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
