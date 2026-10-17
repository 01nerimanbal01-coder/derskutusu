from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'İSLAM’I ANLAMA VE YAŞAMADA SÜNNETİN YERİ VE ÖNEMİ', R['koyu']))

    # Sol panel: Sünnetin Kur'an'ı Açıklama (Beyan) Görevleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SÜNNETİN KUR’AN’I AÇIKLAMA (BEYAN) İŞLEVİ', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Nahl 16/44: "...İnsanlara indirileni açıklayasın diye...")', '#334155', 10, 'bold', 'middle'))

    beyan = [
        (114, '1. Mücmeli Tefsil (Özet Olanı Açıklama)', 'Namazın rekâtları, zekâtın nisabı, haccın yapılışını gösterme.'),
        (162, '2. Umumiliği Tahsis (Geneli Sınırlandırma)', 'Miras veya haram yiyeceklerle ilgili genel hükmü özelleştirme.'),
        (210, '3. Mutlakı Takyid (Kayıtsızı Kayıtlandırma)', 'Vasiyet miktarını malın üçte biriyle (1/3) sınırlandırma.'),
        (258, '4. Müşkili Tavzih (Kapalı/Zor Olanı Aydınlatma)', '"Zulüm" kelimesinin şirk, "ak ve kara iplik"in fecir olduğunu açıklama.'),
        (306, '5. Te’kid ve Teşri (Pekiştirme ve Hüküm Koyma)', 'Kur’an hükümlerini pekiştirme ve yeni meselelerde hüküm koyma.'),
    ]
    for y, b, a in beyan:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: İslam'ı Yaşamada Sünnetin Rehberliği
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İSLAM’I YAŞAMADA SÜNNETİN REHBERLİĞİ', '#92400e', 13, 'bold', 'middle'))

    rehber = [
        (102, 'Kur’an’ın Canlı ve Pratik Uygulaması', 'Hz. Âişe: "Onun ahlakı Kur’an’dı." (Yaşayan Kur’an)'),
        (154, 'İbadetlerde Ölçü ve İtidal (Denge)', 'Aşırılıktan (ifrat) ve ihmalden (tefrit) koruyan orta yol'),
        (206, 'Ahlaki ve Toplumsal Hayatın İnşası', 'Aile hayatı, komşuluk, ticaret ahlakı, merhamet ve adalet'),
        (258, 'Kültürel Birlik ve Kimlik Koruyucusu', 'Asırlardır tüm Müslümanları ortak ibadet ve edepte birleştirme'),
    ]
    for y, b, a in rehber:
        ic.append(P.kutu(415, y, 350, 44, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 34, a, '#334155', 10, 'normal', 'middle'))

    ic.append(P.kutu(415, 310, 350, 26, '#fef2f2', '#dc2626'))
    ic.append(P.metin(590, 327, '"Beni nasıl namaz kılarken görüyorsanız öyle namaz kılın!" (Buhârî)', '#b91c1c', 10, 'bold', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KUR’AN VE SÜNNET BÜTÜNLÜĞÜ: Et ve tırnak gibidir; Sünnet olmadan Kur’an’daki ibadet ve ahlak ilkeleri hayata geçirilemez!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Veda Hutbesi: "Size iki emanet bırakıyorum; onlara sımsıkı sarıldıkça asla sapıtmazsınız: Allah’ın Kitabı ve Peygamberinin Sünneti."', '#334155', 11, 'normal', 'middle'))

    kaydet('12-peygamberimizin-hayati-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic