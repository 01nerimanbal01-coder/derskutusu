from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'DİNLER TARİHİ: İSLAMİYET’İN TARİHÇESİ VE EVRENSEL YAYILIŞI', R['koyu']))

    # Sol panel: İslam Kavramı ve Asr-ı Saadet (Mekke - Medine)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İSLAM KAVRAMI VE ASR-I SAÂDET DÖNEMİ', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'İslam Kavramı: Tevhid Halkasının Sonuncusu', 'Barış, esenlik ve Allah’a teslimiyet. Hz. Âdem’den Hz. Muhammed’e tüm peygamberlerin ortak dini.'),
        (150, 'Vahyin Başlangıcı (610 — Hira Mağarası)', 'Alak Suresi 1-5. ayetlerle nübüvvetin başlaması; Hz. Hatice, Hz. Ali, Hz. Ebû Bekir ve Zeyd’in imanı.'),
        (200, 'Mekke Dönemi (610 - 622: 13 Yıl)', 'Tevhid, ahiret ve ahlak vurgusu; Habeşistan hicretleri, Boykot (616-619), Taif ve Akabe Biatları.'),
        (250, 'Hicret (622) ve Medine Dönemi (622 - 632: 10 Yıl)', 'Mescid-i Nebevî, Muâhât, Medine Vesîkası; Bedir (624), Uhud (625) ve Hendek (627) savunmaları.'),
        (300, 'Hudeybiye (628), Mekke’nin Fethi (630) ve Veda', 'İslam’a davet mektupları, Mekke’nin fethi, Veda Hutbesi (632) ve dinin kemâle ermesi (Mâide, 3).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.0, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Hulefâ-yi Râşidîn ve İslam Medeniyetinin Yayılışı
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HULEFÂ-Yİ RÂŞİDÎN VE EVRENSEL YAYILIŞ', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Hz. Ebû Bekir Dönemi (632 - 634)', 'Yalancı peygamberler ve ridde olaylarının bastırılması; Kur’an-ı Kerim’in Mushaf haline getirilmesi.'),
        (150, 'Hz. Ömer Dönemi (634 - 644)', 'Suriye, Kudüs, Mısır, Irak ve İran’ın fethi; Hicrî takvim, divan ve adliye teşkilatının kurulması.'),
        (200, 'Hz. Osman (644-656) ve Hz. Ali (656-661)', 'Kur’an nüshalarının çoğaltılması, ilk İslam donanması, Kıbrıs ve Kuzey Afrika fetihleri.'),
        (250, 'Emevîler ve Abbâsîler Dönemi', 'Endülüs’ten (İspanya) Mâverâünnehir’e (Orta Asya) yayılış; Beytü’l-Hikme ve İslam Rönesansı.'),
        (300, 'Türklerin İslam’a Hizmeti ve Küresel Yayılış', 'Karahanlı, Gazneli, Selçuklu ve Osmanlı ile Anadolu/Balkanlar; tüccarlarla Güneydoğu Asya.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.0, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ TESPİT: İslamiyet yeni türetilmiş bir din değil; Hz. Âdem’den beri gönderilen ilahi tevhid mesajının Hz. Muhammed (s.a.v.) ile kemale eren son halkasıdır!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Endonezya ve Malezya gibi dünyanın en kalabalık Müslüman nüfuslu bölgeleri askeri seferle değil, Müslüman tüccar ve sûfîlerin güzel ahlakıyla İslamlaşmıştır.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('11-dinler-tarihi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic