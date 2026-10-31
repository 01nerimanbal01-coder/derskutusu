"""5. sınıf Sosyal Bilgiler 3. hafta (Kültürel Özelliklere Saygı ve Birlikte Yaşama Kültürü — 6 kültür başlığı, Türkiye-KKTC ortak özellikler, kültürlerin buluşması, selamlaşma, aşure benzetmesi) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

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


def rozet(x, y, metin, renk, r=10.5, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="1.8"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def kulturel_tanitim_kartlari():
    kutular = [
        ('K Grubu', 'Ebru uygulaması', 'Lefkara nakışı', 'Halı dokumacılığı', MAVI, MAVI_A),
        ('L Grubu', 'Balalayka ve ud', 'Kaval ve gadulka', 'Türkmen sazı', TUR, TUR_A),
        ('M Grubu', 'Surva Festivali', 'Maslenitsa Bayramı', 'Halı Bayramı', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, s3, renk, arka) in enumerate(kutular):
        x = 8 + i * 200
        ic += f'<rect x="{x}" y="8" width="184" height="98" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="8" width="184" height="24" rx="10" fill="{renk}"/><rect x="{x}" y="22" width="184" height="10" fill="{renk}"/>'
        ic += yazi(x + 92, 25, bas + ' : ?', 11.5, '#fff')
        ic += yazi(x + 16, 50, s1, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 16, 68, s2, 10.8, LAC, 'start', ince=True)
        ic += yazi(x + 16, 86, s3, 10.8, LAC, 'start', ince=True)
    return svg(600, 114, ic, '23 Nisan kültür tanıtım grupları: K grubu (ebru, lefkara nakışı, halı dokumacılığı), L grubu (balalayka, gadulka, Türkmen sazı), M grubu (Surva Festivali, Maslenitsa, Halı Bayramı).', 23)


def turkiye_kktc_ortak_pano():
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, 'Türkiye ve KKTC Ortak Kültür ve Tarih Panosu', 11.5, KIR)
    kartlar = [
        ('Tarih ve Bayrak', '1571 Osmanlı fethi · 1983 KKTC', 'Şeritler: Türkiye ve KKTC', KIR, '#fdeaea'),
        ('Ortak Mutfak ve İkram', 'Enginar dolması, humus, tarhana,', 'hellim; su ve macunlu kahve', TUR, TUR_A),
        ('Halk Oyunu ve Giyim', 'Daire biçiminde zeybek oyunu;', 'Trablusgarp’tan Tarabulus kuşağı', MAVI, MAVI_A),
        ('Ortak El Sanatları', 'Zembil, ahşap baskı, ebru ve', 'el dokuması kilim geleneği', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 16 + (i % 2) * 288
        y = 32 + (i // 2) * 42
        ic += f'<rect x="{x}" y="{y}" width="276" height="36" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 10, y + 14, bas + ':', 10.8, renk, 'start')
        ic += yazi(x + 10, y + 29, s1 + ' | ' + s2, 10, LAC, 'start', ince=True)
    return svg(600, 126, ic, 'Türkiye ve KKTC ortak kültür panosu: tarih ve bayrak, ortak mutfak ve kahve ikramı, zeybek ve Tarabulus kuşağı, ortak el sanatları.', 24)


def karsilasma_durumlari_sema():
    kartlar = [
        ('1. Kart · Kuşadası', 'Hollandalı Jan Linskens’in', 'dalış ve tatil için gelmesi', MAVI, MAVI_A),
        ('2. Kart · Rize', 'Ganalı Yahaya Abdulai’nin', 'tıp eğitimi ve horon öğrenmesi', TUR, TUR_A),
        ('3. Kart · Almanya', '1961–1973’te Türk işçilerin', 'gidişi ve dönerin yayılması', YES, YES_A),
        ('4. Kart · Ankara', 'Kızılay iftarında Şakiriye ve', 'tavuk baget paylaşımı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 12}" y1="34" x2="{x + 124}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.3, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Kültürlerin bir araya geldiği dört durum kartı: Kuşadası tatili, Rize tıp eğitimi, Almanya iş göçü, Ankara Kızılay dostluk sofrası.', 22)


def selamlasma_dunyasi_svg():
    ulkeler = [
        ('Türk ve Japon (Ortak)', 'Başı hafifçe öne eğerek', 'saygıyla selamlaşma', YES, YES_A),
        ('Filipinler Geleneği', 'Büyüklerin elini alıp', 'alına götürerek selamlama', MAVI, MAVI_A),
        ('Yunanistan ve Fransa', 'Sırta/omza dokunma veya', 'yanaktan öperek selamlama', TUR, TUR_A),
        ('Yeni Zelanda (Maori)', 'Burun ve alınları birbirine', 'bastırarak selamlaşma', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(ulkeler):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 10.8, renk)
        ic += f'<line x1="{x + 12}" y1="34" x2="{x + 124}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.3, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Farklı toplumlarda selamlaşma biçimleri: Türk-Japon ortak baş eğme, Filipinler, Yunanistan-Fransa ve Yeni Zelanda Maori selamlaşması.', 22)


def stefan_uyum_sureci():
    adimlar = [
        ('Avusturya → Ankara', 'Yeni ülkeye taşınma', MAVI, MAVI_A),
        ('Dil Güçlüğü', 'İletişimde zorlanma', TUR, TUR_A),
        ('Babanın Öğüdü', 'Paylaşma ve saygı', MOR, MOR_A),
        ('Uyum ve Kaynaşma', 'Türkçe ve kültür öğrenme', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="78" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11, renk)
        ic += yazi(x + 68, 60, alt, 10.5, LAC, ince=True)
    return svg(600, 94, ic, 'Stefan’ın Ankara’daki uyum süreci basamakları: taşınma, dil güçlüğü, babanın öğüdü, Türkçe öğrenip kaynaşma.', 22)


def asure_kazani_sema():
    ic = f'<rect x="6" y="6" width="588" height="106" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    # Sol: Aşure kâsesi çizimi (insan figürü yok)
    ic += f'<path d="M36 52 H144 A54 42 0 0 1 36 52 Z" fill="{TUR_A}" stroke="{KAHVE}" stroke-width="2"/>'
    ic += f'<ellipse cx="90" cy="52" rx="54" ry="10" fill="#f7d794" stroke="{KAHVE}" stroke-width="1.6"/>'
    for cx, cy, renk in [(64, 51, KIR), (80, 54, KAHVE), (98, 50, YES), (114, 53, MOR), (90, 48, TUR)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{renk}"/>'
    ic += yazi(90, 102, 'Aşure Kâsesi', 10.8, KAHVE)
    # Sağ: Benzetme şeması
    ic += f'<rect x="176" y="16" width="190" height="84" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(271, 35, 'Aşurenin Özelliği', 11.2, TUR)
    ic += yazi(271, 56, 'Farklı malzemeler aynı', 10.5, LAC, ince=True)
    ic += yazi(271, 72, 'kazanda kaynar; kendi tadını', 10.5, LAC, ince=True)
    ic += yazi(271, 88, 'koruyup ortak lezzet sunar.', 10.5, LAC, ince=True)

    ic += f'<line x1="372" y1="58" x2="394" y2="58" stroke="{LAC}" stroke-width="2"/><path d="M389 53 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="400" y="16" width="182" height="84" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(491, 35, 'Kültürlerin Uyumu', 11.2, YESIL_K)
    ic += yazi(491, 56, 'Farklı milletler saygıyla', 10.5, LAC, ince=True)
    ic += yazi(491, 72, 'bir arada yaşar; birlik ve', 10.5, LAC, ince=True)
    ic += yazi(491, 88, 'beraberliği güçlendirir.', 10.5, LAC, ince=True)
    return svg(600, 118, ic, 'Aşure benzetmesi şeması: farklı malzemelerin ortak bir tat oluşturması ile farklı kültürlerin saygıyla bir arada yaşaması.', 23)


def ulke_tanitim_tablosu():
    satirlar = [
        ('1. Satır', 'Bulgaristan', 'Kukeri kostümü', 'Marteniçka bilekliği', MAVI, MAVI_A),
        ('2. Satır', 'Türkmenistan', 'Telpek başlığı', 'Halı Bayramı', YES, YES_A),
        ('3. Satır', 'Rusya', 'Sarafan elbisesi', 'Maslenitsa Bayramı', TUR, TUR_A),
        ('4. Satır', 'KKTC', 'Kokoşnik başlığı', 'Surva Festivali', MOR, MOR_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    for i, (no, ulke, giyim, kut, renk, arka) in enumerate(satirlar):
        y = 14 + i * 25
        ic += f'<rect x="16" y="{y}" width="568" height="21" rx="5" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(58, y + 15, no, 10.5, renk)
        ic += yazi(165, y + 15, ulke, 10.8, LAC)
        ic += yazi(330, y + 15, giyim, 10.5, LAC, ince=True)
        ic += yazi(495, y + 15, kut, 10.5, LAC, ince=True)
    return svg(600, 126, ic, 'Dört satırlık ülke kültür eşleştirme tablosu: Bulgaristan, Türkmenistan, Rusya ve KKTC.', 24)


def spor_ve_goc_kartlari():
    ic = f'<rect x="8" y="8" width="282" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'İspanya’daki Genç Futbolcumuz', 11.2, MAVI)
    ic += yazi(22, 48, 'Spor, farklı ülkelerden insanları kaynaştırır.', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 66, 'Saygı, nezaket ve anlayışı geliştirir.', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 84, 'Ön yargıları kırıp iki kültürü temsil ettirir.', 10.5, LAC, 'start', ince=True)

    ic += f'<rect x="310" y="8" width="282" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Mersin’e Yerleşen Koreli Jae Ailesi', 11.2, YESIL_K)
    ic += yazi(324, 48, 'Doğal güzellikler ile ilgi ve sevgi etkili oldu.', 10.5, LAC, 'start', ince=True)
    ic += yazi(324, 66, 'Büyüklere saygı ve dayanışma ortaktır.', 10.5, LAC, 'start', ince=True)
    ic += yazi(324, 84, 'Farklılıklarla kabul edilmek uyumu sağladı.', 10.5, LAC, 'start', ince=True)
    return svg(600, 112, ic, 'İspanya’daki genç futbolcumuz ve Mersin’e yerleşen Güney Koreli Jae ailesinin kültürel uyum kartları.', 22)


def misafirperverlik_kalkan_svg():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Türk Misafirperverliği ve Uyum Süreci', 11.5, TUR)
    kutular = [
        ('Ayrım Gözetmeme', 'Dil, din ve ten rengine', 'bakmadan saygı ve sevgi', MAVI, MAVI_A),
        ('Geçici Koruma ve Destek', 'Sığınmacılara imkân paylaşımı', 've uyum projeleri', YES, YES_A),
        ('Toplumsal Sonuç', 'Ön yargılar kalkar, huzurlu', 'birlikte yaşama oluşur', MOR, MOR_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="34" width="182" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 91, 51, bas, 11, renk)
        ic += yazi(x + 91, 68, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 91, 83, s2, 10.2, LAC, ince=True)
    return svg(600, 110, ic, 'Türk misafirperverliği şeması: ayrım gözetmeme, geçici koruma ve uyum projeleri, huzurlu birlikte yaşama sonucu.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kulturel_tanitim_kartlari()
    s[4]['gorsel'] = turkiye_kktc_ortak_pano()
    s[5]['gorsel'] = karsilasma_durumlari_sema()
    s[6]['gorsel'] = selamlasma_dunyasi_svg()
    s[7]['gorsel'] = stefan_uyum_sureci()
    s[8]['gorsel'] = asure_kazani_sema()
    s[9]['gorsel'] = ulke_tanitim_tablosu()
    s[10]['gorsel'] = spor_ve_goc_kartlari()
    s[12]['gorsel'] = misafirperverlik_kalkan_svg()
