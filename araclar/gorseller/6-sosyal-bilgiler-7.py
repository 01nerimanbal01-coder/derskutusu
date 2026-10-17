from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('sosyal-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'KITALAR, OKYANUSLAR VE TÜRKİYE’NİN MUTLAK - GÖRECELİ KONUMU', R['koyu']))

    # Sol panel: Kıtalar, Okyanuslar ve Koordinat Sistemi (Paralel - Meridyen)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KITALAR, OKYANUSLAR VE KOORDİNAT SİSTEMİ', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, '7 Kıta (Büyükten Küçüğe)', 'Asya > Afrika > K. Amerika > G. Amerika > Antarktika > Avrupa > Okyanusya'),
        (148, '3 Büyük Okyanus', 'Büyük Okyanus (Pasifik) > Atlas (Atlantik) > Hint Okyanusu'),
        (196, 'Paraleller (Enlem) — Başlangıç: Ekvator (0°)', '90 Kuzey + 90 Güney = 180 paralel | Arası her yerde 111 km!'),
        (244, 'Meridyenler (Boylam) — Başlangıç: Greenwich (0°)', '180 Doğu + 180 Batı = 360 meridyen | Arası 4 dakika zaman farkı!'),
        (292, 'Yarım Küreleri Belirleyen Çizgiler', 'Ekvator: Kuzey-Güney YK  |  Greenwich: Doğu-Batı YK’ya ayırır.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Türkiye'nin Mutlak (Matematik) ve Göreceli (Özel) Konumu
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. TÜRKİYE’NİN KONUM ÖZELLİKLERİ', '#1e40af', 13, 'bold', 'middle'))

    sag = [
        (100, 'Türkiye’nin Mutlak (Matematik) Konumu', '36° - 42° Kuzey Paralelleri  |  26° - 45° Doğu Meridyenleri!'),
        (148, 'Mutlak Konumun Sonuçları', '• Kuzeyden güneye 6 × 111 = 666 km • Doğusu-batısı arası 76 dk fark'),
        (196, 'Orta Kuşakta Yer Almasının Sonuçları', '• Dört mevsim belirgin yaşanır • Güneyden esen rüzgârlar sıcaklığı artırır'),
        (244, 'Türkiye’nin Göreceli (Özel) Konumu', '• Asya, Avrupa, Afrika kavşağı • İstanbul ve Çanakkale Boğazları'),
        (292, 'Göreceli Konumun Sonuçları', '• Üç tarafı denizlerle çevrili • Batıdan doğuya yükselti artar • Zengin maden.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 15, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'ÇOK ÖNEMLİ FARK: "Yıl içinde dört mevsimin belirgin yaşanması" → MUTLAK KONUM  |  "Aynı anda dört mevsim özelliğinin yaşanması" → GÖRECELİ KONUM!', '#92400e', 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Türkiye hem Ekvator’un KUZEYİNDE (Kuzey Yarım Küre) hem de Greenwich’in DOĞUSUNDA (Doğu Yarım Küre) yer alır.', '#334155', 11, 'normal', 'middle'))

    kaydet('6-sosyal-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
