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
        '“Bir Diyeceğim Var!” Temasında Çok Modlu Dinleme/İzleme Süreci</text>'
        + _kart(18, 42, 205, 145, "1. Dinleme/İzleme Öncesi", [
            "• Dinleme/izleme amacını belirleme",
            "• Başlık ve görsellerden hareketle",
            "  içeriğe yönelik tahminlerde bulunma",
            "• Ön bilgileri harekete geçirme ve",
            "  uygun strateji (not alma vb.) seçme"
        ], "#2563eb", "#eff6ff")
        + _kart(237, 42, 205, 145, "2. Dinleme/İzleme Sırası", [
            "• Sözlü, görsel ve işitsel katmanları",
            "  eş zamanlı takip etme",
            "• Vurgu, tonlama ve beden dilini",
            "  yorumlama; anahtar kavramları",
            "  ve geçiş ifadelerini not alma"
        ], "#059669", "#ecfdf5")
        + _kart(456, 42, 205, 145, "3. Dinleme/İzleme Sonrası", [
            "• Tahminlerle ulaşılan iletiyi",
            "  karşılaştırma ve özetleme",
            "• Örtük iletileri, argümanları ve",
            "  hedef kitleye etkisini çözümleme",
            "• Eleştirel değerlendirme yapma"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 202, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Çok Modlu Metinlerde Anlam Oluşturma ve Eleştirel Çözümleme</text>'
        + _kart(25, 42, 300, 145, "Çok Modlu Metnin Katmanları", [
            "• Dilsel Katman: Sözcük seçimi, söz sanatları, üslup",
            "• İşitsel Katman: Ses tonu, vurgu, duraklama, müzik",
            "• Görsel Katman: Kamera açısı, ışık, renk, semboller",
            "• Jest/Mimik ve Mekânsal Katman: Beden dili ve kurgu",
            "• Katmanlar arası uyum tezin ikna gücünü artırır."
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Argüman ve Güvenilirlik Denetimi", [
            "• Konuşmacının temel iddiası (tezi) nedir?",
            "• İddiayı destekleyen kanıt ve örnekler tutarlı mı?",
            "• Öznel yargılar ile nesnel veriler ayrıştırılmış mı?",
            "• Yönlendirme (manipülasyon) veya mantık hatası var mı?",
            "• Metnin toplumsal ve insani duyarlılıkla ilişkisi nedir?"
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
