from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'SURELERİ TANIYORUM: HUCURÂT SURESİ VE AHLAKİ MESAJLARI', R['koyu']))

    # Sol panel: Hucurât Suresi'nin Tanıtımı ve İlkeleri (1-10. Ayetler)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HUCURÂT SURESİ KÜNYESİ VE İLKELERİ', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, 'Hucurât Suresi Künyesi (Medine — 18 Ayet)', 'Adını Peygamberimizin odaları anlamındaki "el-Hucurât"tan alır.'),
        (150, '1-5. Ayetler: Allah ve Resûlüne Saygı Adabı', 'Peygamberimizin huzurunda sesi yükseltmeme ve nezaket.'),
        (200, '6. Ayet: Haber Doğrulama İlkesi (Tebeyyün)', 'Fâsık (güvenilmez) biri haber getirdiğinde doğruluğunu araştırın!'),
        (250, '9. Ayet: Müminler Arasında Sulh ve Adalet', 'İki grup çatışırsa aralarını adaletle düzeltin (ıslah edin).'),
        (300, '10. Ayet: İslam Kardeşliği İlkesi (Uhuvvet)', '"Müminler ancak kardeştirler; kardeşlerinizin arasını düzeltin!"'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Hucurât Suresi 11-13. Ayetlerdeki Ahlaki Yasaklar ve Takva Ölçüsü
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. KÖTÜ HUYLARDAN SAKINMA VE TAKVA (11-13)', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, '11. Ayet: Alay Etme ve Lakap Takma Yasağı', 'Bir topluluk diğeriyle alay etmesin, kötü lakaplar takmayın!'),
        (150, '12. Ayet (a): Kötü Zan (Sû-i Zan) Yasağı', 'Zannın çoğundan sakının; çünkü zannın bir kısmı günahtır!'),
        (200, '12. Ayet (b): Tecessüs (Kusur Araştırma) Yasağı', 'Birbirinizin gizli hâllerini ve ayıplarını araştırmayın (tecessüs)!'),
        (250, '12. Ayet (c): Gıybet (Dedikodu / Çekiştirme) Yasağı', 'Birbirinizin gıybetini yapmayın (Ölü kardeşinin etini yemek gibidir).'),
        (300, '13. Ayet: Üstünlük Ölçüsü Yalnızca TAKVA’dır!', 'İnsanlar tanışsın diye farklı yaratıldı; en üstün olan en takvalı olandır!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ANAHTAR KAVRAMLAR: Tebeyyün (Haberi araştırma) | Sû-i Zan (Kötü önyargı) | Tecessüs (Gizli kusur arama) | Gıybet (Arkadan konuşma)!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Hucurât 13: "Şüphesiz Allah katında en değerli olanınız, O’na karşı gelmekten en çok sakınanınızdır (en takvalı olanınızdır)."', '#334155', 10, 'normal', 'middle'))

    kaydet('8-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
