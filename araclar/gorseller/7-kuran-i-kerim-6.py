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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUNUT KAVRAMI VE VİTİR NAMAZINDA OKUNUŞU</text>'
    ic += _kart(30, 56, 195, 160, "Kunut Nedir?", ["Allah'a gönülden boyun eğmek", "Huşu ile itaat ve ibadet", "Namazda ayakta dua etmek", "Saygıyla divana durmak"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Ne Zaman Okunur?", ["Yatsıdan sonra Vitir namazında", "3. rekâtta Fatiha ve sureden sonra", "Rükûya gitmeden hemen önce", "Eller kulak hizasına kaldırılıp"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Nasıl Okunur?", ["Tekbir alınır (Allâhü Ekber)", "Eller tekrar bağlanır", "Kunut 1 ve Kunut 2 okunur", "Ardından rükû ve secde yapılır"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUNUT DUALARI - 1 (ALLÂHÜMME İNNÂ NESTEÎNÜKE)</text>'
    ic += _kart(30, 56, 300, 160, "Okunuşu", ["Allâhümme innâ nesteînüke", "ve nestağfirüke ve nestehdîk.", "Ve nü'minü bike ve netûbü ileyk.", "Ve netevekkelü aleyke ve nüsnî aleykel-hayr..."], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(350, 56, 300, 160, "Temel Mesajları", ["• Senden yardım, bağışlanma ve hidayet dileriz", "• Sana iman eder, Sana tövbe ederiz", "• Sana tevekkül eder (güvenir) ve Seni överiz", "• Nimetlerine şükreder, nankörlük etmeyiz"], "#e0f2fe", "#0284c7", "#0369a1")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUNUT DUALARI - 2 (ALLÂHÜMME İYYÂKE NA’BÜDÜ)</text>'
    ic += _kart(30, 56, 300, 160, "Okunuşu", ["Allâhümme iyyâke na'büdü", "ve leke nusallî ve nescüd.", "Ve ileyke nes'â ve nahfid.", "Nercû rahmeteke ve nahşâ azâbek..."], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(350, 56, 300, 160, "Temel Mesajları", ["• Yalnızca Sana kulluk ederiz", "• Senin için namaz kılar ve secdeye kapanırız", "• Sana koşar ve ibadete sevinçle yöneliriz", "• Rahmetini umar, azabından korkarız"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KUNUT DUALARINDA GEÇEN TEMEL İSLAMİ KAVRAMLAR</text>'
    ic += _kart(30, 56, 195, 160, "İstiâne ve İstiğfar", ["Nesteînüke: Yardım dileriz", "Nestağfirüke: Af dileriz", "Nestehdîk: Hidayet isteriz", "Kulluk bilincinin özü"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Tevekkül ve Şükür", ["Netevekkelü: Sana güveniriz", "Neşküruke: Sana şükrederiz", "Velâ nekfüruk: Nankör olmayız", "İman ve sadakat sözü"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Korku ve Ümit (Beyne)", ["Nercû rahmeteke: Rahmet ümidi", "Nahşâ azâbek: Azap endişesi", "Ümit ile korku dengesi", "Samimi ibadet bilinci"], "#f1f5f9", "#64748b", "#334155")
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
