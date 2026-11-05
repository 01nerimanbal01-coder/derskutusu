"""7. sınıf Din Kültürü ve Ahlak Bilgisi 13. hafta (Kâfirûn Suresi ve 2. Ünite Değerlendirmesi) görselleri.
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


def kafirun_kimlik_karti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, 'Kâfirûn Suresi Kimliği', MAVI, kalin=True)
    ic += yazi(92, 52, 'Mushaf Sırası: 109. Sure', LAC, kalin=True)
    ic += yazi(92, 78, 'Ayet Sayısı: 6 · Dönem: Mekke', MAVI)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 24, 'Diğer İsimleri ve Konusu', YES, kalin=True)
    ic += yazi(269, 52, 'İhlas / Mukâşkışe (Şirkten Arındıran)', LAC)
    ic += yazi(269, 78, 'Tevhit İnancı ve İnanç Özgürlüğü', YES, kalin=True)
    return svg(ic, 'Kâfirûn suresinin mushaf sırası, ayet sayısı ve konusu.')


def unite_ibadet_kartlari():
    kartlar = [
        (6, 6, '1. Hac İbadeti', 'Farz · Zilhicce Ayı', MAVI, MAVI_A),
        (184, 6, '2. Umre İbadeti', 'Sünnet · Yıl Boyu Yapılır', YES, YES_A),
        (6, 60, '3. Udhiyye Kurbanı', 'Vacip · Kurban Bayramı', TUR, TUR_A),
        (184, 60, '4. Adak Kurbanı', 'Vacip · Sahibi Etinden Yiyemez', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Hac, umre, udhiyye ve adak kurbanı özet kartları.')


def nuzul_sebebi_karti():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 24, 'Müşriklerin Uzlaşma Teklifi', KIR, kalin=True)
    ic += yazi(92, 52, '«Bir yıl sen bizim putlarımıza tap,', LAC)
    ic += yazi(92, 76, 'bir yıl biz senin İlahına tapalım!»', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 24, 'İlahi Cevap (Kâfirûn Suresi)', YES, kalin=True)
    ic += yazi(269, 52, '«Lâ a’büdü mâ ta’büdûn!»', YES, kalin=True)
    ic += yazi(269, 78, 'Tevhitte şirkle ortaklık olmaz!', LAC, kalin=True)
    return svg(ic, 'Kâfirûn suresinin indiriliş sebebi ve tevhit vurgusu.')


def hac_farzlari_semasi():
    kartlar = [
        (6, 6, '1. İhrama Girmek', 'Mikat Sınırı (Haccın Farzı)', MAVI, MAVI_A),
        (184, 6, '2. Arafat Vakfesi', 'Arefe Günü (Haccın Farzı)', YES, YES_A),
        (6, 60, '3. Ziyaret Tavafı', 'Kâbe Çevresi (Haccın Farzı)', TUR, TUR_A),
        (184, 60, '4. Şeytan Taşlama & Sa’y', 'Mina ve Safa-Merve (Vacip)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Haccın üç farzı ve vacip görevlerinin karşılaştırılması.')


def son_ayet_ozgurluk_karti():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'Kâfirûn Suresi 6. Ayet-i Kerime', CAM, kalin=True)
    ic += yazi(180, 56, '«Leküm dînüküm veliye dîn.»', LAC, kalin=True)
    ic += yazi(180, 86, 'Anlamı: «Sizin dininiz size, benim dinim de banadır.»', YES, kalin=True)
    return svg(ic, 'Kâfirûn suresi 6. ayet okunuşu ve Türkçe meali.')


def sure_siralama_adimlari():
    adimlar = [
        (6, '1. Hitap', 'Kul yâ eyyühe’l…', MAVI, MAVI_A),
        (94, '2. Ret', 'Lâ a’büdü mâ…', KIR, KIR_A),
        (182, '3. Ayrım', 'Ve lâ entüm…', TUR, TUR_A),
        (270, '4. Hüküm', 'Leküm dînüküm…', YES, YES_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 34, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Kâfirûn suresi ayetlerinin başlangıçtan sona sıralaması.')


def enam_kafirun_karsilastirma():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, 'En’âm Suresi, 162. Ayet', MAVI, kalin=True)
    ic += yazi(92, 52, '«Namazım, ibadetlerim, hayatım', LAC)
    ic += yazi(92, 78, 've ölümüm yalnız Allah içindir.»', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 24, 'Kâfirûn Suresi, 2-6. Ayetler', TUR, kalin=True)
    ic += yazi(269, 52, '«Ben sizin taptıklarınıza tapmam;', LAC)
    ic += yazi(269, 78, 'benim dinim yalnız Allah’adır.»', TUR, kalin=True)
    return svg(ic, 'En’âm 162. ayet ile Kâfirûn suresinin ortak tevhit mesajı.')


def kurban_paylasim_karti():
    adimlar = [
        (6, '1/3 Pay', 'Ev Halkı ve Aile', MAVI, MAVI_A),
        (124, '1/3 Pay', 'Misafir ve Komşular', TUR, TUR_A),
        (242, '1/3 Pay', 'Yoksul ve Muhtaçlar', YES, YES_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 112, 103, z, r)
        ic += yazi(x + 56, 36, b1, r, kalin=True)
        ic += yazi(x + 56, 70, b2, LAC, kalin=True)
    return svg(ic, 'Kurban etinin üçe bölünerek paylaşılması şeması.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kafirun_kimlik_karti()
    s[2]['gorsel'] = unite_ibadet_kartlari()
    s[5]['gorsel'] = nuzul_sebebi_karti()
    s[6]['gorsel'] = hac_farzlari_semasi()
    s[7]['gorsel'] = son_ayet_ozgurluk_karti()
    s[8]['gorsel'] = sure_siralama_adimlari()
    s[9]['gorsel'] = enam_kafirun_karsilastirma()
    s[11]['gorsel'] = kurban_paylasim_karti()
