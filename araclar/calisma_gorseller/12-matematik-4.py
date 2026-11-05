"""12. sınıf Matematik 4. hafta (Adi ve Doğal Logaritma) çalışma kâğıdı görselleri."""

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

def dort_log_deger_karti():
    kartlar = [
        ('1. log 1000', '= 3 (10³)', MAVI, MAVI_A),
        ('2. ln (e²)', '= 2 (Doğal taban)', YES, YES_A),
        ('3. log 0,01', '= -2 (10⁻²)', TUR, TUR_A),
        ('4. ln (1/e)', '= -1 (e⁻¹)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört logaritma sayısal değeri kartı.", 34)

def taban_takas_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "TABAN TAKAS VE TOPLAM UYGULAMASI", 10.5, CAM)
    ic += yazi(180, 52, "1/log₂ 30 + 1/log₃ 30 + 1/log₅ 30", 10.0, LAC)
    ic += yazi(180, 76, "= log₃₀ 2 + log₃₀ 3 + log₃₀ 5 = log₃₀ 30 = 1", 9.8, YES)
    return svg(360, 110, ic, "Taban takas toplam panosu.", 34)

def ln_log_islem_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "DOĞAL VE ONLUK LOGARİTMA İŞLEMİ", 10.5, TUR)
    ic += yazi(90, 56, "ln(e⁵) = 5", 10.0, MAVI)
    ic += yazi(90, 76, "e tabanında 5", 9.0, LAC, ince=True)
    ic += yazi(270, 56, "log(100) = 2", 10.0, YES)
    ic += yazi(270, 76, "Fark: 5 - 2 = 3", 9.8, TUR)
    return svg(360, 110, ic, "İşlem panosu.", 34)

def log_isaret_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "LOGARİTMA İŞARET ANALİZİ", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, YES_A, YES)
    ic += yazi(92, 56, "x > 1 İse", 10.0, YES)
    ic += yazi(92, 74, "log x > 0 ve ln x > 0", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, KIR_A, KIR)
    ic += yazi(267, 56, "0 &lt; x &lt; 1 İse", 10.0, KIR)
    ic += yazi(267, 74, "log x &lt; 0 ve ln x &lt; 0", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Logaritma işaret analiz şeması.", 34)

def onluk_log_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "ONLUK LOGARİTMA KUVVET SIRALAMASI", 10.5, YES)
    adimlar = ["log 1 = 0", "log 10 = 1", "log 100 = 2", "log 1000 = 3"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 40, 70, a, 8.8, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "&lt;", 12.0, TUR)
    return svg(360, 110, ic, "Onluk logaritma sıralama panosu.", 34)

def basamak_hesap_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "LOGARİTMA İLE BASAMAK SAYISI HESABI", 10.5, MAVI)
    ic += yazi(180, 52, "log(2⁴⁰) = 40 · log 2 ≈ 40 · 0,301 = 12,04", 10.0, LAC)
    ic += yazi(180, 76, "Tam Kısım = 12 → Basamak Sayısı = 12 + 1 = 13", 9.8, YES)
    return svg(360, 110, ic, "Basamak sayısı hesap panosu.", 34)

def dort_taban_donusum_karti():
    kartlar = [
        ('1. log₂ 5', 'ln 5 / ln 2', MAVI, MAVI_A),
        ('2. log₃ 7', 'log 7 / log 3', YES, YES_A),
        ('3. 1 / log₅ 2', 'log₂ 5', TUR, TUR_A),
        ('4. e^(ln 8)', '= 8 (Doğal)', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört taban dönüşüm kartı.", 34)

def sifre_neper_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "LOGARİTMA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "NOKTA · EĞRİ · POZİTİF · EŞİTLİK · REEL", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli matematik bilgininin soyadını (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre Neper kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_log_deger_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = taban_takas_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = ln_log_islem_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = log_isaret_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = onluk_log_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = basamak_hesap_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_taban_donusum_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_neper_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True