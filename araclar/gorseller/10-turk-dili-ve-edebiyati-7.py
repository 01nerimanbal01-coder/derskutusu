from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turk-dili-ve-edebiyati')
    ic = []
    ic.append(P.baslik(400, 32, '1. TEMA: SÖZÜN EZGİSİ — ANLATMA (KONUŞMA-YAZMA) VE SES OLAYLARI', R['koyu']))

    # Sol panel: Konuşma ve Yazma (Koşuk/Türkü/Masal Üretimi ve Sözlü Geleneğimiz)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SÖZÜN EZGİSİ: KONUŞMA VE YAZMA SÜRECİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Temanın Özü: Sözlü Kültürden Yazılı Kültüre Ezgi', 'Koşuk, ilahi, nefes, türkü ve masal türlerindeki ahenk ve ritim unsurları.'),
        (150, 'Masal Anlatıcılığı (Meddah / Masal Анаsı Üslubu)', 'Döşeme (tekerleme), olay, dilek bölümleri; vurgu, tonlama ve beden dili.'),
        (200, 'Şiir ve Anlatı Yazma: Ahenk Unsurlarını Kullanma', 'Hece ölçüsü, durak, redif, kafiye, aliterasyon ve asonansla ahenk kurma.'),
        (250, 'Söz Sanatları ile İmge Oluşturma', 'Teşbih (benzetme), istiare (eğretileme), teşhis (kişileştirme), telmih.'),
        (300, 'Çok Modlu Metin ve Dijital Hikâye/Masal Sunumu', 'Metni görsel, müzik (ezgi) ve seslendirmeyle bütünleştirerek sunma.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Dil Bilgisi — Ses Olayları ve Yazım-Noktalama
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. TÜRKÇEDE SES OLAYLARI VE YAZIM KURALLARI', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Ünlü Düşmesi (Hece Düşmesi) ve Ünlü Daralması', 'gönül-ü -> gönlü, ayır-ıntı -> ayrıntı | bekle-yor -> bekliyor, de-ye -> diye.'),
        (150, 'Ünsüz Yumuşaması (Değişimi: p, ç, t, k -> b, c, d, ğ)', 'ağaç-ı -> ağacı, kalp-i -> kalbi, git-en -> giden (Tek heceli/özel adlarda olmaz).'),
        (200, 'Ünsüz Benzeşmesi (Sertleşmesi: Fıstıkçı Şahap)', 'f, s, t, k, ç, ş, h, p + c, d, g -> ç, t, k (Örn: seç-kin, 1923’te, kitap-ta).'),
        (250, 'Ünsüz Türemesi ve Kaynaştırma (y, ş, s, n)', 'af-etmek -> affetmek, hak-ı -> hakkı | su-y-u, iki-ş-er (beş-er’de ş kaynaştırma değil!).'),
        (300, 'Ulama ve N-B Çatışması (Dudak Ünsüzü Benzeşmesi)', 'Ünsüzle biten + ünlüyle başlayan (dün_akşam) | saklambaç, çember, tembel (n->m).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: “de-” ve “ye-” fiilleri dışındaki kelimelerde “-y-” kaynaştırma harfi daralma YAPMAZ (anlayacak, ağlayarak -> DOĞRU)!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Birleşik kelimelerde ve türetilirken ünlü düşmesi (kayın+ana -> kaynana, kavuş+ak -> kavşak, uyu+ku -> uyku) sıkça sorulur!', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-turk-dili-ve-edebiyati-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
