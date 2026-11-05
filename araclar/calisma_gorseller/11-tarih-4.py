"""11. sınıf Tarih 4. hafta (1683-1789 Mücadelelerinin Çok Yönlü Sonuçları) görselleri.
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


def antlasma_sonuc_kartlari():
    kartlar = [
        ("1. Kerden (1746)", "İran ile Sınır Korundu", YES, YES_A),
        ("2. Çeşme (1770)", "Donanmanın Yanması", KIR, KIR_A),
        ("3. Kaynarca (1774)", "Kırım &amp; Tazminat", MOR, MOR_A),
        ("4. Esham Sistemi", "İlk İç Borçlanma", TUR, TUR_A),
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
    return svg(360, 125, ic, "18. yüzyıl antlaşma sonuçları kartı.", 34)


def dogu_bati_cephe_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "18. YÜZYIL CEPHE KARŞILAŞTIRMASI: DOĞU VE BATI", 9.8, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "Doğu Cephesi (İran)", 9.2, YESIL_K)
    ic += yazi(92, 76, "Kasr-ı Şirin sınırları", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "1746 Kerden ile kalıcı denge", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", KIR)
    ic += yazi(267, 56, "Batı &amp; Kuzey Cephesi", 9.2, KIR)
    ic += yazi(267, 76, "Avusturya ve Rusya ittifakı", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Toprak kayıpları &amp; göçler", 8.2, KIR, ince=True)
    return svg(360, 125, ic, "Doğu ve Batı cepheleri karşılaştırma kesiti.", 34)


def cesme_baskini_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, "1770 ÇEŞME BASKINI VE DENİZ HAKİMİYETİ KAYBI", 9.8, KIR)
    adımlar = [
        ("1. Baltık Çıkışı", "Rus filosu yola çıkar", 16),
        ("2. Cebelitarık", "Akdeniz’e sızma", 102),
        ("3. Çeşme Limanı", "Osmanlı filosu yakılır", 188),
        ("4. Ağır Bunalım", "Kaynarca’ya giden yol", 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", KIR)
        ic += yazi(x + 35, 54, b, 8.2, KIR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{KIR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Çeşme baskını aşamaları şeması.", 34)


def esham_maliye_modeli():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "OSMANLI MALİYESİ VE İÇ BORÇLANMA (ESHAM)", 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Bütçe Açıkları", 9.2, TUR)
    ic += yazi(92, 76, "Savaş giderleri &amp; tazminat", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Hazine gelirlerinin erimesi", 8.2, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "Esham Senetleri", 9.2, YESIL_K)
    ic += yazi(267, 76, "Gelir paylarının satışı", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "İlk iç borçlanma adımı", 8.2, YES, ince=True)
    return svg(360, 125, ic, "Esham sistemi maliye şeması.", 34)


def toplum_goc_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "18. YÜZYIL TOPLUMSAL VE DEMOGRAFİK DÖNÜŞÜM TABLOSU", 9.8, MOR)
    satirlar = [
        ("Olay / Bölge", "Demografik Etki", "Toplumsal Sonuç", MOR),
        ("Kırım’ın Kaybı", "Yüz binlerce muhacir göçü", "Anadolu’da Müslüman Nüfus Artışı", KIR),
        ("Balkan Savaşları", "Sınır boyu nüfus çekilmesi", "Kentsel İskân ve Barınma Krizi", TUR),
        ("İç Borçlanma", "Esham senetleri ihracı", "Galata bankerlerinin güçlenmesi", MAVI),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 7.8, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Demografik dönüşüm tablosu.", 34)


def denge_siyaseti_diyagrami():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "OSMANLI DENGE SİYASETİ: DEVLETLER ARASI REKABET", 9.8, YESIL_K)
    ic += kutu(20, 36, 145, 70, "#ffffff", MAVI)
    ic += yazi(92, 56, "Doğu Bloku Baskısı", 9.2, MAVI)
    ic += yazi(92, 76, "Rusya’nın sıcak deniz emeli", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Balkanlar ve Boğazlar tehdidi", 8.2, MAVI, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(267, 56, "Batı Bloku Desteği", 9.2, TUR)
    ic += yazi(267, 76, "İngiltere ve Fransa dengesi", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Statükoyu koruma ittifakı", 8.2, TUR, ince=True)
    return svg(360, 125, ic, "Denge siyaseti güçler dengesi kesiti.", 34)


def kırım_surec_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "KIRIM’IN KAYBEDİLME EVRELERİ (1774-1783)", 10.0, TUR)
    kartlar = [
        ("1. Kaynarca (1774)", "Kırım bağımsız oldu", 16),
        ("2. Aynalıkavak (1779)", "Şahin Giray onaylandı", 102),
        ("3. İlhak (1783)", "Rusya Kırım’ı ilhak etti", 188),
        ("4. Yaş (1792)", "Osmanlı ilhakı tanıdı", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Kırım elden çıkış kronolojisi kartı.", 34)


def tarihsel_miras_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, "18. YÜZYIL DÖNÜŞÜM DİNAMİKLERİ", 10.0, CAM)
    kutular = ["Daimi Elçilik", "Askeri Islahat", "İç Borçlanma", "Denge Siyaseti"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", CAM, r=4)
        ic += yazi(x + 37, 66, f"Faz {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, CAM)
    return svg(360, 125, ic, "Tarihsel dönüşüm dinamikleri kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = antlasma_sonuc_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = dogu_bati_cephe_kesiti()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = cesme_baskini_semasi()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = esham_maliye_modeli()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = toplum_goc_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = denge_siyaseti_diyagrami()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = kırım_surec_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = tarihsel_miras_kutulari()
    s[10]["en_fazla"] = 34
