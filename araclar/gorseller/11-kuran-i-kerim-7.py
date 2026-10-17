from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'TECVİT KURALLARI: KALKALE HÜKMÜ VE ÇEŞİTLERİ (قُطْبُ جَدٍّ)', R['koyu']))

    # Sol panel: Kalkalenin Tanımı ve 5 Kalkale Harfi
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KALKALE TANIMI VE HARFLERİ (قُطْبُ جَدٍّ)', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Kalkale Nedir? (Sözlük ve Tecvit Anlamı)', 'Sarsmak, kımıldatmak; sakin harfin mahrecinde kuvvetli bir ses yankısı/vurguyla okunması.'),
        (150, '5 Kalkale Harfi: ق - ط - ب - ج - د', 'Kaf (ق), Tı (ط), Be (ب), Cim (ج) ve Dal (د) harfleridir.'),
        (200, 'Kodlama Formülü: «قُطْبُ جَدٍّ» (Kutbu Ced)', 'Beş kalkale harfinin akılda kalması için birleştirilmiş geleneksel tecvit kodlamasıdır.'),
        (250, 'Kalkale Oluşma Şartı: Sükûn (Cezim/Vakıf)', 'Kalkale harfi mutlaka SAKİN olmalıdır (ya kelimenin ortasında cezimli ya da sonda durulurken).'),
        (300, 'Fonetik Sebep: Şiddet ve Cehr Sıfatları', 'Hem nefesin hem sesin mahreçte hapsolması sebebiyle harfin ancak sarsıntıyla duyulabilmesi.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Kalkale-i Suğrâ ve Kalkale-i Kübrâ
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KALKALE-İ SUĞRÂ VE KALKALE-İ KÜBRÂ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, '1. Kalkale-i Suğrâ (Küçük Kalkale)', 'Kalkale harfi kelimenin ORTASINDA sakin (lâzım sükûnlu) gelirse hafif vurguyla yapılır.'),
        (150, 'Kalkale-i Suğrâ Örnekleri', 'يَقْطَعُونَ (yek-taûne), يَطْمَعُ (yat-mau), أَبْوَابًا (eb-vâben), يَجْعَلْ (yec-al), يَدْخُلُونَ (yed-hulûne).'),
        (200, '2. Kalkale-i Kübrâ (Büyük Kalkale)', 'Kalkale harfi kelimenin SONUNDA bulunup üzerinde VAKIF yapıldığında (durulduğunda) olur.'),
        (250, 'Kalkale-i Kübrâ Örnekleri (İhlâs ve Tebbet)', 'أَحَدٌ -> Ehad, الصَّمَدُ -> es-Samed, يَلِدْ -> yelid, الْفَلَقِ -> el-Felak, وَتَبَّ -> ve tebb!'),
        (300, 'Uygulama Uyarısı: Harekeye Çevirmemek!', 'Kalkale yaparken harfe fetha/kesra harekesi eklenmemeli; sadece mahreç çarptırılmalıdır.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖZET KURAL: «قُطْبُ جَدٍّ» harfleri HAREKELİ iken kalkale yapılmaz! Ortada cezimliyse SUĞRÂ; sonda duruluyorsa KÜBRÂ olur!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kelime sonundaki kalkale harfi şeddeli olup üzerinde durulursa (وَتَبَّ، الْحَقُّ gibi) en kuvvetli Kalkale-i Kübrâ (Ekber) meydana gelir.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
