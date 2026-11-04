"""10. sınıf Türk Dili ve Edebiyatı 1. hafta (Koşuk, Koşma, Türkü ve Ninniyi Anlayarak Okuma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def g0_nazim_bicimleri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    turler = [
        ('Koşuk', 'Sözlü dönem / Kopuz', MAVI, MAVI_A),
        ('Koşma', 'Âşık tarzı / Saz', TUR, TUR_A),
        ('Türkü', 'Bent ve kavuştak', YES, YES_A),
        ('Ninni', 'Çocuğa sevgi ve ezgi', MOR, MOR_A)
    ]
    for i, (b, alt, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 11.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 60, alt, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Dört temel nazım biçimi ve özellikleri kartı', 34)


def g1_turku_yapisi():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'TÜRKÜNÜN BÖLÜMLERİ VE İŞLEVLERİ', 11, MAVI)
    ic += kutu(14, 32, 160, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(94, 48, 'Bent (Asıl Bölüm)', 11, MAVI)
    ic += yazi(94, 68, 'Olay ve duygu burada gelişir', 9, LAC, ince=True)

    ic += kutu(186, 32, 160, 56, YES_A, YES, 6, 1.1)
    ic += yazi(266, 48, 'Kavuştak (Nakarat)', 11, YES)
    ic += yazi(266, 68, 'Her bent sonunda yinelenir', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Türküde bent ve kavuştak bölümleri şeması', 34)


def g2_uyak_redif():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 160, 74, TUR_A, TUR, 8, 1.2)
    ic += yazi(90, 28, 'Uyak (Kafiye):', 11, TUR)
    ic += yazi(90, 50, 'Ses Benzerliği', 12, LAC)
    ic += yazi(90, 68, 'Farklı görevdeki sesler', 9.5, SOLUK, ince=True)

    ic += kutu(190, 10, 160, 74, YES_A, YES, 8, 1.2)
    ic += yazi(270, 28, 'Redif:', 11, YES)
    ic += yazi(270, 50, 'Görev / Anlam Tekrarı', 12, LAC)
    ic += yazi(270, 68, 'Aynı ek veya aynı sözcük', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Uyak ve redif karşılaştırma kartı', 34)


def g3_siir_ilkeleri():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [
        ('Koşuk Konusu', 'Doğa ve yiğitlik', MAVI, MAVI_A),
        ('Koşma Türü', 'Güzelleme/Taşlama', TUR, TUR_A),
        ('Türkü Ezgisi', 'Halk müziği', YES, YES_A),
        ('Ahenk', 'Ölçü, uyak, ritim', MOR, MOR_A)
    ]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel halk şiiri ilkesi kartı', 34)


def g5_tahlil_akisi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. Tahmin', 'Başlık ve biçim', YES, YES_A),
        ('2. Okuma', 'Ritim ve ses', MAVI, MAVI_A),
        ('3. Ahenk', 'Ölçü ve uyak', TUR, TUR_A),
        ('4. İleti', 'Açık/örtük anlam', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Şiir tahlili ve anlama adımları şeması', 34)


def g6_teshis_sanati():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'EDEBÎ SANAT: TEŞHİS (KİŞİLEŞTİRME)', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 52, '"Karlı dağlar boynunu büktü sabahleyin"', 12.5, LAC)
    ic += yazi(180, 70, 'İnsana özgü boyun bükme özelliği doğaya (dağlara) aktarılmıştır.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Teşhis kişileştirme sanatı örnek dize kartı', 34)


def g8_kosma_turleri():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    turler = [
        ('Güzelleme', 'Aşk ve doğa', MAVI, MAVI_A),
        ('Koçaklama', 'Yiğitlik ve savaş', TUR, TUR_A),
        ('Taşlama', 'Toplumsal yergi', YES, YES_A),
        ('Ağıt', 'Ölüm ve yas', MOR, MOR_A)
    ]
    for i, (b, tr, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Konularına göre dört temel koşma türü', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: E - Z - G - İ', 11.5, YES)
    harfler = [('1', 'E'), ('2', 'Z'), ('3', 'G'), ('4', 'İ')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 25, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Ezgi şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_nazim_bicimleri()
    s[1]['gorsel'] = g1_turku_yapisi()
    s[2]['gorsel'] = g2_uyak_redif()
    s[3]['gorsel'] = g3_siir_ilkeleri()
    s[5]['gorsel'] = g5_tahlil_akisi()
    s[6]['gorsel'] = g6_teshis_sanati()
    s[8]['gorsel'] = g8_kosma_turleri()
    s[10]['gorsel'] = g10_sifre_seridi()
