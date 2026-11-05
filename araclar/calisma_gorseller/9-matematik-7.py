"""9. sınıf Matematik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def dörtlu_kart(etiket, kartlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis_karti(etiket, adimlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def uclu_pano(etiket, ust_baslik, kutular, ana_renk=MAVI, ana_acik=MAVI_A):
    ic = kutu(4, 4, 352, 107, ana_acik, ana_renk) + yazi(180, 23, ust_baslik, 10, ana_renk)
    for i, (b, alt, c, d) in enumerate(kutular):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 66, d, c) + yazi(x + 52, 55, b, 9.5, c) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def bilgi_panosu(etiket, baslik, satir1, satir2, c=CAM, d=CAM_A, ic_d='#eaf7fa'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 25, baslik, 10, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, satir1, 9.6, LAC) + yazi(180, 82, satir2, 8.6, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return dörtlu_kart('f(x) = 2x - 8 nitel analizi', [
        ('Eğim (a = 2)', 'a > 0 → Artan', MAVI, MAVI_A),
        ('y-Kesimi', 'x = 0 → (0, -8)', YES, YES_A),
        ('Sıfırı (Kökü)', '2x - 8 = 0 → x = 4', TUR, TUR_A),
        ('Pozitif Aralık', 'x > 4 → (4, ∞)', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Referans fonksiyondan genel doğrusal fonksiyona', 'f(x) = x REFERANS FONKSİYONU VE g(x) = ax + b', [
        ('f(x) = x Referans', 'Orijinden (0,0) geçer', MAVI, '#f4f8fe'),
        ('Dağılma Özelliği', 'a(x ± r) ± k = ax + b', YES, YES_A),
        ('Değişim Oranı (a)', 'a = Δy / Δx sabittir', TUR, TUR_A)
    ], MAVI, MAVI_A)
def g2():
    return bilgi_panosu('İki noktası bilinen doğrusal fonksiyon', 'EĞİM (DEĞİŞİM ORANI) VE SIFIR (KÖK) HESABI',
        'A(x₁, y₁) ve B(x₂, y₂) için Eğim: a = (y₂ - y₁) / (x₂ - x₁) · Sıfırı: ax + b = 0 ⇒ x = -b/a',
        'Doğrusal fonksiyonlarda değişim oranı (eğim) tanım kümesindeki her aralıkta sabittir.', CAM, CAM_A)
def g3():
    return dörtlu_kart('Eğimin (a) işareti ve nitelikler', [
        ('a > 0 İse', 'ℝ’de daima ARTAN', YES, YES_A),
        ('a < 0 İse', 'ℝ’de daima AZALAN', KIR, KIR_A),
        ('a = 0 İse', 'g(x) = b SABİT', TUR, TUR_A),
        ('a ≠ 0 İse', 'Bire bir ve örten', MAVI, MAVI_A)
    ])
def g5():
    return akis_karti('Doğrusal fonksiyon inceleme adımları', [
        ('1. Standart Yaz', 'g(x) = ax + b yap', MAVI, MAVI_A),
        ('2. Eğime Bak', 'a>0 artan, a<0 azalan', YES, YES_A),
        ('3. Eksen Kesimi', '(0, b) ve (-b/a, 0)', TUR, TUR_A),
        ('4. İşaret Tablosu', 'Kökün sağı ve solu', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('Sınırlı aralıkta maksimum ve minimum', 'TANIM KÜMESİNE GÖRE MAKSİMUM VE MİNİMUM DEĞER', [
        ('Tanım Kümesi ℝ', 'Max ve min YOKTUR', KIR, KIR_A),
        ('[c, d] Kapalı Aralık', 'Uç noktalarda alınır', MAVI, '#f4f8fe'),
        ('f(c) ve f(d)', 'Büyüğü max, küçüğü min', YES, YES_A)
    ], YES, YES_A)
def g7():
    return bilgi_panosu('Bire birlik, örtenlik ve sabit fonksiyon', 'BİRE BİR VE ÖRTEN FONKSİYON KOŞULU (g: ℝ → ℝ)',
        'a ≠ 0 iken g(x) = ax + b doğrusal fonksiyonu hem BİRE BİR hem de ÖRTENDİR',
        'a = 0 iken g(x) = b sabit fonksiyonu tüm sayıları b’ye eşlediği için bire bir ve örten değildir.', TUR, TUR_A, '#fff6ea')
def g8():
    return dörtlu_kart('Gerçek yaşam doğrusal modelleri', [
        ('Başlangıç (b)', 't = 0 anındaki değer', MAVI, MAVI_A),
        ('Sabit Artış (+a)', 'f(t) = a·t + b', YES, YES_A),
        ('Sabit Azalış (-a)', 'f(t) = -a·t + b', KIR, KIR_A),
        ('Taksi / Depo', 'Doğrusal değişim', MOR, MOR_A)
    ])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
