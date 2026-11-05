"""12. sınıf Fizik 4. hafta (Açısal Momentum ve Korunumu) çalışma kâğıdı görselleri."""

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

def dort_acisal_buyukluk_karti():
    kartlar = [
        ('1. Momentum (L)', 'kg·m²/s · Vektörel', MAVI, MAVI_A),
        ('2. Tork (τ)', 'N·m · ΔL / Δt', YES, YES_A),
        ('3. Açısal İvme', 'rad/s² · Δω / Δt', TUR, TUR_A),
        ('4. Eylemsizlik', 'kg·m² · I = mr²', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:
            ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört açısal büyüklük kartı.", 34)

def acisal_korunum_patenci_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "AÇISAL MOMENTUMUN KORUNUMU VE DÖNME DİNAMİĞİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(95, 54, "Kollar Açık: I_büyük", 10.0, MAVI)
    ic += yazi(95, 74, "Açısal hız düşük: ω_küçük", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, "Kollar Kapalı: I_küçük", 10.0, YES)
    ic += yazi(265, 74, "Açısal hız yüksek: ω_büyük", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Açısal momentumun korunumu panosu.", 34)

def acisal_momentum_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "AÇISAL MOMENTUM FORMÜL HESABI", 10.5, TUR)
    ic += yazi(90, 56, "Eylemsizlik Momenti: I = 4 kg·m²", 9.6, LAC)
    ic += yazi(90, 76, "Açısal Hız: ω = 5 rad/s", 9.6, MAVI)
    ic += yazi(270, 56, "L = I · ω = 4 · 5", 10.0, YES)
    ic += yazi(270, 76, "L = 20 kg·m²/s", 10.2, YES)
    return svg(360, 110, ic, "Açısal momentum hesap panosu.", 34)

def tork_momentum_iliskisi_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "TORK VE AÇISAL MOMENTUM İLİŞKİSİ", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, YES_A, YES)
    ic += yazi(92, 56, "Net Tork = 0 İse", 10.0, YES)
    ic += yazi(92, 74, "L_ilk = L_son (Korunur)", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, KIR_A, KIR)
    ic += yazi(267, 56, "Net Tork ≠ 0 İse", 10.0, KIR)
    ic += yazi(267, 74, "τ = ΔL / Δt (Değişir)", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Tork ve açısal momentum ilişkisi şeması.", 34)

def gezegen_hiz_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "KEPLER YÖRÜNGESİ ÇİZGİSEL HIZ SIRALAMASI", 10.5, YES)
    adimlar = ["1. Enberi (r_min)", "2. Orta Konum", "3. Enöte (r_max)"]
    for i, a in enumerate(adimlar):
        x = 18 + i * 112
        ic += kutu(x, 42, 102, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 51, 70, a, 9.0, LAC)
        if i < 2:
            ic += yazi(x + 107, 70, "&gt;", 12.0, TUR)
    return svg(360, 110, ic, "Gezegen hız sıralaması şeması.", 34)

def sag_el_kurali_vektor_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "SAĞ EL KURALI VE AÇISAL VEKTÖR YÖNÜ", 10.5, MAVI)
    ic += yazi(180, 52, "Saat yönünün tersine dönme → Başparmak dışarıyı gösterir (⊙)", 9.8, LAC)
    ic += yazi(180, 76, "Açısal momentum vektörü L ve açısal hız ω aynı doğrultudadır", 9.2, MAVI, ince=True)
    return svg(360, 110, ic, "Sağ el kuralı vektör panosu.", 34)

def dort_formul_durum_karti():
    kartlar = [
        ('1. L = I·ω', 'Katı Dönen Cisim', MAVI, MAVI_A),
        ('2. L = mvr', 'Noktasal Parçacık', YES, YES_A),
        ('3. τ = ΔL/Δt', 'Net Dış Tork', TUR, TUR_A),
        ('4. I₁ω₁ = I₂ω₂', 'Korunum Şartı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört formül durum kartı.", 34)

def sifre_moment_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "DÖNME DİNAMİĞİ KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "MERKEZ · ORBİT · MAKSİMUM · EYLEMSİZLİK · NEWTON · TORK", 9.2, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli dönme direnci terimini (6 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre moment kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_acisal_buyukluk_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = acisal_korunum_patenci_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = acisal_momentum_hesap_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = tork_momentum_iliskisi_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = gezegen_hiz_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = sag_el_kurali_vektor_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_formul_durum_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_moment_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True