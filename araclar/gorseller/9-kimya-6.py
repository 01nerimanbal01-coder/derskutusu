def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'


def _kart(x, y, w, h, baslik, satirlar, bg, border, text_c):
    rx = 12
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}" stroke="{border}" stroke-width="2"/>'
    s += f'<text x="{x + w/2}" y="{y + 26}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{text_c}" text-anchor="middle">{baslik}</text>'
    s += f'<line x1="{x+12}" y1="{y+36}" x2="{x+w-12}" y2="{y+36}" stroke="{border}" stroke-width="1" stroke-dasharray="3,3"/>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x + w/2}" y="{y + 58 + i*22}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="middle">{st}</text>'
    return s


def gorsel_1():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ENERJİ DÜZEYLERİ, ALT KABUKLAR VE ORBİTAL KAPASİTELERİ</text>'
    ic += _kart(30, 56, 195, 160, "s ve p Orbitalleri", ["s: 1 orbital, en çok 2 e⁻", "(1. katmandan itibaren var)", "p: 3 orbital, en çok 6 e⁻", "(2. katmandan itibaren var)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "d ve f Orbitalleri", ["d: 5 orbital, en çok 10 e⁻", "(3. katmandan itibaren var)", "f: 7 orbital, en çok 14 e⁻", "(4. katmandan itibaren var)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Katman Kapasitesi (2n²)", ["n=1 (K): s -> 2 e⁻", "n=2 (L): s, p -> 8 e⁻", "n=3 (M): s, p, d -> 18 e⁻", "n=4 (N): s, p, d, f -> 32 e⁻"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ATOM ORBİTALLERİNİN BAĞIL ENERJİ SIRASI (AUFBAU)</text>'
    ic += _kart(30, 56, 300, 160, "Bağıl Enerji Artış Sırası", ["• Çekirdekten uzaklaştıkça enerji artar", "• 1s &lt; 2s &lt; 2p &lt; 3s &lt; 3p &lt; 4s &lt; 3d &lt; 4p", "• Dikkat: 4s orbitalinin enerjisi 3d’den DÜŞÜKTÜR!", "• Önce 4s dolar, sonra 3d orbitali dolar"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(350, 56, 300, 160, "Eş Enerjili Orbitaller", ["• Aynı alt kabuktaki orbitaller eş enerjilidir", "• 2px = 2py = 2pz (3 adet eş enerjili p orbitali)", "• 3d alt kabuğunda 5 adet eş enerjili orbital var", "• Aynı n değerinde enerji: s &lt; p &lt; d &lt; f"], "#e0f2fe", "#0284c7", "#0369a1")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ELEKTRON DİZİLİMİNİN ÜÇ TEMEL KURALI</text>'
    ic += _kart(30, 56, 195, 160, "1. Aufbau Kuralı", ["(İnşa Etme İlkesi)", "Elektronlar en düşük enerjili", "orbitalden (1s) başlayarak", "sırayla yerleşir"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "2. Pauli İlkesi", ["Bir orbitale en fazla 2 elektron", "yerleşebilir", "Bu iki elektronun dönme yönü", "(spinleri) ZIT olmalıdır (↑↓)"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "3. Hund Kuralı", ["Eş enerjili orbitallere (p, d, f)", "elektronlar önce TEKER TEKER", "ve AYNI yönlü (↑ ↑ ↑) yerleşir,", "sonra eşleşmeye başlar"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ÖRNEK ELEKTRON DİZİLİMLERİ VE ORBİTAL ŞEMASI</text>'
    ic += _kart(30, 56, 195, 160, "Karbon (₆C) ve Azot (₇N)", ["₆C: 1s² 2s² 2p² (2 yarı dolu)", "₇N: 1s² 2s² 2p³ (3 yarı dolu)", "₈O: 1s² 2s² 2p⁴ (2 yarı dolu)", "₁₀Ne: 1s² 2s² 2p⁶ (Tam dolu)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Potasyum (₁₉K) ve Ca (₂₀Ca)", ["₁₉K: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", "₂₀Ca: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", "₂₁Sc: ... 3p⁶ 4s² 3d¹", "30’a kadar dizilim kuralı"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Özel Küresel Simetri!", ["₂₄Cr: ... 4s¹ 3d⁵ (4s² 3d⁴ değil!)", "₂₉Cu: ... 4s¹ 3d¹⁰ (4s² 3d⁹ değil!)", "Kararlılık için kendiliğinden", "gerçekleşen temel hal dizilimi"], "#f1f5f9", "#64748b", "#334155")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    bolumler = v.get("bolumler", [])
    eslesme = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    for idx, key in eslesme:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[key]
