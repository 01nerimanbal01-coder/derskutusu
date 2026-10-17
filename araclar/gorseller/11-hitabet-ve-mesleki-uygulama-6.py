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
        'Din Hizmetlerinde İletişim ve Hitabetin Temel Unsurları</text>'
        + _kart(18, 42, 205, 148, "1. Hatip (Kaynak)", [
            "• İmam-hatip, müezzin, vaiz,",
            "  Kur’an kursu öğreticisi",
            "• İhlas, samimiyet, sahih bilgi",
            "  ve güzel ahlak (temsil gücü)",
            "• Söz ile davranış uyumu"
        ], "#2563eb", "#eff6ff")
        + _kart(237, 42, 205, 148, "2. Muhatap (Cemaat)", [
            "• Farklı yaş, eğitim ve",
            "  meslek gruplarından cemaat",
            "• “İnsanlara akılları (anlayış)",
            "  ölçüsünde konuşunuz” ilkesi",
            "• Empati ve muhatap analizi"
        ], "#059669", "#ecfdf5")
        + _kart(456, 42, 205, 148, "3. Mesaj ve Üslup", [
            "• Kur’an ve Sünnete dayalı",
            "  hikmetli davet (Nahl, 125)",
            "• Kavlen leyyinen (yumuşak söz)",
            "• Müjdeleyici, birleştirici ve",
            "  kolaylaştırıcı üslup"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Dinî Hitabet Türleri ve İletişim Engellerini Aşma</text>'
        + _kart(25, 42, 300, 145, "Cami İçi ve Cami Dışı Dinî Hitabet", [
            "• Hutbe: Cuma ve bayram namazlarında minberde",
            "  okunan, namazın şartı/sünneti olan hitabet",
            "• Vaaz (İrşat): Kürsüde cemaati aydınlatma sohbeti",
            "• Emir bi’l-ma’rûf nehiy ani’l-münker sorumluluğu",
            "• Sosyal medya, radyo-TV ve manevi danışmanlık"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Hitabette Kaçınılması Gereken Hatalar", [
            "• Kırıcı, dışlayıcı ve ümitsizliğe düşürücü dil",
            "• Kaynağı belirsiz (mevzû/uydurma) rivayetler",
            "• Cemaatin seviyesine uymayan ağdalı/karmaşık dil",
            "• Monoton ses tonu, aşırı uzatma ve hazırlıksızlık",
            "• Söz ile yaşantının birbiriyle çelişmesi (Saff, 2-3)"
        ], "#0284c7", "#f0f9ff")
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
