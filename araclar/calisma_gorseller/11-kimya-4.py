"""11. sınıf Kimya 4. hafta (Bağ Enerjileriyle Tepkime Entalpisi) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def bag_enerjisi_kartlari():
    kartlar = [
        ("1. Kırılan Bağ", "Endotermik (+ΔH)", TUR, TUR_A),
        ("2. Oluşan Bağ", "Ekzotermik (-ΔH)", YES, YES_A),
        ("3. Net Entalpi", "ΣE_kırılan - ΣE_oluşan", MAVI, MAVI_A),
        ("4. Gaz Fazı Şartı", "Standart Bağ Değerleri", MOR, MOR_A),
    ]
    ic = ""
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, "#ffffff")
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, "Bağ enerjisi ve termokimya kartı.", 34)


def hcl_tepkime_modeli():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "H₂ + Cl₂ → 2HCl TEPKİMESİ ENTALPİ HESABI", 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Kırılan Bağlar (Girenler)", 8.8, TUR)
    ic += yazi(92, 76, "H-H: 436 + Cl-Cl: 242", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Toplam = +678 kJ", 8.6, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Oluşan Bağlar (Ürünler)", 8.8, YESIL_K)
    ic += yazi(267, 76, "2 x (H-Cl: 431) = 862", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "ΔH = 678 - 862 = -184 kJ", 8.6, YES, ince=True)
    return svg(360, 125, ic, "HCl oluşum entalpisi hesabı şeması.", 34)


def bag_kirilma_olusma_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "KİMYASAL BAĞ KOPMASI VE OLUŞUMU ENERJİSİ", 10.0, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Bağ Kopması", 9.2, TUR)
    ic += yazi(92, 76, "Isı Alır (Endotermik)", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Atomlar Serbest Kalır", 8.2, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Bağ Oluşumu", 9.2, YESIL_K)
    ic += yazi(267, 76, "Isı Verir (Ekzotermik)", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Daha Kararlı Düşük Enerji", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Bağ kopması ve oluşumu karşılaştırma kesiti.", 34)


def kovalent_bag_turleri():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "KARBON BAĞLARI: DERECELERİ VE ENERJİLERİ", 10.0, YESIL_K)
    turler = [
        ("C-C Tekli", "347 kJ/mol (Uzun)", 16, MAVI),
        ("C=C İkili", "614 kJ/mol (Orta)", 102, TUR),
        ("C≡C Üçlü", "839 kJ/mol (Kısa)", 188, YES),
        ("Kural", "Bağ sayısı arttıkça sağlamlaşır", 274, MOR),
    ]
    for b, a, x, r in turler:
        ic += kutu(x, 36, 70, 70, "#ffffff", r)
        ic += yazi(x + 35, 54, b, 8.2, r)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Karbon bağ dereceleri ve enerjileri kartı.", 34)


def bag_enerjisi_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "STANDART ORTALAMA BAĞ ENERJİLERİ (kJ/mol) TABLOSU", 9.8, MOR)
    satirlar = [
        ("Bağ Türü", "Enerji (kJ/mol)", "Bağ Türü", "Enerji (kJ/mol)", MOR),
        ("H - H", "436", "C - H", "414", MAVI),
        ("Cl - Cl", "242", "C = O", "745", YESIL_K),
        ("N ≡ N", "946 (Çok Sağlam)", "O - H", "464", TUR),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.0, r)
        ic += yazi(125, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(210, y + 13, k3, 8.0, LAC, ince=(i > 0))
        ic += yazi(295, y + 13, k4, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Standart bağ enerjileri tablosu.", 34)


def azot_molekul_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "AZOT MOLEKÜLÜ (N₂) VE ÜÇLÜ BAĞ KARARLILIĞI", 10.0, CAM)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "N ≡ N Üçlü Bağı", 9.2, YESIL_K)
    ic += yazi(92, 76, "Bağ Enerjisi: 946 kJ/mol", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Son Derece Sağlam Yapı", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", CAM)
    ic += yazi(267, 56, "Kimyasal Asallık", 9.2, CAM)
    ic += yazi(267, 76, "Oda şartlarında tepkimesiz", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Atmosferin %78 koruyucusu", 8.2, CAM, ince=True)
    return svg(360, 125, ic, "Azot üçlü bağ sağlamlığı kesiti.", 34)


def gaz_fazi_sarti_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "BAĞ ENERJİSİ HESAPLAMA KRİTERLERİ", 10.0, TUR)
    kartlar = [
        ("1. Gaz Fazı", "Tüm tanecikler gaz olmalı", 16),
        ("2. Lewis Yapısı", "Tüm kovalent bağlar sayılır", 102),
        ("3. Katsayı Çarpımı", "Mol sayılarıyla çarpılır", 188),
        ("4. Fark Formülü", "Kırılan - Oluşan = ΔH", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Bağ enerjisi hesaplama kriterleri kartı.", 34)


def termokimya_akis_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "BAĞ ENERJİSİNDEN ENTALPİYE ÇÖZÜM ADIMLARI", 10.0, YESIL_K)
    kutular = ["Lewis Yazımı", "Kırılan Bağlar", "Oluşan Bağlar", "ΔH Farkı"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"Adım {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, "Termokimya çözüm adımları akış kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = bag_enerjisi_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = hcl_tepkime_modeli()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = bag_kirilma_olusma_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = kovalent_bag_turleri()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = bag_enerjisi_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = azot_molekul_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = gaz_fazi_sarti_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = termokimya_akis_kutulari()
    s[10]["en_fazla"] = 34
