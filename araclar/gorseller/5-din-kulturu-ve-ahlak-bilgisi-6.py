def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İhlas Suresi\'nin Kimlik Kartı ve Temel Özellikleri</text>'
    ic += _kart(20, 45, 230, 175, "Surenin Kimliği", [
        "• Mushaf sırası: 112. sure",
        "• Ayet sayısı: 4 ayet",
        "• İndirildiği yer: Mekke dönemi",
        "• Adının anlamı: Samimiyet,",
        "  içtenlik, katıksız kulluk"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "Neden İndirilmiştir?", [
        "• Mekkeli müşriklerin \'Bize",
        "  Rabbini anlat, soyunu söyle\'",
        "  sorusuna cevap olarak inmiştir",
        "• Tevhid inancını en özlü biçimde",
        "  açıklayan suredir"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 175, "Fazileti ve Önemi", [
        "• Kur\'an\'ın üçte birine (1/3)",
        "  denk kabul edilmiştir",
        "• Namazlarda Fâtiha\'dan sonra",
        "  en çok okunan suredir",
        "• Kelime-i Tevhid\'in açıklamasıdır"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İhlas Suresi\'nin 4 Ayeti, Okunuşu ve Anlamı</text>'
    ic += _kart(20, 45, 350, 185, "1 ve 2. Ayetler: Ehad ve Samed", [
        "• Bismillâhirrahmânirrahîm",
        "• 1. Kul hüvallâhü ehad:",
        "  \'De ki: O, Allah\'tır, bir tektir.\'",
        "• 2. Allâhü\'s-samed:",
        "  \'Allah Samed\'dir (Her şey O\'na muhtaçtır,",
        "   O ise hiçbir şeye muhtaç değildir).\'"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 185, "3 ve 4. Ayetler: Doğmamış ve Dengi Yoktur", [
        "• 3. Lem yelid ve lem yûled:",
        "  \'O doğurmamış ve doğmamıştır (Çocuğu,",
        "   annesi ve babası yoktur, ezelî-ebedîdir).\'",
        "• 4. Ve lem yekün lehû küfüven ehad:",
        "  \'Ve O\'nun hiçbir dengi (eşi, benzeri,",
        "   ortağı) yoktur.\'"
    ], "#1d4ed8", "#eff6ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İhlas Suresi\'nde Geçen Temel Kavramlar</text>'
    ic += _kart(20, 45, 230, 175, "İHLAS (الْإِخْلَاصُ)", [
        "• Samimiyet ve içtenlik demektir",
        "• İbadetleri gösterişten uzak,",
        "  yalnızca Allah rızası için yapmak",
        "• İmanı şirkten arındırmak",
        "• Kalbi tertemiz tutmak"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "EHAD (الْأَحَدُ)", [
        "• Allah\'ın Güzel İsimlerindendir",
        "• Zâtında, sıfatlarında ve",
        "  işlerinde bir ve tek olan",
        "• Bölünmeyen, eşi olmayan",
        "• Tevhid inancının özü"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 175, "SAMED (الصَّمَدُ)", [
        "• Allah\'ın Güzel İsimlerindendir",
        "• Bütün varlıkların kendisine",
        "  muhtaç olduğu, kendisi ise",
        "  hiçbir şeye muhtaç olmayan",
        "• Tüm dileklerin ve duaların mercii"
    ], "#9333ea", "#faf5ff")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İhlas Suresi\'nin Hayatımıza Kazandırdığı İlkeler</text>'
    ic += _kart(20, 45, 350, 175, "İnanç Dünyamızdaki Yeri", [
        "• Allah\'ın bir ve tek (Tevhid) olduğunu öğretir",
        "• Allah\'ın yaratılmışlara benzemediğini kavratır",
        "• Yalnızca Allah\'a kulluk etmemizi ve sadece O\'ndan",
        "  yardım dilememizi (Samed bilincini) sağlar",
        "• Bizi batıl inançlardan ve şirkten korur"
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Günlük İbadet ve Davranışlarımızdaki Yeri", [
        "• Beş vakit namazda Fâtiha\'dan sonra zamm-ı sure olarak okuruz",
        "• Hatim dualarında (3 İhlas 1 Fâtiha) okuruz",
        "• Yaptığımız her iyiliği \'ihlasla\' (samimiyetle) yapmayı öğreniriz",
        "• Sıkıntı ve darlık anında Samed olan Rabbimize dua ederiz",
        "• Ezan sonrası ve yatmadan önce okuyarak korunma dileriz"
    ], "#15803d", "#f0fdf4")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]
