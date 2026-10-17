def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Yardımlaşma ve Dayanışmanın Toplumsal Birliğe Katkıları</text>'
    ic += _kart(20, 45, 230, 175, "Kültürel Mirasımızda Dayanışma", [
        "• İmece: Köy ve mahalle işlerini",
        "  el birliğiyle nöbetleşe yapma",
        "• Sadaka Taşı ve Zimem Defteri",
        "• Vakıf ve Aşevi (İmaret) geleneği",
        "• Komşuluk ve bayramlaşma kültürü"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "Kurumsal Dayanışma (STK ve Kamu)", [
        "• Türk Kızılayı (Afet, kan, yardım)",
        "• AFAD (Acil durum ve arama-kurtarma)",
        "• Darülaceze, Yeşilay, LÖSEV, TEMA",
        "• Sosyal Yardımlaşma Vakıfları",
        "• Okul içi yardım kampanyaları"
    ], "#2563eb", "#eff6ff")
    ic += _kart(510, 45, 230, 175, "Toplumsal Birliğe Etkisi", [
        "• Sevgi, saygı ve güveni artırır",
        "• Yalnızlık ve çaresizliği giderir",
        "• Zorlukların hızla aşılmasını sağlar",
        "• Empati ve sorumluluk bilinci katar",
        "• Milli birlik ve kardeşliği güçlendirir"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Ana Yönler, Ara Yönler ve Pusula İle Konum Belirleme</text>'
    ic += '<circle cx="190" cy="140" r="80" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>'
    ic += '<line x1="190" y1="50" x2="190" y2="230" stroke="#1d4ed8" stroke-width="2.5"/>'
    ic += '<line x1="100" y1="140" x2="280" y2="140" stroke="#1d4ed8" stroke-width="2.5"/>'
    ic += '<line x1="130" y1="80" x2="250" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,2"/>'
    ic += '<line x1="250" y1="80" x2="130" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,2"/>'
    ic += '<text x="190" y="45" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">KUZEY (K)</text>'
    ic += '<text x="190" y="245" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">GÜNEY (G)</text>'
    ic += '<text x="312" y="144" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">DOĞU (D)</text>'
    ic += '<text x="68" y="144" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">BATI (B)</text>'
    ic += '<text x="265" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">KD</text>'
    ic += '<text x="105" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">KB</text>'
    ic += '<text x="265" y="212" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">GD</text>'
    ic += '<text x="105" y="212" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">GB</text>'
    ic += _kart(380, 50, 360, 180, "Haritada Yön ve Komşuluk Okuma", [
        "• 4 Ana Yön: Kuzey (K), Güney (G), Doğu (D), Batı (B)",
        "• 4 Ara Yön: Kuzeydoğu (KD), Kuzeybatı (KB),",
        "  Güneydoğu (GD), Güneybatı (GB)",
        "• Haritalarda yön oku üst tarafı (Kuzey\'i) gösterir",
        "• İlimizin komşu illerini ana ve ara yönlerle tarif ederiz",
        "• Örn: \'Ankara\'nın kuzeyinde Çankırı, güneyinde Konya vardır\'"
    ], "#0284c7", "#f0f9ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Yaşadığımız İlin Göreceli (Özel) Konum Özellikleri</text>'
    ic += _kart(20, 45, 230, 185, "1. Komşular ve Denizlere Konum", [
        "• Hangi coğrafi bölgede yer aldığı",
        "• Doğusunda, batısında, kuzeyinde",
        "  ve güneyinde hangi iller olduğu",
        "• Denize kıyısı olup olmadığı",
        "• Ülke sınırına (komşu ülkelere) yakınlık"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(265, 45, 230, 185, "2. Yer Şekilleri ve İklim", [
        "• Dağlar, ovalar, platolar, vadiler",
        "• Akarsular, göller ve barajlar",
        "• Yükselti ve yer şekillerinin etkisi",
        "• Görülün iklim ve bitki örtüsü",
        "• Doğal afet riskleri (deprem, heyelan)"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 185, "3. Beşeri ve Ekonomik Özellikler", [
        "• Ulaşım yolları (kara, demir, deniz, hava)",
        "• Tarım, sanayi, ticaret ve madencilik",
        "• Tarihi mekânlar ve doğal güzellikler",
        "• Nüfus yoğunluğu ve göç durumu",
        "• Eğitim ve kültür kurumları"
    ], "#d97706", "#fffbeb")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Göreceli Konumun İlimizin Yaşamına Etkileri (Örnek Çözümleme)</text>'
    ic += _kart(20, 45, 350, 175, "Kıyı İli Örneği (İzmir / Antalya / Trabzon)", [
        "• Denize kıyısı vardır, yükseltisi kıyı kesimde azdır",
        "• İklimi ılıman, kışları ılık geçer",
        "• Deniz ticareti (liman), balıkçılık ve kıyı turizmi gelişmiştir",
        "• Verimli kıyı ovalarında çeşitli tarım ürünleri yetişir",
        "• Ulaşım ve ticaret olanakları nüfusu kendine çeker"
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "İç ve Doğu İli Örneği (Konya / Kayseri / Erzurum)", [
        "• Denize kıyısı yoktur (karasal konum)",
        "• Yükseltisi fazladır (batıdan doğuya gidildikçe yükselti artar)",
        "• Geniş ovalarda tahıl tarımı, yüksek platolarda hayvancılık yapılır",
        "• Önemli kara ve demir yolu kavşaklarında ticaret gelişir",
        "• Kış turizmi (Palandöken, Erciyes) ve tarihi miras öne çıkar"
    ], "#15803d", "#f0fdf4")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]
