"""7. sınıf DKAB 7. hafta (Bir Sure Öğreniyorum: Nâs Suresi ve Anlamı) çalışma kâğıdı görselleri (SVG; insan figürü yok K024; yazı 10.5-13 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def nas_kunye_karti():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += f'<rect x="6" y="6" width="588" height="28" rx="10" fill="{YESIL_K}"/><rect x="6" y="22" width="588" height="12" fill="{YESIL_K}"/>'
    ic += yazi(300, 25, 'NÂS SURESİ KÜNYE KARTI', 12.5, '#fff')
    kutular = [
        ('Adının Anlamı', 'En-Nâs (İnsanlar)', YES, YES_A, 18),
        ('İndirildiği Dönem', 'K : ?', TUR, TUR_A, 212),
        ('Ayet ve Mushaf Sırası', 'L : ?', MAVI, MAVI_A, 406),
    ]
    for bas, deg, renk, arka, x in kutular:
        ic += f'<rect x="{x}" y="44" width="176" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 88, 66, bas, 11.5, renk)
        ic += f'<rect x="{x + 14}" y="78" width="148" height="28" rx="6" fill="#fff" stroke="{renk}" stroke-width="1.3"/>'
        ic += yazi(x + 88, 97, deg, 12, LAC)
    return svg(600, 134, ic, 'Nâs Suresi künye kartı: Adının anlamı En-Nâs (İnsanlar), İndirildiği dönem K, Ayet ve Mushaf sırası L.', 21)


def ilah_sifat_uclusu():
    kartlar = [
        ('I', 'Rabbü’n-nâs', 'İnsanları yaratan, koruyan', 've terbiye eden Rab', YES, YES_A),
        ('II', 'Melikü’n-nâs', 'İnsanlar üzerinde mutlak', 'hüküm ve mülk sahibi', MAVI, MAVI_A),
        ('III', 'İlâhü’n-nâs', 'Sûra üfleyerek kıyameti', 'başlatmakla görevli melek', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 198
        cx = x + 96
        ic += f'<rect x="{x}" y="6" width="192" height="118" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.7"/>'
        ic += rozet(x + 22, 24, no, renk, 10, 11)
        ic += yazi(cx + 8, 28, bas, 12, renk)
        ic += f'<line x1="{x + 14}" y1="40" x2="{x + 178}" y2="40" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(cx, 68, s1, 11, LAC, ince=True)
        ic += yazi(cx, 88, s2, 11, LAC, ince=True)
    return svg(600, 130, ic, 'Üç sıfat kartı: I Rabbü’n-nâs, II Melikü’n-nâs, III İlâhü’n-nâs.', 21)


def ayet_meal_panosu():
    kart = [
        ('1. Ayet', 'Kul eûzü birabbi’n-nâs.', 'De ki: İnsanların Rabbine sığınırım.', YES, YES_A),
        ('2. Ayet', 'Okunuşu: ?', 'İnsanların Melikine (hükümdarına),', MAVI, MAVI_A),
        ('4. Ayet', 'Min şerri’l-vesvâsi’l-hannâs.', 'Anlamı: ?', TUR, TUR_A),
        ('6. Ayet', 'Okunuşu: ?', 'Gerek cinlerden, gerekse insanlardan!', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 64
        ic += f'<rect x="{x}" y="{y}" width="286" height="58" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="58" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 35, s1, 11.5, LAC, 'start')
        ic += yazi(x + 18, y + 51, s2, 11, LAC, 'start', ince=True)
    return svg(600, 134, ic, 'Nâs Suresi 1, 2, 4 ve 6. ayetlerin okunuş ve anlam levhaları.', 21)


def muavvizeteyn_karsilastirma():
    ic = f'<rect x="6" y="6" width="588" height="120" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += yazi(300, 26, 'ORTAK AD: ? (İki Koruyucu Sure)', 12.5, KAHVE)
    ic += f'<rect x="18" y="38" width="270" height="76" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(153, 58, 'Felak Suresi (113. Sure)', 12, MAVI)
    ic += yazi(153, 78, 'Dış dünyadaki şerlerden ve hasetten', 11, LAC, ince=True)
    ic += yazi(153, 96, 'sabahın Rabbine sığınılır.', 11, LAC, ince=True)

    ic += f'<rect x="312" y="38" width="270" height="76" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(447, 58, 'Nâs Suresi (114. Sure)', 12, YESIL_K)
    ic += yazi(447, 78, 'Kalbe fısıldanan iç tehlikeden (?)', 11, LAC, ince=True)
    ic += yazi(447, 96, 'Rab, Melik ve İlah’a sığınılır.', 11, LAC, ince=True)
    return svg(600, 132, ic, 'Felak ve Nâs surelerinin ortak adı ve sığınılan tehlikelerin karşılaştırma şeması.', 21)


def sure_zinciri():
    adlar = [
        ('1. Ayet', 'Birabbi’n-nâs', YES, YES_A),
        ('2. Ayet', 'Meliki’n-nâs', MAVI, MAVI_A),
        ('3. Ayet', 'İlâhi’n-nâs', MOR, MOR_A),
        ('4. Ayet', 'Vesvâsi’l-hannâs', TUR, TUR_A),
        ('5. Ayet', 'Fî sudûri’n-nâs', ALTIN, '#fffbe6'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="12" width="106" height="68" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 53, 36, ust, 10.8, renk)
        ic += yazi(x + 53, 58, alt, 9.8, LAC)
        if i < 4:
            ic += f'<line x1="{x + 108}" y1="46" x2="{x + 116}" y2="46" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 90, ic, 'Nâs Suresi ilk beş ayetinin Mushaf sıralama zinciri.', 20)


def hannas_kalkan_sema():
    ic = f'<rect x="6" y="6" width="276" height="114" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.7"/>'
    ic += yazi(144, 26, '1. Durum: Vesvese Fısıltısı', 12, TUR)
    ic += yazi(144, 52, 'El-Vesvâs: Kalbe (sudûr) şüphe,', 11, LAC, ince=True)
    ic += yazi(144, 70, 'kuruntu ve kötülük telkin eder.', 11, LAC, ince=True)
    ic += yazi(144, 96, 'Hedef: İnsanı yanıltmak', 11.5, KIR)

    ic += f'<line x1="286" y1="63" x2="314" y2="63" stroke="{LAC}" stroke-width="2.2"/><path d="M309 58 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="318" y="6" width="276" height="114" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.7"/>'
    ic += yazi(456, 26, '2. Durum: Allah’a Sığınma (İstiâze)', 12, YESIL_K)
    ic += yazi(456, 52, 'Kul Eûzü-Besmele çekip Nâs', 11, LAC, ince=True)
    ic += yazi(456, 70, 'Suresi’ni okuyarak Allah’ı anar.', 11, LAC, ince=True)
    ic += yazi(456, 96, 'Sonuç: Hannâs sinip geri çekilir!', 11.5, YESIL_K)
    return svg(600, 126, ic, 'Vesvese fısıltısı ve Allah anıldığında hannâsın sinip geri çekilmesi şeması.', 21)


def altinci_ayet_kaynak():
    ic = f'<rect x="150" y="6" width="300" height="34" rx="8" fill="{LAC}"/>'
    ic += yazi(300, 28, '6. Ayet: “Mine’l-cinneti ve’n-nâs”', 12, '#fff')
    ic += f'<line x1="230" y1="40" x2="150" y2="54" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="370" y1="40" x2="450" y2="54" stroke="{LAC}" stroke-width="1.8"/>'

    ic += f'<rect x="12" y="54" width="276" height="68" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(150, 76, '1. Kaynak: Cinlerden (Mine’l-cinneti)', 11.5, MOR)
    ic += yazi(150, 98, 'Görünmeyen şeytanın kalbe verdiği kuruntu', 11, LAC, ince=True)

    ic += f'<rect x="312" y="54" width="276" height="68" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(450, 76, '2. Kaynak: İnsanlardan (Ve’n-nâs)', 11.5, TUR)
    ic += yazi(450, 98, 'Kötülüğe çağıran yanlış çevre ve telkinler', 11, LAC, ince=True)
    return svg(600, 128, ic, '6. ayet Mine’l-cinneti ve’n-nâs: cinlerden ve insanlardan gelen vesvese kaynakları.', 21)


def irade_tercih_karti():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<rect x="6" y="6" width="10" height="104" rx="4" fill="{MAVI}"/>'
    ic += yazi(28, 28, 'İLKE: Şeytanın İnsanı Zorlama Gücü Yoktur!', 12, MAVI, 'start')
    ic += yazi(28, 50, 'Şeytan yalnız vesvese verir ve kötülüğü süslü gösterir; kimseyi zorlayamaz.', 11, LAC, 'start', ince=True)
    ic += f'<rect x="28" y="64" width="256" height="32" rx="6" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(156, 85, '1. Akıl ve İrade ile Reddet', 11.5, YESIL_K)
    ic += f'<rect x="308" y="64" width="268" height="32" rx="6" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(442, 85, '2. Eûzü-Besmele ile Allah’a Sığın', 11.5, MAVI)
    return svg(600, 116, ic, 'Şeytanın zorlama gücü olmadığı, akıl-irade ve Eûzü-Besmele ile korunulduğu bilgi levhası.', 20)


def arkadas_secimi_karti():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{TUR_A}" stroke="{KIR}" stroke-width="1.7"/>'
    ic += yazi(149, 26, '1. Kart · Yanlış Telkin', 12, KIR)
    ic += yazi(149, 50, 'Yalana, haksızlığa ve zararlı', 11, LAC, ince=True)
    ic += yazi(149, 68, 'alışkanlıklara teşvik eden sözler', 11, LAC, ince=True)
    ic += yazi(149, 88, 'Tutum: Uzak dur ve Allah’a sığın', 11, KIR)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.7"/>'
    ic += yazi(451, 26, '2. Kart · Doğru Arkadaşlık', 12, YESIL_K)
    ic += yazi(451, 50, 'Dürüstlüğe, iyiliğe ve güzel', 11, LAC, ince=True)
    ic += yazi(451, 68, 'ahlaka yönlendiren güvenilir çevre', 11, LAC, ince=True)
    ic += yazi(451, 88, 'Tutum: Doğru sözlü dostlar seç', 11, YESIL_K)
    return svg(600, 110, ic, 'Yanlış telkin ve doğru arkadaşlık karşılaştırma kartları.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = nas_kunye_karti()
    s[4]['gorsel'] = ilah_sifat_uclusu()
    s[5]['gorsel'] = ayet_meal_panosu()
    s[6]['gorsel'] = muavvizeteyn_karsilastirma()
    s[7]['gorsel'] = sure_zinciri()
    s[8]['gorsel'] = hannas_kalkan_sema()
    s[9]['gorsel'] = altinci_ayet_kaynak()
    s[10]['gorsel'] = irade_tercih_karti()
    s[12]['gorsel'] = arkadas_secimi_karti()
