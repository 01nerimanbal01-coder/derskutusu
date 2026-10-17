from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turkce')
    ic = []
    ic.append(P.baslik(400, 32, 'BAYRAĞIMIZIN ALTINDA: ŞİİRDE ANLAM, SÖZ SANATLARI VE FİİLLERDE KİP', R['koyu']))

    # Sol panel: Şiir Bilgisi ve Söz Sanatları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ŞİİRDE ANLAM VE SÖZ SANATLARI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Şiirde Tema ve Ana Duygu', 'Bayrak sevgisi, bağımsızlık tutkusu, vatan ve şehitlik bilinci.'),
        (150, 'Benzetme (Teşbih) Sanatı', 'Aralarında ilgi bulunan iki varlıktan zayıfı güçlüye benzetme ("al bayrak").'),
        (200, 'Kişileştirme (Teşhis) ve Konuşturma (İntak)', 'İnsan özelliğini doğaya verme ("Dalgalan sen de şafaklar gibi ey şanlı hilal").'),
        (250, 'Abartma (Mübalağa)', 'Bir durumu olduğundan çok büyük veya çok küçük gösterme ("Bir ah çeksem dağı taşı eritir").'),
        (300, 'Karşıtlık (Tezat)', 'Birbirine zıt kavram ve durumları bir arada kullanma ("ağlamak-gülmek", "gece-gündüz").'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Fiillerde Kip (Haber ve Dilek Kipleri) ve Anlam Kayması
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ÇEKİMLİ FİİLLERDE KİP VE ANLAM KAYMASI', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'Haber (Bildirme) Kipleri — Zaman Bildirir (5)', 'Bilinen (-dı), Duyulan (-mış), Şimdiki (-yor), Gelecek (-ecek), Geniş (-r).'),
        (150, 'Dilek (Tasarlama) Kipleri — Zaman Bildirmez (4)', 'Gereklilik (-meli), Şart (-se), İstek (-e), Emir (eki yok).'),
        (200, 'Çekimli Fiil Formülü', 'Fiil Kök/Gövdesi + Kip Eki + Kişi (Şahıs) Eki -> "dalgalan-ıyor-uz".'),
        (250, 'Fiillerde Anlam (Zaman/Kip) Kayması', 'Bir kip ekinin başka bir kip ekinin yerine kullanılmasıdır.'),
        (300, 'Anlam Kayması Örneği', '"Yarın Ankara’ya gidiyorum." (-yor şekilce şimdiki, anlamca gelecek zaman!).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: Her İNTAK (konuşturma) sanatında aynı zamanda TEŞHİS (kişileştirme) vardır; ancak her teşhiste intak yoktur!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Haber kipleri eylemin NE ZAMAN yapıldığını bildirir; Dilek kipleri ise dilek, şart, istek, gereklilik ve emir tasarlar.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-turkce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
