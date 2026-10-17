# -*- coding: utf-8 -*-
"""12. Sınıf Kimya — 4. Hafta görsel modülü: Elektroliz, Faraday Yasaları ve Korozyon."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">PİL POTANSİYELİNE ETKİ EDEN FAKTÖRLER (LE CHATELIER İLKESİ)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Pil potansiyelini (E_pil) Artıran Etkiler", [
        "• Net pil tepkimesi: A(k) + B⁺(suda) ⇌ A⁺(suda) + B(k) + ısı",
        "• Katot yarı hücresindeki B⁺ derişimini artırmak",
        "• Anot yarı hücresindeki A⁺ derişimini azaltmak (su eklemek)",
        "• Anot yarı hücresine A⁺ iyonlarını çöktüren madde eklemek",
        "• Ekzotermik pil tepkimesinde sıcaklığı düşürmek",
        "• Dengeyi ürünler yönüne (sağa) kaydıran her etki E_pil'i artırır"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Pil Potansiyelini Değiştirmeyen / Azaltanlar", [
        "• Elektrotların kütlesi, boyutu ve temas yüzeyi",
        "  pil potansiyelini (E_pil) DEĞİŞTİRMEZ!",
        "• Anot derişimini artırmak veya katot derişimini",
        "  azaltmak dengeyi girenlere kaydırır (E_pil azalır)",
        "• Sıcaklığı artırmak dengeyi sola kaydırır (E_pil azalır)",
        "• Pil çalıştıkça E_pil azalır; E_pil = 0 olunca pil biter"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">GALVANİK HÜCRE (PİL) İLE ELEKTROLİTİK HÜCRE KARŞILAŞTIRMASI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Galvanik Hücre (Elektrokimyasal Pil)", [
        "• Kimyasal enerjiyi elektrik enerjisine dönüştürür",
        "• İstemsiz değil, İSTEMLİ redoks tepkimesidir (E° > 0)",
        "• Anot negatif (-), katot pozitif (+) kutuptur",
        "• Anotta yükseltgenme, katotta indirgenme olur",
        "• Tuz köprüsü ile yük denkliği sağlanır",
        "• Örnek: Daniell pili, lityum-iyon piller"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Elektrolitik Hücre (Elektroliz Kabı)", [
        "• Elektrik enerjisini kimyasal enerjiye dönüştürür",
        "• İSTEMSİZ redoks tepkimesi dış üreteçle gerçekleştirilir",
        "• Anot pozitif (+), katot negatif (-) kutuptur",
        "• Yine anotta yükseltgenme, katotta indirgenme olur",
        "• Katyonlar (-) katoda, anyonlar (+) anoda gider",
        "• Örnek: Suyun elektrolizi, erimiş tuzların elektrolizi"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">FARADAY ELEKTROLİZ YASALARI VE HESAPLAMALARI</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "1. Temel Bağıntılar", [
        "• Q = I · t",
        "  Q: Yük (Coulomb, C)",
        "  I: Akım şiddeti (Amper, A)",
        "  t: Süre (Saniye, s)",
        "• 1 mol e⁻ = 1 Faraday (F)",
        "• 1 F ≈ 96500 Coulomb"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "2. Kütle Hesabı (m)", [
        "• n(e⁻) = Q / 96500 = (I · t) / 96500",
        "• Xⁿ⁺ + n e⁻ -> X(k)",
        "• Toplanan madde kütlesi:",
        "  m = (I · t · M_A) / (96500 · z)",
        "• M_A: Mol kütlesi",
        "• z: Alınan/verilen e⁻ sayısı (tesir)"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "3. Seri Bağlı Kaplar", [
        "• Seri bağlı elektroliz kaplarından",
        "  geçen elektrik yükü (Q) ve",
        "  devreden geçen e⁻ mol sayısı",
        "  BİRBİRİNE EŞİTTİR!",
        "• n₁ · z₁ = n₂ · z₂",
        "• (m₁/M_A1)·z₁ = (m₂/M_A2)·z₂"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">KOROZYON VE KOROZYONDAN KORUNMA YÖNTEMLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Korozyon ve Elektrolitik Kaplama", [
        "• Korozyon: Metallerin ortam etkisiyle elektrokimyasal",
        "  olarak yükseltgenip aşınmasıdır (Demirin paslanması)",
        "• Boyama ve Galvanizleme (çinko ile kaplama) korur",
        "• Elektrolitik Kaplama: Kaplama yapılacak eşya",
        "  KATODA (-), kaplayacak metal ANODA (+) bağlanır",
        "• Çözeltide kaplayacak metalin iyonları bulunur"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Katodik Koruma (Kurban Elektrot)", [
        "• Gemi gövdeleri, köprü ayakları ve yer altı boru",
        "  hatlarını korozyondan korumak için uygulanır",
        "• Korunacak metale, kendisinden DAHA AKTİF (E° yükseltgenme",
        "  potansiyeli daha büyük) bir metal bağlanır",
        "• Aktif metal (Mg, Zn, Al) anot olup kendi yükseltgenir;",
        "  buna 'Kurban Elektrot' denir; ana metal katot olup korunur"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]