"""12. sınıf Kimya 3. hafta (Elektrotlar ve Elektrokimyasal Hücreler) çalışma kâğıdı görselleri."""

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

def dort_pil_bileseni_karti():
    kartlar = [
        ('1. Anot', 'Yükseltgenme · e⁻ Kaynağı', KIR, KIR_A),
        ('2. Katot', 'İndirgenme · e⁻ Tüketimi', YES, YES_A),
        ('3. Tuz Köprüsü', 'Yük Denkliği · İyon Göçü', MAVI, MAVI_A),
        ('4. Voltmetre', 'Potansiyel Fark · E_pil', TUR, TUR_A),
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
    return svg(360, 110, ic, "Dört pil bileşeni kartı.", 34)

def daniell_iyon_goc_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "STANDART DANIELL PİLİ İYON VE ELEKTRON GÖÇÜ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, KIR_A, KIR)
    ic += yazi(95, 54, "Anot (Zn): e⁻ Gönderir", 10.0, KIR)
    ic += yazi(95, 74, "Anyonlar (NO₃⁻) anota göç eder", 9.0, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, "Katot (Cu): e⁻ Alır", 10.0, YES)
    ic += yazi(265, 74, "Katyonlar (K⁺) katota göç eder", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Daniell pili iyon ve elektron göç panosu.", 34)

def tuz_koprusu_anyon_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "TUZ KÖPRÜSÜ VE YÜK DENKLİĞİ DİNAMİĞİ", 10.5, TUR)
    ic += yazi(180, 52, "Anyonlar Anot Kabına (-)  ·  Katyonlar Katot Kabına (+)", 10.0, LAC)
    ic += yazi(180, 76, "Çözeltilerdeki aşırı pozitif ve negatif yükler anında dengelenir", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Tuz köprüsü anyon göç panosu.", 34)

def hucre_calisma_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "GALVANİK PİL ÇALIŞMA KURALLARI", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, KIR_A, KIR)
    ic += yazi(92, 56, "Anot Elektrot", 10.0, KIR)
    ic += yazi(92, 74, "Zn → Zn²⁺ + 2e⁻ (Aşınır)", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Katot Elektrot", 10.0, YES)
    ic += yazi(267, 74, "Cu²⁺ + 2e⁻ → Cu (Toplanır)", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Galvanik pil çalışma prensibi şeması.", 34)

def pil_calisma_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "PİL REAKSİYON ZİNCİRİ BASAMAKLARI", 10.5, MAVI)
    adimlar = ["1. Zn Yükseltgenir", "2. e⁻ Tele Akar", "3. Cu²⁺ İndirgenir", "4. İyonlar Göç Eder"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.8, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Pil reaksiyon zinciri sıralama panosu.", 34)

def pil_potansiyeli_hesap_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "STANDART PİL GERİLİMİ HESABI (Zn - Ag PİLİ)", 10.5, YES)
    ic += yazi(180, 52, "E°_katot (Ag) = +0,80 V   ·   E°_anot (Zn) = -0,76 V", 10.0, LAC)
    ic += yazi(180, 76, "E°_pil = E°_katot - E°_anot = 0,80 - (-0,76) = +1,56 V", 9.6, YES)
    return svg(360, 110, ic, "Standart pil gerilimi hesap panosu.", 34)

def dort_elektrot_rol_karti():
    kartlar = [
        ('1. Anot Çözeltisi', 'Zn²⁺ Artar', KIR, KIR_A),
        ('2. Katot Çözeltisi', 'Cu²⁺ Azalır', YES, YES_A),
        ('3. Anyon Akışı', 'Anot Kabına', MAVI, MAVI_A),
        ('4. Katyon Akışı', 'Katot Kabına', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)
    return svg(360, 110, ic, "Dört elektrot rol kartı.", 34)

def sifre_hucre_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "ELEKTROKİMYA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "HÜCRE · ÜRETEÇ · CEREYAN · REDOKS · ELEKTROT", 9.4, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli kimyasal sistemi (5 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre hücre kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_pil_bileseni_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = daniell_iyon_goc_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = tuz_koprusu_anyon_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = hucre_calisma_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = pil_calisma_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = pil_potansiyeli_hesap_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_elektrot_rol_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_hucre_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True