from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'PEYGAMBERİMİZİN HAYATI: TAİF DAVETİ, SABIR VE İSLAMLAŞMA', R['koyu']))

    # Sol panel: Taif Yolculuğu, Tepki, Dua ve Addâs
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TAİF DAVETİ (620), DUA VE ADDÂS', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Sakîf İleri Gelenlerinin Tepkisi', 'Abdüyâlîl, Mes’ûd ve Habîb daveti kibir ve alayla reddedip halkı kışkırttı.'),
        (150, 'Taşlanma ve Zeyd b. Hârise’nin Vefası', 'Ayaktakımı Peygamberimizi taşladı; Zeyd b. Hârise bedenini O’na siper etti.'),
        (200, 'Utbe ve Şeybe’nin Bağında Taif Duası', '“Eğer Senin bana gazabın yoksa çektiğim sıkıntılara hiç aldırmam...”'),
        (250, 'Ninovalı Hıristiyan Köle Addâs’ın İmanı', '“Bismillâh” sözü ve Hz. Yûnus’un kardeşi olduğunu duyunca Müslüman oldu.'),
        (300, 'Dağlar Meleği ve Rahmet Peygamberi', 'Helak teklifini reddetti: “Soylarından yalnız Allah’a kul olanlar çıkmasını ümit ederim.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Mekke'ye Dönüş, Kuşatma ve Taif'in Müslüman Oluşu
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. DÖNÜŞ, KUŞATMA VE TAİF’İN İSLAMLAŞMASI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Nahle Vadisi’nde Cinlerin İmanı', 'Sabah namazında Kur’an dinleyen cin grubu iman etti (Ahkâf ve Cin sureleri).'),
        (150, 'Mut’im b. Adîy’in Emanıyla Mekke’ye Giriş', 'Oğullarıyla silahlanan Mut’im b. Adîy’in himayesiyle Mekke’ye güvenle girdi.'),
        (200, 'Taif Kuşatması (8 H. / 630) ve Hidayet Duası', '“Allah’ım! Sakîf kabilesine hidayet ver ve onları Müslüman olarak bize getir!”'),
        (250, 'Urve b. Mes’ûd’un Şehadeti ve Taif Heyeti (631)', 'Abdüyâlîl başkanlığındaki Sakîf Heyeti 9 H. yılında Medine’de Müslüman oldu.'),
        (300, 'İlkeli Kabul ve Osman b. Ebü’l-Âs’ın Valiliği', 'Faiz/içki/put şartları reddedildi; Lât yıkıldı, genç sahabi Osman vali atandı.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, '620 yılında Taif’te taşlanırken yapılan rahmet ve hidayet duası, 11 yıl sonra (631) tüm Taif’in kendi rızasıyla İslam’a girmesiyle kabul olmuştur!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hz. Peygamber insanlara karşı sonsuz şefkatli davranmış; ancak tevhid, namaz ve ahlak ilkelerinden asla taviz vermemiştir.', '#334155', 10, 'normal', 'middle'))

    kaydet('10-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
