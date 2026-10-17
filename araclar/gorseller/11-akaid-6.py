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
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Akaid İlminde İmanın Mahiyeti: Kalp ile Tasdik ve Dil ile İkrar</text>'
        + _kart(25, 42, 300, 145, "1. Kalp ile Tasdik (Asli Rükün)", [
            "• Hz. Peygamber’in Allah’tan getirdiği kesin",
            "  hükümleri (zarûrât-ı dîniyye) kalben onaylamak",
            "• İmanın değişmez özü ve rüknüdür.",
            "• Allah katında mümin sayılmanın temel şartıdır.",
            "• Şüphe barındırmayan kesin inançtır."
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "2. Dil ile İkrar (Dünyevi Şart)", [
            "• Kalpteki imanı kelime-i şehadet ile dilde",
            "  açıkça ifade etmektir.",
            "• Kişiye dünyada Müslüman muamelesi yapılması",
            "  (nikâh, miras, cenaze namazı) için şarttır.",
            "• İkrah (ölüm tehdidi) hâlinde dil ile inkâr",
            "  kalpte iman varsa imana zarar vermez (Nahl, 106)."
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'İcmâlî - Tafsîlî İman ve İmanın Artıp Eksilmesi Meselesi</text>'
        + _kart(25, 42, 300, 145, "Kapsamına Göre: İcmâlî ve Tafsîlî İman", [
            "• İcmâlî (Özet) İman: İnanılacak esaslara toptan",
            "  inanmak (Kelime-i Tevhid ve Kelime-i Şehadet)",
            "• Tafsîlî (Ayrıntılı) İman: Altı iman esasının",
            "  her birine (Allah, melekler, kitaplar, peygamberler,",
            "  ahiret, kader) ayrı ayrı ve delilleriyle inanmak"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "İmanın Artıp Eksilmesi (Kemiyet / Keyfiyet)", [
            "• Kemiyet (Sayı/Esas) Bakımından: İnanılacak 6 esas",
            "  sabit olduğundan iman artmaz ve eksilmez.",
            "• Keyfiyet (Nitelik/Parlaklık) Bakımından: Salih amel,",
            "  ilim ve tefekkürle imanın nuru, gücü ve yakîn",
            "  derecesi artar (Enfâl, 2)."
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
}


def uygula(v):
    hedefler = [0, 1]
    anahtarlar = ["b1", "b2"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
