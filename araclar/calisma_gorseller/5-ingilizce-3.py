"""5-ingilizce-3 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {2: '<svg viewBox="0 0 350 113" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Meslek nesneleri ve '
    'çalışma yeri kartı"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Tools '
    '(Kullanılan Araçlar)</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Stethoscope (Stetoskop) · Thermometer</text><text x="11.0" y="57.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">(Termometre)</text><rect x="4" y="68" '
    'width="342" height="43" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="11.0" y="85.1" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Workplace (Çalışma Yeri)</text><text x="11.0" '
    'y="103.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">HOSPITAL '
    '(Hastane)</text></svg>',
 5: '<svg viewBox="0 0 350 113" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Deniz temizliği '
    'afişi"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Poster Scene · '
    'Sea</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">A sea turtle swimming near plastic bags in</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">the sea</text><rect x="4" y="68" width="342" height="43" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" y="85.1" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">Poster Warning · Beach</text><text x="11.0" y="103.5" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Plastic bottles and rubbish on the sand '
    '(!)</text></svg>',
 10: '<svg viewBox="0 0 350 88" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ece’nin annesinin '
     'haftalık pazar takvimi"><rect x="4" y="3" width="167" height="82" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
     'x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Ece’s '
     'Mum · Weekly</text><text x="87.5" y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#2451d6">Schedule</text><text x="87.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="500" fill="#0b2257">Activity: Going to</text><text x="87.5" y="76.4" text-anchor="middle" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">the market</text><rect x="179" y="3" '
     'width="167" height="82" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="262.5" y="21.2" text-anchor="middle" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Mon: – · Tue: – ·</text><text x="262.5" '
     'y="39.6" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Wed: – · Thu: '
     '–</text><text x="262.5" y="58.0" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#0b2257">Fri: – · Sat: – · Sun: ✓</text><text x="262.5" y="76.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="500" fill="#0b2257">(Market)</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
