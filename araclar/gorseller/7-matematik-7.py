from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'RASYONEL SAYILARIN KARESİ-KÜPÜ, ÇOK ADIMLI İŞLEMLER VE PROBLEMLER', R['koyu']))

    # Sol panel: Rasyonel Sayıların Karesi, Küpü ve Çok Adımlı İşlemler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KARE-KÜP VE ÇOK ADIMLI İŞLEMLER', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Rasyonel Sayının Karesi (n = 2 -> Daima Pozitif)', '(-a/b)² = (-a/b) · (-a/b) = +a²/b²   Ör: (-2/3)² = +4/9.'),
        (150, 'Rasyonel Sayının Küpü (n = 3 -> İşaret Korunur)', '(-a/b)³ = -a³/b³   Ör: (-2/3)³ = -8/27  |  (+1/2)³ = +1/8.'),
        (200, 'Çok Adımlı İşlemlerde İşlem Önceliği', '1) Üslü  2) Parantez içi  3) Çarpma-Bölme  4) Toplama-Çıkarma.'),
        (250, 'Merdivenli İşlemlerde ANA KESİR ÇİZGİSİ', 'Eşittir (=) hizasındaki en uzun çizgi bölme işlemini ayırır!'),
        (300, 'Örnek: (2/3) / 4  ≠  2 / (3/4)', '(2/3) ÷ 4 = 2/12 = 1/6   iken   2 ÷ (3/4) = 2 · (4/3) = 8/3!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Rasyonel Sayı Problemleri Çözüm Stratejileri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. RASYONEL SAYI PROBLEMLERİ STRATEJİLERİ', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '1. Bütünün Kesir Kadarını Bulma (Çarpma)', '120 TL’nin 3/5’ü -> 120 · (3/5) = 72 TL.'),
        (150, '2. Kesir Kadarı Verilen Bütünü Bulma (Bölme)', '3/5’ü 72 TL olan para -> 72 ÷ (3/5) = 72 · (5/3) = 120 TL.'),
        (200, '3. "Kalanın Kesri" Problemleri', 'Önce 1’den ilk kesir çıkarılır, kalan ile ikinci kesir çarpılır!'),
        (250, '4. Kesrin Kesrini Bulma (İki Kesrin Çarpımı)', '2/3’ünün 3/4’ü -> (2/3) · (3/4) = 6/12 = 1/2.'),
        (300, '5. Top Zıplama / Yol / Su Deposu Problemleri', 'Her adımda yüksekliği veya kalan miktarı rasyonel kesirle çarp!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'PARANTEZ UYARISI: (-3/4)² = +9/16 iken, parantezsiz -3²/4 = -9/4 ve -(3/4)² = -9/16 olur!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Tam sayılı kesirlerin karesi veya küpü alınırken ÖNCE BİLEŞİK KESRE çevrilir: (-1 tam 1/2)² = (-3/2)² = +9/4.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
