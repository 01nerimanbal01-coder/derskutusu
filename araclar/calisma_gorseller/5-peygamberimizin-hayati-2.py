"""5-peygamberimizin-hayati-2 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 70" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Soru ve cevabın '
    'uyumu"><rect x="4" y="3" width="167" height="64" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Araştırma sorusu '
    '·</text><text x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">Ebrehe neden kilise</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#234a96">yaptırdı?</text><rect x="179" y="3" width="167" height="64" rx="5" fill="#ecf8f0" '
    'stroke="#2451d6" stroke-width="0.75"/><text x="262.5" y="21.4" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#234a96">Yazılan cevap ·</text><text x="262.5" y="39.8" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Ordusu Kâbe’yi</text><text x="262.5" y="58.2" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">yıkmayı '
    'başaramadı.</text></svg>',
 4: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Araştırmayı '
    'sınırlandırma"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Araştırma '
    'başlığı</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Abdülmuttalib’in Ebrehe’yle görüşmesindeki</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">tutumu</text></svg>',
 7: '<svg viewBox="0 0 350 48" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="İncelenecek kaynak '
    'kartı"><rect x="4" y="3" width="342" height="43" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">İncelenecek '
    'Kaynak</text><text x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Fil suresinin güvenilir meali (anlamı)</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
