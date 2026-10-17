from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fen-bilimleri')
    ic = []
    ic.append(P.baslik(400, 32, 'KUVVET VE KUVVETİN ÖLÇÜLMESİ: DİNAMOMETRE VE NEWTON (N)', R['koyu']))

    # Sol panel: Kuvvetin Cisimler Üzerindeki Etkileri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KUVVET NEDİR? ETKİLERİ NELERDİR?', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Kuvvet Sembolü: F  |  Birimi: Newton - N)', '#334155', 11, 'bold', 'middle'))

    etkiler = [
        (114, '1. Hareket Ettirme ve Durdurma Etkisi', 'Duran topa vurunca hareket eder; kaleci topu tutunca durur.'),
        (162, '2. Hızlandırma ve Yavaşlatma Etkisi', 'Pedala basınca bisiklet hızlanır; frene basınca yavaşlar.'),
        (210, '3. Yön Değiştirme Etkisi', 'Tenis raketiyle gelen topa vurulunca topun yönü değişir.'),
        (258, '4. Döndürme Etkisi', 'Musluğu açmak, direksiyonu çevirmek, kapı kolunu indirmek.'),
        (306, '5. Şekil Değiştirme Etkisi (Esnek / Kalıcı)', 'Yay ve süngerde geçici (esnek); oyun hamuru ve kağıtta kalıcı.'),
    ]
    for y, b, a in etkiler:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Dinamometre ve Ölçüm İlkeleri
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. KUVVETİN ÖLÇÜLMESİ: DİNAMOMETRE', '#1e40af', 13, 'bold', 'middle'))
    ic.append(P.metin(590, 100, '(Yayların Esneklik Özelliğinden Yararlanılarak Yapılır)', '#334155', 10, 'bold', 'middle'))

    ilkeler = [
        (114, 'Uzama Miktarı İle Kuvvet Doğru Orantılıdır!', '10 N kuvvet yayı 2 cm uzatırsa → 30 N kuvvet 6 cm uzatır.'),
        (162, 'İnce Yay = Hassas Ölçüm (Küçük Kuvvetler)', 'İnce bakır yay kolay uzar; küçük kuvvetleri hassas ölçer.'),
        (210, 'Kalın Yay = Büyük Kuvvet Ölçümü', 'Kalın çelik yay zor uzar; daha büyük kuvvetleri ölçebilir.'),
        (258, 'Esneklik Sınırı (Kapasite) Aşılmamalıdır!', '50 N’luk dinamometreye 80 N asılırsa yay bozulur!'),
        (306, 'Bölme Hesabı: Kapasite ÷ Bölme Sayısı', '10 bölmeli 50 N’luk dinamometrede 1 bölme = 5 N gösterir.'),
    ]
    for y, b, a in ilkeler:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 15, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'ESNEK CİSİM: Kuvvet kalkınca eski hâline döner (Yay, paket lastiği, bulaşık süngeri, balon).', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'ESNEK OLMAYAN CİSİM: Kuvvet kalkınca eski hâline dönemez (Oyun hamuru, cam, kağıt, bakır tel).', '#334155', 11, 'normal', 'middle'))

    kaydet('5-fen-bilimleri-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
