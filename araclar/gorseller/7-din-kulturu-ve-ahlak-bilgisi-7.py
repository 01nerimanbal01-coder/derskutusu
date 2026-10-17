from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'BİR SURE ÖĞRENİYORUM: NÂS SURESİ VE ANLAMI', R['koyu']))

    # Sol panel: Nâs Suresi Okunuşu (114. Sure)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. NÂS SURESİ’NİN OKUNUŞU (114. SURE)', R['koyu'], 13, 'bold', 'middle'))

    ayetler = [
        (100, '1-2. Ayet: Kul eûzü birabbi’n-nâs. Meliki’n-nâs.', 'De ki: İnsanların Rabbine, insanların Melikine (hükümdarına),'),
        (150, '3. Ayet: İlâhi’n-nâs.', 'İnsanların İlahına (gerçek mabuduna) sığınırım!'),
        (200, '4. Ayet: Min şerri’l-vesvâsi’l-hannâs.', 'O sinsi vesvesecinin (hannâsın) şerrinden!'),
        (250, '5. Ayet: Ellezî yüvesvisü fî sudûri’n-nâs.', 'O ki, insanların göğüslerine (kalplerine) vesvese verir.'),
        (300, '6. Ayet: Mine’l-cinneti ve’n-nâs.', 'Gerek cinlerden, gerekse insanlardan (olan vesvesecilerden)!'),
    ]
    for y, b, a in ayetler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Nâs Suresi'ndeki Kavramlar ve Mesajlar
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. TEMEL KAVRAMLAR VE ANA MESAJLAR', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, 'En-Nâs (İnsanlar) ve Kur’an’ın Son Suresi', 'Kur’an’ın 114. (son) suresidir; Mekke’de inmiş, 6 ayettir.'),
        (150, 'Allah’ın Üç Sıfatı: Rab, Melik, İlah', 'İnsanları terbiye eden (Rab), yöneten (Melik), ibadet edilen (İlah).'),
        (200, 'Vesvese ve El-Hannâs (Sinsi Vesveseci)', 'Kalbe şüphe/kötülük fısıldayan, Allah anılınca sinip kaçan şeytan.'),
        (250, 'Cinlerden ve İnsanlardan Vesveseciler', 'Kötülüğe çağıran kötü niyetli telkinlerden Allah’a sığınılır.'),
        (300, 'Muavvizeteyn (Felak ve Nâs Sureleri)', 'İki koruyucu sure: Felak dış şerlerden, Nâs iç vesveseden korur.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KUR’AN-I KERİM’İN SIRALAMASI: 1. Sure FATİHA Suresi ile başlar, 114. Sure NÂS Suresi ile sona erer!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Vesveseden korunmak için "Eûzü billâhi mine’ş-şeytâni’r-racîm" denir, Felak ve Nâs sureleri okunarak Allah’a sığınılır.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
