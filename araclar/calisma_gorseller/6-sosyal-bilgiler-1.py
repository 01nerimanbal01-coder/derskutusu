"""6-sosyal-bilgiler-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {2: '<svg viewBox="0 0 350 159" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Üç kuşaklı aile '
    'akrabalık şeması."><rect x="4" y="3" width="342" height="43" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="11.0" y="20.1" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. '
    'Kuşak (Eşler)</text><text x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Ahmet (Erkek) ve Leyla (Kadın)</text><rect x="4" y="49" width="342" height="43" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="11.0" y="66.1" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">2. Kuşak (Ahmet ile Leyla’nın Çocukları)</text><text x="11.0" y="84.5" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Selma (Kadın) ve Gül '
    '(Kadın)</text><rect x="4" y="95" width="342" height="62" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="11.0" '
    'y="112.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">3. Kuşak '
    '(Torunlar)</text><text x="11.0" y="130.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">Selma’nın çocuğu: Ada (Kadın) · Gül’ün</text><text x="11.0" y="149.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">çocuğu: Can (Erkek)</text></svg>',
 5: '<svg viewBox="0 0 350 86" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Üç değer rozeti: '
    'Paylaşma, Birlikte yaşama ve Dayanışma."><rect x="4" y="3" width="342" height="25" rx="5" fill="#fff1df" stroke="#d97706" '
    'stroke-width="0.75"/><text x="11.0" y="20.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">1. Değer: Paylaşma</text><rect x="4" y="31" width="342" height="25" rx="5" fill="#e3f6ea" '
    'stroke="#12a150" stroke-width="0.75"/><text x="11.0" y="48.3" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">2. Değer: Birlikte yaşama</text><rect x="4" y="59" width="342" height="25" rx="5" '
    'fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="76.3" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">3. Değer: Dayanışma</text></svg>',
 9: '<svg viewBox="0 0 350 110" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Yuvarlak masa '
    'toplantısı. Pano: Konu: Okul kütüphanesini geliştirelim. Masada rol kartları: Araştırmacı, Lider, Proje koordinatörü."><rect x="4" '
    'y="3" width="167" height="64" rx="5" fill="#f4f7fe" stroke="#7c3aed" stroke-width="0.75"/><text x="87.5" y="21.4" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">Konu:</text><text '
    'x="87.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Okul '
    'kütüphanesini</text><text x="87.5" y="58.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">geliştirelim</text><rect x="179" y="3" width="167" height="64" rx="5" fill="#f4f7fe" '
    'stroke="#ee7d12" stroke-width="0.75"/><text x="262.5" y="39.8" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#0b2257">Araştırmacı</text><rect x="4" y="71" width="167" height="36" rx="5" '
    'fill="#f4f7fe" stroke="#ee7d12" stroke-width="0.75"/><text x="87.5" y="93.8" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#0b2257">Lider</text><rect x="179" y="71" width="167" height="36" rx="5" fill="#f4f7fe" '
    'stroke="#ee7d12" stroke-width="0.75"/><text x="262.5" y="93.8" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#0b2257">Proje koordinatörü</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
