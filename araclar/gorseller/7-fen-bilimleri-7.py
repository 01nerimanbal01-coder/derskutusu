from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fen-bilimleri')
    ic = []
    ic.append(P.baslik(400, 32, 'KUVVET, İŞ VE ENERJİ İLİŞKİSİ: KİNETİK VE POTANSİYEL ENERJİ', R['koyu']))

    # Sol panel: Kinetik Enerji (Hareket Enerjisi)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KİNETİK (HAREKET) ENERJİSİ (Ek)', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Enerji Nedir? (Birim: Joule - J)', 'Bir cismin İŞ YAPABİLME yeteneğine enerji denir.'),
        (150, 'Kinetik Enerji Tanımı', 'Hareket hâlindeki cisimlerin sahip olduğu enerjidir.'),
        (200, '1. Değişken: Sürat (v) — Doğru Orantılı', 'Kütle sabitken sürat artarsa kinetik enerji ARTAR.'),
        (250, '2. Değişken: Kütle (m) — Doğru Orantılı', 'Sürat sabitken kütle artarsa kinetik enerji ARTAR.'),
        (300, 'Günlük Hayat Örnekleri', 'Koşan sporcu, akan nehir, dönen rüzgâr türbini, uçan kuş.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Potansiyel Enerji (Çekim ve Esneklik)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. POTANSİYEL (DURUM / DEPO) ENERJİSİ (Ep)', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'A) Çekim Potansiyel Enerjisi', 'Belirli bir yükseklikteki cisimlerin ağırlığından dolayı enerjisidir.'),
        (150, 'Çekim Potansiyelinin Bağlı Olduğu Değişkenler', '1) Ağırlık / Kütle (G) ile doğru, 2) Yükseklik (h) ile doğru orantılı!'),
        (200, 'Çekim Potansiyeli Örnekleri', 'Dalda duran elma, barajdaki su, rafın üstündeki kitap.'),
        (250, 'B) Esneklik Potansiyel Enerjisi', 'Esnek cisimlerin sıkıştırılması veya gerilmesiyle depolanan enerji.'),
        (300, 'Esneklik Potansiyelinin Değişkenleri', '1) Yay esneklik özelliğine (cins/kalınlık), 2) Sıkışma/gerilme miktarına!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DENEY DEĞİŞKENLERİ: Bağımsız Değişken = Bizim değiştirdiğimiz | Bağımlı Değişken = Sonuçta değişen enerji!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hem yüksekte olan hem de hareket eden cisimler (ör. uçmakta olan uçak/kuş) HEM KİNETİK HEM POTANSİYEL enerjiye sahiptir!', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-fen-bilimleri-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
