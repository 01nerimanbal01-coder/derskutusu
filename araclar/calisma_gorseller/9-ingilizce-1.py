"""9. sınıf İngilizce 1. hafta (İngilizce Dersine Uyum ve Kitabı Kullanma) çalışma kâğıdı görselleri.
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


def g0_bolumler():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Contents', 'İçindekiler', MAVI, MAVI_A),
        ('Glossary', 'Sözlük', TUR, TUR_A),
        ('Rubrics', 'Ölçütler', YES, YES_A),
        ('E-Portfolio', 'Ürün Dosyası', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 11, c)
        ic += f'<line x1="{x + 10}" y1="42" x2="{x + 70}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 10, LAC, ince=True)
    return svg(360, 100, ic, 'Ders kitabı bölümleri kartları', 34)


def g1_beceriler():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'LANGUAGE SKILLS: RECEPTIVE vs PRODUCTIVE', 11, MAVI)
    ic += kutu(14, 32, 160, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(94, 48, 'Receptive (Alıcı)', 10.5, MAVI)
    ic += yazi(94, 66, 'Listening &amp; Reading', 11, LAC)

    ic += kutu(186, 32, 160, 56, TUR_A, TUR, 6, 1.1)
    ic += yazi(266, 48, 'Productive (Üretici)', 10.5, TUR)
    ic += yazi(266, 66, 'Speaking &amp; Writing', 11, LAC)
    return svg(360, 100, ic, 'Alıcı ve üretici dil becerileri karşılaştırma kartı', 34)


def g2_tekrar_diyalog():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 340, 74, YES_A, YES, 8, 1.2)
    ic += yazi(180, 30, 'Classroom Dialogue: Asking for Repetition', 11, YES)
    ic += yazi(180, 50, '"Could you repeat that, please?"', 13, LAC)
    ic += yazi(180, 70, '(Lütfen tekrar edebilir misiniz?)', 10, SOLUK, ince=True)
    return svg(360, 96, ic, 'Sınıf içi nazik tekrar isteme konuşma kartı', 34)


def g3_yonergeler():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    eylemler = [
        ('Match', 'Eşleştir', MAVI, MAVI_A),
        ('Compare', 'Karşılaştır', TUR, TUR_A),
        ('Underline', 'Altını çiz', YES, YES_A),
        ('Discuss', 'Fikir paylaş', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(eylemler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 11.5, c)
        ic += f'<line x1="{x + 10}" y1="42" x2="{x + 70}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 10, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel ders yönergesi kartı', 34)


def g5_ogrenme_dongusu():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. Goal', 'Hedef koy', YES, YES_A),
        ('2. Practice', 'Alıştırma yap', MAVI, MAVI_A),
        ('3. Feedback', 'Dönüt al', TUR, TUR_A),
        ('4. Assess', 'Öz değerlendir', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Dört adımlı öğrenme ve öz değerlendirme döngüsü', 34)


def g6_soru_karti():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'COMMUNICATION STRATEGY: ASKING FOR MEANING', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 54, '"What does this word mean in Turkish?"', 12.5, LAC)
    ic += yazi(180, 70, '(Bu kelime Türkçe ne anlama geliyor?)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Kelimelerin anlamını sorma kalıbı kartı', 34)


def g8_iletisim_kaliplari():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    kaliplar = [
        ('Spell that?', 'Harf sorma', MAVI, MAVI_A),
        ('Borrow pencil?', 'Ödünç isteme', TUR, TUR_A),
        ('Understood?', 'Anlama kontrolü', YES, YES_A),
        ('See you!', 'Vedalaşma', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(kaliplar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Sınıf içi günlük iletişim kalıpları', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'KEYWORD PUZZLE: S - K - I - L - L', 11.5, YES)
    harfler = [('1', 'S'), ('2', 'K'), ('3', 'I'), ('4', 'L'), ('5', 'L')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Skill şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_bolumler()
    s[1]['gorsel'] = g1_beceriler()
    s[2]['gorsel'] = g2_tekrar_diyalog()
    s[3]['gorsel'] = g3_yonergeler()
    s[5]['gorsel'] = g5_ogrenme_dongusu()
    s[6]['gorsel'] = g6_soru_karti()
    s[8]['gorsel'] = g8_iletisim_kaliplari()
    s[10]['gorsel'] = g10_sifre_seridi()
