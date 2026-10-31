"""5. sınıf Fen Bilimleri 7. hafta (Kuvvet ve Kuvvetin Ölçülmesi: Kuvvetin Etkileri, Dinamometre ve Newton Birimi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.0, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def dinamometre_bolme_sema():
    ic = f'<rect x="8" y="6" width="280" height="92" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(148, 24, '1. Durum: K Cismi (10 Bölmeli Dinamometre)', 10.6, MAVI)
    for k in range(4):
        ic += f'<rect x="{24 + k * 26}" y="36" width="22" height="18" rx="3" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += yazi(140, 49, '→ 4 bölme = 24 N', 10.6, LAC, 'start')
    ic += yazi(148, 78, 'K Cismi = 24 N (1 bölme = 6 N)', 10.2, LAC, ince=True)

    ic += f'<rect x="312" y="6" width="280" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(452, 24, '2. Durum: L Cismi (Aynı Dinamometre)', 10.6, TUR)
    for k in range(7):
        ic += f'<rect x="{324 + k * 18}" y="36" width="15" height="18" rx="2.5" fill="#fff" stroke="{TUR}" stroke-width="1.2"/>'
    ic += yazi(458, 49, '→ 7 bölme = ?', 10.6, LAC, 'start')
    ic += yazi(452, 78, 'L Cismi = ? N  |  10 Bölme Kapasite = ? N', 10.2, LAC, ince=True)
    return svg(600, 104, ic, '10 eşit bölmeli dinamometrede K cismi (4 bölme, 24 N) ve L cismi (7 bölme) karşılaştırma şeması.', 22)


def esnek_berk_panosu():
    kartlar = [
        ('1. Kart · Bulaşık Süngeri', 'Sıkılınca şekli değişir, kuvvet', 'kalkınca eski hâline döner (Esnek).', YES, YES_A),
        ('2. Kart · Sarmal Yay', 'Esnek maddedir; dinamometrelerin', 'iç yapısında kullanılır.', MAVI, MAVI_A),
        ('3. Kart · Oyun Hamuru', 'Kuvvet kalktığında kendiliğinden', 'eski şekline geri döner (Hatalı).', KIR, '#fdeaea'),
        ('4. Kart · Paket Lastiği', 'Esnektir; ancak çok aşırı çekilirse', 'esneklik sınırı aşılır ve kopar.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 54
        ic += f'<rect x="{x}" y="{y}" width="286" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="7" height="46" rx="3.5" fill="{renk}"/>'
        ic += yazi(x + 16, y + 18, bas, 10.6, renk, 'start')
        ic += yazi(x + 16, y + 36, f'{s1} {s2}', 10.0, LAC, 'start', ince=True)
    return svg(600, 116, ic, 'Esnek ve esnek olmayan maddeler panosu: 1. Sünger, 2. Sarmal yay, 3. Oyun hamuru (hatalı), 4. Paket lastiği.', 22)


def kuvvet_etki_kartlari():
    kartlar = [
        ('1. Kart · Tenis Topu', 'Raketle gelen topa', 'vurularak karşılık verme', MAVI, MAVI_A),
        ('2. Kart · El Arabası', 'Duran el arabasını', 'ileri doğru itme', YES, YES_A),
        ('3. Kart · Futbol Topu', 'Kaleye gelen topu', 'eldivenle yakalama', TUR, TUR_A),
        ('4. Kart · Su Musluğu', 'Musluk başlığını', 'sağa-sola çevirme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="6" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 23, bas, 10.6, renk)
        ic += f'<line x1="{x + 12}" y1="31" x2="{x + 124}" y2="31" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 68, 70, s2, 10.0, LAC, ince=True)
    return svg(600, 98, ic, 'Kuvvetin etkileri dört olay kartı: tenis topu, el arabası, futbol topu, su musluğu.', 22)


def iki_dinamometre_kiyas():
    ic = f'<rect x="8" y="6" width="280" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(148, 24, 'K Dinamometresi (10 Bölmeli)', 10.8, MAVI)
    ic += yazi(148, 46, 'Özdeş P cismi asıldığında: 2 bölme uzar.', 10.1, LAC, ince=True)
    ic += yazi(148, 64, 'Yay daha kalın ve serttir.', 10.1, LAC, ince=True)
    ic += yazi(148, 80, 'Daha büyük kuvvetleri ölçebilir.', 10.2, MAVI)

    ic += f'<rect x="312" y="6" width="280" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(452, 24, 'L Dinamometresi (10 Bölmeli)', 10.8, YESIL_K)
    ic += yazi(452, 46, 'Özdeş P cismi asıldığında: 5 bölme uzar.', 10.1, LAC, ince=True)
    ic += yazi(452, 64, 'Yay daha ince ve yumuşaktır.', 10.1, LAC, ince=True)
    ic += yazi(452, 80, 'Küçük kuvvetleri daha hassas ölçer.', 10.2, YESIL_K)
    return svg(600, 100, ic, 'Özdeş P cismi asılan K (2 bölme) ve L (5 bölme) dinamometrelerinin karşılaştırma şeması.', 22)


def hassasiyet_kapasite_kartlari():
    kartlar = [
        ('I. Dinamometre', 'Kapasite: 10 N', '1 bölme = 1 N', YES, YES_A),
        ('II. Dinamometre', 'Kapasite: 20 N', '1 bölme = 2 N', MAVI, MAVI_A),
        ('III. Dinamometre', 'Kapasite: 50 N', '1 bölme = 5 N', TUR, TUR_A),
        ('IV. Dinamometre', 'Kapasite: 100 N', '1 bölme = 10 N', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="82" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 26, bas, 10.6, renk)
        ic += yazi(x + 68, 50, s1, 10.4, LAC)
        ic += yazi(x + 68, 70, s2, 10.0, LAC, ince=True)
    return svg(600, 98, ic, 'Kapasiteleri 10 N, 20 N, 50 N ve 100 N olan dört dinamometre kartı.', 22)


def uzama_kuvvet_grafigi():
    ic = f'<rect x="6" y="6" width="588" height="102" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 22, 'Esnek Yaya Uygulanan Kuvvet – Uzama Miktarı Grafiği', 11.0, LAC)
    ic += f'<line x1="56" y1="30" x2="56" y2="90" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="56" y1="90" x2="340" y2="90" stroke="{LAC}" stroke-width="1.6"/>'
    barlar = [('15 N', 3, 92, YES), ('X Kuvveti', 6, 180, MAVI), ('Y Kuvveti', 9, 268, TUR)]
    for ad, cm, bx, renk in barlar:
        bh = cm * 5.5
        by = 90 - bh
        ic += f'<rect x="{bx}" y="{by:.1f}" width="42" height="{bh:.1f}" rx="4" fill="{renk}"/>'
        ic += yazi(bx + 21, by - 4, f'{cm} cm', 10.2, LAC)
        ic += yazi(bx + 21, 102, ad, 10.2, LAC)
    ic += f'<rect x="358" y="32" width="222" height="64" rx="8" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.4"/>'
    ic += yazi(469, 48, 'Doğru Orantı Bağıntısı', 10.6, KAHVE)
    ic += yazi(469, 66, '15 N kuvvet → 3 cm uzama', 10.1, LAC, ince=True)
    ic += yazi(469, 82, 'Her 5 N kuvvet → 1 cm uzama', 10.2, KAHVE)
    return svg(600, 114, ic, '15 N (3 cm), X kuvveti (6 cm) ve Y kuvveti (9 cm) uzama miktarı sütun grafiği.', 22)


def yay_ozellik_tablosu():
    satirlar = [
        ('M Dinamometresi', 'Bakır (Yumuşak metal)', 'İnce tel', YES, YES_A),
        ('N Dinamometresi', 'Çelik (Sert metal)', 'İnce tel', MAVI, MAVI_A),
        ('R Dinamometresi', 'Çelik (Sert metal)', 'Kalın tel', TUR, TUR_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 22, 'M, N ve R Dinamometrelerindeki Yayların Özellikleri (Uzunluklar Eşit)', 10.8, LAC)
    for i, (ad, cins, kal, renk, arka) in enumerate(satirlar):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, ad, 10.6, renk)
        ic += yazi(x + 90, 65, f'Cinsi: {cins}', 10.0, LAC, ince=True)
        ic += yazi(x + 90, 80, f'Kalınlığı: {kal}', 10.0, LAC, ince=True)
    return svg(600, 108, ic, 'M (ince bakır), N (ince çelik) ve R (kalın çelik) dinamometre yaylarının özellik tablosu.', 22)


def kapasite_asim_deneyi():
    ic = f'<rect x="8" y="6" width="280" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(148, 24, '1. Adım: Kapasite Üstü Yükleme', 10.8, MAVI)
    ic += yazi(148, 46, 'Dinamometre kapasitesi: En fazla 30 N', 10.1, LAC, ince=True)
    ic += yazi(148, 64, 'Kancaya asılan demir blok: 55 N', 10.1, LAC, ince=True)
    ic += yazi(148, 80, 'Kapasite 25 N aşılmıştır!', 10.2, KIR)

    ic += f'<rect x="312" y="6" width="280" height="86" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(452, 24, '2. Adım: Yük Çıkarıldıktan Sonra', 10.8, KIR)
    ic += yazi(452, 46, 'Demir blok kancadan çıkarılıyor.', 10.1, LAC, ince=True)
    ic += yazi(452, 64, 'Sarmal yay eski boyuna dönemiyor;', 10.1, LAC, ince=True)
    ic += yazi(452, 80, 'esneklik sınırı aşıldığı için bozuluyor.', 10.2, KIR)
    return svg(600, 98, ic, '30 N kapasiteli dinamometreye 55 N yük asılması sonucu esneklik sınırının aşılması deneyi.', 22)


def uc_dinamometre_secim_karti():
    kutular = [
        ('X Dinamometresi', 'Maksimum: 20 N', 'En ince yay (En hassas)', YES, YES_A),
        ('Y Dinamometresi', 'Maksimum: 50 N', 'Orta kalınlıkta yay', MAVI, MAVI_A),
        ('Z Dinamometresi', 'Maksimum: 100 N', 'En kalın yay (Büyük yük)', TUR, TUR_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 22, 'Üç Farklı Dinamometrenin Maksimum Ölçüm Kapasiteleri', 10.8, LAC)
    for i, (ad, kap, oz, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, ad, 10.6, renk)
        ic += yazi(x + 90, 65, kap, 10.3, LAC)
        ic += yazi(x + 90, 80, oz, 10.0, LAC, ince=True)
    return svg(600, 108, ic, 'X (20 N), Y (50 N) ve Z (100 N) dinamometrelerinin kapasite ve yay kalınlığı kartları.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dinamometre_bolme_sema()
    s[4]['gorsel'] = esnek_berk_panosu()
    s[5]['gorsel'] = kuvvet_etki_kartlari()
    s[6]['gorsel'] = iki_dinamometre_kiyas()
    s[7]['gorsel'] = hassasiyet_kapasite_kartlari()
    s[8]['gorsel'] = uzama_kuvvet_grafigi()
    s[9]['gorsel'] = yay_ozellik_tablosu()
    s[10]['gorsel'] = kapasite_asim_deneyi()
    s[12]['gorsel'] = uc_dinamometre_secim_karti()
