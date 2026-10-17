from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('temel-dini-bilgiler')
    ic = []
    ic.append(P.baslik(400, 32, 'İMANIN GEÇERLİ (SAHİH) OLMASININ ŞARTLARI', R['koyu']))

    # Sol panel: İmanın Geçerlilik (Sıhhat) Şartları - İlk 3 Şart
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İMANIN GEÇERLİLİK ŞARTLARI (I)', R['koyu'], 13, 'bold', 'middle'))

    sol_sartlar = [
        (102, '1. Yeis (Ümitsizlik) Hâlinde Olmamak',
         'Son nefeste azabı görünce yapılan iman',
         '(İman-ı Ye’s / Firavun’un imanı) GEÇERSİZDİR!'),
        (182, '2. İman Esaslarını Bütünüyle Kabul Etmek',
         'İnanç esasları bir bütündür (Tecezzî kabul etmez);',
         'birini bile inkâr etmek tamamını inkâr sayılır.'),
        (262, '3. Dinin Kesin Hükümlerini Küçümsememek',
         'Zarûrât-ı Dîniyye’den bir hükmü alaya almak,',
         'beğenmemek veya helali haram saymak imana aykırıdır.'),
    ]
    for y, b, s1, s2 in sol_sartlar:
        ic.append(P.kutu(35, y, 335, 68, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 18, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 38, s1, '#334155', 10, 'normal', 'middle'))
        ic.append(P.metin(202, y + 54, s2, '#b91c1c', 10, 'bold', 'middle'))

    # Sağ panel: İmanın Geçerlilik Şartları - Son 3 Şart
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. İMANIN GEÇERLİLİK ŞARTLARI (II)', '#92400e', 13, 'bold', 'middle'))

    sag_sartlar = [
        (102, '4. Şüphe ve Tereddüt Taşımamak (Kesinlik)',
         'İman; "inşallah müminim, galiba ahiret var" gibi',
         'şüphe (şek) kabul etmez, tam ve kesin tasdik gerekir.'),
        (182, '5. Korku (Havf) ve Ümit (Recâ) Arasında Olmak',
         'Ne Allah’ın rahmetinden ümit kesmek (Ye’s),',
         'ne de azabından tamamen emin olmak (Emn): BEYNE’L-HAVF VE’R-RECÂ.'),
        (262, '6. Hür İrade ve İhtiyar (Baskı Olmadan İnanmak)',
         'İman kalbin özgür seçimiyle gerçekleşir; ölüm tehdidi',
         'altında (İkrah) kalbi imanla dolu iken dilin inkârı affedilir.'),
    ]
    for y, b, s1, s2 in sag_sartlar:
        ic.append(P.kutu(415, y, 350, 68, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 18, b, '#92400e', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 38, s1, '#334155', 10, 'normal', 'middle'))
        ic.append(P.metin(590, y + 54, s2, '#1e40af', 10, 'bold', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: İman "Kalp ile tasdik, dil ile ikrar"dır; geçerli olması için gayb perdesi kalkmadan hür iradeyle yapılmalıdır.', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Nisâ 4/150-151: "Allah ile peygamberlerinin arasını ayırmak isteyenler ve ‘Bir kısmına inanır, bir kısmını inkâr ederiz’ diyenler..."', '#334155', 10, 'normal', 'middle'))

    kaydet('12-temel-dini-bilgiler-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
