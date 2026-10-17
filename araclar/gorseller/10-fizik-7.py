from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fizik')
    ic = []
    ic.append(P.baslik(400, 32, 'BİR BOYUTTA SABİT İVMELİ HAREKET: SERBEST DÜŞME (a = g)', R['koyu']))

    # Sol panel: Serbest Düşme Hareketi ve Matematiksel Modeller
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SERBEST DÜŞME VE HAREKET DENKLEMLERİ', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Serbest Düşme Nedir? (Hava Direnci İhmal)', 'İlk hızsız (v₀ = 0) bırakılan cismin yer çekimi ivmesiyle (g) düşey hareketi.'),
        (150, 'Yer Çekimi İvmesi (g ≈ 10 m/s² veya 9,8 m/s²)', 'Hava sürtünmesi yoksa ivme KÜTLEDEN BAĞIMSIZDIR; her cisim aynı ivmeyle düşer!'),
        (200, 'Her Saniye Hız Değişimi: v = g · t', 't = 1 s -> v = 10 m/s | t = 2 s -> v = 20 m/s | t = 3 s -> v = 30 m/s.'),
        (250, 'Alınan Düşey Yol (Yükseklik): h = ½ · g · t²', 't = 1 s -> h = 5 m | t = 2 s -> h = 20 m | t = 3 s -> h = 45 m | t = 4 s -> 80 m.'),
        (300, 'Zamansız Hız Denklemi: v² = 2 · g · h', 'Süre (t) verilmeden düşme yüksekliği (h) ile yere çarpma hızı (v) arasındaki bağ.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: 5-15-25-35m Pratiği ve Hareket Grafikleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. PRATİK KURALLAR (h - 3h - 5h) VE GRAFİKLER', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Ardışık Saniyelerde Alınan Yollar (g = 10 m/s²)', '1. sn: 5 m | 2. sn: 15 m | 3. sn: 25 m | 4. sn: 35 m | 5. sn: 45 m!'),
        (150, 'Galileo Tek Sayılar Kuralı: h, 3h, 5h, 7h...', 'Eşit zaman aralıklarında (t) alınan düşey yollar tek sayılarla orantılı artar.'),
        (200, 'İvme-Zaman (a-t) Grafiği (Aşağı Yön - Seçilirse)', 'İvme sabit ve a = -g = -10 m/s²; altında kalan alan hız değişimini (-g·t) verir.'),
        (250, 'Hız-Zaman (v-t) Grafiği', 'Orijinden başlayan doğrusal grafik; altında kalan üçgen alan yer değiştirmeyi verir.'),
        (300, 'Konum-Zaman (y-t) Grafiği (Parabolik)', 'Eğimi (hızı) her saniye artan parabolik eğri (h = ½gt²).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: Havası boşaltılmış (vakum) ortamda aynı yükseklikten bırakılan demir bilye ile kuş tüyü AYNI ANDA ve AYNI HIZLA yere çarpar!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '“3. saniye sonunda toplam kaç m düştü?” -> h = 5·3² = 45 m | “3. saniye İÇİNDE kaç m düştü?” -> 25 m (5 - 15 - 25)!', '#334155', 10, 'normal', 'middle'))

    kaydet('10-fizik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
