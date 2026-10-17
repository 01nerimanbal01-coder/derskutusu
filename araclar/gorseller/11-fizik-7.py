from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fizik')
    ic = []
    ic.append(P.baslik(400, 32, 'NEWTON YASALARI UYGULAMALARI: SÜRTÜNME, EĞİK DÜZLEM VE BAĞLI SİSTEMLER', R['koyu']))

    # Sol panel: Sürtünme Kuvveti ve Eğik Düzlem Dinamiği
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SÜRTÜNME KUVVETİ VE EĞİK DÜZLEM', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Statik ve Kinetik Sürtünme Kuvveti', 'f_s,max = k_s · N ve f_k = k_k · N (k_s > k_k). Cisim dururken f_s <= f_s,max değerini alır!'),
        (150, 'Yatay ve Düşey Yüzeyde Tepki Kuvveti (N)', 'Yatayda N = m·g ± F_y; düşey duvara bastırılan cisimde ise N = F_yatay olur.'),
        (200, 'Eğik Düzlemde Ağırlığın Bileşenleri', 'Paralel bileşen: G_x = m·g·sin(a)  |  Yüzeye dik bileşen: G_y = N = m·g·cos(a).'),
        (250, 'Sürtünmesiz Eğik Düzlem İvmesi', 'F_net = m·g·sin(a) = m·a  =>  a = g · sin(a) (İvme kütleden BAĞIMSIZDIR!).'),
        (300, 'Sürtünmeli Eğik Düzlemde Hareket', 'Aşağı kayarken: a = g·(sin(a) - k·cos(a)); yukarı fırlatılırsa: a = g·(sin(a) + k·cos(a)).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Bağlı Cisimler, Atwood Düzeneği ve Üst Üste Cisimler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. BAĞLI SİSTEMLER VE İP GERİLMELERİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Sistem Yaklaşımı ve Ortak İvme', 'a_sistem = F_net(sistem) / m_toplam. Sonra tek bir kütleye serbest cisim diyagramı uygulanır.'),
        (150, 'İple Bağlı Yan Yana Cisimlerde Oran', 'Yatay düzlemde sürtünmesiz veya aynı k’lı sistemde ip gerilmeleri kütlelerle doğru orantılıdır.'),
        (200, 'Atwood Düzeneği (Sabit Makarada İki Kütle)', 'm_1 > m_2 ise: a = ((m_1 - m_2) · g) / (m_1 + m_2) ve T = (2·m_1·m_2·g) / (m_1 + m_2).'),
        (250, 'Masadan Sarkan Kütle Düzeneği', 'Sürtünmesiz masada m_1, sarkanda m_2 varsa: a = (m_2 · g) / (m_1 + m_2) ve T = m_1 · a.'),
        (300, 'Asansör İçinde Eylemsizlik Algısı (Görünür Ağırlık)', 'Yukarı hızlanan/aşağı yavaşlayan asansörde T = m·(g + a); tersinde T = m·(g - a).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: Duran bir cisme uygulanan kuvvet F < f_s,max ise cisim HAREKET ETMEZ ve statik sürtünme kuvveti f_s = F olur (f_s,max olmaz)!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'İki aşamalı çözüm: 1) Tüm sistem için F_net = m_toplam · a yazıp ivmeyi bul, 2) Tek bir kütleyi izole edip ip gerilmesini (T) hesapla!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-fizik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic