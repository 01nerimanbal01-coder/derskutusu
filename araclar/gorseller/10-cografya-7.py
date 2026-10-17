from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('cografya')
    ic = []
    ic.append(P.baslik(400, 32, 'KAYAÇLAR VE İKLİM-KAYAÇ YAPISININ AŞINMA-ÇÖZÜNME SÜREÇLERİNE ETKİSİ', R['koyu']))

    # Sol panel: Kayaç Türleri (Magmatik, Tortul, Başkalaşım) ve Kayaç Döngüsü
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KAYAÇ TÜRLERİ VE KAYAÇ DÖNGÜSÜ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, '1. Püskürük (Magmatik) Kayaçlar', 'İç Püskürük (iri kristalli): Granit, Siyenit | Dış Püskürük: Bazalt, Andezit, Obsidyen, Tüf.'),
        (150, '2a. Fiziksel (Kırıntılı) ve Organik Tortul Kayaçlar', 'Fiziksel: Kil taşı, Kum taşı, Çakıl taşı (Konglomera) | Organik: Kömür, Mercan, Tebeşir.'),
        (200, '2b. Kimyasal Tortul Kayaçlar (Suda Kolay Çözünen!)', 'Kalker (Kireç taşı), Jips (Alçı taşı), Kaya tuzu, Traverten -> Karstik şekiller!'),
        (250, '3. Başkalaşım (Metamorfik) Kayaçlar (Yüksek T ve P)', 'Kalker -> Mermer | Granit -> Gnays | Kil taşı -> Şist | Kum taşı -> Kuvarsit.'),
        (300, 'Fosil ve Tabakalanma Özelliği Hangi Kayaçtadır?', 'Yalnızca TORTUL (Sedimanter) kayaçlar tabakalıdır ve içinde FOSİL barındırır!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: İklim ve Kayaç Yapısının Çözünme ve Yer Şekillerine Etkisi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. FİZİKSEL-KİMYASAL ÇÖZÜNME VE TOPOĞRAFYA', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Fiziksel (Mekanik) Çözünme (Sıcaklık Farkı)', 'Çöl, karasal ve tundra iklimlerinde kayaçların kimyası değişmeden ufalanması.'),
        (150, 'Kimyasal Çözünme (Sıcak ve Yağışlı / Nemli İklim)', 'Ekvatoral, Muson ve Karadeniz/Akdeniz kıyılarında suyla kimyasal ayrışma (hızlı toprak!).'),
        (200, 'Granit Kayacı -> Tor Topoğrafyası', 'İç püskürük granitin fiziksel/kimyasal ayrışmasıyla köşeleri yuvarlaklaşmış bloklar.'),
        (250, 'Tüf ve Bazalt -> Peribacaları (Nevşehir / Ürgüp)', 'Üstte dirençli bazalt/andezit şapka, altta yumuşak volkanik tüfün sel sularıyla aşınması.'),
        (300, 'Kalker ve Jips -> Karstik Topoğrafya (Akdeniz / Sivas)', 'Lapya, dolin, uvala, polye, mağara, obruk ve traverten (Pamukkale) oluşumu.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'TÜRKİYE’DE ÇÖZÜNME: İç ve Doğu Anadolu’da (karasal) FİZİKSEL; Karadeniz ve Akdeniz kıyılarında (nemli) KİMYASAL çözünme baskındır!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Toprak oluşumu kimyasal çözünmenin güçlü olduğu sıcak ve yağışlı bölgelerde ÇOK HIZLI, çöllerde ve kutuplarda ÇOK YAVAŞTIR.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-cografya-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
