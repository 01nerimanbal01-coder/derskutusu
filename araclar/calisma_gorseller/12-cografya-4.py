"""12. sınıf Coğrafya 4. hafta (Bölgesel Kalkınma Projeleri) çalışma kâğıdı görselleri."""

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

def dort_proje_hedef_karti():
    kartlar = [
        ('1. GAP', 'Fırat-Dicle · Sulu Tarım', YES, YES_A),
        ('2. KOP', 'Mavi Tünel · Göksu Suyu', MAVI, MAVI_A),
        ('3. DOKAP', 'Yeşil Yol · Ekoturizm', TUR, TUR_A),
        ('4. ZBK', 'Filyos Limanı · Sanayi', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört kalkınma projesi kartı.", 34)

def gap_tarim_etki_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "GÜNEYDOĞU ANADOLU PROJESİ (GAP) TARIMSAL ETKİSİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Pamukta Türkiye Lideri", 10.0, YES)
    ic += yazi(95, 74, "Şanlıurfa ve Harran Ovası sulaması", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, "Enerji ve İstihdam", 10.0, TUR)
    ic += yazi(265, 74, "Atatürk Barajı ve sanayi dönüşümü", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "GAP tarımsal etki panosu.", 34)

def kop_mavi_tunel_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "KONYA OVASI PROJESİ (KOP) VE MAVİ TÜNEL", 10.5, MAVI)
    ic += yazi(180, 52, "Göksu Nehri Havzası → Mavi Tünel → Konya Kapalı Havzası", 10.0, LAC)
    ic += yazi(180, 76, "Yeraltı suyu çekilmesini ve obruk oluşumunu engelleme hedefi", 9.2, YES, ince=True)
    return svg(360, 110, ic, "KOP Mavi Tünel panosu.", 34)

def kalkinma_amaclar_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "BÖLGESEL KALKINMA STRATEJİLERİ", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, YES_A, YES)
    ic += yazi(92, 56, "Göçü Önleme", 10.0, YES)
    ic += yazi(92, 74, "Yerinde istihdam ve refah", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(267, 56, "Altyapı &amp; Ticaret", 10.0, MAVI)
    ic += yazi(267, 74, "Ulaşım, baraj ve limanlar", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Kalkınma amaçları şeması.", 34)

def proje_uygulama_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "BÖLGESEL KALKINMA PROJE AŞAMALARI", 10.5, YES)
    adimlar = ["1. Sorun Tespiti", "2. Planlama", "3. Altyapı İnşası", "4. İstihdam"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Proje uygulama sıralaması.", 34)

def dokap_yesil_yol_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "DOKAP VE YEŞİL YOL YAYLA TURİZMİ PROJESİ", 10.5, YES)
    ic += yazi(180, 52, "Samsun’dan Artvin’e yaylaları birbirine bağlayan doğa koridoru", 9.8, LAC)
    ic += yazi(180, 76, "Ekoturizm, organik tarım ve geleneksel el sanatlarını canlandırma", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "DOKAP Yeşil Yol panosu.", 34)

def dort_havza_eslesme_karti():
    kartlar = [
        ('1. GAP', 'Fırat &amp; Dicle', YES, YES_A),
        ('2. KOP', 'Göksu &amp; Konya', MAVI, MAVI_A),
        ('3. YHGP', 'Yeşilırmak', TUR, TUR_A),
        ('4. ZBK', 'Filyos &amp; Kıyı', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' &amp; ' in alt:
            ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört havza eşleşme kartı.", 34)

def sifre_proje_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "BÖLGESEL KALKINMA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "PAMUK · RİZE · OVA · JEOTERMAL · EKONOMİ", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli kalkınma terimini (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre proje kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_proje_hedef_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = gap_tarim_etki_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = kop_mavi_tunel_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = kalkinma_amaclar_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = proje_uygulama_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = dokap_yesil_yol_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_havza_eslesme_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_proje_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True