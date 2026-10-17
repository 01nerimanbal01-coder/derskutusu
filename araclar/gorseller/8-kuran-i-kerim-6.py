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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">AHSENÜ’L-KASAS: HZ. YAKUP VE HZ. YUSUF (A.S.) KISSASI</text>'
    ic += _kart(30, 56, 195, 160, "Peygamber Soyu", ["Dedesi: Hz. İshak (a.s.)", "Büyükbabası: Hz. İbrahim (a.s.)", "Babası: Hz. Yakup (İsrail)", "Yusuf suresi (12. sure)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Rüya ve Kuyu İmtihanı", ["11 yıldız, güneş ve ay rüyası", "Kardeşlerinin kıskançlığı (haset)", "Kuyuya atılması ve kervan", "Mısır’da saraya satılması"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Hz. Yakup’un Sabrı", ["‘Sabr-ı Cemîl’ (Güzel Sabır)", "İsyan etmeden Allah’a sığınma", "Ümidini asla kaybetmeme", "Evlat acısına metanetle dayanma"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">İFFET, ZİNDAN YILLARI VE MISIR HAZİNE BAKANLIĞI</text>'
    ic += _kart(30, 56, 195, 160, "İffet ve Sadakat", ["İftiraya karşı iffetini koruma", "Günaha girmektense zindanı", "tercih edecek kadar kararlı", "Allah’ın yardımıyla temize çıkma"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Zindanda Tebliğ", ["Zindanda tevhit daveti", "İki gencin rüyasını yorumlama", "Hükümdarın 7 semiz inek rüyası", "7 yıl bolluk, 7 yıl kıtlık"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Mısır Azizi (Bakan)", ["Hazine ve maliye yönetimi", "Bolluk yıllarında başak biriktirme", "Kıtlıkta adaletli dağıtım", "İlim, basiret ve güvenilirlik"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">AFFEDİCİLİK VE AİLENİN YENİDEN KAVUŞMASI</text>'
    ic += _kart(30, 56, 195, 160, "Kardeşlerle Karşılaşma", ["Kıtlıkta Mısır’a erzak gelişi", "Öz kardeşi Bünyamin’e kavuşma", "Kardeşlerin hatasını anlaması", "Pişmanlık ve özür dilemeleri"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Eşsiz Affedicilik", ["‘Bugün size kınama yoktur!’", "‘Allah sizi bağışlasın’ (Yusuf, 92)", "İntikam yerine merhamet", "Kardeşlik bağını onarma"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Rüyanın Gerçekleşmesi", ["Hz. Yakup’un gözlerinin açılması", "Ailenin Mısır’da buluşması", "Rüyasının yıllar sonra çıkması", "Şükür ve tevazu duası (Yusuf, 101)"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KISSADAN ÇIKARILACAK EVRENSEL AHLAKİ İLKELER</text>'
    ic += _kart(30, 56, 195, 160, "Hasetten Kaçınmak", ["Kıskançlık kardeşliği bozar", "Evlatlar arası adalet önemlidir", "Kötülük yapan kendi kaybeder", "Sevgi ve paylaşım esastır"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Sabır ve İffet", ["Zorlukta Sabr-ı Cemîl kuşanmak", "Harama karşı iffeti korumak", "Allah’tan ümidi kesmemek", "Doğruluktan ayrılmamak"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Affetmek ve Tedbir", ["Güçlüyken bağışlayıcı olmak", "Krizlere karşı planlı olmak", "Bollukta israf etmeyip biriktirmek", "Nimetleri Allah’tan bilmek"], "#f1f5f9", "#64748b", "#334155")
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
