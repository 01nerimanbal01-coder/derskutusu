from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('tc-inkilap-tarihi-ve-ataturkculuk')
    ic = []
    ic.append(P.baslik(400, 32, 'I. DÜNYA SAVAŞI’NIN SONUÇLARI VE MONDROS ATEŞKES ANTLAŞMASI', R['koyu']))

    # Sol panel: Wilson İlkeleri ve Savaşın Sonuçları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. WİLSON İLKELERİ VE SAVAŞIN SONUÇLARI', R['koyu'], 13, 'bold', 'middle'))
    sol_maddeler = [
        (98, 'Wilson İlkeleri (8 Ocak 1918)', '• Yenenler yenilenlerden toprak ve tazminat almayacak.'),
        (146, 'Self-Determinasyon İlkesi (Md. 12)', '• Türklerin çoğunlukta olduğu bölgelere egemenlik verilecek.'),
        (194, 'Paris Barış Konferansı (18 Ocak 1919)', '• İzmir İtalya’dan alınıp Yunanistan’a verildi (İlk görüş ayrılığı).'),
        (242, 'Manda ve Himaye Sistemi + Cemiyet-i Akvam', '• Sömürgecilik "Manda" kılıfına sokuldu; Milletler Cemiyeti kuruldu.'),
        (290, 'İmparatorlukların Yıkılması', '• Osmanlı, Avusturya-Macaristan, Rus ve Alman imp. yıkıldı.'),
    ]
    for y, b, a in sol_maddeler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Mondros Ateşkes Antlaşması (30 Ekim 1918)
    ic.append(P.kutu(400, 56, 380, 290, '#fef2f2', '#dc2626'))
    ic.append(P.metin(590, 80, '2. MONDROS ATEŞKES ANTLAŞMASI (30 EKİM 1918)', '#991b1b', 13, 'bold', 'middle'))
    ic.append(P.metin(590, 99, 'Limni Adası Mondros Limanı / Agamemnon Zırhlısı (Rauf Orbay - Calthorpe)', '#334155', 10, 'bold', 'middle'))

    ic.append(P.kutu(415, 112, 350, 68, '#ffffff', '#dc2626'))
    ic.append(P.metin(590, 130, '7. MADDE (En Tehlikeli / İşgallere Hukuki Zemin):', '#b91c1c', 11, 'bold', 'middle'))
    ic.append(P.metin(590, 148, '"İtilaf Devletleri, güvenliklerini tehdit edecek bir durum', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 164, 'ortaya çıkarsa herhangi bir stratejik noktayı işgal edebilecek."', '#334155', 10, 'bold', 'middle'))

    ic.append(P.kutu(415, 188, 350, 68, '#ffffff', '#dc2626'))
    ic.append(P.metin(590, 206, '24. MADDE (Doğu Anadolu’da Ermeni Devleti Planı):', '#b91c1c', 11, 'bold', 'middle'))
    ic.append(P.metin(590, 224, '"Vilâyât-ı Sitte’de (Altı Doğu İli: Erzurum, Van, Bitlis,', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 240, 'Diyarbakır, Harput, Sivas) karışıklık çıkarsa işgal edilecek."', '#334155', 10, 'bold', 'middle'))

    ic.append(P.kutu(415, 264, 350, 68, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 282, 'Askerî ve İletişim Kısıtlamaları (Savunmasız Bırakma):', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(590, 300, '• Boğazlar açılacak ve istihkâmlar İtilaf Devletlerine verilecek.', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 316, '• Osmanlı ordusu terhis edilecek; telgraf ve tünellere el konulacak.', '#334155', 10, 'normal', 'middle'))

    # Alt bant: İlk İşgaller
    ic.append(P.kutu(20, 360, 760, 48, '#f8fafc', R['orta']))
    ic.append(P.metin(400, 380, 'MONDROS SONRASI İLK İŞGAL: 3 Kasım 1918’de İngilizlerin MUSUL’u işgali | İLK DİRENİŞ (İlk Kurşun): Hatay / Dörtyol (19 Aralık 1918)', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Mustafa Kemal Paşa’nın 13 Kasım 1918’de İstanbul Boğazı’ndaki İtilaf donanmasına sözü: "Geldikleri gibi giderler!"', '#b91c1c', 11, 'bold', 'middle'))

    kaydet('12-tc-inkilap-tarihi-ve-ataturkculuk-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
