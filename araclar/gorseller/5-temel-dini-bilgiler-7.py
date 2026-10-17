from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'ALLAH’IN GÜZEL İSİMLERİ: EL-HÂDÎ, ES-SELÂM, EL-VEKÎL', R['koyu']))

    # Sol panel: El-Hâdî, Es-Selâm, El-Vekîl Anlamları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ÜÇ GÜZEL İSMİN (ESMÂ-İ HÜSNÂ) ANLAMI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Esmâ-i Hüsnâ Kavramı', 'Yüce Allah’ın Kur’an ve hadislerde geçen en güzel isimleri.'),
        (150, '1. El-Hâdî (الْهَادِي — Doğru Yola İleten)', 'Kullarına iyilik ve hidayet yolunu gösteren, rehberlik eden.'),
        (200, '2. Es-Selâm (السَّلَامُ — Esenlik ve Barış Kaynağı)', 'Her türlü kusurdan uzak olan; kullarına güven ve huzur veren.'),
        (250, '3. El-Vekîl (الْوَكِيلُ — Güvenilen, İşleri Yöneten)', 'Üzerine düşeni yapıp kendisine tevekkül edenlerin işini en iyi çözen.'),
        (300, 'Fatiha Suresi’nde Hidayet Duası', '"İhdine’s-sırâta’l-müstakîm" -> Bizi dosdoğru yola ilet (El-Hâdî)!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Günlük Hayata Yansımaları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. GÜNLÜK HAYATIMIZA VE AHLAKIMIZA ETKİSİ', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'El-Hâdî İsminin Hayatımıza Yansıması', 'Kur’an ve sünnet rehberliğinde doğruluktan ayrılmamak.'),
        (150, 'Es-Selâm İsminin Hayatımıza Yansıması', '"Es-selâmü aleyküm" diyerek çevremize barış ve güven yaymak.'),
        (200, 'El-Vekîl İsminin Hayatımıza Yansıması', 'Önce çalışıp tedbir almak, sonra sonucu Allah’a bırakmak (Tevekkül).'),
        (250, 'Namaz Sonrası Tesbihatta Es-Selâm', '"Allâhümme ente’s-selâmü ve minke’s-selâm..." duası.'),
        (300, '1. Ünite (Dinimiz İslam) Özeti', 'İman, İslam, İhsan, Mümin Kimliği ve Esmâ-i Hüsnâ bütünlüğü.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ANAHTAR EŞLEŞTİRME: Hidayet / Doğru Yol = EL-HÂDÎ | Barış / Esenlik / Selam = ES-SELÂM | Tevekkül / Güven = EL-VEKÎL!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hasbünallâhü ve ni’me’l-vekîl: "Allah bize yeter, O ne güzel vekildir!" (Âl-i İmrân 3/173).', '#334155', 10.5, 'normal', 'middle'))

    kaydet('5-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
