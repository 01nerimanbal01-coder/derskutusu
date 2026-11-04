"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 2. hafta (Mustafa Kemal'in Çocukluğu ve Eğitim Hayatı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def manastir_sahsiyet_kartlari():
    kartlar = [
        ('Mehmet Tevfik Bey', 'Tarih öğretmeni · Tarih bilinci', MAVI, MAVI_A),
        ('Ömer Naci', 'Sınıf arkadaşı · Edebiyat ve şiir', TUR, TUR_A),
        ('Mehmet Asım Efendi', 'Öğretmeni · Hitabet sanatı', MOR, MOR_A),
        ('Ali Fethi (Okyar)', 'Arkadaşı · Fransız düşünürleri', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Manastır Askerî İdadisinde Mustafa Kemal i etkileyen dört şahsiyet.', 13)


def selanik_ortam_sema():
    kutular = [
        ('Ticaret ve Ulaşım', 'İşlek liman ve demir yolu', 'Batı’daki yeniliklere açık', MAVI, MAVI_A),
        ('Çok Uluslu Yapı', 'Farklı etnik ve dinî gruplar', 'Hoşgörü ve fikirlere saygı', YES, YES_A),
        ('Azınlık İsyanları', 'Çete olayları ve göçler', 'Vatanseverlik ve millî bilinç', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kutular):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.6, r)
        ic += yazi(x + 96, 46, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.1, r)
    return svg(600, 86, ic, 'Selânik şehrinin özellikleri ve Mustafa Kemal in kişiliğine etkileri.', 13)


def aile_ve_egitim_panosu():
    ic = kutu(6, 6, 286, 74, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Aile Ortamı ve İlköğrenim (1886)', 10.6, MAVI)
    ic += yazi(149, 45, '• Uzlaşmacı ve demokratik aile tutumu', 10.0, LAC, ince=True)
    ic += yazi(149, 64, '• Mahalle Mektebi → Şemsi Efendi Mektebi', 10.0, MAVI)

    ic += kutu(308, 6, 286, 74, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Rüştiye ve Harp Akademisi (1894–1905)', 10.6, TUR)
    ic += yazi(451, 45, '• Nakiyüddin Bey: Özgürlük ve demokrasi', 10.0, LAC, ince=True)
    ic += yazi(451, 64, '• 1905 Kurmay Yüzbaşı → Şam 5. Ordu', 10.0, TUR)
    return svg(600, 86, ic, 'Aile ortamı, ilköğrenim ve askerî eğitim bilgileri panosu.', 13)


def kisilik_cikarim_kartlari():
    kartlar = [
        ('1. Kart · Zorlukta Okuma', '→ Azimli ve kararlı olma', YES, YES_A),
        ('2. Kart · Askerlik Sınavı', '→ İdealist ve öz güvenli', MAVI, MAVI_A),
        ('3. Kart · Edebiyat ve Dil', '→ Çok yönlü kişilik', TUR, TUR_A),
        ('4. Kart · Okul Gazetesi', '→ Siyasete duyarsızlık (!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.2, r)
        ic += yazi(x + 71, 52, alt, 9.8, LAC, ince=True)
    return svg(600, 80, ic, 'Mustafa Kemal in öğrencilik davranışları ve kişilik özellikleri kartları.', 13)


def okullar_zaman_seridi():
    okullar = [
        ('1886 · İlkokul', 'Mahalle · Şemsi Ef.', MAVI, MAVI_A),
        ('1894 · Ortaokul', 'Askerî Rüştiye', TUR, TUR_A),
        ('1896 · Lise', 'Manastır İdadisi', MOR, MOR_A),
        ('1899 · Yüksek', 'İstanbul Harp Ok.', YES, YES_A),
        ('1902–1905', 'Harp Akademisi', CAM, CAM_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(okullar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 66, z, r, 8, 1.4)
        ic += yazi(x + 56, 26, bas, 10.1, r)
        ic += yazi(x + 56, 50, alt, 9.6, LAC, ince=True)
    return svg(600, 78, ic, 'Mustafa Kemal in okuduğu okulların kronolojik zaman şeridi.', 12)


def okul_gazetesi_karti():
    ic = kutu(6, 6, 588, 72, MOR_A, MOR, 8, 1.5)
    ic += yazi(300, 24, 'İstanbul Harp Okulu ve Harp Akademisi Yılları (1899–1905)', 10.8, MOR)
    ic += yazi(300, 46, 'Faaliyet: Ülke sorunlarına dikkat çekmek için arkadaşlarını örgütleyip el yazması okul gazetesi çıkardı.', 10.0, LAC, ince=True)
    ic += yazi(300, 64, 'Kanıtladığı Kişilik Özellikleri: Liderlik · Teşkilatçılık (Örgütleyicilik) · Vatanseverlik', 10.2, MOR)
    return svg(600, 84, ic, 'Okul gazetesi çıkarma faaliyetinin gösterdiği kişilik özellikleri.', 13)


def ogretmen_onur_tablosu():
    sutunlar = [
        ('K Öğretmeni (Rüştiye)', 'Matematik dersinde', '“Kemal” adını verdi', MAVI, MAVI_A),
        ('L Öğretmeni (İdadi)', '“Bana yeni ufuk açtı”', 'Tarih bilinci kazandırdı', TUR, TUR_A),
        ('M Öğretmeni (Akademi)', 'Harp Akademisinde', 'Taktik ve strateji öğretti', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(sutunlar):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.5, r)
        ic += yazi(x + 96, 46, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.1, r)
    return svg(600, 86, ic, 'Mustafa Kemal e katkıda bulunan K, L ve M öğretmenleri tablosu.', 13)


def iki_mektep_karsilastirma():
    ic = kutu(6, 6, 286, 70, TUR_A, TUR, 8, 1.5)
    ic += yazi(149, 24, 'Mahalle Mektebi (Geleneksel)', 10.6, TUR)
    ic += yazi(149, 46, 'Klasik yöntemlerle eğitim verir;', 10.0, LAC, ince=True)
    ic += yazi(149, 63, 'Zübeyde Hanım’ın isteğiyle başladı.', 10.0, TUR)

    ic += kutu(308, 6, 286, 70, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Şemsi Efendi Mektebi (Modern)', 10.6, YES)
    ic += yazi(451, 46, 'Yeni usul ders araçları ve bilimsel yöntem;', 10.0, LAC, ince=True)
    ic += yazi(451, 63, 'Ali Rıza Efendi’nin isteğiyle tamamladı.', 10.0, YES)
    return svg(600, 82, ic, 'Geleneksel Mahalle Mektebi ile modern Şemsi Efendi Mektebi karşılaştırması.', 13)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = manastir_sahsiyet_kartlari()
    s[1]['gorsel'] = selanik_ortam_sema()
    s[3]['gorsel'] = aile_ve_egitim_panosu()
    s[5]['gorsel'] = kisilik_cikarim_kartlari()
    s[6]['gorsel'] = okullar_zaman_seridi()
    s[7]['gorsel'] = okul_gazetesi_karti()
    s[8]['gorsel'] = ogretmen_onur_tablosu()
    s[11]['gorsel'] = iki_mektep_karsilastirma()
