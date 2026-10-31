"""8. sınıf DKAB 7. hafta (Bir Ayet Tanıyorum: Ayetel Kürsi ve Anlamı; 1. Ünite Genel Değerlendirmesi) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="1.8"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def kunye_kart_sema():
    ic = f'<rect x="6" y="6" width="588" height="124" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Ayetel Kürsi Tanıtım Kartı (1–4 Numaralı Bilgiler)', 12, YESIL_K)
    satirlar = [
        ('1', 'Yer aldığı sure: Medine döneminde inen Bakara Suresi 255. ayettir.', MAVI, MAVI_A),
        ('2', 'Sure özelliği: Başına besmele çekilen beş ayetlik bağımsız suredir.', TUR, TUR_A),
        ('3', 'Adının kaynağı: İçinde geçen ve hükümranlık bildiren “kürsî” kelimesidir.', YES, '#fff'),
        ('4', 'Esmâ-i Hüsnâ: El-Hayy, El-Kayyûm, El-Aliyy ve El-Azîm isimleri geçer.', MOR, MOR_A),
    ]
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        x = 16 + (i % 2) * 286
        y = 34 + (i // 2) * 44
        ic += f'<rect x="{x}" y="{y}" width="276" height="38" rx="7" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += rozet(x + 18, y + 19, no, renk, 9, 10.8)
        ic += yazi(x + 34, y + 16, metin[:36], 10.5, LAC, 'start', ince=True)
        ic += yazi(x + 34, y + 31, metin[36:], 10.5, LAC, 'start', ince=True)
    return svg(600, 136, ic, 'Ayetel Kürsi tanıtım kartı: 1. Bakara 255. ayettir, 2. Beş ayetlik bağımsız suredir, 3. Kürsî kelimesi, 4. Dört güzel isim.', 14)


def esma_dortlu_sema():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Ayetel Kürsi’de Geçen Dört Güzel İsim (Esmâ-i Hüsnâ)', 12, KAHVE)
    kutular = [
        ('El-Hayy', 'Daima diri olan,', 'canlılara hayat veren', YES, YES_A),
        ('K : ?', 'Varlığı kendinden olup', 'evreni ayakta tutan', MAVI, MAVI_A),
        ('L : ?', 'İzzet ve hükümranlıkça', 'en yüce olan', TUR, TUR_A),
        ('El-Azîm', 'Zatının ve sıfatlarının', 'büyüklüğü sınırsız olan', MOR, MOR_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 14 + i * 144
        ic += f'<rect x="{x}" y="34" width="136" height="84" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 54, bas, 11.5, renk)
        ic += f'<line x1="{x + 14}" y1="62" x2="{x + 122}" y2="62" stroke="{renk}" stroke-width="1.2" stroke-dasharray="3 2"/>'
        ic += yazi(x + 68, 82, s1, 10.5, LAC, ince=True)
        ic += yazi(x + 68, 98, s2, 10.5, LAC, ince=True)
    return svg(600, 134, ic, 'Ayetel Kürsi’deki dört güzel isim şeması: El-Hayy, K kutusu, L kutusu ve El-Azîm.', 14)


def ayet_cumle_kartlari():
    kartlar = [
        ('1. Kart · Allâhü lâ ilâhe illâ Hû', '“Allah, kendisinden başka hiçbir', 'ilah olmayandır.”', MAVI, MAVI_A),
        ('2. Kart · Ya’lemü mâ beyne eydîhim...', '“O, kulların önlerindekileri ve', 'arkalarındakileri (her şeyi) bilir.”', YES, YES_A),
        ('3. Kart · İllâ bimâ şâe', '“Onlar O’nun ilminden, kendisinin', 'dilediği kadarından başkasını kavrayamaz.”', TUR, TUR_A),
        ('4. Kart · Ve lâ yeûdühû hıfzuhümâ', '“Gökleri ve yeri koruyup gözetmek', 'O’na güç (ağır) gelmez.”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 64
        ic += f'<rect x="{x}" y="{y}" width="286" height="56" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="56" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11, renk, 'start')
        ic += yazi(x + 18, y + 35, s1, 10.5, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 49, s2, 10.5, LAC, 'start', ince=True)
    return svg(600, 132, ic, 'Ayetel Kürsi’den dört bölüm kartı ve Türkçe mealleri.', 14)


def ilim_karsilastirma_sema():
    ic = f'<rect x="6" y="6" width="284" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(148, 25, 'Yüce Allah’ın İlmi (Mutlak İlim)', 11.5, MAVI)
    ic += yazi(22, 48, 'Ezelî, ebedî ve sınırsızdır.', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 66, 'Geçmişi, şimdiki anı ve geleceği kuşatır.', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 84, '“Ya’lemü mâ beyne eydîhim ve mâ halfehüm”', 10.5, MAVI, 'start')
    ic += yazi(148, 102, 'Hiçbir şey O’nun bilgisi dışında kalmaz', 10.5, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="284" height="106" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(452, 25, 'İnsanın Bilgisi (Cüz’î Bilgi)', 11.5, TUR)
    ic += yazi(326, 48, 'Sonradan kazanılır ve sınırlıdır.', 10.8, LAC, 'start', ince=True)
    ic += yazi(326, 66, 'Yalnız Allah’ın dilediği kadarı kavranabilir.', 10.8, LAC, 'start', ince=True)
    ic += yazi(326, 84, '“...bi-şey’in min ilmihî illâ bimâ şâe”', 10.2, TUR, 'start')
    ic += yazi(452, 102, 'Akıl ve araştırma ölçüsünde ulaşılır', 10.5, LAC, ince=True)
    return svg(600, 118, ic, 'Yüce Allah’ın sınırsız ilmi ile insanın sınırlı bilgisinin karşılaştırma şeması.', 14)


def okunus_akis_sema():
    adlar = [
        ('1. Bölüm', 'Tevhid · Hayy', MAVI, MAVI_A),
        ('2. Bölüm', 'Uyku Tutmaz ve Mülk', YES, YES_A),
        ('3. Bölüm', 'Şefaat İzni', TUR, TUR_A),
        ('4. Bölüm', 'İlim ve İrade', MOR, MOR_A),
        ('5. Bölüm', 'Kürsî ve Aliyy-Azîm', ALTIN, '#fffbe6'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += f'<rect x="{x}" y="10" width="104" height="68" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 52, 34, ust, 11, renk)
        ic += yazi(x + 52, 56, alt, 10.2, LAC, ince=True)
        if i < 4:
            ic += f'<line x1="{x + 105}" y1="44" x2="{x + 118}" y2="44" stroke="{LAC}" stroke-width="1.8"/>'
            ic += f'<path d="M{x + 114} 40 l4 4 l-4 4" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    return svg(600, 88, ic, 'Ayetel Kürsi’nin 5 bölümlük okunuş ve anlam akışı şeması.', 14)


def kader_baglanti_sema():
    ic = f'<rect x="6" y="6" width="588" height="118" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 24, '1. Ünite (Kader İnancı) ve Ayetel Kürsi İlişkisi Panosu', 12, MAVI)
    kutular = [
        ('El-Hayy', 'Biyolojik Yasalar:', 'Canlılara hayat verilmesi', YES, YES_A),
        ('El-Kayyûm', 'Fiziksel Yasalar:', 'Evrenin yönetilmesi', MAVI, MAVI_A),
        ('İlim ve İrade', 'Kader (Ölçü ve Plan):', 'Bilgi ve dilemeyle takdir', TUR, TUR_A),
        ('Kudret (Kürsî)', 'Kaza ve Koruma:', 'Yaratma ve gözetme gücü', MOR, MOR_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 14 + i * 144
        ic += f'<rect x="{x}" y="34" width="136" height="80" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 68, 52, bas, 11.2, renk)
        ic += yazi(x + 68, 72, s1, 10.5, LAC)
        ic += yazi(x + 68, 90, s2, 10.2, LAC, ince=True)
    return svg(600, 130, ic, '1. Ünite kader kavramları ile Ayetel Kürsi’deki El-Hayy, El-Kayyûm, İlim-İrade ve Kudret ilişki panosu.', 14)


def tenzih_kalkan_sema():
    ic = f'<rect x="6" y="8" width="218" height="92" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(115, 28, '1. Ayet İfadesi', 11.5, MAVI)
    ic += yazi(115, 50, '“O’nu ne bir uyuklama (sinetün)', 10.5, LAC, ince=True)
    ic += yazi(115, 66, 'tutar ne de bir uyku (nevm).”', 10.5, LAC, ince=True)
    ic += yazi(115, 86, '(Her an diri ve uyanık olma)', 10.5, MAVI)

    ic += f'<line x1="226" y1="54" x2="250" y2="54" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="252" y="20" width="96" height="68" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += yazi(300, 46, 'Ortak İlke', 11.5, KAHVE)
    ic += yazi(300, 68, '?', 12.5, TUR)
    ic += f'<line x1="350" y1="54" x2="374" y2="54" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="376" y="8" width="218" height="92" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(485, 28, '2. Ayet İfadesi', 11.5, YESIL_K)
    ic += yazi(485, 50, '“Gökleri ve yeri koruyup', 10.5, LAC, ince=True)
    ic += yazi(485, 66, 'gözetmek O’na ağır gelmez.”', 10.5, LAC, ince=True)
    ic += yazi(485, 86, '(Yorulma ve güçsüzlükten uzak)', 10.5, YESIL_K)
    return svg(600, 108, ic, 'Uyuklama/uyku tutmaması ve evreni korumanın ağır gelmemesi ifadelerinin ortak ilke şeması.', 14)


def sefaat_mulkiyet_sema():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Mutlak Mülkiyet Hükmü', 11.5, YESIL_K)
    ic += yazi(149, 46, '“Lehû mâ fi’s-semâvâti ve mâ fi’l-ard”', 10.8, YESIL_K)
    ic += yazi(149, 66, 'Göklerdeki her şey ve yerdeki', 10.5, LAC, ince=True)
    ic += yazi(149, 82, 'her şey yalnız Allah’ındır.', 10.5, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Şefaat İzni Hükmü', 11.5, MOR)
    ic += yazi(451, 46, '“Men ze’llezî yeşfeu indehû illâ bi-iznih”', 10.8, MOR)
    ic += yazi(451, 66, 'O’nun izni olmaksızın katında', 10.5, LAC, ince=True)
    ic += yazi(451, 82, 'şefaatte bulunacak kimdir?', 10.5, LAC, ince=True)
    return svg(600, 110, ic, 'Ayetel Kürsi’de mutlak mülkiyet ve şefaat izni hükümlerini gösteren şema.', 14)


def korunma_tavsiye_sema():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Günlük Yaşamda Ayetel Kürsi Okuma ve Tevekkül Bilinci', 12, KAHVE)
    ic += f'<rect x="20" y="34" width="268" height="64" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(154, 52, 'Okunması Tavsiye Edilen Vakitler', 11.2, MAVI)
    ic += yazi(154, 70, 'Farz namazların hemen ardından', 10.5, LAC, ince=True)
    ic += yazi(154, 86, 'Gece yatmadan ve evden çıkmadan önce', 10.5, LAC, ince=True)

    ic += f'<rect x="312" y="34" width="268" height="64" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(446, 52, 'Mümine Kazandırdığı Bilinç', 11.2, YESIL_K)
    ic += yazi(446, 70, 'Tedbir alıp El-Kayyûm olan Allah’a sığınmak', 10.5, LAC, ince=True)
    ic += yazi(446, 86, 'İlahi koruma altında huzur ve güven duymak', 10.5, LAC, ince=True)
    return svg(600, 116, ic, 'Ayetel Kürsi’nin okunduğu vakitler ve mümine kazandırdığı tevekkül bilinci şeması.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kunye_kart_sema()
    s[4]['gorsel'] = esma_dortlu_sema()
    s[5]['gorsel'] = ayet_cumle_kartlari()
    s[6]['gorsel'] = ilim_karsilastirma_sema()
    s[7]['gorsel'] = okunus_akis_sema()
    s[8]['gorsel'] = kader_baglanti_sema()
    s[9]['gorsel'] = tenzih_kalkan_sema()
    s[10]['gorsel'] = sefaat_mulkiyet_sema()
    s[12]['gorsel'] = korunma_tavsiye_sema()
