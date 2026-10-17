from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('din')
    ic = []
    ic.append(P.baslik(400, 32, 'AKAİD: ALLAH’IN (C.C.) VARLIĞI VE BİRLİĞİ (İSPAT-I VÂCİB DELİLLERİ)', R['koyu']))

    # Sol panel: Allah'ın Varlığının Delilleri (İspat-ı Vâcib)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. ALLAH’IN VARLIĞININ DELİLLERİ (İSPAT-I VÂCİB)', R['koyu'], 11.2, 'bold', 'middle'))

    sol = [
        (100, 'Hudûs Delili (Sonradan Yaratılmışlık)', 'Âlem hâdistir (sonradan var olmuştur); her hâdisin bir muhdisi (ezelî yaratıcısı) vardır.'),
        (150, 'İmkân Delili (Vâcibü’l-Vücûd - Mümkünü’l-Vücûd)', 'Varlığı ile yokluğu eşit olan mümkün varlıkları tercih edip var eden Zorunlu Varlık (Allah) şarttır.'),
        (200, 'Gâye ve Nizam Delili (İnâyet ve İhtirâ)', 'Evrendeki hassas ölçü, düzen ve amaçlılık üstün ilim ve kudret sahibi Yaratıcıyı gösterir.'),
        (250, 'Fıtrat, Vicdan ve Kabul-i Âmm (Genel Kabul)', 'İnsanın doğuştan inanma eğilimi (fıtrat) ve tarih boyu tüm toplumların Yaratıcı inancı.'),
        (300, 'Teselsül ve Devrin İmkânsızlığı (İptal)', 'Yaratıcılar zincirinin sonsuza dek geriye gitmesi (teselsül) ve kısır döngü (devir) imkânsızdır.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.0, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Allah'ın Birliği (Tevhid) ve Burhân-ı Temânu'
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. ALLAH’IN BİRLİĞİ (TEVHİD VE TEMÂNU’ DELİLİ)', '#92400e', 11.2, 'bold', 'middle'))

    sag = [
        (100, 'Tevhid ve Vahdâniyyet İlkesi', 'Allah’ın zatında, sıfatlarında ve fiillerinde bir ve tek olması; eşi ve ortağı bulunmaması.'),
        (150, 'Temânu’ Delili (Enbiyâ Suresi 22. Ayet)', '“Eğer yerde ve gökte Allah’tan başka ilahlar olsaydı ikisinin de düzeni kesinlikle bozulurdu!”'),
        (200, 'Temânu’ Delilinin Aklî Açıklaması', 'İki ilahın iradesi çatışırsa biri aciz kalır (aciz olan ilah olamaz); evrendeki tek düzen tek İlahı kanıtlar.'),
        (250, 'İhlâs Suresi: Tevhidin Özeti', 'Ehad (Tek), Samed (Hiçbir şeye muhtaç olmayan), doğmamış, doğurmamış ve dengi olmayan.'),
        (300, 'Tevhidin Zıddı: Şirk (En Büyük Zulüm)', 'Allah’a zatında, sıfatlarında veya ibadette ortak koşmak; affedilmeyen tek günah (Nisâ, 48).'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.0, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, '«لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللّٰهُ لَفَسَدَتَا» (Enbiyâ, 22) — Kelam ilminde Allah’ın birliğini kanıtlayan bu delile “Burhân-ı Temânu’” denir!', R['koyu'], 9.8, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Kelamcıların çoğunluğu Hudûs delilini, İslam filozofları (Fârâbî, İbn Sînâ) ise İmkân delilini merkeze almışlardır.', '#334155', 10, 'normal', 'middle'))

    kaydet('11-akaid-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic