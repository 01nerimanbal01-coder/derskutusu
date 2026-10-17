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
        p.baslik_16_9("TEPKİMELERİN ÜÇ FARKLI GÖSTERİM DÜZEYİ", "Makroskobik Gözlem, Tanecik Boyutu (Mikroskobik) ve Sembolik Dil"),
        p.panel(55, 135, 340, 430, "1. Makroskobik Düzey", Renk.MAVI),
        p.kutu(145, 220, 160, 180, "#1E3A8A", "#60A5FA", 3, 12),
        p.kutu(155, 330, 140, 60, "#FDE047", "#F59E0B", 2, 6),
        p.metin(225, 365, "Sarı Çökelti (PbI₂)", 14, "#0F172A", "middle", True),
        p.metin(225, 445, "Laboratuvarda duyu\norganlarıyla yapılan gözlem:", 15, "#E2E8F0", "middle", False),
        p.metin(225, 505, "• Renk değişimi / Çökelti\n• Gaz çıkışı / Isı değişimi", 14, "#93C5FD", "middle", True),
        p.panel(430, 135, 340, 430, "2. Tanecik (Mikroskobik) Boyutu", Renk.YESIL),
        p.daire(520, 240, 22, "#F59E0B", "#FDE047", 2),
        p.metin(520, 245, "Pb²⁺", 13, "#0F172A", "middle", True),
        p.daire(590, 230, 18, "#A855F7", "#D8B4FE", 2),
        p.metin(590, 235, "I⁻", 13, "#F8FAFC", "middle", True),
        p.daire(650, 250, 18, "#38BDF8", "#BAE6FD", 2),
        p.metin(650, 255, "NO₃⁻", 12, "#0F172A", "middle", True),
        p.daire(550, 355, 22, "#F59E0B", "#FDE047", 2),
        p.daire(522, 365, 17, "#A855F7", "#D8B4FE", 2),
        p.daire(578, 365, 17, "#A855F7", "#D8B4FE", 2),
        p.metin(600, 445, "Atom, iyon ve moleküllerin\nçarpışma ve bağ modeli:", 15, "#E2E8F0", "middle", False),
        p.metin(600, 505, "• İyonların kristal örme süreci\n• Elektron/proton aktarımı", 14, "#A7F3D0", "middle", True),
        p.panel(805, 135, 340, 430, "3. Sembolik Düzey", Renk.TURUNCU),
        p.etiket(830, 210, 290, 58, "Pb(NO₃)₂(suda) + 2KI(suda)", Renk.MAVI),
        p.ok(975, 275, 975, 315, "#FDE047", 4),
        p.etiket(830, 325, 290, 58, "PbI₂(k)↓ + 2KNO₃(suda)", Renk.SARI),
        p.metin(975, 445, "Formül, denklem, indis\nve fiziksel hâl sembolleri:", 15, "#E2E8F0", "middle", False),
        p.metin(975, 505, "(k), (s), (g), (suda)\nNet iyon denklemleri", 14, "#FDBA74", "middle", True),
        p.alt_serit("Kimyasal değişimleri tam anlamak için gözlemleri tanecik modeli ve sembolik denklemlerle ilişkilendiririz."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("ÇÖKELME TEPKİMESİNDE TANECİK MODELİ VE İYON DENKLEMLERİ", "AgNO₃(suda) + NaCl(suda) → AgCl(k) + NaNO₃(suda)"),
        p.panel(55, 130, 520, 440, "Karışım Öncesi ve Sonrası Tanecikler", Renk.MAVI),
        p.kutu(85, 195, 200, 150, "#1E293B", "#60A5FA", 2, 10),
        p.metin(185, 220, "Ag⁺(suda) + NO₃⁻(suda)", 14, "#93C5FD", "middle", True),
        p.metin(185, 255, "Na⁺(suda) + Cl⁻(suda)", 14, "#93C5FD", "middle", True),
        p.metin(185, 310, "(Serbest hareketli iyonlar)", 13, "#CBD5E1", "middle", False),
        p.ok(295, 270, 335, 270, "#FDE047", 4),
        p.kutu(345, 195, 200, 150, "#1E293B", "#34D399", 2, 10),
        p.metin(445, 230, "Na⁺(suda) ve NO₃⁻(suda)", 14, "#A7F3D0", "middle", True),
        p.kutu(375, 290, 140, 42, "#F8FAFC", "#94A3B8", 2, 6),
        p.metin(445, 316, "AgCl(k) Çökeltisi", 14, "#0F172A", "middle", True),
        p.etiket(85, 380, 460, 70, "Seyirci (Gözlemci) İyonlar: Na⁺(suda) ve NO₃⁻(suda)\n(Tepkimeye girmeden çözeltide serbest kalırlar)", Renk.SARI),
        p.etiket(85, 470, 460, 70, "Çöken İyonlar: Ag⁺(suda) ve Cl⁻(suda)\n(Birleşerek suda çözünmeyen AgCl katısını oluştururlar)", Renk.YESIL),
        p.panel(605, 130, 540, 440, "Üç Adımda Denklem Yazımı", Renk.MOR),
        p.etiket(635, 195, 480, 75, "1. Moleküler (Toplam) Denklem:\nAgNO₃(suda) + NaCl(suda) → AgCl(k) + NaNO₃(suda)", Renk.MAVI),
        p.etiket(635, 295, 480, 85, "2. Tam İyon Denklemi:\nAg⁺ + NO₃⁻ + Na⁺ + Cl⁻ → AgCl(k) + Na⁺ + NO₃⁻", Renk.TURUNCU),
        p.etiket(635, 405, 480, 85, "3. Net İyon Denklemi (Seyirciler Sadeleşir):\nAg⁺(suda) + Cl⁻(suda) → AgCl(k)", Renk.YESIL),
        p.metin(875, 530, "Çökelme tepkimelerinde net iyon denklemi katı çökeltinin oluşumuna göre yazılır.", 13, "#E2E8F0", "middle", True),
        p.alt_serit("Çökelme tepkimelerinde katı oluşturmayan ve çözeltide serbest kalan iyonlara seyirci iyon denir."),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("ASİT-BAZ VE REDOKS TEPKİMELERİNİN TANECİK SÜRECİ", "Proton (H⁺) Aktarımı ve Elektron (e⁻) Alışverişi"),
        p.panel(55, 130, 530, 440, "Nötralleşme Tepkimesi (Asit + Baz)", Renk.YESIL),
        p.etiket(85, 195, 470, 65, "HCl(suda) + NaOH(suda) → NaCl(suda) + H₂O(s)", Renk.MAVI),
        p.kutu(85, 280, 470, 110, "#064E3B", "#10B981", 2, 10),
        p.metin(320, 315, "Asitten gelen H⁺(suda) (veya H₃O⁺) iyonu ile", 15, "#F8FAFC", "middle", False),
        p.metin(320, 345, "bazdan gelen OH⁻(suda) iyonu birleşerek su oluşturur.", 15, "#F8FAFC", "middle", False),
        p.metin(320, 375, "Seyirci İyonlar: Na⁺(suda) ve Cl⁻(suda)", 14, "#FDE047", "middle", True),
        p.etiket(85, 415, 470, 65, "Net İyon Denklemi:\nH⁺(suda) + OH⁻(suda) → H₂O(s)", Renk.YESIL),
        p.metin(320, 520, "Kuvvetli asit ve bazların nötralleşmesinde net iyon denklemi suyun oluşumudur.", 13, "#CBD5E1", "middle", False),
        p.panel(615, 130, 530, 440, "İndirgenme-Yükseltgenme (Redoks) Süreci", Renk.TURUNCU),
        p.etiket(645, 195, 470, 65, "Zn(k) + CuSO₄(suda) → ZnSO₄(suda) + Cu(k)", Renk.TURUNCU),
        p.kutu(645, 280, 470, 110, "#431407", "#F97316", 2, 10),
        p.metin(880, 312, "Yükseltgenme Yarı Tepkimesi:  Zn(k) → Zn²⁺(suda) + 2e⁻", 15, "#FDE047", "middle", True),
        p.metin(880, 345, "İndirgenme Yarı Tepkimesi:   Cu²⁺(suda) + 2e⁻ → Cu(k)", 15, "#38BDF8", "middle", True),
        p.metin(880, 375, "Seyirci İyon: SO₄²⁻(suda) (Yükü ve yapısı değişmez)", 14, "#E2E8F0", "middle", False),
        p.etiket(645, 415, 470, 65, "Net Redoks Denklemi:\nZn(k) + Cu²⁺(suda) → Zn²⁺(suda) + Cu(k)", Renk.SARI),
        p.metin(880, 520, "Alınan elektron sayısı daima verilen elektron sayısına eşittir!", 14, "#FDBA74", "middle", True),
        p.alt_serit("Nötralleşmede H⁺ ve OH⁻ birleşerek H₂O oluşturur; redoksta ise tanecikler arasında elektron aktarılır."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("TANECİK SAYISI VE ELEKTRİKSEL İLETKENLİK DEĞİŞİMİ", "Tepkime Sürecinde Çözeltideki İyon Derişiminin İzlenmesi"),
        p.panel(55, 130, 530, 440, "Çökelme Sürecinde İyon Sayısı Değişimi", Renk.MAVI),
        p.etiket(85, 195, 470, 65, "BaCl₂(suda) + Na₂SO₄(suda) → BaSO₄(k)↓ + 2NaCl(suda)", Renk.MAVI),
        p.metin(320, 295, "• Ba²⁺ ve SO₄²⁻ iyonları birleşip dibe çöker.", 15, "#E2E8F0", "middle", False),
        p.metin(320, 330, "• Na⁺ ve Cl⁻ seyirci iyonları çözeltide kalır.", 15, "#E2E8F0", "middle", False),
        p.metin(320, 365, "• Çözeltideki toplam serbest iyon derişimi azalır,", 15, "#FDE047", "middle", True),
        p.metin(320, 395, "  ancak seyirci iyonlar sayesinde sıfırlanmaz!", 15, "#FDE047", "middle", True),
        p.etiket(85, 440, 470, 65, "Sonuç: Elektrik iletkenliği azalır fakat devam eder.", Renk.YESIL),
        p.panel(615, 130, 530, 440, "Tam Çökelme / Nötralleşme Özel Durumu", Renk.MOR),
        p.etiket(645, 195, 470, 65, "Ba(OH)₂(suda) + H₂SO₄(suda) → BaSO₄(k)↓ + 2H₂O(s)", Renk.MOR),
        p.metin(880, 295, "• Ba²⁺ ve SO₄²⁻ iyonları BaSO₄(k) olarak çöker.", 15, "#E2E8F0", "middle", False),
        p.metin(880, 330, "• H⁺ ve OH⁻ iyonları H₂O(s) sıvısına dönüşür.", 15, "#E2E8F0", "middle", False),
        p.metin(880, 365, "• Eşdeğer miktarda karıştırıldığında çözeltide", 15, "#F87171", "middle", True),
        p.metin(880, 395, "  serbest seyirci iyon KALMAZ!", 15, "#F87171", "middle", True),
        p.etiket(645, 440, 470, 65, "Sonuç: Elektrik iletkenliği neredeyse sıfıra iner.", Renk.TURUNCU),
        p.alt_serit("Tanecik boyutunda kütlenin ve toplam yükün korunumu her kimyasal tepkimede mutlak olarak sağlanır."),
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
