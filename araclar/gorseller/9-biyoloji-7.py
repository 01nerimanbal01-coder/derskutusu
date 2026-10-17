from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('biyoloji')
    ic = []
    ic.append(P.baslik(400, 32, 'BİLİMSEL ARAŞTIRMA SÜREÇLERİ, DENEY TASARIMI VE BİLİM ETİĞİ', R['koyu']))

    # Sol panel: Kontrollü Deney Tasarımı ve Değişkenler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KONTROLLÜ DENEY VE DEĞİŞKEN ANALİZİ', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Hipotezden Tahmine ("Eğer... ise ...-dır")', 'Sınanabilir hipotezden deney öncesi mantıksal tahmin cümlesi kurulur.'),
        (150, 'Kontrol Grubu ve Deney Grubu', 'Kontrol grubu: Doğal/standart koşul (karşılaştırma referansı) | Deney: Etken uygulanır.'),
        (200, 'Bağımsız Değişken (Neden / Araştırılan Etken)', 'Araştırmacının etkisini test etmek için kendi eliyle değiştirdiği değişkendir.'),
        (250, 'Bağımlı Değişken (Sonuç / Ölçülen Tepki)', 'Bağımsız değişkene bağlı olarak değişen ve ölçülen sonuç değişkenidir.'),
        (300, 'Kontrol Edilen (Sabit Tutulan) Değişkenler', 'Deney ve kontrol grubunda eşit tutulan tüm dış faktörler (sıcaklık, su vb.).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Veri Analizi, Teori-Kanun ve Bilim Etiği
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. VERİ ANALİZİ VE BİLİM ETİĞİ İHLALLERİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Sonuçların Değerlendirilmesi ve Hipotez Revizyonu', 'Veriler hipotezi desteklemezse hipotez terk edilir veya yenisi kurulur!'),
        (150, 'Bilimsel Teori (Kuram) ve Kanun (Yasa) Ayrımı', 'Kanun olayın NASIL gerçekleştiğini, Teori ise NEDEN gerçekleştiğini açıklar.'),
        (200, 'Uydurma (Fabrikasyon) ve Çarpıtma (Falsifikasyon)', 'Yapılmayan deneyi yapılmış göstermek (uydurma) veya veriyi değiştirmek (çarpıtma).'),
        (250, 'İntihal (Aşırma) ve Dilimleme (Salamizasyon)', 'Başkasının eserini kaynak göstermeden almak (intihal); tek araştırmayı bölmek.'),
        (300, 'Biyoetik ve Denek Hakları (3R İlkesi)', 'Canlılara zarar vermemek, aydınlatılmış onam almak ve etik kurul onayı.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: Sağlıklı bir kontrollü deneyde aynı anda YALNIZCA BİR TANE bağımsız değişken değiştirilir!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Bilimsel teoriler (Hücre Teorisi, Evrim Teorisi vb.) yeterince kanıtlanınca kanuna DÖNÜŞMEZ; teori ve kanun farklı bilgi türleridir!', '#334155', 10, 'normal', 'middle'))

    kaydet('9-biyoloji-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
