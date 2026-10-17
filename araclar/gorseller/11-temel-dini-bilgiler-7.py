from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'TEMEL DİNİ BİLGİLER: NECMEDDİN OKYAY’IN SANAT MİRASI VE HAYATIN ANLAMI', R['koyu']))

    # Sol panel: Necmeddin Okyay'ın Sanat Mirası ve Üstatlık Alanları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HEZARFEN SANAT MİRASI VE HOCA KİMLİĞİ', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'Hüsn-i Hat ve Celî Ta’lik Ustalığı', 'Sami Efendi ve Bakkal Arif Efendi’den icazet; sekiz ayrı yazı nev’inde üstün maharet.'),
        (150, 'Necmeddin Ebrusu ve Yazılı Ebru', 'Çiçekli ebru (lale, sümbül, karanfil) ve arapzamkı ile geliştirdiği “yazılı/akkâse ebru”.'),
        (200, 'Kitap Sanatları: Cilt, Ahar ve Mürekkep', 'Klasik Türk cildi, kağıt terbiyesi (ahar) ve dayanıklı is mürekkebi üretimi.'),
        (250, 'Medresetü’l-Hattâtîn ve Akademi Hocalığı', 'Mustafa Düzgünman, Uğur Derman, Ali Alparslan ve Emin Barın gibi ustaları yetiştirmesi.'),
        (300, 'Kemankeşlik (Okçuluk) ve Gül Yetiştiriciliği', 'Okçular Tekkesi geleneğinin ihyası ve Üsküdar’da 400 çeşit gül yetiştirme (Şükûfeperver).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: 1. Ünite Sentezi: Hayatın Anlamı ve İslam Estetiği
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HAYATIN ANLAMI VE İSLAM ESTETİĞİ SENTEZİ', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Varoluş Gayesi: Marifetullah ve Kulluk', 'İnsan başıboş bırakılmamıştır (Kıyâme, 36); yaratılış amacı Allah’ı tanımak ve kulluktur.'),
        (150, 'İman – Salih Amel – Güzel Ahlak Bütünlüğü', 'İmanın kalpte kök salıp ibadet, dürüstlük ve insanlığa faydalı eserlerle meyve vermesi.'),
        (200, 'İslam Estetiği: Tevhid ve Tenzih İlkesi', 'Sanat eserinin faniliği hatırlatıp sonsuz güzellik sahibi olan Allah’a (el-Cemîl) yöneltmesi.'),
        (250, 'İhsan Bilinci ve Zamanın Kıymeti', 'Her işi Allah’ın huzurundaymış gibi özenle yapmak ve ömür sermayesini israf etmemek.'),
        (300, 'Kültürel Mirasa Vefa (Sadaka-i Câriye)', 'Vefattan sonra da sevabı kesilmeyen faydalı ilim, sanat eseri ve hayırlı nesil bırakmak.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, '«إِنَّ اللّٰهَ جَمِيلٌ يُحِبُّ الْجَمَالَ» — “Şüphesiz Allah güzeldir, güzelliği sever.” (Müslim, Îmân, 147)', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Necmeddin Okyay, çiçekli ebrunun yanı sıra bir tekne içinde birden fazla hat yazısını barındıran “yazılı (akkâse) ebru”nun da mucididir!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic