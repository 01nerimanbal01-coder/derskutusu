from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'PEYGAMBERİMİZİN ÇOCUKLUĞU: SÜTANNE HZ. HALİME VE BEREKET YILLARI', R['koyu']))

    # Sol panel: Mekke Geleneği ve Sütanneye Veriliş Sebepleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SÜTANNEYE VERİLİŞ SEBEPLERİ VE KİŞİLER', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, 'Neden Çöl/Yayla Köylerine Gönderilirdi?', '1. Mekke’nin sıcak ve salgın hastalıklı havasından korumak,'),
        (148, 'Fasih Arapça ve Sağlıklı Büyüme', '2. Öz ve düzgün (fasih) Arapçayı yerinde öğrenmelerini sağlamak.'),
        (196, 'İlk Emzirenler', 'Önce annesi Hz. Âmine, ardından Ebû Leheb’in cariyesi Süveybe.'),
        (244, 'Sütannesi: Hz. Halîme (Sa’d Kabilesi)', 'Hevâzin kolundan Benî Sa’d yurdu (Tâif yakınlarındaki yayla).'),
        (292, 'Sütbabası ve Sütkardeşleri', 'Sütbabası: Hâris | Sütkardeşleri: Abdullah, Üneyse ve Şeymâ.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Hz. Halime'nin Evindeki Bereket ve Çocukluk Yılları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SA’D YURDUNDAKİ BEREKET VE DEĞERLER', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, 'Hz. Halîme’nin Yetim Bebeği Seçmesi', 'Kimse yetim diye almazken Halîme şefkatle onu kucağına aldı.'),
        (150, 'Ev ve Sürülerdeki İlahi Bereket', 'Cılız binekleri hızlandı, kurak yurtta koyunları bol süt verdi!'),
        (200, 'Sa’d Yurdunda Geçen 4 Yıl', 'Doğa içinde sağlıklı, cesur, cömert ve fasih dilli büyüdü.'),
        (250, 'Sütkardeşleriyle Örnek İlişkisi', 'Kardeşlerinin hakkını gözetti; Şeymâ ona bakıcılık yaptı.'),
        (300, 'Ahde Vefa Örneği (Huneyn Sonrası)', 'Yıllar sonra sütkardeşi Şeymâ’ya cübbesini serip ikramda bulundu!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KRONOLOJİ: Doğum (571) → 0-4 Yaş: Sütannesi Hz. Halîme (Benî Sa’d Yurdu) → 4-6 Yaş: Annesi Hz. Âmine’nin Yanı', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Değerlerimiz: Yetimi koruma, misafirperverlik, kanaatkârlık, kardeşlik ve büyüklerimize/iyilik yapanlara vefa!', '#334155', 11, 'normal', 'middle'))

    kaydet('5-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
