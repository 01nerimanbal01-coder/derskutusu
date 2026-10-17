# -*- coding: utf-8 -*-
import html as _html

class Renk:
    MAVI = ("#1E3A8A", "#60A5FA", "#2563EB")
    YESIL = ("#064E3B", "#34D399", "#059669")
    TURUNCU = ("#431407", "#FB923C", "#EA580C")
    MOR = ("#3B0764", "#C084FC", "#7C3AED")
    SARI = ("#422006", "#FDE047", "#CA8A04")

class Primitifler:
    def arkaplan_16_9(self, renk="#0F172A"):
        return f"""<rect width="1200" height="675" rx="18" fill="{renk}"/>"""
    def baslik_16_9(self, baslik, alt=""):
        b = _html.escape(str(baslik))
        a = _html.escape(str(alt))
        return (f"""<rect x="40" y="24" width="1120" height="84" rx="14" fill="#1E293B" stroke="#334155" stroke-width="2"/>"""
                f"""<text x="600" y="58" text-anchor="middle" font-size="22" font-weight="800" fill="#F8FAFC">{b}</text>"""
                f"""<text x="600" y="88" text-anchor="middle" font-size="15" fill="#94A3B8">{a}</text>""")
    def panel(self, x, y, w, h, baslik, renk):
        bg, stroke, hdr = renk if isinstance(renk, tuple) else ("#1E293B", renk, renk)
        b = _html.escape(str(baslik))
        return (f"""<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#1E293B" stroke="{stroke}" stroke-width="2.5"/>"""
                f"""<rect x="{x}" y="{y}" width="{w}" height="42" rx="14" fill="{hdr}"/>"""
                f"""<text x="{x + w/2}" y="{y + 27}" text-anchor="middle" font-size="16" font-weight="700" fill="#FFFFFF">{b}</text>""")
    def etiket(self, x, y, w, h, metin, renk):
        bg, stroke, hdr = renk if isinstance(renk, tuple) else ("#1E293B", renk, renk)
        satirlar = str(metin).split("\n")
        n = len(satirlar)
        txt = []
        bas_y = y + (h - (n - 1) * 20) / 2 + 5
        for i, st in enumerate(satirlar):
            s_esc = _html.escape(st)
            fw = "700" if i == 0 else "500"
            fl = "#F8FAFC" if i == 0 else "#E2E8F0"
            txt.append(f"""<text x="{x + w/2}" y="{bas_y + i*20}" text-anchor="middle" font-size="14.5" font-weight="{fw}" fill="{fl}">{s_esc}</text>""")
        return f"""<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{stroke}" stroke-width="2"/>""" + "".join(txt)
    def kutu(self, x, y, w, h, fill, stroke, sw=2, rx=8):
        return f"""<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>"""
    def daire(self, cx, cy, r, fill, stroke="#FFFFFF", sw=2):
        return f"""<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>"""
    def dogru(self, x1, y1, x2, y2, stroke="#F8FAFC", sw=3):
        return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>"""
    def kesikli_dogru(self, x1, y1, x2, y2, stroke="#94A3B8", sw=2):
        return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-dasharray="6,6" stroke-linecap="round"/>"""
    def ok(self, x1, y1, x2, y2, stroke="#FDE047", sw=3):
        return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>"""
    def cokgen(self, noktalar, fill, stroke, sw=2):
        pts = " ".join(f"{x},{y}" for x, y in noktalar)
        return f"""<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>"""
    def metin(self, x, y, metin, punto=15, renk="#F8FAFC", hiza="middle", kalin=False):
        satirlar = str(metin).split("\n")
        fw = "700" if kalin else "500"
        out = []
        for i, st in enumerate(satirlar):
            s_esc = _html.escape(st)
            out.append(f"""<text x="{x}" y="{y + i*(punto+5)}" text-anchor="{hiza}" font-size="{punto}" font-weight="{fw}" fill="{renk}">{s_esc}</text>""")
        return "".join(out)
    def alt_serit(self, metin):
        m = _html.escape(str(metin))
        return (f"""<rect x="40" y="595" width="1120" height="54" rx="12" fill="#1E293B" stroke="#475569" stroke-width="1.5"/>"""
                f"""<text x="600" y="628" text-anchor="middle" font-size="15.5" font-weight="700" fill="#FDE047">{m}</text>""")

def kart_16_9(parcalar):
    ic = "".join(parcalar)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="100%" style="max-width:760px;height:auto;display:block;margin:12px auto;font-family:'Segoe UI',system-ui,sans-serif;">{ic}</svg>"""



def gorsel_1():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("MEKÂNSAL VERİ TÜRLERİ: NOKTA, ÇİZGİ VE ALAN (POLİGON)", "CBS Ortamında Coğrafi Unsur ve Verilerin Vektörel Temsili"),
        p.panel(55, 130, 345, 440, "1. Noktasal (Point) Veri", Renk.MAVI),
        p.daire(155, 235, 10, "#60A5FA", "#F8FAFC", 2),
        p.daire(255, 215, 10, "#FDE047", "#F8FAFC", 2),
        p.daire(215, 295, 10, "#34D399", "#F8FAFC", 2),
        p.daire(300, 280, 10, "#F87171", "#F8FAFC", 2),
        p.etiket(80, 345, 295, 65, "Tek bir (X, Y) koordinat çifti ile\ngösterilen konumsal verilerdir.", Renk.MAVI),
        p.metin(227, 445, "Örnekler:", 15, "#FDE047", "middle", True),
        p.metin(227, 480, "• Okul, hastane, eczane, müze\n• Deprem merkez üssü, kuyu\n• Dağ zirvesi, otobüs durağı", 14, "#E2E8F0", "middle", False),
        p.panel(425, 130, 345, 440, "2. Çizgisel (Line) Veri", Renk.YESIL),
        p.dogru(475, 295, 555, 225, "#34D399", 5),
        p.dogru(555, 225, 645, 275, "#34D399", 5),
        p.dogru(645, 275, 720, 210, "#34D399", 5),
        p.daire(475, 295, 6, "#FDE047", "#0F172A", 2),
        p.daire(555, 225, 6, "#FDE047", "#0F172A", 2),
        p.daire(645, 275, 6, "#FDE047", "#0F172A", 2),
        p.daire(720, 210, 6, "#FDE047", "#0F172A", 2),
        p.etiket(450, 345, 295, 65, "Ardışık noktaların birleşmesiyle\noluşan uzunluk/ağ verileridir.", Renk.YESIL),
        p.metin(597, 445, "Örnekler:", 15, "#FDE047", "middle", True),
        p.metin(597, 480, "• Akarsular, kara ve demir yolları\n• Fay hatları, boru ve enerji hatları\n• Ülke ve il idari sınır çizgileri", 14, "#E2E8F0", "middle", False),
        p.panel(795, 130, 350, 440, "3. Alansal (Poligon) Veri", Renk.TURUNCU),
        p.cokgen([(865, 220), (985, 195), (1075, 255), (1030, 315), (890, 305)], "#7C2D12", "#FB923C", 3),
        p.etiket(820, 345, 300, 65, "Başlangıç ve bitiş noktası birleşen\nkapalı yüzey/bölge verileridir.", Renk.TURUNCU),
        p.metin(970, 445, "Örnekler:", 15, "#FDE047", "middle", True),
        p.metin(970, 480, "• Göller, barajlar, orman alanları\n• Tarım arazileri, milli parklar\n• İl, ilçe ve ülke yüz ölçümleri", 14, "#E2E8F0", "middle", False),
        p.alt_serit("Haritanın ölçeğine göre aynı unsur (örneğin bir şehir) küçük ölçekte nokta, büyük ölçekte alan olarak gösterilebilir."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("ALTLIK HARİTA ÜZERİNDE MEKÂNSAL VERİ OLUŞTURMA SÜRECİ", "COĞ.10.2.2 — Harita Tasarımının Dört Temel Aşaması"),
        p.panel(55, 130, 525, 205, "1. Adım: Haritanın Amacını Belirleme", Renk.MAVI),
        p.etiket(85, 195, 465, 60, "'Bu harita neyi, kime ve hangi ölçekte gösterecek?'", Renk.MAVI),
        p.metin(317, 290, "Örn: Türkiye'de deprem riskini veya okul çevresi afet toplanma\nalanlarını göstermek üzere konu ve hedef kitle seçilir.", 14, "#E2E8F0", "middle", False),
        p.panel(620, 130, 525, 205, "2. Adım: Yöntem, Veri ve Altlık Harita Seçimi", Renk.YESIL),
        p.etiket(650, 195, 465, 60, "Uygun Altlık Harita + Doğru Gösterim Tekniği", Renk.YESIL),
        p.metin(882, 290, "Konuya uygun altlık harita (fiziki, idari, uydu görüntüsü) seçilir;\nverilerin nokta, çizgi veya alan yönteminden hangisiyle işleneceği belirlenir.", 14, "#E2E8F0", "middle", False),
        p.panel(55, 365, 525, 205, "3. Adım: Verileri Harita Üzerine Aktarma ve Sembolleştirme", Renk.TURUNCU),
        p.etiket(85, 430, 465, 60, "CBS Katmanları, Renk, Sembol ve Harita Elemanları", Renk.TURUNCU),
        p.metin(317, 525, "Başlık, lejant (harita anahtarı), ölçek, yön oku ve koordinat\nağı eksiksiz eklenerek mekânsal veriler katmanlara işlenir.", 14, "#E2E8F0", "middle", False),
        p.panel(620, 365, 525, 205, "4. Adım: Mekânsal Dağılışı ve İlişkileri Yorumlama", Renk.MOR),
        p.etiket(650, 430, 465, 60, "Neden-Sonuç, Kümelenme ve Dağılış Analizi", Renk.MOR),
        p.metin(882, 525, "Haritadaki verilerin nerede yoğunlaştığı, hangi coğrafi\nunsurlarla (yükselti, su, ulaşım) ilişkili olduğu analiz edilir.", 14, "#E2E8F0", "middle", False),
        p.alt_serit("İyi bir tematik harita; doğru altlık seçimi, anlaşılır bir lejant ve amaca uygun sembolleştirmeyle oluşturulur."),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("TEMATİK HARİTA GÖSTERİM YÖNTEMLERİ (KARTOGRAFİK TEKNİKLER)", "Nitel ve Nicel Mekânsal Verilerin Görselleştirilmesi"),
        p.panel(55, 130, 525, 210, "1. Koroplet (Dereceli Renklendirme) Haritası", Renk.MAVI),
        p.kutu(85, 195, 70, 55, "#DBEAFE", "#1E3A8A", 2, 4),
        p.kutu(165, 195, 70, 55, "#60A5FA", "#1E3A8A", 2, 4),
        p.kutu(245, 195, 70, 55, "#1D4ED8", "#F8FAFC", 2, 4),
        p.metin(335, 215, "İdari sınırlar içinde yoğunluk/oran", 14, "#FDE047", "start", True),
        p.metin(335, 240, "arttıkça renk tonu koyulaşır.", 14, "#E2E8F0", "start", False),
        p.etiket(85, 268, 465, 52, "Örn: İllere göre aritmetik nüfus yoğunluğu veya okuryazarlık oranı", Renk.MAVI),
        p.panel(620, 130, 525, 210, "2. Noktalama (Dot) ve 3. Oransal Sembol Haritası", Renk.YESIL),
        p.daire(670, 222, 10, "#34D399", "#F8FAFC", 2),
        p.daire(725, 222, 18, "#34D399", "#F8FAFC", 2),
        p.daire(795, 222, 26, "#34D399", "#F8FAFC", 2),
        p.metin(840, 215, "Veri büyüklüğüne göre daire/sembol", 14, "#FDE047", "start", True),
        p.metin(840, 240, "boyutu veya nokta sıklığı artar.", 14, "#E2E8F0", "start", False),
        p.etiket(650, 268, 465, 52, "Örn: Limanların yük hacmi (Oransal) / Tarım ürünü dağılışı (Noktalama)", Renk.YESIL),
        p.panel(55, 360, 525, 210, "4. İzoplet (Eş Değer Çizgisi) Haritası", Renk.TURUNCU),
        p.etiket(85, 420, 465, 60, "Aynı değere sahip noktaların birleştirilmesi:\nİzohips (Yükselti), İzoterm (Sıcaklık), İzobar (Basınç), İzohiyet (Yağış)", Renk.TURUNCU),
        p.metin(317, 518, "Süreklilik gösteren doğal/fiziki verilerin haritalanmasında kullanılır.", 14, "#E2E8F0", "middle", False),
        p.panel(620, 360, 525, 210, "5. Akış (Çizgisel Hareket) Haritası", Renk.MOR),
        p.ok(660, 445, 830, 445, "#FDE047", 8),
        p.ok(860, 445, 1010, 445, "#60A5FA", 3),
        p.metin(882, 505, "Çizgi kalınlığı hareketin/taşınan miktarın hacmini,\nok yönü ise hareket yönünü gösterir (Göç, ticaret, trafik akışı).", 14, "#E2E8F0", "middle", False),
        p.alt_serit("İstatistiksel bir veriyi haritaya aktarırken veri tipine en uygun kartografik yöntemi seçmek doğru okuma sağlar."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("CBS'DE MEKÂNSAL VERİ İLE ÖZNİTELİK (TABLO) VERİSİNİN EŞLEŞTİRİLMESİ", "Haritadaki Her Coğrafi Unsurun Arka Planındaki Veri Tabanı"),
        p.panel(55, 130, 490, 440, "1. Mekânsal (Geometrik) Katman", Renk.MAVI),
        p.kutu(95, 195, 410, 260, "#1E293B", "#60A5FA", 2, 10),
        p.daire(180, 265, 16, "#EF4444", "#F8FAFC", 2),
        p.metin(180, 270, "1", 13, "#F8FAFC", "middle", True),
        p.daire(310, 320, 16, "#34D399", "#F8FAFC", 2),
        p.metin(310, 325, "2", 13, "#0F172A", "middle", True),
        p.daire(410, 245, 16, "#FDE047", "#0F172A", 2),
        p.metin(410, 250, "3", 13, "#0F172A", "middle", True),
        p.metin(300, 420, "Altlık Harita Üzerinde Konumlar (X, Y)", 15, "#93C5FD", "middle", True),
        p.etiket(95, 475, 410, 65, "'Nerede?' sorusuna yanıt verir.\nNokta, çizgi ve poligon geometrisini tutar.", Renk.MAVI),
        p.panel(585, 130, 560, 440, "2. Öznitelik (Attribute) Veri Tablosu", Renk.YESIL),
        p.etiket(615, 195, 500, 52, "ID  |  Unsur Adı         |  Tür         |  Kapasite / Değer", Renk.SARI),
        p.etiket(615, 260, 500, 52, "1   |  Merkez Hastanesi  |  Sağlık      |  650 Yatak", Renk.TURUNCU),
        p.etiket(615, 325, 500, 52, "2   |  Atatürk Lisesi    |  Eğitim      |  920 Öğrenci", Renk.YESIL),
        p.etiket(615, 390, 500, 52, "3   |  Millet Parkı      |  Toplanma    |  15.000 m²", Renk.MAVI),
        p.etiket(615, 475, 500, 65, "'Ne var ve özellikleri neler?' sorusuna yanıt verir.\nSorgulama, filtreleme ve mekânsal analiz yapılmasını sağlar.", Renk.MOR),
        p.alt_serit("CBS'yi sıradan bir çizim programından ayıran temel güç, haritadaki her şeklin bir öznitelik tablosuna bağlı olmasıdır."),
    ]
    return kart_16_9(s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
