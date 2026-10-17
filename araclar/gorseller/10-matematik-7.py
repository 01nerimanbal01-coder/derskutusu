from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('matematik')
    ic = []
    ic.append(P.baslik(400, 32, 'İSTATİSTİKSEL ARAŞTIRMA: İKİ KATEGORİK DEĞİŞKENLİ VERİLER', R['koyu']))

    # Sol panel: İki Yönlü Sıklık Tabloları ve Göreli Sıklık Türleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İKİ YÖNLÜ TABLO VE GÖRELİ SIKLIK TÜRLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Kategorik (Nitel) Değişken Nedir?', 'Sayısal ölçüm yerine sınıflandırma belirten değişken (cinsiyet, dal, kan grubu).'),
        (150, 'İki Yönlü Sıklık (Çapraz) Tablosu', 'Satırlarda 1. kategorik değişken, sütunlarda 2. kategorik değişken yer alır.'),
        (200, 'Marjinal (Kenar) Toplam ve Marjinal Göreli Sıklık', 'Satır veya sütun toplamının genel toplama (N) oranıdır.'),
        (250, 'Birleşik (Ortak) Göreli Sıklık', 'Tablo içindeki bir hücre değerinin (f_ij) genel toplama (N) oranıdır (f_ij / N).'),
        (300, 'Koşullu Göreli Sıklık (Satır veya Sütun Koşullu)', 'Hücre değerinin yalnızca ilgili SATIR veya SÜTUN toplamına oranıdır!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Görselleştirme ve İlişki (Bağımsızlık) Yorumu
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SÜTUN GRAFİKLERİ VE İLİŞKİ ANALİZİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'İstatistiksel Araştırma Süreci (4 Adım)', '1) Soru Oluşturma -> 2) Veri Toplama -> 3) Analiz -> 4) Sonuç Yorumlama.'),
        (150, 'Kümelenmiş (Yan Yana) Sütun Grafiği', 'Her ana kategori için alt kategorilerin sütunları yan yana çizilerek karşılaştırılır.'),
        (200, 'Yığılmış (%100 Oransal) Sütun Grafiği', 'Koşullu göreli sıklıkları (% dağılımı) tek sütun içinde üst üste gösterir.'),
        (250, 'İki Kategorik Değişken Arasında İlişki Var mı?', 'Koşullu göreli sıklıklar satırdan satıra belirgin değişiyorsa İLİŞKİ VARDIR!'),
        (300, 'İlişki Olmaması (Bağımsızlık) Durumu', 'Koşullu yüzdeler her grupta birbirine çok yakınsa değişkenler ilişkisizdir.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: “Katılımcıların yüzde kaçı...” derse paydaya GENEL TOPLAM (Birleşik); “Kızların yüzde kaçı...” derse KIZ TOPLAMI (Koşullu) yazılır!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Farklı büyüklükteki grupları karşılaştırırken sıklık (kişi sayısı) değil, KOŞULLU GÖRELİ SIKLIK (%) kullanılmalıdır!', '#334155', 10, 'normal', 'middle'))

    kaydet('10-matematik-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
