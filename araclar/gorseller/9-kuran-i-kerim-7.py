from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'KUR’AN-I KERİM’İ GÜZEL OKUMA: HARFLERİN ÖZELLİKLERİ VE KALKALE', R['koyu']))

    # Sol panel: Peltek, Kalın (İsti'la) ve İnce (İstifal) Harfler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. PELTEK, KALIN VE İNCE HARFLER', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Peltek Okunan 3 Harf (Dil Ucu - Ön Dişler)', 'ث (Sâ)  —  ذ (Zel)  —  ظ (Zâ) -> Dil ucu üst ön dişlere değdirilir!'),
        (150, 'Kalın (İsti’lâ) Harfler — 7 Harf', 'خ ص ض غ ط ق ظ (“Hussa Dâgıtın Kız” kodlaması) -> Daima kalın okunur.'),
        (200, 'Hem Kalın Hem İnce Okunabilenler', 'ر (Râ) harfi ve Lafzatullah’taki (اللّٰه) ل (Lâm) harfi harekeye göre değişir.'),
        (250, 'İnce (İstifâl) Harfler (Diğer 20 Harf)', 'Üstün harekede “e” sesiyle, esrede “i”, ötrede “ü/u” arası ince sesle okunur.'),
        (300, 'Birbirine Benzer Sesli Harfler Ayrımı', 'ت - ط (Te-Tı) | س - ص - ث (Sin-Sad-Se) | ذ - ز - ظ (Zel-Ze-Zı) | ح - ه - خ.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Kalkale Harfleri (Kutbu Cedin) ve Safir/Boğaz Özellikleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KALKALE HARFLERİ (قُطْبُ جَدٍ) VE SIFATLAR', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Kalkale Nedir? (Sesi Çarptırarak/Sarsarak Okuma)', 'Kalkale harfi CEZİMLİ (sâkin) geldiğinde mahrecin kuvvetle ayrılmasıdır.'),
        (150, '5 Kalkale Harfi — Kodlama: قُطْبُ جَدٍ (KUTBU CEDİN)', 'ق (Kaf)  —  ط (Tı)  —  ب (Be)  —  ج (Cim)  —  د (Dal).'),
        (200, 'Küçük Kalkale (Kelime Ortasında Cezim)', 'Örnek: يَقْطَعُونَ ، أَفَلَا يَتَدَبَّرُونَ ، يَجْعَلُونَ (hafif vurgulu).'),
        (250, 'Büyük Kalkale (Kelime Sonunda Vakıf/Durak)', 'Örnek: قُلْ هُوَ اللّٰهُ أَحَدٌ (أَحَدْ) ، مِنْ شَرِّ مَا خَلَقَ (خَلَقْ) (kuvvetli).'),
        (300, 'Safîr (Keskin Islık Sesli) Harfler', 'ص (Sad), ز (Ze), س (Sin) harfleri dişler arasından keskin sesle çıkar.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ŞİFRE ÖZETİ: Peltek Harfler = ث ذ ظ (3 harf) | Kalın Harfler = خ ص ض غ ط ق ظ (7 harf) | Kalkale = ق ط ب ج د (5 harf)!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'ظ (Zâ) harfi hem PELTEK hem de KALIN okunan tek harftir; ط (Tı) ve ق (Kaf) ise hem KALIN hem KALKALE harfidir!', '#334155', 10, 'normal', 'middle'))

    kaydet('9-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
