from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('dil')
    ic = []
    ic.append(P.baslik(400, 32, 'ARAPÇA — DERS 2: GÜZEL DAVRANIŞLARIM (مُعَامَلَاتِي الْحَسَنَةُ)', R['koyu']))

    # Sol panel: Ahlaki Kavramlar ve Muzâri Fiil Kalıpları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. GÜZEL DAVRANIŞ KAVRAMLARI VE FİİLLER', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Temel Ahlaki Değerler (المفردات)', 'el-İhtirâm (Saygı), et-Teâvün (Yardımlaşma), et-Tesâmuh (Hoşgörü), es-Sıdk (Doğruluk).'),
        (150, 'أَحْتَرِمُ الْكِبَارَ (Ahterimu’l-kibâr)', 'Büyüklere saygı gösteririm. / أَرْحَمُ الصِّغَارَ (Erhamu’s-sığâr): Küçüklere şefkat ederim.'),
        (200, 'أُسَاعِدُ الْمُحْتَاجِينَ (Üsâidü’l-muhtâcîn)', 'Muhtaçlara yardım ederim. / أَحْفَظُ اللِّسَانَ (Ahfazu’l-lisân): Dilimi korurum.'),
        (250, 'أَسْتَأْذِنُ قَبْلَ الدُّخُولِ (Este’zinü kable’d-duhûl)', 'Girmeden önce izin isterim.'),
        (300, 'أَعْتَذِرُ عِنْدَ الْخَطَأِ (A’teziru inde’l-hata’)', 'Hata yaptığımda özür dilerim.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Sosyal Nezaket İfadeleri ve Hadisler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. NEZAKET İFADELERİ VE HADİS-İ ŞERİFLER', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'مِنْ فَضْلِكَ / لَوْ سَمَحْتَ (Min fadlike / Lev semahte)', 'Lütfen / Müsaadenizle (Kadın muhatap için: Min fadliki / Lev semahti).'),
        (150, 'شُكْرًا جَزِيلًا — عَفْوًا / آسِفٌ — آسِفَةٌ', 'Çok teşekkür ederim — Rica ederim / Üzgünüm, özür dilerim (Erkek / Kadın).'),
        (200, 'جَزَاكَ اللّٰهُ خَيْرًا (Cezâkellâhu hayran)', 'Allah seni hayırla mükâfatlandırsın! (Cevabı: وَإِيَّاكَ - Ve iyyâke).'),
        (250, '«تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ»', '“Kardeşinin yüzüne gülümsemen senin için bir sadakadır.” (Tirmizî)'),
        (300, '«مَنْ لَا يَرْحَمْ لَا يُرْحَمْ» / «خَيْرُ النَّاسِ أَنْفَعُهُمْ لِلنَّاسِ»', '“Merhamet etmeyene merhamet olunmaz.” / “İnsanların en hayırlısı en faydalı olandır.”'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİL BİLGİSİ NOTU: Muzâri fiilde “Ben (أَنَا)” için fiil أَ / أُ ile başlar (أَحْتَرِمُ); “Biz (نَحْنُ)” için نَ / نُ ile başlar (نَحْتَرِمُ).', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '«اَلدِّينُ الْمُعَامَلَةُ» (ed-Dînü’l-muâmele) — Din, insanlarla güzel ilişkiler kurmak ve dürüst davranmaktır.', '#334155', 10, 'normal', 'middle'))

    kaydet('10-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
