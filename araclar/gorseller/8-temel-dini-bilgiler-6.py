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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUR’AN-I KERİM’E KARŞI BEŞ TEMEL SORUMLULUĞUMUZ</text>'
    ic += _kart(30, 56, 195, 160, "1. İman ve Saygı", ["Allah kelamı olduğuna inanmak", "Şüphe duymadan tasdik etmek", "Abdestli ve edeple tutmak", "Huşu ile dinlemek (A’râf, 204)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "2. Okumak ve Anlamak", ["Tertîl ve tecvitle okumak", "(Müzzemmil, 4)", "Meal ve tefsirinden anlamak", "Ayetler üzerinde تدبر (tedebbür)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "3. Yaşamak ve Tebliğ", ["Emir ve yasaklarına uymak", "Kur’an ahlakıyla ahlaklanmak", "Öğrenip başkalarına öğretmek", "‘En hayırlınız...’ (Hadis)"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUR’AN OKUMA VE DİNLEME ADABI</text>'
    ic += _kart(30, 56, 195, 160, "Okuma Öncesi Hazırlık", ["Abdest almak ve temiz olmak", "Kıbleye yönelip edeple oturmak", "Eûzü - Besmele çekmek", "(Nahl suresi, 98)"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Tertîl İle Okuma", ["Acele etmeden tane tane okumak", "Tecvit ve mahreçlere uymak", "Anlamını tefekkür etmek", "Sesini güzelleştirmek"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Dinleme Adabı", ["Sessizce ve saygıyla dinlemek", "Başka işle meşgul olmamak", "İlahi rahmete nail olmak", "Secde ayetinde tilavet secdesi"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUR’AN’I ANLAMA VE DÜŞÜNME KAVRAMLARI</text>'
    ic += _kart(30, 56, 195, 160, "Meal ve Tefsir", ["Meal: Ayetlerin yaklaşık anlamı", "Tefsir: Ayetlerin geniş açıklaması", "İndiriliş sebebi (Esbâb-ı Nüzul)", "Dil ve bağlam bütünlüğü"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Tedebbür ve Tefekkür", ["Tedebbür: Derinlemesine düşünmek", "(Sâd suresi, 29)", "‘Rabbim benden ne istiyor?’", "İbret ve öğüt almak"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Canlı Kur’an Olmak", ["Hz. Peygamber’in ahlakı:", "‘Onun ahlakı Kur’an idi’", "(Hz. Aişe r.a. sözü)", "Bilgiyi davranışa dönüştürmek"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KÜLTÜRÜMÜZDE KUR’AN SEVGİSİ VE SAYGISI</text>'
    ic += _kart(30, 56, 195, 160, "Mushaf Saygısı", ["En yüksek ve temiz yerde tutma", "Rahle ve Kur’an kılıfı kullanma", "Öpüp alnına koyma geleneği", "Hat ve tezhip sanatıyla süsleme"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Hafızlık ve Mukabele", ["Kur’an’ı baştan sona ezberleme", "Ramazan’da mukabele geleneği", "Hatim merasimleri ve duaları", "Nesilden nesile koruma"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Hayata Yansıtma", ["Sadece duvarda asılı bırakmamak", "Ailede ve toplumda adalet", "Doğruluk ve merhamet rehberi", "İki dünya mutluluğu (hidayet)"], "#f1f5f9", "#64748b", "#334155")
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
