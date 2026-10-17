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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MEDİNE’DE İSLAM TOPLUMUNU İNŞA EDEN İLK ADIMLAR</text>'
    ic += _kart(30, 56, 195, 160, "1. Mescid-i Nebi", ["İbadet ve cemaat merkezi", "Devlet yönetim ve istişare yeri", "Eğitim yuvası: Suffe", "Toplumsal kaynaşma alanı"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "2. Muâhât (Kardeşlik)", ["Ensar ve Muhacir kardeşliği", "Evini ve işini paylaşma (İsar)", "Evs ve Hazrec barışı", "İman kardeşliği bilinci"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "3. Medine Sözleşmesi", ["Toplumsal barış ve güvenlik", "Din ve vicdan özgürlüğü", "Ortak savunma ilkesi", "Tarihin ilk yazılı anayasası"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MESCİD-İ NEBİ VE SUFFE OKULU (ASHÂB-I SUFFE)</text>'
    ic += _kart(30, 56, 300, 160, "Mescid-i Nebi’nin İşlevleri", ["• Günde beş vakit cemaatle namaz kılınması", "• Elçilerin kabulü ve devlet kararlarının alınması", "• İhtiyaç sahiplerine yardımların ulaştırılması", "• Müslümanların sevinç ve üzüntülerini paylaşması"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(350, 56, 300, 160, "Suffe ve Ashâb-ı Suffe", ["• İslam’ın ilk yatılı eğitim kurumu (üniversitesi)", "• Kur’an, yazı ve dini ilimlerin öğrenilmesi", "• İslam’ı anlatmak üzere illere öğretmen gönderilmesi", "• En meşhur talebelerden biri: Ebu Hureyre (r.a.)"], "#e0f2fe", "#0284c7", "#0369a1")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ENSAR - MUHACİR KARDEŞLİĞİ VE MEDİNE PAZARI</text>'
    ic += _kart(30, 56, 195, 160, "Muhacir ve Ensar", ["Muhacir: Mekke’den göç eden", "Ensar: Medineli yardımcılar", "İsar: Kardeşini kendine tercih", "Abdurrahman b. Avf - Sa’d b. Rebi"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Medine Çarşısı (Pazar)", ["Ekonomik bağımsızlık adımı", "Vergisiz ve hilesiz ticaret", "Ölçü ve tartıda tam dürüstlük", "‘Bizi aldatan bizden değildir’"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Nüfus Sayımı &amp; Ezan", ["Müslümanların sayısının tespiti", "(İlk nüfus sayımı: 1500 kişi)", "Abdullah b. Zeyd’in rüyası", "İlk müezzin: Hz. Bilal-i Habeşi"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MEDİNE SÖZLEŞMESİ (VATANDAŞLIK ANTLAŞMASI)</text>'
    ic += _kart(30, 56, 195, 160, "Taraflar", ["Muhacirler ve Ensar (Evs-Hazrec)", "Medineli Yahudi kabileleri", "Diğer gayrimüslim Araplar", "Başkan ve Hakem: Hz. Peygamber"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Temel Maddeler", ["Herkes dininde serbesttir", "Zulüm ve haksızlık yasaktır", "Dış saldırıda şehir birlikte", "savunulacaktır"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Tarihsel Önemi", ["Çok kültürlü bir arada yaşama", "Hukukun üstünlüğü ilkesi", "İslam Devleti’nin resmen tanınması", "Toplumsal huzur ve güven"], "#f1f5f9", "#64748b", "#334155")
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
