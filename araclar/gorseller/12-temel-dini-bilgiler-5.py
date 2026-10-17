def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#0284c7", bg="#f0f9ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İslam İnancının Özü: Tevhid İlkesi ve Boyutları</text>'
    ic += _kart(20, 45, 230, 175, "Zâtında Tevhid", [
        "• Allah\'ın zâtında bir ve tek olması",
        "• Eşi, benzeri ve dengi olmaması",
        "• Doğmamış ve doğurmamış olması",
        "• Vâcibü\'l-Vücûd (Zorunlu Varlık)",
        "• İhlas Suresi\'nin temel mesajı"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(265, 45, 230, 175, "Sıfatlarında Tevhid", [
        "• Kemâl sıfatların yalnızca O\'na aitliği",
        "• İlim, Kudret, İrade\'de benzersizlik",
        "• Yaratmada (Tekvin) ortağı olmaması",
        "• Eksiklikten münezzeh olma (Tenzih)",
        "• Esma-i Hüsna\'nın tecellisi"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 175, "İbadette Tevhid (Ulûhiyet)", [
        "• Yalnızca Allah\'a kulluk etme",
        "• Yalnızca O\'ndan yardım dileme",
        "• Şirk ve riyadan uzak samimi ihlas",
        "• Kula kulluktan özgürleşme",
        "• İyyâke na\'büdü ve iyyâke nestaîn"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İman ve Salih Amel Bütünlüğü (Asr Suresi Çerçevesinde)</text>'
    ic += _kart(20, 45, 225, 175, "1. Kalpte İman (Kök)", [
        "• Kalp ile tasdik, dil ile ikrar",
        "• Tevhid, nübüvvet ve ahiret bilinci",
        "• Amellerin kabul şartı ve temeli",
        "• İnsana anlam ve gaye kazandırır",
        "• Ağacın toprağa tutunan kökü"
    ], "#15803d", "#f0fdf4")
    ic += '<path d="M250 130 L265 130" stroke="#0f172a" stroke-width="3"/>'
    ic += _kart(268, 45, 225, 175, "2. Salih Amel (Gövde ve Meyve)", [
        "• İmanın davranışa dönüşmüş hali",
        "• İbadet, güzel ahlak ve hayır işleri",
        "• İmanı korur, besler ve güçlendirir",
        "• İhlas ve sünnete uygunluk şartı",
        "• Ağacın dalı, yaprağı ve meyvesi"
    ], "#d97706", "#fffbeb")
    ic += '<path d="M498 130 L513 130" stroke="#0f172a" stroke-width="3"/>'
    ic += _kart(515, 45, 225, 175, "3. Hakkı ve Sabrı Tavsiye", [
        "• Bireysel imandan toplumsal inşaya",
        "• Adaleti ve doğruluğu yayma",
        "• Zorluklara karşı ortak direnç",
        "• Hüsrandan kurtuluşun reçetesi",
        "• Erdemli ve huzurlu toplum"
    ], "#2563eb", "#eff6ff")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İslam İnancında İnsanın Konumu ve Değeri</text>'
    ic += _kart(20, 45, 170, 175, "Ahsen-i Takvîm", [
        "• En güzel biçimde yaratılış",
        "• Maddi ve manevi donanım",
        "• Akıl, kalp ve vicdan nimeti",
        "• Tîn Suresi 4. ayet vurgusu"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(203, 45, 170, 175, "Eşref-i Mahlûkat", [
        "• Yaratılmışların en şereflisi",
        "• İlahi ruh üflenmesi",
        "• İsrâ Suresi 70 (Kerramnâ)",
        "• Doğuştan gelen dokunulmaz onur"
    ], "#059669", "#ecfdf5")
    ic += _kart(386, 45, 170, 175, "Yeryüzü Halifesi", [
        "• Yeryüzünü imar ve ıslah",
        "• Adaleti tesis etme görevi",
        "• Bakara Suresi 30. ayet",
        "• İlahi emaneti taşıma (Ahzâb 72)"
    ], "#7c3aed", "#f5f3ff")
    ic += _kart(570, 45, 170, 175, "Cüz\'î İrade ve Teklîf", [
        "• Seçme özgürlüğü ve akıl",
        "• Hayır ve şer yolunu tercih",
        "• Amellerinden hesaba çekilme",
        "• Özgürlük-sorumluluk dengesi"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İnsanın Dört Boyutlu Sorumluluk Alanı</text>'
    ic += _kart(20, 45, 350, 175, "Allah\'a ve Kendisine Karşı Sorumluluklar", [
        "• Allah\'a karşı: İman, ibadet, şükür, dua ve ihlas (Zâriyât, 56)",
        "• Kendisine karşı: Beden ve ruh sağlığını (emaneti) koruma",
        "• Aklını ilim ve hikmetle geliştirme, nefsini kötülükten arındırma",
        "• Helal rızık kazanma ve vaktini verimli kullanma"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 175, "Topluma ve Çevreye (Tabiata) Karşı Sorumluluklar", [
        "• Topluma karşı: Kul hakkına riayet, adalet, merhamet, sıla-i rahim",
        "• Emanete riayet, sözünde durma ve yardımlaşma (infak)",
        "• Çevreye karşı: Tabiatı Allah\'ın ayeti ve emaneti olarak görme",
        "• İsraftan kaçınma, doğal dengeyi (mîzan) koruma ve fesadı önleme"
    ], "#b45309", "#fffbeb")
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
