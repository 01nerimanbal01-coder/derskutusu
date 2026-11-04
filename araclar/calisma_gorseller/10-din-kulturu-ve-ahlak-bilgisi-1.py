"""10. sınıf Din Kültürü ve Ahlak Bilgisi 1. hafta (İslam’da Bilgi ve Bilginin Kaynakları) çalışma kâğıdı görselleri.
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


def g0_bilgi_kaynaklari():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Selim Akıl', 'Doğru muhakeme', MAVI, MAVI_A),
        ('Salim Duyular', 'Yanılsamasız algı', YES, YES_A),
        ('Sadık Haber', 'Vahiy ve mütevatir', TUR, TUR_A),
        ('Rüya ve İlham', 'Öznel (Bağlamaz)', MOR, MOR_A)
    ]
    for i, (b, alt, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 60, alt, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'İslam\'da bilgi kaynakları karşılaştırma kartları', 34)


def g1_sadik_haber():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'SADIK HABER: KESİN BİLGİ KAYNAĞI', 11, MAVI)
    ic += kutu(14, 32, 160, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(94, 48, 'Mütevatir Haber', 11, MAVI)
    ic += yazi(94, 68, 'Kur\'an-ı Kerim nakli', 9.5, LAC, ince=True)

    ic += kutu(186, 32, 160, 56, YES_A, YES, 6, 1.1)
    ic += yazi(266, 48, 'Peygamberin Haberi', 11, YES)
    ic += yazi(266, 68, 'Sahih vahiy ve sünnet', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Sadık haber dalları şeması', 34)


def g2_ayet_karti():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 340, 74, TUR_A, TUR, 8, 1.2)
    ic += yazi(180, 28, 'ZÜMER SURESİ · 9. AYET', 11, TUR)
    ic += yazi(180, 50, '"Hiç bilenlerle bilmeyenler bir olur mu?"', 13, LAC)
    ic += yazi(180, 70, 'İlim ve tefekkürün insan hayatındaki üstün değeri', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Zümer suresi 9. ayet kartı', 34)


def g3_bilgi_ilkeleri():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [
        ('Selim Akıl', 'Tefekkür', MAVI, MAVI_A),
        ('Öznel Bilgi', 'Rüya bağlamaz', KIR, KIR_A),
        ('Suffe Mektebi', 'Öğretim merkezi', YES, YES_A),
        ('Salim Duyu', 'Fiziksel dünya', TUR, TUR_A)
    ]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, alt, 9.5, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel bilgi ilkesi kartı', 34)


def g5_bilgiden_amele():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. İlim', 'Doğru bilgi', YES, YES_A),
        ('2. Tefekkür', 'Derin kavrama', MAVI, MAVI_A),
        ('3. İman', 'Kalple tasdik', TUR, TUR_A),
        ('4. Salih Amel', 'Yararlı eylem', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Bilgiden amele dönüşüm aşamaları şeması', 34)


def g6_faydali_ilim():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'HZ. PEYGAMBER\'İN İLİM AHLAKI ÖĞÜDÜ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 54, '"Faydasız ilimden Allah\'a sığınırım."', 13, LAC)
    ic += yazi(180, 70, 'Bilgi ahlaki olgunluğa ve insanlığa hizmet etmelidir.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Faydalı ilim ve ahlaki sorumluluk panosu', 34)


def g8_ilim_dallari():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ilimler = [
        ('Tefsir', 'Ayet tefsiri', MAVI, MAVI_A),
        ('Hadis', 'Peygamber sözü', TUR, TUR_A),
        ('Fıkıh', 'İslam hukuku', YES, YES_A),
        ('Kelam', 'İnanç esasları', MOR, MOR_A)
    ]
    for i, (b, tr, c, d) in enumerate(ilimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'İslam medeniyetinde gelişen dört temel ilim dalı', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: B - İ - L - G - İ', 11.5, YES)
    harfler = [('1', 'B'), ('2', 'İ'), ('3', 'L'), ('4', 'G'), ('5', 'İ')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Bilgi şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_bilgi_kaynaklari()
    s[1]['gorsel'] = g1_sadik_haber()
    s[2]['gorsel'] = g2_ayet_karti()
    s[3]['gorsel'] = g3_bilgi_ilkeleri()
    s[5]['gorsel'] = g5_bilgiden_amele()
    s[6]['gorsel'] = g6_faydali_ilim()
    s[8]['gorsel'] = g8_ilim_dallari()
    s[10]['gorsel'] = g10_sifre_seridi()
