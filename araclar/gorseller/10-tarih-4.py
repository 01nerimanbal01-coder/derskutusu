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
        p.baslik_16_9("TÜRK-İSLAM DEVLETLERİNDE HÂKİMİYET ANLAYIŞI VE SEMBOLLERİ", "Kut İnancının İslami Dönemde 'Allah'ın Takdiri ve Nasibi' Olarak Sürmesi"),
        p.panel(55, 130, 525, 440, "Süreklilik Gösteren Unsurlar (Bozkır Mirası)", Renk.MAVI),
        p.etiket(85, 195, 465, 62, "Kut Anlayışı → Zıllullah fi'l-Arz (Allah'ın Yeryüzündeki Gölgesi)", Renk.MAVI),
        p.etiket(85, 275, 465, 62, "Cihan Hâkimiyeti Ülküsü → İ'lâ-yı Kelimetullah ve Cihat", Renk.YESIL),
        p.etiket(85, 355, 465, 62, "Ülke Hanedanın Ortak Malıdır → Taht Mücadeleleri ve Atabeylik", Renk.TURUNCU),
        p.etiket(85, 435, 465, 62, "Töre (Örfî Hukuk) + Şer'î Hukuk (İslam Hukuku) Birlikteliği", Renk.MOR),
        p.metin(317, 535, "Eski Türk devlet geleneği İslami kavramlarla bütünleşmiştir.", 14, "#93C5FD", "middle", True),
        p.panel(615, 130, 530, 440, "Yeni Eklenen İslami Hükümdarlık Sembolleri ve Unvanlar", Renk.TURUNCU),
        p.etiket(645, 195, 470, 58, "Hutbe Okutmak ve Halifeden Menşur (Onay Belgesi) Almak", Renk.SARI),
        p.etiket(645, 270, 470, 58, "Tıraz / Hil'at (Halifenin Gönderdiği Süslü Elbise ve Sancak)", Renk.TURUNCU),
        p.etiket(645, 345, 470, 58, "Çetr (Saltanat Şemsiyesi), Tevki/Tuğra, Nevbet, Otağ, Taht", Renk.YESIL),
        p.etiket(645, 420, 470, 58, "Unvanlar: Karahanlı (Han/Kara/İlig), Gazneli ve Selçuklu (Sultan)", Renk.MAVI),
        p.etiket(645, 495, 470, 52, "Türkiye Selçukluları: Keyhüsrev, Keykavus, Keykubat, Rükneddin", Renk.MOR),
        p.alt_serit("Türk tarihinde 'Sultan' unvanını ilk kez Gazneli Mahmut kullanmış; Tuğrul Bey ise 'Doğu'nun ve Batı'nın Sultanı' ilan edilmiştir."),
    ]
    return kart_16_9(s)


def gorsel_2():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("MERKEZ TEŞKİLATINDA DEĞİŞİM: KURULTAYDAN DİVAN SİSTEMİNE", "Büyük Selçuklu ve Türkiye Selçuklu Devletlerinde Divan Teşkilatı"),
        p.panel(55, 130, 1090, 145, "Divan-ı Saltanat (Büyük Divan) — Başkan: Vezir (Sahib-i Divan-ı Devlet)", Renk.SARI),
        p.metin(600, 215, "İslamiyet öncesi Kurultay'ın (Toy) yerini İran-İslam devlet geleneğinin etkisiyle kurumsallaşan 'Divan-ı Saltanat' ve ona bağlı dört alt divan almıştır:", 15, "#F8FAFC", "middle", False),
        p.panel(55, 295, 255, 275, "1. Divan-ı Tuğra (İnşa)", Renk.MAVI),
        p.etiket(75, 360, 215, 55, "Başkan: Tuğraî / Münşî", Renk.MAVI),
        p.metin(182, 465, "Devletin iç ve dış\nyazışmalarını yürütür;\nhükümdar fermanlarına\ntuğra çeker.", 14, "#E2E8F0", "middle", False),
        p.panel(333, 295, 255, 275, "2. Divan-ı İstifa", Renk.YESIL),
        p.etiket(353, 360, 215, 55, "Başkan: Müstevfî", Renk.YESIL),
        p.metin(460, 465, "Devletin bütün mali\nişlerinden, gelir-gider\nhesaplarından ve bütçeden\nsorumludur.", 14, "#E2E8F0", "middle", False),
        p.panel(611, 295, 255, 275, "3. Divan-ı İşraf", Renk.TURUNCU),
        p.etiket(631, 360, 215, 55, "Başkan: Müşrif", Renk.TURUNCU),
        p.metin(738, 465, "Askerî ve hukuki işler\ndışındaki tüm idari ve\nmali kurumları denetler\n(Teftiş kurulu).", 14, "#E2E8F0", "middle", False),
        p.panel(889, 295, 256, 275, "4. Divan-ı Arz (Ceyş)", Renk.MOR),
        p.etiket(909, 360, 216, 55, "Başkan: Emir-i Arz", Renk.MOR),
        p.metin(1017, 465, "Ordunun ihtiyaçlarını,\nteçhizatını, asker kayıtlarını\nve maaşlarını (bisteganî)\ndüzenler.", 14, "#E2E8F0", "middle", False),
        p.alt_serit("Türkiye Selçuklularında ayrıca hükümdar yokken vekâlet eden Naib-i Saltanat (Niyabet-i Saltanat) ve arazi kayıtlarını tutan Pervaneci bulunurdu."),
    ]
    return kart_16_9(s)


def gorsel_3():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("ORDU TEŞKİLATINDA DÖNÜŞÜM: BÜYÜK SELÇUKLU VE TÜRKİYE SELÇUKLU ORDUSU", "Bozkırın Gönüllü Atlılarından Gulam ve İkta Sistemine Dayalı Profesyonel Orduya"),
        p.panel(55, 130, 525, 440, "1. Gulam (Kapıkulu) Sistemi", Renk.TURUNCU),
        p.etiket(85, 195, 465, 65, "Gulamhane'de Özel Eğitim:\nFarklı milletlerden gençler İslam ve askerlik eğitimi alır.", Renk.TURUNCU),
        p.etiket(85, 280, 465, 65, "Gulamân-ı Saray (Hassa Ordusu):\nDoğrudan Sultan'a bağlı, merkezde bulunan daimî birlikler.", Renk.SARI),
        p.etiket(85, 365, 465, 65, "Bisteganî (Maaş):\nYılda dört kez (üç ayda bir) hazineden nakit maaş alırlar.", Renk.MAVI),
        p.metin(317, 485, "İlk kez Karahanlı ve Gaznelilerde uygulanmış,\nBüyük Selçuklularda Nizamülmülk ile zirveye ulaşmıştır.", 14, "#E2E8F0", "middle", False),
        p.panel(615, 130, 530, 440, "2. İkta Sistemi ve Sipahiler (Eyalet Askerleri)", Renk.YESIL),
        p.etiket(645, 195, 470, 65, "Toprak Geliri Karşılığı Asker:\nDevlet, mîrî arazinin vergi gelirini komutan/memurlara bırakır.", Renk.YESIL),
        p.etiket(645, 280, 470, 65, "İkta Askerleri (Cebelü / Sipahi):\nİkta sahibi, gelirle orantılı sayıda tam teçhizatlı atlı asker besler.", Renk.MAVI),
        p.etiket(645, 365, 470, 65, "Hazineye Yük Olmadan Büyük Ordu + Tarımsal Üretim + Güvenlik", Renk.MOR),
        p.metin(880, 485, "Türkiye Selçukluları ayrıca denizciliğe yönelerek\nEmirü's-Sevahil (Reisü'l-Bahr) komutasında DONANMA kurmuştur!", 14, "#FDE047", "middle", True),
        p.alt_serit("İkta sistemi sayesinde hem hazineden para çıkmadan devasa bir atlı ordu beslenmiş hem de taşrada üretim ve asayiş sağlanmıştır."),
    ]
    return kart_16_9(s)


def gorsel_4():
    p = Primitifler()
    s = [
        p.arkaplan_16_9("#0F172A"),
        p.baslik_16_9("TAŞRA TEŞKİLATI VE HUKUK SİSTEMİ", "Melikler, Atabeyler ve Şer'î - Örfî Yargı Ayrımı"),
        p.panel(55, 130, 530, 440, "Taşra (Eyalet) Yönetimi ve Atabeylik", Renk.MAVI),
        p.etiket(85, 195, 470, 65, "Melik: Eyaletlere yönetici olarak gönderilen hanedan üyeleri", Renk.MAVI),
        p.etiket(85, 280, 470, 65, "Atabey: Meliklerin siyasi ve askerî eğitmeni olan tecrübeli komutan", Renk.TURUNCU),
        p.etiket(85, 365, 470, 65, "Şıhne: Eyaletlerdeki askerî vali  |  Amîd: Sivil yönetici", Renk.YESIL),
        p.etiket(85, 450, 470, 65, "Muhtesip: Çarşı ve pazarları, ölçü-tartıyı denetleyen görevli", Renk.SARI),
        p.panel(615, 130, 530, 440, "Türk-İslam Devletlerinde Hukuk Sistemi", Renk.MOR),
        p.etiket(645, 195, 470, 85, "1. Şer'î Hukuk (İslam Hukuku):\nEvlenme, boşanma, miras, vakıf ve ticaret davalarına bakar.\nBaşkan: Kadiü'l-Kudat (Başkadı)", Renk.YESIL),
        p.etiket(645, 300, 470, 85, "2. Örfî Hukuk (Töre ve Kanunlar):\nDevlet düzenini bozanlara, asayiş ve vergi suçlarına bakar.\nBaşkan: Emir-i Dad", Renk.TURUNCU),
        p.etiket(645, 405, 470, 85, "3. Askerî Yargı ve Divan-ı Mezalim:\nOrdu davalarına Kadıasker (Kazasker) bakar.\nYüksek mahkeme olan Divan-ı Mezalim'e bizzat Sultan başkanlık eder.", Renk.MAVI),
        p.alt_serit("Merkezî otorite zayıfladığında Atabeylerin bağımsızlık ilan etmesi (Zengiler, İldenizliler, Salgurlular) devletin parçalanmasına yol açmıştır."),
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
