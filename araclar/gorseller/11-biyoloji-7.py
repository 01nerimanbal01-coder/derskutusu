from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('biyoloji')
    ic = []
    ic.append(P.baslik(400, 32, 'İNSANDA SİNİR SİSTEMİ: MERKEZÎ VE ÇEVRESEL SİNİR SİSTEMİ', R['koyu']))

    # Sol panel: Merkezî Sinir Sistemi (Beyin Bölümleri)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. MERKEZÎ SİNİR SİSTEMİ: BEYİN BÖLÜMLERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Zarlar (Meninges): Sert, Örümceksi, İnce Zar', 'BOS sıvısı örümceksi ile ince zar arasındadır; darbeyi emer ve iyon dengesini korur.'),
        (150, 'Uç Beyin (Beyin Kabuğu / Korteks)', 'İstemli hareket, 5 duyu algısı, zekâ, hafıza ve bilinç merkezidir (Dışta boz, içte ak madde).'),
        (200, 'Ara Beyin: Talamus, Hipotalamus, Epitalamus', 'Talamus: Koku hariç duyuların santrali. Hipotalamus: Homeostazi, vücut ısısı, hipofiz kontrolü.'),
        (250, 'Orta Beyin (Görme-İşitme Refleksi ve Kas Tonusu)', 'Göz bebeği refleksi, işitmede kulak dikme refleksi ve dinlenme hâlindeki kas tonusu.'),
        (300, 'Arka Beyin: Beyincik, Pons ve Omurilik Soğanı', 'Beyincik: Denge. Omurilik Soğanı (Hayat Düğümü): Solunum, dolaşım, yutma, hapşırma.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Omurilik, Refleks Yayı ve Çevresel Sinir Sistemi
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. OMURİLİK, REFLEKS YAYI VE ÇEVRESEL SİSTEM', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Omuriliğin Yapısı ve Görevleri', 'Dışta ak, içte boz madde! Refleks ve alışkanlık hareketlerini yönetir, uyarıları çapraz iletir.'),
        (150, 'Refleks Yayı Sıralaması (Dorsal -> Ventral)', 'Reseptör -> Duyu Nöronu (Arka/Dorsal kök) -> Ara Nöron -> Motor Nöron (Ön/Ventral kök) -> Efektör.'),
        (200, 'Çevresel Sinir Sistemi: 12 + 31 Çift Sinir', 'Beyinden 12 çift kafa siniri (10.’su Vagus), omurilikten 31 çift omurilik siniri çıkar.'),
        (250, 'Somatik Sinir Sistemi (İstemli)', 'Miyelinli motor nöronlarla iskelet kaslarını yönetir (yazı yazma, koşma, konuşma).'),
        (300, 'Otonom Sinir Sistemi (İstemsiz): Sempatik / Parasempatik', 'İç organları yönetir. Sempatik hızlandırır (sindirim hariç); Parasempatik yavaşlatır (sindirim hariç).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'DİKKAT: Uç beyin ve beyincikte DIŞTA BOZ, İÇTE AK madde; Omurilik ve omurilik soğanında ise DIŞTA AK, İÇTE BOZ madde bulunur!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Diz kapağı refleksi yalnızca 2 nöronlu (duyu + motor, ara nöron YOK) monosinaptik bir reflekstir!', '#334155', 10, 'normal', 'middle'))

    kaydet('11-biyoloji-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
