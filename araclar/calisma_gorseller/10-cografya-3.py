"""10. sınıf Cografya 3. hafta (CBS ve Uzaktan Algılamanın Uygulama Alanları) çalışma kâğıdı görselleri.
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
        ('Vektör Veri', 'Nokta, çizgi, poligon geometri', MAVI, MAVI_A),
        ('Raster Veri', 'Piksel ve hücre ızgara matrisi', YES, YES_A),
        ('Öznitelik Verisi', 'Mekânsal nesnenin sözel tablosu', TUR, TUR_A),
        ('Katman Analizi', 'Üst üste bindirme (Overlay)', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Mekânsal veri modelleri ve CBS ilkeleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'VEKTÖR VERİ TİPLERİ VE YERYÜZÜ TEMSİLLERİ', 11, MAVI)
    tipler = [
        ('Nokta (Point)', 'Kuyu, zirve, yangın kulesi', '#2451d6'),
        ('Çizgi (Line)', 'Karayolu, akarsu, fay hattı', '#ee7d12'),
        ('Poligon (Area)', 'Göl, orman, il sınırları', '#12a150')
    ]
    for i, (b, d, c) in enumerate(tipler):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 52, b, 9.5, c)
        ic += yazi(x + 52, 72, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, 'Vektör veri modelleri nokta çizgi alan şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'RASTER VERİ IZGARA YAPISI VE PİKSEL ÇÖZÜNÜRLÜĞÜ', 11, YES)
    # Sol: Izgara matrisi
    for r in range(4):
        for c in range(4):
            val = (r + c) % 3
            dolgu = '#e3f6ea' if val == 0 else ('#c8e6c9' if val == 1 else '#81c784')
            ic += f'<rect x="{30 + c * 16}" y="{34 + r * 14}" width="15" height="13" fill="{dolgu}" stroke="#12a150" stroke-width="0.8"/>'
    # Sağ bilgi kartı
    ic += kutu(110, 34, 234, 56, '#ffffff', YES, 6, 1.2)
    ic += yazi(227, 52, 'Hücre (Piksel) Boyutu ve Detay', 10, YES)
    ic += yazi(227, 72, 'Piksel küçüldükçe mekânsal çözünürlük ve doğruluk artar.', 8, LAC, ince=True)
    return svg(360, 100, ic, 'Raster veri modeli piksel ızgarası ve çözünürlük şeması', 34)

def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'CBS ÇOK KATMANLI MEKÂNSAL ÇAKIŞTIRMA (OVERLAY)', 11, TUR)
    katmanlar = [
        ('1. Arazi Örtüsü', 'Orman, tarım, yerleşim'),
        ('2. Eğim ve Yükseklik', 'Topoğrafik konturlar'),
        ('3. Jeoloji ve Zemin', 'Kayaç türü, deprem fayı'),
        ('4. Sonuç Analizi', 'Yerleşime uygun alanlar')
    ]
    for i, (k, d) in enumerate(katmanlar):
        x = 10 + i * 86
        c = TUR if i < 3 else YES
        ic += kutu(x, 34, 80, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 40, 50, k, 8.5, c)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Coğrafi bilgi sistemlerinde katman üst üste bindirme modeli', 34)

def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'MEKÂNSAL VERİ TOPLAMA VE DİJİTALLEŞTİRME YÖNTEMLERİ', 10.5, MOR)
    yontemler = [
        ('Uzaktan Algılama', 'Uydu ve uçak sensörleri'),
        ('GNSS / GPS', 'Uydudan hassas koordinat'),
        ('LIDAR Tarama', 'Lazer ile 3B yükseklik'),
        ('Yersel Ölçüm', 'Total station ve teodolit')
    ]
    for i, (b, d) in enumerate(yontemler):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 7, LAC, ince=True)
    return svg(360, 100, ic, 'Mekânsal veri üretme ve dijitalleştirme yöntemleri kartı', 34)

def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'GNSS / GPS KÜRESEL KONUMLANDIRMA İLKESİ', 11, LAC)
    # 4 Uydu geometrisi
    uydular = [(50, 48), (120, 38), (240, 38), (310, 48)]
    for x, y in uydular:
        ic += f'<rect x="{x-10}" y="{y-6}" width="20" height="12" rx="3" fill="#2451d6"/>'
        ic += f'<line x1="{x}" y1="{y+6}" x2="180" y2="78" stroke="#2451d6" stroke-dasharray="3,2" stroke-width="1"/>'
    # Alıcı yer istasyonu
    ic += '<circle cx="180" cy="78" r="6" fill="#ee7d12" stroke="#0b2257" stroke-width="1.2"/>'
    ic += yazi(180, 92, 'En az 4 uydu ile hassas (X, Y, Z, Zaman) konumu', 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'GPS uydu sinyalleriyle yer konumu tespit şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    bilesenler = [
        ('Donanım', 'Bilgisayar, sunucu, GPS alıcısı'),
        ('Yazılım', 'CBS analiz ve haritalama araçları'),
        ('Veri', 'Mekânsal ve öznitelik tabloları'),
        ('Yöntem', 'Standart coğrafi analiz kuralları')
    ]
    for i, (b, d) in enumerate(bilesenler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Coğrafi bilgi sisteminin 4 temel bileşeni kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: U - Y - D - U', 11.5, YES)
    harfler = [('1', 'U'), ('2', 'Y'), ('3', 'D'), ('4', 'U')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Coğrafya dersi şifre anahtar harf kutuları', 34)

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
