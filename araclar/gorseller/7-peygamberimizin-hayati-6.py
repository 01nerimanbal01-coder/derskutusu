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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HÜZÜN YILINDAN İLAHİ TESELLİYE: İSRA VE MİRAÇ</text>'
    ic += _kart(30, 56, 195, 160, "Tarihsel Arka Plan", ["Boykot yıllarının yorgunluğu", "Hüzün Yılı (Hz. Hatice &amp; Ebu Talib)", "Taif yolculuğu ve sıkıntılar", "Yüce Allah'ın ilahi ikramı"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "İsra (Gece Yürüyüşü)", ["Mescid-i Haram'dan (Mekke)", "Mescid-i Aksa'ya (Kudüs)", "İsra suresi 1. ayette geçer", "Cebrail (a.s.) eşliğinde"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Miraç (Yükseliş)", ["Mescid-i Aksa'dan göklere", "Peygamberlerle buluşma", "Sidretü'l-Münteha makamı", "İlahi kudret ayetlerini görme"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MİRAÇ GECESİNİN ÜÇ BÜYÜK HEDİYESİ</text>'
    ic += _kart(30, 56, 195, 160, "1. Beş Vakit Namaz", ["Müminin miracı: Namaz", "Günde 5 vakit farz kılındı", "Sevap bakımından 50 vakte denk", "Doğrudan Miraç'ta emredildi"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "2. Âmenerrasûlü Ayetleri", ["Bakara suresi 285-286. ayetler", "İman esaslarının özeti", "Gücümüzün üstünde yük yok", "Af, mağfiret ve rahmet duası"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "3. Bağışlanma Müjdesi", ["Allah'a şirk koşmayanların", "Büyük günahlarının affı", "Cennete girme müjdesi", "Tevhit ehli için büyük ümit"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">İSRA SURESİNDEKİ AHLAKİ İLKELER (MİRAÇ BİLDİRİSİ)</text>'
    ic += _kart(30, 56, 195, 160, "Tevhit ve Anne-Baba", ["Yalnız Allah'a kulluk etmek", "Anne-babaya 'öf' bile dememek", "Onlara güzel söz söylemek", "Merhamet kanatlarını germek"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Yardımlaşma ve İtidal", ["Akrabaya, yoksula, yolcuya hak", "Saçıp savurmamak (İsraf yok)", "Eli sıkı olmamak (Cimrilik yok)", "Cömertlikte dengeyi korumak"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Adalet ve Dürüstlük", ["Yetim malına dokunmamak", "Verilen sözü yerine getirmek", "Ölçü ve tartıyı tam yapmak", "Bilmediğin şeyin ardına düşmemek"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MİRAÇ OLAYI KARŞISINDA TUTUMLAR VE KUDÜS BİLİNCİ</text>'
    ic += _kart(30, 56, 195, 160, "Hz. Ebubekir'in Sadakati", ["'O söylediyse doğrudur!'", "Tereddütsüz iman ve tasdik", "'Es-Sıddık' unvanını alması", "Gerçek dostluk ve bağlılık"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Mescid-i Aksa ve Kudüs", ["Müslümanların ilk kıblesi", "Etrafı mübarek kılınan belde", "Peygamberler halkasının bağı", "İslam dünyasının ortak mirası"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Mümin İçin Mesajı", ["Her zorlukla bir kolaylık vardır", "Sabrın sonu ilahi lütuftur", "Namazla ruhen yükselmek", "Ahlaki ilkeleri kuşanmak"], "#f1f5f9", "#64748b", "#334155")
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
