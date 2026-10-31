"""5. sınıf Türkçe 7. hafta (Mustafa Dinleme/İzleme: Hikâye Unsurları, Gerçek-Kurgusal Unsurlar, Geçiş ve Bağlantı İfadeleri ve Noktalama) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def hikaye_haritasi_kutulari_svg():
    kutular = [
        ('K Kutusu', '1893 yılının güneşli', 'bir sonbahar sabahı', MAVI, MAVI_A),
        ('L Kutusu', 'Selanik Askerî Rüştiyesi', 'matematik dersliği', TUR, TUR_A),
        ('M Kutusu', 'Mustafa ve öğretmeni', 'Yüzbaşı Mustafa Efendi', MOR, MOR_A),
        ('N Kutusu', 'Başarısıyla öğretmeninden', '“Kemal” adını alması', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="8" width="136" height="24" rx="9" fill="{renk}"/><rect x="{x}" y="22" width="136" height="10" fill="{renk}"/>'
        ic += yazi(x + 68, 24, bas, 10.8, '#fff')
        ic += yazi(x + 68, 54, s1, 10.3, LAC, ince=True)
        ic += yazi(x + 68, 74, s2, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Mustafa metni hikâye haritası K, L, M ve N kutuları: 1893 sonbaharı, Selanik Askerî Rüştiyesi, Mustafa ve öğretmeni, Kemal adını alması.', 22)


def gecis_ifadeleri_kartlari_svg():
    kartlar = [
        ('1. Kart: “Yoruldu ama çalışmayı bırakmadı.”', 'Görev: Düşüncenin yönünü değiştirme', MAVI, MAVI_A),
        ('2. Kart: “Derslerini, özellikle matematiği severdi.”', 'Görev: Düşünceyi destekleme ve açıklama', YES, YES_A),
        ('3. Kart: “Kısacası azimle hedefine ulaştı.”', 'Görev: Düşüncenin yönünü değiştirme', KIR, '#fdeaea'),
        ('4. Kart: “Engeller çıktı; buna rağmen vazgeçmedi.”', 'Görev: Düşüncenin yönünü değiştirme', TUR, TUR_A),
    ]
    ic = ''
    for i, (cumle, gorev, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 20, cumle, 10.2, LAC, 'start')
        ic += yazi(x + 14, y + 39, gorev, 10.2, renk, 'start', ince=True)
    return svg(600, 124, ic, 'Dört geçiş ifadesi kartı: 1. ama, 2. özellikle, 3. kısacası (yanlış görev yazılmış), 4. buna rağmen.', 23)


def mustafa_sahne_kartlari_svg():
    kartlar = [
        ('1. Sahne', 'Şemsi Efendi Mektebine', 'kaydolup okula başlaması', MAVI, MAVI_A),
        ('2. Sahne', 'Tarladaki korkuluğun', 'Mustafa’ya öğüt vermesi', TUR, TUR_A),
        ('3. Sahne', 'Askerî Rüştiye sınavına', 'girip okulu kazanması', YES, YES_A),
        ('4. Sahne', 'Rüzgârın Mustafa’nın', 'kulağına fısıldaması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.3, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Mustafa metninden dört sahne kartı: Şemsi Efendi Mektebi, konuşan korkuluk, Askerî Rüştiye sınavı ve fısıldayan rüzgâr.', 22)


def diyalog_noktalama_karti_svg():
    ic = f'<rect x="8" y="8" width="584" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Matematik Dersliği Diyalog Kartı', 11.2, MAVI)
    ic += f'<line x1="28" y1="34" x2="572" y2="34" stroke="{MAVI}" stroke-width="1.1"/>'
    ic += yazi(40, 56, 'Yüzbaşı Mustafa Efendi öğrencisine dönerek şöyle dedi ( 1 )', 10.8, LAC, 'start', ince=True)
    ic += yazi(40, 78, '( 2 ) Bundan böyle senin adın Mustafa Kemal olsun ( 3 )', 10.8, KIR, 'start')
    return svg(600, 104, ic, 'Matematik öğretmeni Yüzbaşı Mustafa Efendi’nin konuşmasında 1, 2 ve 3 numaralı yay ayraçlar.', 22)


def egitim_kronoloji_adimlari_svg():
    adimlar = [
        ('İlkokul Başlangıcı', 'Şemsi Efendi Mektebi', MAVI, MAVI_A),
        ('Çiftlik Günleri', 'Dayısının yanında kalma', TUR, TUR_A),
        ('Rüştiye Sınavı', 'Selanik Askerî Rüştiyesi', MOR, MOR_A),
        ('Kemal Adını Alma', 'Matematik dersi başarısı', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11, renk)
        ic += yazi(x + 68, 62, alt, 10.4, LAC, ince=True)
    return svg(600, 96, ic, 'Küçük Mustafa’nın eğitim hayatındaki dört gelişmenin kronolojik şeması.', 22)


def konu_ana_fikir_notlari_svg():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Öğrenci Notu K', 11.2, MAVI)
    ic += yazi(149, 52, '“Mustafa’nın çocukluk yıllarında', 10.6, LAC, ince=True)
    ic += yazi(149, 72, 'karşılaştığı güçlükler ve okuma tutkusu”', 10.6, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Öğrenci Notu L', 11.2, YESIL_K)
    ic += yazi(451, 52, '“Engeller karşısında yılmadan çalışan ve', 10.5, LAC, ince=True)
    ic += yazi(451, 72, 'okuyan kişiler hedeflerine ulaşır.”', 10.5, LAC, ince=True)
    return svg(600, 104, ic, 'K notunda metnin konusu, L notunda metnin ana fikri yazılı iki öğrenci kartı.', 22)


def yazim_kesme_calisma_yapragi_svg():
    cumleler = [
        ('1. Cümle:', 'Selanikli küçük Mustafa kitap okumayı çok severdi.', YES, YES_A),
        ('2. Cümle:', '29 ekim cumhuriyet bayramı’nı törenle kutladık.', KIR, '#fdeaea'),
        ('3. Cümle:', 'Mustafa Kemal, Türkçe’yi özenli ve kurallı kullanırdı.', TUR, TUR_A),
        ('4. Cümle:', 'Atatürkün hayatı hepimize ilham kaynağı olmaktadır.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, renk, arka) in enumerate(cumleler):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 54
        ic += f'<rect x="{x}" y="{y}" width="286" height="46" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 12, y + 18, bas, 10.6, renk, 'start')
        ic += yazi(x + 12, y + 36, met, 10, LAC, 'start', ince=True)
    return svg(600, 116, ic, 'Özel adların yazımı ve kesme işaretiyle ilgili dört numaralı cümle kartı.', 22)


def iki_bosluklu_gecis_karti_svg():
    ic = f'<rect x="8" y="8" width="584" height="90" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Geçiş ve Bağlantı İfadeleri Tamamlama Kartı', 11.2, TUR)
    ic += f'<line x1="24" y1="34" x2="576" y2="34" stroke="{TUR}" stroke-width="1.1"/>'
    ic += yazi(24, 56, 'Mustafa çiftlikte kargaları kovalıyordu; [ I ] fırsat buldukça kitap okuyordu.', 10.4, LAC, 'start', ince=True)
    ic += yazi(24, 78, 'O tüm derslerine özenle çalışırdı, [ II ] matematik dersine ayrı ilgi duyardı.', 10.4, LAC, 'start', ince=True)
    return svg(600, 106, ic, 'I ve II numaralı boşlukların bulunduğu iki geçiş ifadesi cümlesi.', 22)


def gercek_kurgu_amac_karti_svg():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Tarihî Gerçeklik Boyutu', 11, MAVI)
    ic += yazi(149, 50, 'Selanik’te doğması, okuduğu okullar', 10.5, LAC, ince=True)
    ic += yazi(149, 70, 've “Kemal” adını alması gerçektir.', 10.5, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Sanatsal Kurgu Boyutu', 11, MOR)
    ic += yazi(451, 50, 'Hayalî diyaloglar ve kişileştirmeler', 10.5, LAC, ince=True)
    ic += yazi(451, 70, 'esere duygu ve merak katar.', 10.5, LAC, ince=True)
    return svg(600, 102, ic, 'Tarihî gerçeklik boyutu ile sanatsal kurgu boyutunu karşılaştıran iki bilgi kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = hikaye_haritasi_kutulari_svg()
    s[4]['gorsel'] = gecis_ifadeleri_kartlari_svg()
    s[5]['gorsel'] = mustafa_sahne_kartlari_svg()
    s[6]['gorsel'] = diyalog_noktalama_karti_svg()
    s[7]['gorsel'] = egitim_kronoloji_adimlari_svg()
    s[8]['gorsel'] = konu_ana_fikir_notlari_svg()
    s[9]['gorsel'] = yazim_kesme_calisma_yapragi_svg()
    s[10]['gorsel'] = iki_bosluklu_gecis_karti_svg()
    s[12]['gorsel'] = gercek_kurgu_amac_karti_svg()
