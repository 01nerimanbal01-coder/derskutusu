from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'BİR SURE ÖĞRENİYORUM: FELAK SURESİ VE ANLAMI', R['koyu']))

    # Sol panel: Felak Suresi Okunuşu ve Künyesi
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. FELAK SURESİ’NİN OKUNUŞU (113. SURE)', R['koyu'], 13, 'bold', 'middle'))

    ayetler = [
        (100, '1. Ayet: قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ', 'Kul eûzü birabbi’l-felak.'),
        (150, '2. Ayet: مِنْ شَرِّ مَا خَلَقَ', 'Min şerri mâ halak.'),
        (200, '3. Ayet: وَمِنْ شَرِّ غَاسِقٍ إِذَا وَقَبَ', 'Ve min şerri gâsikın izâ vekab.'),
        (250, '4. Ayet: وَمِنْ شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ', 'Ve min şerri’n-neffâsâti fi’l-ukad.'),
        (300, '5. Ayet: وَمِنْ شَرِّ حَاسِدٍ إِذَا حَسَدَ', 'Ve min şerri hâsidin izâ hased.'),
    ]
    for y, b, a in ayetler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Felak Suresi'nin Anlamı ve Sığınılan Şerler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ALLAH’A SIĞINILAN KÖTÜLÜKLER (MEALİ)', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, '1. Sabahın Rabbine Sığınma (İstiâze)', 'De ki: "Sabahın Rabbine sığınırım!" (Felak = Sabah aydınlığı)'),
        (150, '2. Yaratılmışların Şerri', 'Yarattığı şeylerin (görünür-görünmez zararların) kötülüğünden,'),
        (200, '3. Çöken Gece Karanlığının Şerri (Gâsık)', 'Karanlığı çöktüğü zaman gecenin ve tehlikelerinin kötülüğünden,'),
        (250, '4. Düğümlere Üfleyenlerin Şerri', 'Büyü, fitne ve dedikodu ile ara bozanların kötülüğünden,'),
        (300, '5. Kıskanç Kişinin Şerri (Haset)', 'Kıskandığı vakit kıskanç (hasetçi) kişinin kötülüğünden!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'MUAVVİZETEYN (İKİ KORUYUCU SURE): Kur’an’ın son iki suresi olan FELAK (113) ve NÂS (114) sureleridir.', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Haset: Başkasındaki nimetin yok olmasını istemektir (yasaktır). Gıpta (İmrenme): Benzerinin kendine de verilmesini dilemektir.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('6-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
