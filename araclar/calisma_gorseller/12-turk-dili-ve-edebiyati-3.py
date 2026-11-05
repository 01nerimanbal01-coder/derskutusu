"""12. sınıf Edebiyat 3. hafta (1960 Sonrası Hikâyecilik) çalışma kâğıdı görselleri."""

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

def dort_hikayeci_karti():
    kartlar = [
        ('1. Nezihe Meriç', 'Bozbulanık · Kadın Psikolojisi', MAVI, MAVI_A),
        ('2. Füruzan', 'Parasız Yatılı · Göç &amp; Yoksulluk', YES, YES_A),
        ('3. Oğuz Atay', 'Korkuyu Beklerken · Yabancılaşma', TUR, TUR_A),
        ('4. Bilge Karasu', 'Troyada Ölüm Vardı · Modernizm', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        if ' · ' in alt:
            ic += yazi(x + 41, 62, alt.split(' · ')[0], 8.8, LAC, ince=True)
            ic += yazi(x + 41, 78, alt.split(' · ')[1], 8.6, LAC, ince=True)
        else:
            ic += yazi(x + 41, 70, alt, 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Dört hikâye yazarı kartı.", 34)

def hikaye_yonelimleri_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "1960 SONRASI TÜRK HİKÂYESİ YÖNELİMLERİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Modernist / Postmodernist", 9.8, YES)
    ic += yazi(95, 74, "Bilinç akışı, yabancılaşma, üst kurmaca", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(265, 54, "Toplumcu &amp; Millî-Manevi", 9.8, MAVI)
    ic += yazi(265, 74, "Göç, kenar mahalle, geleneksel bağlar", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "1960 sonrası hikâye yönelimleri panosu.", 34)

def furuzan_parasiz_yatili_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "FÜRUZAN VE PARASIZ YATILI (1971)", 10.5, YES)
    ic += yazi(180, 52, "Sait Faik Hikâye Armağanı Kazanan Başyapıt", 10.0, LAC)
    ic += yazi(180, 76, "Yoksul kadınların, çocukların ve Almanya’ya işçi göçünün içten anlatımı", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Füruzan Parasız Yatılı panosu.", 34)

def edebiyat_akimlari_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "1960 SONRASI EDEBÎ ÇEŞİTLİLİK", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, MOR_A, MOR)
    ic += yazi(92, 56, "Bireyin İç Dünyası", 10.0, MOR)
    ic += yazi(92, 74, "Yalnızlık &amp; yabancılaşma", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Toplumsal Gerçeklik", 10.0, YES)
    ic += yazi(267, 74, "Almanya göçü &amp; kentleşme", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "1960 sonrası edebî çeşitlilik şeması.", 34)

def hikaye_tahlil_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "MODERNİST HİKÂYE TAHLİL AŞAMALARI", 10.5, MAVI)
    adimlar = ["1. Zaman Kurgusu", "2. İç Çatışma", "3. İmgeler", "4. İleti"]
    for i, a in enumerate(adimlar):
        x = 16 + i * 82
        ic += kutu(x, 42, 76, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 38, 70, a, 9.2, LAC)
        if i < 3:
            ic += yazi(x + 80, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Hikâye tahlil aşamaları sıralaması.", 34)

def rasim_ozdenoren_cozulme_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "RASİM ÖZDENÖREN VE ÇÖZÜLME", 10.5, MOR)
    ic += yazi(180, 52, "Çözülme ve Çok Sesli Bir Ölüm (1973)", 10.0, LAC)
    ic += yazi(180, 76, "Geleneksel değerlerle modern kent yaşamı arasındaki manevi çatışma", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Rasim Özdenören Çözülme panosu.", 34)

def dort_anlatim_teknigi_karti():
    kartlar = [
        ('1. Bilinç Akışı', 'Serbest Zihin Akışı', MAVI, MAVI_A),
        ('2. İç Monolog', 'Düzenli İç Konuşma', YES, YES_A),
        ('3. Üst Kurmaca', 'Kurmaca Bilinci', TUR, TUR_A),
        ('4. Geriye Dönüş', 'Hafıza &amp; Geçmiş', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört anlatım tekniği kartı.", 34)

def sifre_metin_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "EDEBİYAT KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "MERİÇ · EDGÜ · TOMRİS · İMGE · NESNEL", 9.6, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli edebî ürün parçasını (5 harf) bulunuz.", 9.4, TUR, ince=True)
    return svg(360, 110, ic, "Şifre metin kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_hikayeci_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = hikaye_yonelimleri_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = furuzan_parasiz_yatili_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = edebiyat_akimlari_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = hikaye_tahlil_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = rasim_ozdenoren_cozulme_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_anlatim_teknigi_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_metin_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True