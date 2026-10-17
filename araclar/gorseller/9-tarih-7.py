from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('tarih')
    ic = []
    ic.append(P.baslik(400, 32, 'TARİHSEL BİLGİNİN ÜRETİM SÜRECİ: 5T YÖNTEMİ VE DİJİTAL TARİHÇİLİK', R['koyu']))

    # Sol panel: Tarih Araştırma Yönteminin 5 Basamağı (5T)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. TARİH ARAŞTIRMA BASAMAKLARI (5T YÖNTEMİ)', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, '1. Tarama (Kaynak Arama)', 'Konuyla ilgili birinci ve ikinci elden tüm kaynakların (arşiv, buluntu) toplanması.'),
        (150, '2. Tasnif (Sınıflandırma)', 'Toplanan kaynakların zamana, mekâna ve konuya göre ayrılması.'),
        (200, '3. Tahlil (Çözümleme)', 'Kaynaklardaki bilgilerin araştırma için yeterli ve kullanışlı olup olmadığının kontrolü.'),
        (250, '4. Tenkit (Eleştiri — İç ve Dış Tenkit)', 'Dış Tenkit: Eserin orijinalliği/künyesi | İç Tenkit: Yazarın tarafsızlığı ve doğruluğu.'),
        (300, '5. Terkip (Sentez — Eseri Yazma)', 'Doğruluğu sınanmış bilgilerin birleştirilerek tarih eserinin kaleme alınması.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Dijital Tarihçilik ve Tarih Yazımı Etiği
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. DİJİTAL TARİHÇİLİK VE NESNELLİK İLKESİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Dijitalleşme ve Dijital Arşivler', 'Fiziksel belgelerin taranarak (sayısallaştırma) küresel erişime açılması.'),
        (150, 'Büyük Veri (Big Data) ve CBS / Yapay Zekâ', 'Osmanlı tahrir defterleri ve haritaların dijital araçlarla hızlı analizi.'),
        (200, 'Dijital Kaynaklarda Tenkit (Doğrulama) Zorunluluğu', 'İnternetteki sahte/manipüle edilmiş bilgilere karşı çapraz kaynak kontrolü!'),
        (250, 'Anakronizmden Kaçınma İlkesi', 'Geçmişteki bir olayı yaşandığı dönemin şartları ve değerleriyle değerlendirmek.'),
        (300, 'Tarihsel Bilginin Değişebilirliği', 'Yeni bir belge veya arkeolojik buluntu çıktığında tarihsel bilgi güncellenir!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DIŞ TENKİT vs. İÇ TENKİT: “Belge sahte mi, ne zaman/kim yazdı?” -> DIŞ TENKİT | “Yazar doğru mu söylüyor, tarafsız mı?” -> İÇ TENKİT!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Göbeklitepe veya Karahantepe kazıları gibi yeni buluntular, eski tarihsel bilgileri değiştirebilir (tarihsel bilginin dinamik yapısı).', '#334155', 9.8, 'normal', 'middle'))

    kaydet('9-tarih-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
