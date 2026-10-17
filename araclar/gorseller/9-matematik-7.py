from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'DOĞRUSAL FONKSİYONLAR VE NİTEL ÖZELLİKLERİ: f(x) = ax + b', R['koyu']))

    # Sol panel: Doğrusal Referans Fonksiyon f(x) = x ve f(x) = ax + b
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. REFERANS FONKSİYON f(x) = x VE f(x) = ax + b', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Doğrusal Referans Fonksiyon: f(x) = x', 'Tanım: ℝ -> Görüntü: ℝ | Eğim (m) = 1 | Orijinden (0, 0) geçer.'),
        (150, 'Genel Doğrusal Fonksiyon: g(x) = a(x ± r) ± k = ax + b', 'a: Eğim (değişim oranı) | b: y-eksenini kestiği nokta (0, b).'),
        (200, 'Eksenleri Kestiği Noktalar ve Sıfırı (Kökü)', 'y-kesimi: x = 0 için (0, b) | x-kesimi (sıfırı): g(x) = 0 -> x = -b/a.'),
        (250, 'Artanlık, Azalanlık ve Sabitlik Durumu', 'a > 0 ise ℝ’de ARTAN | a < 0 ise ℝ’de AZALAN | a = 0 ise SABİT.'),
        (300, 'Bire Birlik ve Örtenlik (a ≠ 0 İken)', 'Tanım ve değer kümesi ℝ olan her g(x) = ax + b (a ≠ 0) bire bir ve örtendir.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: İşaret İncelemesi ve Cebirsel Özellikler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. NİTEL ÖZELLİKLER VE GERÇEK YAŞAM MODELİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Değişim Oranı (Eğim = a) Hesabı', 'a = [f(x₂) - f(x₁)] / (x₂ - x₁) = Δy / Δx -> Her yerde sabittir!'),
        (150, 'Fonksiyonun İşaret Aralığı (Pozitif / Negatif)', 'g(x) > 0 (x-ekseni üstü) ve g(x) < 0 (x-ekseni altı) kök (-b/a) ile ayrılır.'),
        (200, 'Maksimum ve Minimum Değer Durumu', 'Tanım kümesi ℝ ise max/min yoktur; [c, d] kapalı aralığında uç noktalardadır!'),
        (250, 'Cebirsel İşlem Özellikleriyle Bağlantı', 'a(x + r) + k ifadesi dağılma ve birleşme özellikleriyle ax + (ar + k) olur.'),
        (300, 'Gerçek Yaşam Modellemesi: f(t) = a·t + b', 'b: Başlangıç değeri (t = 0) | a: Birim zamandaki sabit artış veya azalış.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖRNEK ANALİZ: g(x) = 2x - 6 -> Eğim a = 2 (> 0, Artan) | y-kesimi: (0, -6) | Sıfırı (Kökü): 2x - 6 = 0 => x = 3.', R['koyu'], 10.3, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'İşaret: x > 3 için g(x) > 0 (pozitif); x < 3 için g(x) < 0 (negatif). Tanım kümesi ℝ olduğundan bire bir ve örtendir.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
