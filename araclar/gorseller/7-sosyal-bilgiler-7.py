from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('sosyal-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'KÜRESELLEŞMENİN İNSAN VE TOPLUM HAYATINA ETKİSİ', R['koyu']))

    # Sol panel: Küreselleşmenin Boyutları ve Olumlu Etkileri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KÜRESELLEŞME VE OLUMLU ETKİLERİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Küreselleşme ("Küresel Köy") Nedir?', 'İletişim ve ulaşımla dünyanın tek bir pazar ve köy gibi bütünleşmesi.'),
        (150, '1. Bilgi ve İletişim Boyutu', 'Bilime, habere ve eğitime saniyeler içinde küresel erişim.'),
        (200, '2. Ekonomik ve Ticari Boyut', 'E-ticaret, uluslararası üretim zincirleri ve ürün çeşitliliği.'),
        (250, '3. Kültürel Etkileşim ve Dayanışma', 'Farklı kültürleri tanıma; afet ve krizlerde uluslararası yardım.'),
        (300, '4. Küresel Sorunlara Ortak Çözüm', 'İklim değişikliği ve salgınlara karşı uluslararası iş birliği.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Küreselleşmenin Riskleri ve Millî Kültürün Korunması
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. RİSKLER, KÜRESEL SORUNLAR VE ÇÖZÜMLER', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '1. Kültürel Tek Tipleşme (Popüler Kültür)', 'Giyim, yemek (fast-food) ve dilde yerel değerlerin aşınması.'),
        (150, '2. Tüketim Çılgınlığı ve İsraf', 'Reklamlarla "ihtiyaç olmadan satın alma" alışkanlığı ve atık artışı.'),
        (200, '3. Küresel İklim Değişikliği ve Çevre', 'Fosil yakıtlar, sera gazı salımı, kuraklık ve biyoçeşitlilik kaybı.'),
        (250, '4. Dijital Bağımlılık ve Yabancılaşma', 'Aile içi yüz yüze iletişimin azalması ve siber güvenlik riskleri.'),
        (300, 'Çözüm: "Küresel Düşün, Millî ve Yerel Kal!"', 'Türkçemizi, geleneklerimizi ve yerli üretimi koruyarak dünyaya açılmak.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DENGE İLKESİ: Bilim ve teknolojide evrensel gelişmeleri takip ederken millî kültür ve kimliğimizi korumalıyız!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Küresel sorunlar (iklim krizi, açlık, göç, salgınlar) sınır tanımaz; çözümü de uluslararası dayanışma ve bireysel sorumluluk gerektirir.', '#334155', 10, 'normal', 'middle'))

    kaydet('7-sosyal-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
