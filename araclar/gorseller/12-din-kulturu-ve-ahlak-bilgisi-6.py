from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'MÜSLÜMANLARIN BİLİM ALANINDA YAPTIĞI ÖNCÜ VE ÖZGÜN ÇALIŞMALAR', R['koyu']))

    # Sol panel: Naklî (Dinî) İlimlerde Öncü Âlimler ve Eserleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. DİNÎ (NAKLÎ) İLİMLERDE ÖNCÜ ÂLİMLER', R['koyu'], 13, 'bold', 'middle'))
    nakli = [
        (100, 'Tefsir İlmi', 'Taberî (Câmiu’l-Beyân) • Zemahşerî • Fahreddin Râzî • Elmalılı'),
        (150, 'Hadis İlmi (Kütüb-i Sitte)', 'Buhârî (el-Câmiu’s-Sahîh) • Müslim • Tirmizî • Ebû Dâvûd'),
        (200, 'Kelam İlmi (İtikadi Mezhepler)', 'İmam Mâtürîdî (Kitâbü’t-Tevhîd) • İmam Eş’arî (Makâlât)'),
        (250, 'Fıkıh İlmi (Amelî Mezhepler)', 'Ebû Hanîfe (Fıkh-ı Ekber) • İmam Şâfiî (er-Risâle) • Mâlik • İbn Hanbel'),
        (300, 'Coğrafya ve Tarih', 'İbn Haldun (Mukaddime) • Pîrî Reis (Kitâb-ı Bahriye) • İdrîsî'),
    ]
    for y, b, a in nakli:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Aklî (Fen ve Doğa) İlimlerde Öncü Bilginler
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. FEN VE DOĞA İLİMLERİNDE ÖNCÜ BİLGİNLER', '#1e40af', 13, 'bold', 'middle'))
    akli = [
        (100, 'Matematik & Astronomi', 'Hârizmî (Cebir ve 0 - Kitâbü’l-Cebr) • Uluğ Bey • Ali Kuşçu • Bîrûnî'),
        (150, 'Tıp ve Eczacılık', 'İbn Sînâ (el-Kânûn fi’t-Tıb) • Ebû Bekir er-Râzî • Akşemseddin (Mikrop)'),
        (200, 'Fizik, Optik ve Sibernetik', 'İbnü’l-Heysem (Optik - Kitâbü’l-Menâzır) • Cezerî (Robotik/Sibernetik)'),
        (250, 'Kimya (Modern Kimyanın Öncüsü)', 'Câbir b. Hayyân (İmbik, asitler, atomun parçalanabilirliği)'),
        (300, 'Felsefe ve Mantık', 'Kindî • Fârâbî (Muallim-i Sânî / İhsâü’l-Ulûm) • İbn Rüşd'),
    ]
    for y, b, a in akli:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'BATI’DA TANINAN İSİMLERİ: İbn Sînâ → Avicenna | İbn Rüşd → Averroes | Hârizmî → Algoritmi | İbnü’l-Heysem → Alhazen', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Fuat Sezgin: İslam Bilim ve Teknoloji Tarihi alanında 17 ciltlik dev eseriyle bu mirası dünyaya tanıtmıştır.', '#334155', 11, 'normal', 'middle'))

    kaydet('12-din-kulturu-ve-ahlak-bilgisi-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic