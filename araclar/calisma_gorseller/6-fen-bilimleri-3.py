"""6. sınıf Fen Bilimleri 3. hafta (Güneş ve Ay Tutulmaları — bilgi toplama, model ve kayıt diyagramı, rol canlandırma, model düzeltme, bilim insanları) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

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


def fener_ciz(x, y):
    return (f'<rect x="{x}" y="{y - 8}" width="26" height="16" rx="3" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
            f'<rect x="{x + 26}" y="{y - 11}" width="6" height="22" rx="2" fill="{TUR}"/>')


def tutulma_duzenek_karsilastirma():
    ic = f'<rect x="8" y="8" width="282" height="98" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'K Düzeneği (Gölge Büyük Topta)', 11.2, TUR)
    ic += fener_ciz(22, 58)
    ic += f'<polygon points="118,49 216,40 216,76 118,67" fill="{LAC}" opacity=".18"/>'
    ic += f'<circle cx="118" cy="58" r="9" fill="{GRI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<circle cx="226" cy="58" r="20" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<circle cx="212" cy="58" r="9" fill="{LAC}" opacity=".45"/>'
    ic += yazi(36, 92, 'Fener', 10.2, LAC, ince=True)
    ic += yazi(118, 92, 'Küçük top', 10.2, LAC)
    ic += yazi(226, 92, 'Büyük top', 10.2, MAVI)

    ic += f'<rect x="310" y="8" width="282" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'L Düzeneği (Küçük Top Gölgede)', 11.2, MAVI)
    ic += fener_ciz(324, 58)
    ic += f'<polygon points="424,38 548,34 548,82 424,78" fill="{LAC}" opacity=".18"/>'
    ic += f'<circle cx="424" cy="58" r="20" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<circle cx="532" cy="58" r="9" fill="{GRI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<circle cx="532" cy="58" r="9" fill="{LAC}" opacity=".45"/>'
    ic += yazi(338, 92, 'Fener', 10.2, LAC, ince=True)
    ic += yazi(424, 92, 'Büyük top', 10.2, MAVI)
    ic += yazi(532, 92, 'Küçük top', 10.2, LAC)
    return svg(600, 114, ic, 'K düzeneğinde fener, küçük top, büyük top; L düzeneğinde fener, büyük top, küçük top.', 23)


def model_kontrol_hatalari():
    kartlar = [
        ('1. Grup (Güneş Tutulması)', 'Sıra: Fener — Ay (küçük) — Dünya (büyük)', 'Not: Model hatasız kurulmuştur.', YES, YES_A),
        ('2. Grup (Ay Tutulması)', 'Sıra: Fener — Dünya — Ay (hizadan yukarıda)', 'Not: Hizalama düzeltilmelidir.', MAVI, MAVI_A),
        ('3. Grup (Ay Tutulması)', 'Sıra: Fener — Dünya (8 cm) — Ay (16 cm)', 'Not: Modelde büyüklük hatası yoktur.', KIR, '#fdeaea'),
        ('4. Grup (Güneş Tutulması)', 'Sıra: Fener — Dünya (büyük) — Ay (küçük)', 'Not: Ortadaki top yanlış seçilmiştir.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 16, y + 19, f'{bas}: {s1}', 10.1, LAC, 'start')
        ic += yazi(x + 16, y + 38, s2, 10.3, renk, 'start', ince=True)
    return svg(600, 124, ic, 'Dört grubun tutulma modeli ve kontrol notları: 3. grupta Dünya topu Ay’dan küçük olduğu hâlde hatasız denmiştir.', 23)


def ay_tutulmasi_kayit_diyagrami():
    ic = f'<rect x="130" y="6" width="340" height="28" rx="14" fill="{MAVI}"/>'
    ic += yazi(300, 24, 'Merkez Soru: Ay tutulması nasıl gerçekleşir?', 11.2, '#fff')
    bolumler = [
        ('1. Önceden bilinenler', 'Ay’ın dolanma hareketi', MAVI, MAVI_A),
        ('2. Malzemeler', 'Seçilen üç model aracı : ?', TUR, TUR_A),
        ('3. Konumlanma sırası', 'Aynı hizadaki diziliş : ?', MOR, MOR_A),
        ('4. Öğrenilenler', 'Gölgenin düştüğü top : ?', YES, YES_A),
    ]
    for i, (bas, alt, renk, arka) in enumerate(bolumler):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="42" width="136" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 62, bas, 10.8, renk)
        ic += yazi(x + 68, 84, alt, 10.2, LAC, ince=True)
    return svg(600, 110, ic, 'Ay tutulması kayıt diyagramı: merkez soru ve dört bölüm (önceden bilinenler, malzemeler, konumlanma sırası, öğrenilenler).', 22)


def rol_canlandirma_sahnesi():
    kartlar = [
        ('1. Maske: Güneş', 'Güneş tutulması: İlk sırada', 'Ay tutulması: İlk sırada', TUR, TUR_A),
        ('2. Maske: K Gök Cismi', 'Güneş tutulması: Ortada durur', 'Ay tutulması: Son sırada durur', MOR, MOR_A),
        ('3. Maske: L Gök Cismi', 'Güneş tutulması: Son sırada durur', 'Ay tutulması: Ortada durur', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 12 + i * 194
        ic += f'<rect x="{x}" y="8" width="184" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 92, 27, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="35" x2="{x + 170}" y2="35" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 92, 56, s1, 10.3, LAC, ince=True)
        ic += yazi(x + 92, 76, s2, 10.3, LAC, ince=True)
    return svg(600, 104, ic, 'Rol canlandırma etkinliği üç maske kartı: Güneş, K gök cismi ve L gök cismi.', 22)


def arastirma_rapor_sureci_sema():
    adimlar = [
        ('Bilgi Toplama', 'Dijital, yazılı ve görsel', MAVI, MAVI_A),
        ('Fikir Alışverişi', 'Soruları ve veriyi tartış', MOR, MOR_A),
        ('Tanım ve Çizim', 'Kendi cümlenle açıkla', TUR, TUR_A),
        ('Tarih ve Sunum', '8 tarihi kaydet ve sun', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11.2, renk)
        ic += yazi(x + 68, 62, alt, 10.3, LAC, ince=True)
    return svg(600, 96, ic, 'Tutulmaları araştırma ve kaydetme süreci: bilgi toplama, fikir alışverişi, tanım ve çizim, tarih kaydı ve sunum.', 22)


def bilim_insanlari_panosu():
    bilginler = [
        ('Takıyyüddin (1521-1585)', 'İstanbul Gözlemevini kurdu.', 'Saati gözlem aracı yaptı.', MAVI, MAVI_A),
        ('Zerkâle (1029-1100)', 'Toledo’da gözlem yaptı.', 'Eliptik yörünge fikrini sundu.', TUR, TUR_A),
        ('Dilhan Eryurt (1926-2012)', 'Güneş’in tarihini inceledi.', 'Apollo Başarı Ödülü aldı.', YES, YES_A),
    ]
    ic = ''
    for i, (ad, m1, m2, renk, arka) in enumerate(bilginler):
        x = 12 + i * 194
        ic += f'<rect x="{x}" y="8" width="184" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 92, 27, ad, 10.8, renk)
        ic += f'<line x1="{x + 14}" y1="35" x2="{x + 170}" y2="35" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 16, 56, m1, 10.2, LAC, 'start', ince=True)
        ic += yazi(x + 16, 76, m2, 10.2, LAC, 'start', ince=True)
    return svg(600, 104, ic, 'Üç bilim insanı kartı: Takıyyüddin, Zerkâle ve Dilhan Eryurt.', 22)


def tutulma_tarih_tablosu():
    ic = f'<rect x="8" y="6" width="584" height="94" rx="9" fill="#fbfcff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<rect x="8" y="6" width="584" height="26" rx="9" fill="{MAVI}"/>'
    ic += yazi(88, 23, 'Tutulma Türü', 10.6, '#fff')
    ic += yazi(222, 23, 'Ülkemizde En Son', 10.4, '#fff')
    ic += yazi(346, 23, 'Ülkemizde En Yakın', 10.4, '#fff')
    ic += yazi(462, 23, 'Dünyada En Son', 10.4, '#fff')
    ic += yazi(548, 23, 'Dünyada Yakın', 10.4, '#fff')
    for r, ad in enumerate(['Güneş Tutulması', 'Ay Tutulması']):
        y = 32 + r * 34
        ic += f'<line x1="8" y1="{y}" x2="592" y2="{y}" stroke="{GRI}" stroke-width="1"/>'
        ic += yazi(88, y + 22, ad, 10.6, LAC)
        for sx in [164, 286, 408, 508]:
            ic += f'<line x1="{sx}" y1="6" x2="{sx}" y2="100" stroke="{GRI}" stroke-width="1"/>'
            ic += yazi(sx + 48, y + 22, '? (Tarih)', 10.2, TUR, ince=True)
    return svg(600, 106, ic, 'Tutulma tarihleri araştırma kayıt tablosu: iki tutulma için ülkemizde ve dünyada en son ile en yakın toplam sekiz tarih hücresi.', 22)


def model_sinirlilik_karti():
    ic = f'<rect x="8" y="8" width="584" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += fener_ciz(26, 52)
    ic += f'<line x1="60" y1="52" x2="148" y2="52" stroke="{LAC}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += yazi(104, 42, '30 cm', 10.2, LAC)
    ic += f'<circle cx="168" cy="52" r="18" fill="{MAVI}"/>'
    ic += f'<line x1="188" y1="52" x2="236" y2="52" stroke="{LAC}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += yazi(212, 42, '10 cm', 10.2, LAC)
    ic += f'<circle cx="248" cy="52" r="8" fill="{GRI}"/>'
    ic += f'<rect x="282" y="18" width="298" height="72" rx="8" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(431, 36, 'Öğrenci Yorumu:', 10.8, KIR)
    ic += yazi(431, 56, '“Modelimizdeki uzaklıklar ve küre boyutları', 10.3, LAC, ince=True)
    ic += yazi(431, 74, 'uzaydaki gerçek ölçülerle birebir aynıdır.”', 10.3, LAC, ince=True)
    return svg(600, 108, ic, 'El feneri, 30 cm uzakta büyük top ve 10 cm uzakta küçük top düzeneği ile öğrencinin hatalı ölçek iddiası.', 22)


def hatali_gunes_tutulmasi_duzenegi():
    ic = f'<rect x="8" y="8" width="584" height="96" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(300, 25, 'Güneş Tutulması İçin Kurulan Hatalı Model Düzeneği', 11.2, KIR)
    ic += fener_ciz(44, 56)
    ic += f'<line x1="78" y1="56" x2="480" y2="56" stroke="{GRI}" stroke-width="1.4" stroke-dasharray="5 4"/>'
    # Ortada küçük Dünya (hizadan aşağıda!), sonda büyük Ay
    ic += f'<circle cx="220" cy="78" r="9" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(220, 96, 'Ortada: Dünya (Küçük top, hiza dışı)', 10.2, KIR)
    ic += f'<circle cx="430" cy="56" r="20" fill="{GRI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(430, 94, 'Sonda: Ay (Büyük top)', 10.2, LAC)
    ic += yazi(56, 86, 'El feneri', 10.2, LAC, ince=True)
    return svg(600, 112, ic, 'Hatalı Güneş tutulması modeli: ortada hizadan kaymış küçük Dünya topu, sonda ise büyük Ay topu.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tutulma_duzenek_karsilastirma()
    s[4]['gorsel'] = model_kontrol_hatalari()
    s[5]['gorsel'] = ay_tutulmasi_kayit_diyagrami()
    s[6]['gorsel'] = rol_canlandirma_sahnesi()
    s[7]['gorsel'] = arastirma_rapor_sureci_sema()
    s[8]['gorsel'] = bilim_insanlari_panosu()
    s[9]['gorsel'] = tutulma_tarih_tablosu()
    s[10]['gorsel'] = model_sinirlilik_karti()
    s[12]['gorsel'] = hatali_gunes_tutulmasi_duzenegi()
