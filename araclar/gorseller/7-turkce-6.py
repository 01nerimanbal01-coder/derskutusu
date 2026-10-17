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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MOTİVASYON VE ZAMAN YÖNETİMİ UNSURLARI</text>'
    ic += _kart(30, 56, 195, 160, "Hedef Belirleme", ["Net ve ulaşılabilir amaçlar", "Kısa ve uzun vadeli plan", "Azim ve kararlılık", "Adını Göklere Yazdıran Çocuk"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Zaman Yönetimi", ["Öncelik sırası oluşturma", "Zaman tuzaklarından kaçınma", "Verimli çalışma saatleri", "Erteleme alışkanlığını yenme"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "İçsel Motivasyon", ["Merak ve öğrenme tutkusu", "Zorluklar karşısında sabır", "Öz disiplin geliştirme", "Başarıya odaklanma"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">METİN İÇİ VE METİNLER ARASI KARŞILAŞTIRMA</text>'
    ic += _kart(30, 56, 195, 160, "Metin İçi Karşılaştırma", ["Kahramanların değişimi", "Olay öncesi ve sonrası", "Farklı karakterlerin tutumu", "Aynı metindeki zıtlıklar"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Metinler Arası Bakış", ["Konu ve tema ortaklığı", "Farklı metin türleri (Şiir/Öykü)", "Üslup ve bakış açısı farkı", "Verilen mesajın karşılaştırılması"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Bayrağımızın Altında", ["Millî birlik ve bağımsızlık", "Vatan sevgisi ve fedakârlık", "Ortak tarihsel bilinç", "Milli değerlerin aktarımı"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">METNİ ÇÖZÜMLEME VE ÖZETLEME ADIMLARI</text>'
    ic += _kart(30, 56, 195, 160, "1. Metni Çözümleme", ["Ana fikir ve yardımcı fikirler", "Yapı unsurları (Kişi, Yer, Zaman)", "Neden-sonuç ilişkileri", "Dil ve anlatım özellikleri"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "2. Seçme ve Ayıklama", ["Önemli olayları belirleme", "Gereksiz ayrıntıları çıkarma", "Tekrarlardan kaçınma", "Kronolojik sırayı koruma"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "3. Kendi Cümlelerinle Özet", ["Kısa ve öz ifade etme", "Kişisel yorum katmama", "Metnin anlamını bozmama", "Bağlaç ve geçişleri kullanma"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">YAZILI VE SÖZLÜ ANLATIMDA DÜŞÜNCEYİ GELİŞTİRME</text>'
    ic += _kart(30, 56, 195, 160, "Karşılaştırma &amp; Örnekleme", ["En, daha, ise, göre kullanımı", "Benzerlik ve farklılıklar", "Soyut fikri somutlaştırma", "Örneğin, mesela ifadeleri"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Tanımlama &amp; Tanık Gösterme", ["'... nedir?' sorusuna yanıt", "Öznel veya nesnel tanım", "Uzman görüşü ve alıntı söz", "İnandırıcılığı artırma"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Söz Varlığı ve Fiiller", ["Deyim ve atasözü kullanımı", "İş, oluş ve durum fiilleri", "Kip ve kişi ekleriyle çekim", "Bağlama uygun sözcük seçimi"], "#f1f5f9", "#64748b", "#334155")
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
