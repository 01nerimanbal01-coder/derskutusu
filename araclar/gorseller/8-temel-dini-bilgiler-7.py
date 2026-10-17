from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'TOPLUMA KARŞI AHLAKİ SORUMLULUKLARIMIZ: KUL HAKKI VE ADALET', R['koyu']))

    # Sol panel: Kul Hakkı, Kamu Hakkı ve Adalet
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KUL HAKKI, KAMU HAKKI VE ADALET', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'İslam Toplum Ahlakının Özü', '“Müslüman, elinden ve dilinden insanların emin olduğu kimsedir.”'),
        (150, 'Bireysel Kul Hakkı (Maddi ve Manevi)', 'Hırsızlık, borcu ödememek, gıybet, iftira ve alay etmek kul hakkıdır.'),
        (200, 'Müflis (İflas Etmiş Kimse) Hadisi', 'Kul hakkı yiyenin ahirette ibadet sevapları hak sahiplerine dağıtılır!'),
        (250, 'Kamu Hakkı (Beytülmal / Amme Hukuku)', 'Okul, park, su, elektrik ve vergide 85 milyon vatandaşın hakkı vardır.'),
        (300, 'Adalet ve Hakkaniyet (Nahl 90 / Nisâ 135)', 'Akrabamız aleyhine bile olsa doğruluktan ve adaletten şaşmamak.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Yardımlaşma, Komşuluk ve Emanet
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. YARDIMLAŞMA, KOMŞULUK VE EMANET', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'İyilik ve Takvada Yardımlaşma (Mâide 2)', 'Zekât, sadaka, infak ve karz-ı hasen (güzel borç) ile dayanışma.'),
        (150, 'Komşuluk Hukuku ve Duyarlılık', '“Komşusu açken tok yatan bizden değildir.” (Hadis-i Şerif)'),
        (200, 'Emanet Bilinci ve Liyakat (Nisâ 58)', 'Emanetleri ehline (işi en iyi yapabilecek uzman ve dürüst kişiye) vermek.'),
        (250, 'Ahde Vefa (Sözünde Durmak)', 'Verilen sözlere ve yapılan antlaşmalara sadık kalmak mümin özelliğidir.'),
        (300, 'Dürüst Ticaret (Mutaffifîn Suresi)', 'Ölçü ve tartıda hile yapmamak: “Bizi aldatan bizden değildir!”'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KUL HAKKINDAN KURTULMANIN ŞARTI: Haksızlığa son vermek + Zararı tazmin etmek + HAK SAHİBİYLE HELALLEŞMEK!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Yüce Allah kendisine karşı işlenen günahları tövbeyle affedebilir; ancak kul hakkını hak sahibi helal etmedikçe bağışlamaz.', '#334155', 10, 'normal', 'middle'))

    kaydet('8-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
