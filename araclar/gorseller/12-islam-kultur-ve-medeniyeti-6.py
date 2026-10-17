from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('islam-kultur-ve-medeniyeti')
    ic = []
    ic.append(P.baslik(400, 32, 'İSLAM KÜLTÜR VE MEDENİYETİNİN ESASLARI: TEVHİD VE HÜRRİYET', R['koyu']))

    # Sol panel: 1. Esas - Tevhid (Birlik ve Bütünlük İlkesi)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. KURUCU ESAS: TEVHİD (BİRLİK İLKESİ)', R['koyu'], 13, 'bold', 'middle'))
    ic.append(P.metin(202, 100, '("Lâ ilâhe illallah" — Medeniyetin Ruh ve Özü)', '#334155', 10, 'bold', 'middle'))

    tevhid = [
        (114, 'İnançta Tevhid', 'Yalnızca Allah’a kulluk; her türlü şirk ve putperestliği red.'),
        (162, 'Kâinat ve Bilim Tasavvurunda Tevhid', 'Evrendeki kusursuz düzen (Sünnetullah) Tek Yaratıcı’nın eseridir.'),
        (210, 'Sanat ve Mimaride Tevhid', 'Merkezî kubbe, sonsuzluk hissi veren geometrik/hat kompozisyonu.'),
        (258, 'Toplumsal Hayatta Tevhid (Vahdet)', 'Irk ve sınıf ayrımını reddederek müminleri "kardeş" kılma.'),
        (306, 'Ahlak ve Gayede Tevhid', 'Dünya ve ahiret dengesi içinde yalnız Allah’ın rızasını gözetme.'),
    ]
    for y, b, a in tevhid:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: 2. Esas - Hürriyet (Gerçek Özgürlük İlkesi)
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. KURUCU ESAS: HÜRRİYET (ÖZGÜRLÜK)', '#1e40af', 13, 'bold', 'middle'))
    ic.append(P.metin(590, 100, '(Tevhid İnsanı Kula Kulluktan Kurtarıp Özgürleştirir!)', '#334155', 10, 'bold', 'middle'))

    hurriyet = [
        (114, 'Nefsin ve Arzuların Esaretinden Hürriyet', 'Kula kulluktan, dünyevi tutkulara köle olmaktan kurtuluş.'),
        (162, 'Din ve Vicdan Hürriyeti (Bakara 2/256)', '"Dinde zorlama yoktur." — Gayrimüslimlere (Zımmî) tam güvence.'),
        (210, 'Düşünce, İlim ve İfade Hürriyeti', 'Tefekkür, içtihat ve bilimsel araştırma özgürlüğü.'),
        (258, 'Köleliğin Tedricen Ortadan Kaldırılması', 'Köle azadının ibadet/kefaret sayılarak hürriyetin teşvik edilmesi.'),
        (306, 'Hürriyet ve Sorumluluk Dengesi', 'Başkasının hakkına ve ilahi sınırlara zarar vermeyen özgürlük.'),
    ]
    for y, b, a in hurriyet:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 15, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'TEVHİD VE HÜRRİYET İLİŞKİSİ: Yalnızca Allah’a kul olan insan, diğer bütün sahte otoritelerin köleliğinden kurtularak GERÇEK HÜRRİYETE kavuşur!', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hz. Ömer’in Tarihi Sözü: "Annelerinden hür doğan insanları siz ne zamandan beri köleleştirdiniz?"', '#334155', 11, 'normal', 'middle'))

    kaydet('12-islam-kultur-ve-medeniyeti-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
