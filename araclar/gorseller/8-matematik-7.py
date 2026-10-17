from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'KAREKÖKLÜ İFADELER: YAKLAŞIK DEĞER TAHMİNİ VE KATSAYI İŞLEMLERİ', R['koyu']))

    # Sol panel: Tam Kare Olmayan Sayıların Karekökünü Tahmin Etme
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TAM KARE OLMAYAN KAREKÖKÜ TAHMİN ETME', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Hangi İki Doğal Sayı Arasında?', 'Sayının altındaki ve üstündeki en yakın tam kare sayılar belirlenir.'),
        (150, 'Örnek: Karekök 40 Hangi İki Tam Sayı Arasındadır?', '36 < 40 < 49  =>  6 < karekök(40) < 7 (6 ile 7 arasındadır).'),
        (200, 'Hangisine Daha Yakındır? (Fark Kontrolü)', '40 - 36 = 4 birim  |  49 - 40 = 9 birim  =>  6’ya daha yakındır!'),
        (250, 'Onda Birler Basamağına Kadar Tahmin', 'karekök(40) ≈ 6,3  (Tam ortası 6,5 olduğundan 6,5’ten küçüktür).'),
        (300, 'Sayı Doğrusunda Gösterim Adımı', 'Önce tam sayı aralığı, sonra yakın olduğu uç belirlenerek işaretlenir.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Katsayıyı Kök Dışına Çıkarma ve Kök İçine Alma
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KATSAYIYI KÖK DIŞINA ÇIKARMA VE İÇİNE ALMA', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, '1. Çarpanı Kök Dışına Çıkarma (a² · b -> a kök b)', 'Kök içindeki tam kare çarpan (a²), kök dışına katsayı (a) olarak çıkar.'),
        (150, 'Örnekler: Karekök 72 ve Karekök 48', '72 = 36 · 2 => 6 kök 2   |   48 = 16 · 3 => 4 kök 3.'),
        (200, '2. Katsayıyı Kök İçine Alma (a -> a²)', 'Kök dışındaki pozitif katsayı (a), karesi alınarak (a²) kök içine girer.'),
        (250, 'Örnekler: 5 kök 3 ve 3 kök 7', '5² · 3 = 25 · 3 = karekök(75)  |  3² · 7 = 9 · 7 = karekök(63).'),
        (300, 'Kareköklü Sayılarda Sıralama Kuralı', 'Katsayılar kök içine alınır: karekök(75) > 6 (karekök 36) > karekök(18).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'NEGATİF SIRALAMA UYARISI: Eksi (-) işareti kök içine GİRMEZ! Kök dışındaki eksi korunarak katsayının karesi alınır!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Asal çarpan algoritmasında çift olan her iki aynı asal çarpandan biri kök dışına çıkar, tek kalanlar kök içinde çarpılır.', '#334155', 10, 'normal', 'middle'))

    kaydet('8-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
