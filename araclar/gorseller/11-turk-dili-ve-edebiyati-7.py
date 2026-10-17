from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('edebiyat')
    ic = []
    ic.append(P.baslik(400, 32, '1. TEMA: BİR DİYECEĞİM VAR! — TARTIŞMACI ANLATIM VE SUNUM İLKELERİ', R['koyu']))

    # Sol panel: Tartışmacı ve Açıklayıcı Anlatım ile Düşünceyi Geliştirme Yolları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ANLATIM BİÇİMLERİ VE DÜŞÜNCE YOLLARI', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Tartışmacı Anlatım (Tez - Antitez - Sentez)', 'Karşıt bir görüşü çürütüp kendi tezini kanıtlama ve okuru/dinleyiciyi ikna etme amacı taşır.'),
        (150, 'Açıklayıcı ve Kanıtlayıcı Üslup', 'Nesnel bilgi verme, kavramsal netlik ve mantıksal tutarlılık ön plandadır.'),
        (200, 'Tanımlama, Örneklendirme ve Karşılaştırma', 'Soyut kavramları tanımlama, somut örnekler verme ve benzerlik/farklılıkları kıyaslama.'),
        (250, 'Tanık Gösterme (Alıntı Yapma)', 'Alanında uzman bir kişinin adını ve doğrudan sözünü (tırnak içinde) kanıt olarak kullanma.'),
        (300, 'Sayısal Verilerden Yararlanma ve Benzetme', 'İstatistiksel verilerle güvenilirliği artırma; güçlü-zayıf unsurlar arasında ilgi kurma.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Sözlü İletişim (Konuşma/Sunum) ve Çok Modlu Metin Üretimi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İKNA EDİCİ KONUŞMA VE YAZMA SÜRECİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Retorik Üçlüsü: Ethos, Pathos, Logos', 'Ethos (Güvenilirlik), Pathos (Duygusal bağ), Logos (Mantıksal kanıt ve veriler).'),
        (150, 'Planlı Yazma ve Konuşma Aşamaları', 'Hazırlık -> Planlama (Giriş-Gelişme-Sonuç) -> Taslak Üretimi -> Gözden Geçirme -> Sunum.'),
        (200, 'Çok Modlu Sunum Tasarımı İlkeleri', 'Sözel metin, görsel/grafik ve işitsel vurgunun bilgi yükü oluşturmadan uyumlu kullanımı.'),
        (250, 'Sözlü Sunumda Boğumlama, Vurgu ve Beden Dili', 'Akıcı diksiyon, göz teması, jest-mimik uyumu ve zaman yönetimi.'),
        (300, 'İletişim Etiği ve Kaynak Gösterme', 'Dezenformasyondan kaçınma, karşı fikirlere nezaket ve akademik dürüstlük (atıf).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ FARK: Yalnızca bir yazarın veya uzmanın adını anmak “Örneklendirme”dir; uzman kişinin SÖZÜNE de yer vermek “Tanık Gösterme”dir!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '“Bir Diyeceğim Var!” temasında amaç; toplumsal ve kültürel bir meselede kanıtlara dayalı, tutarlı ve ikna edici söz/metin üretmektir.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-turk-dili-ve-edebiyati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
