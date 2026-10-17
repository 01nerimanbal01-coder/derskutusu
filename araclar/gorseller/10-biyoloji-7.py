from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('biyoloji')
    ic = []
    ic.append(P.baslik(400, 32, 'KEMOSENTEZ VE CANLILARDA SİNDİRİM (HÜCRE İÇİ VE HÜCRE DIŞI)', R['koyu']))

    # Sol panel: Kemosentez (Işık Enerjisi Kullanılmadan Besin Sentezi)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KEMOSENTEZ: KİMYASAL ENERJİ İLE SENTEZ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Kemosentez Yapan Canlılar (Yalnızca Prokaryotlar!)', 'Bazı bakteriler (nitrit, nitrat, kükürt, demir) ve arkeler (metanojenler).'),
        (150, 'Enerji Kaynağı: İnorganik Madde Oksidasyonu!', 'NH₃, NO₂⁻, H₂S, Fe²⁺, H₂ gibi inorganikler oksitlenerek kimyasal enerji üretilir.'),
        (200, 'Klorofil Gerekmez — Gece ve Gündüz (24 Saat) Sürer!', 'Işık enerjisi kullanılmadığı için karanlıkta da kesintisiz besin sentezlenir.'),
        (250, 'Oksijen (O₂) Üretilir ancak Atmosfere Verilmez!', 'Üretilen O₂, canlının kendi inorganik maddesini oksitlemesinde kullanılır.'),
        (300, 'Ekolojik Önemi: Azot Döngüsü (Nitrifikasyon)', 'Amonyağı (NH₃) bitkilerin kullanabileceği nitrat (NO₃⁻) tuzlarına dönüştürür.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Sindirim Çeşitleri (Hücre İçi vs. Hücre Dışı Sindirim)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HÜCRE İÇİ VE HÜCRE DIŞI SİNDİRİM', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Sindirim (Hidroliz) Nedir? (ATP Harcanmaz!)', 'Polimerlerin su ve sindirim enzimleriyle monomerlere parçalanmasıdır.'),
        (150, 'Hücre İçi Sindirim (Lizozom Organeli İle)', 'Fagositoz/pinositozla alınan besin kofulunun lizozomla birleşmesi (Amip, Akyuvar).'),
        (200, 'Hücre Dışı Sindirim (Ekzositozla Enzim Salgılama)', 'Saprofitler, böcekçil bitkiler ve hayvanların sindirim boşluğunda gerçekleşir.'),
        (250, 'Neden Hücre Dışı Sindirim Daha Avantajlıdır?', 'Hücre zarından geçemeyecek kadar büyük besinlerden faydalanmayı sağlar!'),
        (300, 'Tek Açıklıklı vs. İki Açıklıklı Sindirim Sistemi', 'Hidra/Planarya: Tek açıklıklı (Gastrovasküler) | Toprak solucanı/Omurgalı: İki açıklıklı.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ UYARI: Hiçbir ÖKARYOT canlı kemosentez yapamaz! Kemosentez yalnızca bazı BAKTERİ ve ARKELERDE görülür!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hidroliz (sindirim) tepkimelerinde doğrudan ATP HARCANMAZ; ancak enzimlerin sentezi ve ekzositozla salgılanması sırasında ATP harcanır.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-biyoloji-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
