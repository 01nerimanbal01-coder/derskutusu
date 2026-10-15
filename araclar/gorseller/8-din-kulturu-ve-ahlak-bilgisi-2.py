# -*- coding: utf-8 -*-
"""8. Sınıf Din Kültürü ve Ahlak Bilgisi — 2. Hafta SVG görselleri.
Konu: 2. İnsanın İradesi ve Kader (Akıl, Küllî İrade, Cüzî İrade, Sorumluluk).
"""
from ozet_gorsel import svg


def g1():
    """Bölüm 1: İnsanın Özellikleri ve Sorumluluk Zinciri (Grafik 1.2 uyarlaması)."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#0f766e"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">İNSANI DİĞER VARLIKLARDAN AYIRAN ÖZELLİKLER</text>')

    # Merkez daire / kutu
    ic.append('<rect x="295" y="130" width="190" height="72" rx="14" fill="#f0fdfa" stroke="#0d9488" stroke-width="2.5"/>')
    ic.append('<text x="390" y="160" text-anchor="middle" font-size="16" font-weight="800" fill="#134e4a">İNSAN</text>')
    ic.append('<text x="390" y="182" text-anchor="middle" font-size="12" font-weight="600" fill="#0f766e">Mükellef (Sorumlu) Varlık</text>')

    # 5 özellik kutusu
    kutular = [
        (25, 65, 220, 62, "#eff6ff", "#3b82f6", "#1e3a8a", "1. Akıl ve İrade Sahibi", "İyiyi kötüden ayırt eder"),
        (535, 65, 220, 62, "#fef3c7", "#f59e0b", "#78350f", "2. Düşünme Yeteneği", "Tefekkür eder ve öğüt alır"),
        (25, 165, 220, 62, "#f3e8ff", "#9333ea", "#581c87", "3. Vahyin Rehberliği", "Peygamber ve kitapla yol bulur"),
        (535, 165, 220, 62, "#dcfce7", "#16a34a", "#14532d", "4. Özgür Olması", "Baskı olmadan seçim yapar"),
        (265, 240, 250, 60, "#fee2e2", "#e11d48", "#881337", "5. Sorumlu Olması", "Tercihlerinin sonucunu üstlenir"),
    ]
    for x, y, w, h, bg, st, tc, b1, b2 in kutular:
        ic.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.8"/>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 26}" text-anchor="middle" font-size="13" font-weight="700" fill="{tc}">{b1}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 46}" text-anchor="middle" font-size="12" fill="#334155">{b2}</text>')

    # Bağlantı çizgileri
    ic.append('<line x1="245" y1="96" x2="295" y2="145" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,3"/>')
    ic.append('<line x1="535" y1="96" x2="485" y2="145" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,3"/>')
    ic.append('<line x1="245" y1="196" x2="295" y2="178" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,3"/>')
    ic.append('<line x1="535" y1="196" x2="485" y2="178" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,3"/>')
    ic.append('<line x1="390" y1="202" x2="390" y2="240" stroke="#e11d48" stroke-width="2.2"/>')

    return svg(780, 315, "".join(ic), "İnsanın özellikleri şeması")


def g2():
    """Bölüm 2: Cüzî İrade ve Seçim Alanları."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#1d4ed8"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">CÜZÎ İRADE: İNSANIN ÖZGÜR TERCİH ALANI</text>')

    ic.append('<rect x="240" y="66" width="300" height="52" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>')
    ic.append('<text x="390" y="89" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">CÜZÎ İRADE (Sınırlı Özgürlük)</text>')
    ic.append('<text x="390" y="108" text-anchor="middle" font-size="12" fill="#1e40af">İnsanın dileme, seçme ve karar verme gücü</text>')

    secimler = [
        (25, 145, 230, "#f0fdf4", "#16a34a", "#14532d", "İbadet ve Kulluk", "Namaz kılmak, oruç tutmak,", "dua ve şükürde bulunmak"),
        (275, 145, 230, "#fefce8", "#ca8a04", "#713f12", "Ahlaki Davranışlar", "Doğru söylemek, yardımlaşmak,", "kötülükten uzak durmak"),
        (525, 145, 230, "#fdf2f8", "#db2777", "#831843", "Çalışma ve Tedbir", "Ders çalışmak, meslek seçmek,", "kurallara ve sağlığa dikkat etmek"),
    ]
    for x, y, w, bg, st, tc, bas, s1, s2 in secimler:
        ic.append(f'<line x1="390" y1="118" x2="{x + w // 2}" y2="{y}" stroke="#64748b" stroke-width="1.8"/>')
        ic.append(f'<rect x="{x}" y="{y}" width="{w}" height="92" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.8"/>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 26}" text-anchor="middle" font-size="13" font-weight="700" fill="{tc}">{bas}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 50}" text-anchor="middle" font-size="12" fill="#334155">{s1}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 70}" text-anchor="middle" font-size="12" fill="#334155">{s2}</text>')

    ic.append('<rect x="25" y="252" width="730" height="42" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>')
    ic.append('<text x="390" y="278" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">Sonuç: İnsan kendi cüzî iradesiyle yaptığı tüm bu seçimlerden sorumludur.</text>')

    return svg(780, 308, "".join(ic), "Cüzî irade ve insanın tercih alanı")


def g3():
    """Bölüm 3: Küllî İrade ve Cüzî İrade Karşılaştırması."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#4f46e5"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">KÜLLÎ İRADE İLE CÜZÎ İRADE KARŞILAŞTIRMASI</text>')

    # Sol sütun: Külli İrade
    ic.append('<rect x="25" y="66" width="350" height="225" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>')
    ic.append('<rect x="25" y="66" width="350" height="38" rx="10" fill="#7c3aed"/>')
    ic.append('<text x="200" y="90" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">KÜLLÎ İRADE (Allah\'ın İradesi)</text>')
    kulli = [
        "• Sınırsız, mutlak ve her şeye hâkimdir.",
        "• Anne-baba, ırk ve doğum yeri seçimi.",
        "• Göz rengi, saç rengi ve fiziksel yapı.",
        "• Kalp atışı ve solunum gibi biyolojik düzen.",
        "• İnsan bu alandan SORUMLU TUTULMAZ."
    ]
    for i, m in enumerate(kulli):
        renk = "#5b21b6" if i == 4 else "#1e293b"
        kalin = "700" if i == 4 else "500"
        ic.append(f'<text x="42" y="{130 + i * 32}" font-size="13" font-weight="{kalin}" fill="{renk}">{m}</text>')

    # Sağ sütun: Cüzi İrade
    ic.append('<rect x="405" y="66" width="350" height="225" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>')
    ic.append('<rect x="405" y="66" width="350" height="38" rx="10" fill="#059669"/>')
    ic.append('<text x="580" y="90" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">CÜZÎ İRADE (İnsanın İradesi)</text>')
    cuzi = [
        "• Allah\'ın insana verdiği sınırlı özgürlüktür.",
        "• İman etmek, ibadet etmek ve dua etmek.",
        "• İyi veya kötü ahlaki davranışları seçmek.",
        "• Çalışmak, araştırmak ve tedbir almak.",
        "• İnsan bu alandan SORUMLU TUTULUR."
    ]
    for i, m in enumerate(cuzi):
        renk = "#065f46" if i == 4 else "#1e293b"
        kalin = "700" if i == 4 else "500"
        ic.append(f'<text x="422" y="{130 + i * 32}" font-size="13" font-weight="{kalin}" fill="{renk}">{m}</text>')

    return svg(780, 305, "".join(ic), "Küllî irade ve cüzî irade karşılaştırma tablosu")


def g4():
    """Bölüm 5: İki Yol, Tercih ve Sorumluluk Süreci."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#b45309"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">AKIL, VAHİY, TERCİH VE SORUMLULUK SÜRECİ</text>')

    adimlar = [
        (25, 72, 165, 110, "#eff6ff", "#2563eb", "#1e3a8a", "1. Rehberlik", "Akıl + Vahiy", "Doğru ve yanlış", "yolu gösterir"),
        (215, 72, 165, 110, "#fef3c7", "#d97706", "#78350f", "2. Tercih", "Cüzî İrade", "İnsan iki yoldan", "birini seçer"),
        (405, 72, 165, 110, "#f3e8ff", "#7c3aed", "#581c87", "3. Yaratma", "Küllî İrade", "Allah kulun seçtiği", "fiili yaratır"),
        (595, 72, 160, 110, "#dcfce7", "#16a34a", "#14532d", "4. Karşılık", "Sorumluluk", "Kişi sonucunu", "üstlenir"),
    ]
    for x, y, w, h, bg, st, tc, b1, b2, s1, s2 in adimlar:
        ic.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{st}" stroke-width="2"/>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 26}" text-anchor="middle" font-size="13" font-weight="800" fill="{tc}">{b1}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 48}" text-anchor="middle" font-size="13" font-weight="700" fill="{st}">{b2}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 72}" text-anchor="middle" font-size="12" fill="#334155">{s1}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 90}" text-anchor="middle" font-size="12" fill="#334155">{s2}</text>')

    # Oklar
    for x1, x2 in [(190, 215), (380, 405), (570, 595)]:
        ic.append(f'<line x1="{x1}" y1="127" x2="{x2}" y2="127" stroke="#64748b" stroke-width="2.5"/>')

    # Alt kutu: Ayet ilkeleri
    ic.append('<rect x="25" y="200" width="730" height="72" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>')
    ic.append('<text x="390" y="226" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">Kur\'an İlkeleri: "Şüphesiz biz ona doğru yolu gösterdik..." (İnsan, 3)</text>')
    ic.append('<text x="390" y="250" text-anchor="middle" font-size="12" fill="#78350f">"Allah, hiç kimseye gücünün üstünde bir şey yüklemez..." (Bakara, 286) • "...Yaptıklarınızdan mutlaka sorumlu tutulacaksınız." (Nahl, 93)</text>')

    return svg(780, 286, "".join(ic), "Akıl, vahiy, irade ve sorumluluk süreci")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[1]["gorsel"] = g2()
    b[2]["gorsel"] = g3()
    b[4]["gorsel"] = g4()
