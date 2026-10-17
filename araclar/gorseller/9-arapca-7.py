from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('arapca')
    ic = []
    ic.append(P.baslik(400, 32, 'ÜNİTE 1: HAYDİ TANIŞALIM — DERS 2: TANIŞMA (التَّعَارُفُ) VE DİL YAPILARI', R['koyu']))

    # Sol panel: Hedef Kelimeler (Milliyetler / İsm-i Mensub ve Meslekler)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. MİLLİYETLER (النِّسْبَةُ) VE MESLEKLER', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Ülkeden Milliyet Yapımı: İsm-i Mensub (-î / -iyye)', 'تُرْكِيَا -> تُرْكِيٌّ (Türk erkek)  |  تُرْكِيَّةٌ (Türk kadın).'),
        (150, 'Örnek Ülke ve Milliyetler (المُذَكَّرُ وَالمُؤَنَّثُ)', 'مِصْرُ -> مِصْرِيٌّ / مِصْرِيَّةٌ  |  فِلَسْطِينُ -> فِلَسْطِينِيٌّ / فِلَسْطِينِيَّةٌ.'),
        (200, 'Okul ve Meslek Kelimeleri (المِهَنُ)', 'طَالِبٌ / طَالِبَةٌ (Öğrenci) | مُعَلِّمٌ / مُعَلِّمَةٌ (Öğretmen) | صَدِيقٌ / صَدِيقَةٌ.'),
        (250, 'Diğer Temel Meslekler (مُذَكَّر / مُؤَنَّث)', 'طَبِيبٌ / طَبِيبَةٌ (Doktor) | مُهَنْدِسٌ / مُهَنْدِسَةٌ (Mühendis).'),
        (300, 'Tanışma ve Memnuniyet İfadeleri', 'تَشَرَّفْتُ بِمَعْرِفَتِكَ / فُرْصَةٌ سَعِيدَةٌ (Tanıştığımıza memnun oldum!).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Hedef Dil Yapıları (Soru Edatları ve Bitişik Zamirler)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HEDEF DİL YAPILARI VE SORU EDATLARI', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'İsim Sorma ve Bitişik Zamirler (ـي / ـكَ / ـكِ / ـهُ / ـهَا)', 'مَا اسْمُكَ؟ (Adın ne? - Erkek) | مَا اسْمُكِ؟ (Kadın) -> اِسْمِي أَحْمَدُ.'),
        (150, 'Kimdir Sorma: مَنْ هٰذَا؟ / مَنْ هٰذِهِ؟', 'مَنْ هٰذَا؟ -> هٰذَا صَدِيقِي عَلِيٌّ. | مَنْ هٰذِهِ؟ -> هٰذِهِ مُعَلِّمَتِي.'),
        (200, 'Memleket ve Milliyet Sorma: مِنْ أَيْنَ أَنْتَ؟', 'مِنْ أَيْنَ أَنْتَ؟ -> أَنَا مِنْ تُرْكِيَا، أَنَا تُرْكِيٌّ. (Türkiye’denim, Türk’üm).'),
        (250, 'Meslek ve Milliyet Sorusu: مَا جِنْسِيَّتُكَ؟ / مَا مِهْنَتُهُ؟', 'مَا جِنْسِيَّتُكِ؟ -> أَنَا تُرْكِيَّةٌ. | مَا مِهْنَتُهُ؟ -> هُوَ مُهَنْدِسٌ.'),
        (300, 'Evet/Hayır Sorusu: هَلْ أَنْتَ طَالِبٌ؟ (نَعَمْ / لَا)', 'نَعَمْ، أَنَا طَالِبٌ فِي الصَّفِّ التَّاسِعِ.  |  لَا، أَنَا مُعَلِّمٌ.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL (İSM-İ MENSUB): Ülke sonuna erkek için şeddeli يٌّ (-iyyun), kadın için يَّةٌ (-iyyetun) eklenir!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'SORU EDATLARI: مَنْ (Kim - akıllılar için) | مَا (Ne - cansız/kavramlar için) | مِنْ أَيْنَ (Nereden) | كَيْفَ (Nasıl) | هَلْ (-mı/-mi?).', '#334155', 9.8, 'normal', 'middle'))

    kaydet('9-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
