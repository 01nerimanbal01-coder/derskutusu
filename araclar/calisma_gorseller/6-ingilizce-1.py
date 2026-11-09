"""6-ingilizce-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="İhtiyaçtan bölüme"><rect '
    'x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Çalışma '
    'ihtiyacım</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Kelimeyi okuyup anlıyorum. Seslerini doğru</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">söylemek için çalışacağım.</text></svg>',
 3: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kitap rehberi '
    'kontrolü"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">A / '
    'B</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">A: Ready to Say → telaffuz; B: Ready to</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Explore → yalnız ses çalışması</text><rect x="4" y="68" width="342" '
    'height="62" rx="5" fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="85.4" text-anchor="start" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">C / D</text><text x="11.0" y="103.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">C: Ready to Build → dilin kullanımı; '
    'D:</text><text x="11.0" y="122.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Ready to Play → oyunlaştırma</text></svg>',
 7: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sunma ve '
    'değerlendirme"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Bugünkü '
    'hedef</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Hazırladığım projeyi sunacağım; neleri</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">öğrendiğimi değerlendireceğim.</text></svg>',
 11: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alanlar arası '
     'öğrenme"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
     'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#234a96">Hedef</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
     'font-weight="500" fill="#172849">Dil öğrenirken farklı alanları ve kültürleri</text><text x="11.0" y="57.2" text-anchor="start" '
     'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">tanımak.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
