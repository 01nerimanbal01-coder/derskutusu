from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'HARFLERİ HAREKELERLE BİRLEŞTİREREK KELİME OKUMA UYGULAMALARI', R['koyu']))

    # Sol panel: Üstün, Esre ve Ötre Karışık Üç Harfli Kelimeler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HAREKELİ KELİME OKUMA ÖRNEKLERİ', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '(Sağdan Sola Doğru Uzatmadan Birleştirme)', '#334155', 10, 'bold', 'middle'))

    kelimeler = [
        (114, 'Sadece Üstünlü Kelimeler (ـَ ـَ ـَ)', 'كَتَبَ (ke-te-be) • خَلَقَ (ha-le-ka) • نَصَرَ (na-sa-ra)'),
        (162, 'Üstün ve Esreli Kelimeler (ـَ ـِ ـَ)', 'عَلِمَ (a-li-me) • حَمِدَ (ha-mi-de) • شَرِبَ (şe-ri-be)'),
        (210, 'Ütre, Esre ve Üstünlü Kelimeler (ـُ ـِ ـَ)', 'خُلِقَ (hu-li-ka) • قُرِئَ (ku-ri-e) • كُتِبَ (kü-ti-be)'),
        (258, 'Üstün ve Ötreli Kelimeler (ـَ ـُ ـَ)', 'حَسُنَ (ha-sü-ne) • كَبُرَ (ke-bü-ra) • كَرُمَ (ke-ru-me)'),
        (306, 'Kendinden Sonraya Birleşmeyen Harflerle', 'رُزِقَ (ru-zi-ka) • أَذِنَ (e-zi-ne) • وَجَدَ (ve-ce-de)'),
    ]
    for y, b, a in kelimeler:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 11, 'normal', 'middle'))

    # Sağ panel: Benzer Sesli Harfleri Ayırt Etme ve Okuma Kuralları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. TELAFFUZDA DİKKAT EDİLECEK NOKTALAR', '#92400e', 13, 'bold', 'middle'))

    kurallar = [
        (100, 'T (ت - ط) ve D (د - ض) Ayrımı', 'تَ (te: ince) vs. طَ (ta: kalın) | دَ (de: ince) vs. ضَ (da: kalın)'),
        (150, 'S Sesli 3 Harf (ث - س - ص)', 'ثَ (se: peltek-ince) • سَ (se: keskin-ince) • صَ (sa: kalın)'),
        (200, 'Z Sesli 3 Harf (ذ - ز - ظ)', 'ذَ (ze: peltek-ince) • زَ (ze: keskin-ince) • ظَ (za: peltek-kalın)'),
        (250, 'H Sesli 3 Harf (ح - خ - هـ)', 'حَ (ha: boğaz ortası) • خَ (ha: hırıltılı kalın) • هَ (he: göğüs/ince)'),
        (300, 'Ra (ر) Harfinin Özel Durumu', 'Üstün ve ötrede KALIN (رَ ra, رُ ru); esrede İNCE (رِ ri) okunur!'),
    ]
    for y, b, a in kurallar:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: Harekeli harfler okunurken sesler ASLA uzatılmaz (ke-te-be şeklinde net okunur; kâ-tê-bê yapılmaz!).', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kendinden sonraki harfle birleşmeyen 6 harf: ا - د - ذ - ر - ز - و (Elif, Dal, Zel, Ra, Ze, Vav)', '#334155', 11, 'normal', 'middle'))

    kaydet('5-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
