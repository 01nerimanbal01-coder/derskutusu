from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('arapca')
    ic = []
    ic.append(P.baslik(400, 32, 'HARF-İ TARİF (الـ / el-) İLE AKRABA VE MESLEK DİYALOGLARI', R['koyu']))

    # Sol panel: Şemsî ve Kamerî Harfler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HARF-İ TARİF (el-) VE OKUNUŞ KURALLARI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Harf-i Tarif (الـ / el-) Ne İşe Yarar?', 'İsmin başına gelir, belirli yapar; sondaki tenvin (-ün) düşer (-ü olur).'),
        (150, 'Kamerî Harfler (Ay Harfleri — 14 Harf)', '"el-" takısındaki Lam (ل) cezimli olarak AÇIKÇA OKUNUR.'),
        (200, 'Kamerî Örnekler (Akraba ve Meslek)', 'el-Ebü (الْأَبُ), el-Ammü (الْعَمُّ), el-Muallimü (الْمُعَلِّمُ).'),
        (250, 'Şemsî Harfler (Güneş Harfleri — 14 Harf)', '"el-" takısındaki Lam OKUNMAZ; ilk harf ŞEDDELİ okunur!'),
        (300, 'Şemsî Örnekler (Meslekler)', 'et-Tabîbü (الطَّبِيبُ), et-Tâciru (التَّاجِرُ), eş-Şurtiyyü (الشُّرْطِيُّ).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Akraba ve Meslek Diyalogları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. AKRABALARIM VE MESLEKLERİ DİYALOGLARI', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'مَنْ هٰذَا؟ / مَنْ هٰذِهِ؟ (Men hâzâ? / Men hâzihî?)', 'Bu kimdir? (Erkek için Hâzâ / Kadın için Hâzihî)'),
        (150, 'هٰذَا عَمِّي. هُوَ مُهَنْدِسٌ. (Hâzâ ammî. Hüve mühendisün.)', 'Bu benim amcamdır. O bir mühendistir.'),
        (200, 'هٰذِهِ خَالَتِي. هِيَ طَبِيبَةٌ. (Hâzihî hâletî. Hiye tabîbetün.)', 'Bu benim teyzemdir. O bir (kadın) doktordur.'),
        (250, 'مَا مِهْنَةُ خَالِكَ؟ (Mâ mihnetü hâlike?)', 'Senin dayının mesleği nedir? -> Hâlî muallimün.'),
        (300, 'أَيْنَ يَعْمَلُ؟ (Eyne ya’melü?)', 'Nerede çalışıyor? -> Fî’l-medreseti (Okulda) / Fî’l-müsteşfâ.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'MÜZEKKER - MÜENNES UYUMU: Erkek akraba için "Hâzâ - Hüve - tabîbün"; Kadın akraba için "Hâzihî - Hiye - tabîbetün (ـة)"!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'ammî (amcam) - ammetî (halam) | hâlî (dayım) - hâletî (teyzem) | ceddî (dedem) - ceddetî (ninem).', '#334155', 10.5, 'normal', 'middle'))

    kaydet('6-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
