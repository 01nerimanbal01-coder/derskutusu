from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('arapca')
    ic = []
    ic.append(P.baslik(400, 32, '2. ÜNİTE: ALIŞVERİŞ (التَّسَوُّقُ) — 1. DERS: BAKKALDA (فِي الْبَقَّالَةِ)', R['koyu']))

    # Sol panel: Bakkalda Temel Gıda Kelimeleri ve Ölçü Birimleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. BAKKALDA TEMEL GIDA KELİMELERİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'خُبْزٌ (Hubzün - Ekmek) | حَلِيبٌ (Halîbün - Süt)', 'جُبْنٌ (Cübnün - Peynir) | زُبْدَةٌ (Zübdetün - Tereyağı).'),
        (150, 'بَيْضٌ (Beydun - Yumurta) | زَيْتُونٌ (Zeytûnün - Zeytin)', 'عَسَلٌ (Aselün - Bal) | سُكَّرٌ (Sükkerun - Şeker).'),
        (200, 'شَايٌ (Şâyün - Çay) | أُرْزٌ (Ürzün - Pirinç)', 'دَقِيقٌ (Dakîkun - Un) | زَيْتٌ (Zeytün - Sıvı yağ).'),
        (250, 'Miktar ve Paket İfadeleri (Ölçü Birimleri)', 'كِيلُو (Kîlû - Kilo) | عُلْبَةٌ (Ulbetün - Kutu/Paket).'),
        (300, 'Diğer Ölçü ve Satış Kelimeleri', 'زُجَاجَةٌ (Zücâcetün - Şişe) | لِيرَةٌ تُرْكِيَّةٌ (Türk Lirası).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Alışveriş ve Fiyat Sorma Diyalog Kalıpları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ALIŞVERİŞ VE FİYAT SORMA DİYALOGLARI', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'أَيُّ خِدْمَةٍ؟ / مَاذَا تُرِيدُ؟ (Eyyü hidmetin? / Mâzâ türîdü?)', 'Nasıl yardımcı olabilirim? / Ne istiyorsun (almak istersin)?'),
        (150, 'أُرِيدُ كِيلُو جُبْنٍ مِنْ فَضْلِكَ. (Ürîdü kîlû cübnin min fadlike.)', 'Lütfen bir kilo peynir istiyorum. (Ürîdü = İstiyorum)'),
        (200, 'هَلْ يُوجَدُ عَسَلٌ؟ (Hel yûcedü aselün?)', 'Bal bulunur mu (var mı)? -> نَعَمْ، يُوجَدُ (Evet, var).'),
        (250, 'بِكَمْ هٰذَا؟ / بِكَمِ الْحَلِيبُ؟ (Bikem hâzâ? / Bikemi’l-halîbü?)', 'Bu kaç lira? / Süt kaç lira? -> بِعِشْرِينَ لِيرَةً (20 TL).'),
        (300, 'تَفَضَّلْ! (Tefaddal! - Buyur!) — شُكْرًا (Şükran - Teşekkürler)', 'بِكُلِّ سُرُورٍ / عَفْوًا (Memnuniyetle / Rica ederim).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KALIPLAR: "Ürîdü..." (İstiyorum...) | "Hel yûcedü...?" (...var mı?) | "Bikem...?" (Kaç lira / Ne kadar?)!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'el-Bakkâlü (الْبَقَّالُ) = Bakkal (satıcı) | el-Bakkâletü (الْبَقَّالَةُ) = Bakkal dükkânı | el-Müşterî (الْمُشْتَرِي) = Müşteri.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
