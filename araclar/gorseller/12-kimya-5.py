def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563EB", bg="#EFF6FF"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ELEKTROLİZ VE FARADAY YASALARI (NİCEL HESAPLAMALAR)</text>'
    )
    ic += _kart(20, 44, 310, 190, "GALVANİK HÜCRE vs. ELEKTROLİZ HÜCRESİ", [
        "• Galvanik (Pil): İstemsiz değil İSTEMLİ (Delta_G &lt; 0,",
        "  E_pil &gt; 0); kimyasal enerjiyi elektrik enerjisine çevirir.",
        "• Elektroliz: İSTEMSİZ (E_pil &lt; 0) redoks tepkimelerini",
        "  dışarıdan elektrik enerjisi vererek gerçekleştirir.",
        "• Her iki hücrede de:",
        "   - ANOT (+ uç): Yükseltgenme (Anyonlar anota gider).",
        "   - KATOT (- uç): İndirgenme (Katyonlar katota gider)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "FARADAY\'IN ELEKTROLİZ YASALARI", [
        "• 1 mol elektronun yükü = 1 Faraday (1 F) = 96.500 C.",
        "• Devreden geçen yük: Q = I . t  (C = Amper x saniye).",
        "• Devreden geçen elektron mol sayısı: n_(e-) = (I . t) / 96500.",
        "• Toplanan madde kütlesi formülü:",
        "  m = (I . t . M_A) / (96500 . z)  (z: tesir değerliği / yük).",
        "• Seri bağlı kaplarda geçen elektron mol sayısı EŞİTTİR:",
        "  n_1 . z_1 = n_2 . z_2"
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SULU ÇÖZELTİLERİN ELEKTROLİZİ VE ÖNCELİK KURALI</text>'
    )
    ic += _kart(20, 44, 310, 190, "KATOTTA İNDİRGENME ÖNCELİĞİ (- UÇ)", [
        "• Katyonlar (Na+, Mg2+, H+, Cu2+, Ag+) katota yönelir.",
        "• KURAL: İndirgenme potansiyeli (pasifliği) EN BÜYÜK",
        "  olan katyon katotta İLK ÖNCE indirgenir!",
        "• Aktif metallerin (Na+, K+, Ca2+, Mg2+, Al3+) sulu",
        "  çözeltisinde metal yerine SU (H+) indirgenir ve",
        "  katotta H2(g) açığa çıkar (Cu2+, Ag+ ise kendisi birikir)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "ANOTTA YÜKSELTGENME ÖNCELİĞİ (+ UÇ)", [
        "• Anyonlar (Cl-, Br-, OH-, SO4^2-, NO3^-) anota yönelir.",
        "• KURAL: Yükseltgenme potansiyeli EN BÜYÜK olan",
        "  anyon anotta İLK ÖNCE yükseltgenir!",
        "• Kök anyonların (SO4^2-, NO3^-, PO4^3-) ve F- iyonunun",
        "  sulu çözeltisinde bu iyonlar yerine SU (OH-) yükseltgenir",
        "  ve anotta O2(g) açığa çıkar (Cl-, Br-, I- ise Cl2, Br2 verir)."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SUYUN ELEKTROLİZİ (HOFFMANN VOLTAMETRESİ) VE ELEKTROKAPLAMA</text>'
    )
    ic += _kart(20, 44, 310, 190, "SUYUN ELEKTROLİZİ (2H2O -> 2H2 + O2)", [
        "• Saf su elektriği iletmediği için birkaç damla H2SO4 eklenir.",
        "• Anot (+): 2H2O(s) -&gt; O2(g) + 4H+ + 4e-  (V hacim O2).",
        "• Katot (-): 4H+ + 4e- -&gt; 2H2(g)         (2V hacim H2).",
        "• DİKKAT: Katotta toplanan H2 gazının hacmi ve mol",
        "  sayısı, anotta toplanan O2 gazının TAM İKİ KATIDIR",
        "  (V_H2 = 2 . V_O2)."
    ], "#0284C7", "#F0F9FF")
    ic += _kart(350, 44, 310, 190, "METAL KAPLAMACILIK (ELEKTROKAPLAMA)", [
        "• Bir metali aşınmadan korumak veya estetik görünüm",
        "  vermek için başka bir metalle kaplama işlemidir.",
        "• ANOT (+): Kaplama yapacak saf metal (Örn: Gümüş - Ag).",
        "• KATOT (-): Üzeri kaplanacak eşya (Örn: Demir çatal).",
        "• ELEKTROLİT: Kaplama metalinin tuz çözeltisi (AgNO3).",
        "• Anottaki Ag çözünür, katottaki çatalın üzerine Ag birikir."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KOROZYON (PASLANMA) VE KATODİK KORUMA (KURBAN ELEKTROT)</text>'
    )
    adimlar = [
        ("KOROZYON NEDİR?", "Metallerin ortamda bulunan oksijen, nem ve asidik maddelerle istenmeyen elektrokimyasal tepkimeye girerek aşınmasıdır.", "#DC2626", "#FEF2F2"),
        ("KLASİK KORUNMA YOLLARI", "Metali boyamak, verniklemek, galvanize etmek (çinko ile kaplamak) veya paslanmaz çelik gibi alaşımlar kullanmak.", "#2563EB", "#EFF6FF"),
        ("KATODİK KORUMA VE KURBAN ELEKTROT", "Korunacak metal yapıya (gemi gövdesi, boru hattı, LPG tankı), ondan DAHA AKTİF (yükseltgenme potansiyeli daha büyük) bir metal bağlanır.", "#059669", "#ECFDF5"),
        ("ANOT VE KATOT GÖREVİ", "Daha aktif olan metal (Mg, Al, Zn) ANOT (Kurban Elektrot) olarak kendisi aşınır; korunacak demir yapı ise KATOT yapılarak paslanmaz!", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
