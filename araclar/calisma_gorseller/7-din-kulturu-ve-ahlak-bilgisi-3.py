"""7. sınıf DKAB 3. hafta (Dünya ve Ahiret Hayatı: Ahiretin Anlamı, Ölüm ve Kıyamet) çalışma kâğıdı görselleri.
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


def omur_ecel_berzah_seridi():
    ic = f'<rect x="6" y="6" width="588" height="94" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Dünya Yaşam Süreci ve Ahiret Hayatına İlk Geçiş Şeridi', 11.4, LAC)
    ic += f'<circle cx="34" cy="60" r="10" fill="{YES}"/>' + yazi(34, 86, 'Doğum', 10.5, YESIL_K)
    ic += f'<line x1="46" y1="60" x2="64" y2="60" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="68" y="38" width="186" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(161, 56, 'K = ?', 11.2, MAVI)
    ic += yazi(161, 73, '(Doğumdan ölüme yaşam süresi)', 10.0, LAC, ince=True)

    ic += f'<line x1="256" y1="60" x2="274" y2="60" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="278" y="38" width="118" height="44" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(337, 56, 'L = ?', 11.2, TUR)
    ic += yazi(337, 73, '(Ölüm vakti)', 10.0, LAC, ince=True)

    ic += f'<line x1="398" y1="60" x2="416" y2="60" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="420" y="38" width="160" height="44" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(500, 56, 'M = ?', 11.2, MOR)
    ic += yazi(500, 73, '(Kabirdeki ilk basamak)', 10.0, LAC, ince=True)
    return svg(600, 106, ic, 'Zaman şeridi: Doğum, K yaşam süresi, L ölüm vakti ve M kabirdeki ilk basamak.', 19)


def olum_kiyamet_panosu():
    satirlar = [
        ('1. Satır (Sona eren)', 'Ölüm: Bireyin dünya hayatı', 'Kıyamet: Dünya ve kâinat düzeni', MAVI, MAVI_A),
        ('2. Satır (Sebebi)', 'Ölüm: Ecel vaktinin gelmesi', 'Kıyamet: İsrafil’in sûra üflemesi', YES, YES_A),
        ('3. Satır (Zaman bilgisi)', 'Ölüm: Ecel vakti Allah katındadır', 'Kıyamet: Vaktini insanlar hesaplar', KIR, '#fdeaea'),
        ('4. Satır (Ardından gelen)', 'Ölüm: Berzah (kabir) hayatı', 'Kıyamet: Sonsuz ahiret aşamaları', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 10.8, renk, 'start')
        ic += yazi(x + 18, y + 33, s1, 10.1, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 45, s2, 10.1, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Ölüm ve kıyamet karşılaştırma panosu: 1. Sona eren, 2. Sebebi, 3. Zaman bilgisi (hatalı), 4. Ardından gelen.', 20)


def dort_kaynak_karti():
    kartlar = [
        ('1. Kart · Mülk 2', '“Hanginizin daha iyi iş', 'yapacağını sınamak için...”', MAVI, MAVI_A),
        ('2. Kart · Al-i İmran 185', '“Her canlı ölümü tadar...', 'Karşılığınız tam verilir.”', TUR, TUR_A),
        ('3. Kart · Buhari Hadisi', '“İnsan hayal kurarken', 'ecel çizgisi önüne çıkar.”', MOR, MOR_A),
        ('4. Kart · Lokman 34', '“Kıyamet vaktinin bilgisi', 'yalnız Allah katındadır.”', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 10.2, renk)
        ic += f'<line x1="{x + 12}" y1="33" x2="{x + 124}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, s1, 9.6, LAC, ince=True)
        ic += yazi(x + 68, 70, s2, 9.6, LAC, ince=True)
    return svg(600, 102, ic, 'Dört ayet ve hadis kartı: 1. Mülk 2, 2. Al-i İmran 185, 3. Buhari Çizgilerin hadisi, 4. Lokman 34.', 19)


def kavram_asama_ayrimi():
    ic = f'<rect x="8" y="8" width="260" height="88" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(138, 26, 'K Grubu (Dünya Süresi Kavramları)', 11.0, TUR)
    ic += yazi(138, 50, 'Ömür ve Ecel kavramları', 10.6, LAC)
    ic += yazi(138, 72, '(Ahiret aşamaları arasında sayılmaz)', 10.2, LAC, ince=True)

    ic += f'<rect x="284" y="8" width="308" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(438, 26, 'Ahiret Yolunun Aşamaları (Durakları)', 11.0, MAVI)
    ic += yazi(438, 50, 'Ölüm (Berzah) → Kıyamet → Baas', 10.5, LAC)
    ic += yazi(438, 72, 'Mahşer → Mizan → Cennet / Cehennem', 10.5, LAC)
    return svg(600, 104, ic, 'Ahiretle ilgili kavramların K grubu (ömür ve ecel) ile ahiret yolunun aşamaları olarak ayrımı.', 19)


def ahiret_duraklari_zinciri():
    duraklar = [
        ('1. Durak', 'Ölüm ve Berzah', MAVI, MAVI_A),
        ('2. Durak', 'Kıyamet Kopuşu', TUR, TUR_A),
        ('3. Durak', 'Baas ve Mahşer', MOR, MOR_A),
        ('4. Durak', 'Defter ve Mizan', ALTIN, '#fffbe6'),
        ('5. Durak', 'Cennet / Cehennem', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(duraklar):
        x = 8 + i * 118
        ic += f'<rect x="{x}" y="10" width="102" height="76" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 51, 35, ust, 11.0, renk)
        ic += yazi(x + 51, 60, alt, 10.1, LAC, ince=True)
        if i < 4:
            ic += f'<line x1="{x + 111}" y1="48" x2="{x + 117}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Ahiret yolculuğunun beş durağı: 1. Ölüm ve Berzah, 2. Kıyamet, 3. Baas ve Mahşer, 4. Defter ve Mizan, 5. Cennet ya da Cehennem.', 18)


def cizgilerin_hadisi_sema():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Hz. Peygamber’in Çizgilerle Anlattığı Hadis Şeması (Buhari, “Rikâk”, 4)', 11.2, KAHVE)
    ic += f'<rect x="28" y="42" width="120" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(88, 68, 'İnsan Yaşamı', 10.8, MAVI)
    # Uzun istek ve arzu çizgileri (kesikli, ecel çizgisini aşan)
    ic += f'<line x1="152" y1="52" x2="424" y2="52" stroke="{MAVI}" stroke-width="2" stroke-dasharray="6 4"/>'
    ic += f'<line x1="152" y1="76" x2="424" y2="76" stroke="{MAVI}" stroke-width="2" stroke-dasharray="6 4"/>'
    ic += yazi(506, 60, 'İstek ve Arzular', 10.3, MAVI)
    ic += yazi(506, 76, '(Uzak Hedefler)', 9.8, MAVI, ince=True)
    # Yakındaki ecel çizgisi (dikey kesen)
    ic += f'<line x1="286" y1="36" x2="286" y2="92" stroke="{KIR}" stroke-width="3"/>'
    ic += f'<rect x="232" y="34" width="108" height="20" rx="5" fill="#fdeaea" stroke="{KIR}" stroke-width="1.2"/>'
    ic += yazi(286, 48, 'Ecel Çizgisi', 10.5, KIR)
    return svg(600, 108, ic, 'Çizgilerin hadisi şeması: insanın uzun istek ve arzu çizgileri ile daha yakında onları kesen ecel çizgisi.', 19)


def infitar_sahneleri_sema():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'İnfitar Suresi 1–5. Ayetlerde Bildirilen Kıyamet Olayları ve Sonucu', 11.3, LAC)
    kutular = [
        ('Gökyüzü ve Yıldızlar', 'Gökyüzü yarılır, yıldızlar', 'dağılıp etrafa saçılır.', MAVI, MAVI_A),
        ('Denizler ve Kabirler', 'Denizler taşar, kabirlerin', 'altı üstüne getirilir.', TUR, TUR_A),
        ('İnsanın Durumu', 'Her insan dünyada neleri yapıp', 'yapmadığını açıkça anlar.', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.8, renk)
        ic += yazi(x + 90, 67, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 90, 82, s2, 10.1, LAC, ince=True)
    return svg(600, 110, ic, 'İnfitar suresi 1-5. ayetler şeması: gökyüzü ve yıldızlar, denizler ve kabirler, insanın yaptıklarını anlaması.', 19)


def ahiret_bilgi_kaynaklari():
    ic = f'<rect x="8" y="6" width="584" height="94" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 25, 'Ahiret Hayatına İlişkin Doğru Bilginin İki Temel Kaynağı', 11.3, MAVI)
    ic += f'<rect x="24" y="36" width="264" height="54" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(156, 54, '1. Kur’an-ı Kerim Ayetleri', 10.8, MAVI)
    ic += yazi(156, 74, 'Allah’ın indirdiği vahiylerle ahireti tanıtır.', 10.1, LAC, ince=True)

    ic += f'<rect x="312" y="36" width="264" height="54" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(444, 54, '2. Hz. Peygamber’in Hadisleri', 10.8, YESIL_K)
    ic += yazi(444, 74, 'Peygamberimiz ahiret aşamalarını açıklar.', 10.1, LAC, ince=True)
    return svg(600, 106, ic, 'Ahiret bilgisinin iki temel kaynağı: Kur’an-ı Kerim ayetleri ve Hz. Peygamber’in hadisleri.', 19)


def dunya_amaci_gorus_karti():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Görüş Kartı', 11.2, KIR)
    ic += yazi(149, 50, '“Dünya hayatı amaçsızdır; insanın', 10.5, LAC, ince=True)
    ic += yazi(149, 68, 'davranışlarından hesaba çekileceği', 10.5, LAC, ince=True)
    ic += yazi(149, 84, 'ikinci bir hayat bulunmaz.”', 10.5, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Görüş Kartı', 11.2, YESIL_K)
    ic += yazi(451, 50, '“İnsan amaçsız yaratılmamıştır; dünya', 10.5, LAC, ince=True)
    ic += yazi(451, 68, 'hayatı kimin daha iyi davranacağının', 10.5, LAC, ince=True)
    ic += yazi(451, 84, 'denendiği bir imtihan süresidir.”', 10.5, LAC, ince=True)
    return svg(600, 104, ic, 'Dünya hayatının amacı hakkında iki görüş kartı.', 19)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = omur_ecel_berzah_seridi()
    s[4]['gorsel'] = olum_kiyamet_panosu()
    s[5]['gorsel'] = dort_kaynak_karti()
    s[6]['gorsel'] = kavram_asama_ayrimi()
    s[7]['gorsel'] = ahiret_duraklari_zinciri()
    s[8]['gorsel'] = cizgilerin_hadisi_sema()
    s[9]['gorsel'] = infitar_sahneleri_sema()
    s[10]['gorsel'] = ahiret_bilgi_kaynaklari()
    s[12]['gorsel'] = dunya_amaci_gorus_karti()
