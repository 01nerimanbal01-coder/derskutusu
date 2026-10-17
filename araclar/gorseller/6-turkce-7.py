from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turkce')
    ic = []
    ic.append(P.baslik(400, 32, 'BAĞIMSIZLIK YOLU: "CEPHEYE KOŞAN AT", DEYİMLER VE TAMLAMALAR', R['koyu']))

    # Sol panel: "Cepheye Koşan At" Metni, Anlatıcı ve Deyimler
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HİKÂYE UNSURLARI, ANLATICI VE DEYİMLER', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, '"Cepheye Koşan At" Metninin Teması', 'Millî Mücadele ruhu, vatan sevgisi ve fedakârlık.'),
        (148, '1. Kişili (Kahraman) Anlatıcı Bakış Açısı', '"Gittim, gördüm, koştum" (Olayı yaşayan kahraman anlatır).'),
        (196, '3. Kişili (Gözlemci / Hâkim) Anlatıcı', '"Gitti, gördü, koştu" (Olayı dışarıdan izleyen anlatır).'),
        (244, 'Deyimler (En Az İki Sözcük, Kalıplaşmış)', 'Mecaz anlamlı, mastar (-mak/-mek) ekiyle biten kalıplar:'),
        (292, 'Metindeki Deyim Örnekleri', 'Kulak kabartmak • Gözden kaybolmak • Canını dişine takmak.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: İsim (Ad) Tamlamaları ve Sıfat Tamlamaları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İSİM VE SIFAT TAMLAMALARI', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, 'Tamlayan (1. Sözcük) + Tamlanan (2. Sözcük)', 'İki veya daha fazla sözcüğün anlamca bütünleşmesidir.'),
        (148, '1. Belirtili İsim Tamlaması (İkisi de Ek Alır)', '"At-ın yele-si", "Vatan-ın bağımsızlığ-ı" (Neyin / Kimin?)'),
        (196, '2. Belirtisiz İsim Tamlaması (Sadece 2.si Ek Alır)', '"Cephe yol-u", "Kurtuluş Savaş-ı" (Ne sorusuna cevap verir)'),
        (244, '3. Zincirleme İsim Tamlaması (En Az 3 İsim)', '"Anadolu insan-ının vatan sevgi-si", "Okul bahçe-sinin kapı-sı"'),
        (292, 'Sıfat Tamlaması (Sıfat + İsim — Ek Şart Değil)', '"Cesur asker", "Yorgun at", "Bu vatan", "Üç cephe" (Nasıl/Hangi/Kaç?)'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 15, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'AYIRT ETME İPUCU: İsim tamlamasında 2. sözcük mutlaka iyelik eki (-ı/-i/-sı/-si) alır ("devlet bayrağı"); Sıfat tamlamasında ek almaz ("kırmızı bayrak")!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Deyim vs. Atasözü: Deyimler durum betimler (yargı/öğüt vermez: "göze girmek"); Atasözleri ise tam cümledir ve öğüt verir ("Damlaya damlaya göl olur").', '#334155', 10, 'normal', 'middle'))

    kaydet('6-turkce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
