from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'TEFSİR: KUR’AN’I ANLAMANIN VE YORUMLAMANIN TEMEL İLKELERİ', R['koyu']))

    # Sol panel: Metin İçi İlkeler: Arap Dili ve Kur'an Bütünlüğü
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. DİL, SİYAK-SİBAK VE KUR’AN BÜTÜNLÜĞÜ', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'Arap Dilinin Kurallarını ve Belâgatını Bilmek', 'Kelimelerin nüzul dönemindeki anlamlarını, hakikat-mecaz, âm-hâs ve deyimleri dikkate almak.'),
        (150, 'Kur’an’ın Kur’an ile Tefsiri (İç Bütünlük)', 'Bir yerde mücmel (özlü) geçen ayeti başka bir yerdeki mufassal (açıklayıcı) ayetle anlamak.'),
        (200, 'Siyak ve Sibak (Metin İçi Bağlam)', 'Ayetin öncesindeki (sibak) ve sonrasındaki (siyak) ayetlerle olan konu bütünlüğünü korumak.'),
        (250, 'Cımbızlama (Bağlamdan Koparma) Hatası', 'Ayeti öncesinden ve sonrasından koparıp kendi ön yargısına delil yapmak tefsirde en büyük hatadır!'),
        (300, 'Muhkem Ayetleri Merkeze Almak (Âl-i İmrân, 7)', 'Anlamı açık (muhkem) ayetleri temel alıp müteşâbih ayetleri muhkemlerin ışığında yorumlamak.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Tarihsel Bağlam: Sünnet, Sahabe ve Sebeb-i Nüzul
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SÜNNET, SAHABE VE NÜZUL ORTAMI', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Hz. Peygamber’in Sünnetine Başvurmak', 'Kur’an’ın ilk ve en yetkili müfessiri Hz. Peygamber’dir (Nahl, 44 — Tebyîn görevi).'),
        (150, 'Sahabe ve Tâbiîn Kavillerini Dikkate Almak', 'Vahyin inişine bizzat şahit olan sahabilerin (İbn Abbas, İbn Mes’ûd) açıklamalarından yararlanmak.'),
        (200, 'Esbâb-ı Nüzûlü (İniş Sebeplerini) Bilmek', 'Ayetin hangi olay veya soru üzerine indiğini bilmek, hükmün amacını (makâsıdını) aydınlatır.'),
        (250, 'Mekkî ve Medenî Ayetleri ile Nüzul Sırasını Bilmek', 'Tedricilik (aşama aşama iniş) ilkesini ve nâsih-mensûh ilişkisini doğru tespit etmek.'),
        (300, 'Temel Tefsir Kaidesi: Sebebin Hususiliği', '“İtibar, sebebin hususiliğine (özelliğine) değil, lafzın umumiliğine (genelliğine)dir!”'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'TEFSİR USULÜ SIRALAMASI: 1) Kur’an’ın Kur’an’la tefsiri -> 2) Sünnetle tefsiri -> 3) Sahabe sözü -> 4) Arap dili ve Sebeb-i Nüzul bilgisi!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '«اَلْعِبْرَةُ بِعُمُومِ اللَّفْظِ لَا بِخُصُوصِ السَّبَبِ» — Ayet özel bir olay üzerine inse bile hükmü kıyamete kadar tüm benzer durumları kapsar.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-tefsir-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic