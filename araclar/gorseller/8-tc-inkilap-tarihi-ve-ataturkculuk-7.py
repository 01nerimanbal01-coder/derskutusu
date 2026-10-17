from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('tc-inkilap-tarihi-ve-ataturkculuk')
    ic = []
    ic.append(P.baslik(400, 32, 'MONDROS ATEŞKES ANTLAŞMASI (30 EKİM 1918) VE İŞGALLERE KARŞI TEPKİLER', R['koyu']))

    # Sol panel: I. Dünya Savaşı Sonu ve Mondros Ateşkes Antlaşması (7 ve 24. Maddeler)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. MONDROS ATEŞKES ANTLAŞMASI (30 EKİM 1918)', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Wilson İlkeleri (ABD) ve Ateşkes Çağrısı', '"Yenenler yenilenlerden toprak ve tazminat almayacak" vaadi.'),
        (150, '7. Madde (En Tehlikeli Madde — İşgal Hukuku)', '"İtilaf Devletleri güvenliklerini tehdit eden stratejik noktayı işgal edebilir."'),
        (200, '24. Madde (Vilâyât-ı Sitte — Doğu’da Ermeni Devleti)', 'Doğu’daki 6 ilde (Erzurum, Van, Bitlis, Sivas, Elazığ, Diyarbakır) karışıklık çıkarsa işgal!'),
        (250, 'Askerî ve Ekonomik Hükümler (Savunmasız Bırakma)', 'Ordu terhis edilecek, silah-cephane ve haberleşme (telgraf/demiryolu) teslim!'),
        (300, 'İlk İşgaller (Kasım 1918 - Mayıs 1919)', 'İlk işgal: Musul (İngiltere) | İzmir’in İşgali: 15 Mayıs 1919 (Yunanistan).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Mondros'a ve İşgallere Karşı Tutumlar (İstanbul Hükûmeti, Mustafa Kemal, Türk Halkı)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İŞGALLERE KARŞI TUTUM VE TEPKİLER', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '1. İstanbul Hükûmetinin Tutumu (Teslimiyetçi)', 'İşgalleri geçici saydı; halka "Sükûneti koruyun, direnmeyin" dedi.'),
        (150, '2. İtilaf Devletleri ve Azınlıkların Tutumu', '7. maddeye dayanarak Anadolu’yu işgal edip parçalamaya başladılar.'),
        (200, '3. Mustafa Kemal Paşa’nın Tutumu (Vatansever/Kararlı)', '"Geldikleri gibi giderler!" -> Bağımsızlık ve Millî Mücadele fikri.'),
        (250, '4. Türk Milletinin Tepkisi: Müdafaa-i Hukuk Cemiyetleri', 'Mitingler ve telgraflarla işgalleri protesto edip cemiyetler kurdu.'),
        (300, '5. Kuvâ-yı Milliye (Millî Kuvvetler) Ruhu', 'Halkın vatanı savunmak için kurduğu silahlı direniş birlikleri (İlk kurşun!).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'LGS ANAHTARI: 7. Madde = Anadolu’nun işgaline HUKUKİ ZEMİN hazırlamak | 24. Madde = Doğu Anadolu’da Ermeni devleti kurmak!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Haberleşme ve ulaşım ağlarına el konulmasının amacı: Türk milletinin işgalleri öğrenip birlikte örgütlenmesini engellemektir!', '#334155', 10.5, 'normal', 'middle'))

    kaydet('8-tc-inkilap-tarihi-ve-ataturkculuk-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
