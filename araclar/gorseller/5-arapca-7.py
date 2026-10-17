from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('arapca')
    ic = []
    ic.append(P.baslik(400, 32, 'ARAP ALFABESİNİN İLK HARFLERİ (أ - ز), HAREKELER VE TANIŞMA', R['koyu']))

    # Sol panel: Elif'ten Ze'ye İlk 11 Harf ve Özellikleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HARFLER VE KELİME ÖRNEKLERİ (أ - ز)', R['koyu'], 13, 'bold', 'middle'))

    harfler = [
        (100, 'أ (Elif) • ب (Be) • ت (Te) • ث (Se)', 'أَبٌ (Baba) • بَابٌ (Kapı) • تِينٌ (İncir) • ثَوْبٌ (Elbise)'),
        (150, 'ج (Cim) • ح (Ha) • خ (Hı)', 'جَمَلٌ (Deve) • حَقِيبَةٌ (Çanta) • خُبْزٌ (Ekmek)'),
        (200, 'د (Dal) • ذ (Zel)', 'دَفْتَرٌ (Defter) • دِيكٌ (Horoz) • ذَهَبٌ (Altın)'),
        (250, 'ر (Ra) • ز (Ze)', 'رَجُلٌ (Adam) • رُمَّانٌ (Nar) • زَهْرَةٌ (Çiçek)'),
        (300, 'Nokta Farkıyla Ayrılan Kardeş Harfler', 'ب (1 altta) - ت (2 üstte) - ث (3 üstte) | ج - ح - خ'),
    ]
    for y, b, a in harfler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Kısa Harekeler (Fetha, Kesra, Damme) ve Cezim
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HAREKELER (الْحَرَكَاتُ) VE DİYALOG TEKRARI', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, 'el-Fethatu (الْفَتْحَةُ — Üstün: ـَ )', 'Harfin üstüne konur, "e / a" sesi verir: بَ (be), رَ (ra).'),
        (150, 'el-Kesratu (الْكَسْرَةُ — Esre: ـِ )', 'Harfin altına konur, "i / ı" sesi verir: بِ (bi), تِ (ti).'),
        (200, 'ed-Dammetu (الضَّمَّةُ — Ötre: ـُ )', 'Harfin üstüne konur, "ü / u" sesi verir: بُ (bu), دُ (dü).'),
        (250, 'es-Sükûn (السُّكُونُ — Cezim: ـْ )', 'Hareketsiz harfi önceki harfe bağlar: أَبْ (eb), بِنْتٌ (kız).'),
        (300, 'Kendini ve Arkadaşını Tanıtma', 'أَنَا أَحْمَدُ (Ben Ahmet) • هٰذَا عَلِيٌّ (Bu Ali) • هٰذِهِ زَيْنَبُ (Bu Zeynep).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: Bu gruptaki أ - د - ذ - ر - ز harfleri kendinden sonra gelen harfle BİRLEŞMEZ!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'İşaret İsimleri: هٰذَا (Hâzâ: Bu - Eril/Müzekker için)  |  هٰذِهِ (Hâzihî: Bu - Dişil/Müennes için)', '#334155', 11, 'normal', 'middle'))

    kaydet('5-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
