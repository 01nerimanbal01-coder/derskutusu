from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('mesleki-arapca')
    ic = []
    ic.append(P.baslik(400, 32, 'AKAİD KAVRAMLARI, İNANÇ BAKIMINDAN İNSANLAR VE AKSÂM-I SEB’A', R['koyu']))

    # Sol panel: İnanç Bakımından İnsanlar (المؤمن - الكافر - المنافق - المشرك)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İNANÇ BAKIMINDAN İNSANLAR (أَقْسَامُ النَّاسِ)', R['koyu'], 13, 'bold', 'middle'))

    insanlar = [
        (98, 'el-Mü’minu (الْمُؤْمِنُ)', 'Kalbiyle tasdik edip diliyle ikrar eden (آمَنَ بِاللّٰهِ)'),
        (146, 'el-Müşriku (الْمُشْرِكُ)', 'Allah’a ibadette ve ilahlıkta ortak koşan (أَشْرَكَ بِاللّٰهِ)'),
        (194, 'el-Kâfiru (الْكَافِرُ)', 'İman esaslarını bilerek inkâr eden / gizleyen (كَفَرَ بِالْحَقِّ)'),
        (242, 'el-Münâfıku (الْمُنَافِقُ)', 'Diliyle inanmış görünüp kalbiyle inkâr eden (أَظْهَرَ الْإِيمَانَ وَأَبْطَنَ الْكُفْرَ)'),
        (290, 'Tevhîd ve Şirk (التَّوْحِيدُ وَالشِّرْكُ)', 'لاَ إِلٰهَ إِلاَّ اللّٰهُ — إِنَّ الشِّرْكَ لَظُلْمٌ عَظِيمٌ (Lokman 13)'),
    ]
    for y, b, a in insanlar:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Sarf - Aksâm-ı Seb'a (الأقسام السبعة - Fiillerin Yapıca 7 Kısmı)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. AKSÂM-I SEB’A (أَقْسَامُ السَّبْعَةِ — 7 FİİL KISMI)', '#92400e', 13, 'bold', 'middle'))

    ic.append(P.kutu(415, 96, 350, 108, '#ffffff', '#d97706'))
    ic.append(P.metin(590, 114, 'A) SAHİH FİİLLER (الْفِعْلُ الصَّحِيحُ — İllet Harfi ا، و، ي Yok):', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(590, 136, '1. Sâlim (السَّالِمُ): Hemze ve şedde yok → كَتَبَ ، عَبَدَ ، شَكَرَ', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 158, '2. Mehmûz (الْمَهْمُوزُ): Kökünde hemze (أ) var → أَمَرَ ، سَأَلَ ، قَرَأَ', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 180, '3. Muda’af (الْمُضَعَّفُ): Son iki harfi aynı (şeddeli) → فَرَّ ، مَدَّ ، ظَنَّ', '#334155', 10, 'normal', 'middle'))

    ic.append(P.kutu(415, 212, 350, 124, '#ffffff', '#2563eb'))
    ic.append(P.metin(590, 230, 'B) MU’TELL FİİLLER (الْفِعْلُ الْمُعْتَلُّ — İllet Harfi ا، و، ي Var):', '#1e40af', 11, 'bold', 'middle'))
    ic.append(P.metin(590, 252, '4. Misâl (الْمِثَالُ): İlk harfi illetli → وَجَدَ ، وَحَّدَ ، يَئِسَ', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 274, '5. Ecvef (الْأَجْوَفُ): Orta harfi illetli → قَالَ ، كَانَ ، صَامَ', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 296, '6. Nâkıs (النَّاقِصُ): Son harfi illetli → دَعَا ، هَدَى ، رَضِيَ', '#334155', 10, 'normal', 'middle'))
    ic.append(P.metin(590, 318, '7. Lefîf (اللَّفِيفُ): İki illet harfi var → وَقَى (Mefrûk) ، طَوَى (Makrûn)', '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KURAL: Bir fiilin Aksâm-ı Seb’a’daki türü belirlenirken eklerine değil, SÜLÂSÎ MÜCERRED (3 harfli mazi kök) hâline bakılır!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Örnek: يُؤْمِنُ → Kökü: أَمِنَ (Mehmûz) | يَعْبُدُونَ → Kökü: عَبَدَ (Sâlim) | يَهْدِي → Kökü: هَدَى (Nâkıs)', '#334155', 11, 'normal', 'middle'))

    kaydet('12-mesleki-arapca-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
