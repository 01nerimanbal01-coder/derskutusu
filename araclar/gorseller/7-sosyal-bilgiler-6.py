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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MİLLÎ MESELELER VE TÜRK TOPLUMUNUN KENETLENMESİ</text>'
    ic += _kart(30, 56, 195, 160, "Millî Mücadele Ruhu", ["Tekalif-i Milliye Emirleri", "Kuvâ-yı Millîye dayanışması", "Vatan savunmasında birlik", "Bağımsızlık kararlılığı"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Kıbrıs &amp; 15 Temmuz", ["1974 Kıbrıs Barış Harekâtı", "Ambargolara karşı ASELSAN", "15 Temmuz demokrasi zaferi", "Milli iradeye sahip çıkma"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Afetlerde Dayanışma", ["Deprem ve yangınlarda birlik", "Kızılay ve AFAD gönüllülüğü", "Yardım kampanyaları", "Tasada ve kıvançta ortaklık"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KÜRESELLEŞMENİN BOYUTLARI VE İNSAN HAYATINA ETKİSİ</text>'
    ic += _kart(30, 56, 195, 160, "İletişim ve Teknoloji", ["İnternet ve dijital ağlar", "Bilgiye anında erişim", "Dünyanın küresel köy olması", "Zaman-mekân sınırının kalkması"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Ekonomi ve Ticaret", ["Uluslararası e-ticaret", "Küresel tedarik zincirleri", "Çok uluslu şirketler", "Üretim ve tüketim hızı"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Kültürel Etkileşim", ["Farklı kültürleri tanıma", "Ortak küresel değerler", "Popüler kültür yayılımı", "Yerel kültürü koruma ihtiyacı"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KÜRESELLEŞMENİN OLUMLU VE OLUMSUZ YÖNLERİ</text>'
    ic += _kart(30, 56, 300, 160, "Olumlu Etkileri (Fırsatlar)", ["• Bilimsel ve tıbbi gelişmelerin hızlı paylaşımı", "• Uluslararası eğitim ve seyahat imkânları", "• Küresel sorunlara (iklim, salgın) ortak çözüm", "• Farklı toplumlar arası hoşgörü ve diyalog"], "#dcfce7", "#10b981", "#047857")
    ic += _kart(350, 56, 300, 160, "Olumsuz Etkileri (Riskler)", ["• Kültür emperyalizmi ve tek tipleşme (yozlaşma)", "• Aşırı tüketim çılgınlığı ve çevre kirliliği", "• Gelişmiş-gelişmekte olan ülke gelir uçurumu", "• Geleneksel el sanatları ve yerel dillerin zayıflaması"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MİLLÎ KİMLİĞİ KORUYARAK DÜNYA VATANDAŞI OLMAK</text>'
    ic += _kart(30, 56, 195, 160, "Öz Kültürünü Yaşatmak", ["Türkçeyi doğru kullanmak", "Millî ve manevi değerler", "Geleneksel sanatları koruma", "Tarih bilincine sahip olma"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Küresel Sorumluluk", ["İklim değişikliğiyle mücadele", "Sıfır atık ve doğa bilinci", "İnsan haklarına saygı", "Evrensel barışa katkı"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Bilinçli Tüketim", ["Yerli üretimi destekleme", "Dijital okuryazarlık", "Popüler kültürü sorgulama", "Üreten toplum olma hedefi"], "#f1f5f9", "#64748b", "#334155")
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
