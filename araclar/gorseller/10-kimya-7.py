from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kimya')
    ic = []
    ic.append(P.baslik(400, 32, 'MOL KAVRAMI: AKB-GRAM İLİŞKİSİ, İZOTOP KÜTLESİ VE FORMÜL HESAPLARI', R['koyu']))

    # Sol panel: AKB, Gerçek Atom Kütlesi ve Ortalama Atom Kütlesi
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. AKB, GERÇEK KÜTLE VE ORTALAMA ATOM KÜTLESİ', R['koyu'], 11.5, 'bold', 'middle'))

    sol = [
        (100, 'Atomik Kütle Birimi (1 akb / u) Tanımı', '1 tane ¹²C atomunun kütlesinin 1/12’sine 1 akb denir: 1 akb = 1 / N_A gram!'),
        (150, 'Gram ile akb Arasındaki Altın Dönüşüm!', '1 gram = N_A akb (6,02 × 10²³ akb)  <--->  1 akb = 1 / N_A gram.'),
        (200, '1 Tane Atom Kütlesi vs. 1 Mol Atom Kütlesi (O=16)', '1 tane O atomu = 16 akb = 16/N_A g  |  1 mol O atomu = 16 g = 16·N_A akb!'),
        (250, 'Gerçek Atom/Molekül Kütlesi Kavramı', '1 TANE atom veya molekülün GRAM cinsinden kütlesidir (M_A / N_A gram).'),
        (300, 'İzotoplar ve Ortalama Atom Kütlesi', 'Ort. A.K. = (m₁ · %Bolluk₁ + m₂ · %Bolluk₂) / 100 (Örn: Cl = 35,5).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Bileşiklerde Mol-Atom-Kütle ve Formül Problemleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. BİLEŞİKLERDE MOL ANALİZİ VE FORMÜL BULMA', '#92400e', 11.5, 'bold', 'middle'))

    sag = [
        (100, '1 Mol Bileşikteki Atomların Mol Sayısı', '1 mol C₃H₈ bileşiğinde: 3 mol C atomu + 8 mol H atomu = 11 mol atom vardır!'),
        (150, 'Bileşikte Kütlece Yüzde Bileşim', 'Kütlece % = (Elementin 1 mol bileşikteki kütlesi / Bileşiğin M_A’sı) × 100.'),
        (200, 'Basit (Kaba) Formül ve Molekül (Gerçek) Formülü', 'Elementlerin mol sayıları en küçük tam sayılara sadeleştirilirse basit formül bulunur.'),
        (250, 'Kristal Sulu (Hidrat) Bileşik Problemleri', 'CuSO₄·nH₂O ısıtılınca uçan suyun kütlesinden n katsayısı (mol oranı) bulunur.'),
        (300, 'Atom Kütlesi Bilinmeyen (X) Elementi Bulma', 'Verilen mol ve kütle (n = m / M_A) eşitliğinden önce bileşiğin M_A’sı, sonra X bulunur.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'TUZAK UYARISI (H₂O = 18 g/mol): “1 tane H₂O molekülü 18 gramdır” YANLIŞ! Doğrusu: “1 tane H₂O = 18 akb = 18/N_A gramdır!”', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '“0,2 mol SO₃ gazı kaç mol atom içerir?” -> 1 molde 4 mol atom varsa, 0,2 molde 0,2 × 4 = 0,8 mol atom vardır!', '#334155', 10, 'normal', 'middle'))

    kaydet('10-kimya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
