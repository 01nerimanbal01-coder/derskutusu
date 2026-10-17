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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ARAPÇADA GEZİ TÜRLERİ VE MEKÂNLAR (ER-RIHLE)</text>'
    ic += _kart(30, 56, 195, 160, "Gezi Türleri", ["Rıhletün مدرسية (Okul gezisi)", "Rıhletün siyâhiyye (Turistik)", "Rıhletün ilmiyye (Bilimsel)", "Nüzhetün (Piknik / Kır gezisi)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Kültürel Mekânlar", ["El-müthaf (Müze)", "El-mecidüt-târîhî (Tarihi cami)", "El-kal’a (Kale) - El-kasr (Saray)", "El-mektebe (Kütüphane)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Doğal Mekânlar", ["El-ğâbe (Orman) - El-cibel (Dağ)", "El-bahr (Deniz) - Eş-şâtı (Sahil)", "El-hadîka (Park / Bahçe)", "El-muhayyem (Kamp alanı)"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ULAŞIM ARAÇLARI VE YOLCULUK HAZIRLIĞI</text>'
    ic += _kart(30, 56, 195, 160, "Ulaşım (Bi-vâsıtati)", ["Bil-hâfileti (Otobüsle)", "Bit-tâirati (Uçakla)", "Bil-kıtâri (Trenle)", "Bis-seyyâreti (Arabayla) - Sefîne"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Gezi Eşyaları", ["Hakîbetüs-sefer (Yol çantası)", "Cevâzüs-sefer (Pasaport)", "Tezkiratün (Bilet) - Harîta", "Âletüt-tasvîr (Fotoğraf makinesi)"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Temel Fiiller", ["Yüsâfiru (Seyahat ediyor)", "Yezhebü ilâ (…-e gidiyor)", "Yezûru (Ziyaret ediyor)", "Yeltakıtu suveran (Fotoğraf çeker)"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">CÜMLE BAĞLAÇLARI VE ZAMAN İFADELERİ</text>'
    ic += _kart(30, 56, 195, 160, "Sıralama Bağlaçları", ["Evvelen (İlk olarak / Önce)", "Sümme (Sonra / Daha sonra)", "Ba’de zâlike (Bundan sonra)", "Ahîran (Son olarak)"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Sebep ve Amaç", ["Li- (için): liziyâreti (ziyaret için)", "Li-enne (çünkü)", "Ve (ve) - Ev (veya)", "Lâkin (fakat / ama)"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Zaman Zarfları", ["Fil-utleti (Tatilde)", "Yevmel-cum’ati (Cuma günü)", "Ğaden (Yarın) - Emsi (Dün)", "Fil-usbu’il-kâdim (Gelecek hafta)"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">GEZİ DİYALOGLARINDA SORU KALIPLARI</text>'
    ic += _kart(30, 56, 300, 160, "Yer, Zaman ve Araç Soruları", ["• İlâ eyne tezhebü? (Nereye gidiyorsun?)", "• Metâ satبدأ er-rıhle? (Gezi ne zaman başlayacak?)", "• Keyfe / Bimâzâ tüsâfiru? (Nasıl seyahat ediyorsun?)", "• Ma’a men tezhebü? (Kiminle gidiyorsun?)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(350, 56, 300, 160, "Örnek Cevap Cümleleri", ["• Ezhebü ilâ İstanbul (İstanbul’a gidiyorum).", "• Satبدأ er-rıhle ğaden sabâhan (Yarın sabah).", "• Üsâfiru bil-hâfileti / bit-tâirati (Otobüsle / Uçakla).", "• Ezhebü ma’a usratî / asdikâî (Ailemle / Arkadaşlarımla)."], "#e0e7ff", "#6366f1", "#4338ca")
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
