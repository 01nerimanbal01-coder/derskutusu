"""7. sınıf Fen Bilimleri 13. hafta (Kanın Yapısı, Kan Grupları ve Dolaşım Sistemi Sağlığı) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def santrifuj_tupu_modeli():
    ic = kutu(6, 6, 172, 103, TUR_A, TUR)
    ic += yazi(92, 24, '1. Üst Katman (%55)', TUR, kalin=True)
    ic += yazi(92, 52, 'Açık Sarı Sıvı Kısım', LAC, kalin=True)
    ic += yazi(92, 80, '%90 Su + %10 Besin, Hormon, Atık', LAC)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 24, '2. Alt Katman (%45)', KIR, kalin=True)
    ic += yazi(269, 52, 'Çöken Hücresel Kısım', LAC, kalin=True)
    ic += yazi(269, 80, 'Alyuvar + Akyuvar + Kan Pulcukları', KIR)
    return svg(ic, 'Santrifüj tüpünde %55 plazma ve %45 kan hücreleri ayrımı.')


def kan_grubu_kartlari():
    kartlar = [
        (6, 6, '1. A Rh(+) Grubu', 'Protein: A ve Rh(+)', KIR, KIR_A),
        (184, 6, '2. B Rh(-) Grubu', 'Protein: Yalnız B (Rh Yok)', MAVI, MAVI_A),
        (6, 60, '3. AB Rh(+) Grubu', 'Protein: A + B + Rh(+)', MOR, MOR_A),
        (184, 60, '4. 0 Rh(-) Grubu', 'Protein: A, B ve Rh Yok', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört kan grubunun alyuvar zarı protein özellikleri.')


def kan_hucreleri_mikroskop():
    kartlar = [
        (6, 'X Hücresi', 'Kırmızı · Disk Şekilli', 'O₂ ve CO₂ Taşır (En Çok)', KIR, KIR_A),
        (124, 'Y Hücresi', 'Beyaz · Çekirdekli', 'Mikroplarla Savaşır', MAVI, MAVI_A),
        (242, 'Z Parçacığı', 'Çok Küçük · Renksiz', 'Kanı Pıhtılaştırır', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, b3, r, z in kartlar:
        ic += kutu(x, 6, 112, 103, z, r)
        ic += yazi(x + 56, 26, b1, r, kalin=True)
        ic += yazi(x + 56, 56, b2, LAC, kalin=True)
        ic += yazi(x + 56, 84, b3, r)
    return svg(ic, 'X, Y ve Z kan hücrelerinin yapı ve görev kartları.')


def kan_bagisi_kriter_tablosu():
    kartlar = [
        (6, 6, '1. Efe (15 Yaş, 58 kg)', 'Yaş Sınırı: 18–65 Yaş!', KIR, KIR_A),
        (184, 6, '2. Zeynep (29 Yaş, 62 kg)', 'Sağlıklı · Tüm Şartlara Uygun', YES, YES_A),
        (6, 60, '3. Selin (24 Yaş, 44 kg)', 'Kilo Sınırı: En Az 50 kg!', TUR, TUR_A),
        (184, 60, '4. Ahmet (72 Yaş, 70 kg)', 'Yaş > 65 ve Bulaşıcı Hastalık', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Kan bağışı yaş, kilo ve sağlık kriterleri karşılaştırma kartları.')


def enfeksiyon_akyuvar_karti():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Sağlıklı Birey Kan Sayımı', YES, kalin=True)
    ic += yazi(92, 56, 'Akyuvar: 6.000 / mm³ (Normal)', LAC, kalin=True)
    ic += yazi(92, 84, 'Vücutta aktif enfeksiyon yok', LAC)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 26, 'Boğaz Enfeksiyonlu Hasta', KIR, kalin=True)
    ic += yazi(269, 56, 'Akyuvar: 15.500 / mm³ (Yüksek!)', KIR, kalin=True)
    ic += yazi(269, 84, 'Savunma sistemi aktifleşti!', LAC, kalin=True)
    return svg(ic, 'Sağlıklı birey ve enfeksiyonlu hastada akyuvar sayısı karşılaştırması.')


def pihtilasma_adimlari():
    adimlar = [
        (6, '1. Kesik', 'Damar Yaralanır', KIR, KIR_A),
        (94, '2. Göç', 'Pulcuklar Toplanır', TUR, TUR_A),
        (182, '3. Ağ', 'Lifli Pıhtı Oluşur', MOR, MOR_A),
        (270, '4. Onarım', 'Kanama Durur', YES, YES_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Kan pulcuklarının pıhtılaşma oluşturma aşamaları.')


def rakim_alyuvar_grafigi():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Yüksek Rakıma Çıkıldığında X Hücresi Sayısı', LAC, kalin=True)
    ic += f'<rect x="65" y="54" width="75" height="34" rx="4" fill="{MAVI}" />'
    ic += yazi(102, 103, '0 m (Deniz Seviyesi)', MAVI, kalin=True)
    ic += f'<rect x="215" y="30" width="75" height="58" rx="4" fill="{KIR}" />'
    ic += yazi(252, 103, '3000 m (Dağ Zirvesi — O₂ Az)', KIR, kalin=True)
    return svg(ic, 'Deniz seviyesinden 3000 metre yüksekliğe çıkıldığında alyuvar artışı.')


def kizilay_afis_karti():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 26, 'TÜRK KIZILAYI', KIR, kalin=True)
    ic += yazi(92, 56, '«1 Ünite Kan = 3 Can!»', LAC, kalin=True)
    ic += yazi(92, 84, 'Alyuvar + Plazma + Trombosit', KIR)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Kan Bağışının Etkisi', YES, kalin=True)
    ic += yazi(269, 56, 'Hayat Kurtarır & Dayanışma Sağlar', LAC, kalin=True)
    ic += yazi(269, 84, 'Kan Hücrelerini Yeniler', YES, kalin=True)
    return svg(ic, 'Türk Kızılayı kan bağışı ve toplumsal dayanışma kartı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = santrifuj_tupu_modeli()
    s[2]['gorsel'] = kan_grubu_kartlari()
    s[5]['gorsel'] = kan_hucreleri_mikroskop()
    s[6]['gorsel'] = kan_bagisi_kriter_tablosu()
    s[7]['gorsel'] = enfeksiyon_akyuvar_karti()
    s[8]['gorsel'] = pihtilasma_adimlari()
    s[9]['gorsel'] = rakim_alyuvar_grafigi()
    s[11]['gorsel'] = kizilay_afis_karti()
