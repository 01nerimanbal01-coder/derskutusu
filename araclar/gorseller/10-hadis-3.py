# -*- coding: utf-8 -*-
import html as _html

def svg_basla(w, h):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{w}px;display:block;margin:12px auto;font-family:system-ui,-apple-system,sans-serif;">'

def svg_bitir():
    return '</svg>'

def Arka(w, h, renk="#f8fafc"):
    return f'<rect width="{w}" height="{h}" rx="14" fill="{renk}" stroke="#cbd5e1" stroke-width="1.5"/>'

def Baslik(w, metin, renk="#1e3a8a"):
    return (f'<rect x="16" y="10" width="{w-32}" height="28" rx="7" fill="{renk}"/>'
            f'<text x="{w//2}" y="29" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">{_html.escape(str(metin))}</text>')

def Kutu(x, y, w, h, dolgu="#ffffff", kenar="#94a3b8", kw=1.5, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Yazi(x, y, metin, punto=10, renk="#1e293b", hiza="middle", kalin=False):
    fw = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{punto}" fill="{renk}"{fw}>{_html.escape(str(metin))}</text>'

def Daire(cx, cy, r, dolgu="#3b82f6", kenar="#1d4ed8", kw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Cizgi(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'

def Cokgen(noktalar, dolgu="#bbf7d0", kenar="#15803d", kw=2):
    pts = " ".join(f"{x},{y}" for x, y in noktalar)
    return f'<polygon points="{pts}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Ok(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'

def kaydet(*args):
    pass



def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HADİS İLMİ KAVRAMLARININ DÖRT ANA KATEGORİDE SINIFLANDIRILMASI", "#0f766e")

    kategoriler = [
        ("1. HADİSİN YAPISAL UNSURLARI", "• Sened (İsnad): Râvîler zinciri\n• Metin: Hadisin sözlü/fiilî mesaj kısmı\n• Tarîk (Vecih): Alternatif sened kolları", "#2563eb", "#dbeafe"),
        ("2. HADİSİN AKTARIM SÜRECİ", "• Rivâyet: Hadisi senediyle nakletme\n• Tahammül: Hadisi hocadan öğrenip alma\n• Edâ: Öğrenilen hadisi talebeye aktarma", "#059669", "#d1fae5"),
        ("3. AKTARAN NESİLLER VE KİŞİLER", "• Sahâbî: Hz. Peygamber'i mümin olarak gören\n• Tâbiî: Sahâbîyi mümin olarak gören nesil\n• Râvî: Hadisi nakleden her bir kimse", "#d97706", "#fef3c7"),
        ("4. HADİS ÂLİMLERİ UNVANLARI", "• Müsnid → Muhaddis → Hâfız → Hüccet\n• Hâkim → Emîrü'l-Mü'minîn fi'l-Hadîs\n• (Bilgi ve ezber derecesine göre hiyerarşi)", "#7c3aed", "#f3e8ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(kategoriler):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 96
        s += Kutu(x, y, 312, 84, ar, r, 2, 10)
        s += Kutu(x, y, 312, 26, r, r, 1, 10)
        s += Yazi(x + 156, y + 18, bas, 9.5, "#ffffff", "middle", True)
        for j, satir in enumerate(acik.split("\n")):
            s += Yazi(x + 14, y + 44 + j * 16, satir, 8.8, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BİR HADİSİN ANATOMİSİ: SENED (İSNAD) VE METİN", "#1e3a8a")

    # Sol: Sened Zinciri
    s += Kutu(24, 48, 360, 152, "#eff6ff", "#2563eb", 2, 10)
    s += Yazi(204, 70, "1. SENED / İSNAD (Râvîler Zinciri — Dayanak)", 10.5, "#1d4ed8", "middle", True)

    raviler = [
        ("Hz. Peygamber (sav)", "#047857", "#d1fae5"),
        ("Sahâbî: Hz. Ömer b. Hattâb (ra)", "#0284c7", "#e0f2fe"),
        ("Tâbiî: Alkame b. Vakkâs → Yahyâ b. Saîd", "#2563eb", "#dbeafe"),
        ("Musannif (Derleyen): İmam Buhârî", "#4f46e5", "#e0e7ff")
    ]
    for i, (ad, r, ar) in enumerate(raviler):
        y = 82 + i * 28
        s += Kutu(44, y, 320, 22, ar, r, 1.2, 6)
        s += Yazi(204, y + 15, ad, 9, r, "middle", True)

    s += Ok(386, 124, 404, 124, "#1e3a8a", 2.5)

    # Sağ: Metin
    s += Kutu(408, 48, 248, 152, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(532, 70, "2. METİN (Hadisin Söz Kısmı)", 10.5, "#047857", "middle", True)
    s += Kutu(424, 86, 216, 98, "#ffffff", "#059669", 1.5, 8)
    s += Yazi(532, 110, "« إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ »", 12, "#065f46", "middle", True)
    s += Yazi(532, 136, "\"Ameller ancak niyetlere", 9.8, "#1e293b", "middle", True)
    s += Yazi(532, 154, "göredir...\"", 9.8, "#1e293b", "middle", True)
    s += Yazi(532, 174, "(Buhârî, Bed'ü'l-Vahy, 1)", 8.8, "#64748b", "middle", False)

    s += Kutu(24, 210, 632, 32, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(340, 230, "Abdullah b. Mübârek: \"İsnad (sened) dindendir; eğer isnad olmasaydı dileyen dilediğini (din adına) söylerdi.\"", 9.5, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HADİS ÖĞRENME VE AKTARMA SÜRECİ: TAHAMMÜL VE EDÂ", "#6d28d9")

    s += Kutu(26, 52, 290, 140, "#e0f2fe", "#0284c7", 2, 10)
    s += Yazi(171, 76, "1. TAHAMMÜLÜ'L-HADÎS", 11, "#0369a1", "middle", True)
    s += Yazi(171, 96, "(Hadisi Hocadan Alma / Öğrenme)", 9.5, "#0284c7", "middle", True)
    s += Yazi(40, 122, "• Talebenin hadisi hocasından bizzat", 9.2, "#1e293b", "start", False)
    s += Yazi(40, 140, "  dinleyerek (semâ'), okuyarak (kıraat)", 9.2, "#1e293b", "start", False)
    s += Yazi(40, 158, "  veya icâzetle teslim alıp ezberlemesi.", 9.2, "#1e293b", "start", False)

    s += Ok(318, 122, 362, 122, "#6d28d9", 2.5)
    s += Yazi(340, 112, "RİVÂYET", 9, "#6d28d9", "middle", True)

    s += Kutu(364, 52, 290, 140, "#f3e8ff", "#7c3aed", 2, 10)
    s += Yazi(509, 76, "2. EDÂÜ'L-HADÎS", 11, "#6d28d9", "middle", True)
    s += Yazi(509, 96, "(Hadisi Başkasına Aktarma / Öğretme)", 9.5, "#7c3aed", "middle", True)
    s += Yazi(378, 122, "• Râvînin usulüne uygun olarak aldığı", 9.2, "#1e293b", "start", False)
    s += Yazi(378, 140, "  hadisi, senedini zikrederek (haddesenâ /", 9.2, "#1e293b", "start", False)
    s += Yazi(378, 158, "  ahberenâ lafızlarıyla) talebelerine nakletmesi.", 9.2, "#1e293b", "start", False)

    s += Kutu(26, 204, 628, 32, "#ecfdf5", "#059669", 1.5, 8)
    s += Yazi(340, 224, "Kısaca: Hadisi öğrenip yüklenmek 'TAHAMMÜL', emaneti sonraki nesle eksiksiz teslim etmek 'EDÂ'dır.", 9.6, "#065f46", "middle", True)
    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HADİS ÂLİMLERİNİN İLMİ UNVAN HİYERARŞİSİ", "#b45309")

    basamaklar = [
        ("1. RÂVÎ / MÜSNİD", "Hadisi senediyle rivayet eden (anlam ve usul uzmanı olması şart olmayan) kimse", "#64748b", "#f1f5f9", 580),
        ("2. MUHADDİS", "Hadisleri sened ve metin yönünden bilen, birçok hadis kaynağını ve râvîyi tanıyan âlim", "#0284c7", "#e0f2fe", 520),
        ("3. HÂFIZ", "Yüz bin (100.000) hadisi sened ve metinleriyle ezbere bilen hadis âlimi", "#059669", "#d1fae5", 460),
        ("4. HÜCCET", "Üç yüz bin (300.000) hadisi sened, metin ve râvî halleriyle ezbere bilen âlim", "#d97706", "#fef3c7", 400),
        ("5. HÂKİM / EMÎRÜ'L-MÜ'MİNÎN Fİ'L-HADÎS", "Mertebelerin zirvesi: Tüm hadisleri bilen otorite (Buhârî, Müslim, Ahmed b. Hanbel)", "#dc2626", "#fef2f2", 340)
    ]

    for i, (ad, acik, r, ar, w) in enumerate(basamaklar):
        y = 198 - i * 38
        x = (W - w) // 2
        s += Kutu(x, y, w, 34, ar, r, 1.8, 6)
        s += Yazi(W // 2, y + 14, ad, 9.2, r, "middle", True)
        s += Yazi(W // 2, y + 28, acik, 8.3, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-hadis-3", 1, gorsel_1())
    kaydet("10-hadis-3", 2, gorsel_2())
    kaydet("10-hadis-3", 3, gorsel_3())
    kaydet("10-hadis-3", 4, gorsel_4())


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
