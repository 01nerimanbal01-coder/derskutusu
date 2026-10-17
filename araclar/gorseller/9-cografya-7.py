from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('cografya')
    ic = []
    ic.append(P.baslik(400, 32, 'TÜRKİYE’NİN COĞRAFİ KONUMU: MUTLAK VE GÖRECELİ KONUM', R['koyu']))

    # Sol panel: Türkiye'nin Mutlak (Matematik) Konumu
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. MUTLAK (MATEMATİK) KONUM: 36°-42° K | 26°-45° D', R['koyu'], 11.5, 'bold', 'middle'))

    sol = [
        (100, 'Yengeç Dönencesi’nin Kuzeyinde Olması', 'Güneş ışınları hiçbir zaman dik (90°) gelmez; gölge boyu asla sıfır olmaz!'),
        (150, 'Orta Kuşakta Yer Almasının Sonuçları (ABCD)', 'Akdeniz iklimi, Batı rüzgârları, Cephesel yağışlar, Dört mevsim belirgin.'),
        (200, 'Güneyinden Kuzeyine Gidildikçe (Enlem Etkisi)', 'Güneş geliş açısı, sıcaklık, deniz tuzluluğu ve çizgisel hız AZALIR.'),
        (250, 'Kuzey Anadolu’ya Gidildikçe Artanlar', 'Gölge boyu, gece-gündüz süre farkı, grup ve tan (alacakaranlık) süresi ARTAR.'),
        (300, '26° - 45° Doğu Meridyenleri (Boylam Etkisi)', 'En doğusu ile en batısı arasında 19 meridyen × 4 dk = 76 dakika yerel saat farkı!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Türkiye'nin Göreceli (Özel) Konumu
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. GÖRECELİ (ÖZEL) KONUM VE JEOPOLİTİK ÖNEM', '#92400e', 11.5, 'bold', 'middle'))

    sag = [
        (100, 'Üç Kıtanın (Asya, Avrupa, Afrika) Kavşak Noktası', 'İstanbul ve Çanakkale Boğazları ile küresel deniz ve enerji koridoru.'),
        (150, 'Ortalama Yükseltinin Fazla Olması (1141 m)', 'Batıdan doğuya yükselti artar, sıcaklık düşer; kısa mesafede iklim değişir!'),
        (200, 'Aynı Anda Dört Mevsim Özelliklerinin Yaşanması!', 'Yükselti, yer şekilleri ve üç tarafının denizlerle çevrili olmasının sonucudur.'),
        (250, 'Genç Oluşumlu (III. ve IV. Zaman) Arazi Yapısı', 'Kuzey, Doğu ve Batı Anadolu fay hatları, deprem riski ve zengin jeotermal su.'),
        (300, 'Enerji Kaynaklarına ve Pazarlara Komşuluk', 'Orta Doğu/Hazar petrol-doğal gazı ile sanayileşmiş Avrupa arasında köprü (TANAP).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN AYRIM: “Yıl içinde dört mevsim yaşanması” -> MUTLAK KONUM (Orta Kuşak) | “Aynı anda/günde dört mevsim yaşanması” -> GÖRECELİ KONUM!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Türkiye’de dağların güney yamacının daha sıcak olması (Bakı etkisi) MUTLAK KONUM; İzmir’in Erzurum’dan sıcak olması GÖRECELİ KONUMDUR!', '#334155', 9.8, 'normal', 'middle'))

    kaydet('9-cografya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
