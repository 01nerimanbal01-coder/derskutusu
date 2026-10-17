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
        p.baslik_16_9("KLOROPLASTTA FOTOSENTEZ MODELİ", "Işığa Bağımlı ve Işıktan Bağımsız Tepkimeler Arasındaki Madde Döngüsü"),
        p.panel(55, 130, 480, 440, "1. Işığa Bağımlı Tepkimeler (Tilakoit Zar / Grana)", Renk.YESIL),
        p.etiket(85, 195, 420, 52, "Girenler:  Işık Enerjisi + H₂O (Su)", Renk.MAVI),
        p.kutu(85, 265, 420, 125, "#064E3B", "#10B981", 2, 10),
        p.metin(295, 298, "• Klorofil ve ETS elemanları görev alır.", 15, "#F8FAFC", "middle", False),
        p.metin(295, 328, "• Suyun fotolizi: H₂O → 2H⁺ + 2e⁻ + ½O₂", 15, "#FDE047", "middle", True),
        p.metin(295, 358, "• Fotofosforilasyon ile ATP üretilir.", 15, "#F8FAFC", "middle", False),
        p.etiket(85, 410, 420, 52, "Atmosfere Verilen Yan Ürün:  O₂ (Oksijen)", Renk.TURUNCU),
        p.etiket(85, 480, 420, 55, "Stromaya Aktarılanlar:  ATP ve NADPH", Renk.SARI),
        p.ok(545, 310, 655, 310, "#FDE047", 4),
        p.metin(600, 292, "ATP + NADPH", 14, "#FDE047", "middle", True),
        p.ok(655, 390, 545, 390, "#60A5FA", 4),
        p.metin(600, 418, "ADP + Pᵢ + NADP⁺", 13, "#93C5FD", "middle", True),
        p.panel(665, 130, 480, 440, "2. Işıktan Bağımsız Tepkimeler (Stroma)", Renk.TURUNCU),
        p.etiket(695, 195, 420, 52, "Girenler:  CO₂ + ATP + NADPH", Renk.MAVI),
        p.kutu(695, 265, 420, 125, "#431407", "#F97316", 2, 10),
        p.metin(905, 298, "• Calvin Döngüsü (enzimatik tepkimeler).", 15, "#F8FAFC", "middle", False),
        p.metin(905, 328, "• Doğrudan ışık gerekmez; enzimler görev yapar.", 15, "#FDE047", "middle", True),
        p.metin(905, 358, "• CO₂ tutularak (karbon fiksasyonu) indirgenir.", 15, "#F8FAFC", "middle", False),
        p.etiket(695, 410, 420, 52, "Temel Ürün:  PGAL → Glikoz (C₆H₁₂O₆) ve Organik Baz/Amino Asit", Renk.YESIL),
        p.etiket(695, 480, 420, 55, "Tilakoite Dönenler:  ADP + Pᵢ ve NADP⁺", Renk.MOR),
        p.alt_serit("Işığa bağımlı evrede üretilen ATP ve NADPH, stromada CO₂'den organik besin sentezlemek için harcanır."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("FOTOSENTEZDE ATOMLARIN İZLENMESİ (İZOTOP DENEYLERİ)", "6CO₂ + 12H₂O → C₆H₁₂O₆ + 6O₂ + 6H₂O"),
        p.panel(55, 130, 530, 440, "Karbondioksit (CO₂) Atomlarının Hedefi", Renk.MAVI),
        p.etiket(95, 195, 450, 65, "Karbon (C) Atomu  →  C₆H₁₂O₆ (Glikozun Karbonu)", Renk.MAVI),
        p.etiket(95, 285, 450, 65, "CO₂'nin Oksijeni (O)  →  C₆H₁₂O₆ ve Üretilen H₂O", Renk.TURUNCU),
        p.kutu(95, 375, 450, 150, "#1E293B", "#60A5FA", 2, 10),
        p.metin(320, 415, "Önemli Sonuç:", 16, "#FDE047", "middle", True),
        p.metin(320, 450, "Karbondioksitteki oksijen atomları (¹⁸O),", 15, "#F8FAFC", "middle", False),
        p.metin(320, 480, "atmosfere verilen O₂ gazının yapısına KATILMAZ!", 15, "#F87171", "middle", True),
        p.panel(615, 130, 530, 440, "Su (H₂O) Atomlarının Hedefi", Renk.YESIL),
        p.etiket(655, 195, 450, 65, "Suyun Hidrojeni (H)  →  C₆H₁₂O₆ ve Üretilen H₂O", Renk.YESIL),
        p.etiket(655, 285, 450, 65, "Suyun Oksijeni (¹⁸O)  →  Atmosfere Verilen O₂ Gazı!", Renk.SARI),
        p.kutu(655, 375, 450, 150, "#064E3B", "#34D399", 2, 10),
        p.metin(880, 415, "Radyoaktif İzotop (¹⁸O) Kanıtı:", 16, "#FDE047", "middle", True),
        p.metin(880, 450, "Bitkiye H₂¹⁸O verildiğinde açığa çıkan", 15, "#F8FAFC", "middle", False),
        p.metin(880, 480, "oksijen gazının tamamı ¹⁸O₂ olarak ölçülür.", 15, "#34D399", "middle", True),
        p.alt_serit("Atmosfere verilen oksijenin kaynağı tamamen suyun (H₂O) fotolizidir; besindeki karbon ve oksijenin kaynağı ise CO₂'dir."),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("FOTOSENTEZ HIZINI ETKİLEYEN ÇEVRESEL FAKTÖRLER", "Işık Şiddeti, CO₂ Yoğunluğu, Sıcaklık ve Dalga Boyu Grafikleri"),
        p.panel(55, 130, 525, 210, "1. Işık Şiddeti ve 2. CO₂ Yoğunluğu", Renk.MAVI),
        p.ok(95, 310, 320, 310, "#94A3B8", 2),
        p.ok(95, 315, 95, 185, "#94A3B8", 2),
        p.dogru(95, 310, 200, 210, "#60A5FA", 4),
        p.dogru(200, 210, 305, 210, "#60A5FA", 4),
        p.metin(200, 328, "Doygunluk noktası", 12, "#93C5FD", "middle", False),
        p.metin(445, 235, "Belirli bir değere kadar\nhızı artırır, sonra diğer\nfaktörler sınırladığı için\nhız sabit kalır.", 14, "#E2E8F0", "middle", False),
        p.panel(620, 130, 525, 210, "3. Sıcaklık (Enzim Etkisi)", Renk.TURUNCU),
        p.ok(660, 310, 885, 310, "#94A3B8", 2),
        p.ok(660, 315, 660, 185, "#94A3B8", 2),
        p.dogru(660, 295, 775, 195, "#F97316", 4),
        p.dogru(775, 195, 860, 310, "#EF4444", 4),
        p.metin(775, 328, "Optimum (~25-35 °C)", 12, "#FDBA74", "middle", True),
        p.metin(1010, 235, "Optimum sıcaklıkta hız\nmaksimumdur; yüksek\nsıcaklıkta enzimler\ndenatüre olur!", 14, "#E2E8F0", "middle", False),
        p.panel(55, 360, 1090, 210, "4. Işığın Dalga Boyu (Engelmann Deneyi)", Renk.MOR),
        p.etiket(95, 420, 310, 60, "Mor - Mavi Işık (380-480 nm)\nYüksek Emilim → Yüksek Fotosentez", Renk.MOR),
        p.etiket(445, 420, 310, 60, "Yeşil Işık (500-560 nm)\nYansıtılır → En Düşük Fotosentez", Renk.YESIL),
        p.etiket(795, 420, 310, 60, "Kırmızı Işık (620-700 nm)\nYüksek Emilim → Yüksek Fotosentez", Renk.TURUNCU),
        p.metin(600, 525, "Klorofil mor, mavi ve kırmızı ışığı en çok soğurur; yeşil ışığı büyük oranda yansıttığı için fotosentez hızı yeşilde en düşüktür.", 14, "#FDE047", "middle", True),
        p.alt_serit("Fotosentez hızını aynı anda birden fazla faktör etkiliyorsa, hızı miktarı en az olan faktör belirler (Minimum Yasası)."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("FOTOSENTEZ DENEY DÜZENEKLERİ VE DEĞİŞKEN ANALİZİ", "Su Bitkisi (Elodea) ile O₂ Kabarcık Sayısı Ölçümü"),
        p.panel(55, 130, 530, 440, "Elodea Deneyinde Hızı Artıran Uygulamalar", Renk.YESIL),
        p.etiket(90, 195, 460, 58, "1. Işık kaynağını bitkiye yaklaştırmak (Işık şiddeti artar)", Renk.SARI),
        p.etiket(90, 270, 460, 58, "2. Suya soda / NaHCO₃ eklemek (Çözünmüş CO₂ artar)", Renk.MAVI),
        p.etiket(90, 345, 460, 58, "3. Yeşil filtre yerine mor veya kırmızı ışık kullanmak", Renk.MOR),
        p.etiket(90, 420, 460, 58, "4. Sıcaklığı 10 °C'den 30 °C'ye (optimuma) getirmek", Renk.YESIL),
        p.metin(320, 520, "Uyarı: Kaynatılıp soğutulmuş suda CO₂ gazı uçtuğu için\nveya KOH / Ca(OH)₂ bulunan kapta fotosentez DURUR!", 14, "#F87171", "middle", True),
        p.panel(615, 130, 530, 440, "Bilimsel Deney Tasarımında Değişkenler", Renk.MAVI),
        p.etiket(650, 200, 460, 95, "Bağımsız Değişken (Araştırılan Etken):\nDeneyde araştırmacının bilerek değiştirdiği faktör\n(Örn: Işığın rengi veya ışık kaynağının uzaklığı)", Renk.TURUNCU),
        p.etiket(650, 315, 460, 95, "Bağımlı Değişken (Gözlenen Sonuç):\nBağımsız değişkene bağlı olarak değişen sonuç\n(Örn: Birim zamanda çıkan O₂ kabarcık sayısı / fotosentez hızı)", Renk.YESIL),
        p.etiket(650, 430, 460, 95, "Kontrol Değişkenleri (Sabit Tutulanlar):\nDeneyin güvenirliği için her düzenekte eşit tutulanlar\n(Örn: Sıcaklık, su miktarı, bitki türü ve yaprak sayısı)", Renk.MAVI),
        p.alt_serit("Kontrollü deneylerde yalnızca araştırılan bağımsız değişken değiştirilir; diğer tüm faktörler sabit tutulur."),
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
