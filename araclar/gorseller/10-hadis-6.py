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
        'Sünnetin Evrenselliğinin 3 Temel Dayanağı</text>'
        + _kart(20, 42, 200, 142, "1. Son Peygamber Oluşu", [
            "• Hz. Muhammed (sav) Hâtemü’n-",
            "  Nebiyyîn’dir (Ahzâb 40)",
            "• Kıyamete kadar tüm insanlığa",
            "  gönderilmiştir (Sebe 28)",
            "• Mesajı zamanlar üstüdür"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. İnsanın Fıtratına Uygunluk", [
            "• Sünnet, insanın değişmeyen",
            "  fıtratına, aklına ve",
            "  vicdanına hitap eder",
            "• Güç yetirilebilir, dengeli",
            "  ve uygulanabilir ilkeler sunar"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 142, "3. Evrensel Ahlak ve Hukuk", [
            "• Veda Hutbesi ilkeleri:",
            "  Can, mal, akıl, nesil ve",
            "  din emniyeti",
            "• Irkçılığın reddi, adalet,",
            "  merhamet ve çevre ahlakı"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Sünnetin Evrensel (Bağlayıcı) ve Yerel/Kültürel (Beşerî) Boyutları</text>'
        + _kart(25, 42, 300, 145, "Evrensel ve Dini Sünnet (Teşrîî Sünnet)", [
            "• Peygamberlik (risalet) sıfatıyla bildirdiği",
            "  inanç, ibadet, helal-haram ve ahlak ilkeleri",
            "• Kıyamete kadar tüm Müslümanları bağlar",
            "• Örnek: Namazın kılınışı, zekât oranları, kul hakkı,",
            "  adalet, dürüstlük, aile ve komşuluk hakları"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Beşerî ve Kültürel Sünnet (Zevâid / Cibillî)", [
            "• Bir insan olarak yaşadığı coğrafyanın iklim ve",
            "  örfüne göre yaptığı günlük tercihler",
            "• Dini bir zorunluluk (farz/vacip) değildir",
            "• Örnek: Hicaz iklimine uygun kıyafet şekli, sevdiği",
            "  yemekler, binit tercihi veya dönemin savaş araçları"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Cevâmiu’l-Kelim: Az Sözle Çok ve Evrensel Anlam İfade Eden Hadisler</text>'
        + _kart(25, 42, 300, 142, "Niyet ve Sorumluluk İlkeleri", [
            "• ”Ameller niyetlere göredir.” (İhlas ve hukuk ilkesi)",
            "• ”Zarar vermek ve zarara zararla karşılık vermek",
            "  yoktur.” (Lâ darara velâ dırâr - Evrensel hukuk)",
            "• ”Hepiniz çobansınız ve yönetimini üstlendiğiniz",
            "  kimselerden sorumlusunuz.”"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 142, "İnsanlık, Merhamet ve Kardeşlik İlkeleri", [
            "• ”Merhamet etmeyene merhamet olunmaz.”",
            "• ”Hiçbiriniz kendisi için istediğini kardeşi için de",
            "  istemedikçe gerçek mümin olamaz.”",
            "• ”Kolaylaştırınız, zorlaştırmayınız; müjdeleyiniz,",
            "  nefret ettirmeyiniz!”"
        ], "#ea580c", "#fff7ed")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Farklı Kültürlerde Sünnetin Yaşatılması ve Çağdaş Sorunlara Çözümleri</text>'
        + _kart(25, 42, 300, 138, "Kültürler Üstü Uyum Yeteneği", [
            "• Sünnet, yerel kültürlerin İslam’a aykırı olmayan",
            "  güzel örf ve adetlerini (ma’rûf) korumuştur",
            "• Afrika’dan Anadolu’ya, Balkanlar’dan Uzak Doğu’ya",
            "  kadar her toplum sünnetin ilkelerini benimsemiştir"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Modern Çağın Krizlerine Nebevî Reçeteler", [
            "• Tüketim çılgınlığı ve iklim krizine -> İsraf yasağı",
            "• Irkçılık ve ayrımcılığa -> Veda Hutbesi eşitliği",
            "• Bireyselleşme ve yalnızlığa -> Sıla-i rahim ve infak",
            "• Şiddet ve nefrete -> Rıfk (yumuşak huyluluk) ve sulh"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


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
