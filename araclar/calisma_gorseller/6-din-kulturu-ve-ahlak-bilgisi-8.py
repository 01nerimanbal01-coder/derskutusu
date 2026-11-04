"""6. sınıf DKAB 8. hafta (Felak Suresi'nin Mesajları, İstiâze Bilinci ve 1. Ünite Genel Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); eğik kesir yok (K155); ayet levhası yok (K055)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def suhuf_dagilim_semasi():
    kartlar = [
        ('Hz. Âdem (a.s.)', '10 Suhuf', YES, YES_A),
        ('Hz. Şit (a.s.) (!)', '30 Suhuf (?)', KIR, KIR_A),
        ('Hz. İdris (a.s.) (!)', '50 Suhuf (?)', TUR, TUR_A),
        ('Hz. İbrahim (a.s.)', '10 Suhuf', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, sayi, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, ad, 12, '#fff')
        ic += yazi(x + 69, 62, sayi, 12, LAC)
    return svg(600, 96, ic, 'Dört peygambere gönderilen 100 suhuf şeması; Hz. Şit ve Hz. İdris sayıları yer değiştirmiş.', 22)


def felak_mesaj_kartlari():
    satirlar = [
        ('2. Ayet', 'Min şerri mâ halak → Yaratılmışların şerrinden sığınmak', YES, YES_A),
        ('3. Ayet', 'Gâsikın izâ vekab → Çöken gecenin tehlikelerine tedbir almak', MAVI, MAVI_A),
        ('4. Ayet', 'Neffâsâti fi’l-ukad → ? (Günlük yaşam ilkesi)', TUR, TUR_A),
        ('5. Ayet', 'Hâsidin izâ hased → Kıskançlık ve hasetten uzak durmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(51, y + 15, no, 12, '#fff')
        ic += yazi(104, y + 15, metin, 12, LAC, 'start', ince=(i != 2))
    return svg(600, 112, ic, 'Felak Suresi ayetlerinin günlük yaşam mesajları panosu; 4. ayet soru işaretli.', 22)


def sifat_zit_panosu():
    kartlar = [
        ('1. Sıdk', 'Doğruluk · Zıddı: Kizb', YES, YES_A),
        ('2. Emanet', '? · Zıddı: Hıyanet', MAVI, MAVI_A),
        ('3. Fetanet', 'Akıl ve zekâ · Zıddı: ?', TUR, TUR_A),
        ('4. Tebliğ', '? · Zıddı: Kitman', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 92, 30, renk, renk, 6, 1)
        ic += yazi(x + 52, y + 25, bas, 12, '#fff')
        ic += yazi(x + 194, y + 25, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Peygamberlerin sıfatları ve zıt kavramları panosu.', 22)


def ilahi_kitap_karsilastirma():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, 'Önceki Kitaplar (Tevrat · Zebur · İncil)', 12, '#fff')
    ic += yazi(150, 52, 'Belirli bir kavme ve döneme indi', 12, LAC, ince=True)
    ic += yazi(150, 74, 'Zamanla insanlarca değiştirildi', 12, KIR)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, 'Son İlahi Kitap: Kur’an-ı Kerim', 12, '#fff')
    ic += yazi(450, 52, 'Kıyamete dek tüm insanlığa (evrensel)', 12, LAC, ince=True)
    ic += yazi(450, 74, 'Aslı bozulmadan Allah’ın korumasında', 12, YES)
    return svg(600, 100, ic, 'Önceki ilahi kitaplar ile Kur’an-ı Kerim karşılaştırma kartları.', 22)


def peygamber_gorev_semasi():
    kutular = [
        ('1. Tebliğ Görevi', 'Vahyi eksiksiz iletmek', MAVI, MAVI_A),
        ('2. Beyan Görevi', 'Vahyi açıklayıp öğretmek', YES, YES_A),
        ('3. Temsil Görevi', 'Yaşayarak örnek olmak', TUR, TUR_A),
        ('4. Mucize', 'Allah’ın izniyle kanıt sunmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kutular):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Peygamberlerin tebliğ, beyan, temsil görevleri ve mucize kavramı şeması.', 22)


def tedbir_istiaze_kartlari():
    kartlar = [
        ('1. Durum', 'Çalışıp başarı için dua etmek', YES, YES_A),
        ('2. Durum', 'Kapıyı kilitleyip Felak okumak', MAVI, MAVI_A),
        ('3. Durum', 'Başarıya gıpta edip dua etmek', CAM, CAM_A),
        ('4. Durum (!)', 'Tedbirsizce nazar boncuğuna güvenmek', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 82, 30, renk, renk, 6, 1)
        ic += yazi(x + 47, y + 25, bas, 12, '#fff')
        ic += yazi(x + 190, y + 25, metin, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Dört durum kartı: ilk üçü tedbir ve istiâze, 4. durum batıl inanç.', 22)


def haset_gipta_sema():
    ic = kutu(8, 8, 284, 84, KIR_A, KIR, 9, 1.6)
    ic += kutu(8, 8, 284, 26, KIR, KIR, 9, 1)
    ic += yazi(150, 25, 'Haset (Kıskançlık — Yasak)', 12, '#fff')
    ic += yazi(150, 52, 'Başkasındaki nimetin yok olmasını ister', 12, LAC, ince=True)
    ic += yazi(150, 74, 'Birey huzurunu ve kardeşliği yıkar', 12, KIR)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, 'Gıpta (İmrenme — Güzel Tutum)', 12, '#fff')
    ic += yazi(450, 52, 'Nimetin onda kalmasını ve kendisinde', 12, LAC, ince=True)
    ic += yazi(450, 74, 'de olmasını diler · Sevgiyi artırır', 12, YES)
    return svg(600, 100, ic, 'Haset ve gıpta kavramlarının birey ve toplum üzerindeki etkilerini karşılaştıran şema.', 22)


def unite_ozet_tablosu():
    satirlar = [
        ('1. Satır', 'Cebrail (a.s.) → Vahiy meleğidir', YES, YES_A),
        ('2. Satır (!)', 'Hâtemü’l-Enbiyâ → Hz. Âdem’in unvanıdır (?)', KIR, KIR_A),
        ('3. Satır', 'Muavvizeteyn → Felak ve Nâs sureleridir', MAVI, MAVI_A),
        ('4. Satır', 'Mucize → Allah’ın izniyle gerçekleşen kanıttır', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 92, 22, renk, renk, 6, 1)
        ic += yazi(54, y + 15, no, 12, '#fff')
        ic += yazi(110, y + 15, metin, 12, LAC, 'start', ince=(i != 1))
    return svg(600, 112, ic, '1. ünite genel değerlendirme tablosu; 2. satırda Hâtemü’l-Enbiyâ unvanı yanlış eşleştirilmiş.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = suhuf_dagilim_semasi()
    s[4]['gorsel'] = felak_mesaj_kartlari()
    s[5]['gorsel'] = sifat_zit_panosu()
    s[6]['gorsel'] = ilahi_kitap_karsilastirma()
    s[8]['gorsel'] = peygamber_gorev_semasi()
    s[9]['gorsel'] = tedbir_istiaze_kartlari()
    s[11]['gorsel'] = haset_gipta_sema()
    s[12]['gorsel'] = unite_ozet_tablosu()
