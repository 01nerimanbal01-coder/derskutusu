"""11. sınıf Din Kültürü 4. hafta (Özgürlük, Sorumluluk ve Kader) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kader_kavram_kartlari():
    kartlar = [
        ("1. Tevekkül", "Tedbir + Allah’a Güven", YES, YES_A),
        ("2. Ecel &amp; Ömür", "Dünya Hayatı Süresi", TUR, TUR_A),
        ("3. Helal Rızık", "Emek ve Alın Teri", MAVI, MAVI_A),
        ("4. Hür İrade", "Sorumlu Tercih Gücü", MOR, MOR_A),
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
    return svg(360, 125, ic, "Kader ve sorumluluk kavram kartları.", 34)


def dogru_tevekkul_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "İSLAM’DA DOĞRU TEVEKKÜLÜN İKİ AŞAMASI", 10.0, YESIL_K)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "1. Aşama: Tedbir", 9.2, TUR)
    ic += yazi(92, 76, "Gerekli tüm sebeplere sarılma", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Çalışma, gayret ve özen", 8.4, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "2. Aşama: Tevekkül", 9.2, YESIL_K)
    ic += yazi(267, 76, "Sonucu Allah’a havale etme", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Huzur ve teslimiyet", 8.4, YES, ince=True)
    return svg(360, 125, ic, "Doğru tevekkül basamakları şeması.", 34)


def hz_omer_tedbir_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "HZ. ÖMER: SALGIN HASTALIK VE KADER İLKESİ", 10.0, MAVI)
    ic += kutu(16, 36, 96, 70, "#ffffff", KIR)
    ic += yazi(64, 56, "Salgın Riski", 9.0, KIR)
    ic += yazi(64, 76, "Şam’da veba tehlikesi", 8.2, LAC, ince=True)
    ic += yazi(64, 92, "Karantina tedbiri", 8.2, KIR, ince=True)
    ic += kutu(132, 36, 96, 70, "#ffffff", MAVI)
    ic += yazi(180, 56, "Geri Dönüş", 9.0, MAVI)
    ic += yazi(180, 76, "İlahi hikmete uyum", 8.2, LAC, ince=True)
    ic += yazi(180, 92, "Akılcı idare", 8.2, MAVI, ince=True)
    ic += kutu(248, 36, 96, 70, "#ffffff", YES)
    ic += yazi(296, 56, "Kader Hükmü", 9.0, YESIL_K)
    ic += yazi(296, 76, "Kaderden kadere kaçış", 8.2, LAC, ince=True)
    ic += yazi(296, 92, "Bilinçli tercih", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Hz. Ömer veba ve kader şeması.", 34)


def yanlis_kader_soylemleri():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, "TOPLUMDAKİ YANLIŞ KADER ALGISININ ELEŞTİRİSİ", 9.8, KIR)
    kartlar = [
        ("Kader Mahkûmu", "Suçu kadere yükleme", 16),
        ("Kör Tesadüf", "Evrendeki ölçüyü inkâr", 102),
        ("Pasif Tembellik", "Çalışmadan rızık umma", 188),
        ("Alın Yazısı", "İradeyi yok sayma", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", KIR)
        ic += yazi(x + 35, 54, b, 8.2, KIR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{KIR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Yanlış kader söylemleri ve eleştirisi.", 34)


def kader_algilari_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "KADER VE İRADE ANLAYIŞLARININ KARŞILAŞTIRILMASI", 9.8, MOR)
    satirlar = [
        ("Görüş Adı", "İnsanın Konumu", "Ahlaki Mesuliyet", MOR),
        ("Cebriye Anlayışı", "Rüzgâr Önündeki Kuru Yaprak", "Sorumluluğu Reddetme", KIR),
        ("Doğru Ehl-i Sünnet", "Akıl ve Cüz’î İrade Sahibi", "Eylemlerinden Mesul", YESIL_K),
        ("Mutezile Yaklaşımı", "Kendi Fiilini Tamamen Yaratan", "Küllî İradeyi Sınırlama", TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(65, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Kader ekolleri karşılaştırma tablosu.", 34)


def dagci_tedbir_modeli():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "TEDBİR VE TEVEKKÜL BÜTÜNLÜĞÜ MODELİ", 10.0, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Maddi Tedbirler", 9.2, TUR)
    ic += yazi(92, 76, "Güvenlik kaskı ve ip kontrolü", 8.2, LAC, ince=True)
    ic += yazi(92, 92, "Eğitim ve fiziksel hazırlık", 8.2, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Manevi Tevekkül", 9.2, YESIL_K)
    ic += yazi(267, 76, "Huzurla yola çıkış ve dua", 8.2, LAC, ince=True)
    ic += yazi(267, 92, "Takdire rıza gösterme", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Tedbir ve tevekkül modeli şeması.", 34)


def rizik_gayret_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "RIZIK VE EMEK İLİŞKİSİ İLKELERİ", 10.0, YESIL_K)
    kartlar = [
        ("1. Helal Kazanç", "Meşru yoldan alın teri", 16),
        ("2. İsraftan Kaçış", "Nimetleri dengeli harcama", 102),
        ("3. Paylaşma", "Zekât ve infak şuuru", 188),
        ("4. Rezzak Olan", "Yegâne rızık verici Allah", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Rızık ve emek ilkeleri kartı.", 34)


def ahlaki_sorumluluk_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, "SORUMLU İNSANIN HAYAT DÖNGÜSÜ", 10.0, CAM)
    kutular = ["Bilinçli Akıl", "Hür İrade", "Sorumlu Eylem", "Hesap Bilinci"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", CAM, r=4)
        ic += yazi(x + 37, 66, f"İlke {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, CAM)
    return svg(360, 125, ic, "Ahlaki sorumluluk akış kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = kader_kavram_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = dogru_tevekkul_semasi()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = hz_omer_tedbir_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = yanlis_kader_soylemleri()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = kader_algilari_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = dagci_tedbir_modeli()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = rizik_gayret_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = ahlaki_sorumluluk_kutulari()
    s[10]["en_fazla"] = 34
