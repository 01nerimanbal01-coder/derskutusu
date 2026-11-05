"""7. sınıf Fen Bilimleri 12. hafta (Dolaşım Sistemi: Kalp, Kan Damarları ve Büyük/Küçük Kan Dolaşımı) görselleri.
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


def kalp_odacik_modeli():
    ic = kutu(6, 6, 172, 48, MAVI_A, MAVI)
    ic += yazi(92, 24, '1. Sağ Kulakçık', MAVI, kalin=True)
    ic += yazi(92, 43, 'Kirli Kan (CO₂ zengin)', LAC)
    ic += kutu(184, 6, 170, 48, KIR_A, KIR)
    ic += yazi(269, 24, '2. Sol Kulakçık', KIR, kalin=True)
    ic += yazi(269, 43, 'Temiz Kan (O₂ zengin)', LAC)
    ic += kutu(6, 60, 172, 49, MAVI_A, MAVI)
    ic += yazi(92, 79, '3. Sağ Karıncık', MAVI, kalin=True)
    ic += yazi(92, 98, 'Akciğere kirli kan pompalar', LAC)
    ic += kutu(184, 60, 170, 49, KIR_A, KIR)
    ic += yazi(269, 79, '4. Sol Karıncık', KIR, kalin=True)
    ic += yazi(269, 98, 'Aortla vücuda temiz kan pompalar', LAC)
    return svg(ic, 'Kalbin dört odacığı ve taşıdıkları temiz-kirli kan durumu.')


def damar_tablo_kartlari():
    kartlar = [
        (6, 6, '1. Atardamar', 'Kalpten → Organlara', KIR, KIR_A),
        (184, 6, '2. Toplardamar', 'Organlardan → Kalbe', MAVI, MAVI_A),
        (6, 60, '3. Kılcal Damar', 'Madde Alışverişi Ağı', MOR, MOR_A),
        (184, 60, '4. Aort Atardamarı', 'En Büyük Temiz Kan Damarı', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Atardamar, toplardamar, kılcal damar ve aort bilgi kartları.')


def kucuk_dolasim_semasi():
    ic = kutu(6, 6, 108, 103, MAVI_A, MAVI)
    ic += yazi(60, 32, 'Sağ Karıncık', MAVI, kalin=True)
    ic += yazi(60, 58, 'K Damarı ile', LAC, kalin=True)
    ic += yazi(60, 82, 'Kirli Kan Çıkar', MAVI)
    ic += kutu(122, 6, 116, 103, CAM_A, CAM)
    ic += yazi(180, 32, 'AKCİĞERLER', CAM, kalin=True)
    ic += yazi(180, 58, 'CO₂ verilir,', LAC)
    ic += yazi(180, 82, 'O₂ alınır (Temizlenir)', YES, kalin=True)
    ic += kutu(246, 6, 108, 103, KIR_A, KIR)
    ic += yazi(300, 32, 'Sol Kulakçık', KIR, kalin=True)
    ic += yazi(300, 58, 'L Damarı ile', LAC, kalin=True)
    ic += yazi(300, 82, 'Temiz Kan Gelir', KIR)
    return svg(ic, 'Küçük kan dolaşımında K ve L damarlarıyla kanın temizlenmesi şeması.')


def kilcal_madde_alisverisi():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 26, '1 Yönü (Kandan Dokuya)', KIR, kalin=True)
    ic += yazi(92, 54, 'Kılcal Damar → Doku Hücresi', LAC)
    ic += yazi(92, 82, 'Oksijen (O₂) + Besin Geçer', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, '2 Yönü (Dokudan Kana)', MAVI, kalin=True)
    ic += yazi(269, 54, 'Doku Hücresi → Kılcal Damar', LAC)
    ic += yazi(269, 82, 'Karbondioksit (CO₂) + Atık', MAVI, kalin=True)
    return svg(ic, 'Kılcal damar ile doku hücreleri arasındaki madde alışverişi yönleri.')


def karincik_duvar_kalinligi():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'Sağ Karıncık Duvarı', MAVI, kalin=True)
    ic += yazi(92, 54, 'Orta Kalınlıkta Kas Tabakası', LAC)
    ic += yazi(92, 82, 'Hedef: Yalnızca Akciğerler', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 26, 'Sol Karıncık Duvarı', KIR, kalin=True)
    ic += yazi(269, 54, 'Çok Kalın ve Güçlü Kas!', LAC, kalin=True)
    ic += yazi(269, 82, 'Hedef: Aort ile Tüm Vücut', KIR, kalin=True)
    return svg(ic, 'Sağ ve sol karıncık kas duvarı kalınlıklarının karşılaştırılması.')


def buyuk_dolasim_sirasi():
    adimlar = [
        (6, '1. Başlangıç', 'Sol Karıncık', KIR, KIR_A),
        (94, '2. Dağıtım', 'Aort Atardamarı', TUR, TUR_A),
        (182, '3. Dokular', 'Organ Kılcalları', MOR, MOR_A),
        (270, '4. Bitiş', 'Sağ Kulakçık', MAVI, MAVI_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Büyük kan dolaşımının başlangıçtan bitişe dört adımı.')


def kan_basinci_grafigi():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Damarlardaki Kan Basıncı Karşılaştırması', LAC, kalin=True)
    ic += f'<rect x="52" y="34" width="56" height="54" rx="4" fill="{KIR}" />'
    ic += yazi(80, 102, 'K (En Yüksek)', KIR, kalin=True)
    ic += f'<rect x="152" y="54" width="56" height="34" rx="4" fill="{MOR}" />'
    ic += yazi(180, 102, 'L (Orta)', MOR, kalin=True)
    ic += f'<rect x="252" y="70" width="56" height="18" rx="4" fill="{MAVI}" />'
    ic += yazi(280, 102, 'M (En Düşük)', MAVI, kalin=True)
    return svg(ic, 'K, L ve M damarlarındaki kan basıncı sütun grafiği.')


def egzersiz_nabiz_karti():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Dinlenme Hâli', YES, kalin=True)
    ic += yazi(92, 56, 'Nabız: ~75 atım / dk', LAC, kalin=True)
    ic += yazi(92, 84, 'Normal O₂ ve enerji ihtiyacı', LAC)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 26, 'Koşu ve Egzersiz Hâli', KIR, kalin=True)
    ic += yazi(269, 56, 'Nabız: ~140 atım / dk', KIR, kalin=True)
    ic += yazi(269, 84, 'Kasların O₂ ihtiyacı artar!', LAC, kalin=True)
    return svg(ic, 'Dinlenme ve egzersiz sırasında nabız hızı karşılaştırması.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kalp_odacik_modeli()
    s[2]['gorsel'] = damar_tablo_kartlari()
    s[5]['gorsel'] = kucuk_dolasim_semasi()
    s[6]['gorsel'] = kilcal_madde_alisverisi()
    s[7]['gorsel'] = karincik_duvar_kalinligi()
    s[8]['gorsel'] = buyuk_dolasim_sirasi()
    s[9]['gorsel'] = kan_basinci_grafigi()
    s[11]['gorsel'] = egzersiz_nabiz_karti()
