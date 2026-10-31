"""6. sınıf DKAB 2. hafta (İnsanlara Rehber: Peygamber — Bilgileri Ayet ve Hadisle Doğrulama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155); ayet levhası yok (K055)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def ibrahim_kissa_akisi():
    adimlar = [
        ('1. Adım', 'Bayram günü şehir boşalır;', 'tapınağa geri dönülür.', MAVI, MAVI_A),
        ('2. Adım', 'Büyük put dışındakiler kırılır;', 'balta büyük puta asılır.', MAVI, MAVI_A),
        ('3. Adım', '“Belki büyük put yapmıştır,', 'konuşabiliyorsa ona sorun.”', TUR, TUR_A),
        ('4. Adım (?)', '“Hiçbir şey yapamıyorsa niçin', 'ondan yardım diliyorsunuz?”', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(adimlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 56
        ic += kutu(x, y, 286, 48, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 74, 36, renk, renk, 6, 1)
        ic += yazi(x + 43, y + 28, bas, 10.6, '#fff')
        ic += yazi(x + 184, y + 21, s1, 10.4, LAC)
        ic += yazi(x + 184, y + 38, s2, 10.2, SOLUK, ince=True)
    return svg(600, 118, ic, 'Hz. İbrahim kıssasının dört adımlı akış şeması.', 23)


def istasyon_plani():
    koseler = [
        ('1. İstasyon (4 dk.)', 'Kur’an’da Adı Geçen', 'Peygamberler Köşesi', MAVI, MAVI_A),
        ('2. İstasyon (4 dk.)', 'Peygamberlerin Görevleri', '(Süre doldu: yarısı boş)', TUR, TUR_A),
        ('3. İstasyon (4 dk.)', 'Peygamberlerin Özellikleri', '(Sıradaki geçiş köşesi)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(koseler):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 84, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 24, renk, renk, 9, 1)
        ic += yazi(x + 94, 24, bas, 10.8, '#fff')
        ic += yazi(x + 94, 52, s1, 10.6, LAC)
        ic += yazi(x + 94, 72, s2, 10.2, renk, ince=True)
    return svg(600, 100, ic, 'Peygamberleri Tanıyalım etkinliği üç istasyon köşesi ve dört dakikalık süre döngüsü.', 22)


def ayet_hadis_kartlari():
    kartlar = [
        ('1. Kart: Maide 67 ve 92', '“Rabb’inden indirileni tebliğ et; Resul’ün görevi apaçık duyurmaktır.”', MAVI, MAVI_A),
        ('2. Kart: Nisa 165', '“İnsanların bahanesi kalmasın diye müjdeleyici ve uyarıcı elçiler gönderdik.”', TUR, TUR_A),
        ('3. Kart: İbrahim 4', '“Açıklasın diye her peygamberi kendi kavminin diliyle gönderdik.”', MOR, MOR_A),
        ('4. Kart: Buhari, Ezan', '“Ben namazı nasıl kılıyorsam siz de öyle kılın.”', YES, YES_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        y = 6 + i * 28
        ic += kutu(8, y, 584, 24, arka, renk, 6, 1.4)
        ic += kutu(8, y, 166, 24, renk, renk, 6, 1)
        ic += yazi(91, y + 16, bas, 10.4, '#fff')
        ic += yazi(184, y + 16, metin, 10.2, LAC, 'start', ince=True)
    return svg(600, 120, ic, 'Dört doğrulama kartı: Maide 67-92, Nisa 165, İbrahim 4 ve Buhari Ezan hadisi.', 23)


def hadis_tugla_karti():
    ic = kutu(8, 8, 284, 86, TUR_A, TUR, 9, 1.6)
    ic += yazi(150, 26, '1. Hadis: Bina ve Son Tuğla (Buhari)', 10.8, TUR)
    # Tuğla duvar çizimi
    for r in range(2):
        for c in range(4):
            bx, by = 36 + c * 54, 36 + r * 22
            bos = (r == 0 and c == 3)
            ic += kutu(bx, by, 50, 18, '#fff' if bos else '#d97724', TUR, 3, 1.2, ' stroke-dasharray="4 3"' if bos else '')
            if bos:
                ic += yazi(bx + 25, by + 13, 'Son Tuğla', 10, TUR)
    ic += kutu(308, 8, 284, 86, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(450, 28, '2. Hadis: İnsanlığın Atası (Tirmizi)', 10.8, MAVI)
    ic += yazi(450, 52, '“İnsanlar Âdem’in çocuklarıdır', 10.6, LAC)
    ic += yazi(450, 72, 've Âdem topraktan yaratılmıştır.”', 10.6, LAC, ince=True)
    return svg(600, 102, ic, 'Solda son tuğla benzetmesi hadis kartı, sağda Hz. Âdem hadis kartı.', 22)


def bilgi_toplama_adimlari():
    adimlar = [
        ('1. BUL', 'Kur’an ve TDV kaynağı', MAVI, MAVI_A),
        ('2. NOT ET', 'Kaynak adıyla not et', CAM, CAM_A),
        ('3. DOĞRULA', 'Ayet ve hadisle sına', TUR, TUR_A),
        ('4. KAYDET', 'Şema, kart ve günlük', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 76, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 136, 24, renk, renk, 9, 1)
        ic += yazi(x + 68, 24, bas, 10.8, '#fff')
        ic += yazi(x + 68, 56, alt, 10.2, LAC, ince=True)
    return svg(600, 92, ic, 'Bilgi toplamanın dört basamağı: Bul, Not Et, Doğrula ve Kaydet.', 22)


def yazalim_semasi():
    ic = kutu(8, 6, 584, 98, KUM, GRI, 10, 1.5)
    ic += yazi(300, 24, '“Yazalım” Şeması — Kerem’in Seçimleri (Havuz: Farsça, Arapça, vahiy, 25, 28, resul-nebi)', 10.5, LAC)
    kutular = [
        ('1. Kökeni', 'Farsça', YES, YES_A),
        ('2. Aldığı mesaj', 'vahiy', MAVI, MAVI_A),
        ('3. Kur’an’daki sayı', 'yirmi sekiz (!)', KIR, KIR_A),
        ('4. Kur’an’daki adları', 'resul ve nebi', TUR, TUR_A),
    ]
    for i, (ust, c, renk, arka) in enumerate(kutular):
        x = 16 + i * 144
        ic += kutu(x, 34, 136, 58, arka, renk, 8, 1.5)
        ic += yazi(x + 68, 54, ust, 10.5, SOLUK, ince=True)
        ic += yazi(x + 68, 76, c, 11, renk)
    return svg(600, 110, ic, 'Yazalım şeması: 1 Farsça, 2 vahiy, 3 yirmi sekiz (hatalı seçim), 4 resul ve nebi.', 20)


def kart_321_kontrol():
    satirlar = [
        ('3 BİLGİ', 'Vahiy-tebliğ farkı · Kur’an’da 25 peygamber adı · Kur’an en büyük mucizedir', MAVI, MAVI_A),
        ('2 KAVRAM', 'Çalışmam gereken iki kavram: nübüvvet ve ismet', TUR, TUR_A),
        ('1 KAVRAM', '“Babil halkı bayramda kırlara çıktı, Hz. İbrahim putları kırdı…” (Kıssa özeti)', KIR, KIR_A),
    ]
    ic = ''
    for i, (etiket, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 32
        ic += kutu(8, y, 584, 28, arka, renk, 7, 1.5)
        ic += kutu(8, y, 106, 28, renk, renk, 7, 1)
        ic += yazi(61, y + 18, etiket, 10.6, '#fff')
        ic += yazi(124, y + 18, metin, 10.2, LAC, 'start', ince=True)
    return svg(600, 104, ic, 'Zeynep’in 3-2-1 kartı: 3 bilgi, 2 kavram ve 1 kavram satırında kavram yerine yazılmış kıssa özeti.', 22)


def kaynak_karsilastirma():
    ic = kutu(8, 8, 282, 82, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(149, 28, 'Tarih Kaynağı (M. Asım Köksal)', 10.8, MAVI)
    ic += yazi(149, 50, 'Peygamberler Tarihi eserinde', 10.4, LAC, ince=True)
    ic += yazi(149, 68, 'Hz. İbrahim kıssası aktarılır.', 10.4, LAC, ince=True)

    ic += kutu(310, 8, 282, 82, YES_A, YES, 9, 1.6)
    ic += yazi(451, 28, 'Temel Kaynak (Enbiya 62-63. Ayetler)', 10.8, YES)
    ic += yazi(451, 50, '“Belki onu şu büyükleri yapmıştır,', 10.4, LAC, ince=True)
    ic += yazi(451, 68, 'konuşabiliyorlarsa onlara sorun!”', 10.4, LAC, ince=True)
    return svg(600, 98, ic, 'Sol kartta M. Asım Köksal Peygamberler Tarihi, sağ kartta Enbiya suresi 62-63. ayetler.', 22)


def ogrenme_gunlugu_karti():
    ic = kutu(8, 6, 584, 86, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 6, 584, 24, MOR, MOR, 9, 1)
    ic += yazi(300, 22, 'KONTROL NOKTASI · ÖĞRENME GÜNLÜĞÜM', 10.8, '#fff')
    ic += yazi(24, 48, '1. Beni en çok etkileyen bilgi : Hz. İbrahim’in insanları düşündürerek yol göstermesi', 10.4, LAC, 'start')
    ic += yazi(24, 72, '2. Etkilenme sebebim ve doğrulayan ayet : ………………………………………………………………', 10.4, MOR, 'start', ince=True)
    return svg(600, 98, ic, 'Kontrol Noktası öğrenme günlüğü kartı: etkileyen bilgi ve sebebi.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ibrahim_kissa_akisi()
    s[4]['gorsel'] = istasyon_plani()
    s[5]['gorsel'] = ayet_hadis_kartlari()
    s[6]['gorsel'] = hadis_tugla_karti()
    s[7]['gorsel'] = bilgi_toplama_adimlari()
    s[8]['gorsel'] = yazalim_semasi()
    s[9]['gorsel'] = kart_321_kontrol()
    s[10]['gorsel'] = kaynak_karsilastirma()
    s[12]['gorsel'] = ogrenme_gunlugu_karti()
