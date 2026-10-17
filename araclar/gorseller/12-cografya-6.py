from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('cografya')
    ic = []
    ic.append(P.baslik(400, 32, 'TÜRKİYE EKONOMİSİNDE HİZMET SEKTÖRÜ VE GELECEKTE ŞEHİR-EKONOMİ', R['koyu']))

    # Sol panel: Türkiye GSYH'sinde Hizmet Sektörünün Payı
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TÜRKİYE’DE HİZMET SEKTÖRÜNÜN YERİ', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Üçüncül Ekonomik Faaliyet: GSYH Payı ~%60+)', '#334155', 11, 'bold', 'middle'))

    alt_kollar = [
        (114, 'Ulaşım ve Lojistik', 'Doğu-Batı koridoru, Boğazlar, otoyollar, YHT ve limanlar'),
        (160, 'Ticaret (İç ve Dış Ticaret)', 'İstanbul, İzmir, Bursa, Gaziantep, Kayseri merkezleri'),
        (206, 'Turizm (“Bacası Tütmeyen Sanayi”)', 'Dış ticaret açığını kapatan en önemli döviz kaynağı'),
        (252, 'Eğitim, Sağlık ve Finans', 'Sağlık turizmi, İstanbul Finans Merkezi, üniversiteler'),
        (298, 'Bilişim ve İletişim (Dördüncül)', 'Teknoparklar, yazılım ihracatı, e-ticaret ekosistemi'),
    ]
    for y, b, a in alt_kollar:
        ic.append(P.kutu(35, y, 335, 38, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 30, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Gelecekte Şehir ve Ekonomi (Akıllı Şehirler & Dijital Ekonomi)
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. GELECEKTE ŞEHİR VE EKONOMİ EĞİLİMLERİ', '#1e40af', 13, 'bold', 'middle'))

    gelecek = [
        (102, 'Akıllı Şehirler (Smart Cities)', 'IoT sensörleri, akıllı ulaşım, sıfır atık ve enerji verimliliği'),
        (154, 'Dikey Tarım ve Sürdürülebilirlik', 'Gökdelen seralar, topraksız (hidroponik) tarım, yeşil çatılar'),
        (206, 'Endüstri 4.0 ve Karanlık Fabrikalar', 'Yapay zekâ, otonom robotlar, nesnelerin interneti (IoT)'),
        (258, 'Dijital Ekonomi ve Uzaktan Çalışma', 'E-ticaret, fintek, siber güvenlik, bulut bilişim meslekleri'),
    ]
    for y, b, a in gelecek:
        ic.append(P.kutu(415, y, 350, 44, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 34, a, '#334155', 10, 'normal', 'middle'))

    ic.append(P.kutu(415, 310, 350, 26, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 327, 'Cittaslow (Sakin Şehir): Seferihisar (İlk), Akyaka, Gökçeada, Şavşat...', '#92400e', 10, 'bold', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'CUMHURİYET’TEN GÜNÜMÜZE SEKTÖREL DÖNÜŞÜM: 1923’te Tarım 1. sıradayken → Günümüzde HİZMET (%60+) > SANAYİ (~%28) > TARIM (~%7)', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Bir ülkenin gelişmişliği arttıkça tarımın GSYH içindeki oransal payı azalır, hizmet ve sanayinin payı artar (Tarımsal üretim miktarı ise artar!).', '#334155', 10, 'normal', 'middle'))

    kaydet('12-cografya-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic