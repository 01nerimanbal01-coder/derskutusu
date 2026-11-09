"""5-matematik-2 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="P noktasından d '
    'doğrusuna çizilen dikme ve eğik parçalar"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Dik Bağlantı (90°)</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">P noktasından d doğrusuna inen dikme: [PH]</text><text x="11.0" '
    'y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">(H’de ∟ diklik '
    'işareti)</text><rect x="4" y="68" width="342" height="62" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" '
    'y="85.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Eğik '
    'Bağlantılar</text><text x="11.0" y="103.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">P noktasından d doğrusuna çizilen eğik</text><text x="11.0" y="122.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">parçalar: [PK] ve [PL]</text></svg>',
 9: '<svg viewBox="0 0 350 70" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="167" height="64" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">I · Merkez</text><text '
    'x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">değiştirildi; pergel</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#234a96">açıklığı korundu.</text><rect x="179" y="3" width="167" height="64" rx="5" '
    'fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="262.5" y="21.4" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">II · Merkez korundu;</text><text x="262.5" y="39.8" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">pergel '
    'açıklığı</text><text x="262.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">büyütüldü.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
