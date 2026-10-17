def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Yörünge (Katman) Kavramından Atom Orbitali Kavramına Geçiş</text>'
    c += _kart(18, 54, 314, 170, "Bohr Yörüngesi (Klasik Yaklaşım)", [
        "• Elektronun çekirdek etrafında izlediği varsayılan",
        "  dairesel ve kesin çizgisel yoldur.",
        "• Elektronun yeri ve hızı aynı anda kesin bilinir.",
        "• İki boyutlu düzlemsel hareket öngörür.",
        "• Yalnızca tek elektronlu (H, He+) sistemleri açıklar."
    ], "#922b21", "#fdedec")
    c += _kart(348, 54, 314, 170, "Atom Orbitali (Modern Atom Teorisi)", [
        "• Elektronun çekirdek etrafında bulunma olasılığının",
        "  en yüksek olduğu üç boyutlu hacimsel bölgedir.",
        "• Heisenberg Belirsizlik İlkesine dayanır.",
        "• Farklı enerji düzeylerinde farklı şekillere sahiptir.",
        "• s, p, d ve f olmak üzere 4 temel türü vardır."
    ], "#1a5276", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Atom Orbitallerinin Türleri, Alt Orbital Sayıları ve Maksimum Elektron Kapasiteleri</text>'
    c += _kart(18, 54, 152, 180, "s Orbitali (l = 0)", [
        "• Küresel simetriktir.",
        "• 1. enerji düzeyinden",
        "  (n = 1) itibaren",
        "  her katmanda bulunur.",
        "• Alt orbital sayısı: 1",
        "• Maksimum e- : 2"
    ], "#1e8449", "#e9f7ef")
    c += _kart(182, 54, 152, 180, "p Orbitali (l = 1)", [
        "• Çift loblu (papyon)",
        "  uzaysal yapıdadır.",
        "• 2. enerji düzeyinden",
        "  (n ≥ 2) itibaren var.",
        "• Alt orbital: 3 (px,py,pz)",
        "• Maksimum e- : 6"
    ], "#2874a6", "#eaf2f8")
    c += _kart(346, 54, 152, 180, "d Orbitali (l = 2)", [
        "• Dört loblu karmaşık",
        "  sınır yüzeyine sahiptir.",
        "• 3. enerji düzeyinden",
        "  (n ≥ 3) itibaren var.",
        "• Alt orbital sayısı: 5",
        "• Maksimum e- : 10"
    ], "#b9770e", "#fef9e7")
    c += _kart(510, 54, 152, 180, "f Orbitali (l = 3)", [
        "• Çok loblu karmaşık",
        "  uzaysal geometri.",
        "• 4. enerji düzeyinden",
        "  (n ≥ 4) itibaren var.",
        "• Alt orbital sayısı: 7",
        "• Maksimum e- : 14"
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Atom Orbitallerinin Bağıl Enerjileri: Madelung-Kletchkowski (n + l) Kuralı</text>'
    c += _kart(18, 54, 314, 180, "Kural 1: (n + l) Değeri Büyüdükçe Enerji Artar", [
        "• Baş kuantum sayısı (n) ve orbital türü değeri",
        "  (s=0, p=1, d=2, f=3) toplanır.",
        "• (n + l) toplamı büyük olan orbitalin enerjisi",
        "  daha yüksektir!",
        "• Örnek: 3d (3+2=5) &gt; 4s (4+0=4) olduğundan",
        "  3d orbitalinin enerjisi 4s\'den büyüktür!"
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 180, "Kural 2: (n + l) Eşitse n\'si Büyük Olan Büyüktür", [
        "• İki farklı orbitalin (n + l) toplamı birbirine",
        "  eşitse, baş kuantum sayısı (n) büyük olanın",
        "  çekirdeğe uzaklığı ve enerjisi daha fazladır.",
        "• Örnek: 3d (3+2=5) ve 4p (4+1=5) için",
        "  n+l eşittir; n(4p)=4 &gt; n(3d)=3 olduğundan",
        "  Enerji sıralaması: 4s &lt; 3d &lt; 4p olur!"
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Tek Elektronlu ve Çok Elektronlu Atomlarda Bağıl Enerji Sıralaması</text>'
    c += _kart(18, 54, 314, 165, "Çok Elektronlu Atomlarda Bağıl Enerji Sırası", [
        "• Elektronlar arası itme nedeniyle aynı katmandaki",
        "  alt kabukların enerjisi ayrışır (s &lt; p &lt; d &lt; f).",
        "• Genel Sıra: 1s &lt; 2s &lt; 2p &lt; 3s &lt; 3p &lt; 4s &lt; 3d &lt;",
        "  4p &lt; 5s &lt; 4d &lt; 5p &lt; 6s &lt; 4f &lt; 5d &lt; 6p &lt; 7s",
        "• Eş enerjili (dejener) orbitaller: 2px = 2py = 2pz"
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 165, "Bilimsel Veriye Dayalı Tahmin ve Karşılaştırma", [
        "• İyonlaşma enerjisi ve spektrum verileri, K (Z=19)",
        "  ve Ca (Z=20) atomlarında son elektronun 3d yerine",
        "  4s orbitaline yerleştiğini kanıtlar.",
        "• Çünkü temel hâlde 4s orbitalinin bağıl enerjisi",
        "  3d orbitalinden daha düşüktür."
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
