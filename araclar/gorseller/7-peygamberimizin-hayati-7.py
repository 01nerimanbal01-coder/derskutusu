from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'YENİ YURT ARAYIŞI: AKABE BİATLARI VE MUS’AB BİN UMEYR (r.a.)', R['koyu']))

    # Sol panel: Yeni Yurt Arayışı ve Birinci Akabe Biatı (621)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. YENİ YURT ARAYIŞI VE I. AKABE BİATI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Neden Yeni Yurt Arayışı Başladı?', 'Mekke’de boykot, Hüzün Yılı ve Taif sonrası baskıların artması.'),
        (150, '620 Yılı: Akabe’de 6 Yesribli (Medineli) İle İlk Görüşme', 'Hac mevsiminde Hazrec kabilesinden 6 kişi Müslüman oldu.'),
        (200, '621 Yılı: Birinci Akabe Biatı (12 Kişi)', 'Allah’a ortak koşmama, çalmama, iftira etmeme, iyilikte itaat sözü.'),
        (250, 'İslam’ın İlk Öğretmeni: Mus’ab bin Umeyr (r.a.)', 'Peygamberimiz tarafından Medine’ye Kur’an öğretmeni gönderildi.'),
        (300, 'Medine’de İslam’ın Hızla Yayılması', 'Mus’ab’ın güzel ahlakıyla Evs ve Hazrec kabileleri İslam’la buluştu.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: İkinci Akabe Biatı (622) ve Sonuçları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. II. AKABE BİATI (622) VE HİCRETE HAZIRLIK', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '622 Yılı: İkinci Akabe Biatı (73 Erkek + 2 Kadın = 75 Kişi)', 'Medineli Müslümanlar Peygamberimizi Medine’ye davet etti!'),
        (150, 'İkinci Akabe Biatı’ndaki Koruma Sözü', '"Seni kendi canımızı ve ailemizi koruduğumuz gibi koruyacağız!"'),
        (200, '12 Temsilci (Nakîb) Seçimi', 'Peygamberimiz Medineli kabileler arasından 12 temsilci (nakîb) seçti.'),
        (250, 'Akabe Biatlarının Tarihi Sonucu', 'Yesrib (Medine) İslam’ın yeni yurdu oldu ve HİCRET yolu açıldı!'),
        (300, 'Ensar ve Muhacir Kardeşliğinin Temeli', 'Medineli yardımcılar (Ensar), Mekkeli göçmenlere (Muhacir) kucak açtı.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KRONOLOJİ: 620 İlk Görüşme (6 kişi) -> 621 I. Akabe Biatı (12 kişi + Mus’ab) -> 622 II. Akabe Biatı (75 kişi -> Hicret)!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Biat: Peygamberimize bağlılık ve itaat sözü vermek | Mus’ab bin Umeyr: İslam’ın Medine’deki ilk muallimi (öğretmeni).', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
