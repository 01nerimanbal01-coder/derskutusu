def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'


def _kart(x, y, w, h, baslik, satirlar, bg, border, text_c):
    rx = 12
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}" stroke="{border}" stroke-width="2"/>'
    s += f'<text x="{x + w/2}" y="{y + 26}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{text_c}" text-anchor="middle">{baslik}</text>'
    s += f'<line x1="{x+12}" y1="{y+36}" x2="{x+w-12}" y2="{y+36}" stroke="{border}" stroke-width="1" stroke-dasharray="3,3"/>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x + w/2}" y="{y + 58 + i*22}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="middle">{st}</text>'
    return s


def gorsel_1():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HZ. MUSA’NIN (A.S.) DOĞUMU, MISIR VE MEDYEN YILLARI</text>'
    ic += _kart(30, 56, 195, 160, "Nil Nehri ve Saray", ["İsrailoğullarına Firavun zulmü", "Annesinin Nil’e bırakması", "Hz. Asiye’nin sahiplenmesi", "Firavun sarayında büyümesi"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Medyen’e Hicret", ["Mazluma yardım ederken kaza", "Medyen şehrine yolculuk", "Kuyuda iki kıza yardım etmesi", "Hz. Şuayb (a.s.) ile tanışma"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Peygamberlik Görevi", ["Medyen’de 10 yıl kalması", "Mısır’a dönerken Tûr Dağı", "Tuvâ Vadisi’nde ilk vahiy", "‘Kelîmullah’ unvanını alması"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HZ. MUSA’NIN MUCİZELERİ VE KARDEŞİ HZ. HARUN (A.S.)</text>'
    ic += _kart(30, 56, 195, 160, "Hz. Harun’un Desteği", ["Hz. Musa’nın samimi duası", "Hitabeti güçlü kardeşi Harun", "Vezir ve yardımcı peygamber", "Birlikte tebliğ sorumluluğu"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "İki Büyük Mucize", ["1. Asâ Mucizesi (Ejderha olması)", "Sihirbazların hilesini yutması", "2. Yed-i Beyzâ (Parlayan el)", "Sihirbazların secdeye kapanması"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "İlahi Kitap: Tevrat", ["Dört büyük kitaptan ilki", "Tûr Dağı’nda indirildi", "On Emir ve ahlaki ilkeler", "Ulu’l-Azm peygamberlerden biri"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">FİRAVUN İLE MÜCADELE VE KIZILDENİZ MUCİZESİ</text>'
    ic += _kart(30, 56, 195, 160, "Tebliğ ve Yumuşak Söz", ["Tâhâ 44: ‘Yumuşak söz söyleyin’", "Firavun’un ilahlık iddiası", "Kibir ve zulümde ısrar etmesi", "Uyarı musibetlerinden ders almama"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Kızıldeniz’in Yarılması", ["İsrailoğullarının Mısır’dan çıkışı", "‘Rabbim benimledir, yol gösterir!’", "Asâ ile denizin on iki yola ayrılması", "Müminlerin güvenle karşıya geçmesi"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Son Nefeste İman", ["Firavun ve ordusunun boğulması", "Son anda ‘İman ettim’ demesi", "Ümitsizlik anındaki iman geçersiz!", "Gelecek nesillere ibret olması"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HZ. MUSA KISSASINDAN KADER VE TEVEKKÜL DERSLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Kader ve İlahi Takdir", ["Allah’ın takdirini kimse bozamaz", "Firavun’un sarayında korunması", "Tedbir alıp Allah’a güvenmek", "Zulmün sonu daima hüsrandır"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Tevekkül ve Cesaret", ["En zor anda ümitsiz olmamak", "Mazlumun yanında yer almak", "Kardeşlik ve yardımlaşma", "Sabırla hakikati savunmak"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Hz. Musa’nın Duaları", ["‘Rabbim! Göğsüme genişlik ver’", "‘İşimi bana kolaylaştır’", "‘Rabbim! Bana indireceğin her", "hayra muhtacım’ (Kasas, 24)"], "#f1f5f9", "#64748b", "#334155")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    bolumler = v.get("bolumler", [])
    eslesme = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    for idx, key in eslesme:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[key]
