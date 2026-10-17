from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'KUR’AN’DAN MESAJLAR: ÂL-İ İMRÂN 190-191 VE ULÜ’L-ELBÂB (AKIL SAHİPLERİ)', R['koyu']))

    # Sol panel: Âl-i İmrân Suresi 190-191. Ayetlerin Analizi
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ÂL-İ İMRÂN SURESİ 190-191. AYETLER', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Âl-i İmrân 190: Kâinattaki İki Büyük Delil (Âyât)', '1) Göklerin ve yerin yaratılışı, 2) Gece ile gündüzün birbiri ardınca gelişi.'),
        (150, 'Ulü’l-Elbâb (Derin Akıl ve Sağduyu Sahipleri)', 'Önyargılardan arınmış, varlığın özünü kavrayan temiz akıl sahipleri.'),
        (200, 'Âl-i İmrân 191: Her Hâlde Allah’ı Zikretmek', 'Ayaktayken (kıyâmen), otururken (kuûden) ve yanları üzerine yatarken!'),
        (250, 'Zikir ile Tefekkürün Ayrılmaz Bütünlüğü', 'Kalp ve dil Allah’ı anarken (zikir), akıl da kâinatın yaratılışını düşünür (tefekkür).'),
        (300, 'Gaye ve Hikmet Duası: “Rabbimiz! Boşuna Yaratmadın!”', '“Rabbenâ mâ halakte hâzâ bâtılan sübhâneke fekınâ azâbe’n-nâr.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: 1. Ünite (İslam'da Varlık ve Bilgi) Sentezi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. VARLIK, BİLGİ VE AHLAKİ SORUMLULUK SENTEZİ', '#92400e', 11.5, 'bold', 'middle'))

    sag = [
        (100, 'Varlık Anlayışı: Gaye ve Nizam (Bâtıl Değil, Hak!)', 'Evrendeki hiçbir varlık tesadüfen ve amaçsız (bâtıl/abes) yaratılmamıştır.'),
        (150, 'Bilgi Kaynakları: Selim Akıl, Sağlam Duyular, Vahiy', 'Duyular kâinatı gözlemler, selim akıl tefekkür eder, doğru haber (vahiy) yol gösterir.'),
        (200, 'İsrâ 36 ve Mülk 23 ile Ortak Mesaj', 'Kulak, göz ve kalp (akıl) nimetlerini hakikati bulmak için kullanma sorumluluğu.'),
        (250, 'Kozmolojik (Varoluş) ve Teleolojik (Gaye-Nizam) Delil', 'Kâinatın yaratılışından Yaratıcı’ya, kusursuz düzenden O’nun hikmetine ulaşmak.'),
        (300, 'Bilginin İmana ve Salih Amele Dönüşmesi', 'Kâinatı tefekkür eden insan Allah’ı tenzih eder ve ahiret bilinciyle yaşar.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'PEYGAMBERİMİZİN UYARISI: Bu ayetler indiğinde Hz. Peygamber “Bu ayetleri okuyup da üzerinde tefekkür etmeyene yazıklar olsun!” buyurmuştur.', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'ULÜ’L-ELBÂB’IN 3 ÖZELLİĞİ: 1) Allah’ı her durumda zikrederler, 2) Kâinatın yaratılışını tefekkür ederler, 3) Ahiret sorumluluğuyla dua ederler.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
