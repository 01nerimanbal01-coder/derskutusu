from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('felsefe')
    ic = []
    ic.append(P.baslik(400, 32, 'MANTIK VE ARGÜMANTASYON: AKIL YÜRÜTME TÜRLERİ VE SAFSATALAR', R['koyu']))

    # Sol panel: Argümantasyonun Yapısı ve 3 Temel Akıl Yürütme Türü
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ARGÜMAN YAPISI VE AKIL YÜRÜTME TÜRLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Argüman Yapısı: Öncül(ler) + Sonuç Önermesi', 'Gerekçe sunan önermelere ÖNCÜL, savunulan iddiaya SONUÇ denir.'),
        (150, 'Öncül ve Sonuç Belirteçleri (İpuçları)', 'Öncül: çünkü, zira, için | Sonuç: o hâlde, dolayısıyla, demek ki, sonuç olarak.'),
        (200, '1. Tümdengelim (Dedüksiyon): Bütünden Parçaya', 'Genel/tümel öncüllerden zorunlu özel sonuç çıkarma (Öncüller doğruysa sonuç kesin!).'),
        (250, '2. Tümevarım (Endüksiyon): Parçadan Bütüne', 'Tekil gözlemlerden genel yargıya ulaşma (Sonuç olasılıklıdır, yeni gözlemle değişebilir).'),
        (300, '3. Analoji (Benzeşim): Tekilden Tekile', 'İki varlık arasındaki ortak benzerlikten yola çıkarak biri için geçerli olanı diğerine aktarma.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Geçerlilik-Sağlamlık ve Enformel Mantık Yanlışları (Safsatalar)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SAĞLAM ARGÜMAN VE SAFSATALAR (MANTIK HATALARI)', '#92400e', 11.2, 'bold', 'middle'))

    sag = [
        (100, 'Geçerli Argüman vs. Sağlam (İyi) Argüman', 'Geçerlilik: Biçimsel zorunluluk | Sağlamlık: Geçerli yapı + DOĞRU öncüller!'),
        (150, 'Kişiye Saldırı (Ad Hominem) ve Sen de (Tu Quoque)', 'Fikri çürütmek yerine kişinin karakterine/dış görünüşüne saldırma safsatası.'),
        (200, 'Otoriteye, Çoğunluğa ve Duyguya Başvurma', '“Herkes böyle diyor (Ad Populum)” veya acındırma/korkutma ile ikna çabası.'),
        (250, 'Korkuluk (Saman Adam) ve İkilem (Sahte İkilem)', 'Rakibin görüşünü çarpıtıp saldırma (korkuluk); sadece 2 uç seçenek sunma.'),
        (300, 'Kısır Döngü (Döngüsel Kanıt) ve Acele Genelleme', 'İspat edilecek sonucu öncül olarak kullanma; yetersiz örnekle genelleme yapma.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ FARK: Önermeler “Doğru veya Yanlış” olur; Argümanlar (Çıkarımlar) ise “Geçerli veya Geçersiz / Sağlam” olur!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Bir argümanın SAĞLAM (güçlü) olması için hem akıl yürütme biçiminin GEÇERLİ olması hem de öncüllerinin gerçeğe uygun (DOĞRU) olması şarttır.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-felsefe-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
