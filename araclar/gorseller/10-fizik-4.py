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
        p.baslik_16_9("HIZ-ZAMAN (v-t) VE İVME-ZAMAN (a-t) GRAFİKLERİ", "Sabit İvmeli Hareketin Grafiksel Analizi"),
        p.panel(55, 130, 520, 440, "Hız-Zaman (v-t) Grafiği", Renk.MAVI),
        p.ok(110, 490, 520, 490, "#94A3B8", 3),
        p.ok(110, 520, 110, 200, "#94A3B8", 3),
        p.metin(535, 495, "t (s)", 14, "#F8FAFC", "start", True),
        p.metin(110, 185, "v (m/s)", 14, "#F8FAFC", "middle", True),
        p.cokgen([(110, 400), (470, 230), (470, 490), (110, 490)], "#1E3A8A", "#3B82F6", 2),
        p.dogru(110, 400, 470, 230, "#60A5FA", 4),
        p.kesikli_dogru(110, 230, 470, 230, "#94A3B8", 2),
        p.kesikli_dogru(470, 230, 470, 490, "#94A3B8", 2),
        p.metin(85, 405, "v₀", 15, "#FDE047", "middle", True),
        p.metin(85, 235, "v", 15, "#34D399", "middle", True),
        p.metin(470, 515, "t", 15, "#F8FAFC", "middle", True),
        p.metin(300, 390, "Altta Kalan Alan = Δx", 15, "#FDE047", "middle", True),
        p.metin(270, 275, "Eğim = a = Δv / Δt", 15, "#93C5FD", "middle", True),
        p.panel(615, 130, 530, 440, "İvme-Zaman (a-t) Grafiği", Renk.YESIL),
        p.ok(670, 450, 1090, 450, "#94A3B8", 3),
        p.ok(670, 520, 670, 200, "#94A3B8", 3),
        p.metin(1105, 455, "t (s)", 14, "#F8FAFC", "start", True),
        p.metin(670, 185, "a (m/s²)", 14, "#F8FAFC", "middle", True),
        p.kutu(670, 280, 360, 170, "#064E3B", "#10B981", 3, 0),
        p.dogru(670, 280, 1030, 280, "#34D399", 5),
        p.metin(645, 285, "a", 16, "#34D399", "middle", True),
        p.metin(1030, 475, "t", 15, "#F8FAFC", "middle", True),
        p.metin(850, 365, "Alan = Δv = a · t", 16, "#A7F3D0", "middle", True),
        p.metin(850, 400, "(Hız Değişimi)", 14, "#E2E8F0", "middle", False),
        p.etiket(645, 510, 470, 42, "v = v₀ + Δv  ⇒  Son Hız = İlk Hız + (a · t)", Renk.SARI),
        p.alt_serit("v-t grafiğinin eğimi ivmeyi, altında kalan alan yer değiştirmeyi; a-t grafiğinin alanı ise hız değişimini verir."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("HIZLANMA VE YAVAŞLAMA DURUMLARI", "Hız Vektörü (v) ile İvme Vektörünün (a) Yön İlişkisi"),
        p.panel(55, 130, 525, 205, "1. Pozitif Yönde Hızlanan (+v, +a)", Renk.YESIL),
        p.ok(100, 225, 310, 225, "#34D399", 5),
        p.metin(205, 208, "v (+)", 15, "#34D399", "middle", True),
        p.ok(100, 265, 260, 265, "#FDE047", 5),
        p.metin(180, 290, "a (+)", 15, "#FDE047", "middle", True),
        p.metin(430, 240, "Aynı yönlü:\nSürat artar!", 15, "#E2E8F0", "middle", True),
        p.panel(620, 130, 525, 205, "2. Pozitif Yönde Yavaşlayan (+v, -a)", Renk.TURUNCU),
        p.ok(665, 225, 875, 225, "#34D399", 5),
        p.metin(770, 208, "v (+)", 15, "#34D399", "middle", True),
        p.ok(875, 265, 715, 265, "#F87171", 5),
        p.metin(795, 290, "a (-)", 15, "#F87171", "middle", True),
        p.metin(1000, 240, "Zıt yönlü:\nSürat azalır!", 15, "#E2E8F0", "middle", True),
        p.panel(55, 365, 525, 205, "3. Negatif Yönde Hızlanan (-v, -a)", Renk.MAVI),
        p.ok(310, 460, 100, 460, "#60A5FA", 5),
        p.metin(205, 443, "v (-)", 15, "#60A5FA", "middle", True),
        p.ok(260, 500, 100, 500, "#F87171", 5),
        p.metin(180, 525, "a (-)", 15, "#F87171", "middle", True),
        p.metin(430, 475, "Aynı yönlü:\nSürat artar!", 15, "#E2E8F0", "middle", True),
        p.panel(620, 365, 525, 205, "4. Negatif Yönde Yavaşlayan (-v, +a)", Renk.MOR),
        p.ok(875, 460, 665, 460, "#60A5FA", 5),
        p.metin(770, 443, "v (-)", 15, "#60A5FA", "middle", True),
        p.ok(665, 500, 825, 500, "#FDE047", 5),
        p.metin(745, 525, "a (+)", 15, "#FDE047", "middle", True),
        p.metin(1000, 475, "Zıt yönlü:\nSürat azalır!", 15, "#E2E8F0", "middle", True),
        p.alt_serit("Hız ve ivme vektörleri aynı yönlü ise cisim hızlanır; zıt yönlü ise cisim yavaşlar."),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("SABİT İVMELİ HAREKETTE YER DEĞİŞTİRME HESABI", "Yamuk Alanı ve Ortalama Hız Yöntemi"),
        p.panel(55, 130, 530, 440, "Alan Parçalama: Dikdörtgen + Üçgen", Renk.MAVI),
        p.kutu(110, 330, 340, 160, "#1E3A8A", "#60A5FA", 2, 0),
        p.cokgen([(110, 330), (450, 210), (450, 330)], "#065F46", "#34D399", 2),
        p.metin(280, 415, "Alan 1 = v₀ · t", 18, "#93C5FD", "middle", True),
        p.metin(335, 300, "Alan 2 = ½ · a · t²", 16, "#A7F3D0", "middle", True),
        p.etiket(95, 510, 450, 42, "Δx = v₀ · t + ½ · a · t²", Renk.SARI),
        p.panel(615, 130, 530, 440, "Ortalama Hız ve Zamansız Hız Denklemi", Renk.MOR),
        p.etiket(650, 200, 460, 65, "v_ort = (v₀ + v) / 2", Renk.MAVI),
        p.etiket(650, 290, 460, 65, "Δx = [(v₀ + v) / 2] · t", Renk.YESIL),
        p.etiket(650, 380, 460, 65, "v² = v₀² + 2 · a · Δx", Renk.TURUNCU),
        p.metin(880, 495, "Sabit ivmeli harekette ortalama hız,\nilk ve son hızın aritmetik ortalamasıdır.", 15, "#E2E8F0", "middle", False),
        p.alt_serit("Sabit ivmeli hareket denklemlerinin tamamı v-t grafiğinin eğim ve alan bağıntılarından türetilir."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("DOĞADAKİ SABİT İVMELİ HAREKET: SERBEST DÜŞME", "Yer Çekimi İvmesi (g ≈ 10 m/s²) Etkisinde Hareket"),
        p.panel(55, 130, 510, 440, "Her Saniye Hız ve Yol Değişimi (v₀ = 0)", Renk.TURUNCU),
        p.daire(150, 195, 16, "#FDE047", "#F59E0B", 2),
        p.metin(290, 200, "t = 0 s   →   v = 0 m/s", 15, "#F8FAFC", "start", True),
        p.ok(150, 215, 150, 265, "#94A3B8", 2),
        p.metin(195, 245, "5 m (x)", 14, "#FDE047", "start", True),
        p.daire(150, 285, 16, "#FB923C", "#EA580C", 2),
        p.metin(290, 290, "t = 1 s   →   v = 10 m/s", 15, "#F8FAFC", "start", True),
        p.ok(150, 305, 150, 375, "#94A3B8", 2),
        p.metin(195, 345, "15 m (3x)", 14, "#FB923C", "start", True),
        p.daire(150, 395, 16, "#F87171", "#DC2626", 2),
        p.metin(290, 400, "t = 2 s   →   v = 20 m/s", 15, "#F8FAFC", "start", True),
        p.ok(150, 415, 150, 505, "#94A3B8", 2),
        p.metin(195, 465, "25 m (5x)", 14, "#F87171", "start", True),
        p.daire(150, 525, 16, "#EF4444", "#B91C1C", 2),
        p.metin(290, 530, "t = 3 s   →   v = 30 m/s", 15, "#F8FAFC", "start", True),
        p.panel(600, 130, 545, 440, "Serbest Düşme Bağıntıları", Renk.YESIL),
        p.etiket(635, 200, 475, 65, "Anlık Hız:  v = g · t", Renk.MAVI),
        p.etiket(635, 290, 475, 65, "Düşme Yüksekliği:  h = ½ · g · t²", Renk.YESIL),
        p.etiket(635, 380, 475, 65, "Zamansız Hız:  v² = 2 · g · h", Renk.SARI),
        p.etiket(635, 470, 475, 65, "Ardışık Saniye Yolları: 5 m - 15 m - 25 m - 35 m", Renk.TURUNCU),
        p.alt_serit("Hava direnci ihmal edildiğinde serbest bırakılan cisimler g ≈ 10 m/s² sabit ivmeyle hızlanır."),
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
