from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'FIKIH TARİHİ: KANUNLAŞTIRMA HAREKETLERİ VE GÜNÜMÜZ ÇALIŞMALARI', R['koyu']))

    # Sol panel: Kanunlaştırma (Taknîn) Dönemi: Mecelle ve Hukuk-ı Aile
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KANUNLAŞTIRMA (TAKNÎN) HAREKETLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Taknîn (Kanunlaştırma) İhtiyacı', 'Tanzimat sonrası mahkemelerde yeknesak (standart) hüküm uygulama zarureti.'),
        (150, 'Mecelle-i Ahkâm-ı Adliyye (1869-1876)', 'Ahmed Cevdet Paşa başkanlığında Hanefî fıkhına göre hazırlanan ilk medeni kanun.'),
        (200, 'Mecelle’nin Yapısı (1851 Madde)', '1 Mukaddime (99 Küllî Kaide) + 16 Kitap (Borçlar, Eşya ve Yargılama Hukuku).'),
        (250, 'Hukuk-ı Aile Kararnamesi (1917)', 'Mecelle’de yer almayan Aile Hukukunu (nikâh, nafaka, boşanma) düzenleyen kanun.'),
        (300, 'Diğer Mezheplerden İstifade (Telfîk)', '1917 Kararnamesi kadın haklarını korumak için Mâlikî vb. mezheplerden yararlandı.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Günümüz Fıkıh Çalışmaları ve Kurumsal İçtihat
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. GÜNÜMÜZ FIKIH KURULLARI VE MESELELERİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Kolektif (Kurumsal / Şûrâî) İçtihat', 'Fıkıh âlimleri ile tıp, iktisat ve fen uzmanlarının kurullar halinde ortak içtihadı.'),
        (150, 'Uluslararası Fıkıh Akademileri', 'Cidde İslam Fıkıh Akademisi (İİT), Mekke Fıkıh Akademisi, Avrupa Fetva Meclisi.'),
        (200, 'Türkiye’deki Kurumsal Yapılar', 'Diyanet İşleri Başkanlığı Din İşleri Yüksek Kurulu ve TDV İslam Ansiklopedisi.'),
        (250, 'Tıp, Biyoetik ve Gıda Meseleleri', 'Organ nakli, beyin ölümü, tüp bebek, otopsi, jelatin ve helal gıda sertifikasyonu.'),
        (300, 'İktisat ve Modern Finans Meseleleri', 'Katılım bankacılığı (murâbaha/mudârebe), tekâfül sigorta, borsa ve kripto varlıklar.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KÜLLÎ KAİDE ÖRNEKLERİ: “Bir işten maksat ne ise hüküm ona göredir.” • “Şek ile yakîn zâil olmaz.” • “Zarar izâle olunur.”', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Mecelle yalnız Hanefî mezhebini esas alırken; 1917 Hukuk-ı Aile Kararnamesi dört Sünnî mezhepten yararlanmıştır.', '#334155', 10, 'normal', 'middle'))

    kaydet('10-fikih-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
