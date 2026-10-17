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
        p.baslik_16_9("ÜÇGENİN YARDIMCI ELEMANLARININ ÖZEL NOKTALARI", "İç Teğet Çember, Çevrel Çember, Ağırlık Merkezi ve Diklik Merkezi"),
        p.panel(55, 130, 525, 210, "1. Açıortaylar ve 2. Kenarortaylar", Renk.MAVI),
        p.etiket(80, 190, 475, 58, "İç Açıortayların Kesim Noktası (I):\nİç teğet çemberin merkezidir; kenarlara eşit uzaklıktadır.", Renk.MAVI),
        p.etiket(80, 262, 475, 58, "Kenarortayların Kesim Noktası (G - Ağırlık Merkezi):\nTabana 1 birim (k), köşeye 2 birim (2k) uzaklıktadır.", Renk.YESIL),
        p.panel(620, 130, 525, 210, "3. Kenar Orta Dikmeler ve 4. Yükseklikler", Renk.TURUNCU),
        p.etiket(645, 190, 475, 58, "Kenar Orta Dikmelerin Kesim Noktası (O):\nÇevrel çemberin merkezidir; köşelere eşit uzaklıktadır.", Renk.TURUNCU),
        p.etiket(645, 262, 475, 58, "Yüksekliklerin Kesim Noktası (H - Diklik Merkezi):\nDar açılıda içte, dik üçgende dik köşede, genişte dışta!", Renk.MOR),
        p.panel(55, 360, 1090, 210, "İkizkenar ve Eşkenar Üçgende Yardımcı Elemanlar (YA-Kİ Kuralı)", Renk.YESIL),
        p.cokgen([(260, 410), (140, 545), (380, 545)], "#064E3B", "#34D399", 3),
        p.dogru(260, 410, 260, 545, "#FDE047", 3),
        p.metin(260, 398, "A", 15, "#F8FAFC", "middle", True),
        p.metin(125, 550, "B", 15, "#F8FAFC", "middle", True),
        p.metin(395, 550, "C", 15, "#F8FAFC", "middle", True),
        p.metin(260, 563, "H (Diklik = Kenarortay = Açıortay)", 13, "#FDE047", "middle", True),
        p.etiket(440, 415, 670, 60, "İkizkenar Üçgende (|AB| = |AC|) Tepe Açısından İndirilen:\nh_a = n_a = V_a  (Yükseklik = Açıortay = Kenarortay aynı doğrudur!)", Renk.SARI),
        p.etiket(440, 490, 670, 60, "Genel Üçgende Aynı Köşeden Çizilen Elemanların Sıralaması:\nh_a ≤ n_a ≤ V_a   (En kısa yükseklik, ortanca açıortay, en uzun kenarortay)", Renk.MAVI),
        p.alt_serit("Eşkenar üçgende tüm kenarlara ait yükseklik, açıortay ve kenarortay uzunlukları birbirine eşittir."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("ÜÇGENİN TEMEL ALAN BAĞINTISI VE YÜKSEKLİK KONUMLARI", "Alan(ABC) = (Taban · Yükseklik) / 2 = (a · h_a) / 2"),
        p.panel(55, 130, 345, 440, "1. Dar Açılı Üçgen", Renk.MAVI),
        p.cokgen([(210, 200), (95, 430), (355, 430)], "#1E3A8A", "#60A5FA", 3),
        p.kesikli_dogru(210, 200, 210, 430, "#FDE047", 3),
        p.metin(228, 325, "h_a", 16, "#FDE047", "start", True),
        p.metin(225, 455, "a (Taban)", 15, "#93C5FD", "middle", True),
        p.etiket(80, 485, 295, 60, "Yükseklik üçgenin içindedir.\nA(ABC) = (a · h_a) / 2", Renk.MAVI),
        p.panel(425, 130, 345, 440, "2. Dik Açılı Üçgen", Renk.YESIL),
        p.cokgen([(470, 200), (470, 430), (725, 430)], "#064E3B", "#34D399", 3),
        p.metin(450, 315, "c", 16, "#FDE047", "middle", True),
        p.metin(595, 455, "a (Dik Kenar)", 15, "#A7F3D0", "middle", True),
        p.metin(615, 300, "b (Hipotenüs)", 15, "#F8FAFC", "start", True),
        p.etiket(450, 485, 295, 60, "Dik kenarlar birbirinin yüksekliğidir:\nA(ABC) = (a · c) / 2 = (b · h_b) / 2", Renk.YESIL),
        p.panel(795, 130, 350, 440, "3. Geniş Açılı Üçgen", Renk.TURUNCU),
        p.cokgen([(835, 200), (915, 430), (1110, 430)], "#431407", "#F97316", 3),
        p.kesikli_dogru(835, 200, 835, 430, "#FDE047", 3),
        p.kesikli_dogru(835, 430, 915, 430, "#94A3B8", 2),
        p.metin(860, 325, "h_a", 16, "#FDE047", "start", True),
        p.metin(1012, 455, "a (Taban)", 15, "#FDBA74", "middle", True),
        p.etiket(820, 485, 300, 60, "Yükseklik dışarıya iner ama\nformülde SADECE 'a' tabanı alınır!", Renk.TURUNCU),
        p.alt_serit("Geniş açılı üçgende dışarıdan inen yükseklik hesaplanırken uzantı parçası tabana eklenmez!"),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("TABAN VE YÜKSEKLİK DEĞİŞİMİNE GÖRE ALAN ORANLARI", "Yükseklikleri Eşit veya Tabanları Eşit Üçgenlerde Alan Paylaşımı"),
        p.panel(55, 130, 530, 440, "1. Yükseklikleri Eşit Üçgenler (Tepe Noktası Ortak)", Renk.MAVI),
        p.cokgen([(310, 195), (105, 435), (525, 435)], "#1E293B", "#60A5FA", 3),
        p.dogru(310, 195, 245, 435, "#FDE047", 3),
        p.metin(310, 180, "A (Ortak Tepe)", 14, "#F8FAFC", "middle", True),
        p.metin(175, 460, "2k", 16, "#93C5FD", "middle", True),
        p.metin(385, 460, "5k", 16, "#34D399", "middle", True),
        p.metin(200, 360, "2S", 22, "#FDE047", "middle", True),
        p.metin(365, 360, "5S", 22, "#34D399", "middle", True),
        p.etiket(85, 490, 470, 60, "Yükseklikleri eşit olan üçgenlerin alanları\ntaban uzunluklarıyla doğru orantılıdır: A₁ / A₂ = a₁ / a₂", Renk.MAVI),
        p.panel(615, 130, 530, 440, "2. Ağırlık Merkezi (G) ve Alanların 6 Eşit Parçaya Bölünmesi", Renk.YESIL),
        p.cokgen([(880, 195), (675, 435), (1085, 435)], "#064E3B", "#34D399", 3),
        p.dogru(880, 195, 880, 435, "#94A3B8", 2),
        p.dogru(675, 435, 982, 315, "#94A3B8", 2),
        p.dogru(1085, 435, 777, 315, "#94A3B8", 2),
        p.daire(880, 355, 6, "#FDE047", "#F59E0B", 2),
        p.metin(845, 300, "S", 16, "#FDE047", "middle", True),
        p.metin(915, 300, "S", 16, "#FDE047", "middle", True),
        p.metin(785, 370, "S", 16, "#FDE047", "middle", True),
        p.metin(975, 370, "S", 16, "#FDE047", "middle", True),
        p.metin(830, 415, "S", 16, "#FDE047", "middle", True),
        p.metin(930, 415, "S", 16, "#FDE047", "middle", True),
        p.etiket(645, 490, 470, 60, "Üç kenarortay, üçgenin alanını 6 eş alana (6S) böler.\nTek bir kenarortay ise alanı 2 eş parçaya (3S - 3S) ayırır.", Renk.YESIL),
        p.alt_serit("Taban sabitken yükseklik k katına çıkarsa alan da k katına çıkar; hem taban hem yükseklik değişirse oranları çarpılır."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("SİNÜS ALAN TEOREMİ VE EŞKENAR ÜÇGENİN ALANI", "İki Kenar ve Arasındaki Açı Bilindiğinde Alan Hesabı"),
        p.panel(55, 130, 530, 440, "Sinüs Alan Bağıntısı", Renk.MOR),
        p.cokgen([(260, 200), (110, 420), (490, 420)], "#3B0764", "#C084FC", 3),
        p.metin(165, 300, "c", 18, "#FDE047", "middle", True),
        p.metin(300, 448, "a", 18, "#FDE047", "middle", True),
        p.metin(155, 400, "B açısı", 15, "#F8FAFC", "start", True),
        p.etiket(90, 480, 460, 68, "Alan(ABC) = ½ · a · c · sin(B)\n= ½ · a · b · sin(C) = ½ · b · c · sin(A)", Renk.MOR),
        p.panel(615, 130, 530, 440, "Eşkenar Üçgenin Yüksekliği ve Alanı", Renk.TURUNCU),
        p.cokgen([(880, 195), (710, 420), (1050, 420)], "#431407", "#FB923C", 3),
        p.kesikli_dogru(880, 195, 880, 420, "#FDE047", 3),
        p.metin(775, 300, "a", 18, "#FDBA74", "middle", True),
        p.metin(985, 300, "a", 18, "#FDBA74", "middle", True),
        p.metin(880, 448, "a (Tüm açılar 60°)", 16, "#F8FAFC", "middle", True),
        p.etiket(650, 475, 460, 75, "Yükseklik:  h = a · sin(60°)\nAlan:  A(ABC) = ½ · a² · sin(60°)", Renk.SARI),
        p.alt_serit("Sinüs alan formülü: iki kenar uzunluğu ve aralarındaki açının sinüsü bilindiğinde alanı doğrudan verir."),
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
