"""11. sınıf Türk Dili ve Edebiyatı 4. hafta (Sözlü İletişim Engelleri) görselleri.
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


def iletisim_engel_kartlari():
    kartlar = [
        ("1. Fiziksel", "Gürültü &amp; Akustik", KIR, KIR_A),
        ("2. Psikolojik", "Önyargı &amp; Savunma", TUR, TUR_A),
        ("3. Semantik", "Ağdalı Jargon &amp; Dil", MAVI, MAVI_A),
        ("4. Kültürel", "Zıt Jest ve Mimikler", MOR, MOR_A),
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
    return svg(360, 125, ic, "Sözlü iletişim engelleri kartı.", 34)


def dil_tarzi_karsilastirma():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "İLETİŞİM ÇATIŞMASI: SEN DİLİ VE BEN DİLİ", 10.0, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(92, 56, "Sen Dili (Yargılayıcı)", 9.2, KIR)
    ic += yazi(92, 76, "'Hep sorumsuz davranıyorsun!'", 8.2, LAC, ince=True)
    ic += yazi(92, 92, "Savunma ve direnç doğurur", 8.2, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Ben Dili (Açıklayıcı)", 9.2, YESIL_K)
    ic += yazi(267, 76, "'Gecikince endişeleniyorum.'", 8.2, LAC, ince=True)
    ic += yazi(267, 92, "Empati ve iş birliği sağlar", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Sen dili ve ben dili karşılaştırma şeması.", 34)


def semantik_mesaj_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "SEMANTİK ENGEL: ORTAK KODLAMA VE ANLAM ALANI", 9.8, MAVI)
    ic += kutu(16, 36, 96, 70, "#ffffff", TUR)
    ic += yazi(64, 56, "Ağır Jargon", 9.0, TUR)
    ic += yazi(64, 76, "Karmaşık terimler", 8.4, LAC, ince=True)
    ic += yazi(64, 92, "Mesaj anlaşılamaz", 8.2, TUR, ince=True)
    ic += kutu(132, 36, 96, 70, "#ffffff", KIR)
    ic += yazi(180, 56, "İletişim Kopar", 9.0, KIR)
    ic += yazi(180, 76, "Geri bildirim yok", 8.4, LAC, ince=True)
    ic += yazi(180, 92, "Anlamsal tıkanma", 8.2, KIR, ince=True)
    ic += kutu(248, 36, 96, 70, "#ffffff", YES)
    ic += yazi(296, 56, "Sade Dil Çözümü", 9.0, YESIL_K)
    ic += yazi(296, 76, "Açık ve yalın üslup", 8.4, LAC, ince=True)
    ic += yazi(296, 92, "Tam mutabakat", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Semantik engel çözüm kesiti.", 34)


def dinleme_turleri_diyagrami():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "DİNLEME TÜRLERİ VE NİTELİKLERİ", 10.0, YESIL_K)
    turler = [
        ("1. Etkin Dinleme", "Empatik ve tam odaklı", 16),
        ("2. Görünüşte", "Zihnen başka yerde", 102),
        ("3. Seçici Dinleme", "Sadece ilgisini duyan", 188),
        ("4. Tuzak Kurucu", "Açık aramak için dinleyen", 274),
    ]
    for b, a, x in turler:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Dinleme türleri sınıflandırma kartı.", 34)


def iletisim_ogeleri_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "SÖZLÜ İLETİŞİM SÜRECİ BİLEŞENLERİ TABLOSU", 9.8, MOR)
    satirlar = [
        ("Öğe Adı", "İletişimdeki Görevi", "Başarı Kriteri", MOR),
        ("Gönderici (Kaynak)", "Mesajı kodlayan taraf", "Açık ve anlaşılır ifade", MAVI),
        ("Kanal (Araç)", "Mesajın iletildiği ortam", "Parazit ve gürültüsüz ortam", YESIL_K),
        ("Dönüt (Geri Bildirim)", "Alıcının yanıt ve tepkisi", "Doğrulayıcı ve yapıcı yansıtma", TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 7.8, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, "İletişim süreci bileşenleri tablosu.", 34)


def beden_dili_ipucu_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "BEDEN DİLİ: AÇIK VE KAPALI İLETİŞİM DÖNGÜSÜ", 10.0, CAM)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "Açık Beden Dili", 9.2, YESIL_K)
    ic += yazi(92, 76, "Doğal göz teması &amp; tebessüm", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Kolları serbest bırakma", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(267, 56, "Kapalı Beden Dili", 9.2, KIR)
    ic += yazi(267, 76, "Göz kaçırma &amp; kollar kavuşuk", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Savunmacı ve çekingen duruş", 8.2, KIR, ince=True)
    return svg(360, 125, ic, "Beden dili açık ve kapalı duruş kesiti.", 34)


def drama_cozumleme_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "İLETİŞİM DRAMASI ÇÖZÜMLEME KRİTERLERİ", 10.0, TUR)
    kartlar = [
        ("1. Mekân &amp; Rol", "Karakterlerin konumu", 16),
        ("2. Çatışma Noktası", "Engelin doğduğu an", 102),
        ("3. Çözüm Dili", "Ben diliyle uzlaşma", 188),
        ("4. Ortak Karar", "Etkin dinleme neticesi", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Drama çözümleme basamakları kartı.", 34)


def iletisim_sonuc_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "ETKİLİ VE SAĞLIKLI SÖZLÜ İLETİŞİM DÖNGÜSÜ", 10.0, YESIL_K)
    kutular = ["Etkin Dinleme", "Empatik Bakış", "Ben Dili", "Sağlam İkna"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"İlke {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, "Etkili iletişim adımları akış kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = iletisim_engel_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = dil_tarzi_karsilastirma()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = semantik_mesaj_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = dinleme_turleri_diyagrami()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = iletisim_ogeleri_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = beden_dili_ipucu_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = drama_cozumleme_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = iletisim_sonuc_kutulari()
    s[10]["en_fazla"] = 34
