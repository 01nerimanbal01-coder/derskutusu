"""5-peygamberimizin-hayati-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 48" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ziyaretçilerin iki '
    'amacı"><rect x="4" y="3" width="342" height="43" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.1" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Mekke’ye '
    'gelenler</text><text x="11.0" y="38.5" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Kâbe’yi ziyaret eder; alışveriş yaparlardı.</text></svg>',
 3: '<svg viewBox="0 0 350 170" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Yapı, yer ve amaç '
    'fişi"><rect x="4" y="3" width="342" height="25" rx="5" fill="#dce9ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.3" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Ebrehe’nin '
    'yaptırdığı</text><rect x="4" y="31" width="342" height="25" rx="5" fill="#dce9ff" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="11.0" y="48.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Kilise</text><rect x="4" y="59" width="342" height="25" rx="5" fill="#f0f5fc" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="76.3" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#172849">Bulunduğu şehir</text><rect x="4" y="87" width="342" height="25" rx="5" fill="#f0f5fc" '
    'stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="104.3" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">?</text><rect x="4" y="115" width="342" height="25" rx="5" fill="#f0f5fc" '
    'stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="132.3" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">Yaptırma amacı</text><rect x="4" y="143" width="342" height="25" rx="5" '
    'fill="#f0f5fc" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="160.3" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#172849">?</text></svg>',
 7: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sorudan kaynağa"><rect '
    'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Araştırma '
    'sorusu</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Kur’an’da fil sahiplerinin planının boşa</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">çıkması nasıl anlatılır?</text></svg>',
 11: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Çelişen iki bilgi"><rect '
     'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
     'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Bilgi toplama '
     'dosyası</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#172849">Bir notta ordunun başarılı, diğerinde</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">başarısız olduğu yazıyor.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
