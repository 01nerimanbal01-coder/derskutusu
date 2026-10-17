# -*- coding: utf-8 -*-
"""10. Sınıf Temel Dini Bilgiler — 5. Hafta Görselleri
Konu: 1. Ünite: Hayatın Anlamı — İslam'da Dünya ve Ahiret Dengesi, Salih Amel ve İstikamet
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0d9488", arka="#f0fdfa"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """İslam'da Dünya ve Ahiret Dengesi (Kasas 77 ve Bakara 201)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İslam'da Dünya ve Ahiret Dengesi: 'Ahiretin Tarlası Dünya'", "#0d9488", "#f0fdfa")

    # Sol Kefe: Dünya Hayatı
    s += '<rect x="30" y="58" width="290" height="175" rx="10" fill="#fff" stroke="#0284c7" stroke-width="1.6"/>'
    s += '<rect x="30" y="58" width="290" height="28" rx="10" fill="#0284c7"/>'
    s += '<text x="175" y="77" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">1. DÜNYA HAYATI (İmtihan ve Ekim Yeri)</text>'
    s += '<text x="175" y="106" text-anchor="middle" fill="#1e293b" font-size="10.2">• Helalinden çalışıp rızık kazanmak</text>'
    s += '<text x="175" y="126" text-anchor="middle" fill="#1e293b" font-size="10.2">• İlim, sanat ve teknoloji üretmek</text>'
    s += '<text x="175" y="146" text-anchor="middle" fill="#1e293b" font-size="10.2">• Aileyi ve toplumu imar etmek</text>'
    s += '<text x="175" y="172" text-anchor="middle" fill="#0369a1" font-size="10.5" font-weight="700">&quot;Dünyadan da nasibini unutma!&quot; (Kasas, 77)</text>'
    s += '<text x="175" y="192" text-anchor="middle" fill="#dc2626" font-size="9.8">Aşırılık: Dünyevileşme (Ahireti unutmak)</text>'

    # Merkez Terazi
    s += '<circle cx="380" cy="145" r="38" fill="#0f766e" stroke="#99f6e4" stroke-width="2.5"/>'
    s += '<text x="380" y="141" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">DENGE</text>'
    s += '<text x="380" y="157" text-anchor="middle" fill="#ccfbf1" font-size="10" font-weight="700">(İtidal)</text>'

    # Sağ Kefe: Ahiret Hayatı
    s += '<rect x="440" y="58" width="290" height="175" rx="10" fill="#fff" stroke="#16a34a" stroke-width="1.6"/>'
    s += '<rect x="440" y="58" width="290" height="28" rx="10" fill="#16a34a"/>'
    s += '<text x="585" y="77" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">2. AHİRET HAYATI (Ebedi Hasat Yurdu)</text>'
    s += '<text x="585" y="106" text-anchor="middle" fill="#1e293b" font-size="10.2">• Allah\'a iman ve ihlasla ibadet</text>'
    s += '<text x="585" y="126" text-anchor="middle" fill="#1e293b" font-size="10.2">• Salih amel ve güzel ahlak</text>'
    s += '<text x="585" y="146" text-anchor="middle" fill="#1e293b" font-size="10.2">• Hesap bilinciyle kul hakkından sakınmak</text>'
    s += '<text x="585" y="172" text-anchor="middle" fill="#15803d" font-size="10.5" font-weight="700">&quot;Allah\'ın sana verdiğiyle ahireti ara!&quot;</text>'
    s += '<text x="585" y="192" text-anchor="middle" fill="#dc2626" font-size="9.8">Aşırılık: Ruhbanlık (Dünyayı tamamen terk)</text>'

    s += '<rect x="30" y="246" width="700" height="40" rx="8" fill="#ccfbf1" stroke="#0d9488"/>'
    s += '<text x="380" y="270" text-anchor="middle" fill="#0f766e" font-size="11" font-weight="700">Rabbenâ Âtinâ Duası (Bakara, 201): &quot;Rabbimiz! Bize dünyada da iyilik (hasene) ver, ahirette de iyilik ver!&quot;</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Asr Suresi Işığında Hayatın Anlamını Koruyan 4 Temel İlke."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Asr Suresi Işığında İnsanı Hüsrandan (Ziyandan) Kurtaran 4 İlke", "#1d4ed8", "#eff6ff")

    ilkeler = [
        ("1. Sahih İman", "Ellezîne âmenû", "Allah'a, ahirete ve", "iman esaslarına", "şüphesiz inanmak.", "#1d4ed8", "#dbeafe"),
        ("2. Salih Amel", "Ve amilü's-sâlihât", "İmanı doğrulayan,", "insanlığa faydalı", "güzel işler yapmak.", "#16a34a", "#dcfce7"),
        ("3. Hakkı Tavsiye", "Ve tevâsav bi'l-hakk", "Topluma doğruluğu,", "adaleti ve hakikati", "hatırlatmak.", "#d97706", "#fef3c7"),
        ("4. Sabrı Tavsiye", "Ve tevâsav bi's-sabr", "Zorluklara ve günaha", "karşı direnmekte", "yardımlaşmak.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, ar, a1, a2, a3, r, bg) in enumerate(ilkeler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="106" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{ar}</text>'
        s += f'<text x="{x+84}" y="140" text-anchor="middle" fill="#1e293b" font-size="10.5">{a1}</text>'
        s += f'<text x="{x+84}" y="160" text-anchor="middle" fill="#1e293b" font-size="10.5">{a2}</text>'
        s += f'<text x="{x+84}" y="180" text-anchor="middle" fill="#1e293b" font-size="10.5">{a3}</text>'
        s += f'<text x="{x+84}" y="220" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{"Bireysel Boyut" if i < 2 else "Toplumsal Boyut"}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Hayatı Anlamlandıran Kavramlar: İstikamet, İhlas, Takva ve Tevekkül."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Müminin Hayat Pusulası: İstikamet, İhlas, Takva ve Tevekkül", "#7c3aed", "#f5f3ff")

    kavramlar = [
        ("İstikamet (Sırat-ı Müstakim)", "İfrat ve tefritten uzak durarak", "emrolunduğu gibi dosdoğru", "yaşamak (Hûd, 112).", "#7c3aed", "#f5f3ff"),
        ("İhlas (Samimiyet)", "İbadet ve iyilikleri gösterişten", "(riyadan) uzak, yalnız Allah", "rızası için yapmak.", "#0284c7", "#f0f9ff"),
        ("Takva (Sorumluluk Bilinci)", "Allah'ın sevgisini kaybetmekten", "sakınarak haramlardan ve kul", "hakkından korunmak.", "#16a34a", "#f0fdf4"),
        ("Tevekkül ve Azim", "Üzerine düşen tüm tedbirleri", "aldıktan sonra sonucu Allah'a", "güvenerek bırakmak.", "#d97706", "#fffbeb"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(kavramlar):
        x = 28 + (i % 2) * 358
        y = 58 + (i // 2) * 116
        s += f'<rect x="{x}" y="{y}" width="344" height="102" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="{y}" width="344" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+172}" y="{y+18}" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+172}" y="{y+48}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+172}" y="{y+66}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+172}" y="{y+84}" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Zaman ve Ömür Sermayesinin Değerlendirilmesi (Beş Şey Gelmeden Beş Şeyin Kıymeti)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Ömür Sermayesini Koruma: 'Beş Şey Gelmeden Beş Şeyin Kıymetini Bil!'", "#b45309", "#fffbeb")

    hadis = [
        ("1. Gençliğin Kıymeti", "İhtiyarlık gelmeden önce!", "#dc2626"),
        ("2. Sağlığın Kıymeti", "Hastalık gelmeden önce!", "#16a34a"),
        ("3. Zenginliğin Kıymeti", "Fakirlik gelmeden önce!", "#d97706"),
        ("4. Boş Vaktin Kıymeti", "Meşguliyet gelmeden önce!", "#0284c7"),
        ("5. Hayatın Kıymeti", "Ölüm gelmeden önce!", "#7c3aed"),
    ]
    for i, (bas, alt, r) in enumerate(hadis):
        x = 24 + i * 144
        s += f'<rect x="{x}" y="60" width="134" height="170" rx="10" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        s += f'<circle cx="{x+67}" cy="98" r="20" fill="{r}"/>'
        s += f'<text x="{x+67}" y="104" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">{i+1}</text>'
        s += f'<text x="{x+67}" y="144" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+67}" y="176" text-anchor="middle" fill="#334155" font-size="9.8">{alt}</text>'

    s += '<rect x="24" y="244" width="712" height="42" rx="8" fill="#fef3c7" stroke="#d97706"/>'
    s += '<text x="380" y="269" text-anchor="middle" fill="#92400e" font-size="11" font-weight="700">Hadis-i Şerif: İnsanın ahirette ilk sorgulanacağı nimetler ömrünü, gençliğini, malını ve ilmini nerede harcadığıdır.</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
