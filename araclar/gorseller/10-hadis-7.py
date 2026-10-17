from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'HADİSLERDEN MESAJLAR: KUR’AN VE SÜNNETE BAĞLILIK (SEKALEYN)', R['koyu']))

    # Sol panel: İki Emanet (Sekaleyn) ve Kur'an'da Resul'e İtaat
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İKİ BÜYÜK EMANET VE KUR’AN DELİLLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Veda Hutbesi’ndeki İki Emanet (Emreyn)', '“Size iki şey bırakıyorum; sarıldığınız sürece sapmazsınız: Kitap ve Sünnet.”'),
        (150, 'Nisâ Suresi 80. Ayet', '“Kim Resûl’e itaat ederse gerçekte Allah’a itaat etmiş olur.”'),
        (200, 'Haşr Suresi 7. Ayet', '“Peygamber size ne verdiyse onu alın; sizi neden menettiyse ondan sakının!”'),
        (250, 'Nahl Suresi 44. Ayet (Tebyîn Görevi)', '“İnsanlara indirileni açıklayasın (beyân edesin) diye sana bu Kur’an’ı indirdik.”'),
        (300, 'Âl-i İmrân Suresi 31. Ayet', '“De ki: Eğer Allah’ı seviyorsanız bana uyun ki Allah da sizi sevsin.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Sünnetin 3 İşlevi ve Erîke Hadisi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SÜNNETİN İŞLEVLERİ VE ERÎKE HADİSİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, '1. Te’kîd (Pekiştirme ve Destekleme)', 'Kur’an’da yer alan iman, ibadet ve ahlak hükümlerini teyit edip güçlendirmesi.'),
        (150, '2. Beyân / Tebyîn (Açıklama Görevi)', 'Mücmel ayetleri açıklaması (namaz rekâtları, zekât nisabı, hac uygulamaları).'),
        (200, 'Beyânın Alt Türleri: Tafsîl, Tahsîs, Takyîd', 'Özlü olanı detaylandırma, genel hükmü özelleştirme ve mutlak olanı kayıtlandırma.'),
        (250, '3. Teşrî’ (Müstakil Hüküm Koyma)', 'Kur’an’da açıkça geçmeyen konularda Allah’ın izniyle helal/haram hükmü koyması.'),
        (300, 'Erîke (Koltuk) Hadisi ile Nebevî Uyarı', '“Koltuğuna yaslanıp bize yalnız Kur’an yeter diyenler çıkacaktır; dikkat edin!”'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, '«تَرَكْتُ فِيكُمْ أَمْرَيْنِ لَنْ تَضِلُّوا مَا تَمَسَّكْتُمْ بِهِمَا: كِتَابَ اللّٰهِ وَسُنَّةَ نَبِيِّهِ» (Muvatta, Kader, 3)', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kur’an ve Sünnet etle tırnak gibidir; Sünnet olmadan Kur’an’ın anlaşılması ve İslam’ın yaşanması mümkün değildir!', '#334155', 10, 'normal', 'middle'))

    kaydet('10-hadis-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
