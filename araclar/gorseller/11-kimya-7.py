from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kimya')
    ic = []
    ic.append(P.baslik(400, 32, 'KİMYASAL TEPKİMELERDE HIZ: ÇARPIŞMA TEORİSİ VE AKTİVASYON ENERJİSİ', R['koyu']))

    # Sol panel: Çarpışma Teorisi ve Etkin Çarpışma Şartları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ÇARPIŞMA TEORİSİ VE ETKİN ÇARPIŞMA', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Çarpışma Teorisinin Temel İlkesi', 'Kimyasal tepkimenin gerçekleşmesi için reaktif tanecikleri birbiriyle çarpışmalıdır.'),
        (150, 'Etkin (Ürünle Sonuçlanan) Çarpışma', 'Her çarpışma ürüne dönüşmez; yalnızca ETKİN ÇARPIŞMALAR kimyasal tepkimeyle sonuçlanır.'),
        (200, 'Şart 1: Uygun Geometrik Doğrultu ve Yön', 'Atomların bağ kuracak orbitalleri uygun doğrultuda ve zıt yönlü çarpışmalıdır.'),
        (250, 'Şart 2: Yeterli Kinetik Enerji (E >= E_a)', 'Çarpışan taneciklerin toplam kinetik enerjisi eşik enerjisini (E_a) aşmalıdır.'),
        (300, 'Aktifleşmiş Kompleks (Geçiş Hâli)', 'En yüksek potansiyel enerjili, kararsız ara durumdur; ürüne veya girenlere dönüşebilir.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Aktivasyon Enerjisi (E_a) ve Potansiyel Enerji Diyagramları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. AKTİVASYON ENERJİSİ VE PE DİYAGRAMLARI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Aktivasyon (Eşik) Enerjisi (E_a) Özellikleri', 'Daima POZİTİFTİR (E_a > 0). Sıcaklıkla değişmez, yalnız katalizörle düşürülebilir!'),
        (150, 'İleri ve Geri Aktivasyon Enerjisi', 'E_ai = PE(Aktifleşmiş Kompleks) - PE(Girenler)  |  E_ag = PE(AK) - PE(Ürünler).'),
        (200, 'Tepkime Entalpisi (ΔH) ile İlişkisi', 'ΔH = E_ai - E_ag = PE(Ürünler) - PE(Girenler) bağıntısı her zaman geçerlidir!'),
        (250, 'Endotermik Tepkimede (ΔH > 0) Karşılaştırma', 'E_ai > E_ag ve PE(Ürünler) > PE(Girenler). Düşük sıcaklıkta girenler daha kararlıdır.'),
        (300, 'Ekzotermik Tepkimede (ΔH < 0) Karşılaştırma', 'E_ai < E_ag ve PE(Ürünler) < PE(Girenler). E_a büyüdükçe tepkime hızı YAVAŞLAR!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN FORMÜL: ΔH = E_ai - E_ag   (Dikkat: Ürünler - Girenler yazarken PE kullanılır; E_a kullanırken İLERİ eksi GERİ yazılır!)', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Eşik enerjisi (E_a) ne kadar KÜÇÜK ise o engeli aşabilen tanecik sayısı o kadar fazladır ve tepkime o kadar HIZLIDIR!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-kimya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
