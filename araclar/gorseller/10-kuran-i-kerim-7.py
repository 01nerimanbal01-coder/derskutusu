from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('kuran-i-kerim')
    ic = []
    ic.append(P.baslik(400, 32, 'TECVİT: MED (UZATMA) ÇEŞİTLERİ II — LÂZIM, ÂRIZ VE LÎN', R['koyu']))

    # Sol panel: Sükûn Sebebiyle Oluşan Medler: Medd-i Lâzım ve Medd-i Ârız
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SÜKÛN SEBEBİYLE MEDLER: LÂZIM VE ÂRIZ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Sebeb-i Med Olan Sükûn İkiye Ayrılır!', '1) Sükûn-u Lâzım (Aslî/Kalıcı)  |  2) Sükûn-u Ârız (Geçici/Durak sükûnu).'),
        (150, 'Medd-i Lâzım: Harf-i Med + Sükûn-u Lâzım', 'Durulsa da geçilse de değişmeyen cezim veya şedde! Örn: الضَّآلِّينَ ، الحَآقَّةُ ، الم.'),
        (200, 'Medd-i Lâzım Hükmü ve Miktarı', 'Hükmü VACİPTİR; bütün kıraat imamlarına göre 4 ELİF (asgari 3-4) uzatılır!'),
        (250, 'Medd-i Ârız: Harf-i Med + Sükûn-u Ârız (Durak)', 'Kelime sonunda durulduğunda (vakıf) ortaya çıkan geçici sükûn! Örn: العَالَمِينَ -> العَالَمِينْ.'),
        (300, 'Medd-i Ârız Hükmü ve Okunuş Vecihleri', 'Hükmü CAİZDİR; durak hızına göre 1, 2, 3 veya 4 elif (Tûl, Tevassut, Kasr) uzatılır.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Medd-i Lîn ve Tüm Med Çeşitlerinin Genel Karşılaştırması
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. MEDD-İ LÎN VE 6 MED TÜRÜNÜN ÖZET TABLOSU', '#92400e', 11.5, 'bold', 'middle'))

    sag = [
        (100, 'Harf-i Lîn (Yumuşak Harfler): Cezimli وْ ve يْ', 'Kendinden önceki harf ÜSTÜN harekeli olan cezimli Vav (ـَوْ) ve Yâ (ـَيْ)!'),
        (150, 'Medd-i Lîn Nasıl Oluşur? (Kureyş Suresi Örneği)', 'Harf-i Lîn’den sonra sükûn gelirse oluşur: قُرَيْشٍ (Kureyş), خَوْفٍ (Havf), الصَّيْفِ (Sayf).'),
        (200, 'Hemze Sebebiyle Oluşan Medler (Hatırlatma)', 'Aynı kelimede hemze -> Medd-i Muttasıl (Vacip) | Ayrı kelimede -> Medd-i Munfasıl (Caiz).'),
        (250, 'Sükûn Sebebiyle Oluşan Medler (Bu Hafta)', 'Kalıcı sükûn/şedde -> Medd-i Lâzım (Vacip) | Durak sükûnu -> Medd-i Ârız (Caiz).'),
        (300, 'Geçildiğinde Düşen Medler Hangileridir?', 'Medd-i Ârız ve (sükûn-u ârızlı) Medd-i Lîn durulmaz da GEÇİLİRSE uzatması düşer!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN AYRIM: Harf-i Med’den (ا، و، ي) sonra durulursa MEDD-İ ÂRIZ (العَالَمِينْ); Harf-i Lîn’den (ـَوْ / ـَيْ) sonra durulursa MEDD-İ LÎN (قُرَيْشْ)!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Fâtiha suresinin son kelimesi olan “الضَّآلِّينَ” kelimesinde eliften sonra şeddeli lâm geldiği için MEDD-İ LÂZIM vardır; durulurken نْ üzerinde MEDD-İ ÂRIZ oluşur.', '#334155', 9.5, 'normal', 'middle'))

    kaydet('10-kuran-i-kerim-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
