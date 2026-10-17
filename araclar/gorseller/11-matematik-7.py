from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'ÖZEL DÖRTGENLER: YAMUK VE PARALELKENARIN ÖZELLİKLERİ', R['koyu']))

    # Sol panel: Yamuk ve Özel Yamuk Türleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. YAMUK VE ÖZEL YAMUK TÜRLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Yamuk Tanımı ve Komşu Açılar', 'En az iki kenarı paralel olan dörtgendir (AB // DC). Yan kenar uç açıları toplamı 180°’dir.'),
        (150, 'Orta Taban (EF) ve Köşegen Parçası (KL)', 'Orta taban: |EF| = (a + c) / 2  |  Köşegenlerin orta tabanda ayırdığı parça: |KL| = |a - c| / 2.'),
        (200, 'İkizkenar Yamuk Özellikleri', 'Yan kenarlar eşit (|AD| = |BC|), taban açıları eşit, köşegenler eşit (|AC| = |BD|).'),
        (250, 'Dik Yamuk ve Dik Köşegenli İkizkenar Yamuk', 'Dik yamukta dikme indirilir. İkizkenar yamukta AC ⊥ BD ise yükseklik h = (a + c) / 2.'),
        (300, 'Yamuğun Alanı ve Alan Oranları', 'Alan(ABCD) = ((a + c) / 2) · h = |EF| · h. Kelebek yan üçgenlerin alanları eşittir (S_1 = S_3).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Paralelkenar ve Özellikleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. PARALELKENAR VE ALAN BAĞINTILARI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Karşılıklı Kenar ve Açı Özellikleri', 'Karşılıklı kenarlar paralel ve eşit; karşılıklı açılar eşit, ardışık açılar toplamı 180°’dir.'),
        (150, 'Köşegenlerin Birbirini Ortalaması', 'Köşegenler eşit değildir ancak birbirini ortalar: |AO| = |OC| ve |BO| = |OD|.'),
        (200, 'Komşu Açıortayların Dik Kesişimi', 'Ardışık iki köşeden çıkan açıortaylar dik kesişir (90°) ve kesim noktası orta tabandadır!'),
        (250, 'Paralelkenarda Alan Formülleri', 'Alan = a · h_a = b · h_b = a · b · sin(A). Köşegenler alanı 4 eşit üçgene böler (S, S, S, S).'),
        (300, 'Köşegen Kuvvet Bağıntısı', 'e^2 + f^2 = 2 · (a^2 + b^2). İçerde alınan P noktası için karşılıklı alanlar toplamı eşittir.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: Yamukta köşegenlerin oluşturduğu 4 bölgede karşılıklı alanlar çarpımı eşittir: S_1 · S_3 = S_2 · S_4 (ve S_1 = S_3 => S^2 = A_alt · A_üst)!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Paralelkenarın bir kenarı üzerinde alınan E noktası karşı iki köşeyle birleştirilirse oluşan üçgenin alanı tüm alanın YARISIDIR!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
