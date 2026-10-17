from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('sosyal-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'YAŞADIĞIMIZ İLİN GÖRECELİ KONUMU VE HAYATIMIZA ETKİLERİ', R['koyu']))

    # Sol panel: Göreceli Konumu Oluşturan Unsurlar
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İLİMİZİN GÖRECELİ KONUM UNSURLARI', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Bir İli Diğer İllerden Ayıran Özel Konum Özellikleri)', '#334155', 10, 'bold', 'middle'))

    unsurlar = [
        (114, 'Komşu İller ve Sınır Kapıları', 'Hangi illerle veya komşu ülkelerle sınır komşusudur?'),
        (162, 'Denizlere ve Boğazlara Göre Konum', 'Denize kıyısı olan kıyı ili mi, yoksa iç kesimde (karasal) mi?'),
        (210, 'Yeryüzü Şekilleri ve Yükselti', 'Dağlar, ovalar, platolar, vadiler ve deniz seviyesinden yükseltisi.'),
        (258, 'Su Kaynakları (Akarsu, Göl, Baraj)', 'İlin içinden geçen nehirler, göller ve yer altı suları.'),
        (306, 'Ulaşım Hatları ve Tarihî-Doğal Varlıklar', 'Kara, demir, deniz, hava yolları; müzeler ve millî parklar.'),
    ]
    for y, b, a in unsurlar:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Göreceli Konumun İklim, Ekonomi ve Nüfusa Etkisi
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. GÖRECELİ KONUMUN İNSAN HAYATINA ETKİSİ', '#1e40af', 13, 'bold', 'middle'))

    etkiler = [
        (100, 'İklime Etkisi (Ilıman vs. Sert Karasal)', 'Kıyı illerinde (Antalya, İzmir) ılıman; yüksek doğu illerinde sert kış.'),
        (150, 'Tarıma ve Ürün Çeşitliliğine Etkisi', 'Verimli ovalarda (Çukurova, Konya) tarım; engebeli yerde hayvancılık.'),
        (200, 'Sanayi ve Ticarete Etkisi', 'Ulaşım kavşağındaki ve limanlı illerde (İstanbul, İzmit) ticaret-sanayi.'),
        (250, 'Turizme Etkisi', 'Güneşli kıyılarda yaz turizmi; yüksek dağlarda (Uludağ, Palandöken) kış turizmi.'),
        (300, 'Nüfus ve Yerleşmeye Etkisi', 'İklimi ılıman, yer şekilleri sade ve ulaşımı gelişmiş iller kalabalıktır!'),
    ]
    for y, b, a in etkiler:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'PUSULA VE YÖNLER: 4 Ana Yön (Kuzey, Güney, Doğu, Batı) + 4 Ara Yön (Kuzeydoğu, Kuzeybatı, Güneydoğu, Güneybatı)', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Türkiye’de batıdan doğuya doğru gidildikçe yükselti artar, sıcaklık ortalaması düşer ve karasallık şiddetlenir.', '#334155', 11, 'normal', 'middle'))

    kaydet('5-sosyal-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
