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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MÜMİN KİMLİĞİNİ OLUŞTURAN ÜÇ TEMEL BOYUT</text>'
    ic += _kart(30, 56, 195, 160, "1. İman Boyutu (Kök)", ["Kalp ile tasdik, dil ile ikrar", "Tevhit ve güven bilinci", "Altı iman esasına bağlılık", "Hayata anlam ve yön verme"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "2. İbadet Boyutu (Gövde)", ["İmanın eyleme dönüşmesi", "Namaz, oruç, zekât, dua", "Allah ile canlı bağ kurma", "Şükür ve sorumluluk bilinci"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "3. Ahlak Boyutu (Meyve)", ["İman ve ibadetin tezahürü", "Doğruluk, adalet, merhamet", "Elinden ve dilinden güven", "Salih amellerle örnek olma"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUR’AN-I KERİM’DE MÜMİNLERİN TEMEL VASIFLARI</text>'
    ic += _kart(30, 56, 195, 160, "Mü'minûn Suresi 1-9", ["Namazlarında huşu içindedirler", "Boş ve yararsız işten yüz çevirirler", "Zekâtlarını özenle verirler", "Emanet ve sözlerine sadıktırlar"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Enfâl Suresi 2-4", ["Allah anılınca kalpleri titrer", "Ayetler okununca imanları artar", "Yalnız Rablerine tevekkül ederler", "Rızıktan infak ederler"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Hucurât Suresi 10-12", ["Müminler ancak kardeştirler", "Alay ve lakap takmazlar", "Zandan ve gıybetten kaçınırlar", "Kardeşlerinin arasını düzeltirler"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">İBADETLERİN AHLAKİ DAVRANIŞLARA ETKİSİ</text>'
    ic += _kart(30, 56, 195, 160, "Namazın Etkisi", ["Kötülük ve hayasızlıktan korur", "Zaman bilinci ve disiplin katar", "Beden ve çevre temizliği sağlar", "Birlik ve cemaat ruhu verir"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Oruç ve Zekâtın Etkisi", ["Oruç sabır ve iradeyi güçlendirir", "Yoksulların halini anlamayı sağlar", "Zekât cimrilik ve bencilliği siler", "Toplumsal sevgi ve barışı kurar"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "İhsan Bilinci", ["Allah'ı görüyormuş gibi yaşamak", "Kimse yokken de dürüst kalmak", "Özü ile sözü bir olmak", "Her işi en güzel biçimde yapmak"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">GÜNLÜK HAYATTA MÜMİN KİMLİĞİNİN YANSIMALARI</text>'
    ic += _kart(30, 56, 195, 160, "Aile ve Okulda", ["Anne-baba ve öğretmene saygı", "Arkadaşlarla yardımlaşma", "Emaneti ve okul malını koruma", "Çalışkanlık ve sorumluluk"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Toplumda ve Çevrede", ["Komşu ve kul hakkına riayet", "Selamlaşma ve güler yüz", "Doğayı ve hayvanları koruma", "İsraftan uzak durma"], "#e0f2fe", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Dijital Dünyada", ["Doğru bilgi paylaşımı", "Siber zorbalıktan kaçınma", "Vakti faydalı işlerde kullanma", "Mahremiyete özen gösterme"], "#f1f5f9", "#64748b", "#334155")
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
