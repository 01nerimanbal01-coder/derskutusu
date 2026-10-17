def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Allah (cc), İnsan ve Kâinat İlişkisinde Deliller Bütünlüğü</text>'
        + _kart(25, 42, 300, 145, "1. Akli (Kevnî / Felsefi) Deliller", [
            "• Kâinat kitabını gözlem ve tefekkürle okuma",
            "• Gaye ve Nizam (Düzen ve Amaç) Delili",
            "• Hudûs (Sonradan Yaratılış) Delili",
            "• İmkân (Zorunlu Varlık / Vâcibü’l-Vücûd) Delili",
            "• Fıtrat ve Ahlak Delilleri"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "2. Naklî (Vahyi / Şer’î) Deliller", [
            "• Vahiy kitabını (Kur’an-ı Kerim) ve Sünneti okuma",
            "• İhlas Suresi: Tevhit ve Samediyet ilkesi",
            "• Enbiyâ 22: ”Lev kâne fîhimâ âlihetün...” (Tevhit)",
            "• Mülk 3-4: Evrende kusursuz ölçü ve denge",
            "• Peygamberlerin tebliği ve mucizeleri"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Kâinattaki Ölçüden Yaratıcıya Ulaştıran Temel Akli Deliller</text>'
        + _kart(20, 42, 200, 140, "Nizam (Gaye) Delili", [
            "• Evrendeki hassas ayar",
            "• Gezegen yörüngeleri, su",
            "  döngüsü, DNA dizilimi",
            "• Her düzen bir düzenleyiciyi",
            "  (Musavvir, Hakîm) gösterir"
        ], "#059669", "#ecfdf5")
        + _kart(240, 42, 200, 140, "Hudûs ve İmkân Delili", [
            "• Evren değişir ve sonradan",
            "  var olmuştur (hâdis)",
            "• Sonradan olan her şey bir",
            "  Yaratıcıya (Muhdis / Vâcibü’l-",
            "  Vücûd) muhtaçtır"
        ], "#d97706", "#fffbeb")
        + _kart(460, 42, 200, 140, "Burhân-ı Temânu’ (Tevhit)", [
            "• ”Eğer yerde ve gökte Allah’tan",
            "  başka ilahlar olsaydı ikisinin",
            "  de düzeni bozulurdu” (Enbiya 22)",
            "• Evrendeki tek düzen, Yaratıcının",
            "  birliğini (Vahdaniyet) kanıtlar"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 195, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Kur’an-ı Kerim’de Tefekkür, Âfâk (Dış Âlem) ve Enfüs (İç Âlem) Ayetleri</text>'
        + _kart(25, 42, 300, 138, "Âfâkî Deliller (Dış Dünyadaki İşaretler)", [
            "• Göklerin ve yerin yaratılışı (Âl-i İmrân 190)",
            "• Gece ile gündüzün birbiri ardınca gelişi",
            "• Yağmurun ölü toprağı diriltmesi (Rûm 50)",
            "• Gemilerin denizde akıp gitmesi ve rüzgârlar"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 138, "Enfüsî Deliller (İnsanın Kendi Yaratılışı)", [
            "• ”Kendi nefislerinizde de (ayetler var); görmüyor",
            "  musunuz?” (Zâriyât 21 ve Fussilet 53)",
            "• İnsanın en güzel biçimde (Ahsen-i takvîm) yaratılışı",
            "• Akıl, vicdan, dil, parmak izi ve fıtrat mucizesi"
        ], "#ea580c", "#fff7ed")
    )
    return _svg(680, 195, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'İnsanın Kâinattaki Konumu: Halifelik, Emanet ve Sorumluluk</text>'
        + _kart(20, 42, 200, 135, "1. Halife ve Muhatap", [
            "• Yeryüzünü imar etmekle",
            "  görevli iradeli varlık",
            "• İlahi emaneti (akıl ve",
            "  sorumluluk) yüklenmiştir"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 135, "2. Kâinatın Musahhar Oluşu", [
            "• Göklerde ve yerde olanlar",
            "  insanın hizmetine (teshir)",
            "  verilmiştir (Câsiye 13)",
            "• Nimet aynı zamanda sınavdır"
        ], "#16a34a", "#f0fdf4")
        + _kart(460, 42, 200, 135, "3. Çevre ve Mizan Bilinci", [
            "• ”Ölçüyü (mizanı) bozmayın”",
            "  (Rahmân 7-8)",
            "• İsraftan kaçınmak ve",
            "  doğal dengeyi korumak"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 190, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
