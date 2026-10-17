from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'PEYGAMBERİMİZİN HAYATI: İSLAM DEVLETİ’NİN MERKEZİ OLARAK MEDİNE', R['koyu']))

    # Sol panel: Toplumsal, Hukuki ve İktisadi Kurumlaşma
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ANAYASAL, İDARİ VE İKTİSADİ KURUMLAŞMA', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'Muâhât (Ensar - Muhacir Kardeşliği)', 'Kan bağı yerine iman kardeşliğini esas alan sosyal dayanışma ve toplumsal kaynaşma.'),
        (150, 'Medine Sözleşmesi (Vesîkası - 47/52 Madde)', 'Tarihin ilk yazılı anayasası; Müslümanlar ve Yahudiler arasında vatandaşlık ve ortak savunma.'),
        (200, 'Yargı ve Hukuk Birliği', 'Anlaşmazlıklarda nihai merci olarak Allah ve Resûlü’nün (Hz. Muhammed’in) kabul edilmesi.'),
        (250, 'İlk Nüfus Sayımı (1500 Müslüman)', 'İdari ve askeri planlama amacıyla Medine’deki Müslümanların isim isim kaydedilmesi.'),
        (300, 'Medine İslam Çarşısı (Sûku’l-Medîne)', 'Benî Kaynukâ pazarına alternatif; vergisiz, tekel/spekülasyon ve faizden arınmış adil çarşı.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Güvenlik, Savunma ve Diplomatik Merkez Olarak Medine
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. GÜVENLİK, DİPLOMASİ VE EĞİTİM MERKEZİ', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Seriyye ve Gazvelerle Güvenlik Çemberi', 'Medine çevresindeki kabilelerle saldırmazlık antlaşmaları ve kervan yollarının denetimi.'),
        (150, 'Harem Bölgesi İlanı ve Çevre Koruma', 'Mekke gibi Medine’nin de “Harem” ilan edilmesi; ağaç kesmenin ve avlanmanın yasaklanması.'),
        (200, 'Mescid-i Nebevî ve Suffe Akademisi', 'Devlet yönetim merkezi, elçilerin kabul yeri ve Muallim-i İslam yetiştiren Suffe okulu.'),
        (250, 'İslam’a Davet Mektupları ve Elçiler', 'Hudeybiye sonrası Bizans, Sâsânî, Habeşistan ve Mısır hükümdarlarına gönderilen elçiler.'),
        (300, 'Heyetler Yılı (Senetü’l-Vüfûd - 9 H. / 631)', 'Arap Yarımadası’nın dört bir yanından gelen heyetlerle Medine’nin başkent kimliğinin zirvesi.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'MEDİNE MODELİ: Mescid + Suffe (İlim) + Muâhât (Sosyal Dayanışma) + Medine Vesîkası (Hukuk) + Medine Çarşısı (Bağımsız Ekonomi)!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Yesrib’i “Medînetü’n-Nebî”ye (Medeniyet Şehrine) dönüştüren bu adımlar, İslam Devleti’nin kurumsal temellerini oluşturmuştur.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
