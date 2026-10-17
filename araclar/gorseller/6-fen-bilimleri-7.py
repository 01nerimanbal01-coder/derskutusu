from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fen-bilimleri')
    ic = []
    ic.append(P.baslik(400, 32, 'SABİT SÜRATLİ / HIZLI HAREKET GRAFİKLERİ & ÜREME, BÜYÜME VE GELİŞME', R['koyu']))

    # Sol panel: Sabit Süratli ve Sabit Hızlı Hareket & Grafikler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SABİT SÜRATLİ VE SABİT HIZLI HAREKET', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, 'Sürat (Alınan Yol / Zaman) — Skaler', 'Sürat = Alınan Yol (x) ÷ Zaman (t)  |  Birim: m/s veya km/h'),
        (150, 'Hız (Yer Değiştirme / Zaman) — Yönlü', 'Sabit Hızlı Hareket: Hem büyüklük hem de YÖN değişmemeli!'),
        (200, 'Çembersel Pistte Dönen Araç Tuzağı', 'Eşit sürede eşit yol alırsa: SÜRATİ SABİT ama yön değiştiği için HIZI DEĞİŞKENDİR!'),
        (250, 'Yol - Zaman Grafiği (Doğrusal Artan)', 'Eşit zaman aralıklarında eşit yol artışı (ör. 1 s→10 m, 2 s→20 m).'),
        (300, 'Sürat - Zaman Grafiği (Yatay Düz Çizgi)', 'Zaman ilerledikçe sürat değeri sabit kalır (Altındaki alan = Yol).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Bitki ve Hayvanlarda Üreme, Büyüme ve Gelişmeye Giriş
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. CANLILARDA ÜREME ÇEŞİTLERİNE GİRİŞ', '#1e40af', 13, 'bold', 'middle'))

    sag = [
        (100, 'Üreme Nedir? (Neslin Devamı)', 'Yaşamak için şart değildir; NESLİN DEVAMI için şarttır!'),
        (150, '1. Eşeysiz Üreme (Tek Ata Canlı)', 'Üreme hücresi ve döllenme YOK; oluşan yavru atayla birebir aynıdır.'),
        (200, 'Eşeysiz Üreme Çeşitleri (4 Çeşit)', 'Bölünerek (Bakteri, Amip) • Tomurcuklanarak (Hidra, Bira mayası)'),
        (250, 'Rejenerasyon ve Vejetatif Üreme', 'Rejenerasyon (Denizyıldızı, Planarya) • Vejetatif (Çilek, Patates, Gül)'),
        (300, '2. Eşeyli Üreme (İki Ata - Kalıtsal Çeşitlilik)', 'Sperm + Yumurta → Döllenme → Zigot → Embriyo → Yavru Birey.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'YOL ÜÇGENİ: Alınan Yol (x) = Sürat (v) × Zaman (t)  |  Birim Çevirme: 1 m/s = 3,6 km/h  (10 m/s = 36 km/h, 20 m/s = 72 km/h)', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'DİKKAT: Kertenkelenin kopan kuyruğunu onarması üreme DEĞİL, yenilenmedir; Denizyıldızının kopan kolundan yeni birey oluşması ÜREMEDİR!', '#334155', 10, 'bold', 'middle'))

    kaydet('6-fen-bilimleri-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
