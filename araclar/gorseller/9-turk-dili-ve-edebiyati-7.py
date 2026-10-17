from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turk-dili-ve-edebiyati')
    ic = []
    ic.append(P.baslik(400, 32, '1. TEMA: SÖZÜN İNCELİĞİ — KONUŞMA, YAZMA VE İYİ BİR ANLATIMIN ÖZELLİKLERİ', R['koyu']))

    # Sol panel: Konuşma ve Yazma (Deneme & Mülakat Üretimi)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KONUŞMA VE YAZMA (METİN ÜRETİM SÜRECİ)', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Hazırlık ve Planlama Aşaması', 'Konu, amaç, hedef kitle ve metin türü (deneme/mülakat) belirlenir.'),
        (150, 'Deneme Yazma: “Ben” Dili ve İçtenlik', 'Yazar, kanıtlama kaygısı gütmeden özgün düşüncelerini samimi dille yazar.'),
        (200, 'Mülakat (Görüşme) Gerçekleştirme', 'Önceden açık uçlu sorular hazırlanır; nezaket ve etkin dinleme uygulanır.'),
        (250, 'Düşünceyi Geliştirme Yolları', 'Tanımlama, örnekleme, karşılaştırma, tanık gösterme ve benzetme kullanılır.'),
        (300, 'Gözden Geçirme ve Paylaşma', 'Metin; yazım, noktalama ve anlatım bozuklukları açısından denetlenir.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: İyi Bir Anlatımın Nitelikleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İYİ BİR ANLATIMIN TEMEL ÖZELLİKLERİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Açıklık (Netlik — Tek Anlamlılık)', 'Anlatımın tartışmaya yer bırakmayacak kadar net olması, bulanık olmaması.'),
        (150, 'Duruluk (Gereksiz Sözcük Bulunmaması)', 'Cümlede eş anlamlı veya aynı anlama gelen gereksiz sözcük kullanılmaması.'),
        (200, 'Yalınlık (Sadelik — Süssüzlük)', 'Ağır sanatlı söyleyişlerden, abartılı imgelerden uzak, doğal anlatım.'),
        (250, 'Akıcılık (Kolay Okunabilirlik ve Ses Uyumu)', 'Söylenmesi güç kelimelerden kaçınarak metnin pürüzsüzce okunması.'),
        (300, 'Özgünlük, Özlülük ve Tutarlılık', 'Başkasına benzememe (özgünlük), az sözle çok şey anlatma (özlülük).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KARIŞTIRMA: DURULUK = Gereksiz sözcük olmaması (“gizli sır” -> duruluğu bozar!) | YALINLIK = Ağır söz sanatları olmaması!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Sözlü anlatımda vurgu, tonlama, telaffuz (boğumlama) ve beden dili; yazılı anlatımda ise noktalama ve bağdaşıklık esastır.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-turk-dili-ve-edebiyati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
