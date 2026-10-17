from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'ALLAH’IN GÜZEL İSİMLERİ: EL-HÂDÎ, ES-SELÂM, EL-VEKÎL (6. SINIF)', R['koyu']))

    # Sol panel: Esmâ-i Hüsnâ ve Kur'an'daki Delilleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. EL-HÂDÎ, ES-SELÂM VE EL-VEKÎL İSİMLERİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'El-Hâdî (الْهَادِي — Hidayet ve Rehberlik Veren)', 'Akıl, peygamber ve vahiy ile insanı hakikate ulaştıran.'),
        (150, 'Es-Selâm (السَّلَامُ — Mutlak Esenlik Kaynağı)', 'Noksanlıklardan münezzeh; dünyaya ve cennete (Dâru’s-Selâm) huzur veren.'),
        (200, 'El-Vekîl (الْوَكِيلُ — Tevekkül Edilen Dost)', 'Tedbir alıp kendisine sığınanların işlerini en iyi şekilde gözeten.'),
        (250, 'Haşr Suresi 23. Ayette "Es-Selâm"', '"O, kendisinden başka ilah olmayan Allah’tır; Melik’tir, Kuddûs’tür, Selâm’dır..."'),
        (300, 'Furkân Suresi 31. Ayette "El-Hâdî"', '"Doğru yolu gösterici (Hâdî) ve yardımcı olarak Rabbin yeter!"'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: İman-Ahlak İlişkisi ve 1. Ünite Bütünlüğü
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. MÜMİN KİMLİĞİNE VE DAVRANIŞLARA ETKİSİ', '#92400e', 12.5, 'bold', 'middle'))

    sag = [
        (100, 'Hidayet Yolunda İstikamet (El-Hâdî)', 'Sırât-ı müstakîm (dosdoğru yol) üzerinde dürüst ve adil yaşamak.'),
        (150, 'Toplumsal Barış ve Güven (Es-Selâm)', '"Müslüman, elinden ve dilinden insanların güvende olduğu kişidir."'),
        (200, 'Çalışma, Tedbir ve Tevekkül (El-Vekîl)', 'Tembellikten kaçınıp gayret göstermek; zorlukta Allah’a sığınmak.'),
        (250, 'Dâru’s-Selâm (Esenlik Yurdu: Cennet)', 'Dünyada barış ve doğruluk üzere yaşayanların ahiretteki mükâfatı.'),
        (300, '1. Ünite (Dinimiz İslam) Sentezi', 'Kelime-i Tevhid, İman-İbadet-Ahlak bağı ve Esmâ-i Hüsnâ bilinci.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KUR’AN’DA TEVEKKÜL: "Kararını verdiğin zaman artık Allah’a dayanıp güven (tevekkül et)!" (Âl-i İmrân 3/159).', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'El-Hâdî -> Sırât-ı Müstakîm (Hidayet) | Es-Selâm -> Emniyet ve Barış | El-Vekîl -> Tedbir ve Tevekkül.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('6-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
