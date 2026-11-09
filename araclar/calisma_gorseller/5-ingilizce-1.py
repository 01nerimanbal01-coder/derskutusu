"""5-ingilizce-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 80" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Çalışma yolu '
    'şeması"><rect x="4" y="3" width="342" height="23" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="19.0" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257"><tspan font-weight="700" '
    'fill="#2451d6">1. Adım:</tspan> Listening</text><rect x="4" y="29" width="342" height="23" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="11.0" y="45.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257"><tspan font-weight="700" fill="#12a150">2. Adım:</tspan> Reading</text><rect x="4" y="55" '
    'width="342" height="23" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" y="71.0" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257"><tspan font-weight="700" fill="#d97706">3. '
    'Adım:</tspan> Writing</text></svg>',
 7: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Kendi '
    'kontrolüm</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Neleri öğrendim? Hangi çalışmayı yeniden</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">yapmalıyım?</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
