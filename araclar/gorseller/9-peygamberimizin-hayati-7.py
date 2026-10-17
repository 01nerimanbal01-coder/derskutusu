from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('peygamberimizin-hayati')
    ic = []
    ic.append(P.baslik(400, 32, 'İSLAM ÖNCESİ MEKKE’DE EKONOMİK, KÜLTÜREL VE DİNÎ HAYAT', R['koyu']))

    # Sol panel: Ekonomik ve Kültürel Hayat (Îlâf, Kervanlar, Panayırlar, Şiir)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. EKONOMİK VE KÜLTÜREL YAPI (TİCARET VE ŞİİR)', R['koyu'], 11.5, 'bold', 'middle'))

    sol = [
        (100, 'Kuzey-Güney Kervan Ticareti (Kureyş Suresi)', 'Kışın Yemen’e (güney), yazın Şam’a (kuzey) düzenlenen büyük ticaret kervanları.'),
        (150, 'Îlâf Antlaşmaları (Hâşim bin Abdümenâf)', 'Komşu devletlerle yapılan ticaret güvenliği ve serbest geçiş antlaşmaları.'),
        (200, 'Ünlü Arap Panayırları (Ukâz, Mecenne, Zülmecâz)', 'Hac mevsimi öncesi kurulan ekonomik ticaret ve edebî yarışma pazarları.'),
        (250, 'Sözlü Kültür, Şiir ve Hitabet (Edebiyat)', 'Beğenilen 7 şairin şiirlerinin Kâbe duvarına asılması: Muallakât-ı Seb’a!'),
        (300, 'Cahiliye Ekonomisindeki Haksızlıklar', 'Ağır tefecilik (riba/faiz), ölçü-tartı hilesi ve borcunu ödeyemeyenin köleleştirilmesi.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Dini Yapı (Putperestlik ve Haniflik)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. DİNÎ YAPI: PUTPERESTLİK VE HANİFLER', '#92400e', 11.5, 'bold', 'middle'))

    sag = [
        (100, 'Mekke’ye Putperestliğin Girişi (Amr bin Luhay)', 'Tevhid kıblesi olan Kâbe’nin içine ve çevresine 360 put yerleştirilmesi.'),
        (150, 'Müşriklerin Allah İnancı ve Putları Aracı Kılması', 'Yaratıcı olarak Allah’ı kabul edip “Putlar bizi Allah’a yaklaştırıyor” (Zümer 3) demeleri.'),
        (200, 'Haram Aylar Uygulaması (4 Ay)', 'Zilkade, Zilhicce, Muharrem ve Recep aylarında savaşın yasaklanması (Ficâr hariç).'),
        (250, 'Hanîflik (Hz. İbrahim’in Tevhid Dinini Koruyanlar)', 'Putlara tapmayan, içki içmeyen, diri diri kız gömmeye karşı çıkan tevhid ehli.'),
        (300, 'Mekke’deki Başlıca Hanîf Şahsiyetler', 'Zeyd bin Amr, Kus bin Sâide, Varaka bin Nevfel ve bizzat Hz. Muhammed (s.a.v.)!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ KAVRAMLAR: Îlâf = Ticaret güvenlik antlaşması | Ukâz = En büyük panayır | Muallakât-ı Seb’a = Kâbe’ye asılan 7 şiir!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Haram aylarda (Zilkade, Zilhicce, Muharrem, Recep) yapılan savaşlara “hukuku çiğneyen savaş” anlamında FİCÂR SAVAŞLARI denmiştir.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('9-peygamberimizin-hayati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
