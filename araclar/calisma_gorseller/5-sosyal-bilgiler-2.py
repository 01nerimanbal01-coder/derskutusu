"""5-sosyal-bilgiler-2 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 48" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="342" height="43" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Tanıtım</text><text '
    'x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Bu '
    'kıyafeti bazı özel günlerde giyiyoruz.</text></svg>',
 8: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgi kartları"><rect '
    'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Ziyaretçi</text><text '
    'x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Bu '
    'yemeği denemek istemiyorum. Nasıl</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">yapıldığını anlattığınız için teşekkür ederim.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
