from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'SİYER: HZ. MUHAMMED’İN (S.A.V.) GENÇLİK YILLARI', R['koyu']))

    # Sol panel: Ticaret, Ficâr ve Hilfü'l-Fudûl
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TİCARET, FİCÂR VE HİLFÜ’L-FUDÛL', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Ticaret Seyahatleri ve “Muhammedü’l-Emîn”', 'Busrâ ve Yemen kervanları; dürüstlüğüyle “Güvenilir Muhammed” unvanını alması.'),
        (150, 'Ficâr Savaşı (Haram Aylarda Savaş)', 'Bizzat kan dökmedi; yalnızca amcalarını koruyup atılan okları topladı.'),
        (200, 'Hilfü’l-Fudûl (Erdemliler Cemiyeti - 590)', 'Zübeydli mazlum tüccarın hakkını almak için Abdullah b. Cüd’ân’ın evinde kuruldu.'),
        (250, 'Hz. Hatice (Tâhire) ile Mudârebe Ortaklığı', 'Emek-sermaye ortaklığıyla Şam seferi; yardımcısı Meysere’nin şahitliği.'),
        (300, 'Evliliği (595) ve 6 Mübarek Çocuğu', '25 yaşında evlilik; Kâsım, Zeyneb, Rukiye, Ümmü Gülsûm, Fâtıma ve Abdullah.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Hanesindeki Vefa, Kâbe Hakemliği ve Hira İnzivası
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. VEFA, KÂBE HAKEMLİĞİ VE HİRA İNZİVASI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Ebû Tâlib’e Vefa: Hz. Ali ve Zeyd b. Hârise', 'Kıtlıkta Hz. Ali’yi hanesine aldı; köle Zeyd b. Hârise’yi azat edip evlat edindi.'),
        (150, 'Kâbe’nin Tamiri (M. 605 — 35 Yaşında)', 'Sel ve yangın sonrası Kâbe’nin yalnız helal kazançla yeniden inşası.'),
        (200, 'Hacerü’l-Esved Krizi ve Hakem Seçilmesi', 'Ebû Ümeyye’nin teklifiyle Benî Şeybe kapısından ilk giren el-Emîn hakem oldu.'),
        (250, 'Yaygı (Ridâ) Üzerinde Barışçıl Çözüm', 'Her kabile reisine yaygının ucundan tutturup taşı birlikte kaldırtarak savaşı önledi.'),
        (300, 'İsmet Sıfatı ve Hira’da Tahannüs (İnziva)', 'Putlara ve cahiliye kötülüklerine hiç bulaşmadı; Nur Dağı Hira’da tefekkür etti.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'Hz. Peygamber’in 40 yıllık lekesiz gençliği (Muhammedü’l-Emîn), risalet davetine başladığında en büyük güven ve ikna zemini olmuştur!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'NOT: Peygamberimizin 7 çocuğundan 6’sı Hz. Hatice’den, en küçük oğlu İbrahim ise Medine’de Hz. Mâriye’den dünyaya gelmiştir.', '#334155', 10, 'normal', 'middle'))

    kaydet('10-siyer-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
