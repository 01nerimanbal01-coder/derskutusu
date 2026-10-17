from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'ALLAH’IN GÜZEL İSİMLERİ: EL-HÂDÎ, ES-SELÂM, EL-VEKÎL (7. SINIF)', R['koyu']))

    # Sol panel: El-Hâdî, Es-Selâm ve El-Vekîl İsimlerinin Derin Anlamları
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ESMÂ-İ HÜSNÂ VE KUR’ANİ DELİLLERİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'El-Hâdî (الْهَادِي — Hidayet ve İstikamet Rehberi)', 'Fıtrat, akıl, peygamber ve Kur’an ile hak yolu gösteren (Kasas 56).'),
        (150, 'Es-Selâm (السَّلَامُ — Mutlak Güven ve Barış Kaynağı)', 'Kusurlardan münezzeh; kullarını selamete çıkaran (Haşr 23).'),
        (200, 'El-Vekîl (الْوَكِيلُ — İşleri En Güzel Şekilde Yöneten)', 'Tedbir alıp tevekkül edenlerin en güvenilir dostu (Zümer 62).'),
        (250, 'Kasas Suresi 56. Ayet (Hidayet Yalnız Allah’tandır)', '"Sen sevdiğini hidayete erdiremezsin; Allah dilediğine hidayet verir."'),
        (300, 'Tevekkülün Şartı: Fiilî Dua + Kavli (Sözlü) Dua', 'Önce gayret ve çalışma (fiilî dua), sonra El-Vekîl’e sığınma!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Mümin Kimliğine ve Toplumsal Hayata Yansımaları
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. MÜMİN KİMLİĞİNDE TECELLİLERİ VE 1. ÜNİTE ÖZETİ', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'El-Hâdî -> Hayırda Rehber ve Örnek Olmak', 'İyiliği emredip kötülükten sakındırmak, doğruya kılavuzluk etmek.'),
        (150, 'Es-Selâm -> Emanet ve Güven İnsanı Olmak', 'Can, mal ve onur emniyetini korumak; selamı aramızda yaymak.'),
        (200, 'El-Vekîl -> Sorumluluk, Güvenilirlik ve Azim', 'Aldığı vekâlet ve emaneti koruyup işini sağlam yapmak.'),
        (250, '1. Ünite Bütünlüğü: İman - İbadet - Ahlak', 'İman kalpte kök, ibadet gövde, güzel ahlak ise meyvedir!'),
        (300, 'İhsan Bilinci (Cibrîl Hadisi)', 'Allah’ı görüyormuş gibi yaşamak ve Esmâ-i Hüsnâ ile ahlaklanmak.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ZÜMER SURESİ 62. AYET: "Allah her şeyin yaratıcısıdır ve O, her şey üzerinde Vekîl’dir (yöneten ve gözetendir)!"', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'El-Hâdî: Hidayet ve İstikamet | Es-Selâm: Barış ve Emniyet | El-Vekîl: Tedbir, Emanet ve Tevekkül.', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-temel-dini-bilgiler-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
