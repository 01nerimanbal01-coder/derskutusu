"""12. sınıf T.C. İnkılap Tarihi 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.8, kc) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Mondros maddeleri ve ilk işgal/direniş', [('7. Madde', 'İşgallere hukuki kılıf', KIR, KIR_A), ('24. Madde', 'Doğu’da 6 il planı', TUR, TUR_A), ('Musul (3 Kasım)', 'İlk işgal edilen yer', MAVI, MAVI_A), ('Hatay Dörtyol', 'İlk silahlı direniş', YES, YES_A)])

def g1():
    return pano('Mondros 24. madde Vilayat-ı Sitte altı doğu ili', 'MONDROS 24. MADDE · VİLÂYÂT-I SİTTE (ALTI DOĞU İLİ - BESDEV)', 'Bitlis · Erzurum · Sivas · Diyarbakır · Elazığ (Harput) · Van', 'Karışıklık çıkarsa işgal edilecek denilerek Doğu’da Ermeni devleti amaçlanmıştır.', KIR, KIR_A, '#fde8e7')

def g2():
    return pano('18 Ocak 1919 Paris Barış Konferansı ve İzmir kararı', 'PARİS BARIŞ KONFERANSI (18 OCAK 1919) · İLK GÖRÜŞ AYRILIĞI', 'Gizli antlaşmalarda İtalya’ya vaat edilen İzmir, İngiltere’nin etkisiyle Yunanistan’a verildi.', 'Bu karar İtilaf Devletleri arasındaki ilk görüş ayrılığını başlatmıştır.', MAVI, MAVI_A, '#f4f8fe')

def g3():
    return kart4('Wilson, Mondros fiilen bitiş ve telgraf denetimi', [('Wilson Md. 12', 'Türklere egemenlik', YES, YES_A), ('Mondros Etkisi', 'Fiilen sona erdirdi', TUR, TUR_A), ('13 Kasım 1918', 'Geldikleri gibi giderler', MAVI, MAVI_A), ('Telgraf Denetimi', 'Örgütlenmeyi önleme', MOR, MOR_A)])

def g5():
    return akis4('1918-1919 mütareke dönemi kronolojisi', [('1. Ocak 1918', 'Wilson İlkeleri', MAVI, MAVI_A), ('2. 30 Ekim 1918', 'Mondros Ateşkesi', TUR, TUR_A), ('3. 3 Kasım 1918', 'Musul’un İşgali', KIR, KIR_A), ('4. Ocak 1919', 'Paris Konferansı', MOR, MOR_A)])

def g6():
    return pano('I. Dünya Savaşı sonu imzalanan barış antlaşmaları', 'I. DÜNYA SAVAŞI SONUNDA İMZALANAN BARIŞ ANTLAŞMALARI', 'Almanya: Versay  ·  Avusturya: Sen Jermen  ·  Bulgaristan: Nöyi', 'Macaristan: Triyanon  ·  Osmanlı: Sevr (Geçersiz taslak) -> Lozan (1923)', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Rauf Orbay, manda-himaye ve Milletler Cemiyeti', 'MONDROS ATEŞKESİ VE PARİS KONFERANSI KAVRAMLARI', 'İmzalayan: Rauf (Orbay) Bey  ·  Yeni Sömürgecilik: Manda ve Himaye', 'Uluslararası Örgüt: Milletler Cemiyeti (Cemiyet-i Akvam)', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Milli direniş kavramları ve öncüleri', [('Kuvâ-yı Milliye', 'Milis direniş gücü', YES, YES_A), ('Mehmet Çavuş', 'Dörtyol ilk kurşun', TUR, TUR_A), ('Hasan Tahsin', 'İzmir ilk kurşun', MAVI, MAVI_A), ('Ahmet İzzet Pş.', 'Mondros hükümeti', MOR, MOR_A)])

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
