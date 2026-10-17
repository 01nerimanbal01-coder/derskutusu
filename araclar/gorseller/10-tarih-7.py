from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('tarih')
    ic = []
    ic.append(P.baslik(400, 32, 'TÜRKİSTAN’DAN TÜRKİYE’YE (1040-1299): EKONOMİ, BİLİM VE KÜLTÜR', R['koyu']))

    # Sol panel: Toprak Yönetimi (İkta), Ticaret ve Ahilik Teşkilatı
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TOPRAK SİSTEMİ, TİCARET VE AHİLİK', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Mîrî Arazi Anlayışı: Has, İkta, Mülk ve Vakıf', 'Toprağın mülkiyeti devlete (mîrî), işleme hakkı halka aittir.'),
        (150, 'İkta Sistemi (Nizâmülmülk) ve İkta Askerleri', 'Vergi geliriyle komutan/memur maaşı ödenir, atlı asker (sipahi) beslenir!'),
        (200, 'Ahîlik Teşkilatı (Ahi Evran ve Bacıyân-ı Rûm)', 'Esnaf dayanışması, mesleki eğitim, kalite-fiyat denetimi ve fütüvvet ahlakı.'),
        (250, 'Uluslararası Ticaret: Kervansaraylar ve Sigorta', 'Ribat/Kervansaraylarda 3 gün ücretsiz konaklama; dünyada ilk devlet sigortası!'),
        (300, 'Türkiye Selçuklularında Liman Fetihleri', 'Antalya, Sinop, Alanya (Alâiye) ve Suğdak’ın fethiyle deniz ticareti gelişti.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Bilim, Eğitim (Nizamiye Medreseleri), Dil ve Sanat
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. BİLİM, MEDRESELER, EDEBİYAT VE SANAT', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Nizâmiye Medreseleri (Bağdat - 1067) ve Anadolu', 'Büyük Selçuklu’da Nizâmiye; Anadolu’da Yağıbasan, Çifte Minareli, Gök Medrese.'),
        (150, 'Bilim İnsanları: Ömer Hayyam, Cezerî, Birûnî', 'Celâlî Takvimi (Ömer Hayyam), Sibernetik/Robotik öncüsü (El-Cezerî).'),
        (200, 'Anadolu’nun Manevi Mimarları (Mutasavvıflar)', 'Mevlânâ Celâleddîn-i Rûmî, Yunus Emre, Hacı Bektâş-ı Velî, Hoca Ahmed Yesevî.'),
        (250, 'Dil Politikası ve Karamanoğlu Mehmet Bey (1277)', 'Selçuklu’da bilim Arapça, edebiyat Farsça; 1277 Fermanı ile Türkçe resmi dil!'),
        (300, 'Selçuklu Mimarisi: Külliye, Kümbet ve Darüşşifa', 'Gevher Nesibe Darüşşifası (Kayseri - 1206), Divriği Ulu Camii ve Darüşşifası.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'İKTA SİSTEMİNİN 4 FAYDASI: 1) Üretimde süreklilik, 2) Hazineden para çıkmadan büyük ordu, 3) Göçebelerin yerleşikleşmesi, 4) Taşra güvenliği!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Vakıf arazilerinin geliri cami, medrese, darüşşifa (hastane) ve imarethane gibi sosyal kurumların ücretsiz hizmet vermesini sağlamıştır.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-tarih-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
