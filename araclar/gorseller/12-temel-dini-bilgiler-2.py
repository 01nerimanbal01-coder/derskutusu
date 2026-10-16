# -*- coding: utf-8 -*-
"""12. Sınıf Temel Dinî Bilgiler (İslam 2) — 2. Hafta SVG Görselleri"""

RENK = {
    "kirmizi": "#e63946",
    "mavi": "#2563eb",
    "yesil": "#16a34a",
    "turuncu": "#ea580c",
    "mor": "#7c3aed",
    "lacivert": "#1e293b",
    "acik_mavi": "#eff6ff",
    "acik_yesil": "#f0fdf4",
    "acik_turuncu": "#fff7ed",
    "acik_mor": "#f5f3ff",
    "acik_kirmizi": "#fef2f2",
    "gri": "#64748b",
    "acik_gri": "#f8fafc",
    "cizgi": "#cbd5e1",
}


def _baslik(W, H, etiket, baslik_metni, renk):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px; font-family:\'Inter\', \'Segoe UI\', sans-serif;">'
        f'<rect width="{W}" height="{H}" rx="14" fill="{RENK["acik_gri"]}" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
        f'<rect x="16" y="14" width="110" height="24" rx="6" fill="{renk}"/>'
        f'<text x="71" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{etiket}</text>'
        f'<text x="138" y="31" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{baslik_metni}</text>'
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="{RENK["cizgi"]}" stroke-width="1"/>'
    )


def gorsel_1():
    """İslam İnancının Temel Kaynakları: Kitap (Kur'an) ve Sünnet"""
    W, H = 720, 320
    s = _baslik(W, H, "TEMEL KAYNAKLAR", "İslam İnancının İki Temel Kaynağı: Kur'an-ı Kerim ve Sünnet", RENK["mavi"])
    boxes = [
        ("1. KİTAP (KUR'AN-I KERİM)", "İslam'ın İlk ve Asli Kaynağı", [
            "• Cebrail (as) aracılığıyla Hz. Muhammed'e (sav) Arapça",
            "  olarak indirilmiş, mushaflara yazılmış ilahi kitaptır.",
            "• Tevatür yoluyla hiçbir değişikliğe uğramadan ulaşmıştır.",
            "• İnanç, ibadet, ahlak ve sosyal hayatın temel hükümlerini",
            "  belirler; fıtrat (doğuştan inanma yeteneği) ile uyumludur.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("2. SÜNNET (KAVLÎ, FİİLÎ VE TAKRİRÎ)", "Kur'an'ın Açıklayıcısı ve Uygulama Rehberi", [
            "• Kavlî Sünnet: Hz. Peygamber'in mübarek sözleri.",
            "• Fiilî Sünnet: Hz. Peygamber'in davranış ve uygulamaları.",
            "• Takrirî Sünnet: Sahabenin yaptığı işleri görüp onaylaması.",
            "• Kur'an'da emredilen namaz, oruç, zekât ve hac gibi",
            "  ibadetlerin nasıl yapılacağını uygulamalı olarak gösterir.",
        ], RENK["yesil"], RENK["acik_yesil"]),
    ]
    for i, (b, alt, items, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+60}" font-size="11.5" font-weight="700" fill="{rk}">{alt}</text>'
        for j, m in enumerate(items):
            s += f'<text x="{x+14}" y="{y+90 + j*28}" font-size="10.8" fill="{RENK["lacivert"]}">{m}</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Ravi Sayısı ve Sağlamlık Bakımından Hadis Çeşitleri"""
    W, H = 720, 320
    s = _baslik(W, H, "HADİS TASNİFİ", "Ravi Sayısı ve Sağlamlık Derecesine Göre Hadis Çeşitleri", RENK["mor"])
    cols = [
        ("Ravilerin Sayısı Bakımından", RENK["mavi"], RENK["acik_mavi"], [
            ("1. Mütevatir Hadis", "Her devirde yalan üzere birleşmesi imkânsız toplulukların naklettiği kesin hadis."),
            ("2. Meşhur Hadis", "İlk nesilde 1-2 kişi iken sonraki dönemlerde 3+ raviyle yaygınlaşan hadis."),
            ("3. Âhâd Hadis", "Her tabakada bir veya birkaç kişi tarafından nakledilen (mütevatir olmayan) hadis."),
        ]),
        ("Sağlamlık Derecesi Bakımından", RENK["mor"], RENK["acik_mor"], [
            ("1. Sahih Hadis", "Adalet ve zabt sahibi güvenilir ravilerin kesintisiz senetle naklettiği sağlam hadis."),
            ("2. Hasen Hadis", "Ravisinin hafıza/ezber yönü sahih derecesine tam çıkamayan, ibadet/ahlakta delil olan hadis."),
            ("3. Zayıf Hadis", "Senet veya ravisinde kusur bulunan; inanç ve helal-haram konularında delil sayılmayan hadis."),
        ]),
    ]
    for i, (title, rk, ark, rows) in enumerate(cols):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+22}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">{title}</text>'
        for j, (k, v) in enumerate(rows):
            yy = y + 60 + j * 60
            s += f'<text x="{x+14}" y="{yy}" font-size="11.5" font-weight="800" fill="{rk}">{k}</text>'
            s += f'<text x="{x+14}" y="{yy+18}" font-size="10.3" fill="{RENK["lacivert"]}">{v[:48]}</text>'
            s += f'<text x="{x+14}" y="{yy+34}" font-size="10.3" fill="{RENK["lacivert"]}">{v[48:]}</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """İcmali İman - Tafsili İman ve İmanın Mahiyeti"""
    W, H = 720, 320
    s = _baslik(W, H, "İMANIN MAHİYETİ", "İcmali İman, Tafsili İman ve Tasdik – İkrar – Amel İlişkisi", RENK["yesil"])
    s += f'<rect x="24" y="62" width="328" height="112" rx="10" fill="{RENK["acik_mavi"]}" stroke="{RENK["mavi"]}" stroke-width="1.8"/>'
    s += f'<text x="188" y="88" text-anchor="middle" font-size="13" font-weight="800" fill="{RENK["mavi"]}">İCMALİ İMAN (Toplu / Özlü İman)</text>'
    s += f'<text x="38" y="114" font-size="11" fill="{RENK["lacivert"]}">• İnanılacak esaslara ayrıntıya girmeden toptan inanmaktır.</text>'
    s += f'<text x="38" y="136" font-size="11" fill="{RENK["lacivert"]}">• Özeti: Kelime-i Tevhit ve Kelime-i Şehadet\'tir.</text>'
    s += f'<text x="38" y="158" font-size="10.5" font-weight="700" fill="{RENK["mavi"]}">Lâ ilâhe illallah Muhammedün Resûlullah</text>'

    s += f'<rect x="368" y="62" width="328" height="112" rx="10" fill="{RENK["acik_yesil"]}" stroke="{RENK["yesil"]}" stroke-width="1.8"/>'
    s += f'<text x="532" y="88" text-anchor="middle" font-size="13" font-weight="800" fill="{RENK["yesil"]}">TAFSİLİ İMAN (Ayrıntılı İman)</text>'
    s += f'<text x="382" y="114" font-size="11" fill="{RENK["lacivert"]}">• İman esaslarının her birine ayrı ayrı ve delilleriyle inanmaktır.</text>'
    s += f'<text x="382" y="136" font-size="11" fill="{RENK["lacivert"]}">• Özeti: Âmentü duası (6 iman esası) ve Kur\'an\'ın tamamı.</text>'
    s += f'<text x="382" y="158" font-size="10.5" font-weight="700" fill="{RENK["yesil"]}">Herhangi bir esası inkâr etmek kişiyi dinden çıkarır.</text>'

    s += f'<rect x="24" y="190" width="672" height="112" rx="10" fill="#fff" stroke="{RENK["lacivert"]}" stroke-width="1.6"/>'
    s += f'<text x="360" y="214" text-anchor="middle" font-size="13" font-weight="800" fill="{RENK["lacivert"]}">Ehlisünnet\'e Göre İmanın Mahiyeti: Kalp ile Tasdik – Dil ile İkrar – Amel</text>'
    s += f'<text x="42" y="240" font-size="11.2" fill="{RENK["lacivert"]}">1. Kalp ile Tasdik: İmanın asıl rüknü (değişmez şartı) kalbin gönülden doğrulamasıdır.</text>'
    s += f'<text x="42" y="262" font-size="11.2" fill="{RENK["lacivert"]}">2. Dil ile İkrar: Kişinin dünyada Müslüman olarak tanınması ve muamele görmesi için gereklidir.</text>'
    s += f'<text x="42" y="284" font-size="11.2" fill="{RENK["lacivert"]}">3. Amel: İmanı korur ve olgunlaştırır; ameli terk eden günahkâr olur fakat dinden çıkmaz.</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """İmanın Geçerli Olmasının 5 Şartı"""
    W, H = 720, 330
    s = _baslik(W, H, "GEÇERLİLİK ŞARTLARI", "İmanın Geçerli Olmasının Beş Temel Şartı", RENK["turuncu"])
    sartlar = [
        ("1. Kesin Hükümleri Kabul", "Farz ve haram olduğu kesin olan hükümleri inkâr etmemek ve alaya almamak", RENK["mavi"], RENK["acik_mavi"]),
        ("2. Bütününe İman Etmek", "Kur'an-ı Kerim'in ve iman esaslarının bir kısmına inanıp bir kısmını reddetmemek", RENK["yesil"], RENK["acik_yesil"]),
        ("3. Korku ve Ümit (Beyne'l-Havfi ve'r-Recâ)", "Allah'ın azabından emin olmamak ve rahmetinden de asla ümit kesmemek", RENK["mor"], RENK["acik_mor"]),
        ("4. Son Nefese Ertelememek", "Ölüm (ye's) anı gelip çatmadan iman etmek (Firavun'un son an imanı geçersizdir)", RENK["turuncu"], RENK["acik_turuncu"]),
        ("5. Hür İradeyle İnanmak", "Baskı, tehdit ve zorlama olmaksızın kendi özgür iradesiyle iman etmek", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (ad, acik, rk, ark) in enumerate(sartlar):
        y = 60 + i * 51
        s += f'<rect x="24" y="{y}" width="672" height="43" rx="8" fill="{ark}" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="225" height="43" rx="8" fill="{rk}"/>'
        s += f'<text x="136" y="{y+26}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="262" y="{y+26}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">{acik}</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """İnanç Bakımından İnsanlar: Mümin, Münafık, Kâfir, Müşrik ve Fasık"""
    W, H = 720, 330
    s = _baslik(W, H, "İNANÇ BAKIMINDAN", "İnanç Bakımından İnsanların Sınıflandırılması", RENK["kirmizi"])
    tipler = [
        ("1. MÜMİN", "Kalbiyle tasdik edip diliyle ikrar eden; ihlasla Allah'a güvenen ve salih amel işleyen kimse.", RENK["yesil"], RENK["acik_yesil"]),
        ("2. MÜNAFIK", "Kalbiyle inanmadığı hâlde menfaat için diliyle Müslüman görünen ikiyüzlü kimse (Nifak).", RENK["turuncu"], RENK["acik_turuncu"]),
        ("3. KÂFİR", "Allah'ın varlığını, birliğini, peygamberini veya dinin kesin hükümlerini inkâr eden kimse (Küfür).", RENK["kirmizi"], RENK["acik_kirmizi"]),
        ("4. MÜŞRİK", "Allah'a inanmakla birlikte zatında, sıfatlarında veya ibadette O'na ortak koşan kimse (Şirk).", RENK["mor"], RENK["acik_mor"]),
        ("5. FÂSIK", "Allah'ın emirlerine itaatten ayrılan, büyük günah işlemeyi alışkanlık edinen kimse (Fısk).", RENK["mavi"], RENK["acik_mavi"]),
    ]
    for i, (ad, acik, rk, ark) in enumerate(tipler):
        y = 60 + i * 51
        s += f'<rect x="24" y="{y}" width="672" height="43" rx="8" fill="{ark}" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="145" height="43" rx="8" fill="{rk}"/>'
        s += f'<text x="96" y="{y+26}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="184" y="{y+26}" font-size="11.3" font-weight="600" fill="{RENK["lacivert"]}">{acik}</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """İslam İnanç Esasları (Âmentü) ve Büyük Melekler"""
    W, H = 720, 320
    s = _baslik(W, H, "ÂMENTÜ ESASLARI", "Altı İman Esası ve Dört Büyük Meleğin Görevleri", RENK["lacivert"])
    esaslar = [
        "1. Allah'a (cc) İman",
        "2. Meleklere İman",
        "3. Kitaplara İman",
        "4. Peygamberlere İman",
        "5. Ahiret Gününe İman",
        "6. Kader ve Kazaya İman",
    ]
    for i, e in enumerate(esaslar):
        col = i % 3
        row = i // 3
        x = 24 + col * 228
        y = 62 + row * 46
        s += f'<rect x="{x}" y="{y}" width="216" height="36" rx="8" fill="{RENK["lacivert"]}"/>'
        s += f'<text x="{x+108}" y="{y+23}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{e}</text>'

    s += f'<rect x="24" y="164" width="672" height="138" rx="10" fill="#fff" stroke="{RENK["mavi"]}" stroke-width="1.8"/>'
    s += f'<text x="360" y="188" text-anchor="middle" font-size="13" font-weight="800" fill="{RENK["mavi"]}">Başlıca Melekler ve Görevleri</text>'
    melekler = [
        ("Cebrail (as):", "Peygamberlere vahiy getirmekle görevli melektir."),
        ("Mikâil (as):", "Tabiat olaylarını ve canlıların rızıklarını düzenlemekle görevlidir."),
        ("İsrafil (as):", "Sûr'a üfleyerek kıyameti ve yeniden dirilişi (ba's) başlatmakla görevlidir."),
        ("Azrail (as) & Kirâmen Kâtibîn:", "Azrail can almakla; Kirâmen Kâtibîn ise insanların amellerini yazmakla görevlidir."),
    ]
    for i, (m, g) in enumerate(melekler):
        yy = 214 + i * 21
        s += f'<text x="42" y="{yy}" font-size="11.2" font-weight="700" fill="{RENK["lacivert"]}">• {m}</text>'
        s += f'<text x="235" y="{yy}" font-size="11.2" fill="{RENK["gri"]}">{g}</text>'
    s += "</svg>"
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
    "b5": gorsel_5(),
    "b6": gorsel_6(),
}



def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
