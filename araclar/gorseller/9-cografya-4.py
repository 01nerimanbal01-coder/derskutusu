# -*- coding: utf-8 -*-
"""9. Sınıf Coğrafya — 4. Hafta görsel modülü:
Mekânsal Bilgi Teknolojileri — Mekânın Aynası Haritalar, Unsurlar, Projeksiyonlar ve Ölçek"""

C_MOR = "#6c3483"
C_MAVI = "#1a5276"
C_YESIL = "#1e8449"
C_TURUNCU = "#b9770e"
C_KIRMIZI = "#922b21"
C_ACIK_MOR = "#f5eef8"
C_ACIK_MAVI = "#eaf2f8"
C_ACIK_YESIL = "#e9f7ef"
C_ACIK_SARI = "#fef9e7"
C_ACIK_KIRMIZI = "#fdedec"
C_KOYU = "#1c2833"
C_GRI = "#566573"
C_SINIR = "#d5d8dc"


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def gorsel_1():
    """Bir Çizimin Harita Sayılabilmesi İçin 3 Şart ve Haritanın 5 Temel Unsuru."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Haritanın Tanımı (Kuşbakışı + Ölçek + Düzlem) ve 5 Temel Unsuru</text>',
    ]
    unsurlar = [
        ("1. Harita Başlığı", "Haritanın kullanım", "amacını ve konusunu", "belirtir.", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Ölçek (Küçültme)", "Gerçek uzunluk ile", "harita uzunluğu", "oranıdır (Kroki ≠ Harita).", C_YESIL, C_ACIK_YESIL, 148),
        ("3. Lejant (Harita Anahtarı)", "Haritadaki sembol,", "renk ve işaretlerin", "dilidir.", C_TURUNCU, C_ACIK_SARI, 280),
        ("4. Yön Oku", "Kuzey yönünü göstererek", "haritanın doğru", "konumlanmasını sağlar.", C_KIRMIZI, C_ACIK_KIRMIZI, 412),
        ("5. Koordinat Sistemi", "Enlem ve boylamlarla", "mutlak konumu", "gösterir.", C_MOR, C_ACIK_MOR, 544),
    ]
    for baslik, s1, s2, s3, renk, bg, x in unsurlar:
        p.append(f'<rect x="{x}" y="60" width="120" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="120" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+60}" y="79" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+60}" y="116" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+60}" y="136" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+60}" y="156" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+12}" y="182" width="96" height="44" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+60}" y="209" text-anchor="middle" font-size="9.5" font-weight="700" fill="{renk}">Temel Unsur</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Harita Projeksiyon Yöntemleri: Silindirik, Konik ve Düzlem (Ufki)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Harita Projeksiyon (İzdüşüm) Yöntemleri: Bozulmaları En Aza İndirme</text>',
    ]
    proj = [
        ("1. Silindirik Projeksiyon", "Ekvator ve Çevresi (0°–30°)", "Kutuplara gidildikçe bozulma artar.", "Brezilya, Endonezya, Kenya, Nijerya", "Şekli (açıyı) korur, alanı bozar.", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Konik Projeksiyon", "Orta Kuşak (30°–60° Enlemleri)", "Orta enlemlerden uzaklaştıkça bozulur.", "Türkiye, İtalya, Fransa, Japonya, ABD", "Alan koruyan haritalarda yaygındır.", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Düzlem (Ufki) Projeksiyon", "Kutup Bölgeleri (60°–90°) ve Dar Alan", "Merkez noktadan uzaklaştıkça bozulur.", "Antarktika, Grönland, İzlanda, Norveç", "Dar alanlı büyük ölçekli çizimler.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, kusak, kural, ulkeler, ozellik, renk, bg, x in proj:
        p.append(f'<rect x="{x}" y="58" width="208" height="186" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="{renk}">{kusak}</text>')
        p.append(f'<text x="{x+104}" y="126" text-anchor="middle" font-size="10" fill="{C_KOYU}">{kural}</text>')
        p.append(f'<rect x="{x+12}" y="140" width="184" height="50" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="160" text-anchor="middle" font-size="9.5" font-weight="700" fill="{C_KOYU}">Örnek Ülkeler / Bölgeler:</text>')
        p.append(f'<text x="{x+104}" y="178" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{ulkeler}</text>')
        p.append(f'<text x="{x+104}" y="218" text-anchor="middle" font-size="9.5" font-weight="600" fill="{C_GRI}">{ozellik}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Konularına Göre Harita Türleri: Genel ve Tematik (Özel) Haritalar."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kullanım Amaçlarına (Konularına) Göre Harita Türleri</text>',
        # Sol: Genel
        f'<rect x="18" y="58" width="314" height="172" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Genel Haritalar (Çok Amaçlı)</text>',
        f'<text x="32" y="108" font-size="10.5" fill="{C_KOYU}" font-weight="700">• Fiziki Haritalar: Yükselti basamaklarını ve</text>',
        f'<text x="42" y="124" font-size="10.5" fill="{C_KOYU}">yer şekillerini gösterir (Renkler = Yükselti!).</text>',
        f'<text x="32" y="148" font-size="10.5" fill="{C_KOYU}" font-weight="700">• Siyasi / İdari Haritalar: Ülke ve il sınırlarını,</text>',
        f'<text x="42" y="164" font-size="10.5" fill="{C_KOYU}">başkentleri ve yönetim birimlerini gösterir.</text>',
        f'<text x="32" y="188" font-size="10.5" fill="{C_MAVI}" font-weight="700">• Topoğrafya ve Atlas Haritaları</text>',
        # Sağ: Tematik
        f'<rect x="348" y="58" width="314" height="172" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Tematik (Özel) Haritalar (Tek Konulu)</text>',
        f'<text x="362" y="108" font-size="10.5" fill="{C_KOYU}" font-weight="700">Belirli bir konunun mekânsal dağılışını gösterir:</text>',
        f'<text x="362" y="130" font-size="10.5" fill="{C_KOYU}">• Türkiye Deprem Tehlike Haritası, Jeoloji Haritası</text>',
        f'<text x="362" y="150" font-size="10.5" fill="{C_KOYU}">• İklim, Toprak, Bitki Örtüsü ve Hidrografya Haritası</text>',
        f'<text x="362" y="170" font-size="10.5" fill="{C_KOYU}">• Nüfus Yoğunluğu, Göç, Turizm ve Maden Haritası</text>',
        f'<text x="362" y="194" font-size="10.5" fill="{C_YESIL}" font-weight="700">• Koroplet, Korokromatik, İzoplet ve Noktalama</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Büyük Ölçekli ve Küçük Ölçekli Haritaların Karşılaştırılması."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Ölçeklerine Göre Haritaların Karşılaştırılması (Kesir Ölçek Paydasına Dikkat!)</text>',
        # Sol: Büyük Ölçek
        f'<rect x="18" y="58" width="314" height="176" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Büyük Ölçekli Haritalar (1/1.000 – 1/200.000)</text>',
        f'<text x="32" y="106" font-size="10.5" fill="{C_KOYU}">• Ölçek paydası KÜÇÜKTÜR (Az küçültülmüştür).</text>',
        f'<text x="32" y="126" font-size="10.5" fill="{C_KOYU}">• Dar alanları gösterir (Şehir planı, topoğrafya).</text>',
        f'<text x="32" y="146" font-size="10.5" fill="{C_KOYU}">• Ayrıntı gösterme gücü YÜKSEKTİR.</text>',
        f'<text x="32" y="166" font-size="10.5" fill="{C_KOYU}">• Bozulma (hata) oranı AZDIR.</text>',
        f'<text x="32" y="186" font-size="10.5" font-weight="700" fill="{C_TURUNCU}">• İzohipsler arası yükselti farkı (Δh) AZDIR.</text>',
        # Sağ: Küçük Ölçek
        f'<rect x="348" y="58" width="314" height="176" rx="10" fill="{C_ACIK_KIRMIZI}" stroke="{C_KIRMIZI}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_KIRMIZI}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Küçük Ölçekli Haritalar (1/500.000\'den Küçük)</text>',
        f'<text x="362" y="106" font-size="10.5" fill="{C_KOYU}">• Ölçek paydası BÜYÜKTÜR (Çok küçültülmüştür).</text>',
        f'<text x="362" y="126" font-size="10.5" fill="{C_KOYU}">• Geniş alanları gösterir (Dünya ve Kıta haritaları).</text>',
        f'<text x="362" y="146" font-size="10.5" fill="{C_KOYU}">• Ayrıntı gösterme gücü DÜŞÜKTÜR.</text>',
        f'<text x="362" y="166" font-size="10.5" fill="{C_KOYU}">• Bozulma (hata) oranı FAZLADIR.</text>',
        f'<text x="362" y="186" font-size="10.5" font-weight="700" fill="{C_KIRMIZI}">• İzohipsler arası yükselti farkı (Δh) FAZLADIR.</text>',
    ]
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
    return v
