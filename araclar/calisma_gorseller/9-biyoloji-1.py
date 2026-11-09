"""9-biyoloji-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {2: '<svg viewBox="0 0 350 104" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Laboratuvar notu: Çok az '
    'miktarda DNA var, aynı DNA dizisinden çok sayıda kopya gerekiyor"><rect x="4" y="3" width="342" height="99" rx="5" fill="#fffdf5" '
    'stroke="#8a5a2b" stroke-width="0.75"/><text x="11.0" y="20.5" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#8a5a2b">Laboratuvar Notu</text><text x="11.0" y="38.9" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">• Örnek: Çok az miktarda DNA var.</text><text '
    'x="11.0" y="57.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">• '
    'Sorun: Bu miktar inceleme için yetmiyor.</text><text x="11.0" y="75.7" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">• Gereken: Aynı DNA dizisinden çok sayıda</text><text x="11.0" y="94.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">kopya</text></svg>',
 5: '<svg viewBox="0 0 350 113" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kart 1: Doğal bir olayın '
    'nasıl gerçekleştiğini açıklar. Kart 2: Doğal bir olayın neden gerçekleştiğini açıklar."><rect x="4" y="3" width="342" height="43" '
    'rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. Kart</text><text x="11.0" y="38.5" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Doğal bir olayın NASIL gerçekleştiğini '
    'açıklar.</text><rect x="4" y="49" width="342" height="62" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="11.0" '
    'y="66.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">2. '
    'Kart</text><text x="11.0" y="84.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Doğal bir olayın NEDEN gerçekleştiğini</text><text x="11.0" y="103.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">açıklar.</text></svg>',
 9: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Haber sitesi başlığı: '
    'Yeni bir çalışma kanıtladı: Bu besin bütün hastalıkları önlüyor!"><rect x="4" y="3" width="342" height="62" rx="5" fill="#f4f7fe" '
    'stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d63a3a">Haber Sitesi — SAĞLIK</text><text x="11.0" y="38.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">“Yeni bir çalışma kanıtladı: Bu besin '
    'bütün</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">hastalıkları önlüyor!”</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
