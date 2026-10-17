from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'ÖRNEK BİR ŞAHSİYET: HEZARFEN NECMEDDİN OKYAY VE İSLAM ESTETİĞİ', R['koyu']))

    # Sol panel: Hezarfen Necmeddin Okyay'ın Hayatı ve Sanatları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HEZARFEN NECMEDDİN OKYAY (1883-1976)', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Üsküdarlı Din Âlimi, Hafız ve Sanatkâr', 'Üsküdar Yeni Valide Camii’nde 40 yıl imam-hatiplik ve Güzel Sanatlar hocalığı.'),
        (150, 'Neden “Hezarfen” (Bin Sanatlı) Denmiştir?', 'Hat, ebru, cilt, okçuluk, gülcülük, mürekkepçilik gibi 10’dan fazla dalda üstat!'),
        (200, '“Necmeddin Ebrusu” (Çiçekli Ebru Mucidi)', 'Ebru sanatına lale, karanfil, gelincik ve sümbül motiflerini ilk kez kazandırdı.'),
        (250, 'Hüsn-i Hat (Talik/Celî) ve Tuğrakeşlik', 'Sami Efendi’nin öğrencisi; is mürekkebi ve aharlı kâğıt yapımının büyük ustası.'),
        (300, 'Gül Yetiştiriciliği (Toygar Tepesi Bahçesi)', '400’den fazla gül çeşidi yetiştirerek Peygamber sevgisini (gül-i Muhammedî) yaşattı.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: İslam Medeniyetinde Sanat, İhsan ve Hayatın Anlamı
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İSLAM MEDENİYETİNDE SANAT VE ESTETİK', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, '“Allah Güzeldir, Güzelliği Sever” (Hadis-i Şerif)', 'El-Cemîl, El-Bedî’ ve El-Musavvir isimlerinin insan elindeki estetik tezahürü.'),
        (150, 'İhsan ve İtkân Bilinci (İşi En Güzel Yapmak)', 'Her sanatı ve mesleği Allah’ın huzurundaymış gibi titizlikle icra etmek.'),
        (200, 'Sabır, Tevazu ve Usta-Çırak Geleneği (İcâzet)', 'Bilgi ve sanatın kuşaktan kuşağa edep ve sabırla aktarılması (Mustafa Düzgünman).'),
        (250, 'Çok Yönlülük ve Vaktin Kıymetini Bilmek', 'İbadet, ilim, sanat ve tabiat sevgisini tek bir ömürde uyumlu şekilde birleştirmek.'),
        (300, '1. Ünite (Hayatın Anlamı) ile Bağlantısı', 'İman ve kulluk bilincinin hayatı güzelleştiren somut bir medeniyet modelidir.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ANAHTAR BİLGİ: Farsça “Hezâr (1000)” + Arapça “Fen (Sanat/Bilim)” = HEZARFEN (Çok yönlü bilge ve sanatkâr)!', R['koyu'], 10.3, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Necmeddin Okyay, geleneksel Türk-İslam sanatlarını Osmanlı’dan Cumhuriyet kuşaklarına aktaran en önemli kültür köprüsüdür.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
