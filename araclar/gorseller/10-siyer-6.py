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
        'Hz. Muhammed’in (sav) Soy Ağacı ve Aile Büyükleri</text>'
        + _kart(25, 42, 300, 145, "Baba Tarafı (Kureyş / Hâşimoğulları)", [
            "• Hz. İbrahim (as) -> Hz. İsmail (as) -> Adnan",
            "• Kusay b. Kilâb -> Abdümenâf -> Hâşim",
            "• Dedesi: Abdülmuttalib (Şeybe - Zemzem’i yeniden",
            "  bulan ve Fil Vakası’nda Mekke’yi temsil eden lider)",
            "• Babası: Abdullah (Doğumdan önce Yesrib’de vefat etti)"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Anne Tarafı ve Kutlu Doğum (571)", [
            "• Annesi: Âmine bint Vehb (Zühreoğulları kabilesi)",
            "• Doğumu: 20 Nisan 571 (12 Rebîülevvel Pazartesi,",
            "  Fil Vakası’ndan yaklaşık 50-55 gün sonra, Mekke)",
            "• Dedesi Abdülmuttalib ”Muhammed” (Övülmüş) adını,",
            "  annesi Âmine ise ”Ahmed” adını verdi"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Hz. Muhammed’in (sav) Çocukluk Dönemi Kronolojisi (0 - 12 Yaş)</text>'
        + _kart(16, 42, 152, 142, "1. Sütanne (0-4 Yaş)", [
            "• İlk emzirenler: Annesi",
            "  Âmine ve Süveybe",
            "• Benî Sa’d yurdunda",
            "  Halîme bint Ebû Züeyb",
            "• Bereket ve fasih Arapça"
        ], "#0284c7", "#f0f9ff")
        + _kart(178, 42, 152, 142, "2. Annesi (4-6 Yaş)", [
            "• 4 yaşında Mekke’ye,",
            "  annesi Âmine’nin",
            "  yanına dönüşü",
            "• 6 yaşında Medine ziyareti",
            "  ve Ebvâ’da Âmine’nin vefatı"
        ], "#d97706", "#fffbeb")
        + _kart(340, 42, 152, 142, "3. Dedesi (6-8 Yaş)", [
            "• Dadısı Ümmü Eymen",
            "  ile Mekke’ye dönüşü",
            "• Dedesi Abdülmuttalib’in",
            "  özel şefkati ve",
            "  8 yaşında vefatı"
        ], "#7c3aed", "#f5f3ff")
        + _kart(502, 42, 160, 142, "4. Amcası (8+ Yaş)", [
            "• Öz amcası Ebû Tâlib",
            "  ve yengesi Fâtıma",
            "  bint Esed’in himayesi",
            "• Çobanlık ve 9/12 yaşında",
            "  Şam (Busra) yolculuğu"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 198, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Sütanneye Verilme Geleneğinin Nedenleri ve Süt Kardeşleri</text>'
        + _kart(25, 42, 300, 142, "Çöl Havası (Bâdiye) Geleneğinin Hikmetleri", [
            "• 1. Mekke’nin sıcak ve salgın hastalıklı havasından",
            "     bebekleri koruyup sağlam bünyeli yetiştirmek",
            "• 2. Yabancıların etkisiyle bozulmamış saf ve",
            "     fasih (düzgün) Arapçayı yerinde öğrenmeleri",
            "• 3. Çöl hayatının özgüven, sabır ve cesaret kazandırması"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 142, "Sütanneleri ve Süt Kardeşleri", [
            "• Süveybe (Ebû Leheb’in cariyesi): Süt kardeşi",
            "  Hz. Hamza (amcası) ve Ebû Seleme",
            "• Halîme (Hevâzin / Benî Sa’d kabilesinden):",
            "  Süt babası Hâris; süt kardeşleri Abdullah,",
            "  Üneyse ve Şeymâ (Huzâfe)"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Yetim ve Öksüz Büyümesinin Risalet Kişiliğine Etkisi (Duhâ Suresi 6-10)</text>'
        + _kart(25, 42, 300, 138, "Duhâ Suresi 6-8: İlahi Himaye", [
            "• ”O, seni yetim bulup da barındırmadı mı?”",
            "• Babasız (yetim) ve 6 yaşında annesiz (öksüz) kalması,",
            "  O’nu doğrudan Yüce Allah’ın (cc) terbiye ve",
            "  korumasına yöneltmiştir"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Empati, Vefa ve Merhamet Ahlakı", [
            "• Yetimlerin, yoksulların ve kimsesizlerin acısını",
            "  bizzat yaşayarak en derin merhameti kuşanmıştır",
            "• Dadısı Ümmü Eymen’e ”Annemden sonra annem”,",
            "  Fâtıma bint Esed’e ve Halîme’ye ömür boyu vefa"
        ], "#059669", "#ecfdf5")
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
