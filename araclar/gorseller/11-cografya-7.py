from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('cografya')
    ic = []
    ic.append(P.baslik(400, 32, 'TÜRKİYE’NİN SU KAYNAKLARI VE EKONOMİK-SOSYAL ETKİLERİ', R['koyu']))

    # Sol panel: Türkiye'nin Denizleri, Akarsuları ve Gölleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. DENİZLER, AKARSULAR VE GÖLLERİMİZ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Dört Denizimiz ve Tuzluluk Oranı Sıralaması', 'Akdeniz (%3.8) > Ege > Marmara > Karadeniz (%1.8). Boğazlarda alt ve üst akıntılar.'),
        (150, 'Türkiye Akarsularının Genel Özellikleri', 'Yatak eğimleri ve hidroelektrik potansiyelleri yüksek; rejimleri düzensiz, ulaşıma elverişsiz.'),
        (200, 'Açık ve Kapalı Havzalarımız', 'Fırat-Dicle (Basra), Kızılırmak-Yeşilırmak (Karadeniz); Aras-Kura ve Van/Tuz Gölü kapalı havzası.'),
        (250, 'Doğal Göller: Tektonik, Karstik, Set Gölleri', 'Tektonik: Tuz, Beyşehir, İznik. Karstik: Salda. Volkanik Set: Van Gölü. Alüvyal: Eymir/Mogan.'),
        (300, 'Jeotermal ve Karstik Yer Altı Suları', 'Fay kaynakları (Ege/Güney Marmara kaplıca-jeotermal) ve voklüz kaynakları (Akdeniz).'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Su Kaynaklarının Ekonomik-Sosyal Etkileri ve Sürdürülebilirlik
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SU KAYNAKLARININ TÜRKİYE’YE ETKİLERİ', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Sektörel Su Kullanımı Dağılımı', 'Türkiye’de tatlı suyun ~%74-77’si TARIMDA (sulama), kalanı içme-kullanma ve sanayide tüketilir.'),
        (150, 'Tarımsal Kalkınma: GAP ve KOP Projeleri', 'Atatürk, Keban, Karakaya, Ilısu barajları ve Mavi Tünel ile sulamalı tarım ve ürün çeşitliliği.'),
        (200, 'Enerji Üretimi: HES ve Jeotermal Santraller', 'Doğu Anadolu ve Karadeniz’de HES; Büyük Menderes grabeninde (Aydın-Denizli) jeotermal enerji.'),
        (250, 'Deniz Ticareti, Balıkçılık ve Turizm', 'İstanbul/Çanakkale Boğazları, limanlar, Karadeniz balıkçılığı ve termal/kıyı turizmi.'),
        (300, 'Su Stresi (Kişi Başı ~1313 m³) ve Koruma', 'Türkiye “su zengini” değil “su stresi” çeken ülkedir; damla sulama ve havza yönetimi şarttır!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ÖNEMLİ AYIRIM: Sınırlarımız içindeki en uzun akarsu KIZILIRMAK (1355 km); Türkiye’den doğup dışarı dökülen en uzun akarsu FIRAT’tır!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Gideğeni (dışa akışı) olan göllerin suları TATLI (Beyşehir, Eğirdir); gideğeni olmayan kapalı havza göllerinin suları TUZLU/SODALIDIR (Tuz, Van)!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-cografya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
