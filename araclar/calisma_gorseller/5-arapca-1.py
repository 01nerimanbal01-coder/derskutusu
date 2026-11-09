"""5-arapca-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 44" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sabah selamlaşması"><rect '
    'x="4" y="3" width="167" height="36" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="25.8" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Selam · صَبَاحُ '
    'الْخَيْرِ</text><rect x="179" y="3" width="167" height="36" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text '
    'x="262.5" y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#12a150">Karşılık · ؟</text></svg>',
 3: '<svg viewBox="0 0 350 48" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Eksik ad bilgisi"><rect '
    'x="4" y="3" width="342" height="43" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Tanışma '
    'defteri</text><text x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Yeni kız öğrencinin adı: ______</text></svg>',
 5: '<svg viewBox="0 0 350 82" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Harf kartları: A خ, B ح, '
    'C ج, D ث"><rect x="4" y="3" width="167" height="36" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" '
    'y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">A Kartı · '
    'خ</text><rect x="179" y="3" width="167" height="36" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" '
    'y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">B Kartı · '
    'ح</text><rect x="4" y="43" width="167" height="36" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="87.5" '
    'y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">C Kartı · '
    'ج</text><rect x="179" y="43" width="167" height="36" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" '
    'y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">D Kartı · '
    'ث</text></svg>',
 10: '<svg viewBox="0 0 350 82" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dört sınıf '
     'yönergesi"><rect x="4" y="3" width="167" height="36" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" '
     'y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">A Kartı · '
     'اِقْرَئِي</text><rect x="179" y="3" width="167" height="36" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text '
     'x="262.5" y="25.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">B '
     'Kartı · قُومِي</text><rect x="4" y="43" width="167" height="36" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text '
     'x="87.5" y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">C '
     'Kartı · اِجْلِسِي</text><rect x="179" y="43" width="167" height="36" rx="5" fill="#f0e9fe" stroke="#7c3aed" '
     'stroke-width="0.75"/><text x="262.5" y="65.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="700" fill="#7c3aed">D Kartı · اُكْتُبِي</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
