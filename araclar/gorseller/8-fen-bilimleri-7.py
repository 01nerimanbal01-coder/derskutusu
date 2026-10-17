from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('fen-bilimleri')
    ic = []
    ic.append(P.baslik(400, 32, 'KALITIM: CİNSİYETE BAĞLI KALITIM, SOY AĞAÇLARI VE AKRABA EVLİLİĞİ', R['koyu']))

    # Sol panel: İnsanda Cinsiyetin Belirlenmesi (44 + XX / 44 + XY)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İNSANDA CİNSİYETİN BELİRLENMESİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'İnsanda 46 Kromozomun Dağılımı', '44 Vücut Kromozomu + 2 Eşey (Cinsiyet) Kromozomu = 46.'),
        (150, 'Dişi (Kadın) ve Erkek Eşey Kromozomları', 'Dişi (Anne): 44 + XX   |   Erkek (Baba): 44 + XY.'),
        (200, 'Cinsiyet Çaprazlaması: XX  ×  XY', 'Oluşan yavrular: %50 XX (Kız) ve %50 XY (Erkek) -> Olasılık 1/2!'),
        (250, 'Bebeğin Cinsiyetini Hangi Ebeveyn Belirler?', 'Anneden daima X gelir; Babadan X veya Y geldiği için BABA belirler!'),
        (300, 'Önceki Doğumlar Sonraki Doğumu Etkiler mi?', 'Hayır! 5 kız çocuktan sonra 6. çocuğun erkek olma ihtimali yine %50’dir!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Soy Ağaçları ve Akraba Evliliğinin Genetik Sonuçları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SOY AĞAÇLARI VE AKRABA EVLİLİĞİ', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'Soy Ağacı (Pedigri) Sembolleri', 'Daire (○) = Dişi | Kare (□) = Erkek | Boyalı = Özelliği gösteren.'),
        (150, 'Soy Ağacında Çekinik (aa) Bulma Taktiği', 'Sağlam anne-babadan (Aa × Aa) hasta çocuk (aa) doğabilir!'),
        (200, 'Taşıyıcı Birey (Heterozigot — Aa) Nedir?', 'Kendisisi sağlam görünümlü olup hastalık genini (a) taşıyan birey.'),
        (250, 'Akraba Evliliğinin Genetik Sakıncası', 'Çekinik hastalık genlerinin (a ile a) bir araya gelme (aa) ihtimalini artırır!'),
        (300, 'Kalıtsal Hastalık Örnekleri', 'Orak hücreli anemi, Akdeniz anemisi, kistik fibrozis, hemofili, renk körlüğü.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'LGS UYARISI: Akraba evliliği YENİ BİR HASTALIK GENİ (MUTASYON) OLUŞTURMAZ; var olan çekinik genlerin buluşma ihtimalini artırır!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Soy ağacında çekinik (aa) bireyin hem annesinde hem babasında mutlaka en az bir tane küçük "a" aleli bulunmak zorundadır!', '#334155', 10.5, 'normal', 'middle'))

    kaydet('8-fen-bilimleri-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
