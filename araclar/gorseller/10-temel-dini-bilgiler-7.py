from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'TEMEL DİNİ BİLGİLER: HEZARFEN NECMEDDİN OKYAY VE HAYATIN ANLAMI', R['koyu']))

    # Sol panel: Hayatı ve Hezarfen Sanatları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HAYATI VE “HEZARFEN” SANATLARI', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Üsküdar’dan Yükselen Bir Âlim (1883-1976)', 'Hafız, kıraat âlimi ve Üsküdar Yeni Valide Camii’nde 40 yıllık imam-hatip.'),
        (150, 'Neden “Hezarfen” (Bin Sanatlı) Denildi?', 'Hat, ebru, klasik cilt, tuğrakeşlik, ahar, mürekkep, okçuluk ve gülcülük üstadı.'),
        (200, 'Necmeddin Ebrusu (Çiçekli Ebru)', 'Su yüzeyine lale, karanfil, sümbül, gelincik motiflerini kazandıran özgün üslup.'),
        (250, 'Kemankeşlik (Geleneksel Türk Okçuluğu)', 'Okçuluk icazeti alarak Okçular Tekkesi geleneğini yaşattı; “Okyay” soyadını aldı.'),
        (300, 'Şükûfeperverlik (Gül Yetiştiriciliği)', 'Toygar Tepesi’ndeki bahçesinde 400’den fazla gül çeşidi yetiştirerek ödüller aldı.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Hayatın Anlamı ve İman-Amel-Estetik Bütünlüğü
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İMAN, AMEL VE İSLAM ESTETİĞİ BÜTÜNLÜĞÜ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Hayatın Anlamı: İman ve Salih Amel', 'İnsan başıboş yaratılmamıştır; ömür kulluk, güzel ahlak ve üretimle anlam kazanır.'),
        (150, '“Allah Güzeldir, Güzelliği Sever” İlkesi', 'İslam sanatları Allah’ın el-Cemîl ve el-Bedî isimlerinin estetik tezahürüdür.'),
        (200, 'İhsan Şuuruyla Sanat İcrası', 'Her yazıyı, ebruyu ve cildi Allah’ın huzurundaymış gibi en mükemmel şekilde yapmak.'),
        (250, 'Cami Mihrabı ile Sanat Atölyesi Bütünlüğü', 'İbadet hayatı ile sanat, spor ve tabiat sevgisinin birbirini tamamlaması.'),
        (300, 'Sadaka-i Câriye ve Talebe Yetiştirme', 'Medresetü’l-Hattâtîn ve Akademi’de Uğur Derman, M. Düzgünman gibi ustalar yetiştirdi.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'Hezarfen Necmeddin Okyay; zamanı israf etmeyen, imanını sanat ve güzel ahlakla birleştiren örnek bir Müslüman şahsiyettir.', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Ünite 1 Özeti: Hayat; tevhid inancı, ihlaslı ibadet, ihsan bilinci ve insanlığa faydalı eserler bırakmakla gerçek anlamına ulaşır.', '#334155', 10, 'normal', 'middle'))

    kaydet('10-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
