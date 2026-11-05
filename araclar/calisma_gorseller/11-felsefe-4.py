"""11. sınıf Felsefe 4. hafta (Çevre Sorunları ve İklim Adaleti) görselleri.
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


def iklim_adaleti_kartlari():
    kartlar = [
        ("1. İklim Adaleti", "Tarihsel Kirlilik Bedeli", TUR, TUR_A),
        ("2. Gelecek Nesil", "Kuşaklararası Sorumluluk", YES, YES_A),
        ("3. İçsel Değer", "Varlığın Kendi Amacı", MAVI, MAVI_A),
        ("4. Derin Ekoloji", "Köklü Zihniyet Değişimi", MOR, MOR_A),
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
    return svg(360, 125, ic, "İklim adaleti ve etik sorumluluk kartı.", 34)


def kuresel_sorumluluk_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "KÜRESEL İKLİM ADALETİ: SALINIM VE ETKİ DENGESİZLİĞİ", 9.8, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(92, 56, "Gelişmiş Sanayi", 9.2, KIR)
    ic += yazi(92, 76, "Yüksek Karbon Salımı", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Tarihsel Kirlilik Sorumlusu", 8.2, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Kırılgan Bölgeler", 9.2, YESIL_K)
    ic += yazi(267, 76, "Düşük Karbon Salımı", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "En Ağır Kuraklık ve Sel", 8.2, TUR, ince=True)
    return svg(360, 125, ic, "Küresel iklim dengesizliği kesiti.", 34)


def kusaklararasi_hak_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "KUŞAKLARARASI ADALET VE GELECEK KUŞAKLARIN HAKKI", 9.8, YESIL_K)
    adımlar = [
        ("1. Bugünün İnsanı", "Ahlaki karar verici", 16),
        ("2. Kaynak Emaneti", "Özenli ve tasarruflu", 102),
        ("3. İklim Güvencesi", "Yıkımı sınırlandırma", 188),
        ("4. Gelecek Nesil", "Yaşanabilir temiz dünya", 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Kuşaklararası adalet zinciri.", 34)


def icsel_aracsal_diyagrami():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "ÇEVRE ETİĞİNDE DEĞER PARADİGMALARI", 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Araçsal Paradigma", 9.2, TUR)
    ic += yazi(92, 76, "Doğa madendir, tüketilir", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "İnsan merkezci çıkar", 8.4, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "İçsel Paradigma", 9.2, YESIL_K)
    ic += yazi(267, 76, "Doğa amaçtır, korunur", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Biyotik varoluş hakkı", 8.4, YES, ince=True)
    return svg(360, 125, ic, "Araçsal ve içsel paradigma şeması.", 34)


def felsefi_arguman_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "ÇEVRE POLİTİKALARININ FELSEFİ TEMELLERİ TABLOSU", 9.8, MOR)
    satirlar = [
        ("Politika İlkesi", "Felsefi Argümanı", "Etik Dayanağı", MOR),
        ("Kirleten Öder", "Zarar veren bedelini üstlenir", "Düzeltici Adalet", KIR),
        ("İklim Fonu", "Zengin ülkeler yoksula destek verir", "Dağıtıcı İklim Adaleti", YESIL_K),
        ("İhtiyat İlkesi", "Geri dönülmez riski önceden durdurma", "Hans Jonas Sorumluluğu", MAVI),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 7.8, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Çevre felsefesi ilkeleri tablosu.", 34)


def ekolojik_asim_kesiti():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, "DÜNYA LİMİT AŞIM GÜNÜ: EKOLOJİK BORÇLANMA", 9.8, KIR)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "Doğal Yenilenme", 9.2, YESIL_K)
    ic += yazi(92, 76, "Gezegenin yıllık bütçesi", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Sürdürülebilir sınır: 1 Dünya", 8.4, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(267, 56, "Aşırı Tüketim Yükü", 9.2, KIR)
    ic += yazi(267, 76, "Kaynaklar erken tükenir", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Gelecekten borç çalınır", 8.4, KIR, ince=True)
    return svg(360, 125, ic, "Limit aşım günü karşılaştırma kesiti.", 34)


def derin_ekoloji_kartlari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "ARNE NAESS: DERİN EKOLOJİ İLKELERİ", 10.0, CAM)
    kartlar = [
        ("1. Biyotik Eşitlik", "Tüm türlerin varoluş hakkı", 16),
        ("2. Sadeliğe Çağrı", "Maddi tüketimi azaltma", 102),
        ("3. Çeşitlilik", "Biyolojik zenginlik değeri", 188),
        ("4. Eylem Bilinci", "Sorumlu felsefi duruş", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", CAM)
        ic += yazi(x + 35, 54, b, 8.2, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Derin ekoloji ilkeleri kartı.", 34)


def iklim_eylem_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "SÜRDÜRÜLEBİLİR DÜNYA İÇİN FELSEFİ ADIMLAR", 10.0, YESIL_K)
    kutular = ["Farkındalık", "İklim Adaleti", "Hakkaniyet", "Biyotik Uyum"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"İlke {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, "Felsefi iklim eylem akış kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = iklim_adaleti_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = kuresel_sorumluluk_kesiti()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = kusaklararasi_hak_semasi()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = icsel_aracsal_diyagrami()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = felsefi_arguman_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = ekolojik_asim_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = derin_ekoloji_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = iklim_eylem_kutulari()
    s[10]["en_fazla"] = 34
