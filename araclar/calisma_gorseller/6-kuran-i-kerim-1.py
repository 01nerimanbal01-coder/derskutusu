"""6-kuran-i-kerim-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Okuma hedefi</text><text '
    'x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Bir '
    'bölümdeki dört hizbin hepsini baştan</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">sona okumak.</text></svg>',
 9: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="167" height="82" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.2" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Sayfa kenarı · '
    'Cüz</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">başında hizip</text><text x="87.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#234a96">numarası yok; sonra</text><text x="87.5" y="76.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">2, 3 ve 4 görülüyor.</text><rect x="179" '
    'y="3" width="167" height="82" rx="5" fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="262.5" y="30.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Çıkarım · Bu '
    'cüzde</text><text x="262.5" y="48.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">yalnız üç hizip</text><text x="262.5" y="67.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#234a96">olmalı.</text></svg>',
 11: '<svg viewBox="0 0 350 82" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sayfa kenarındaki iki '
     'numara"><rect x="4" y="3" width="167" height="36" rx="5" fill="#dce9ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" '
     'y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Cüz '
     'işareti</text><rect x="179" y="3" width="167" height="36" rx="5" fill="#dce9ff" stroke="#2451d6" stroke-width="0.75"/><text '
     'x="262.5" y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#172849">Hizip işareti</text><rect x="4" y="43" width="167" height="36" rx="5" fill="#f0f5fc" stroke="#2451d6" '
     'stroke-width="0.75"/><text x="87.5" y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="500" fill="#172849">12</text><rect x="179" y="43" width="167" height="36" rx="5" fill="#f0f5fc" stroke="#2451d6" '
     'stroke-width="0.75"/><text x="262.5" y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="500" fill="#172849">3</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
