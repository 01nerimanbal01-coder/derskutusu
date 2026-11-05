"""12. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.4, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.4, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.4, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.4, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Yararlı (millî) cemiyetler ve bölgeleri', [('Trakya-Paşaeli', 'Doğu Trakya savunması', MAVI, MAVI_A), ('Kilikyalılar', 'Çukurova (Adana)', YES, YES_A), ('Millî Kongre', 'Dr. Esat Işık · Basın', TUR, TUR_A), ('Trabzon M. H.', 'Pontus’a karşı mücadele', MOR, MOR_A)])

def g1():
    return uclu('Amasya Genelgesi gerekçe, amaç ve yöntem', 'AMASYA GENELGESİ (22 HAZİRAN 1919) · KURTULUŞ PLANI', ('Gerekçe 1', 'Vatan bütünlüğü tehlikede', KIR, KIR_A), ('Gerekçe 2', 'İstanbul görev yapamıyor', TUR, TUR_A), ('Amaç ve Yöntem', 'Milletin azim ve kararı!', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('İzmir işgali ve Amiral Bristol Raporu', 'İZMİR’İN İŞGALİ (15 MAYIS 1919) VE AMİRAL BRİSTOL RAPORU', 'İlk Kurşun: Gazeteci Hasan Tahsin → Kuvâ-yı Millîye ruhunun doğuşu', 'Amiral Bristol Raporu: Türklerin çoğunlukta ve haklı olduğunu kanıtlayan ilk uluslararası belge', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('Hazırlık dönemi önemli bilgiler', [('Kilikyalılar', 'Yararlı millî cemiyet', YES, YES_A), ('Erzurum Kong.', 'Bölgesel → Ulusal karar', MAVI, MAVI_A), ('Sivas Kongresi', 'Manda kesin reddedildi', KIR, KIR_A), ('Sine-i Millet', '7-8 Temmuz istifası', MOR, MOR_A)])

def g5():
    return akis4('Millî Mücadele hazırlık kronolojisi', [('1. Samsun', '19 Mayıs 1919 çıkış', MAVI, MAVI_A), ('2. Amasya', '22 Haziran Genelge', TUR, TUR_A), ('3. Kongreler', 'Erzurum ve Sivas', YES, YES_A), ('4. Ankara', '27 Aralık 1919 merkez', MOR, MOR_A)])

def g6():
    return pano('Sivas Kongresi sonrası siyasi başarı ve Amasya Görüşmeleri', 'TEMSİL HEYETİ’NİN SİYASİ BAŞARILARI', '1. Damat Ferit Paşa Hükûmeti’nin İstifası: Temsil Heyeti’nin ilk siyasi başarısı', '2. Amasya Görüşmeleri (20-22 Ekim 1919): İstanbul Hükûmeti Temsil Heyeti’ni resmen tanıdı', MOR, MOR_A, '#f5f0ff')

def g7():
    return pano('Hasan Tahsin, ARMHC ve Yürütme Yetkisi', 'KUVÂ-YI MİLLÎYE VE ULUSAL ÖRGÜTLENME', 'Hasan Tahsin (İlk Kurşun) · ARMHC (Cemiyetlerin Birleşmesi) · Yürütme Yetkisi', 'Ali Fuat Paşa’nın Batı Cephesi’ne atanması Temsil Heyeti’nin hükûmet gibi çalıştığını gösterir.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Zararlı cemiyetler ve Ankara’nın seçimi', [('Mavri Mira', 'Megali İdea (Rum)', KIR, KIR_A), ('Hınçak-Taşnak', 'Ermeni devleti amacı', TUR, TUR_A), ('Mandacılar', 'İngiliz/ABD himayesi', MOR, MOR_A), ('Ankara Merkez', 'Demiryolu · Batı’ya yakın', YES, YES_A)])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
