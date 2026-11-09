"""6-ingilizce-2 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 100" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bell schedule: Lesson 1 '
    '08:40, Break 09:20, Lesson 2 09:30, Lunch 12:00."><rect x="4" y="3" width="167" height="45" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="87.5" y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Lesson 1</text><text x="87.5" y="39.5" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">Starts at 08:40</text><rect x="179" y="3" width="167" height="45" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" y="21.1" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Break</text><text x="262.5" y="39.5" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Starts at 09:20</text><rect x="4" y="52" '
    'width="167" height="45" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="87.5" y="70.1" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Lesson 2</text><text x="87.5" y="88.5" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Starts at '
    '09:30</text><rect x="179" y="52" width="167" height="45" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" '
    'y="70.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#7c3aed">Lunch</text><text x="262.5" y="88.5" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Starts at 12:00</text></svg>',
 9: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Duyuru: Music club, every '
    'Friday, 4:00 p.m., music room, bring your instrument"><rect x="4" y="3" width="342" height="62" rx="5" fill="#f4f7fe" '
    'stroke="#7c3aed" stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#0b2257">MUSIC CLUB every Friday</text><text x="11.0" y="38.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">4:00 p.m. · music room</text><text x="11.0" '
    'y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Bring your '
    'instrument!</text></svg>',
 13: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gezi kaydı: bu yıl beş '
     'okul gezisi, Deniz hepsine katıldı."><rect x="4" y="3" width="342" height="62" rx="5" fill="#e3f6ea" stroke="#12a150" '
     'stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#12a150">School Trips This Year · Deniz</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto '
     'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Trip 1: Joined · Trip 2: Joined · Trip 3:</text><text x="11.0" '
     'y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Joined · Trip '
     '4: Joined · Trip 5: Joined</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
