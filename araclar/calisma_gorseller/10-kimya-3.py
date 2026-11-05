"""10. sınıf Kimya 3. hafta (Kimyasal Tepkime Türleri: Çökelme, İndirgenme-Yükseltgenme ve Asit-Baz Tepkimeleri) çalışma kâğıdı görselleri.
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
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Yanma', 'O₂ gazı ile redoks tepkimesi', KIR, KIR_A),
        ('Sentez (Oluşum)', 'Küçük moleküllerden tek ürün', YES, YES_A),
        ('Analiz (Ayrışma)', 'Tek bileşikten küçük maddeler', TUR, TUR_A),
        ('Asit-Baz & Çökelme', 'Nötralleşme ve katı oluşumu', MAVI, MAVI_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '5 temel kimyasal tepkime türü karşılaştırma kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, KIR_A, KIR)
    ic += yazi(180, 22, 'METAN GAZI (CH₄) YANMA REAKSİYONU VE REDOKS', 11, KIR)
    ic += kutu(16, 34, 328, 54, '#ffffff', KIR, 6, 1.2)
    ic += yazi(180, 52, 'CH₄(g) + 2O₂(g) -> CO₂(g) + 2H₂O(s) + Enerji (Isı)', 11, LAC)
    ic += yazi(180, 74, 'Karbon yükseltgenir, oksijen indirgenir (Ekzotermik Yanma)', 8.5, KIR, ince=True)
    return svg(360, 100, ic, 'Metan gazı yanma denklemi ve ekzotermik redoks şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'ASİT-BAZ NÖTRALLEŞME VE NET İYON DENKLEMİ', 11, MAVI)
    ic += kutu(16, 34, 156, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(94, 50, 'HCl(suda) + NaOH(suda)', 9.5, MAVI)
    ic += yazi(94, 70, '-> NaCl(suda) + H₂O(s)', 9, LAC, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(266, 50, 'Net İyon Denklemi', 9.5, YES)
    ic += yazi(266, 70, 'H⁺(suda) + OH⁻(suda) -> H₂O(s)', 9, YES, ince=True)
    return svg(360, 100, ic, 'Asit baz nötralleşmesi ve su oluşumu net iyon modeli', 34)

def g3():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'ÇÖZÜNME-ÇÖKELME TEPKİMESİ VE SARI ÇÖKELEK', 11, YES)
    # Tüp modeli sembolik
    ic += '<rect x="40" y="36" width="30" height="50" rx="6" fill="#e8eefe" stroke="#0b2257" stroke-width="1.2"/>'
    ic += '<rect x="42" y="72" width="26" height="12" rx="4" fill="#f2b705"/>'
    ic += yazi(55, 60, 'K⁺, NO₃⁻', 6.5, MAVI)
    ic += yazi(55, 80, 'PbI₂↓', 7, '#8a5a2b')
    # Sağ bilgi kutusu
    ic += kutu(90, 36, 254, 52, '#ffffff', YES, 6, 1.2)
    ic += yazi(217, 52, 'Net İyon: Pb²⁺(suda) + 2I⁻(suda) -> PbI₂(k)', 10, YES)
    ic += yazi(217, 72, 'K⁺ ve NO₃⁻ seyirci iyonlardır (Çözeltide serbest)', 8, LAC, ince=True)
    return svg(360, 100, ic, 'Kurşun iyodür çökelme tepkimesi ve seyirci iyonlar şeması', 34)

def g5():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'SENTEZ (OLUŞUM) VE ANALİZ (AYRIŞMA) KARŞILAŞTIRMASI', 10.5, TUR)
    # Sol Sentez
    ic += kutu(16, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(94, 50, 'Sentez: A + B -> AB', 9.5, YES)
    ic += yazi(94, 70, 'N₂(g) + 3H₂(g) -> 2NH₃(g)', 8.5, LAC, ince=True)
    # Sağ Analiz
    ic += kutu(188, 34, 156, 54, '#ffffff', KIR, 6, 1.2)
    ic += yazi(266, 50, 'Analiz: AB -> A + B', 9.5, KIR)
    ic += yazi(266, 70, '2KClO₃(k) -> 2KCl(k) + 3O₂(g)', 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Sentez ve analiz tepkimeleri karşılaştırma modeli', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'KİMYASAL TEPKİMELERDE KORUNAN NİCELİKLER', 11, LAC)
    korunanlar = [
        ('Atom Türü ve Sayısı', 'Daima korunur', YES),
        ('Toplam Kütle', 'Kapalı kapta korunur', MAVI),
        ('Toplam Yük', 'Daima korunur', MOR),
        ('Molekül Sayısı', 'Değişebilir (Korunmayabilir)', TUR)
    ]
    for i, (b, d, c) in enumerate(korunanlar):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 50, b, 7.5, c)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Kimyasal tepkimelerde korunan ve değişebilen nicelikler', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    semboller = [
        ('(k) Katı', 'Kristal veya amorf çökelek fazı'),
        ('(s) Sıvı', 'Saf sıvı bileşikler (Örn: H₂O)'),
        ('(g) Gaz', 'Uçucu gaz fazındaki elementler'),
        ('(suda) Akua', 'Su içinde iyonlaşmış çözeltiler')
    ]
    for i, (b, d) in enumerate(semboller):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kimyasal tepkime denklemlerinde faz sembolleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: R - E - D - O - K - S', 11.5, YES)
    harfler = [('1', 'R'), ('2', 'E'), ('3', 'D'), ('4', 'O'), ('5', 'K'), ('6', 'S')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 21, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 21, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Kimya dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
