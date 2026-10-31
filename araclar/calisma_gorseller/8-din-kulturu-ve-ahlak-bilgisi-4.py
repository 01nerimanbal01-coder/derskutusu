"""8. sınıf DKAB 4. hafta (Kaderle İlgili Kavramlar: ömür, ecel, rızık, tevekkül, başarı, sağlık ve hastalık, veba olayı) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def kum_saati_sema():
    ic = f'<rect x="6" y="6" width="356" height="128" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    # Kum saati çizimi
    ic += f'<rect x="26" y="18" width="68" height="8" rx="3" fill="{KAHVE}"/>'
    ic += f'<rect x="26" y="114" width="68" height="8" rx="3" fill="{KAHVE}"/>'
    ic += f'<path d="M32 26 L88 26 C88 54 63 66 61 70 C63 74 88 86 88 114 L32 114 C32 86 57 74 59 70 C57 66 32 54 32 26 Z" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<path d="M40 42 L80 42 C76 54 64 62 60 66 C56 62 44 54 40 42 Z" fill="{ALTIN}"/>'
    ic += f'<path d="M36 112 L84 112 C80 98 70 88 60 82 C50 88 40 98 36 112 Z" fill="{ALTIN}"/>'
    ic += f'<circle cx="60" cy="75" r="2.8" fill="{TUR}"/>'
    # K ve L kutuları
    ic += f'<rect x="108" y="18" width="242" height="48" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += rozet(126, 42, 'K', MAVI, 10, 11.5)
    ic += yazi(144, 36, 'Kumların tamamı:', 11.5, MAVI, 'start')
    ic += yazi(144, 54, 'Doğumdan ölüme yaşanan süre', 11, LAC, 'start', ince=True)
    ic += f'<rect x="108" y="74" width="242" height="48" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.4"/>'
    ic += rozet(126, 98, 'L', TUR, 10, 11.5)
    ic += yazi(144, 92, 'Son kum tanesinin düştüğü an:', 11.5, TUR, 'start')
    ic += yazi(144, 110, 'Yaşam süresinin bittiği an', 11, LAC, 'start', ince=True)
    # Sağ kart: Ankebut 57
    ic += f'<rect x="372" y="6" width="222" height="128" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(483, 28, 'Ankebut suresi 57. ayet', 12, KAHVE)
    ic += yazi(483, 54, '“Her canlı ölümü tadacak', 11.5, LAC, ince=True)
    ic += yazi(483, 74, 've sonunda dönüp', 11.5, LAC, ince=True)
    ic += yazi(483, 94, 'huzurumuza geleceksiniz.”', 11.5, LAC, ince=True)
    ic += yazi(483, 118, '(Tohum, ağaç, balina, yıldızlar)', 10.5, KAHVE, ince=True)
    return svg(600, 140, ic, 'Kum saati benzetmesi: K kumların tamamı (doğumdan ölüme yaşanan süre), L son kum tanesinin düştüğü an (yaşam süresinin bittiği an) ve Ankebut suresi 57. ayet.', 25)


def rizik_panosu():
    ic = f'<rect x="6" y="6" width="286" height="122" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'Doğada Rızık İçin Çaba', 12, YESIL_K)
    ic += yazi(20, 48, '• Kuşların uzak ülkelere göç etmesi', 11, LAC, 'start', ince=True)
    ic += yazi(20, 68, '• Balinaların okyanusları aşması', 11, LAC, 'start', ince=True)
    ic += yazi(20, 88, '• Arıların uzaktaki çiçekleri bulması', 11, LAC, 'start', ince=True)
    ic += yazi(149, 114, 'Kaynak: Er-Rezzak olan Allah', 11, YESIL_K)

    ic += f'<rect x="308" y="6" width="286" height="122" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'İslam’da Kazanç İlkeleri', 12, TUR)
    ic += f'<rect x="320" y="36" width="262" height="38" rx="6" fill="#fff" stroke="{YES}" stroke-width="1.3"/>'
    ic += yazi(330, 52, 'Helal Yol:', 11, YESIL_K, 'start')
    ic += yazi(392, 52, 'Alın teri ve emekle kazanmak', 11, LAC, 'start', ince=True)
    ic += yazi(330, 68, '(Necm 39: İnsan çabasının sonucunu alır)', 10.5, YESIL_K, 'start', ince=True)
    ic += f'<rect x="320" y="80" width="262" height="38" rx="6" fill="#fff" stroke="{KIR}" stroke-width="1.3"/>'
    ic += yazi(330, 96, 'Uygun Olmayan:', 11, KIR, 'start')
    ic += yazi(424, 96, 'Hırsızlık, şans oyunları,', 11, LAC, 'start', ince=True)
    ic += yazi(330, 112, 'haksız kazanç, tembellik ve dilenmek', 10.5, KIR, 'start', ince=True)
    return svg(600, 134, ic, 'Rızık panosu: solda doğada rızık için çaba örnekleri, sağda İslam’da helal kazanç ve uygun olmayan yollar.', 25)


def ayet_hadis_kartlari():
    kartlar = [
        ('1. Kart · Necm 39–40', '“İnsan ancak çabasının sonucunu elde eder.', 'Çabasının karşılığı mutlaka görülecektir.”', MAVI, MAVI_A),
        ('2. Kart · Nisa 71', '“Ey iman edenler! Tedbirinizi alın...”', '(Önce önlem, sonra Allah’a güven)', MOR, MOR_A),
        ('3. Kart · Bakara 168', '“Yeryüzünde bulunan maddelerin helâl', 've temiz olanlarından yiyin...”', YES, YES_A),
        ('4. Kart · Hadis (Ebu Davud)', '“Tedavi olunuz; çünkü Allah yarattığı', 'her hastalığın şifasını da yaratmıştır.”', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 66
        ic += f'<rect x="{x}" y="{y}" width="286" height="58" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="58" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 36, s1, 11, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 51, s2, 11, LAC, 'start', ince=True)
    return svg(600, 136, ic, 'Dört ayet ve hadis kartı: 1. Necm 39-40, 2. Nisa 71, 3. Bakara 168, 4. Ebu Davud Tıb 1 hadisi.', 25)


def hicret_tevekkul_sema():
    ic = f'<rect x="8" y="8" width="272" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += rozet(28, 28, '1', MAVI, 11, 11.5)
    ic += yazi(152, 29, '1. Aşama: Tedbir ve Görev', 12, MAVI)
    ic += yazi(144, 56, 'Hicret yolculuğunda güvenlik için', 11.5, LAC, ince=True)
    ic += yazi(144, 74, 'Mekke’nin güneyindeki', 11.5, LAC, ince=True)
    ic += yazi(144, 92, 'Sevr Mağarası’na gidilmesi', 11.5, MAVI)

    ic += f'<line x1="286" y1="60" x2="314" y2="60" stroke="{LAC}" stroke-width="2.2"/><path d="M309 55 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="320" y="8" width="272" height="104" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += rozet(340, 28, '2', YES, 11, 11.5)
    ic += yazi(464, 29, '2. Aşama: Tevbe suresi 40. ayet', 12, YESIL_K)
    ic += yazi(456, 56, 'Endişelenen Hz. Ebu Bekir’e:', 11.5, LAC, ince=True)
    ic += yazi(456, 74, '“Tasalanma! Allah bizimle', 11.5, YESIL_K)
    ic += yazi(456, 92, 'beraberdir.” buyrulması', 11.5, YESIL_K)
    return svg(600, 120, ic, 'Hicret yolculuğunda tevekkülün iki aşaması: 1. Sevr Mağarası tedbiri, 2. Tevbe suresi 40. ayetteki Allah’a güven.', 23)


def veba_olayi_zinciri():
    adlar = [
        ('1. Adım', 'Serğ Köyü Haberi', MAVI, MAVI_A),
        ('2. Adım', 'İstişare ve Karar', MOR, MOR_A),
        ('3. Adım', 'Kaderden Kadere', TUR, TUR_A),
        ('4. Adım', 'İki Yamaç Örneği', ALTIN, '#fffbe6'),
        ('5. Adım', 'Hadis ve Dönüş', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += f'<rect x="{x}" y="12" width="102" height="72" rx="12" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 51, 38, ust, 11.5, renk)
        ic += yazi(x + 51, 62, alt, 11, LAC)
        if i < 4:
            ic += f'<line x1="{x + 104}" y1="48" x2="{x + 117}" y2="48" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 113} 43 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Veba olayının 5 halkalı akış şeması: Serğ Köyü haberi, istişare, kaderden kadere sözü, iki yamaç örneği, hadis ve Medine’ye dönüş.', 22)


def basari_tutum_kartlari():
    kartlar = [
        ('Kaan', 'Düzenli antrenman yapıp yarışmayı kazandım; bu başarı Allah’ın lütfudur.', YES, YES_A),
        ('Mert', 'Sınava hiç çalışmadım; düşük not almam tamamen kötü talihim yüzündendir.', KIR, '#fdeaea'),
        ('Selin', 'İlk denememde hata yaptım ama vazgeçmedim; planlı çalışarak hedefime ulaştım.', MAVI, MAVI_A),
        ('Duru', 'Yarışmada rakibimin hakkını çiğneyerek birinci oldum; gerçek başarı budur.', TUR, TUR_A),
    ]
    ic = ''
    for i, (isim, metin, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 62
        ic += f'<rect x="{x}" y="{y}" width="286" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 20, isim + ':', 11.5, renk, 'start')
        ic += yazi(x + 14, y + 36, metin[:46], 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 14, y + 49, metin[46:], 10.8, LAC, 'start', ince=True)
    return svg(600, 130, ic, 'Dört öğrencinin (Kaan, Mert, Selin, Duru) başarı ve kader konusundaki tutum kartları.', 24)


def bes_nimet_sema():
    veriler = [
        ('İhtiyarlık gelmeden', 'Gençlik', MAVI, MAVI_A),
        ('Hastalık gelmeden', 'Sağlık', YES, YES_A),
        ('Fakirlik gelmeden', '1 : ?', TUR, TUR_A),
        ('İşler sıkışmadan', '2 : ?', MOR, MOR_A),
        ('Ecel gelmeden', '3 : ?', ALTIN, '#fffbe6'),
    ]
    ic = yazi(300, 18, 'Hadis-i Şerif: “Beş şey gelmeden önce beş şeyin kıymetini biliniz.”', 11.5, KAHVE)
    for i, (ust, alt, renk, arka) in enumerate(veriler):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="28" width="110" height="78" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 55, 48, ust, 10.2, LAC, ince=True)
        ic += f'<line x1="{x + 14}" y1="58" x2="{x + 96}" y2="58" stroke="{renk}" stroke-width="1.2" stroke-dasharray="3 2"/>'
        ic += yazi(x + 55, 84, alt, 11.5, renk)
    return svg(600, 114, ic, 'Beş şeyin kıymetini bilme hadisi şeması: Gençlik, Sağlık ve 1, 2, 3 numaralı boşluklar.', 23)


def iki_yamac_sema():
    ic = f'<rect x="6" y="6" width="588" height="108" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Hz. Ömer’in Vadi Benzetmesi: “Bir Kaderden Başka Bir Kadere”', 12, KAHVE)
    # Sol: Verimli Yamaç
    ic += f'<rect x="20" y="34" width="256" height="68" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += f'<path d="M32 92 Q75 56 120 92 Z" fill="{YES}" opacity="0.35"/>'
    ic += yazi(148, 54, '1. Seçenek: Verimli Yamaç', 11.5, YESIL_K)
    ic += yazi(148, 72, 'Otu ve suyu bol alan', 11, LAC, ince=True)
    ic += yazi(148, 90, '→ Allah’ın kaderi içindedir', 11, YESIL_K)
    # Sağ: Kıraç Yamaç
    ic += f'<rect x="324" y="34" width="256" height="68" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += f'<path d="M336 92 Q379 56 424 92 Z" fill="{KAHVE}" opacity="0.3"/>'
    ic += yazi(452, 54, '2. Seçenek: Kıraç Yamaç', 11.5, TUR)
    ic += yazi(452, 72, 'Kurak ve verimsiz alan', 11, LAC, ince=True)
    ic += yazi(452, 90, '→ Allah’ın kaderi içindedir', 11, TUR)
    return svg(600, 120, ic, 'Hz. Ömer’in verimli yamaç ve kıraç yamaç benzetmesi: her iki seçim de Allah’ın kaderi içindedir.', 23)


def saglik_kalkan_kart():
    ic = f'<rect x="6" y="6" width="286" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'Hastalanmadan Önce Önlem', 12, MAVI)
    ic += yazi(22, 47, '• Helal ve temiz gıdalarla beslenmek (Bakara 168)', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 65, '• Elbiseyi ve çevreyi temiz tutmak (Müddessir 4–5)', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 83, '• Uyku düzeni, dinlenme ve harekete özen göstermek', 10.8, LAC, 'start', ince=True)
    ic += yazi(149, 102, 'Beden ve ruh sağlığını koruma görevi', 10.8, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="106" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'Hastalanınca Yapılacaklar', 12, YESIL_K)
    ic += yazi(324, 47, '• Doktora başvurup tedavi olmak', 10.8, LAC, 'start', ince=True)
    ic += yazi(324, 65, '• İlaçları ve iyileşme yollarını takip etmek', 10.8, LAC, 'start', ince=True)
    ic += yazi(324, 83, '• Şifayı Allah’tan isteyip dua etmek', 10.8, LAC, 'start', ince=True)
    ic += yazi(451, 102, 'Hadis: “Her hastalığın şifası yaratılmıştır.”', 10.8, YESIL_K)
    return svg(600, 118, ic, 'Sağlığı koruma önlemleri ve hastalanınca yapılacak görevler kartı.', 23)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kum_saati_sema()
    s[4]['gorsel'] = rizik_panosu()
    s[5]['gorsel'] = ayet_hadis_kartlari()
    s[6]['gorsel'] = hicret_tevekkul_sema()
    s[7]['gorsel'] = veba_olayi_zinciri()
    s[8]['gorsel'] = basari_tutum_kartlari()
    s[9]['gorsel'] = bes_nimet_sema()
    s[10]['gorsel'] = iki_yamac_sema()
    s[12]['gorsel'] = saglik_kalkan_kart()
