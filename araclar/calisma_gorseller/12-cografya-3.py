"""12. sınıf Coğrafya 3. hafta (Kentleşme, Göç ve Fonksiyonel Arazi) çalışma kâğıdı görselleri."""

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

def dort_sehircilik_kavrami_karti():
    kartlar = [
        ('1. Akıllı Şehir', 'Yapay Zekâ · Sensörlü Altyapı', MAVI, MAVI_A),
        ('2. Sakin Şehir', 'Cittaslow · Yerel Kimlik', YES, YES_A),
        ('3. Dikey Tarım', 'Topraksız Üretim · Gökdelen', TUR, TUR_A),
        ('4. Dönüşüm', 'Afet Direnci · Güvenli Konut', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört şehircilik kavramı kartı.", 34)

def nufus_degisim_grafigi_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "TÜRKİYE KENT VE KIR NÜFUS ORANI DEĞİŞİMİ", 10.6, CAM)
    ic += kutu(20, 36, 150, 58, KIR_A, KIR)
    ic += yazi(95, 54, "1927: %24 Kent · %76 Kır", 9.8, KIR)
    ic += yazi(95, 74, "Kırsal nüfus baskın dönem", 9.0, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, "1985: %53 Kent · %47 Kır", 9.8, YES)
    ic += yazi(265, 74, "Kent nüfusu kır nüfusunu geçti", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Türkiye kent ve kır nüfus oranı panosu.", 34)

def seferihisar_sakin_sehir_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "TÜRKİYE’NİN İLK SAKİN ŞEHRİ: SEFERİHİSAR (2009)", 10.6, YES)
    ic += yazi(180, 52, "İzmir Seferihisar · Uluslararası Cittaslow Ağı Üyesi", 10.0, LAC)
    ic += yazi(180, 76, "Geleneksel mimari, yerel üretici pazarları ve temiz enerji kullanımı", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Seferihisar sakin şehir panosu.", 34)

def arazi_kullanimi_dinamik_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "FONKSİYONEL ARAZİ KULLANIMI DİNAMİKLERİ", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, YES_A, YES)
    ic += yazi(92, 56, "Doğru Kullanım", 10.0, YES)
    ic += yazi(92, 74, "Yamaçta orman &amp; teraslama", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, KIR_A, KIR)
    ic += yazi(267, 56, "Yanlış Kullanım", 10.0, KIR)
    ic += yazi(267, 74, "Tarım ovasında sanayi tesisi", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Fonksiyonel arazi kullanımı dinamik şeması.", 34)

def kentlesme_tarihsel_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "TÜRKİYE KENTLEŞME TARİHSEL DÖNEMLERİ", 10.5, MAVI)
    adimlar = ["1927-50 Kır", "1950-80 Göç", "1985 Dönüm", "2000+ Akıllı"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 38, 70, a, 9.4, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Kentleşme tarihsel dönemler sıralama panosu.", 34)

def cittaslow_kriterleri_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "CITTASLOW (SAKİN ŞEHİR) KRİTERLERİ", 10.6, MOR)
    ic += yazi(180, 52, "Nüfus Kriteri: Nüfus 50.000 altında olmalıdır", 10.0, LAC)
    ic += yazi(180, 76, "Geleneksel mutfak, doğa koruma, el sanatları ve sakin yaşam tarzı", 9.3, YES, ince=True)
    return svg(360, 110, ic, "Cittaslow kriterleri panosu.", 34)

def dort_sakin_sehir_karti():
    kartlar = [
        ('1. Seferihisar', 'İzmir · İlk Sakin Şehir', YES, YES_A),
        ('2. Halfeti', 'Şanlıurfa · Batık Şehir', MAVI, MAVI_A),
        ('3. Akyaka', 'Muğla · Özgün Mimari', TUR, TUR_A),
        ('4. Şavşat', 'Artvin · Doğa &amp; Yayla', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:
            ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.0, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.2, LAC, ince=True)
    return svg(360, 110, ic, "Dört sakin şehir kartı.", 34)

def sifre_sehir_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "ŞEHİRCİLİK KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "ŞAVŞAT · EĞİRDİR · HALFETİ · İZMİR · RANT", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli kentsel yerleşme birimini (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre şehircilik kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_sehircilik_kavrami_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = nufus_degisim_grafigi_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = seferihisar_sakin_sehir_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = arazi_kullanimi_dinamik_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = kentlesme_tarihsel_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = cittaslow_kriterleri_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_sakin_sehir_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_sehir_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True