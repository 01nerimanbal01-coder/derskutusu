"""10. sınıf Tarih 3. hafta (Türkistan’dan Türkiye’ye Uzanan Süreçte Meydana Gelen Önemli Askerî Mücadelelerin Türk Tarihinin Seyrine Etkileri) çalışma kâğıdı görselleri.
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
        ('Saltuklular', 'Erzurum ve çevresi (Mama Hatun)', MAVI, MAVI_A),
        ('Mengücekliler', 'Erzincan ve Divriği (Ulu Cami)', YES, YES_A),
        ('Dânişmendliler', 'Sivas, Tokat (Yağıbasan Medresesi)', TUR, TUR_A),
        ('Artuklular & Çaka', 'Mardin (Malabadi) & İzmir (Donanma)', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Anadolu\'da kurulan ilk Türk beylikleri ve merkezleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'DÂNİŞMENDLİLER VE YAĞIBASAN MEDRESESİ (TOKAT)', 11, MAVI)
    ic += kutu(16, 34, 328, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(180, 50, 'Anadolu\'nun İlk Kapalı Avlulu Türk Medresesi (1157)', 10, MAVI)
    ic += yazi(180, 72, 'Tıp, astronomi ve İslam ilimlerinde eğitim merkezi olarak hizmet vermiştir.', 8, LAC, ince=True)
    return svg(360, 100, ic, 'Dânişmendliler Tokat Niksar Yağıbasan Medresesi tarihi bilgi kartı', 34)

def g2():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ic += yazi(180, 22, 'ÇAKA BEYLİĞİ VE TÜRK DENİZCİLİĞİNİN DOĞUŞU (1081)', 11, CAM)
    # Sembolik kadırga gövdesi ve yelken
    ic += '<path d="M 40 76 L 100 76 L 90 84 L 50 84 Z" fill="#0e8fa8" stroke="#0b2257" stroke-width="1.2"/>'
    ic += '<polygon points="70,72 70,42 92,60" fill="#2451d6"/>'
    # Sağ bilgi kutusu
    ic += kutu(116, 34, 228, 54, '#ffffff', CAM, 6, 1.2)
    ic += yazi(230, 52, 'İlk Türk Donanması: İzmir (1081)', 10.5, CAM)
    ic += yazi(230, 72, 'Ege adalarında Bizans donanmasına karşı zaferler kazanıldı.', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Çaka Beyliği ve Türk deniz kuvvetlerinin kuruluşu sembolü', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'SALTUKLULAR VE ERZURUM MİMARİ MİRASI', 11, TUR)
    eserler = [
        ('Mama Hatun Külliyesi', 'Tercan\'da eşsiz kümbet ve kervansaray'),
        ('Erzurum Ulu Cami', 'Saltuklu Meliki Nasreddin Mehmed yapısı'),
        ('Üç Kümbetler', 'Anadolu\'daki en eski anıt mezar örnekleri')
    ]
    for i, (b, d) in enumerate(eserler):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', TUR, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, TUR)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Saltuklular dönemi Erzurum mimari eserleri kartı', 34)

def g5():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'ARTUKLULAR VE MALABADİ KÖPRÜSÜ TAŞ KEMERİ (SİLVAN)', 10.5, YES)
    # Köprü kemeri sembolü
    ic += '<path d="M 30 80 Q 75 42 120 80" fill="none" stroke="#12a150" stroke-width="3"/>'
    ic += '<line x1="20" y1="80" x2="130" y2="80" stroke="#0b2257" stroke-width="1.5"/>'
    # Sağ bilgi kutusu
    ic += kutu(136, 34, 208, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(240, 52, 'Dönemin En Geniş Taş Kemeri (40,86 m)', 9.5, YES)
    ic += yazi(240, 72, 'Artuklu mühendisliğinin ve taş işçiliğinin şaheseridir.', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Artuklular dönemi Malabadi Taş Köprüsü mimari modeli', 34)

def g6():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'MENGÜCEKLİLER: DİVRİĞİ ULU CAMİİ VE DARÜŞŞİFASI', 11, MOR)
    ic += kutu(16, 34, 328, 54, '#ffffff', MOR, 6, 1.2)
    ic += yazi(180, 50, 'UNESCO Dünya Kültür Mirası Listesi\'nde Yer Alan Şaheser (1228)', 9.5, MOR)
    ic += yazi(180, 72, 'Ahlatlı ustaların taş üzerine işlediği eşsiz barok kabartmalar ve akıl hastanesi.', 8, LAC, ince=True)
    return svg(360, 100, ic, 'Mengücekliler Divriği Ulu Camii ve Şifahanesi mimari kartı', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    terimler = [
        ('Beylik', 'Anadolu\'da fetih hakkıyla kurulan siyasi teşekkül'),
        ('Subaşı', 'Şehir ve kalelerin asayişinden sorumlu ordu komutanı'),
        ('Donanma', 'Çaka Bey\'in İzmir\'de kurduğu ilk Türk filosu'),
        ('Kümbet', 'Çadır sanatından esinlenen silindirik anıt mezar')
    ]
    for i, (b, d) in enumerate(terimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'İlk Türk beylikleri dönemi teşkilat ve sanat kavramları', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: B - E - Y - L - İ - K', 11.5, YES)
    harfler = [('1', 'B'), ('2', 'E'), ('3', 'Y'), ('4', 'L'), ('5', 'İ'), ('6', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 21, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 21, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Tarih dersi şifre anahtar harf kutuları', 34)

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
