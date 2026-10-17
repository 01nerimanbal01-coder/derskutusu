from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('arapca')
    ic = []
    ic.append(P.baslik(400, 32, '3. ÜNİTE: KÜLTÜR VE SANAT — 1. DERS: EDEBİYAT (الأَدَبُ)', R['koyu']))

    # Sol panel: Edebi Türler ve Kavramlar
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. EDEBÎ TÜRLER VE KAVRAMLAR (المُفْرَدَاتُ)', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'الأَدَبُ (Edebiyat) — الأَدِيبُ (Edip/Edebiyatçı)', 'نَادِي الأَدَبِ : Edebiyat Kulübü | مَجَلَّةُ المَدْرَسَةِ : Okul Dergisi'),
        (150, 'الشِّعْرُ (Şiir) — القَصِيدَةُ (Kaside / Şiir Metni)', 'الشَّاعِرُ (Erkek Şair) | الشَّاعِرَةُ (Kadın Şair) | شُعَرَاءُ (Şairler)'),
        (200, 'القِصَّةُ (Hikâye / Öykü — Çoğulu: القِصَصُ)', 'قِصَّةٌ قَصِيرَةٌ : Kısa Hikâye / Öykü | قِصَّةٌ مُفِيدَةٌ : Faydalı Hikâye'),
        (250, 'الرِّوَايَةُ (Roman — Çoğulu: الرِّوَايَاتُ)', 'رِوَايَةٌ تَارِيخِيَّةٌ : Tarihî Roman | رِوَايَةٌ بُولِيسِيَّةٌ : Polisiye Roman'),
        (300, 'المَسْرَحِيَّةُ (Tiyatro) — المَقَالَةُ (Makale)', 'الكَاتِبُ / المُؤَلِّفُ : Yazar / Müellif (Çoğulu: الكُتَّابُ)'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Fiiller, Tercihler ve Diyalog Kalıpları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. EDEBî TERCİHLER VE DİYALOG KALIPLARI', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'Okuma ve Yazma Fiilleri (المُضَارِعُ)', 'أَقْرَأُ (Okuyorum) — تَقْرَأُ (Okuyorsun) | أَكْتُبُ (Yazıyorum) — يَكْتُبُ (Yazıyor)'),
        (150, 'Sevgi ve Tercih Kalıpları', 'أُحِبُّ قِرَاءَةَ القِصَصِ (Hikâye okumayı severim) | أُفَضِّلُ الرِّوَايَةَ (Romanı tercih ederim)'),
        (200, 'Ne Okuduğunu Sorma', 'مَاذَا تَقْرَأُ يَا عَلِيُّ؟ -> أَقْرَأُ رِوَايَةً تَارِيخِيَّةً مُمْتِعَةً.'),
        (250, 'Kitabın Yazarını veya Şairini Sorma', 'مَنْ كَاتِبُ هٰذَا الكِتَابِ؟ (Bu kitabın yazarı kim?) | مَنْ شَاعِرُ القَصِيدَةِ؟'),
        (300, 'Kitabın Konusunu Anlatma (تَتَحَدَّثُ عَنْ...)', 'هٰذِهِ القَصِيدَةُ تَتَحَدَّثُ عَنْ حُبِّ الوَطَنِ (Bu şiir vatan sevgisinden bahsediyor).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖRNEK CÜMLE: مُحَمَّد عَاكِف أَرْصُوي شَاعِرٌ كَبِيرٌ كَتَبَ نَشِيدَ الاِسْتِقْلَالِ. (Mehmet Akif Ersoy İstiklal Marşı’nı yazan büyük bir şairdir.)', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'TEKİL -> ÇOĞUL: كِتَابٌ -> كُتُبٌ | قِصَّةٌ -> قِصَصٌ | رِوَايَةٌ -> رِوَايَاتٌ | شَاعِرٌ -> شُعَرَاءُ | كَاتِبٌ -> كُتَّابٌ', '#334155', 10, 'normal', 'middle'))

    kaydet('8-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
