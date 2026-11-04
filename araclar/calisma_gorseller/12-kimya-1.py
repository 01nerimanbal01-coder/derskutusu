"""12. sınıf Kimya 1. hafta (Redoks Tepkimeleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_redoks_terimi_karti():
    terimler = [
        ('Yükseltgenme', 'Elektron Verme', 'Basamak Artışı', KIR, KIR_A),
        ('İndirgenme', 'Elektron Alma', 'Basamak Azalışı', YES, YES_A),
        ('İndirgen Tür', 'Elektron Veren', 'Yükseltgenen Madde', MAVI, MAVI_A),
        ('Yükseltgen Tür', 'Elektron Alan', 'İndirgenen Madde', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, sat1, sat2, r, z) in enumerate(terimler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, sat1, 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, sat2, 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel redoks terimi bilgi kartı.', 34)


def zn_cu_redoks_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'ÇİNKO - BAKIR REDOKS TRANSFER ŞEMASI', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, KIR_A, KIR)
    ic += yazi(95, 54, 'Zn → Zn²⁺ + 2e⁻', 10.0, KIR)
    ic += yazi(95, 74, 'Yükseltgenme (İndirgen tür)', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, 'Cu²⁺ + 2e⁻ → Cu', 10.0, YES)
    ic += yazi(265, 74, 'İndirgenme (Yükseltgen tür)', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Çinko ve bakır redoks tepkimesi yarı tepkimeleri.', 34)


def kmno4_hesap_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, 'KMnO₄ BİLEŞİĞİNDE Mn BASAMAĞI HESABI', 10.6, MOR)
    ic += yazi(180, 52, 'K (+1)  +  Mn (x)  +  4 · O (-2)  =  0', 10.2, LAC)
    ic += yazi(180, 76, '1 + x - 8 = 0  →  x = +7  (Manganın yükseltgenme basamağı)', 9.5, MOR)
    return svg(360, 110, ic, 'KMnO4 bileşiğinde mangan basamağı hesabı.', 34)


def redoks_karsilastirma_panosu():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Redoks Tepkimeleri', 10.4, YES)
    ic += yazi(91, 48, 'CH₄ + 2O₂ → CO₂ + 2H₂O', 9.4, LAC, ince=True)
    ic += yazi(91, 66, 'Yanma &amp; Metal asit tepkimesi', 9.2, LAC, ince=True)
    ic += yazi(91, 84, 'Elektron basamağı DEĞİŞİR', 9.4, YES)

    ic += kutu(184, 6, 170, 98, MAVI_A, MAVI)
    ic += yazi(269, 26, 'Redoks Olmayanlar', 10.4, MAVI)
    ic += yazi(269, 48, 'HCl + NaOH → NaCl + H₂O', 9.4, LAC, ince=True)
    ic += yazi(269, 66, 'Nötralleşme &amp; Çökelmeler', 9.2, LAC, ince=True)
    ic += yazi(269, 84, 'Elektron basamağı SABİTTİR', 9.4, MAVI)
    return svg(360, 110, ic, 'Redoks ve redoks olmayan tepkime türleri.', 34)


def redoks_denklestirme_akisi():
    adımlar = [
        ('1. Basamak', 'Tüm atomların yükü', MAVI, MAVI_A),
        ('2. Fark', 'Alınan/verilen e⁻', TUR, TUR_A),
        ('3. Eşitle', 'Katsayıyla çarpma', YES, YES_A),
        ('4. Denklem', 'H₂O &amp; atom denkliği', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Redoks tepkimesi denkleştirme adımları akış şeması.', 34)


def dort_tepkime_ornek_karti():
    tepkimeler = [
        ('Yanma', 'CH₄ + O₂ → REDOKS', YES, YES_A),
        ('Nötralleşme', 'Asit + Baz → Değil', MAVI, MAVI_A),
        ('Çökelme', 'Ag⁺ + Cl⁻ → Değil', TUR, TUR_A),
        ('Ayrışma', 'CaCO₃ → Değil', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(tepkimeler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' → ')[0], 9.0, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' → ')[1], 9.2, r)
    return svg(360, 110, ic, 'Dört kimyasal tepkime türü karşılaştırma kartı.', 34)


def periyodik_grup_kurallari_karti():
    kurallar = [
        ('1A Metalleri', 'Daima +1 Basamak', MAVI, MAVI_A),
        ('2A Metalleri', 'Daima +2 Basamak', YES, YES_A),
        ('Flor (F)', 'Daima -1 Basamak', KIR, KIR_A),
        ('Oksijen (O)', 'Genellikle -2', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kurallar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Periyodik elementlerin yükseltgenme basamak kuralları.', 34)


def sifre_kimya_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'ELEKTROKİMYA VE REDOKS KAVRAM PANOSU', 10.8, CAM)
    ic += yazi(180, 50, 'RADİKAL · ELEKTRON · DENKLEM · OKSİT · KATYON · SİSTEM', 9.6, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli elektrokimya terimini (6 harf) bulunuz.', 9.4, CAM, ince=True)
    return svg(360, 110, ic, 'Şifre kimya kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_redoks_terimi_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = zn_cu_redoks_modeli()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = kmno4_hesap_panosu()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = redoks_karsilastirma_panosu()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = redoks_denklestirme_akisi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = dort_tepkime_ornek_karti()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = periyodik_grup_kurallari_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_kimya_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
