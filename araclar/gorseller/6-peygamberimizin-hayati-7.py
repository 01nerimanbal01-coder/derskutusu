from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'VAHYİN GELİŞİ: HİRA MAĞARASI, İLK VAHİY (610) VE İLK MÜSLÜMANLAR', R['koyu']))

    # Sol panel: İlk Vahiy Süreci
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HİRA MAĞARASI VE İLK VAHİY (MİLADİ 610)', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Hira Mağarası’nda Tefekkür ve İnziva', 'Nur Dağı’ndaki Hira Mağarası’nda Ramazan ayında tefekkür.'),
        (150, 'Vahiy Meleği Cebrail (a.s.) ve "İkra!" Emri', '610 yılı Ramazan ayı Kadir Gecesi (40 yaşında): "Oku!"'),
        (200, 'İlk Vahiy: Alak Suresi 1-5. Ayetler', '"Yaratan Rabbinin adıyla oku! ... Kalemle yazmayı öğretti."'),
        (250, 'Hz. Hatice’nin Tesellisi ve Varaka bin Nevfel', 'Varaka: "Bu, Hz. Musa’ya gelen Nâmûs-ı Ekber’dir (Cebrail)."'),
        (300, 'Fetret-i Vahiy ve Müddessir Suresi', 'Kısa kesintiden sonra: "Ey örtünüp bürünen! Kalk ve uyar!"'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: İlk İman Edenler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İLK MÜSLÜMANLAR (SÂBİKÛN-İ EVVELÛN)', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, '1. Hz. Hatice (r.a.) — İlk Müslüman (Kadınlar)', 'Peygamberimizin vefakâr eşi; yeryüzünde ilk iman eden kişi.'),
        (150, '2. Hz. Ali (r.a.) — Çocuklar Arasında İlk', 'Peygamberimizin yanında büyüyen amcasının oğlu (kuzeni).'),
        (200, '3. Hz. Zeyd bin Hârise (r.a.) — Azatlılardan İlk', 'Peygamberimizin azatlısı ve manevi evladı (Zeyd bin Muhammed).'),
        (250, '4. Hz. Ebû Bekir (r.a.) — Hür Erkeklerden İlk', 'Peygamberimizin en yakın ve sadık dostu (es-Sıddîk).'),
        (300, 'İlk Vahyin Mesajı: İlim ve Okuma', 'Okumak, kalem, yazmak ve düşünmek İslam’ın ilk emridir!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALAK SURESİ 1. AYET: "İkra’ bismi rabbikellezî halak" — "Yaratan Rabbinin adıyla oku!"', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hz. Hatice: "Allah seni asla utandırmaz; çünkü sen akrabanı gözetir, doğru konuşur ve güçsüzlere yardım edersin."', '#334155', 10.5, 'normal', 'middle'))

    kaydet('6-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
