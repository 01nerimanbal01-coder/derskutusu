"""5. sınıf Türkçe 5. hafta (Bir İp Bul, Oyuna Başla!: Yönerge Okuma, Görsel Okuma, Oyun Söz Varlığı, Hazırlıksız Konuşma ve Karşılaştırma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def okuma_amaci_yontem_kartlari():
    kartlar = [
        ('1. Kart · Oyunu Oynamak', 'Kuralları adım adım okuma', YES, YES_A),
        ('2. Kart · Bilgi Bulmak (!)', 'Tüm metni ezberleyerek okuma', KIR, KIR_A),
        ('3. Kart · Oyunu Tanıtmak (!)', 'Oyun başlıklarını atlama', TUR, TUR_A),
        ('4. Kart · Keyif Almak (!)', 'Yalnızca sayfa sayısına bakma', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okuma amacına göre seçilen okuma yöntemlerini gösteren dört kart.', 20)


def karsilastirma_cumle_kartlari():
    satirlar = [
        ('1. Kart', 'Çocuklar hafta sonu okul bahçesinde neşeyle mendil kapmaca oynadı.', MAVI, MAVI_A),
        ('2. Kart (!)', 'İp atlama da dijital oyun da kurallarla oynanır; oysa ip atlama hareket ettirir.', YES, YES_A),
        ('3. Kart', 'Kedi beşiği oyununda iki ucu birbirine bağlanmış orta kalınlıkta ip kullanılır.', TUR, TUR_A),
        ('4. Kart', 'Halat çekme yarışması başlamadan önce ortaya düz bir sınır çizgisi çizilir.', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(100, y + 15, metin, LAC, 'start', kalin=(i == 1))
    return svg(600, 112, ic, 'Benzerlik ve farklılık ifadeleri içeren karşılaştırma cümle kartları.', 20)


def gorsel_mesaj_tablo_kartlari():
    kartlar = [
        ('1. Ortadaki Çizgi ve Halat', 'Oyun halat çekmedir (Açık)', MAVI, MAVI_A),
        ('2. Neşeyle Gülen İfadeler', 'Oyun eğlencelidir (Örtük)', YES, YES_A),
        ('3. Numaralar ve Yön Okları', 'Hareket sırası ve yönü (Açık)', TUR, TUR_A),
        ('4. Siyah-Beyaz Eski Kare', 'Eskiden de oynanırdı (Örtük)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Görsel okuma unsurlarının açık ve örtük mesaj kartları.', 20)


def yuzey_anlam_yorum_karti():
    ic = kutu(6, 6, 588, 88, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'YÖNERGE METNİ · İP ÇEVİRME OYUNU', '#fff', kalin=True)
    ic += yazi(300, 48, '“İp çevirme oyunu en az 5 oyuncu ve 3 m uzunluğunda bir iple bahçede oynanır.”', LAC, kalin=True)
    ic += yazi(300, 74, 'Soru A: Kaç oyuncuyla oynanır?  |  Soru B: İp neden yere yakın çevrilmelidir?', MAVI, kalin=True)
    return svg(600, 100, ic, 'Yönerge metninde yüzey anlam ve yorum sorularını karşılaştıran kart.', 20)


def hazirliksiz_konusma_plani():
    kartlar = [
        ('1. Giriş', 'Oyunun adını söyleme', MAVI, MAVI_A),
        ('2. Hazırlık', 'Kişi sayısı ve malzeme', YES, YES_A),
        ('3. Süreç', 'Başlangıç ve kurallar', TUR, TUR_A),
        ('4. Bitiş', 'Bitiş ve kazanan kuralı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Hazırlıksız konuşmada dört soruluk zihinsel plan aşamaları.', 20)


def yonerge_yazim_denetimi():
    satirlar = [
        ('1. Adım', '1. Oyuncular bahçede geniş bir çember oluşturur.', YES, YES_A),
        ('2. Adım', '2. Ebe eline 3 m uzunluğunda sağlam bir ip alır.', MAVI, MAVI_A),
        ('3. Adım (!)', '3. ebe ipi yerden çevirir ve oyuncular zıplar', KIR, KIR_A),
        ('4. Adım', '4. İpe değen oyuncu yeni ebe olarak ortaya geçer.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 90, 22, renk, renk, 6, 1)
        ic += yazi(51, y + 15, no, '#fff', kalin=True)
        ic += yazi(106, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'Yönerge yazımında sıra sayısı, büyük harf ve noktalama denetimi panosu.', 20)


def ses_ve_beden_dili_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 25, '1. Ses ve Hız Ayarı', MAVI, kalin=True)
    ic += yazi(149, 50, '• Kuralları yavaş ve tane tane söyle', LAC, kalin=True)
    ic += yazi(149, 74, '• Önemli kuralı vurgula, adım arası dur', LAC)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, '2. Beden Dili ve Etkileşim', YESIL_K, kalin=True)
    ic += yazi(451, 50, '• Hareketleri elinle göstererek açıkla', LAC, kalin=True)
    ic += yazi(451, 74, '• Dinleyenlerle göz teması kur', LAC)
    return svg(600, 98, ic, 'Hazırlıksız konuşmada ses kullanımı ve beden dili rehber kartı.', 20)


def soz_varligi_panosu():
    kartlar = [
        ('Zıt Anlam İlişkisi', 'kazanmak ↔ kaybetmek · başlamak ↔ bitmek', MAVI, MAVI_A),
        ('Eş Anlam İlişkisi', 'yarış = müsabaka · kural = ilke', YES, YES_A),
        ('Genel ve Tür Adı', 'ip (genel) → sicim (ince), halat/urgan (kalın)', TUR, TUR_A),
        ('İp Deyimleri', 'ipin ucunu kaçırmak · ipleri eline almak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Oyun söz varlığı, anlam ilişkileri ve ip deyimleri bilgi panosu.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = okuma_amaci_yontem_kartlari()
    s[4]['gorsel'] = karsilastirma_cumle_kartlari()
    s[5]['gorsel'] = gorsel_mesaj_tablo_kartlari()
    s[6]['gorsel'] = yuzey_anlam_yorum_karti()
    s[7]['gorsel'] = hazirliksiz_konusma_plani()
    s[8]['gorsel'] = yonerge_yazim_denetimi()
    s[10]['gorsel'] = ses_ve_beden_dili_karti()
    s[11]['gorsel'] = soz_varligi_panosu()
