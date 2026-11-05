"""12. sınıf Edebiyat 4. hafta (Küçürek Hikâye ve Postmodernizm) çalışma kâğıdı görselleri."""

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

def dort_kucurek_terimi_karti():
    kartlar = [
        ('1. Küçürek', 'Minimal · Yoğun Anlam', MAVI, MAVI_A),
        ('2. Üstkurmaca', 'Kurmaca Bilinci', YES, YES_A),
        ('3. Metinlerarası', 'Alıntı &amp; Gönderme', TUR, TUR_A),
        ('4. Pastiş', 'Üslup Taklidi', MOR, MOR_A),
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
    return svg(360, 110, ic, "Dört küçürek anlatım terimi kartı.", 34)

def kucurek_yapi_panosu():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, "KÜÇÜREK (MİNİMAL) HİKÂYE YAPI NİTELİĞİ", 10.5, CAM)
    ic += kutu(20, 36, 150, 58, YES_A, YES)
    ic += yazi(95, 54, "Kelime Ekonomisi", 10.0, YES)
    ic += yazi(95, 74, "Gereksiz betimlemeler atılır", 8.8, LAC, ince=True)
    ic += kutu(190, 36, 150, 58, MOR_A, MOR)
    ic += yazi(265, 54, "Okurun Tamamlaması", 10.0, MOR)
    ic += yazi(265, 74, "Anlam boşlukları zihinde kurulur", 8.8, LAC, ince=True)
    return svg(360, 110, ic, "Küçürek hikâye yapı panosu.", 34)

def ferit_edgu_dogu_oykuleri_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, "FERİT EDGÜ VE DOĞU ÖYKÜLERİ", 10.5, YES)
    ic += yazi(180, 52, "Doğu Öyküleri · İşte Deniz Maria · Çığlık (1976)", 10.0, LAC)
    ic += yazi(180, 76, "Türk edebiyatında minimal hikâyenin kurucu ve dönüştürücü ustası", 9.2, TUR, ince=True)
    return svg(360, 110, ic, "Ferit Edgü minimal hikâye panosu.", 34)

def minimal_klasik_karsilastirma_semasi():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "MİNİMAL VE KLASİK HİKÂYE KARŞILAŞTIRMASI", 10.5, TUR)
    ic += kutu(20, 38, 145, 54, MAVI_A, MAVI)
    ic += yazi(92, 56, "Klasik Hikâye", 10.0, MAVI)
    ic += yazi(92, 74, "Geniş olay &amp; detaylı mekân", 9.0, LAC, ince=True)
    ic += kutu(195, 38, 145, 54, YES_A, YES)
    ic += yazi(267, 56, "Küçürek Hikâye", 10.0, YES)
    ic += yazi(267, 74, "Bir anlık şok &amp; açık uçlu son", 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Minimal ve klasik hikâye şeması.", 34)

def cozumleme_siralamasi():
    ic = kutu(6, 6, 348, 98, MAVI_A, MAVI)
    ic += yazi(180, 22, "KÜÇÜREK HİKÂYE ÇÖZÜMLEME AŞAMALARI", 10.5, MAVI)
    adimlar = ["1. Vurucu Cümle", "2. İma &amp; Boşluk", "3. Zihinde Kurma", "4. Evrensel Yorum"]
    for i, a in enumerate(adimlar):
        x = 12 + i * 85
        ic += kutu(x, 42, 80, 48, '#ffffff', MAVI, r=4)
        ic += yazi(x + 40, 70, a, 8.6, LAC)
        if i < 3:
            ic += yazi(x + 82, 70, "→", 12.0, TUR)
    return svg(360, 110, ic, "Çözümleme aşamaları sıralaması.", 34)

def parodi_teknigi_panosu():
    ic = kutu(6, 6, 348, 98, MOR_A, MOR)
    ic += yazi(180, 24, "POSTMODERN PARODİ VE İRONİ TEKNİĞİ", 10.5, MOR)
    ic += yazi(180, 52, "Ciddi veya klasik bir metni alaycı ve mizahi yaklaşımla dönüştürme", 9.8, LAC)
    ic += yazi(180, 76, "Geleneksel kalıpları yıkarak metne çok sesli ve eleştirel boyut kazandırma", 9.2, YES, ince=True)
    return svg(360, 110, ic, "Parodi tekniği panosu.", 34)

def dort_minimalist_yazar_karti():
    kartlar = [
        ('1. Ferit Edgü', 'Doğu Öyküleri', MAVI, MAVI_A),
        ('2. N. Tosuner', 'Sarsıcı &amp; Yalın', YES, YES_A),
        ('3. Oğuz Atay', 'Üstkurmaca', TUR, TUR_A),
        ('4. Bilge Karasu', 'Kurgusal Bilgelik', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 70, alt, 9.0, LAC, ince=True)
    return svg(360, 110, ic, "Dört minimalist yazar kartı.", 34)

def sifre_kucurek_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, "MİNİMALİZM KAVRAM BULMACASI", 10.8, TUR)
    ic += yazi(180, 50, "KURMACA · ÜSLUP · ÇAĞRIŞIM · ÜSTKURMACA · RİTİM · EDGÜ · KESİT", 8.8, LAC)
    ic += yazi(180, 76, "İpuçlarını çözerek gizli kısa öykü türünü (7 harf) bulunuz.", 9.3, TUR, ince=True)
    return svg(360, 110, ic, "Şifre küçürek kavram panosu.", 34)

def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = dort_kucurek_terimi_karti()
    s[0]["en_fazla"] = 34
    s[0]["gorsel_var"] = True
    s[1]["gorsel"] = kucurek_yapi_panosu()
    s[1]["en_fazla"] = 34
    s[1]["gorsel_var"] = True
    s[2]["gorsel"] = ferit_edgu_dogu_oykuleri_panosu()
    s[2]["en_fazla"] = 34
    s[2]["gorsel_var"] = True
    s[3]["gorsel"] = minimal_klasik_karsilastirma_semasi()
    s[3]["en_fazla"] = 34
    s[3]["gorsel_var"] = True
    s[5]["gorsel"] = cozumleme_siralamasi()
    s[5]["en_fazla"] = 34
    s[5]["gorsel_var"] = True
    s[6]["gorsel"] = parodi_teknigi_panosu()
    s[6]["en_fazla"] = 34
    s[6]["gorsel_var"] = True
    s[8]["gorsel"] = dort_minimalist_yazar_karti()
    s[8]["en_fazla"] = 34
    s[8]["gorsel_var"] = True
    s[10]["gorsel"] = sifre_kucurek_panosu()
    s[10]["en_fazla"] = 34
    s[10]["gorsel_var"] = True