from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'KUR’AN’DAN MESAJLAR: BAKARA SURESİ 286. AYET VE SORUMLULUK BİLİNCİ', R['koyu']))

    # Sol panel: Teklif-Güç Dengesi ve İrade-Sorumluluk İlkeleri
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. İLAHİ ADALET VE SORUMLULUK İLKELERİ', R['koyu'], 11.8, 'bold', 'middle'))

    sol = [
        (100, 'Âmene’r-Resûlü’nün Son Ayeti (Bakara, 286)', 'Bakara Suresi’nin son iki ayeti (285-286) yatsı namazlarından sonra okunan “Âmene’r-Resûlü”dür.'),
        (150, 'Güç Yetirebilme İlkesi (Teklîf-i mâ lâ yutâk)', '“Allah hiçbir kimseye gücünün yettiğinden (vüs’atinden) fazlasını yüklemez.”'),
        (200, 'Amellerin Bireysel Karşılığı (Kesb ve İktisâb)', '“Herkesin kazandığı iyilik kendi yararına (lehâ), işlediği kötülük de kendi zararınadır (aleyhâ).”'),
        (250, 'Kolaylaştırma ve Ruhsat İlkesi', 'İslam’da güçlük (harec) kaldırılmıştır; hastalık ve yolculukta kolaylık (ruhsat) tanınmıştır.'),
        (300, 'Cebriye ve Kaderiye Yanılgılarına Reddiye', 'İnsan ne robot gibi iradesizdir ne de sınırsız güce sahiptir; gücü nispetinde sorumludur.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Bakara 286'daki Üç Büyük Dua (Rabbenâ Duaları)
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. AYETTEKİ ÜÇ BÜYÜK YAKARIŞ (RABBENA)', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, '1. Dua: Unutma ve Yanılma İçin Bağışlanma', '“Rabbimiz! Unutursak veya hataya düşersek bizi sorumlu tutma (muâhaze etme)!”'),
        (150, '2. Dua: Ağır Yüklerden (Isr) Korunma', '“Rabbimiz! Bizden öncekilere yüklediğin gibi sırtımıza ağır bir yük yükleme!”'),
        (200, '3. Dua: Takatimiz Olmayan İmtihanlardan Sığınma', '“Rabbimiz! Güç yetiremeyeceğimiz (tâkatimizin olmadığı) şeyi bize taşıtma!”'),
        (250, 'Üç İlahi Lütfu İsteme: Afv, Mağfiret, Rahmet', '“Bizi affet (Va’fü annâ), bizi bağışla (Vağfir lenâ), bize merhamet et (Verhamnâ)!”'),
        (300, 'Tevhid ve Nusret (Yardım) İkrarı', '“Sen bizim Mevlâ’mızsın (dostumuz ve yardımcımızsın); inkârcı topluluğa karşı bize yardım et!”'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, '«لَا يُكَلِّفُ اللّٰهُ نَفْسًا إِلَّا وُسْعَهَا لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ» (Bakara, 286)', R['koyu'], 10.0, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Sahih-i Müslim’de geçen hadise göre müminler bu ayetteki her “Rabbimiz!” duasını okuduğunda Allah Teâlâ: “Kabul ettim (Peşinen verdim)!” buyurmuştur.', '#334155', 9.8, 'normal', 'middle'))

    kaydet('11-din-kulturu-ve-ahlak-bilgisi-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
