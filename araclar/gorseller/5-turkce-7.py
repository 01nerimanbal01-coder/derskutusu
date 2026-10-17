from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turkce')
    ic = []
    ic.append(P.baslik(400, 32, 'ATATÜRK’Ü TANIMAK: "MUSTAFA" METNİ, HİKÂYE UNSURLARI VE BAĞLAÇLAR', R['koyu']))

    # Sol panel: Hikâye Unsurları & Gerçek / Kurgusal Unsurlar
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HİKÂYE UNSURLARI & GERÇEK - KURGU', R['koyu'], 13, 'bold', 'middle'))

    unsurlar = [
        (100, 'Olay Örgüsü (Ne Oldu?)', 'Küçük Mustafa’nın Selanik’te okul hayatı ve öğrenme tutkusu.'),
        (148, 'Şahıs ve Varlık Kadrosu (Kim?)', 'Ana karakter: Mustafa; Yardımcı: Zübeyde Hanım, Ali Rıza Efendi, Öğretmeni.'),
        (196, 'Mekân / Yer ve Zaman (Nerede - Ne Zaman?)', 'Selanik, Şemsi Efendi Okulu, Askerî Rüştiye (Çocukluk yılları).'),
        (244, 'Gerçek Unsurlar (Yaşanabilir / Tarihî)', 'Mustafa’nın okula gitmesi, öğretmenin ona "Kemal" adını vermesi.'),
        (292, 'Kurgusal (Hayalî) Unsurlar', 'Yazarın metni zenginleştirmek için kurguladığı hayalî ayrıntılar.'),
    ]
    for y, b, a in unsurlar:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Geçiş ve Bağlantı İfadeleri + Noktalama İşaretleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. GEÇİŞ İFADELERİ VE NOKTALAMA İŞARETLERİ', '#92400e', 13, 'bold', 'middle'))

    sag = [
        (100, 'Düşüncenin Yönünü Değiştirenler', 'ama, fakat, lakin, ancak, oysa, buna rağmen, ne var ki'),
        (148, 'Destekleyici ve Açıklayıcı İfadeler', 'özellikle, örneğin, hatta, üstelik, açıkçası, başka bir deyişle'),
        (196, 'Özetleyen ve Sonuç Bildiren İfadeler', 'kısacası, özetle, sonuç olarak, böylece, gördüğünüz gibi'),
        (244, 'Nokta (.) ve Virgül (,)', 'Tamamlanmış cümle sonuna (.); eş görevli sözcükler arasına (,).'),
        (292, 'İki Nokta (:) ve Konuşma Çizgisi (—)', 'Açıklama ve konuşmadan önce (:); satır başı diyalogda (—).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 15, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ANA FİKİR (MESAJ): Azimle çalışmak, kitap okumak ve vatan sevgisi insanı büyük hedeflere ulaştırır.', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Yazım Kuralı: Özel adlara (Mustafa’nın, Selanik’te, Türkçe’yi değil → Türkçeyi!) gelen çekim ekleri kesme işaretiyle ayrılır, yapım ekleri ayrılmaz!', '#334155', 10, 'normal', 'middle'))

    kaydet('5-turkce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
