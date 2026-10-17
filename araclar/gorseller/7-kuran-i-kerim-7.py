from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'KUNUT DUALARI (1-2): ANLAMLARI, MESAJLARI VE VİTİR NAMAZI', R['koyu']))

    # Sol panel: Kunut-1 Duası Mesajları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KUNUT-1 DUASI: İSTİÂNE VE İSTİĞFAR', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Kunut Kelimesinin Anlamı', 'Allah’a gönülden boyun eğmek, huşû ile ayakta dua etmek.'),
        (150, 'Allâhümme innâ nesteînüke... (Yardım ve Hidayet)', 'Allah’ım! Senden yardım (nesteînüke) ve hidayet (nehdîke) dileriz.'),
        (200, 'Ve nestağfiruke ve netûbü ileyk (Tövbe)', 'Senden bağışlanma diler (istiğfar) ve Sana tövbe ederiz.'),
        (250, 'Ve nü’minü bike ve netevekkelü aleyk (Tevekkül)', 'Sana iman eder ve yalnızca Sana güvenip dayanırız.'),
        (300, 'Nüsnî aleyke’l-hayra... (Hamd ve Şükür)', 'Seni hayırla över, Sana şükreder ve asla nankörlük etmeyiz!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Kunut-2 Duası Mesajları ve Vitir Namazında Okunuşu
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KUNUT-2 DUASI VE VİTİR NAMAZI UYGULAMASI', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Allâhümme iyyâke na’büdü... (Tevhid ve İbadet)', 'Allah’ım! Yalnız Sana kulluk eder ve yalnız Senin için namaz kılarız.'),
        (150, 'Ve nescüdü ve ileyke nes’â ve nahfid', 'Yalnız Sana secde eder ve Sana kulluğa koşarız.'),
        (200, 'Nercû rahmeteke ve nahşâ azâbek (Havf ve Recâ)', 'Rahmetini umar (recâ), azabından korkarız (havf).'),
        (250, 'Vitir Namazında Ne Zaman Okunur?', 'Yatsıdan sonra kılınan 3 rekâtlık Vitir namazının 3. REKÂTINDA!'),
        (300, 'Uygulama Sırası (3. Rekât)', 'Fatiha + Zamm-ı Sure -> "Allâhü Ekber" (Tekbir) -> El bağla -> KUNUT!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'HAVF VE RECÂ DENGESİ: Mümin, Allah’ın rahmetini umut eder (Recâ) ve azabından sakınır (Havf) -> Kunut-2 Duası!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kunut dualarını henüz ezberleyemeyen kişi vitir namazında "Rabbenâ âtinâ" duasını veya 3 kez "Allâhümmağfirlî" okuyabilir.', '#334155', 10, 'normal', 'middle'))

    kaydet('7-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
