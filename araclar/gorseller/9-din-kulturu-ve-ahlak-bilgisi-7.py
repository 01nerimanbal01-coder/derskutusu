from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'KUR’AN’DAN MESAJLAR: RÛM SURESİ 20-27. AYETLER VE KÂİNATTAKİ DELİLLER', R['koyu']))

    # Sol panel: Rûm Suresi 20-23. Ayetler (İnsanın Yaratılışı, Eşler, Diller ve Uyku)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İNSANDAKİ AYETLER (DELİLLER): RÛM 20-23', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Rûm 20 — Topraktan Yaratılış (İlk Yaratılış)', 'İnsanın topraktan (türâb) yaratılıp yeryüzüne yayılan beşer olması.'),
        (150, 'Rûm 21 — Eşler Arasında Meveddet ve Rahmet', 'Huzur (sekînet) bulmak için eşler yaratılması, sevgi ve merhamet bağı.'),
        (200, 'Rûm 22 — Dillerin ve Renklerin Farklılığı', 'Göklerin-yerin yaratılışı ile dillerin ve ten renklerinin çeşitliliği birer ayettir!'),
        (250, 'Rûm 23 — Gece-Gündüz Uyku ve Rızık Arayışı', 'Gece ve gündüz uyumanız ve Allah’ın lütfundan rızık aramanız O’nun delillerindendir.'),
        (300, 'Kimler İçin Delildir? (Muhatap Vurgusu)', 'Düşünenler (yetefekkerûn), bilenler (ya’lemûn) ve işitenler (yesmeûn) için!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Rûm Suresi 24-27. Ayetler (Kâinattaki Düzen ve Yeniden Diriliş)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KÂİNATTAKİ DÜZEN VE AHİRET: RÛM 24-27', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Rûm 24 — Şimşek (Korku ve Ümit) ve Yağmur', 'Şimşeğin korku ve ümit vermesi; yağmurla ölü toprağın diriltilmesi (haşir delili!).'),
        (150, 'Rûm 25 — Göğün ve Yerin Allah’ın Emriyle Durması', 'Kâinattaki kusursuz düzen ve bir çağrıyla yerden çıkacak olma (kıyamet).'),
        (200, 'Rûm 26 — Göklerde ve Yerdekilerin O’na İtaati', 'Kâinattaki her varlık Allah’ındır ve hepsi O’na boyun eğmiştir (kânitûn).'),
        (250, 'Rûm 27 — Yaratmayı Başlatan ve Tekrar Eden (Muîd)', 'İlk kez yaratan Allah için yeniden diriltmek (iâde) çok daha kolaydır!'),
        (300, 'El-Azîz ve El-Hakîm İsimleri (Esmâ-i Hüsnâ)', 'En yüce sıfatlar O’nundur; O mutlak güç (Azîz) ve hikmet (Hakîm) sahibidir.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ANAHTAR KAVRAM: Kur’an’da “Âyet (çoğulu: Âyât)” hem sureleri oluşturan cümleler hem de Allah’ın varlığının KÂİNATTAKİ DELİLLERİ demektir!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Rûm 20-27. ayetlerde tam 6 kez “Ve min âyâtihî... (O’nun varlığının ve kudretinin delillerindendir ki...)” ifadesi tekrarlanmaktadır.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
