"""12. sınıf Matematik 3. hafta (Logaritma Fonksiyonunun Özellikleri) çalışma kâğıdı görselleri."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'

YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def dort_log_ozellik_karti():
    kartlar = [
        ('1. Çarpım Kuralı', 'log(x·y) = log x + log y', MAVI, MAVI_A),
        ('2. Bölüm Kuralı', 'log(x/y) = log x - log y', YES, YES_A),
        ('3. Taban Değişimi', 'log_a b = ln b / ln a', TUR, TUR_A),
        ('4. Kuvvet Kuralı', 'log(xⁿ) = n · log x', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Dört logaritma cebir kuralı kartı.", 34)

def log_zincir_kurali_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "LOGARİTMA ZİNCİR ÇARPIM KURALI", 10.5, CAM)
    ic += yazi(180, 52, "log₂ 3 · log₃ 4 · log₄ 8 = log₂ 8", 10.2, LAC)
    ic += yazi(180, 76, "Sonuç: log₂ (2³) = 3 · log₂ 2 = 3", 9.6, YES)
    return svg(360, 110, ic, "Logaritma zincir çarpım kuralı panosu.", 34)

def log_fark_bolum_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "LOGARİTMA BÖLÜM VE FARK UYGULAMASI", 10.5, TUR)
    ic += yazi(180, 52, "log₂ 24 - log₂ 3 = log₂ (24 / 3)", 10.0, LAC)
    ic += yazi(180, 76, "= log₂ 8 = log₂ (2³) = 3", 9.8, TUR)
    return svg(360, 110, ic, "Logaritma fark ve bölüm panosu.", 34)

def log_temel_kurallar_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "ÖZEL LOGARİTMA DEĞERLERİ", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Sıfır Değeri", 10.0, MAVI)
    ic += yazi(92, 74, "log_a 1 = 0 (Her tabanda)", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Birim Değer", 10.0, YES)
    ic += yazi(267, 74, "log_a a = 1 · ln e = 1", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Özel logaritma değerleri şeması.", 34)

def log_degerleri_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "LOGARİTMA DEĞERLERİ BÜYÜKLÜK SIRALAMASI", 10.5, YES)
    adimlar = ["log₂ 2 = 1", "log₂ 8 = 3", "log₂ 16 = 4", "log₂ 32 = 5"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 38, 70, a, 9.2, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "&lt;", 12.0, TUR)
    return svg(360, 110, ic, "Logaritma değer sıralaması panosu.", 34)

def taban_degistirme_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "TABAN DEĞİŞTİRME ÖZDEŞLİĞİ", 10.5, MAVI)
    ic += yazi(180, 52, "log_a b = (log b) / (log a)", 10.2, LAC)
    ic += yazi(180, 76, "log 2 = x ve log 3 = y ise  log₂ 3 = y / x", 9.8, MAVI)
    return svg(360, 110, ic, "Taban değiştirme özdeşliği panosu.", 34)

def dort_uslu_log_karti():
    kartlar = [
        ('1. a^(log_a x)', '= x (Doğrudan)', MAVI, MAVI_A),
        ('2. e^(ln 5)', '= 5 (Doğal taban)', YES, YES_A),
        ('3. 10^(log 9)', '= 9 (Onluk taban)', TUR, TUR_A),
        ('4. 2^(log₂ 7)', '= 7 (İkili taban)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört üslü logaritma eşitliği kartı.", 34)

def sifre_taban_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "LOGARİTMA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "TANIM · ASİMPTOT · BÖLÜM · ARTAN · NEPER", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli logaritma bileşenini (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre taban kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_log_ozellik_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = log_zincir_kurali_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = log_fark_bolum_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = log_temel_kurallar_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = log_degerleri_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = taban_degistirme_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_uslu_log_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_taban_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True