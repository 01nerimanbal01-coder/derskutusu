from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('turkce')
    ic = []
    ic.append(P.baslik(400, 32, 'CÜMLENİN ÖGELERİ: YARDIMCI ÖGELER (NESNE, TAMLAYICILAR) VE VURGU', R['koyu']))

    # Sol panel: Cümlenin Yardımcı Ögeleri (Nesne, Yer Tamlayıcısı, Zarf Tamlayıcısı)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. YARDIMCI ÖGELER VE SORULARI', R['koyu'], 12.5, 'bold', 'middle'))

    sol = [
        (100, '1. Belirtili Nesne (Yükleme: Neyi? / Kimi? / Nereyi?)', 'Belirtme hâl eki (-ı/-i/-u/-ü) alır: "Vatan-ı koruduk."'),
        (150, '2. Belirtisiz Nesne (Özneden Sonra: Ne?)', 'Ek almaz: "Atatürk cepheden mektup yazdı." (Ne yazdı? -> mektup).'),
        (200, '3. Yer Tamlayıcısı / Dolaylı Tümleç (-e / -de / -den)', 'Kime, kimde, kimden / Neye, nerede, nereden? (Mutlaka -e/-de/-den!).'),
        (250, '4. Zarf Tamlayıcısı (Zaman, Durum, Miktar, Yön)', 'Nasıl, ne zaman, ne kadar, niçin, neyle, kimle, nereye (eksiz)?'),
        (300, 'Öge Bulma Sırası (YÖN Kuralı!)', 'Önce 1) YÜKLEM -> 2) ÖZNE -> 3) NESNE -> 4) TAMLAYICILAR!'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Cümlede Vurgu, Ara Söz ve Kritik Tuzaklar
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. CÜMLEDE VURGU, ARA SÖZ VE LGS TUZAKLARI', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Yön-Yer Sözcükleri Tuzağı (içeri, dışarı, ileri, geri...)', 'Yalın hâldeyse ZARF ("içeri girdi"); -e/-de/-den alırsa YER TAMLAYICISI!'),
        (150, 'Fiil Cümlelerinde Vurgu Kuralı', 'Yüklemden HEMEN ÖNCEKİ öge vurgulanır! (Yüklem baştaysa yüklemde).'),
        (200, 'İsim Cümlelerinde Vurgu Kuralı', 'Yüklemi isim olan cümlelerde vurgu YÜKLEMİN KENDİSİNDEDİR!'),
        (250, '"mi" Soru Eki ve "de/da" Bağlacında Vurgu', '"mi" ve "de/da" kendisinden ÖNCEKİ ögeye vurgu kazandırır.'),
        (300, 'Ara Söz ve Cümle Dışı Unsur (CDU)', 'İki virgül/kısa çizgi arası açıklama = Ara söz; Bağlaç/Ünlem = CDU.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'ALTIN KURAL: Tamlamalar, deyimler, birleşik fiiller ve fiilimsi grupları ÖGELER BULUNURKEN ASLA BÖLÜNMEZ!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, '"İçeri girdi" -> Zarf Tamlayıcısı (Nereye? - eksiz) | "İçeriye girdi" -> Yer Tamlayıcısı (Nereye? - "-e" yönelme ekli)!', '#334155', 10.5, 'normal', 'middle'))

    kaydet('7-turkce-7.svg' if False else '8-turkce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
