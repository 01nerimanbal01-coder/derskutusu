from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('tarih')
    ic = []
    ic.append(P.baslik(400, 32, '18. YÜZYILDA İKİ BÜYÜK AFET: 1755 LİZBON VE 1766 İSTANBUL DEPREMLERİ', R['koyu']))

    # Sol panel: 1755 Lizbon Depremi ve Avrupa'ya Etkileri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. 1755 LİZBON DEPREMİ VE AYDINLANMA', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, '1 Kasım 1755: Deprem, Tsunami ve Yangın', 'Atlas Okyanusu merkezli (~8.5-9.0 büyüklüğünde) deprem, dev tsunami ve 5 gün süren yangın.'),
        (150, 'Portekiz İmparatorluğu’nun Güç Kaybı', 'Başkent Lizbon’un %85’i yıkıldı; Portekiz’in sömürgecilikteki küresel rekabet gücü sarsıldı.'),
        (200, 'Marki de Pombal ve Modern Kriz Yönetimi', 'Başbakan Pombal’ın “Ölüleri gömün, kalanları doyurun” ilkesi ve Gaiola (ahşap kafes) mimarisi.'),
        (250, 'Modern Sismolojinin Doğuşu (İlk Anket)', 'Kilise bölgelerine deprem hasar ve gözlem anketi gönderilerek bilimsel sismoloji başlatıldı.'),
        (300, 'Aydınlanma Felsefesinde Tartışma (Voltaire - Rousseau)', 'Teodise/iyimserlik eleştirisi (Voltaire) ve şehirleşme/doğa ilişkisi vurgusu (Rousseau, Kant).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: 1766 İstanbul Depremi ve Osmanlı'da İmar-Kriz Yönetimi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. 1766 İSTANBUL DEPREMİ VE OSMANLI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, '22 Mayıs 1766 (Kurban Bayramı’nın 3. Günü)', 'Marmara Denizi merkezli büyük deprem ve 5 Ağustos 1766’daki ikinci yıkıcı deprem.'),
        (150, 'Fatih Camii, Surlar ve Kapalıçarşı Hasarı', 'Fatih Camii’nin ana kubbesi çöktü; Topkapı Sarayı, Yedikule ve su kemerleri ağır hasar aldı.'),
        (200, 'Sultan III. Mustafa’nın Kriz ve İmar Yönetimi', 'Padişah çadırda kaldı, hazineden fon ayırdı; taşradan mimar, kalfa ve malzeme getirtti.'),
        (250, 'Fatih Camii’nin Yeniden İnşası (1767-1771)', 'Mimar Mehmed Tahir Ağa tarafından Barok etkilerle dört fil ayağı üzerine yeniden inşa edildi.'),
        (300, 'Ahşap-Hımış Yapı Tekniği ve Fiyat Denetimi', 'Depreme dayanıklı ahşap karkas (hımış) yapıların yaygınlaşması ve kereste/kireç narhı.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KARŞILAŞTIRMA: Her iki deprem de devlet müdahalesini, depreme dayanıklı ahşap karkas mimariyi (Gaiola / Hımış) ve şehir planlamasını geliştirmiştir!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '1755 Lizbon Depremi Avrupa’da Aydınlanma düşüncesini ve sismolojiyi tetiklerken; 1766 Depremi İstanbul’un mimari dokusunu yenilemiştir.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-tarih-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
