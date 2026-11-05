"""12. sınıf İnkılap Tarihi 3. hafta (I. Dünya Savaşı ve Cepheler) çalışma kâğıdı görselleri."""

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

def dort_cephe_turu_karti():
    kartlar = [
        ('1. Taarruz', 'Kafkas &amp; Kanal (2K)', KIR, KIR_A),
        ('2. Savunma', 'Çanakkale · Irak · Hicaz', MAVI, MAVI_A),
        ('3. Yardım', 'Galiçya · Romanya', YES, YES_A),
        ('4. Karadeniz', 'Yavuz &amp; Midilli Baskını', TUR, TUR_A),
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
    return svg(360, 110, ic, "Dört Osmanlı cephe türü kartı.", 34)

def canakkale_zafer_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "18 MART 1915 ÇANAKKALE ZAFERİ KÜRESEL ETKİSİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Boğazlar Kapatıldı", 10.0, YES)
    ic += yazi(95, 74, "Çarlık Rusyası’na yardım engellendi", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, KIR_A, KIR)
    ic += yazi(265, 54, "Bolşevik İhtilali (1917)", 10.0, KIR)
    ic += yazi(265, 74, "Savaş en az iki yıl uzadı", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Çanakkale Zaferi küresel etki panosu.", 34)

def kanal_cephesi_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "KANAL TAARRUZ CEPHESİ VE MISIR HEDEFİ", 10.5, TUR)
    ic += yazi(180, 52, "Hedef: İngiltere’nin Hindistan sömürge yolunu kesmek ve Süveyş’i almak", 9.6, LAC)
    ic += yazi(180, 76, "Çöl şartları ve lojistik yetersizlik sebebiyle taarruz sonuçsuz kaldı", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Kanal cephesi ve Mısır hedefi panosu.", 34)

def cepheler_harita_semasi():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "OSMANLI DEVLETİ’NİN SAVAŞTIĞI CEPHELER", 10.5, MOR)
    ic += kutu(20, 38, 145, 54, KIR_A, KIR)
    ic += yazi(92, 56, "Kafkas Cephesi", 10.0, KIR)
    ic += yazi(92, 74, "Toprak kazanılan tek cephe", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Çanakkale &amp; Irak", 10.0, YES)
    ic += yazi(267, 74, "Destansı savunma zaferleri", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Osmanlı cepheler haritası şeması.", 34)

def savas_kronolojisi_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "BİRİNCİ DÜNYA SAVAŞI KRONOLOJİSİ", 10.5, MAVI)
    adimlar = ["1914 Suikast", "1914 Karadeniz", "1915 Çanakkale", "1918 Brest-Litowsk"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Savaş kronolojisi sıralama panosu.", 34)

def kafkas_mus_bitlis_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "MUSTAFA KEMAL’İN KAFKAS CEPHESİ BAŞARISI", 10.5, YES)
    ic += yazi(180, 52, "16. Kolordu Komutanı Mustafa Kemal (1916)", 10.0, LAC)
    ic += yazi(180, 76, "Muş ve Bitlis Rus işgalinden geri alındı; Generalliğe terfi etti", 9.4, YES, ince=True)
    return svg(360, 110, ic, "Kafkas Muş Bitlis başarı panosu.", 34)

def dort_komutan_cephe_karti():
    kartlar = [
        ('1. M. Kemal', 'Çanakkale · Anafartalar', KIR, KIR_A),
        ('2. Halil Paşa', 'Irak · Kutül Amare', YES, YES_A),
        ('3. Fahreddin P.', 'Hicaz · Çöl Kaplanı', TUR, TUR_A),
        ('4. Cevat Paşa', '18 Mart Deniz Zaferi', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört kahraman komutan kartı.", 34)

def sifre_cephe_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "I. DÜNYA SAVAŞI KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "CİHAT · ENVER · PAZAR · HİCAZ · ELVİYE", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli askerî harp hattını (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre cephe kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_cephe_turu_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = canakkale_zafer_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = kanal_cephesi_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = cepheler_harita_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = savas_kronolojisi_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = kafkas_mus_bitlis_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_komutan_cephe_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_cephe_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True