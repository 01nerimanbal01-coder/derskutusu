"""10. sınıf Arapca 3. hafta (Akrabalarım, Meslekleri ve Çalışma Yerleri: İkil ve Çoğul İsimler (المُثَنَّى وَالْجَمْعُ), İşaret İsimleri (هٰذَانِ / هٰتَانِ / هٰؤُلَاءِ) ve Müzari Fiil Çekimi) çalışma kâğıdı görselleri.
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
        ('Mübteda', 'Cümleye başlanan merfû isim', MAVI, MAVI_A),
        ('Haber', 'Mübtedayı tamamlayan merfû öge', YES, YES_A),
        ('Cinsiyet Uyumu', 'Müzekker / Müennes tam denkliği', TUR, TUR_A),
        ('Tesniye (İkil)', 'İsim sonuna (انِ) eki getirilir', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Arapça isim cümlesi ve tesniye kuralları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 24, 'TESNİYE (İKİL) İŞARET ZAMİRLERİ VE MÜHENDİS ÖRNEĞİ', 11, MAVI)
    # Sol kart: Müzekker ikil
    ic += kutu(16, 36, 158, 52, '#ffffff', MAVI, 6, 1.2)
    ic += yazi(95, 54, 'هٰذَانِ مُهَنْدِسَانِ', 13, LAC)
    ic += yazi(95, 74, 'İki erkek mühendis (Müzekker)', 9, MAVI, ince=True)
    # Sağ kart: Müennes ikil
    ic += kutu(186, 36, 158, 52, '#ffffff', TUR, 6, 1.2)
    ic += yazi(265, 54, 'هٰتَانِ مُهَنْدِسَتَانِ', 13, LAC)
    ic += yazi(265, 74, 'İki kadın mühendis (Müennes)', 9, TUR, ince=True)
    return svg(360, 100, ic, 'Tesniye eril ve dişil işaret zamirleri şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 24, 'Arapçada Tekil ve İkil Yapılış Kuralı', 11, YES)
    ic += kutu(16, 36, 96, 52, '#ffffff', YES, 6, 1.2)
    ic += yazi(64, 54, 'مُعَلِّمٌ', 13, LAC)
    ic += yazi(64, 74, 'Tekil Öğretmen', 9, SOLUK, ince=True)
    ic += yazi(132, 62, '+  انِ  =', 14, YES)
    ic += kutu(160, 36, 184, 52, '#ffffff', YES, 6, 1.2)
    ic += yazi(252, 54, 'مُعَلِّمَانِ', 14, YES)
    ic += yazi(252, 74, 'İki Öğretmen (Merfû Tesniye)', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Tekil isimden ikil tesniye türetme kuralı', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 24, 'İsim Cümlesinde Mübteda ve Haber Uyumu', 11, TUR)
    ornekler = [
        ('الطَّالِبُ مُجْتَهِدٌ', 'Tekil Eril: Öğrenci çalışkandır', MAVI),
        ('الطَّالِبَانِ مُجْتَهِدَانِ', 'İkil Eril: İki öğrenci çalışkandır', YES),
        ('الطَّالِبَاتُ مُجْتَهِدَاتٌ', 'Çoğul Dişil: Kız öğrenciler çalışkandır', MOR)
    ]
    for i, (ar, tr, c) in enumerate(ornekler):
        x = 12 + i * 114
        ic += kutu(x, 34, 108, 56, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 54, 54, ar, 12, c)
        ic += yazi(x + 54, 76, tr, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'İsim cümlesinde mübteda ve haber uyumu örnekleri', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'İSİM CÜMLESİ KURMA ADIMLARI', 11, MOR)
    adimlar = [
        ('1. Mübteda', 'Belirli ve merfû'),
        ('2. Cinsiyet', 'Eril / Dişil uyumu'),
        ('3. Sayı Dengesi', 'Tekil / İkil / Çoğul'),
        ('4. Haber', 'Belirsiz ve merfû')
    ]
    for i, (b, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 32, 80, 56, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 9.5, MOR)
        ic += yazi(x + 40, 72, d, 8, LAC, ince=True)
        if i < 3:
            ic += yazi(x + 83, 60, '>', 11, SOLUK)
    return svg(360, 100, ic, 'Arapça isim cümlesi kurma basamakları akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'ŞAHIS ZAMİRLERİNDE TEKİL VE İKİL KARŞILAŞTIRMASI', 10.5, LAC)
    zamirler = [
        ('هُوَ', 'O (Eril)', 'هُمَا', 'O İkisi (Eril)', MAVI),
        ('هِيَ', 'O (Dişil)', 'هُمَا', 'O İkisi (Dişil)', TUR),
        ('أَنْتَ', 'Sen (Eril)', 'أَنْتُمَا', 'Siz İkiniz', YES),
        ('أَنْتِ', 'Sen (Dişil)', 'أَنْتُمَا', 'Siz İkiniz', MOR)
    ]
    for i, (t, te, ik, ike, c) in enumerate(zamirler):
        x = 10 + i * 86
        ic += kutu(x, 30, 80, 60, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 46, f'{t} -> {ik}', 11, c)
        ic += yazi(x + 40, 64, te, 7.5, SOLUK, ince=True)
        ic += yazi(x + 40, 78, ike, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Şahıs zamirlerinde tekil ve tesniye ikil tablosu', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    kavramlar = [
        ('Mübteda', 'Özne konumundaki isim'),
        ('Haber', 'Yüklem konumundaki bilgi'),
        ('Müzekker', 'Eril varlıkları niteleyen'),
        ('Müennes', 'Dişil varlıkları niteleyen')
    ]
    for i, (b, d) in enumerate(kavramlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Arapça gramer temel kavram kartları', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: R - A - H - İ - M', 11.5, YES)
    harfler = [('1', 'R'), ('2', 'A'), ('3', 'H'), ('4', 'İ'), ('5', 'M')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Arapça dersi şifre anahtar harf kutuları', 34)

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
