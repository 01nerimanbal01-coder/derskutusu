"""10. sınıf Turk-dili-ve-edebiyati 3. hafta (Sözün Ezgisi Teması Okuma Sürecini Değerlendirme, Şiir Dinletisi (Konuşma) ve Dinleme/İzleme: Türkü) çalışma kâğıdı görselleri.
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
        ('Bent', 'Türküde asıl konunun anlatıldığı dize öbeği', MAVI, MAVI_A),
        ('Kavuştak', 'Bentleri birbirine bağlayan nakarat bölümü', YES, YES_A),
        ('Kırık Hava', 'Ritmik, usullü ve hareketli ezgili türkü', TUR, TUR_A),
        ('Uzun Hava', 'Serbest ritimli, usulsüz ve geniş sesli türkü', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Türkü nazım şekli yapı taşları ve ezgi türleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'TÜRKÜ NAZIM ŞEKLİNDE BENT VE KAVUŞTAK DÜZENİ', 11, MAVI)
    # Sol Bent
    ic += kutu(16, 34, 156, 54, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(94, 50, 'Bent (Asıl Sözler)', 9.5, MAVI)
    ic += yazi(94, 70, '3 veya 4 dizeden oluşur, tema işlenir', 7.5, LAC, ince=True)
    # Sağ Kavuştak
    ic += kutu(188, 34, 156, 54, '#ffffff', YES, 6, 1.2)
    ic += yazi(266, 50, 'Kavuştak (Bağlama / Nakarat)', 9.5, YES)
    ic += yazi(266, 70, 'Bentlerin sonunda aynen tekrarlanır', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Türküde bent ve kavuştak dize yapısı şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'EZGİLERİNE GÖRE TÜRKÜLERİN KARŞILAŞTIRILMASI', 11, TUR)
    # Sol Kırık Hava
    ic += kutu(16, 34, 156, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(94, 50, 'Kırık Hava (Usullü)', 9.5, TUR)
    ic += yazi(94, 70, 'Belirli bir ritim ve tempoyla söylenir (Halay, Zeybek)', 6.5, LAC, ince=True)
    # Sağ Uzun Hava
    ic += kutu(188, 34, 156, 54, '#ffffff', MOR, 6, 1.2)
    ic += yazi(266, 50, 'Uzun Hava (Usulsüz)', 9.5, MOR)
    ic += yazi(266, 70, 'Serbest ritimli, geniş ses aralıklı (Bozlak, Hoyrat, Maya)', 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Kırık hava ve uzun hava icra özellikleri karşılaştırması', 34)

def g3():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'TÜRKÜLERDE HECE ÖLÇÜSÜ VE DURAK DÜZENLERİ', 11, YES)
    olculer = [
        ('7\'li Hece', 'Genellikle manilerde ve kısa türkülerde (4+3 durak)', MAVI),
        ('8\'li Hece', 'Koşma ve türkülerde yaygın ritim (4+4 durak)', YES),
        ('11\'li Hece', 'En yaygın türkü ve bozlak ölçüsü (6+5 veya 4+4+3 durak)', TUR)
    ]
    for i, (b, d, c) in enumerate(olculer):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 9, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, 'Türkülerde hece ölçüsü ve durak kalıpları kartı', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'ANADOLU\'DA UZUN HAVA TÜRLERİ VE YÖRELERİ', 11, MOR)
    turler = [
        ('Bozlak', 'İç Anadolu (Kırşehir) ve Güney (Türkmen)', MAVI),
        ('Hoyrat', 'Güneydoğu Anadolu (Şanlıurfa, Kerkük)', TUR),
        ('Maya', 'Doğu Anadolu ve Elazığ yöresi', YES),
        ('Ağıt', 'Ölüm ve yas üzerine yakılan türküler', KIR)
    ]
    for i, (b, d, c) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, c)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Anadolu uzun hava türleri ve yöresel dağılımı kartı', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'TÜRKÜLERDE SÖZ VE MÜZİK BÜTÜNLÜĞÜ', 11, LAC)
    # Sembolik bağlama saz teknesi ve sapı
    ic += '<ellipse cx="60" cy="62" rx="20" ry="14" fill="#8a5a2b" stroke="#0b2257" stroke-width="1.2"/>'
    ic += '<line x1="80" y1="62" x2="130" y2="62" stroke="#8a5a2b" stroke-width="3"/>'
    # Sağ bilgi kutusu
    ic += kutu(140, 34, 204, 54, '#ffffff', TUR, 6, 1.2)
    ic += yazi(242, 50, 'Saz Eşliğinde İcra Edilir', 9.5, TUR)
    ic += yazi(242, 70, 'Zamanla yöre halkının ortak malı (anonim) olur.', 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Türkülerde saz eşliği ve anonimleşme süreci sembolü', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    turler = [
        ('Türkü', 'Ezgili, bent ve kavuştaklı anonim nazım şekli'),
        ('Mâni', 'Tek dörtlük (aaxa), 7\'li hece anonim şiir'),
        ('Ağıt', 'Ölüm acısını dile getiren ezgili halk şiiri'),
        ('Ninni', 'Bebekleri uyutmak için söylenen ezgili söz')
    ]
    for i, (b, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Anonim Türk halk edebiyatı nazım türleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: T - Ü - R - K - Ü', 11.5, YES)
    harfler = [('1', 'T'), ('2', 'Ü'), ('3', 'R'), ('4', 'K'), ('5', 'Ü')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Türk dili ve edebiyatı dersi şifre anahtar harf kutuları', 34)

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
