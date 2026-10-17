from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'KESİR - BÖLME İLİŞKİSİ, DEVİRLİ ONDALIK GÖSTERİM VE YUVARLAMA', R['koyu']))

    # Sol panel: Kesir - Bölme İlişkisi ve Sonlu / Devirli Ondalık Gösterim
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KESİR - BÖLME VE DEVİRLİ ONDALIKLAR', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, 'Kesir = Bölme İşlemi (a / b = a ÷ b)', 'Pay bölünen, kesir çizgisi bölme, payda ise bölendir: 3/4 = 3 ÷ 4 = 0,75.'),
        (150, 'Sonlu Ondalık Gösterim', 'Bölme işleminde kalanın 0 olduğu ondalıklar: 7/5 = 1,4  |  3/8 = 0,375.'),
        (200, 'Devirli (Periyodik) Ondalık Gösterim', 'Bölmede kalan 0 olmaz, rakamlar tekrar eder: 1/3 = 0,333...'),
        (250, 'Devir Çizgisinin Kullanımı', 'Sadece tekrar eden rakamların üstüne çizgi konur: 2,4555... → 2,4(5̄).'),
        (300, 'Paydayı 10, 100, 1000 Yaparak Çevirme', '3/20 kesrini 5 ile genişletirsek: 15/100 = 0,15 bulunur.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Ondalık Gösterimleri Yuvarlama Kuralları
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. ONDALIK GÖSTERİMLERİ YUVARLAMA', '#1e40af', 13, 'bold', 'middle'))

    sag = [
        (100, 'Yuvarlama Adımı: Sağdaki İlk Rakama Bak!', 'Yuvarlanacak basamağın hemen SAĞINDAKİ rakam kontrol edilir:'),
        (150, 'Rakam 5’ten Küçükse (0, 1, 2, 3, 4)', 'Basamak DEĞİŞMEZ, sağdaki rakamlar silinir!'),
        (200, 'Rakam 5 veya 5’ten Büyükse (5, 6, 7, 8, 9)', 'Yuvarlanan basamak 1 ARTIRILIR, sağdaki rakamlar silinir!'),
        (250, 'Örnek 1: 4,372 → Onda Birler Basamağına', '3’ün sağında 7 var (7 ≥ 5) → 3 bir artar → 4,4 olur.'),
        (300, 'Örnek 2: 4,372 → Yüzde Birler Basamağına', '7’nin sağında 2 var (2 < 5) → 7 değişmez → 4,37 olur.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'DEVİRLİ SAYILARDA SIRALAMA: Devir çizgisi açılarak basamaklar alt alta hizalanır (Ör: 2,4̄ = 2,444... > 2,400...).', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Bir doğal sayıyı (Birlere) yuvarlarken virgülün hemen sağındaki ONDA BİRLER basamağına bakılır!', '#334155', 11, 'normal', 'middle'))

    kaydet('6-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
