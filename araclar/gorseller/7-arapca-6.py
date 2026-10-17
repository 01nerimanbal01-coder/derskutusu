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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ARAPÇADA MESLEKLER (EL-MİHEN) - ERİL VE DİŞİL</text>'
    ic += _kart(30, 56, 195, 160, "Eğitim &amp; Sağlık", ["Muallim / Muallime (Öğretmen)", "Tabîb / Tabîbe (Doktor)", "Mümerrid / Mümerrida (Hemşire)", "Saydalî / Saydaliyye (Eczacı)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Teknik &amp; Güvenlik", ["Mühendis / Mühendise", "Şurtî / Şurtıyye (Polis)", "Tayyâr / Tayyâre (Pilot)", "Cündî (Asker) - İtfâî (İtfaiyeci)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Hizmet &amp; Zanaat", ["Fellâh (Çiftçi) - Habbâz (Fırıncı)", "Hayyât (Terzi) - Neccâr (Marangoz)", "Hallâk (Berber) - Tabbâh (Aşçı)", "Sâik (Şoför) - Cezzâr (Kasap)"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MESLEKLER VE ÇALIŞMA YERLERİ (EYNE YA’MELÜ?)</text>'
    ic += _kart(30, 56, 195, 160, "Okul ve Hastane", ["El-Muallim -> fil-medrese", "(Öğretmen okulda çalışır)", "Et-Tabîb -> fil-müsteşfâ", "(Doktor hastanede çalışır)"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Fırın, Tarla ve Atölye", ["El-Habbâz -> fil-furn (Fırında)", "El-Fellâh -> fil-hakl (Tarlada)", "Et-Tabbâh -> fil-mat'am (Lokanta)", "El-Mühendis -> fil-masna' (Fabrika)"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Ulaşım ve Güvenlik", ["Et-Tayyâr -> fil-matâr (Havaalanı)", "Eş-Şurtî -> fî merkezil-emni", "El-Bâi' -> fis-sûk (Çarşıda)", "El-Kâdî -> fil-mahkeme"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">GELECEKTEKİ MESLEK TERCİHİ KALIPLARI (EL-MÜSTAKBEL)</text>'
    ic += _kart(30, 56, 195, 160, "Sorular", ["Mâ mihnetüke? (Mesleğin ne?)", "Mâzâ türîdü en tekûne?", "(Gelecekte ne olmak istiyorsun?)", "Fil-müstakbel (Gelecekte)"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Olumlu Cevap (Ürîdü)", ["Ürîdü en ekûne...", "(... olmak istiyorum)", "Ürîdü en ekûne tabîben", "Ürîdü en ekûne muallimeten"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Gelecek Zaman (Se-)", ["Se-ekûnü mühendisen", "(Mühendis olacağım)", "Se-a'melü fil-müsteşfâ", "(Hastanede çalışacağım)"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">FİİL ÇEKİMLERİ VE MESLEK GÖREVLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Çalışmak (Ya'melü)", ["Ene a'melü (Ben çalışıyorum)", "Ente ta'melü / Enti ta'melîne", "Hüve ya'melü (O çalışıyor - E)", "Hiye ta'melü (O çalışıyor - K)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Kim Ne Yapar?", ["El-muallimü yüderriüs-tullâb", "Et-tabîbü yüâlicül-merdâ", "El-habbâzü yasna'ul-hubz", "Et-tayyâru yakûdüt-tâira"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Dil Bilgisi İpucu", ["Müzekker -> Müennes: (-tun)", "Tabîb -> Tabîbetün", "Harf-i cer: fî (de/da)", "fil-medreseti (okulda)"], "#f1f5f9", "#64748b", "#334155")
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
