"""6. sınıf Türkçe 3. hafta (Türkçenin Beyliği: Anlam Tahmini, Anahtar Kelime, Ses Kullanımı ve Virgül) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def uc_dal_sema():
    ic = f'<rect x="6" y="6" width="588" height="100" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, '13. Yüzyılda Anadolu Türk Halkının Tutunduğu Üç Dal', 11.4, LAC)
    dallar = [
        ('1. Dal: Anayurt', 'Bu topraklardan ayrılmamaya', 've yurtta tutunmaya söz verir.', YES, YES_A),
        ('2. Dal: K = ?', 'Ahiler çarşıyı düzene sokar;', 'esnaf loncalarla korunur.', TUR, TUR_A),
        ('3. Dal: Gönül Dalı', 'Anadolu erenleri dikmiştir;', 'L = ?', MAVI, MAVI_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(dallar):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="62" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 68, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 84, s2, 10.2, LAC)
    return svg(600, 112, ic, 'Anadolu halkının tutunduğu üç dal şeması: 1. Anayurt, 2. K dalı, 3. Gönül dalı ve L açıklaması.', 22)


def virgul_kartlari():
    kartlar = [
        ('1. Kart: Tırnaksız Alıntı', 'Bu yazıtları dikkatle inceleyelim, dedi.', 'Alıntı cümlenin sonuna virgül konur.', MAVI, MAVI_A),
        ('2. Kart: Konuşma Çizgili Alıntı', '— Yeni kelimeleri deftere yazdım, dedi.', 'Alıntı sözün bitimine virgül konur.', YES, YES_A),
        ('3. Kart: Konuşma Öncesi İfade', 'Usta çırağına döndü. Çırağına, / — Gel, dedi.', 'Konuşma öncesi ifadeye soru işareti konur.', KIR, '#fdeaea'),
        ('4. Kart: Eş Görevli Kelimeler', 'Demirci, dokumacı, terzi loncada buluştu.', 'Eş görevli sözcükler arasına virgül konur.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 10.8, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.1, LAC, 'start')
        ic += yazi(x + 18, y + 46, s2, 10.0, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört virgül kartı: 1. Tırnaksız alıntı, 2. Konuşma çizgili alıntı, 3. Konuşma öncesi ifade (hatalı bilgi), 4. Eş görevli kelimeler.', 23)


def hikaye_unsur_karti():
    ic = f'<rect x="8" y="6" width="584" height="94" rx="10" fill="{KUM}" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += f'<rect x="8" y="6" width="584" height="24" rx="10" fill="{KAHVE}"/><rect x="8" y="20" width="584" height="10" fill="{KAHVE}"/>'
    ic += yazi(300, 22, 'HİKÂYE METNİ KARTI · Eski Sözlüğün Sırrı', 11.2, '#fff')
    ic += yazi(24, 48, '“Bir sonbahar ikindisinde Zeynep, kasabanın eski sahaflar çarşısındaki dükkâna girdi.', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 66, 'Sahaf Hüseyin Usta ile birlikte tozlu raftaki yıpranmış yazma sözlüğü dikkatle onardılar', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 84, 've içindeki unutulmuş Türkçe kelimeleri tek tek okuyup deftere kaydettiler.”', 10.5, LAC, 'start', ince=True)
    return svg(600, 106, ic, 'Hikâye metni kartı: Sonbahar ikindisinde Zeynep ve sahaf Hüseyin Usta kasabanın eski sahaflar çarşısında yıpranmış yazma sözlüğü onarıp okur.', 22)


def kelime_tahmin_karti():
    ic = f'<rect x="8" y="8" width="380" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(198, 26, 'Tuna’nın Kelime Tahmin Tablosu (“lonca”)', 11.2, MAVI)
    ic += yazi(22, 48, 'Tuna’nın Tahmini: Esnaf ve zanaatçıların kurduğu birlik', 10.3, LAC, 'start', ince=True)
    ic += yazi(22, 68, 'TDK Sözlük Anlamı: Belli bir iş kolundaki usta ve', 10.3, LAC, 'start', ince=True)
    ic += yazi(32, 84, 'esnafın oluşturduğu meslek örgütü, esnaf birliği.', 10.3, LAC, 'start', ince=True)

    ic += f'<rect x="400" y="8" width="192" height="88" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(496, 26, 'Tahmin Değerlendirme', 11.0, KAHVE)
    ic += yazi(414, 48, '★ Tamamen doğru: 3 yıldız', 10.2, YESIL_K, 'start')
    ic += yazi(414, 66, '★ Kısmen doğru: 2 yıldız', 10.2, TUR, 'start')
    ic += yazi(414, 84, '★ Doğru değil: 1 yıldız', 10.2, KIR, 'start')
    return svg(600, 104, ic, 'Tuna’nın lonca kelimesi için yaptığı tahmin, TDK sözlük anlamı ve yıldız değerlendirme ölçütü.', 22)


def tahmin_sureci_sema():
    adimlar = [
        ('1. Adım', 'Bilinmeyen kelimeyi', 'seçme', MAVI, MAVI_A),
        ('2. Adım', 'Bağlamdan tahmin', 'yazma', TUR, TUR_A),
        ('3. Adım', 'TDK Sözlük’ten', 'kontrol etme', MOR, MOR_A),
        ('4. Adım', 'Yıldız boyayarak', 'değerlendirme', YES, YES_A),
    ]
    ic = ''
    for i, (ust, s1, s2, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 28, ust, 11.2, renk)
        ic += yazi(x + 68, 52, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 68, 70, s2, 10.1, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 137}" y1="48" x2="{x + 147}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Kelime anlamını tahmin etme ve doğrulama sürecinin dört adımı.', 22)


def ses_tonu_panosu():
    roller = [
        ('Haber Spikeri', 'Ciddi ve açık seçik', 'bir tonla konuşur.', MAVI, MAVI_A),
        ('Şair', 'Duygusunu hissettirerek', 'acele etmeden okur.', MOR, MOR_A),
        ('Yaşlı Bilge', 'Sakin kalır, önemli', 'yerleri vurgular.', YES, YES_A),
        ('Duyuru Yapan', 'Sesini yüksek ve güçlü', 'tutar, dikkat çeker.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(roller):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.0, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.2, LAC, ince=True)
    return svg(600, 102, ic, 'Dört konuşmacı rolünün ses tonu özellikleri: Haber spikeri, Şair, Yaşlı bilge ve Duyuru yapan.', 22)


def anahtar_kelime_karti():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Anahtar Kelime Çözümleme Tablosu · Seçilen Kelime: “Töre”', 11.4, LAC)
    kutular = [
        ('1. Sözlük Anlamı', 'Bir toplulukta benimsenmiş', 'gelenek, görenek ve kurallar', MAVI, MAVI_A),
        ('2. Yakın Anlam ve Çağrışım', 'Yakın anlam: Gelenek / Âdet', 'Çağrışım: Toplumsal düzen', TUR, TUR_A),
        ('3. Deyim / Kalıp Söz', '“Töreye uymak” (Metnin', 'ana düşüncesini destekler)', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.7, renk)
        ic += yazi(x + 90, 67, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.1, LAC, ince=True)
    return svg(600, 110, ic, 'Töre anahtar kelimesi için sözlük anlamı, yakın anlam, çağrışım ve deyim çözümleme kartı.', 22)


def de_da_yazim_karti():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Cümle Kartı', 11.2, YESIL_K)
    ic += yazi(149, 50, '“Kardeşim bu akşam şiir de okudu.”', 10.8, LAC)
    ic += yazi(149, 72, '(“de” çıkarılınca: Kardeşim bu akşam şiir okudu.)', 10.0, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Cümle Kartı', 11.2, KIR)
    ic += yazi(451, 50, '“Çarşı da demirci ve terzi dükkânları vardı.”', 10.6, LAC)
    ic += yazi(451, 72, '(Bulunma yeri bildiriyor; çıkarılınca anlam bozuluyor.)', 10.0, LAC, ince=True)
    return svg(600, 102, ic, 'İki cümlede de/da yazımı karşılaştırma kartları.', 22)


def konusma_olcut_karti():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Mert’in “Ailemizde Sevgi Sözleri” Konuşması Öz Değerlendirme Kartı', 11.2, KAHVE)
    olcutler = [
        ('1. Ölçüt', 'Açık ve anlaşılır konuşma', '★ ★ ★ (Tam)', YES, YES_A),
        ('2. Ölçüt', 'Deneyimlerle ilişkilendirme', '★ ☆ ☆ (Eksik)', KIR, '#fdeaea'),
        ('3. Ölçüt', 'Sevgi ifadelerine yer verme', '★ ★ ★ (Tam)', MAVI, MAVI_A),
    ]
    for i, (bas, acik, yildiz, renk, arka) in enumerate(olcutler):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="58" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, acik, 10.2, LAC, ince=True)
        ic += yazi(x + 90, 83, yildiz, 10.6, renk)
    return svg(600, 108, ic, 'Mert’in konuşma değerlendirme kartı: açık ve anlaşılır konuşma 3 yıldız, deneyimlerle ilişkilendirme 1 yıldız, sevgi ifadelerine yer verme 3 yıldız.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = uc_dal_sema()
    s[4]['gorsel'] = virgul_kartlari()
    s[5]['gorsel'] = hikaye_unsur_karti()
    s[6]['gorsel'] = kelime_tahmin_karti()
    s[7]['gorsel'] = tahmin_sureci_sema()
    s[8]['gorsel'] = ses_tonu_panosu()
    s[9]['gorsel'] = anahtar_kelime_karti()
    s[10]['gorsel'] = de_da_yazim_karti()
    s[12]['gorsel'] = konusma_olcut_karti()
