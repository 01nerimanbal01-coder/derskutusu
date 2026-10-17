from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din-kulturu-ve-ahlak-bilgisi')
    ic = []
    ic.append(P.baslik(400, 32, 'BİR AYET TANIYORUM: AYETEL KÜRSİ (BAKARA 255) VE ANLAMI', R['koyu']))

    # Sol panel: Ayetel Kürsi'nin Tanıtımı ve Okunuşu
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. AYETEL KÜRSİ’NİN KÜNYESİ VE OKUNUŞU', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Bulunduğu Sure ve Ayet Numarası', 'Bakara Suresi’nin 255. ayetidir (Sure değil, tek bir ayettir!).'),
        (150, 'Adının Kaynağı: "Kürsî" (İlahi Hükümranlık)', 'İçinde geçen "vesia kürsiyyühü’s-semâvâti ve’l-ard" ifadesi.'),
        (200, '1. Bölüm: Allâhü lâ ilâhe illâ hüve’l-hayyü’l-kayyûm...', 'Lâ te’huzühû sinetün ve lâ nevm. Lehû mâ fi’s-semâvâti ve mâ fi’l-ard.'),
        (250, '2. Bölüm: Men ze’llezî yeşfeu indehû illâ bi-iznih...', 'Ya’lemü mâ beyne eydîhim ve mâ halfehüm ve lâ yühîtûne...'),
        (300, '3. Bölüm: Vesia kürsiyyühü’s-semâvâti ve’l-ard...', 'Ve lâ yeûdühû hıfzuhümâ ve hüve’l-aliyyü’l-azîm.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Ayetel Kürsi'de Geçen Esmâ-i Hüsnâ ve Tevhid İlkeleri
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ESMÂ-İ HÜSNÂ VE TEMEL İLKELER (LGS)', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, '1. Tevhid İlkesi ("Lâ ilâhe illâ Hû")', 'Allah’tan başka hiçbir ilah yoktur (Mutlak tevhid inancı).'),
        (150, '2. El-Hayy ve El-Kayyûm İsimleri', 'El-Hayy: Daima diri olan | El-Kayyûm: Her şeyi ayakta tutan/yöneten.'),
        (200, '3. Uyuklama ve Uykudan Münezzeh Olma', '"O’nu ne bir uyuklama (sinetün) tutar ne de bir uyku (nevm)!"'),
        (250, '4. Şefaat İzninin ve Mutlak İlmin Sahibi', 'İzni olmadan kimse şefaat edemez; O geçmişi ve geleceği bilir.'),
        (300, '5. El-Aliyy ve El-Azîm (Kürsî ve Koruma)', 'Gökleri ve yeri korumak O’na ağır gelmez; O çok yüce ve büyüktür!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'LGS KAVRAM ANAHTARI: El-Hayy (Diri) | El-Kayyûm (Evreni ayakta tutan) | El-Aliyy (Çok yüce) | El-Azîm (Çok büyük)!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kürsî: Yüce Allah’ın sınırsız hükümranlığı, saltanatı, ilmi ve kudreti demektir (Bakara Suresi 255. Ayet).', '#334155', 10.5, 'normal', 'middle'))

    kaydet('8-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
