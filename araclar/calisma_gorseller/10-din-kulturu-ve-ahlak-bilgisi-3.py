"""10. sınıf Din-kulturu-ve-ahlak-bilgisi 3. hafta (Allah-Âlem İlişkisi: Yaratılış, Gayb ve Şehâdet Âlemi) çalışma kâğıdı görselleri.
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
        ('Evrendeki Düzen', 'Hassas kozmik denge ve nizam', YES, YES_A),
        ('Yaratılış Gayesi', 'İnsanın bilinçli kulluk vazifesi', MAVI, MAVI_A),
        ('İlahi İrade', 'Küllî ve cüz\'î irade dengesi', TUR, TUR_A),
        ('Hikmet ve İbret', 'Kâinattaki ayetleri tefekkür', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'İnsanın evrendeki konumu ve ilahi düzen ilkeleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İNSANIN YARATILIŞ GAYESİ VE SORUMLULUKLARI', 11, MAVI)
    ögeler = [
        ('Akıl ve İrade', 'Hakkı batıldan ayırt etme', MAVI),
        ('İbadet ve Kulluk', 'Yaratıcıya şükran ve itaat', YES),
        ('Yeryüzünü İmar', 'Adalet, barış ve emanet', TUR)
    ]
    for i, (b, d, c) in enumerate(ögeler):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 52, b, 9.5, c)
        ic += yazi(x + 52, 72, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'İnsanın varoluş gayesi ve ahlaki sorumlulukları şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'KÜLLÎ VE CÜZ\'Î İRADE ARASINDAKİ AYRIM', 11, YES)
    # Sol: Küllî İrade
    ic += kutu(16, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(94, 50, 'Küllî İrade (İlahi)', 9.5, YES)
    ic += yazi(94, 70, 'Doğum yeri, anne-baba, evren yasaları', 7.5, LAC, ince=True)
    # Sağ: Cüz’î İrade
    ic += kutu(188, 34, 156, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(266, 50, 'Cüz\'î İrade (İnsani)', 9.5, TUR)
    ic += yazi(266, 70, 'İnanç, amel, ahlak ve tercihler', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Külli irade ve cüzi irade karşılaştırma şeması', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    sifatlar = [
        ('Tekvin', 'Yoktan var etme kudreti', TUR),
        ('İlim', 'Geçmişi ve geleceği bilme', MAVI),
        ('Kudret', 'Her şeye gücü yetme', YES),
        ('Basîr', 'Her şeyi eksiksiz görme', MOR)
    ]
    for i, (b, d, c) in enumerate(sifatlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Allah\'ın subûti sıfatları ve anlamları kartı', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'İNSANIN MANEVİ TEKÂMÜL BASAMAKLARI', 11, MOR)
    adimlar = [
        ('1. Bilgi (İlim)', 'Varlık ve vahyi tanıma'),
        ('2. İnanç (İman)', 'Kalp ile tasdik etme'),
        ('3. Eylem (Amel)', 'Hayırlı davranış sergileme'),
        ('4. İhlas ve İhsan', 'Allah görür gibi yaşama')
    ]
    for i, (b, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'İslam ahlakında ilim amel ihlas basamakları', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'EVRENDEKİ MİZAN VE İLAHİ ADALET ÖLÇÜSÜ', 11, LAC)
    # Geometrik mizan sembolü
    ic += '<line x1="180" y1="36" x2="180" y2="76" stroke="#0b2257" stroke-width="2"/>'
    ic += '<line x1="120" y1="48" x2="240" y2="48" stroke="#0b2257" stroke-width="1.8"/>'
    ic += '<line x1="120" y1="48" x2="105" y2="68" stroke="#2451d6" stroke-width="1"/>'
    ic += '<line x1="120" y1="48" x2="135" y2="68" stroke="#2451d6" stroke-width="1"/>'
    ic += '<line x1="240" y1="48" x2="225" y2="68" stroke="#12a150" stroke-width="1"/>'
    ic += '<line x1="240" y1="48" x2="255" y2="68" stroke="#12a150" stroke-width="1"/>'
    ic += yazi(120, 82, 'Hak ve Adalet', 8.5, MAVI)
    ic += yazi(240, 82, 'Denge ve Mizan', 8.5, YES)
    return svg(360, 100, ic, 'İlahi mizan ve kozmik adalet terazisi sembolü', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    terimler = [
        ('Gayb Âlemi', 'Duyu ötesi ilahi varlık alanı'),
        ('Hikmet', 'Eşyadaki gizli gaye ve fayda'),
        ('Fıtrat', 'İnsanın doğuştan gelen temiz özü'),
        ('Tevhit', 'Allah\'ın birliği ve tekliği inancı')
    ]
    for i, (b, d) in enumerate(terimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Temel kelam ve inanç terimleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: G - A - Y - B', 11.5, YES)
    harfler = [('1', 'G'), ('2', 'A'), ('3', 'Y'), ('4', 'B')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Din kültürü dersi şifre anahtar harf kutuları', 34)

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
