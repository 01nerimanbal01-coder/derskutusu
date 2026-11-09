"""9-din-kulturu-ve-ahlak-bilgisi-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {1: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ayet kartı: Biz gökleri, '
    'yeri ve bunlar arasındakileri oyun olsun diye yaratmadık. (Enbiyâ, 16)"><rect x="4" y="3" width="342" height="62" rx="5" '
    'fill="#fbf7ee" stroke="#c9a86a" stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#8a5a2b">Ayet-i Kerime Meali</text><text x="11.0" y="38.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">“Biz gökleri, yeri ve bunlar '
    'arasındakileri</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#0b2257">oyun olsun diye yaratmadık.” (Enbiyâ, 16)</text></svg>',
 8: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Emaneti yüklenmekten '
    'çekinen varlıklar: gökler, yer, dağlar"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Ahzâb Suresi 72. Ayette Emanetten Çekinen</text><text x="11.0" y="38.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">Varlıklar</text><text x="11.0" y="57.2" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">1. Gökler · 2. Yer · 3. '
    'Dağlar</text></svg>',
 12: '<svg viewBox="0 0 350 178" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Apartman panosu '
     'notları"><rect x="4" y="3" width="342" height="62" rx="5" fill="#fff7c2" stroke="#d97706" stroke-width="0.75"/><text x="11.0" '
     'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#8a5a2b">Apartman Panosu '
     '— 1. Not</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#0b2257">Kuzenimiz Elif evleniyor. Düğüne hepimiz</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">davetliyiz.</text><rect x="4" y="68" width="342" height="43" rx="5" '
     'fill="#dff3e6" stroke="#12a150" stroke-width="0.75"/><text x="11.0" y="85.1" text-anchor="start" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="700" fill="#12a150">Apartman Panosu — 2. Not</text><text x="11.0" y="103.5" text-anchor="start" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Nuri Amca hasta. Alışverişini sırayla '
     'yapalım.</text><rect x="4" y="114" width="342" height="62" rx="5" fill="#e3ecff" stroke="#2451d6" stroke-width="0.75"/><text '
     'x="11.0" y="131.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
     'fill="#2451d6">Apartman Panosu — 3. Not</text><text x="11.0" y="149.8" text-anchor="start" font-family="Noto Sans, sans-serif" '
     'font-size="1.01em" font-weight="500" fill="#0b2257">Bayramda bütün komşularla bahçede</text><text x="11.0" y="168.2" '
     'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">buluşalım.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
