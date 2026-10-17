def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#0284c7", bg="#f0f9ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#0f172a"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#f8fafc" text-anchor="middle">Güneş, Dünya ve Ay\'ın Hacimsel Büyüklük Karşılaştırması</text>'
    ic += '<circle cx="140" cy="140" r="78" fill="#f59e0b" stroke="#fde047" stroke-width="3"/>'
    ic += '<text x="140" y="135" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">GÜNEŞ</text>'
    ic += '<text x="140" y="155" font-family="sans-serif" font-size="11.5" fill="#fef3c7" text-anchor="middle">Pilav Tenceresi / Karpuz</text>'
    ic += '<text x="140" y="236" font-family="sans-serif" font-size="11.5" fill="#fde047" text-anchor="middle">Çapı Dünya\'nın ~109 katı</text>'

    ic += '<circle cx="390" cy="140" r="28" fill="#2563eb" stroke="#60a5fa" stroke-width="2.5"/>'
    ic += '<text x="390" y="144" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DÜNYA</text>'
    ic += '<text x="390" y="195" font-family="sans-serif" font-size="11.5" fill="#93c5fd" text-anchor="middle">Nohut Tanesi / Erik</text>'
    ic += '<text x="390" y="236" font-family="sans-serif" font-size="11.5" fill="#93c5fd" text-anchor="middle">Çapı Ay\'ın ~4 katı</text>'

    ic += '<circle cx="610" cy="140" r="10" fill="#cbd5e1" stroke="#f8fafc" stroke-width="2"/>'
    ic += '<text x="610" y="175" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">AY</text>'
    ic += '<text x="610" y="195" font-family="sans-serif" font-size="11.5" fill="#e2e8f0" text-anchor="middle">Mercimek / Bezelye</text>'
    ic += '<text x="610" y="236" font-family="sans-serif" font-size="11.5" fill="#e2e8f0" text-anchor="middle">En küçük gök cismi</text>'
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Güneş, Dünya ve Ay\'ın Dönme ve Dolanma Hareketleri (Saat Yönünün Tersine!)</text>'
    ic += _kart(20, 45, 230, 185, "1. Güneş\'in Hareketi", [
        "• Kendi ekseni etrafında döner",
        "• Yön: Batıdan Doğuya",
        "  (Saat yönünün tersine)",
        "• 1 tam turu ~25 günde tamamlar",
        "• Samanyolu galaksisinde dolanır"
    ], "#d97706", "#fffbeb")
    ic += _kart(265, 45, 230, 185, "2. Dünya\'nın 2 Hareketi", [
        "• Kendi ekseninde dönme: 24 saat",
        "  (1 gün -> Gece ve gündüz oluşur)",
        "• Güneş etrafında dolanma:",
        "  365 gün 6 saat (1 yıl)",
        "• Her iki hareket de saat yönü tersi"
    ], "#2563eb", "#eff6ff")
    ic += _kart(510, 45, 230, 185, "3. Ay\'ın 3 Hareketi", [
        "• Kendi ekseninde dönme: ~27,3 gün",
        "• Dünya etrafında dolanma: ~27,3 gün",
        "  (Bu eşitlikten hep aynı yüzü görünür)",
        "• Dünya ile birlikte Güneş etrafında",
        "  dolanma: 365 gün 6 saat (1 yıl)"
    ], "#475569", "#f1f5f9")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#0f172a"/>'
    ic += '<text x="380" y="26" font-family="sans-serif" font-size="14.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">Güneş - Dünya - Ay Yörünge ve Hareket Modeli (Batıdan Doğuya / Saat Yönünün Tersi)</text>'
    ic += '<ellipse cx="380" cy="135" rx="280" ry="80" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>'
    ic += '<circle cx="240" cy="135" r="42" fill="#f59e0b" stroke="#fde047" stroke-width="2.5"/>'
    ic += '<text x="240" y="139" font-family="sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">GÜNEŞ</text>'
    ic += '<circle cx="580" cy="135" r="45" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>'
    ic += '<circle cx="580" cy="135" r="16" fill="#2563eb" stroke="#93c5fd" stroke-width="2"/>'
    ic += '<text x="580" y="139" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Dünya</text>'
    ic += '<circle cx="625" cy="135" r="7" fill="#e2e8f0"/>'
    ic += '<text x="645" y="139" font-family="sans-serif" font-size="11" fill="#e2e8f0">Ay</text>'
    ic += '<text x="380" y="230" font-family="sans-serif" font-size="11.5" fill="#bae6fd" text-anchor="middle">Dünya Güneş etrafında 365 gün 6 saatte dolanırken, Ay da Dünya etrafında (~27,3 gün) dolanır.</text>'
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Bilimsel Model Tasarlarken Dikkat Edilecek Ölçütler</text>'
    ic += _kart(20, 45, 350, 175, "1. Büyüklük Oranının Doğru Seçimi", [
        "• Hacimsel sıralama: Güneş > Dünya > Ay",
        "• Örnek 1: Basketbol topu (Güneş) - Nohut (Dünya) - Mercimek (Ay)",
        "• Örnek 2: Karpuz (Güneş) - Erik/Üzüm (Dünya) - Bezelye (Ay)",
        "• Örnek 3: Pilav tenceresi (Güneş) - Ceviz (Dünya) - Nohut (Ay)",
        "• Üçünü eşit boyda çizmek bilimsel model hatasıdır!"
    ], "#059669", "#ecfdf5")
    ic += _kart(390, 45, 350, 175, "2. Konum ve Hareket Yönünün Doğruluğu", [
        "• Ay, Dünya\'ya Güneş\'ten çok daha yakındır (~384.000 km)",
        "• Güneş Dünya\'dan ~150 milyon km uzaktadır (perspektif etkisi)",
        "• Güneş\'in dönmesi, Dünya\'nın dönme ve dolanması, Ay\'ın dönme",
        "  ve dolanması hepsi SAAT YÖNÜNÜN TERSİNE (Batıdan Doğuya)",
        "• Hareketli modellerde maşa/tel mekanizmasıyla dolanma gösterilir"
    ], "#7c3aed", "#f5f3ff")
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
