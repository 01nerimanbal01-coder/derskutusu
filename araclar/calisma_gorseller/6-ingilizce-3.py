"""6-ingilizce-3 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 104" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Menü: Vegetable soup 40 '
    'TL, Tuna sandwich 60 TL, Green salad 35 TL, Lemonade 25 TL, Chocolate cake 45 TL, Ice cream 30 TL"><rect x="4" y="3" width="342" '
    'height="99" rx="5" fill="#fffdf7" stroke="#8a5a2b" stroke-width="0.75"/><text x="11.0" y="20.5" text-anchor="start" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#8a5a2b">MENU</text><text x="11.0" y="38.9" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Vegetable soup 40 TL Lemonade 25 '
    'TL</text><text x="11.0" y="57.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Tuna sandwich 60 TL Chocolate cake</text><text x="11.0" y="75.7" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#d63a3a">45 TL</text><text x="11.0" y="94.1" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Green salad 35 TL Ice cream 30 '
    'TL</text></svg>',
 9: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadde üzerindeki '
    'yapıların konum haritası."><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">North Side of Main ·</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Street (Yan Yana)</text><text x="87.5" y="58.0" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">[ Café ] — [ Museum</text><text x="87.5" '
    'y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">· ] — [ Cinema '
    ']</text><rect x="179" y="3" width="167" height="82" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="262.5" '
    'y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">South Side of '
    'Main ·</text><text x="262.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#12a150">Street (Karşı Sıra)</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">[ Park ] — [ Bank ] —</text><text x="262.5" y="76.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">· [ School ]</text></svg>',
 14: '<svg viewBox="0 0 350 70" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hava tahmini: Antalya 34 '
     'derece güneşli, Nevşehir 22 derece bulutlu"><rect x="4" y="3" width="167" height="64" rx="5" fill="#fff1df" stroke="#ee7d12" '
     'stroke-width="0.75"/><text x="87.5" y="21.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#0b2257">Weather forecast · ·</text><text x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Saturday · Antalya</text><text x="87.5" y="58.2" '
     'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">34 °C · '
     'sunny</text><rect x="179" y="3" width="167" height="64" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="262.5" '
     'y="30.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
     'fill="#2451d6">Nevşehir</text><text x="262.5" y="49.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="500" fill="#0b2257">22 °C · cloudy</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
