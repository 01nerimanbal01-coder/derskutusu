"""6-fen-bilimleri-14 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 44" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Düzlem aynada gelen ışın, '
    'normal ve yansıyan ışın modeli"><rect x="4" y="3" width="342" height="25" rx="5" fill="#eef1f6" stroke="#9aa6bd" '
    'stroke-width="0.75"/><text x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#2451d6">N (Normal) · Gelen Işın · Yansıyan Işın i r</text></svg>',
 1: '<svg viewBox="0 0 350 44" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ayna ile 25 derece açı '
    'yapan K ışını düzeneği"><rect x="4" y="3" width="342" height="25" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">N · K '
    'Işını r = ? · 25°</text></svg>',
 2: '<svg viewBox="0 0 350 52" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Düzgün ve dağınık yansıma '
    'ışın diyagramı"><rect x="4" y="3" width="167" height="46" rx="5" fill="#e0f4f8" stroke="#0e8fa8" stroke-width="0.75"/><text x="87.5" '
    'y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0e8fa8">Düzgün '
    'Yansıma</text><text x="87.5" y="39.9" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#0e8fa8">(Ayna)</text><rect x="179" y="3" width="167" height="46" rx="5" fill="#fff1df" stroke="#d97706" '
    'stroke-width="0.75"/><text x="262.5" y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#d97706">Dağınık Yansıma</text><text x="262.5" y="39.9" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">(Pürüzlü)</text></svg>',
 5: '<svg viewBox="0 0 350 44" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gelen ve yansıyan ışın '
    'arası 110 derece olan düzenek"><rect x="4" y="3" width="342" height="25" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#7c3aed">Toplam = 110° α = ?</text></svg>',
 6: '<svg viewBox="0 0 350 49" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Düzlem aynaya dik '
    'gönderilen lazer ışını"><rect x="4" y="3" width="342" height="44" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text '
    'x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">LAZER · '
    'Yüzeye Dik (90°)</text><text x="11.0" y="37.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#475569">Normal (N) Üzerinden</text></svg>',
 7: '<svg viewBox="0 0 350 68" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dağınık yansımada farklı '
    'eğimli yüzey normalleri"><rect x="4" y="3" width="342" height="63" rx="5" fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text '
    'x="11.0" y="19.0" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#d97706">Pürüzlü '
    'Yüzeyin Yakın Görünümü (Her</text><text x="11.0" y="37.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#d97706">Noktada i = r)</text><text x="11.0" y="56.6" text-anchor="start" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#2451d6">N(a) · N(b)</text></svg>',
 8: '<svg viewBox="0 0 350 102" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dört farklı açıyla gelen '
    'K, L, M, P ışın kartları"><rect x="4" y="3" width="167" height="46" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text '
    'x="87.5" y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">K '
    'Işını</text><text x="87.5" y="39.9" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#0b2257">Yüzeye dik (90°)</text><rect x="179" y="3" width="167" height="46" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="262.5" y="21.1" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#12a150">L Işını</text><text x="262.5" y="39.9" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="500" fill="#0b2257">Normalle 20°</text><rect x="4" y="53" width="167" height="46" rx="5" '
    'fill="#fff1df" stroke="#d97706" stroke-width="0.75"/><text x="87.5" y="71.1" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#d97706">M Işını</text><text x="87.5" y="89.9" text-anchor="middle" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Aynayla 50°</text><rect x="179" y="53" width="167" height="46" '
    'rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="71.1" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">P Işını</text><text x="262.5" y="89.9" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#0b2257">Aynayla 30°</text></svg>',
 9: '<svg viewBox="0 0 350 140" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Üç deneysel ölçümde '
    'gelme ve yansıma açısı verileri"><rect x="4" y="3" width="167" height="65" rx="5" fill="#e0f4f8" stroke="#0e8fa8" '
    'stroke-width="0.75"/><text x="87.5" y="21.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#0e8fa8">Lazer ve İletki</text><text x="87.5" y="40.0" text-anchor="middle" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="700" fill="#0e8fa8">Deneyi Ölçüm</text><text x="87.5" y="58.8" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0e8fa8">Sonuçları</text><rect x="179" y="3" '
    'width="167" height="65" rx="5" fill="#e8eefe" stroke="#2451d6" stroke-width="0.75"/><text x="262.5" y="21.2" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#2451d6">1. Ölçüm</text><text x="262.5" y="40.0" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Gelme: 20° ·</text><text '
    'x="262.5" y="58.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#0b2257">Yansıma: 20°</text><rect x="4" y="72" width="167" height="65" rx="5" fill="#e3f6ea" stroke="#12a150" '
    'stroke-width="0.75"/><text x="87.5" y="90.2" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="700" fill="#12a150">2. Ölçüm</text><text x="87.5" y="109.0" text-anchor="middle" font-family="Noto Sans, sans-serif" '
    'font-size="1.01em" font-weight="700" fill="#0b2257">Gelme: 45° ·</text><text x="87.5" y="127.8" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Yansıma: 45°</text><rect x="179" y="72" '
    'width="167" height="65" rx="5" fill="#f0e9fe" stroke="#7c3aed" stroke-width="0.75"/><text x="262.5" y="90.2" text-anchor="middle" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#7c3aed">3. Ölçüm</text><text x="262.5" y="109.0" '
    'text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" fill="#0b2257">Gelme: 70° ·</text><text '
    'x="262.5" y="127.8" text-anchor="middle" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="700" '
    'fill="#0b2257">Yansıma: 70°</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
