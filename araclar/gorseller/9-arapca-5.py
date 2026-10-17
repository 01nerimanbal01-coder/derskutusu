def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Arapçada Munfasıl (Ayrık) Tekil Kişi Zamirleri (9.1.1)</text>'
    c += _kart(18, 54, 206, 175, "1. Tekil Şahıs (Konuşan)", [
        "• Ene (Ben): Hem erkek",
        "  (müzekker) hem de kadın",
        "  (müennes) için ortaktır.",
        "• Örn: Ene talibun (Erkek)",
        "• Örn: Ene talibetun (Kız)",
        "• Cümle başında özne olur."
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 175, "2. Tekil Şahıs (Muhatap)", [
        "• Ente (Sen - Erkek): Tâ harfi",
        "  fethalı (üstünlü) okunur.",
        "• Enti (Sen - Kadın): Tâ harfi",
        "  kesralı (esreli) okunur.",
        "• Örn: Hel ente muallimun?",
        "• Örn: Hel enti muallimetun?"
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 175, "3. Tekil Şahıs (Gaib/Gaibe)", [
        "• Huve (O - Erkek): Müzekker",
        "  varlıklar için kullanılır.",
        "• Hiye (O - Kadın): Müennes",
        "  varlıklar için kullanılır.",
        "• Örn: Huve tabibun.",
        "• Örn: Hiye tabibetun."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Tanışma ve Hal-Hatır Sorma Diyalog Kalıpları</text>'
    c += _kart(18, 54, 314, 170, "İsim ve Memleket Sorma (Müzekker / Müennes)", [
        "• Mâ ismuke? (Adın ne? - Erkeğe) -> İsmî Ahmed.",
        "• Mâ ismuki? (Adın ne? - Kadına) -> İsmî Zeyneb.",
        "• Min eyne ente? (Nerelisin? - Erkeğe)",
        "• Min eyne enti? (Nerelisin? - Kadına)",
        "• Cevap: Ene min Turkiyâ / Ene Turkiyyun."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "Hal-Hatır ve Meslek Sorma", [
        "• Keyfe hâluke / hâluki? (Nasılsın?)",
        "• Cevap: Ene bi-hayrin, elhamdulillâh.",
        "• Men hâzâ? (Bu kim? - Erkek) -> Hâzâ sadîkî.",
        "• Men hâzihî? (Bu kim? - Kadın) -> Hâzihî sadîkatî.",
        "• Teşerraftu bi-ma\'rifetike (Tanıştığımıza memnun oldum)."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Müzekker - Müennes Uyumu ve Tâ-i Merbûta (Kapalı Tâ) Kuralı</text>'
    c += _kart(18, 54, 314, 170, "Müzekker (Eril) Kelimeler", [
        "• Sonunda müenneslik alameti (kapalı tâ) bulunmayan",
        "  eril isim ve sıfatlardır.",
        "• Örnekler: Tâlibun (erkek öğrenci), Muallimun",
        "  (erkek öğretmen), Mühendisun, Tabîbun, Cedîdun.",
        "• İşaret zamiri olarak \'Hâzâ\' (Bu) ile kullanılır."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 170, "Müennes (Dişil) Kelimeler", [
        "• Sonuna Tâ-i Merbûta (kapalı tâ: -etun / -atun)",
        "  eklenerek dişil yapılan isim ve sıfatlardır.",
        "• Örnekler: Tâlibetun (kız öğrenci), Muallimetun",
        "  (kadın öğretmen), Mühendisetun, Tabîbetun.",
        "• İşaret zamiri olarak \'Hâzihî\' (Bu) ile kullanılır."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Selamlaşma Adabı: Ayet, Hadis ve Hikmetli Sözler</text>'
    c += _kart(18, 54, 314, 165, "Kur\'an ve Sünnette Selamlaşma", [
        "• Selam: \'Es-selâmu aleykum ve rahmetullâh\'",
        "• Cevap: \'Ve aleykumu\'s-selâm ve rahmetullâhi",
        "  ve berekâtuh\' (daha güzeliyle veya misliyle).",
        "• Hadis-i Şerif: \'Aranızda selamı yayınız!\'",
        "  (Efşû\'s-selâme beynekum)."
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 165, "Sosyal İfadeler ve Günlük Kalıplar", [
        "• Ehlen ve sehlen (Hoş geldiniz) -> Ehlen bike/biki",
        "• Sabâhu\'l-hayr (Günaydın) -> Sabâhu\'n-nûr",
        "• Mesâu\'l-hayr (İyi akşamlar) -> Mesâu\'n-nûr",
        "• İle\'l-likâ / Ma\'a\'s-selâme (Görüşmek üzere /",
        "  Güle güle)."
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
