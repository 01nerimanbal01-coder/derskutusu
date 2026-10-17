from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turk-dili-ve-edebiyati')
    ic = []
    ic.append(P.baslik(400, 32, 'HİKÂYE METİNLERİNDE KELİMEDE ANLAM, İMLA VE NOKTALAMA', R['koyu']))

    # Sol panel: Hikâyede Kelimede Anlam ve Anlam Olayları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HİKÂYEDE KELİMEDE ANLAM KATMANLARI', R['koyu'], 13, 'bold', 'middle'))
    katmanlar = [
        (100, 'Gerçek (Temel) Anlam', 'Sözcüğün akla gelen ilk, sözlük anlamı'),
        (148, 'Yan Anlam (Yakıştırma)', 'Şekil/işlev benzerliği (masanın gözü, kapı kolu)'),
        (196, 'Mecaz (Değişmece) Anlam', 'Gerçek anlamdan tamamen uzaklaşma (ince fikir)'),
        (244, 'Terim Anlam', 'Bilim/sanat dalına özgü kavram (bilinç akışı, tema)'),
        (292, 'Çok Anlamlılık & Bağlam', 'Sözcüğün cümle içinde kazandığı yeni anlam değeri'),
    ]
    for y, b, a in katmanlar:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Hikâye Metinlerinde İmla ve Noktalama
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. HİKÂYEDE İMLA VE NOKTALAMA İLKELERİ', '#92400e', 13, 'bold', 'middle'))
    kurallar = [
        (100, 'Diyaloglarda Uzun Çizgi (—) ve Tırnak (" ")', 'Konuşma çizgisinden sonra cümle sonunda tırnak KULLANILMAZ!'),
        (152, 'İç Konuşma ve Alıntılarda Tırnak (" ")', 'Kahramanın zihninden geçen cümleler tırnak içine alınır.'),
        (204, 'Bilinç Akışı ve Eksiltili Cümlede Üç Nokta (...)', 'Yüklemi olmayan, zihinsel çağrışımlarla kesilen cümle sonları.'),
        (256, 'Birleşik Kelimelerin Yazımı (Bitişik / Ayrı)', 'Ses düşmesi/anlam kaybı varsa bitişik: kaynana, bülbülyuvası.'),
    ]
    for y, b, a in kurallar:
        ic.append(P.kutu(415, y, 350, 44, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 34, a, '#334155', 10, 'normal', 'middle'))

    ic.append(P.kutu(415, 308, 350, 28, '#fef2f2', '#dc2626'))
    ic.append(P.metin(590, 326, 'DİKKAT: Zarffiil eklerinden (-ıp, -arak, -ınca) sonra VİRGÜL KONMAZ!', '#b91c1c', 10, 'bold', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f8fafc', R['orta']))
    ic.append(P.metin(400, 380, 'ANLAM AKTARMALARI: İstiare (Benzetme) • Mecazımürsel (Ad Aktarması) • Deyim Aktarması (İnsandan Doğaya / Duyular Arası)', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Örnek: "Acı bir çığlık odada yankılandı." (Duyular arası aktarma: tatma → işitme)', '#334155', 11, 'normal', 'middle'))

    kaydet('12-turk-dili-ve-edebiyati-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic