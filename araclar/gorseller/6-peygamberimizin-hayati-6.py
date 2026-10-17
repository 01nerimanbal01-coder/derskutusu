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
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Hz. Peygamber\'in (s.a.v.) Gençlik Yıllarındaki Üstün Ahlaki Özellikleri</text>'
    ic += _kart(20, 45, 230, 185, "1. Doğruluk ve Güvenilirlik", [
        "• Asla yalan söylememesi (es-Sâdık)",
        "• Emanetleri canı gibi koruması",
        "• Mekke halkının ortak takdirle",
        "  \'Muhammedü\'l-Emîn\' lakabını vermesi",
        "• Ticarette tam dürüstlük"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "2. İffet, Haya ve Nezih Hayat", [
        "• Cahiliye kötülüklerinden uzak durma",
        "• Putlara asla tapmaması",
        "• İçki, kumar ve kötü eğlencelere",
        "  hiçbir zaman yaklaşmaması",
        "• İlahi koruma (İsmet sıfatı)"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "3. Adalet, Merhamet ve Yardım", [
        "• Mazlumların ve zayıfların yanında",
        "• Hılfü\'l-Fudûl (Erdemliler Cemiyeti)",
        "• Hacerü\'l-Esved hakemliği",
        "• Akrabayı, yetimi ve yoksulu gözetme",
        "• Alın teriyle helal rızık kazanma"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Gençlik Yıllarında Adalet ve Barış Öncülüğü: İki Tarihi Olay</text>'
    ic += _kart(20, 45, 350, 175, "Hılfü\'l-Fudûl (Erdemliler Topluluğu - 20 Yaş)", [
        "• Yemenli bir tüccarın Mekke\'de gasp edilen hakkını",
        "  korumak için Abdullah bin Cüd\'ân\'ın evinde kuruldu",
        "• Amaç: Mekke\'de yerli-yabancı hiçbir mazlumu",
        "  zalimin karşısında yalnız bırakmamak",
        "• Peygamberimiz: \'İslam\'da da böyle bir antlaşmaya",
        "  çağrılsam yine icabet ederim!\' buyurmuştur"
    ], "#1d4ed8", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Hacerü\'l-Esved Hakemliği (35 Yaş)", [
        "• Kâbe\'nin tamiri sırasında Hacerü\'l-Esved taşını yerine",
        "  koyma şerefi yüzünden kabileler arasında savaş çıkacaktı",
        "• Kâbe\'nin kapısından giren Muhammedü\'l-Emîn hakem seçildi",
        "• Hırkasını yere serip taşı üzerine koydu ve her kabile",
        "  temsilcisine bir ucundan tutturarak kan dökülmesini önledi"
    ], "#d97706", "#fffbeb")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Hz. Hatice\'nin (r.a.) İlk Vahiy Günündeki Tarihi Şahitliği</text>'
    ic += _kart(20, 45, 720, 175, "\'Vallahi Allah Seni Asla Mahcup Etmez ve Yalnız Bırakmaz!\' (Buhârî, Bed\'ü\'l-Vahy, 1)", [
        "• İlk vahiy geldiğinde heyecanlanan Hz. Peygamber\'i (s.a.v.) eşi Hz. Hatice (r.a.), onun gençlik yıllarından beri",
        "  sahip olduğu üstün ahlaki özelliklerini sayarak şöyle teselli etmiştir:",
        "• 1. \'Çünkü sen akrabalık bağlarını gözetirsin (Sıla-i rahim yaparsın).\'",
        "• 2. \'Sözün doğrusunu söylersin ve emaneti sahibine eksiksiz verirsin.\'",
        "• 3. \'İşini göremeyen güçsüzlerin yükünü taşırsın, yoksula ve kimsesize yardım edersin.\'",
        "• 4. \'Misafiri ağırlarsın ve hak yolunda felakete uğrayanların imdadına koşarsın!\'"
    ], "#0f766e", "#f0fdfa")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Peygamberimizin Gençlik Ahlakından Hayatımıza Çıkarımlar</text>'
    ic += _kart(20, 45, 350, 175, "Nübüvvet Öncesi Ahlakın Tebliğe Etkisi", [
        "• 40 yıllık tertemiz gençlik hayatı, onun peygamberliğinin",
        "  en güçlü delillerinden biri olmuştur (Yûnus Suresi, 16)",
        "• En azılı düşmanları (Ebû Cehil vb.) bile ona \'yalancı\'",
        "  diyememiş, güvenilirliğini itiraf etmek zorunda kalmıştır",
        "• Sözden önce \'yaşanan güzel ahlak\' kalpleri fethetmiştir"
    ], "#9333ea", "#faf5ff")
    ic += _kart(390, 45, 350, 175, "Bugünün Gençleri Olarak Bize Düşen Görevler", [
        "• Çevremizde \'güvenilir ve dürüst insan (emîn)\' olarak tanınmak",
        "• Kötü alışkanlıklar ve akran baskısına karşı iradeli durmak",
        "• Haksızlık karşısında mazlumun yanında yer almak (Adalet)",
        "• Ailemize yük olmadan çalışkan ve üretken olmak",
        "• Yaşlılara saygı, küçüklere ve yetimlere merhamet göstermek"
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
