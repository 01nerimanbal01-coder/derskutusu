from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'SALLİ VE BARİK DUALARI İLE ANLAMLARI (SALAVAT DUALARI)', R['koyu']))

    # Sol panel: Allahümme Salli Duası
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ALLAHÜMME SALLİ DUASI VE ANLAMI', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, '1. Cümle: Allâhümme salli alâ Muhammedin...', 'Allah’ım! Muhammed’e ve Muhammed’in ailesine rahmet et.'),
        (150, '2. Cümle: Kemâ salleyte alâ İbrâhîme...', 'İbrahim’e ve İbrahim’in ailesine rahmet ettiğin gibi.'),
        (200, '3. Cümle: İnneke hamîdün mecîd.', 'Şüphesiz Sen övülmeye layık (Hamîd) ve şanı yüce (Mecîd) olansın.'),
        (250, '"Salli" Kelimesinin Anlamı', 'Allah’tan Peygamberimize rahmet etmesini ve şanını yüceltmesini dilemek.'),
        (300, '"Âl" Kavramı', 'Peygamberimizin Ehl-i Beyt’i (ailesi) ve samimi müminler.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Allahümme Barik Duası ve Okunduğu Yerler
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ALLAHÜMME BARİK DUASI VE OKUNDUĞU YERLER', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '1. Cümle: Allâhümme bârik alâ Muhammedin...', 'Allah’ım! Muhammed’i ve Muhammed’in ailesini mübarek kıl.'),
        (150, '2. Cümle: Kemâ bârekte alâ İbrâhîme...', 'İbrahim’i ve İbrahim’in ailesini mübarek kıldığın gibi.'),
        (200, '3. Cümle: İnneke hamîdün mecîd.', 'Şüphesiz Sen övülmeye layık ve şanı yüce olansın.'),
        (250, 'Namazda Okunduğu Yerler (Ka’de-i Ahîre)', 'Tüm namazların son oturuşunda Ettehiyyâtü’den sonra okunur.'),
        (300, 'Diğer Okunduğu Yerler', 'Cenaze namazında 2. tekbirden sonra; İkindi/Yatsı sünneti ilk oturuşta.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'EZBER İPUCU: Salli duasında "salli ... kemâ salleyte" (rahmet et); Barik duasında "bârik ... kemâ bârekte" (mübarek kıl) denir!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Her iki duada da tevhid mücadelesinin iki büyük peygamberi Hz. Muhammed (s.a.v.) ve Hz. İbrahim (a.s.) birlikte anılır.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('6-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
