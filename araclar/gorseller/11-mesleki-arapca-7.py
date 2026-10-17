from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('dil')
    ic = []
    ic.append(P.baslik(400, 32, 'MESLEKİ ARAPÇA: ESMÂ-İ HÜSNÂ TECELİLERİ VE DUA METİNLERİ', R['koyu']))

    # Sol panel: Esmâ-i Hüsnâ ve Ahlaki Tecellileri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İLÂHÎ İSİMLER VE KULLUK YANSIMALARI', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'İlim ve Hikmet İsimleri: الْعَلِيمُ - الْحَكِيمُ', 'el-Alîm (Her şeyi bilen), el-Hakîm (Her işi hikmetli olan), el-Habîr (Haberdar olan).'),
        (150, 'Merhamet ve Bağışlama: الرَّحْمٰنُ - الْغَفُورُ - الْعَفُوُّ', 'er-Rahmân, er-Rahîm, el-Ğafûr (Çok bağışlayan), el-Afüvv (Affeden), et-Tevvâb.'),
        (200, 'Rızık ve Yaratma: الْخَالِقُ - الرَّزَّاقُ - الْكَرِيمُ', 'el-Hâlık (Yaratan), er-Rezzâk (Rızık veren), el-Kerîm (Cömert), el-Vehhâb (Karşılıksız veren).'),
        (250, 'Kudret ve Koruma: الْقَدِيرُ - الْحَفِيظُ - الْوَكِيلُ', 'el-Kadîr (Gücü yeten), el-Hafîz (Koruyan), el-Vekîl (Güvenilen), eş-Şâfî (Şifa veren).'),
        (300, 'Adalet ve Hüküm: الْعَدْلُ - الْحَكَمُ - السَّلَامُ', 'el-Adl (Mutlak adil), el-Hakem (Hükmeden), es-Selâm (Esenlik ve güven kaynağı).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Dil Bilgisi (İzâfet ve Sıfat Tamlaması) ve Esmâ Duaları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. TAMLAMA YAPILARI VE ESMÂ DUALARI', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Sıfat Tamlaması (التَّرْكِيبُ الْوَصْفِيُّ)', 'اَلْأَسْمَاءُ الْحُسْنَى (En güzel isimler) / اَلرَّبُّ الْكَرِيمُ (Cömert Rab) — 4 yönden uyum!'),
        (150, 'İsim Tamlaması / İzâfet (الْإِضَافَةُ)', 'عَبْدُ الرَّحْمٰنِ (Rahmân’ın kulu) / رَحْمَةُ اللّٰهِ (Allah’ın rahmeti) — Muzâfun ileyh mecrurdur.'),
        (200, 'Nidâ (Seslenme) ve Dua Kalıbı: يَا + İsim', 'يَا غَفُورُ اغْفِرْ لِي (Ey Ğafûr! Beni bağışla) / يَا شَافِي اشْفِنِي (Ey Şâfî! Bana şifa ver).'),
        (250, 'Kadir Gecesi Duası (Tirmizî)', '«اَللّٰهُمَّ إِنَّكَ عَفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنِّي» (Allah’ım! Sen Afüvv’sün, affı seversin, beni affet!).'),
        (300, 'Haşr Suresi 22-24. Ayetler (Hüvallâhüllezî)', 'En çok Esmâ-i Hüsnâ barındıran ayet grubu: el-Melik, el-Kuddûs, es-Selâm, el-Mü’min...'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİL BİLGİSİ KURALI: “يَا (Yâ)” nidâ harfinden sonra gelen tek kelimelik ilahi isim (münâdâ) tenvinsiz DAMME (ötre) üzerine mebni olur: يَا رَحْمٰنُ، يَا رَزَّاقُ!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '«وَلِلّٰهِ الْأَسْمَاءُ الْحُسْنَى فَادْعُوهُ بِهَا» — “En güzel isimler Allah’ındır; öyleyse O’na o güzel isimlerle dua edin!” (A’râf, 180)', '#334155', 10, 'normal', 'middle'))

    kaydet('11-mesleki-arapca-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic