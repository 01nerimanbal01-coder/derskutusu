"""5-sosyal-bilgiler-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {6: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kerem’in 4. ve 5. '
    'sınıftaki grupları ve rolleri"><rect x="4" y="3" width="342" height="62" rx="5" fill="#e8eefe" stroke="#2451d6" '
    'stroke-width="0.75"/><text x="11.0" y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">Kerem · 4. Sınıfta</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">• 4-A sınıfı: Öğrenci</text><text x="11.0" y="57.2" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">• Mahalle futbol takımı: '
    'Oyuncu</text><rect x="4" y="68" width="342" height="62" rx="5" fill="#e3f6ea" stroke="#12a150" stroke-width="0.75"/><text x="11.0" '
    'y="85.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#12a150">Kerem · 5. '
    'Sınıfta</text><text x="11.0" y="103.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">• 5-B sınıfı: Öğrenci ve sınıf nöbetçisi</text><text x="11.0" y="122.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">• Satranç kulübü: Üye</text></svg>',
 7: '<svg viewBox="0 0 350 175" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dört farklı topluluk '
    'kartı"><rect x="4" y="3" width="167" height="101" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="87.5" y="21.5" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">K Topluluğu</text><text '
    'x="87.5" y="39.9" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Aynı '
    'otobüste</text><text x="87.5" y="58.3" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">yolculuk eden,</text><text x="87.5" y="76.7" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">birbirini tanımayan</text><text x="87.5" y="95.1" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">yolcular</text><rect x="179" y="3" '
    'width="167" height="101" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="262.5" y="39.9" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">L Topluluğu</text><text x="262.5" y="58.3" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Okulun '
    'satranç</text><text x="262.5" y="76.7" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">kulübü üyeleri</text><rect x="4" y="108" width="167" height="64" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="87.5" y="126.4" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#12a150">M Topluluğu</text><text x="87.5" y="144.8" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">Mahalledeki fidan</text><text x="87.5" y="163.2" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">dikme gönüllüleri</text><rect x="179" y="108" '
    'width="167" height="64" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="126.4" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">N Topluluğu</text><text x="262.5" y="144.8" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Bir voleybol</text><text '
    'x="262.5" y="163.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">takımının oyuncuları</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
