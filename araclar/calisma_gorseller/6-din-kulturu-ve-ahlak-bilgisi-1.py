"""6-din-kulturu-ve-ahlak-bilgisi-1 çalışma kâğıdı görselleri (SVG; K024 insan figürü yok; K150 EK 1:1 gövde puntosu; K183 0 çakışma)."""

GORSELLER = {0: '<svg viewBox="0 0 350 113" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kavramları karışan '
    'kartlar"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#234a96">Tebliğ</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" '
    'font-weight="500" fill="#172849">Allah’ın emir ve hükümlerini peygambere</text><text x="11.0" y="57.2" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">bildirmesi.</text><rect x="4" y="68" '
    'width="342" height="43" rx="5" fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="85.1" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Vahiy</text><text x="11.0" y="103.5" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">Peygamberin aldığı mesajı '
    'insanlara iletmesi.</text></svg>',
 4: '<svg viewBox="0 0 350 132" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bilgiyi '
    'sınıflandırma"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" '
    'y="20.4" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Sınıflanacak '
    'bilgi</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Peygamberler, ibadetlerin nasıl yapılacağını</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">yaşayarak gösterir.</text><rect x="4" y="68" width="342" height="62" '
    'rx="5" fill="#ecf8f0" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="85.4" text-anchor="start" font-family="Noto Sans, '
    'sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Klasörler</text><text x="11.0" y="103.8" text-anchor="start" '
    'font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">A: Kavramların sözlük anlamı / B:</text><text '
    'x="11.0" y="122.2" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Peygamberlerin rehberliği</text></svg>',
 8: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Olağanüstü olay '
    'örneği"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
    'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Ders kitabındaki '
    'örnek</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
    'fill="#172849">Hz. Musa’nın asasının Allah’ın izniyle yılana</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto '
    'Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#172849">dönüşmesi.</text></svg>',
 12: '<svg viewBox="0 0 350 67" style="max-height:none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kaynağı izlenebilen '
     'kayıt"><rect x="4" y="3" width="342" height="62" rx="5" fill="#edf3ff" stroke="#2451d6" stroke-width="0.75"/><text x="11.0" y="20.4" '
     'text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" fill="#234a96">Araştırma '
     'amacı</text><text x="11.0" y="38.8" text-anchor="start" font-family="Noto Sans, sans-serif" font-size="1.01em" font-weight="500" '
     'fill="#172849">Peygamberlerin rehberliği hakkında</text><text x="11.0" y="57.2" text-anchor="start" font-family="Noto Sans, '
     'sans-serif" font-size="1.01em" font-weight="500" fill="#172849">doğrulanabilir bilgi toplamak.</text></svg>'}


def uygula(o):
    s = o.get("sorular", [])
    for idx, svg in GORSELLER.items():
        if int(idx) < len(s):
            s[int(idx)]["gorsel"] = svg
