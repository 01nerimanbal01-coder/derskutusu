from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'PERGEL VE CETVEL İLE EŞKENAR, İKİZKENAR VE ÇEŞİTKENAR ÜÇGEN İNŞASI', R['koyu']))

    # Sol panel: Pergel ve Cetvel ile Eşkenar Üçgen İnşası Adımları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. PERGEL VE CETVELLE ÜÇGEN İNŞASI', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Çemberin Yarıçaplarının Eşitliği İlkesinden Yararlanma)', '#334155', 10, 'bold', 'middle'))

    adimlar = [
        (114, '1. Adım: Taban Doğru Parçasını Çizme', 'Cetvel ile belirlenen uzunlukta [AB] doğru parçası çizilir.'),
        (164, '2. Adım: A Merkezli Çember Yayı Çizme', 'Pergel ikinci kenar uzunluğu kadar açılıp A merkezli yay çizilir.'),
        (214, '3. Adım: B Merkezli Çember Yayı Çizme', 'Pergel üçüncü kenar uzunluğu kadar açılıp B merkezli yay çizilir.'),
        (264, '4. Adım: Kesişim Noktasını (C) Birleştirme', 'İki yayın kesiştiği C noktası A ve B ile birleştirilip ABC üçgeni oluşur!'),
    ]
    for y, b, a in adimlar:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    ic.append(P.kutu(35, 312, 335, 26, '#fef3c7', '#d97706'))
    ic.append(P.metin(202, 329, 'Eşkenar Üçgende pergel açıklığı hiç değiştirilmez (|AB|=|AC|=|BC|)!', '#92400e', 10, 'bold', 'middle'))

    # Sağ panel: Kenar ve Açılarına Göre Üçgenlerin Birleşik Sınıflandırılması
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. ÜÇGENLERDE KENAR - AÇI İLİŞKİSİ TABLOSU', '#1e40af', 13, 'bold', 'middle'))

    tablo = [
        (100, 'Eşkenar Üçgen', '3 kenarı eşit • 3 açısı da 60° (Sadece DAR AÇILI olur!)'),
        (150, 'İkizkenar Üçgen', '2 kenarı ve taban açıları eşit (Dar, Dik veya Geniş açılı olabilir)'),
        (200, 'Çeşitkenar Üçgen', '3 kenarı ve 3 açısı farklı (Dar, Dik veya Geniş açılı olabilir)'),
        (250, 'İkizkenar Dik Üçgen', 'Açıları: 90° - 45° - 45° (Dik kenar uzunlukları birbirine eşit)'),
        (300, 'Üçgenin İç Açıları Toplamı', 'Her üçgenin iç açılarının ölçüleri toplamı 180°’dir!'),
    ]
    for y, b, a in tablo:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: "Dik açılı eşkenar üçgen" veya "Geniş açılı eşkenar üçgen" ÇİZİLEMEZ; çünkü eşkenar üçgenin her açısı 60°’dir!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Çember merkezinden yay üzerindeki tüm noktalara çizilen yarıçaplar (r) birbirine eşittir.', '#334155', 11, 'normal', 'middle'))

    kaydet('5-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
