from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'MEAL VE TEFSİRLERDEN YARARLANMA İLKELERİ', R['koyu']))

    # Sol panel: Tercüme, Meal ve Tefsir Farkı
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TERCÜME, MEAL VE TEFSİR KAVRAMLARI', R['koyu'], 13, 'bold', 'middle'))
    kavramlar = [
        (100, 'Tercüme (Çeviri)', 'Bir sözün başka bir dile birebir, eş değer aktarılmasıdır.'),
        (150, 'Meal (“Eksik / Yaklaşık Çeviri”)', 'Kur’an ayetlerinin başka bir dile yaklaşık anlamla aktarımı.'),
        (200, 'Neden "Tercüme" Değil "Meal" Denir?', 'İlahi kelamın eşsiz belagati birebir başka dile çevrilemez!'),
        (250, 'Tefsir (Açıklama ve Yorumlama)', 'Ayetlerin iniş sebebi, bağlamı ve hükümlerinin açıklanması.'),
        (300, 'Müfessir', 'Tefsir ilmiyle uğraşan ve Kur’an’ı açıklayan uzman âlim.'),
    ]
    for y, b, a in kavramlar:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Meal ve Tefsir Okurken Dikkat Edilecek İlkeler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. MEAL VE TEFSİRDEN YARARLANMA İLKELERİ', '#92400e', 13, 'bold', 'middle'))
    ilkeler = [
        (100, '1. Kur’an Bütünlüğü (Siyak-Sibak / Bağlam)', 'Ayetler tek başına değil, öncesi-sonrası ve diğer ayetlerle okunmalı.'),
        (150, '2. Sünnet ve Hadis Bilgisine Başvurma', 'Mücmel (özet) ayetlerin uygulanışı Hz. Peygamber’in sünnetiyle anlaşılır.'),
        (200, '3. Esbâb-ı Nüzûl (İniş Sebepleri) ve Mekki-Medeni', 'Ayetin hangi olay üzerine, nerede ve ne zaman indiği bilinmelidir.'),
        (250, '4. Muhkem ve Müteşâbih Ayet Ayrımı', 'Yoruma açık (müteşâbih) ayetler, açık (muhkem) ayetler ışığında anlaşılır.'),
        (300, '5. Tek Mealle Yetinmeme & Tefsire Başvurma', 'Anlaşılmayan yerlerde güvenilir tefsirlere (Kur’an Yolu vb.) bakılmalı.'),
    ]
    for y, b, a in ilkeler:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'TEMEL KURAL: Meal, Kur’an’ın bizzat kendisi değil; mütercimin Kur’an’dan anladığının özlü aktarımıdır.', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Yalnızca meal okuyarak dini konularda kesin fıkhî hüküm (fetva) çıkarılamaz; mutlaka tefsir ve sünnete başvurulmalıdır.', '#334155', 11, 'normal', 'middle'))

    kaydet('12-kuran-i-kerim-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic