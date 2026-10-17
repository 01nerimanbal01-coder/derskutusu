from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('felsefe')
    ic = []
    ic.append(P.baslik(400, 32, 'TEKNOLOJİ VE HAYAT: ONTOLOJİK ANLAM KAYBI VE YABANCILAŞMA', R['koyu']))

    # Sol panel: Teknolojinin Doğası ve Felsefi Yaklaşımlar
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TEKNOLOJİNİN DOĞASI VE FELSEFESİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Tekhne (Zanaat/Beceri) ve Teknoloji', 'İnsanın doğayı dönüştürme bilgisi; araç olmaktan çıkıp yaşam dünyasını kuran güç.'),
        (150, 'Araçsalcı (Enstrümantalist) Yaklaşım', '“Teknoloji tarafsız bir araçtır; iyi ya da kötü olması insanın kullanım amacına bağlıdır.”'),
        (200, 'Özcü / Otonom Yaklaşım (Heidegger, Ellul)', '“Teknoloji sadece bir araç değildir; insanın varlığı algılama biçimini kökten değiştirir.”'),
        (250, 'Heidegger ve “Çerçeveleme (Gestell)”', 'Modern teknolojinin doğayı ve insanı sadece tüketilecek bir “rezerv/kaynak” olarak görmesi.'),
        (300, 'Fiziksel Gerçeklikten Sanal/Simüle Evrene', 'Dijitalleşme, yapay zekâ ve algoritmaların gerçek ile kurgu arasındaki sınırı bulanıklaştırması.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Ontolojik Anlam Kaybı ve Yabancılaşma
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ONTOLOJİK ANLAM KAYBI VE YABANCILAŞMA', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Ontolojik Anlam Kaybı Nedir?', 'Varlığın (doğanın ve insanın) içsel değerini yitirip salt hesaplanabilir veriye/nesneye indirgenmesi.'),
        (150, 'Baudrillard: Simülasyon ve Hipergerçeklik', 'Gerçeğin yerini kopyaların (simülakrların) alması; imajın hakikatten daha gerçek algılanması.'),
        (200, 'Yabancılaşma (Alienasyon) Kavramı', 'İnsanın kendi ürettiği teknolojik sistemlerin kölesi hâline gelerek özünden ve doğadan kopması.'),
        (250, 'Dijital Yalnızlaşma ve Yüzeyselleşme', 'Sürekli çevrim içi (bağlantıda) olmasına rağmen sahici insani ilişkilerden uzaklaşma.'),
        (300, 'Eleştirel ve Bilinçli Teknoloji Etiği', 'Teknolojiyi reddetmek yerine insan onurunu ve varoluşsal anlamı merkeze alan özne kalabilmek.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'HEIDEGGER’İN UYARISI: “Modern teknoloji nehrin üzerine hidroelektrik santrali kurduğunda, artık nehir santrale değil; nehir santralin çarkına kapatılmıştır!”', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Yabancılaşma: İnsanın kendi elleriyle ürettiği tekniğin özerk bir güç kazanarak insanı yönetmeye başlamasıdır.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-felsefe-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
