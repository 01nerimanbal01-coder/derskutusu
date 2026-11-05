"""10. sınıf Felsefe 3. hafta (Felsefi Sorunun Temel Özellikleri ve Felsefi Soru Oluşturma) çalışma kâğıdı görselleri.
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
        ('Tutarlılık', 'Çelişkisiz akıl yürütme', MAVI, MAVI_A),
        ('Rasyonellik', 'Akla ve mantığa dayanma', YES, YES_A),
        ('Refleksiflik', 'Düşüncenin kendine dönmesi', TUR, TUR_A),
        ('Temellendirme', 'Gerekçe ve kanıt sunma', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefi düşüncenin 4 temel niteliği kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'MANTIKSAL ARGÜMAN YAPISI VE KIYAS ŞEMASI', 11, MAVI)
    # Öncüller ve Sonuç
    ic += kutu(16, 34, 156, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(94, 48, '1. Öncül: Bütün insanlar ölümlüdür.', 7.5, LAC, ince=True)
    ic += yazi(94, 64, '2. Öncül: Sokrates bir insandır.', 7.5, LAC, ince=True)
    ic += yazi(94, 78, '-> Öncüller iddiaya temel oluşturur', 7, MAVI)
    ic += yazi(180, 62, '=>', 14, MAVI)
    ic += kutu(188, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(266, 52, 'Zorunlu Mantıksal Sonuç', 9.5, YES)
    ic += yazi(266, 72, 'O hâlde Sokrates de ölümlüdür.', 8, LAC, ince=True)
    return svg(360, 100, ic, 'Mantıkta geçerli argüman ve tümdengelim şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'FELSEFEDE TEMELLENDİRME VE GEREKÇELENDİRME DÖNGÜSÜ', 10.5, YES)
    ogeler = [
        ('1. Felsefi İddia', 'Öne sürülen ana tez', YES),
        ('2. Gerekçe', 'Mantıksal delil ve kanıt', MAVI),
        ('3. Eleştirel Sınama', 'Karşıt görüş ve çelişki', TUR),
        ('4. Temellendirme', 'Sağlam mantıksal zemin', MOR)
    ]
    for i, (b, d, c) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, c)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefede iddiayı temellendirme döngüsü basamakları', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'KAVRAM ANALİZİ: İÇLEM VE KAPLAM İLİŞKİSİ', 11, TUR)
    ic += kutu(16, 34, 156, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(94, 50, 'Kaplam (Kapsanan Bireyler)', 9, TUR)
    ic += yazi(94, 70, 'Kavram genelleştikçe kaplam artar', 7.5, LAC, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(266, 50, 'İçlem (Ortak Nitelikler)', 9, MAVI)
    ic += yazi(266, 70, 'Kavram özelleştikçe içlem artar', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kavram analizinde içlem ve kaplam ters orantısı kartı', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'FELSEFİ SORGULAMANIN GELİŞİM AŞAMALARI', 11, MOR)
    adimlar = [
        ('1. Merak', 'Var olanı fark etme'),
        ('2. Şüphe', 'Kabulleri sorgulama'),
        ('3. Soru Sorma', 'Öze dönük araştırma'),
        ('4. Rasyonellik', 'Akılla sistem kurma')
    ]
    for i, (b, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefi düşünüşün merak ve şüphe gelişim akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'KLASİK AKIL VE MANTIK İLKELERİ', 11, LAC)
    ilkeler = [
        ('Özdeşlik', 'Bir şey ne ise odur (A, A\'dır)', MAVI),
        ('Çelişmezlik', 'Bir şey aynı anda hem A hem non-A olamaz', TUR),
        ('Üçüncü Durum', 'Bir önerme ya doğrudur ya da yanlıştır', YES)
    ]
    for i, (b, d, c) in enumerate(ilkeler):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 52, b, 9.5, c)
        ic += yazi(x + 52, 72, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Mantığın 3 temel akıl ilkesi karşılaştırma kartı', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    alanlar = [
        ('Ontoloji', 'Varlık felsefesi: Varlığın arkasındaki ilk ilke'),
        ('Epistemoloji', 'Bilgi felsefesi: Doğru bilginin kaynağı ve sınırı'),
        ('Aksiyoloji', 'Değer felsefesi: Ahlak ve estetik yargılar'),
        ('Mantık', 'Doğru düşünme ve çıkarım kuralları bilimi')
    ]
    for i, (b, d) in enumerate(alanlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Felsefenin 4 temel alt disiplini kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: M - E - R - A - K', 11.5, YES)
    harfler = [('1', 'M'), ('2', 'E'), ('3', 'R'), ('4', 'A'), ('5', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Felsefe dersi şifre anahtar harf kutuları', 34)

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
