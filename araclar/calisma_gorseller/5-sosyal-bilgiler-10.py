"""5. sınıf Sosyal Bilgiler 10. hafta (Yaşadığımız İlde Meydana Gelebilecek Afetlerin Etkilerini Azaltmaya Yönelik Önlemler ve Afet Bilinci) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_il_afet_riski_kartlari():
    kartlar = [
        ('1. Rize', 'Bol yağış · Heyelan', MAVI, MAVI_A),
        ('2. Hakkâri', 'Dik dağlar · Çığ', MOR, MOR_A),
        ('3. Konya', 'İç ova · Tsunami (?)', KIR, KIR_A),
        ('4. Muğla', 'Yaz kurak · Yangın', TUR, TUR_A),
    ]
    ic = ''
    for i, (il, risk, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 23, il, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="31" x2="{x + 74}" y2="31" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, risk, 9.0, LAC, ince=True)
    return svg(360, 86, ic, 'Dört ilin coğrafi özellikleri ve afet riski kartları.', 15)


def deprem_asamalari_davranis_kartlari():
    kartlar = [
        ('1. Sabitleme', 'Dolaplara L-demir', MAVI, MAVI_A),
        ('2. Korunma', 'Çök-Kapan-Tutun', TUR, TUR_A),
        ('3. Güvenlik', 'Vanaları kapatma', MOR, MOR_A),
        ('4. Hazırlık', 'Acil durum çantası', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Deprem öncesi, sırası ve sonrası dört davranış kartı.', 15)


def afet_cantasi_malzeme_gruplari():
    gruplar = [
        ('1. Grup · Beslenme', 'Su ve kuru gıdalar', MAVI, MAVI_A),
        ('2. Grup · Sağlık', 'İlk yardım ve ilaçlar', YES, YES_A),
        ('3. Grup · İletişim', 'Fener, düdük, radyo', TUR, TUR_A),
        ('4. Grup · Süs Eşyası', 'Cam vazo ve porselen', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(gruplar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, alt, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Afet ve Acil Durum Çantası malzeme seçim grupları.', 16)


def farkindalik_eylem_asamalari():
    asama = [
        ('I. Planlama', 'Amaç, süre ve', 'görev dağılımı', MAVI, MAVI_A),
        ('II. [ ? ]', 'Tahliye tatbikatı ve', 'çanta tanıtım sergisi', YES, YES_A),
        ('III. Değerlendirme', 'Hedefe ulaşma ve', 'katkı analizi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(asama):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 22, bas, 10.1, r)
        ic += yazi(x + 56, 45, s1, 9.3, LAC, ince=True)
        ic += yazi(x + 56, 65, s2, 9.3, LAC)
    return svg(360, 88, ic, 'Farkındalık etkinliğinin planlama, uygulama ve değerlendirme aşamaları.', 15)


def heyelan_ve_erozyon_farki():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Heyelan (Toprak Kayması)', 10.0, TUR)
    ic += yazi(91, 44, 'Dik, killi ve bol yağışlı yamaç', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'Toprak kütlesi ANİDEN kayar', 9.5, TUR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Erozyon (Toprak Aşınması)', 10.0, YESIL_K)
    ic += yazi(269, 44, 'Bitki örtüsü cılız, kurak arazi', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'Üst toprak YAVAŞÇA süpürülür', 9.5, YESIL_K)
    return svg(360, 88, ic, 'Heyelan ve erozyon kavramlarının karşılaştırma kartı.', 15)


def okul_deprem_tahliye_akisi():
    adimlar = [
        ('Adım A', 'Çök-Kapan-Tutun', TUR, TUR_A),
        ('Adım B', 'Eşya sabitleme', MAVI, MAVI_A),
        ('Adım C', 'Toplanma alanı', MOR, MOR_A),
        ('Adım D', 'Sakin tahliye', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 55, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Okulda deprem öncesi, sırası ve sonrası tahliye basamakları.', 15)


def afet_risk_azaltma_panosu():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 21, 'İlimizde Afet Riskini Azaltma İlkeleri Panosu', 10.4, MAVI)
    ic += yazi(180, 40, '• Deprem: Fay hattından uzak sağlam zemin ve yönetmeliğe uygun bina.', 9.4, LAC, ince=True)
    ic += yazi(180, 58, '• Sel: Dere yataklarını açık tutma, altyapı ıslahı ve yeşil alanları koruma.', 9.4, LAC, ince=True)
    ic += yazi(180, 75, '• Çığ ve Erozyon: Yamaçları ağaçlandırma, teraslama ve çığ perdeleri.', 9.4, YESIL_K)
    return svg(360, 92, ic, 'Deprem, sel, çığ ve erozyon etkilerini azaltma ilkeleri panosu.', 16)


def sms_ve_duduk_onemi_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, '1. İletişimde SMS Tercihi', 10.1, CAM)
    ic += yazi(91, 44, 'Sesli arama hatları kilitler;', 9.5, LAC, ince=True)
    ic += yazi(91, 64, 'SMS ve internet mesajı kullanın', 9.4, CAM)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Afet Çantasında Düdük', 10.1, TUR)
    ic += yazi(269, 44, 'Bağırmak enerjiyi hızla tüketir;', 9.5, LAC, ince=True)
    ic += yazi(269, 64, 'düdük sesi uzağa kolayca ulaşır', 9.4, TUR)
    return svg(360, 88, ic, 'Afet sonrasında SMS kullanımı ve düdüğün önemi kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_il_afet_riski_kartlari()
    s[2]['gorsel'] = deprem_asamalari_davranis_kartlari()
    s[5]['gorsel'] = afet_cantasi_malzeme_gruplari()
    s[6]['gorsel'] = farkindalik_eylem_asamalari()
    s[7]['gorsel'] = heyelan_ve_erozyon_farki()
    s[8]['gorsel'] = okul_deprem_tahliye_akisi()
    s[9]['gorsel'] = afet_risk_azaltma_panosu()
    s[11]['gorsel'] = sms_ve_duduk_onemi_karti()
