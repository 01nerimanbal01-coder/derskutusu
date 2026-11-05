"""12. sınıf Biyoloji 3. hafta (DNA Yapısı ve Özellikleri) çalışma kâğıdı görselleri."""

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

def dort_nukleik_bileseni_karti():
    kartlar = [
        ('1. Pürin Bazı', 'Adenin &amp; Guanin · Çift Halka', MAVI, MAVI_A),
        ('2. Pirimidin', 'Sitozin &amp; Timin · Tek Halka', YES, YES_A),
        ('3. Deoksiriboz', '5 Karbonlu Pentoz Şekeri', TUR, TUR_A),
        ('4. Fosfodiester', 'Omurga Bağı · 3-5 Hattı', MOR, MOR_A),
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
        elif ' &amp; ' in alt:
            ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.0, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' &amp; ')[1], 8.8, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört nükleik asit yapısal bileşeni kartı.", 34)

def watson_crick_sarmal_modeli():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "WATSON-CRICK DNA ÇİFT SARMAL MODELİ", 10.6, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "5 → 3 İpliği", 10.0, YES)
    ic += yazi(95, 74, "A = T (İkili H-Bağı)", 9.2, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(265, 54, "3 → 5 İpliği (Antiparalel)", 10.0, MAVI)
    ic += yazi(265, 74, "G ≡ C (Üçlü H-Bağı)", 9.2, LAC, ince=True)
    return svg(360, 110, ic, "Watson-Crick DNA çift sarmal modeli şeması.", 34)

def dna_nukleotit_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "DNA NÜKLEOTİT HESAPLAMA VERİLERİ", 10.6, TUR)
    ic += yazi(90, 56, "Toplam Nükleotit = 1200", 9.8, LAC)
    ic += yazi(90, 76, "Guanin (G) = 400", 9.6, KIR)
    ic += yazi(270, 56, "Sitozin (C) = 400", 9.6, KIR)
    ic += yazi(270, 76, "Adenin + Timin = 400", 9.6, YES)
    return svg(360, 110, ic, "DNA nükleotit nicel hesaplama veri panosu.", 34)

def dna_kimyasal_dinamik_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "DNA KİMYASAL DİNAMİKLERİ VE BAĞ YAPILARI", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Pürin = Pirimidin", 10.0, MAVI)
    ic += yazi(92, 74, "A + G = T + C", 9.2, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, KIR_A, KIR)
    ic += yazi(267, 56, "G ≡ C Zenginliği", 10.0, KIR)
    ic += yazi(267, 74, "Yüksek Isı Direnci", 9.2, LAC, ince=True)
    return svg(360, 110, ic, "DNA kimyasal dinamikleri ve bağ şeması.", 34)

def nukleik_organizasyon_siralamasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 22, "GENETİK MATERYAL YAPISAL BASAMAKLARI", 10.5, YES)
    adimlar = ["1. Baz", "2. Nükleozit", "3. Nükleotit", "4. Polinükleotit"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', YES, r=4)
        ic += yazi(x + 38, 70, a, 9.4, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Nükleik organizasyon hiyerarşik sıralama şeması.", 34)

def chargaff_kurallari_panosu():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 24, "CHARGAFF BAZ EŞLEŞME KURALLARI", 10.6, MAVI)
    ic += yazi(180, 52, "A / T = 1   ve   G / C = 1", 10.2, LAC)
    ic += yazi(180, 76, "(A + G) / (T + C) = 1 (Pürin / Pirimidin = 1)", 9.5, MAVI)
    return svg(360, 110, ic, "Chargaff kuralları oran panosu.", 34)

def dort_baz_ozellik_karti():
    kartlar = [
        ('Adenin (A)', 'Pürin · İkili Bağ', MAVI, MAVI_A),
        ('Guanin (G)', 'Pürin · Üçlü Bağ', YES, YES_A),
        ('Timin (T)', 'Pirimidin · DNA', TUR, TUR_A),
        ('Sitozin (C)', 'Pirimidin · Ortak', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört bazın özellikleri kartı.", 34)

def sifre_pentoz_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "NÜKLEİK ASİT KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "PÜRİN · ESTER · NÜKLEOTİT · TİMİN · OKAZAKİ · ZİNCİR", 9.4, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli beş karbonlu şekeri (6 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre nükleik asit kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_nukleik_bileseni_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = watson_crick_sarmal_modeli()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = dna_nukleotit_hesap_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = dna_kimyasal_dinamik_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = nukleik_organizasyon_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = chargaff_kurallari_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_baz_ozellik_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_pentoz_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True