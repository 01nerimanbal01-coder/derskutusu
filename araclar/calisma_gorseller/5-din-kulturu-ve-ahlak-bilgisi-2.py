"""5-din-kulturu-ve-ahlak-bilgisi-2 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 113" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="342" height="43" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Birinci not</text><text '
    'x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Gece ve '
    'gündüz birbirini izliyor.</text><rect x="4" y="49" width="342" height="62" rx="5" fill="#ecf8f0" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="66.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#234a96">İkinci not</text><text x="11.0" y="84.8" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">İslam inancında bu düzen, Allah’ın</text><text x="11.0" y="103.2" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">yaratmasıyla '
    'ilişkilidir.</text></svg>',
 9: '<svg viewBox="0 0 350 70" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="167" height="64" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">K</text><text x="87.5" '
    'y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Allah’ın eşi ve '
    'ortağı</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">yoktur.</text><rect x="179" y="3" width="167" height="64" rx="5" fill="#ecf8f0" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="262.5" y="21.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#234a96">L · Başka varlıklar ·</text><text x="262.5" y="39.8" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Allah’a denk kabul</text><text x="262.5" y="58.2" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">edilir.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
