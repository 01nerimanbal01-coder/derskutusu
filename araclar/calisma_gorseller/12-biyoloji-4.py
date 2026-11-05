"""12. sınıf Biyoloji 4. hafta (RNA Çeşitleri ve Karşılaştırma) çalışma kâğıdı görselleri."""

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

def dort_rna_bileseni_karti():
    kartlar = [
        ('1. mRNA', 'Kodon Şifresi · Mesaj Taşıma', MAVI, MAVI_A),
        ('2. tRNA', 'Antikodon · Amino Asit', YES, YES_A),
        ('3. rRNA', 'Ribozom Yapısı · Kataliz', TUR, TUR_A),
        ('4. Riboz', '5C Şeker · OH Grubu', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört RNA bileşeni kartı.", 34)

def trna_yonca_modeli_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "TAŞIYICI RNA (tRNA) YONCA YAPRAĞI MODELİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Antikodon Bölgesi", 10.0, YES)
    ic += yazi(95, 74, "mRNA kodonunu tamamlar", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, TUR_A, TUR)
    ic += yazi(265, 54, "Amino Asit Ucu (3')", 10.0, TUR)
    ic += yazi(265, 74, "Katlanmalarda H-bağları vardır", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "tRNA yonca yaprağı modeli panosu.", 34)

def mrna_kodon_hesap_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "mRNA KODON HESAPLAMA VERİLERİ", 10.5, TUR)
    ic += yazi(90, 56, "Toplam Nükleotit = 300", 9.8, LAC)
    ic += yazi(90, 76, "Kodon Başına = 3 Nükleotit", 9.6, MAVI)
    ic += yazi(270, 56, "Toplam Kodon = 300 / 3", 9.8, YES)
    ic += yazi(270, 76, "= 100 Kodon", 10.2, YES)
    return svg(360, 110, ic, "mRNA kodon hesaplama panosu.", 34)

def rna_metabolizma_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "RNA METABOLİK ÖZELLİKLERİ VE SENTEZİ", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Transkripsiyon", 10.0, MAVI)
    ic += yazi(92, 74, "DNA’dan RNA Polimerazla", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Tekrar Kullanım", 10.0, YES)
    ic += yazi(267, 74, "Yıkılmadan defalarca okunur", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "RNA metabolizma şeması.", 34)

def mrna_sentez_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "mRNA SENTEZ VE ÇIKIŞ BASAMAKLARI", 10.5, MAVI)
    adimlar = ["1. Gen Açılır", "2. Transkripsiyon", "3. Çekirdek Çıkış", "4. Ribozom Bağ"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "mRNA sentez basamakları sıralaması.", 34)

def rna_oran_dagilim_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "HÜCREDEKİ RNA ÇEŞİTLERİNİN DAĞILIMI", 10.5, YES)
    ic += yazi(180, 52, "rRNA: %80 (En yüksek)  ·  tRNA: %15  ·  mRNA: %5", 10.0, LAC)
    ic += yazi(180, 76, "Ribozom organelinin temel yapısal ve katalitik çekirdeğidir", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "RNA çeşitleri oran panosu.", 34)

def dort_kod_terimi_karti():
    kartlar = [
        ('1. Kodon', 'mRNA Üçlüsü', MAVI, MAVI_A),
        ('2. Antikodon', 'tRNA Üçlüsü', YES, YES_A),
        ('3. Genetik Kod', 'DNA Üçlüsü', TUR, TUR_A),
        ('4. Transkripsiyon', 'RNA Üretimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört genetik kod terimi kartı.", 34)

def sifre_riboz_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "RNA KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "RİBOZOM · İPLİK · BAZ · ORGANEL · ZİNCİR", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli pentoz şekerini (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre riboz kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_rna_bileseni_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = trna_yonca_modeli_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = mrna_kodon_hesap_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = rna_metabolizma_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = mrna_sentez_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = rna_oran_dagilim_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_kod_terimi_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_riboz_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True