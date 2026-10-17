from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fizik')
    ic = []
    ic.append(P.baslik(400, 32, 'VEKTÖRLER: KARTEZYEN KOORDİNAT SİSTEMİ VE BİLEŞKE VEKTÖR (R)', R['koyu']))

    # Sol panel: Kartezyen Koordinat Sisteminde Vektör ve Özellikleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KARTEZYEN SİSTEMDE VEKTÖR VE ÖZELLİKLERİ', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, '2B (x, y) ve 3B (x, y, z) Kartezyen Gösterim', 'Başlangıcı orijin (0, 0) olan vektör uç nokta koordinatlarıyla A(x, y) yazılır.'),
        (150, 'Eşit Vektörler ve Zıt (Negatif) Vektörler', 'K = L (yön ve büyüklük aynı) | K = -M (büyüklük aynı, yön tam zıt: 180°).'),
        (200, 'Bir Vektörün Skaler (Gerçek Sayı) ile Çarpımı', 'k > 0 ise yön değişmez | k < 0 ise yön 180° döner; büyüklük |k| katına çıkar.'),
        (250, 'Vektörlerin Taşınabilirliği İlkesi', 'Doğrultusu, yönü ve büyüklüğü korunarak vektör uzayda paralel taşınabilir.'),
        (300, 'Vektörün Dik Bileşenlerine Ayrılması (Ax, Ay)', 'Ax = A · cosθ (yatay bileşen)  |  Ay = A · sinθ (düşey bileşen).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Vektörlerin Toplanması (Bileşke Vektör R)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. BİLEŞKE VEKTÖR (R = A + B) YÖNTEMLERİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, '1. Uç Uca Ekleme (Çokgen) Yöntemi', 'Birinin bitişine diğerinin başlangıcı eklenir; ilk başlangıçtan son uca R çizilir.'),
        (150, '2. Paralelkenar Yöntemi', 'Başlangıç noktaları birleştirilir; paralelkenarın ortak köşeden çıkan köşegeni R’dir.'),
        (200, 'Aynı Yönlü (0°) ve Zıt Yönlü (180°) Vektörler', 'θ = 0° ise R_max = A + B  |  θ = 180° ise R_min = |A - B|.'),
        (250, 'Dik Vektörler (θ = 90° — Pisagor Bağıntısı)', 'A ⊥ B ise bileşke karesi: R² = A² + B² (Örn: 3-4-5, 6-8-10, 5-12-13).'),
        (300, 'Eşit Büyüklükteki İki Vektörün Özel Açıları (A = B)', 'θ = 0° ise R = 2A | θ = 60° ise R² = 3A² | θ = 90° ise R² = 2A² | θ = 120° ise R = A!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ KURAL: İki vektörün bileşkesinin büyüklüğü daima |A - B| ≤ R ≤ A + B aralığındadır; açı büyüdükçe R küçülür!', R['koyu'], 10.3, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Vektör çıkarmada A - B = A + (-B) eşitliği kullanılır; yani çıkan vektör (B) ters çevrilip A ile toplanır.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-fizik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
