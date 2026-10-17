def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "PEYGAMBERİMİZE İTAATİN KAPSAMI VE ALANLARI", 14, "#166534", "bold")
    cols = [
        (25, "1. İbadet Hayatında", "Namaz, oruç, zekât ve haccı", "Hz. Peygamber'in öğrettiği", "ve uyguladığı gibi eda etmek"),
        (248, "2. Hukuk ve Adalette", "Anlaşmazlıklarda onun", "verdiği hükmü gönül", "rızasıyla kabul etmek (Nisâ, 65)"),
        (471, "3. Ahlak ve Muamelatta", "Dürüstlük, merhamet, aile", "ve komşuluk ilişkilerinde", "onun üsve-i hasenesine uymak")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+102, 74, b, 12, "#15803d", "bold")
        ic += _metin(x+102, 104, s1, 11, "#334155")
        ic += _metin(x+102, 126, s2, 11, "#334155")
        ic += _metin(x+102, 148, s3, 11, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "HZ. PEYGAMBER'İN TASARRUF VE DAVRANIŞLARININ AYRIMI", 13, "#1e3a8a", "bold")
    ic += _kutu(28, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(183, 72, "Dinî ve التشريعي (Teşriî / Bağlayıcı) Sünnet", 11, "#1d4ed8", "bold")
    ic += _metin(183, 98, "• Peygamberlik (risalet) görevi gereği", 11, "#334155")
    ic += _metin(183, 120, "  inanç, ibadet, helal-haram ve ahlak", 11, "#334155")
    ic += _metin(183, 142, "  konularında koyduğu ilkelerdir.", 11, "#334155")
    ic += _metin(183, 168, "Hükmü: Bütün müminler için bağlayıcıdır.", 11, "#1e40af", "bold")

    ic += _kutu(362, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(517, 72, "Beşerî ve Tecrübî (Cibillî) Davranışlar", 11, "#1d4ed8", "bold")
    ic += _metin(517, 98, "• İnsan olması ve yaşadığı coğrafya gereği", 11, "#334155")
    ic += _metin(517, 120, "  yeme-içme, giyim, ziraat (hurma aşılama)", 11, "#334155")
    ic += _metin(517, 142, "  ve savaş taktiği (Bedir kuyuları) tercihleri.", 11, "#334155")
    ic += _metin(517, 168, "Hükmü: İstişare ve uzmanlığa açıktır.", 11, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fef2f2", "#ef4444", 12, 2)
    ic += _metin(350, 34, "SÜNNETTEN YÜZ ÇEVİRMENİN BİREYSEL VE TOPLUMSAL SONUÇLARI", 13, "#991b1b", "bold")
    items = [
        (25, "İbadetlerde Bozulma", "Kur'an'daki mücmel", "emirlerin nasıl uygulanacağı", "bilinemez hâle gelir"),
        (192, "Bid'at ve Hurafeler", "Sünnet terk edildiğinde", "boşluğu uydurma inanç", "ve bid'atler doldurur"),
        (359, "Tefrika ve Bölünme", "Ortak peygamber modeli", "kaybolunca ümmet içinde", "ayrılıklar baş gösterir"),
        (526, "Amellerin Boşa Gitmesi", "Peygamberin emrine", "muhalefet fitne ve azap", "uyarısına muhatap kılar")
    ]
    for x, b, s1, s2, s3 in items:
        ic += _kutu(x, 48, 150, 134, "#ffffff", "#f87171", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#b91c1c", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 120, s2, 10, "#334155")
        ic += _metin(x+75, 140, s3, 10, "#991b1b", "bold")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "ÖRNEK BİR SAHABİ: ÜMMÜ SELEME (RA) VE HUDEYBİYE FERASETİ", 13, "#6b21a8", "bold")
    ic += _kutu(28, 48, 644, 132, "#ffffff", "#c084fc", 10, 1.5)
    ic += _metin(350, 74, "Müminlerin Annesi Hz. Ümmü Seleme (Hind bint Ebû Ümeyye - ra)", 12, "#7e22ce", "bold")
    ic += _metin(350, 100, "• Habeşistan ve Medine'ye hicret eden ilk fedakâr müminlerdendir.", 11, "#334155")
    ic += _metin(350, 122, "• Hz. Âişe'den sonra en çok hadis rivayet eden (378 hadis) ve fetva veren âlim hanım sahabidir.", 11, "#334155")
    ic += _metin(350, 144, "• Hudeybiye Antlaşması'nda Hz. Peygamber'e sunduğu hikmetli istişare ile sahabilerin", 11, "#334155")
    ic += _metin(350, 164, "  itaat krizini aşmasını ve kurbanlarını kesip ihramdan çıkmasını sağlamıştır.", 11, "#581c87", "bold")
    return _svg(700, 210, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
