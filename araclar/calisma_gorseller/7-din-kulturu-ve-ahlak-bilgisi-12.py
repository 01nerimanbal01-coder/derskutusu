"""7. sınıf Din Kültürü ve Ahlak Bilgisi 12. hafta (Hac ve Kurbanın Kültürümüze Yansımaları, En'âm 162) görselleri.
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


def enam_162_karti():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 26, "En'âm Suresi 162. Ayet-i Kerime", YES, kalin=True)
    ic += yazi(180, 52, '«De ki: Şüphesiz benim namazım, ibadetlerim (kurbanım),', LAC, kalin=True)
    ic += yazi(180, 74, 'hayatım ve ölümüm âlemlerin Rabbi olan Allah içindir.»', LAC, kalin=True)
    ic += yazi(180, 96, 'Temel Mesaj: Tevhit · İhlas · Allah’a (cc) Tam Teslimiyet', MAVI, kalin=True)
    return svg(ic, "En'âm suresi 162. ayet meali ve tevhit-ihlas mesajı kartı.")


def kultur_yansima_panosu():
    kartlar = [
        (6, 6, '1. Surre Alayı & Haremeyn', 'Tarih ve Vakıf Medeniyeti', MAVI, MAVI_A),
        (184, 6, '2. Kurbanın 3’e Bölünmesi', 'Kurban · Yardımlaşma', YES, YES_A),
        (6, 60, '3. «Kurban Olduğum»', 'Kurban · Dil ve Deyimler', TUR, TUR_A),
        (184, 60, '4. Zemzem ve Hurma', 'Hac/Umre · Misafirperverlik', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Hac ve kurban ibadetinin kültürümüzdeki dört farklı yansıması.')


def kurban_paylasim_semasi():
    paylar = [
        (6, '1/3 Pay', 'Ev Halkı ve Aile', MAVI, MAVI_A),
        (124, '1/3 Pay', 'Komşu ve Misafirler', TUR, TUR_A),
        (242, '1/3 Pay', 'Yoksul ve Muhtaçlar', YES, YES_A),
    ]
    ic = ''
    for x, p, aciklama, r, z in paylar:
        ic += kutu(x, 6, 112, 103, z, r)
        ic += yazi(x + 56, 36, p, r, kalin=True)
        ic += yazi(x + 56, 66, aciklama, LAC, kalin=True)
        ic += yazi(x + 56, 92, 'Sünnete Uygun Pay', r)
    return svg(ic, 'Kurban etinin üç eşit paya bölünerek paylaşılması şeması.')


def hac_umre_karsilastirma():
    ic = kutu(6, 6, 112, 103, MAVI_A, MAVI)
    ic += yazi(62, 26, 'Yalnız Hacda', MAVI, kalin=True)
    ic += yazi(62, 52, 'Arafat Vakfesi', LAC)
    ic += yazi(62, 74, 'Müzdelife · Mina', LAC)
    ic += yazi(62, 95, 'Hükmü: Farz', MAVI, kalin=True)
    ic += kutu(124, 6, 112, 103, YES_A, YES)
    ic += yazi(180, 26, 'Ortak Unsurlar', YES, kalin=True)
    ic += yazi(180, 52, 'İhram (Mikat)', LAC, kalin=True)
    ic += yazi(180, 74, 'Kâbe Tavafı', LAC, kalin=True)
    ic += yazi(180, 95, 'Safa-Merve Sa’y', YES, kalin=True)
    ic += kutu(242, 6, 112, 103, TUR_A, TUR)
    ic += yazi(298, 26, 'Umre İbadeti', TUR, kalin=True)
    ic += yazi(298, 52, 'Yılın Her Günü', LAC)
    ic += yazi(298, 74, 'Vakfe/Kurban Yok', LAC)
    ic += yazi(298, 95, 'Hükmü: Sünnet', TUR, kalin=True)
    return svg(ic, 'Hac ve umre ibadetlerinin ortak ve farklı yönleri şeması.')


def surre_alayi_karti():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 28, 'Osmanlı Kültür Mirası: Surre Alayları ve Haremeyn', TUR, kalin=True)
    ic += yazi(180, 56, 'Her yıl Recep ayında İstanbul’dan dualarla uğurlanan kervan,', LAC)
    ic += yazi(180, 78, 'Mekke ve Medine (Haremeyn) halkına yardım ve hediyeler ulaştırırdı.', LAC, kalin=True)
    ic += yazi(180, 98, 'Amaç: Kutsal beldelere hizmet ve kardeşlik köprüsü kurmak', MAVI, kalin=True)
    return svg(ic, 'Osmanlı Surre Alayları ve Haremeyn hizmet geleneği bilgi kartı.')


def hac_adimlari_sirasi():
    adimlar = [
        (6, '1. Mikat', 'İhram & Niyet', MAVI, MAVI_A),
        (94, '2. Arefe', 'Arafat Vakfesi', YES, YES_A),
        (182, '3. Mina', 'Taşlama & Kurban', TUR, TUR_A),
        (270, '4. Kâbe', 'Ziyaret Tavafı', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Hac ibadetinin dört temel aşamasının sıralama şeması.')


def kurban_cesitleri_tablosu():
    kartlar = [
        (6, 6, '1. Udhiyye Kurbanı', 'Kurban Bayramı · Vacip', YES, YES_A),
        (184, 6, '2. Akika Kurbanı', 'Yeni Doğan Çocuk · Şükür', MAVI, MAVI_A),
        (6, 60, '3. Adak Kurbanı', 'Şarta Bağlı · Vacip', TUR, TUR_A),
        (184, 60, '4. Hedy Kurbanı (?)', 'Ramazan Bayramı Sadakası?', KIR, KIR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört farklı kurban çeşidi ve açıklamaları karşılaştırma kartı.')


def enam_teslimiyet_ozeti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 28, 'İbadette İhlas', MAVI, kalin=True)
    ic += yazi(92, 56, 'Namaz ve kurbanı yalnız', LAC)
    ic += yazi(92, 78, 'Allah (cc) rızası için yapmak', LAC, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 28, 'Hayatta Sorumluluk', YES, kalin=True)
    ic += yazi(269, 56, 'Hayatı ve ölümü Allah’a', LAC)
    ic += yazi(269, 78, '(cc) tam teslimiyetle yaşamak', LAC, kalin=True)
    return svg(ic, "En'âm suresi 162. ayetin ibadet ve hayat bilincine katkısı.")


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = enam_162_karti()
    s[2]['gorsel'] = kultur_yansima_panosu()
    s[5]['gorsel'] = kurban_paylasim_semasi()
    s[6]['gorsel'] = hac_umre_karsilastirma()
    s[7]['gorsel'] = surre_alayi_karti()
    s[8]['gorsel'] = hac_adimlari_sirasi()
    s[9]['gorsel'] = kurban_cesitleri_tablosu()
    s[11]['gorsel'] = enam_teslimiyet_ozeti()
