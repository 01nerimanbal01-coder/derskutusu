"""7. sınıf DKAB 1. hafta (Varlıklar âlemi, gayb ve meleklerin özellikleri ile görevleri) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:calc(16mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def bilgi_yollari_sema():
    kartlar = [
        ('1. Örnek: Bahçedeki Ağaç', 'Çıplak gözle doğrudan', 'görülüp incelenir.', 'K', YES, YES_A),
        ('2. Örnek: Mikroorganizma', 'Mikroskop gibi gözlem', 'araçlarıyla seçilir.', 'L', MAVI, MAVI_A),
        ('3. Örnek: Meleklerin Görevleri', 'Duyuların ötesindedir;', 'vahiyle öğrenilir.', 'M', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="6" width="192" height="116" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="6" width="192" height="26" rx="10" fill="{renk}"/><rect x="{x}" y="20" width="192" height="12" fill="{renk}"/>'
        ic += yazi(x + 96, 23, bas, 11.2, '#fff')
        ic += yazi(x + 96, 52, s1, 11.2, LAC, ince=True)
        ic += yazi(x + 96, 70, s2, 11.2, LAC, ince=True)
        ic += f'<rect x="{x + 28}" y="84" width="136" height="28" rx="7" fill="#fff" stroke="{renk}" stroke-width="1.5" stroke-dasharray="4 3"/>'
        ic += yazi(x + 96, 102, f'Bilgi yolu: {harf} ?', 11.5, renk)
    return svg(600, 128, ic, 'Üç varlık örneği ve bilgi edinme yolları: 1. Bahçedeki ağaç (K), 2. Mikroorganizma (L), 3. Meleklerin görevleri (M).', 23)


def ozellik_gorev_pano():
    kartlar = [
        ('1', 'Özellik Kartı (Mavi)', 'Melekler nurdan yaratılmıştır;', 'yeme ve uyku ihtiyaçları yoktur.', MAVI, MAVI_A),
        ('2', 'Özellik Kartı (Mavi)', 'Mikâil yağmur ve rüzgâr gibi', 'tabiat olaylarını düzenler.', MAVI, MAVI_A),
        ('3', 'Görev Kartı (Yeşil)', 'Meleklerin cinsiyeti yoktur ve', 'sayılarını yalnız Allah bilir.', YES, YES_A),
        ('4', 'Görev Kartı (Yeşil)', 'Cebrail ilahi vahyi peygamberlere', 'ulaştırmakla yükümlüdür.', YES, YES_A),
    ]
    ic = ''
    for i, (no, bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 66
        ic += f'<rect x="{x}" y="{y}" width="286" height="58" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += rozet(x + 20, y + 29, no, renk, 10, 11.5)
        ic += yazi(x + 38, y + 18, bas, 11.2, renk, 'start')
        ic += yazi(x + 38, y + 36, s1, 11, LAC, 'start', ince=True)
        ic += yazi(x + 38, y + 51, s2, 11, LAC, 'start', ince=True)
    return svg(600, 136, ic, 'Dört sınıflandırma kartı: 1. Nurdan yaratılma, 2. Mikâil tabiat olayları, 3. Cinsiyet olmaması, 4. Cebrail vahiy.', 24)


def varlik_kartlari():
    kart = [
        ('1. Kart · Dağ ve Deniz', 'Çıplak gözle doğrudan', 'görülen somut varlıklar', YES, YES_A),
        ('2. Kart · Uzak Gök Cismi', 'Çok uzakta olduğu için', 'teleskopla incelenen cisim', MAVI, MAVI_A),
        ('3. Kart · Meleklerin Sayısı', 'Duyularla algılanamayan', 'gayb âlemi bilgisi', TUR, TUR_A),
        ('4. Kart · Merhamet Duygusu', 'Gözle görülmeyen ancak', 'yardım davranışında hissedilen', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 62
        ic += f'<rect x="{x}" y="{y}" width="286" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="54" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 48, s2, 10.8, LAC, 'start', ince=True)
    return svg(600, 128, ic, 'Dört varlık kartı: 1. Dağ ve deniz, 2. Uzak gök cismi, 3. Meleklerin sayısı, 4. Merhamet duygusu.', 22)


def uc_varlik_karsilastirma():
    kutular = [
        ('K Varlığı: ?', 'Nurdan yaratılmıştır.', 'Allah’ın emrine karşı gelmez.', MAVI, MAVI_A),
        ('L Varlığı: ?', 'İrade ve sorumluluk taşır.', 'İnanan ve inanmayanları vardır.', TUR, TUR_A),
        ('Şeytan (İblis)', 'Cinlerdendir; kibirlenerek', 'ilahi emre karşı gelmiştir.', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="8" width="192" height="96" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 96, 28, bas, 12, renk)
        ic += f'<line x1="{x + 16}" y1="36" x2="{x + 176}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 96, 58, s1, 11, LAC, ince=True)
        ic += yazi(x + 96, 78, s2, 11, LAC, ince=True)
    return svg(600, 112, ic, 'Gayb âlemindeki üç kavramın karşılaştırması: K (nurdan, itaatkâr), L (sorumlu, inanan/inanmayan), Şeytan (cinlerden, asi).', 22)


def arastirma_adimlari():
    adlar = [
        ('1. Adım', 'Soruyu Belirle', MAVI, MAVI_A),
        ('2. Adım', 'Kur’an ve Sünnet', YES, YES_A),
        ('3. Adım', 'Özellik / Görev', TUR, TUR_A),
        ('4. Adım', 'Anahtar Eşleştir', MOR, MOR_A),
        ('5. Adım', 'Kontrol Et', ALTIN, '#fffbe6'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 8 + i * 118
        ic += f'<rect x="{x}" y="12" width="98" height="68" rx="12" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 49, 36, ust, 11.5, renk)
        ic += yazi(x + 49, 58, alt, 10.8, LAC)
        if i < 4:
            ic += f'<line x1="{x + 100}" y1="46" x2="{x + 116}" y2="46" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 111} 41 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 92, ic, 'Melekler araştırmasında 5 basamaklı akış: Soruyu belirle, Kur’an ve sünnet, Özellik/görev ayır, Anahtar eşleştir, Öğretmen kontrolü.', 20)


def adem_kissasi_pano():
    ic = f'<rect x="6" y="6" width="290" height="108" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += yazi(151, 24, 'Hz. Âdem Kıssasından İlkeler', 12, KAHVE)
    ic += yazi(20, 46, 'Melekler: “Seni tenzih ederiz; senin bize', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 62, '  öğrettiğinden başka bilgimiz yoktur.”', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 82, 'İblis cinlerdendir; kibirlenip emre', 10.8, KIR, 'start', ince=True)
    ic += yazi(20, 98, '  uymamış, melekler ise itaat etmiştir.', 10.8, LAC, 'start', ince=True)

    ic += f'<rect x="306" y="6" width="288" height="108" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(450, 24, 'Kavram Çıkarımı', 12, MAVI)
    ic += yazi(320, 48, '1) Melekler her şeyi kendiliğinden bilmez.', 10.8, LAC, 'start', ince=True)
    ic += yazi(320, 68, '2) Gaybı yalnız Allah bilir.', 10.8, YESIL_K, 'start')
    ic += yazi(320, 88, '3) İblis’in isyanı meleklere mal edilemez.', 10.8, LAC, 'start', ince=True)
    return svg(600, 120, ic, 'Hz. Âdem kıssasında meleklerin bilgisi ve İblis’in durumu.', 23)


def dort_buyuk_melek_sema():
    ogeler = [
        ('1. Bölüm', 'Cebrail (Cibril)', 'Ruhulkudüs / Ruhulemin', 'Görev: İlahi vahiy', MAVI, MAVI_A),
        ('2. Bölüm', 'Mikâil', 'Doğa ve rızık düzeni', 'Görev: Tabiat olayları', YES, YES_A),
        ('3. Bölüm', 'İsrafil', 'Kıyamet ve yeniden diriliş', 'Görev: Sûra üfleme', TUR, TUR_A),
        ('4. Bölüm', 'Azrail', 'Melekülmevt (Ölüm meleği)', 'Görev: Can alma', MOR, MOR_A),
    ]
    ic = ''
    for i, (bol, ad, unvan, gor, renk, arka) in enumerate(ogeler):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="142" height="108" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 71, 23, bol, 11, renk)
        ic += yazi(x + 71, 43, ad, 11.5, LAC)
        ic += yazi(x + 71, 63, unvan, 10.5, LAC, ince=True)
        ic += f'<rect x="{x + 10}" y="76" width="122" height="26" rx="6" fill="#fff" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 71, 93, gor, 10.5, renk)
    return svg(600, 120, ic, 'Dört büyük melek şeması: 1. Cebrail (vahiy), 2. Mikâil (tabiat), 3. İsrafil (sûr), 4. Azrail (can alma).', 23)


def yazici_sorgu_kartlari():
    ic = f'<rect x="6" y="6" width="286" height="102" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += rozet(26, 26, '1', MAVI, 11, 11.5)
    ic += yazi(158, 26, '1. Görev Kartı: ?', 12, MAVI)
    ic += yazi(149, 52, 'İnsanın sağında ve solunda yer', 11.2, LAC, ince=True)
    ic += yazi(149, 70, 'alarak iyi ve kötü davranışları', 11.2, LAC, ince=True)
    ic += yazi(149, 88, 'eksiksiz kaydeden yazıcı melekler', 11.2, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="102" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += rozet(328, 26, '2', YES, 11, 11.5)
    ic += yazi(460, 26, '2. Görev Kartı: ?', 12, YESIL_K)
    ic += yazi(451, 52, 'Ölümden sonra kabirde insanları', 11.2, LAC, ince=True)
    ic += yazi(451, 70, 'inanç ve yaşayışlarıyla ilgili', 11.2, LAC, ince=True)
    ic += yazi(451, 88, 'sorgulamakla görevli melekler', 11.2, YESIL_K)
    return svg(600, 114, ic, '1. Görev kartı: davranışları kaydeden yazıcı melekler; 2. Görev kartı: kabirde sorgulayan melekler.', 22)


def gayb_tartisma_karti():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{TUR_A}" stroke="{KIR}" stroke-width="1.8"/>'
    ic += yazi(149, 25, 'Yanlış İddia Kartı', 12, KIR)
    ic += yazi(149, 49, '“Gelecek hafta yaşanacak bütün', 11, LAC, ince=True)
    ic += yazi(149, 67, 'olayları cinlerden kesin olarak', 11, LAC, ince=True)
    ic += yazi(149, 85, 'öğrendim ve biliyorum.”', 11, KIR)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(451, 25, 'İslam’ın Bilgi Ölçütü', 12, YESIL_K)
    ic += yazi(451, 49, 'Gaybı yalnız Allah bilir.', 11, LAC, ince=True)
    ic += yazi(451, 67, 'Peygamberler vahiyle bildirileni bilir.', 11, LAC, ince=True)
    ic += yazi(451, 85, 'Kaynaksız iddialara itibar edilmez.', 11, YESIL_K)
    return svg(600, 110, ic, 'Yanlış iddia kartı (cinlerden geleceği öğrenme iddiası) ve İslam’ın gayb bilgi ölçütü.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bilgi_yollari_sema()
    s[4]['gorsel'] = ozellik_gorev_pano()
    s[5]['gorsel'] = varlik_kartlari()
    s[6]['gorsel'] = uc_varlik_karsilastirma()
    s[7]['gorsel'] = arastirma_adimlari()
    s[8]['gorsel'] = adem_kissasi_pano()
    s[9]['gorsel'] = dort_buyuk_melek_sema()
    s[10]['gorsel'] = yazici_sorgu_kartlari()
    s[12]['gorsel'] = gayb_tartisma_karti()
