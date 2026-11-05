"""11. sınıf Coğrafya 8. hafta görselleri (SVG; insan figürü yok K024; beyaz bant yok K178; 24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket):
    stil = ' style="width:100%;max-height:24mm;display:block;margin:1mm auto;"'
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+81},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def uclu(baslik, k1, a1, k2, a2, k3, a3, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + yazi(180, 22, baslik, 10.0, c)
    for i, (k, a, rk, dk) in enumerate([(k1, a1, MAVI, MAVI_A), (k2, a2, TUR, TUR_A), (k3, a3, YES, YES_A)]):
        x = 12 + i * 114
        ic += kutu(x, 32, 108, 70, dk, rk) + yazi(x + 54, 54, k, 9.2, rk) + yazi(x + 54, 78, a, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.2, LAC) + yazi(180, 82, s2, 8.4, SOLUK, ince=True)
    return svg(360, 115, ic, etiket)

def g0():
    return cizelge4([('Yukarı Kıyıdaş', 'Fırat, Dicle, Çoruh', MAVI, MAVI_A), ('Aşağı Kıyıdaş', 'Meriç ve Asi', TUR, TUR_A), ('Ramsar Alanı', 'Manyas ve Göksu', YES, YES_A), ('Su Stresi', 'Kişi başı ~1300 m^3', KIR, KIR_A)], 'Türkiye su kaynakları temel kavramları')
def g1():
    return ikili('SINIR AŞAN SULARDA TÜRKİYE JEOPOLİTİĞİ', 'Yukarı Kıyıdaş (Doğduğu Ülke)', 'Fırat, Dicle, Çoruh, Aras, Kura', 'Aşağı Kıyıdaş (Döküldüğü Ülke)', 'Meriç (Bulgaristan) · Asi (Lübnan)', MAVI, MAVI_A, TUR, TUR_A, 'Yukarı ve aşağı kıyıdaş akarsularımız')
def g2():
    return uclu('TÜRKİYE SEKTÖREL SU TÜKETİM DAĞILIMI', 'Tarımsal Sulama', '~%75 (En yüksek pay)', 'İçme ve Kullanma', '~%15 (Kentsel şebeke)', 'Sanayi Üretimi', '~%10 (Fabrika/soğutma)', YES, YES_A, 'Sektörel su kullanımı')
def g3():
    return cizelge4([('Sınır Aşan', 'Fırat - Dicle - Asi', MAVI, MAVI_A), ('Damla Sulama', 'Buharlaşmayı önler', YES, YES_A), ('Gri Su', 'Arıtılmış evsel su', CAM, CAM_A), ('Yağmur Hasadı', 'Çatı suyu depolama', MOR, MOR_A)], 'Su yönetimi ve tasarruf kavramları')
def g6():
    return akis4([('1. Vahşi Sulama', 'Aşırı su tüketimi', TUR, TUR_A), ('2. Seviye Düşüşü', 'Yer altı suyu çekilir', KIR, KIR_A), ('3. Obruk Çökmesi', 'Karstik tavan çöker', MOR, MOR_A), ('4. Göl Kuruması', 'Ekosistem kaybı', GRI, GRI_A)], 'Aşırı su kullanımının çevresel sonuçları')
def g7():
    return uclu('FALKENMARK SU STRESİ GÖSTERGESİ (KİŞİ BAŞI / YIL)', 'Su Zengini Ülke', '> 1700 m^3 tatlı su', 'Su Stresi (Türkiye)', '1000 - 1700 m^3 (~1300)', 'Su Kıtlığı Sınırı', '< 1000 m^3 tatlı su', KIR, KIR_A, 'Falkenmark su stresi sınıflandırması')
def g8():
    return ikili('SÜRDÜRÜLEBİLİR SU YÖNETİMİ ÇÖZÜMLERİ', 'Tarımsal Önlemler', 'Damla sulama ve kurakçıl ürün', 'Kentsel Önlemler', 'Gri su arıtımı ve yağmur hasadı', YES, YES_A, MAVI, MAVI_A, 'Tarım ve kentte sürdürülebilir su yönetimi')
def g9():
    return cizelge4([('Çevresel Etki', 'Ramsar biyoçeşitlilik', YES, YES_A), ('Ekonomik Etki', 'Tarım, HES, balıkçılık', MAVI, MAVI_A), ('Politik Etki', 'Boğazlar ve Mavi Vatan', MOR, MOR_A), ('Sosyokültürel', 'Çeşme, hamam, kaplıca', TUR, TUR_A)], 'Su kaynaklarının dört boyutlu etkileri')

def uygula(o):
    s = o['sorular']
    for idx, fn in [(0, g0), (1, g1), (2, g2), (3, g3), (6, g6), (7, g7), (8, g8), (9, g9)]:
        s[idx]['gorsel'] = fn()
