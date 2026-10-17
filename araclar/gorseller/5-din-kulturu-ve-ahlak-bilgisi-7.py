from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'İHLAS SURESİ’NİN MESAJLARI VE 1. ÜNİTE (ALLAH İNANCI) ÖZETİ', R['koyu']))

    # Sol panel: İhlas Suresi Ayet Ayet Tevhid Mesajı
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İHLAS SURESİ’NİN DÖRT TEMEL İLKESİ', R['koyu'], 13, 'bold', 'middle'))

    ayetler = [
        (100, '1. Ayet: قُلْ هُوَ اللّٰهُ أَحَدٌ (El-Ehad)', 'De ki: O Allah BİR ve TEKTİR! (Tevhid İnancı)'),
        (150, '2. Ayet: اَللّٰهُ الصَّمَدُ (Es-Samed)', 'Her şey O’na muhtaçtır; O hiçbir şeye muhtaç değildir!'),
        (200, '3. Ayet: لَمْ يَلِدْ وَلَمْ يُولَدْ (Ezelî ve Ebedî)', 'Doğurmamış ve doğmamıştır (Çocuğu, annesi-babası yoktur).'),
        (250, '4. Ayet: وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ (Benzersiz)', 'Hiçbir şey O’nun dengi, eşi ve benzeri değildir!'),
        (300, 'İhlas Kavramı (Samimiyet)', 'İbadetleri gösterişten (riya) uzak, yalnız Allah için yapmak.'),
    ]
    for y, b, a in ayetler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: 1. Ünite (Allah İnancı) Bütüncül Kavram Haritası
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. 1. ÜNİTE: ALLAH İNANCI KAVRAM HARİTASI', '#92400e', 13, 'bold', 'middle'))

    unite = [
        (100, 'Evrendeki Mükemmel Ölçü ve Düzen', 'Gece-gündüz, mevsimler, su döngüsü → Tesadüf olamaz!'),
        (150, 'Tevhid ve Kelime-i Tevhid', 'Lâ ilâhe illallah Muhammedün Resûlullah (Enbia 21/22).'),
        (200, 'Esmâ-i Hüsnâ (Allah’ın Güzel İsimleri)', 'Er-Rahmân, Er-Rahîm, El-Hâlık, El-Alîm, Es-Semî’, El-Basîr, El-Kâdir.'),
        (250, 'Allah İle İletişim: Dua', 'Sevinçte şükürle, darlıkta sabırla her an Rabbimize yönelmek.'),
        (300, 'Tevhid İnancının Ahlaka Etkisi', 'Dürüstlük, merhamet, emaneti koruma ve sorumluluk bilinci.'),
    ]
    for y, b, a in unite:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ENBİYÂ SURESİ 22. AYET: "Eğer yerde ve gökte Allah’tan başka ilahlar olsaydı, kesinlikle ikisinin de düzeni bozulurdu!"', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'El-Alîm: Her şeyi bilen | Es-Semî’: Her şeyi işiten | El-Basîr: Her şeyi gören | El-Kâdir: Her şeye gücü yeten.', '#334155', 11, 'normal', 'middle'))

    kaydet('5-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
