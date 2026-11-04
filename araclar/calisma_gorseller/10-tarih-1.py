"""10. sınıf Tarih 1. hafta (Dandanakan, Pasinler ve Malazgirt: Mücadeleleri Karşılaştırma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def g0_savaslar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    savaslar = [
        ('1040 Dandanakan', 'Devlet kuruldu', MAVI, MAVI_A),
        ('1048 Pasinler', 'Bizans\'a ilk zafer', TUR, TUR_A),
        ('1071 Malazgirt', 'Anadolu kapıları', YES, YES_A),
        ('1072 Beylikler', 'İlk Türk beylikleri', MOR, MOR_A)
    ]
    for i, (b, sonuc, c, d) in enumerate(savaslar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 60, sonuc, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Selçuklu askerî mücadeleleri ve tarihî sonuçları kartı', 34)


def g1_karsilastirma_tablosu():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'MÜCADELELERİN KARŞILAŞTIRILMASI', 11, MAVI)
    ic += kutu(14, 32, 106, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(67, 48, '1040 Dandanakan', 10, MAVI)
    ic += yazi(67, 68, 'Gaznelilere karşı', 9, LAC, ince=True)

    ic += kutu(126, 32, 106, 56, TUR_A, TUR, 6, 1.1)
    ic += yazi(179, 48, '1048 Pasinler', 10, TUR)
    ic += yazi(179, 68, 'Doğu Roma ile ilk', 9, LAC, ince=True)

    ic += kutu(238, 32, 106, 56, YES_A, YES, 6, 1.1)
    ic += yazi(291, 48, '1071 Malazgirt', 10, YES)
    ic += yazi(291, 68, 'Yurt edinme zaferi', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Dandanakan, Pasinler ve Malazgirt karşılaştırma tablosu', 34)


def g2_zaman_seridi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 340, 74, YES_A, YES, 8, 1.2)
    ic += yazi(180, 28, '1040 DANDANAKAN ZAFERİ VE DEVLETİN KURULUŞU', 11, YES)
    ic += yazi(180, 50, 'Tuğrul Bey sultan ilan edildi ve Büyük Selçuklu kuruldu.', 12, LAC)
    ic += yazi(180, 70, 'Horasan bölgesinde kesin Selçuklu hâkimiyeti başladı.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, '1040 Dandanakan zaferi ve Tuğrul Bey zaman kartı', 34)


def g3_askeri_ilkeler():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [
        ('Pasinler', 'İlk büyük meydan', MAVI, MAVI_A),
        ('Dandanakan', 'Horasan devleti', TUR, TUR_A),
        ('Alp Arslan', 'Malazgirt komutanı', YES, YES_A),
        ('Kınık Boyu', 'Oğuz kökeni', MOR, MOR_A)
    ]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel Selçuklu askerî ve siyasi ilkesi', 34)


def g5_ilerleme_akisi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. 1040', 'Dandanakan', YES, YES_A),
        ('2. 1048', 'Pasinler', MAVI, MAVI_A),
        ('3. 1071', 'Malazgirt', TUR, TUR_A),
        ('4. 1072+', 'Beylikler', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Türkistan\'dan Anadolu\'ya ilerleme kronolojisi', 34)


def g6_anadolu_haritasi():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'MALAZGİRT SONRASI ANADOLU\'DA TÜRK YERLEŞMESİ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 52, 'Saltuklular (Erzurum) · Danişmentliler (Sivas) · Mengücekliler (Erzincan)', 10, LAC)
    ic += yazi(180, 70, 'Fethedilen bölgelerde ilk Türk beylikleri kurulmaya başlandı.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Malazgirt zaferi sonrası ilk beylikler panosu', 34)


def g8_liderler():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    liderler = [
        ('Tuğrul Bey', 'İlk sultan', MAVI, MAVI_A),
        ('Çağrı Bey', 'Ordu komutanı', TUR, TUR_A),
        ('İbrahim Yınal', 'Pasinler fatihi', YES, YES_A),
        ('Alp Arslan', 'Malazgirt fatihi', MOR, MOR_A)
    ]
    for i, (b, tr, c, d) in enumerate(liderler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Dört büyük Selçuklu komutan ve devlet adamı', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: Z - A - F - E - R', 11.5, YES)
    harfler = [('1', 'Z'), ('2', 'A'), ('3', 'F'), ('4', 'E'), ('5', 'R')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Zafer şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_savaslar()
    s[1]['gorsel'] = g1_karsilastirma_tablosu()
    s[2]['gorsel'] = g2_zaman_seridi()
    s[3]['gorsel'] = g3_askeri_ilkeler()
    s[5]['gorsel'] = g5_ilerleme_akisi()
    s[6]['gorsel'] = g6_anadolu_haritasi()
    s[8]['gorsel'] = g8_liderler()
    s[10]['gorsel'] = g10_sifre_seridi()
