# -*- coding: utf-8 -*-
"""12. Sınıf Kelam — 2. Hafta SVG Görselleri"""

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
    """Kelam İlminin Doğuşu ve Tarihî Gelişim Dönemleri (5 Dönem)"""
    W, H = 720, 330
    s = _baslik(W, H, "TARİHÇE", "Kelam İlminin Doğuşu ve Beş Tarihî Dönemi", RENK["mavi"])
    donemler = [
        ("1. Hz. Peygamber", "Vahiy ve sünnet rehberliği; tartışmasız teslimiyet", RENK["yesil"], RENK["acik_yesil"]),
        ("2. İlk İhtilaflar", "Büyük günah ve kader tartışmaları; Ebu Hanife (Fıkh-ı Ekber)", RENK["mavi"], RENK["acik_mavi"]),
        ("3. Mutezile Dönemi", "Vâsıl b. Atâ; akılcı savunu, el-menzile beyne'l-menzileteyn", RENK["turuncu"], RENK["acik_turuncu"]),
        ("4. Ehlisünnet Kelamı", "İmam Eş'arî ve İmam Mâtürîdî; nakil ile aklın dengesi", RENK["mor"], RENK["acik_mor"]),
        ("5. Yeni İlm-i Kelam", "XIX. yy'dan günümüze pozitivizm ve materyalizme cevap", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (ad, acik, rk, ark) in enumerate(donemler):
        y = 60 + i * 51
        s += f'<rect x="24" y="{y}" width="672" height="43" rx="8" fill="{ark}" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="175" height="43" rx="8" fill="{rk}"/>'
        s += f'<text x="111" y="{y+26}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="215" y="{y+26}" font-size="12" font-weight="600" fill="{RENK["lacivert"]}">{acik}</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Ehlisünnet Kelamının Oluşumu: Eş'arîlik ve Mâtürîdîlik"""
    W, H = 720, 320
    s = _baslik(W, H, "EHLİSÜNNET", "Ehlisünnet Kelam Mektepleri: Eş'arîlik ve Mâtürîdîlik", RENK["yesil"])
    boxes = [
        ("Eş'arîlik Mektebi", "Kurucu: Ebü'l-Hasan el-Eş'arî (ö. 936)", [
            "• Bağdat ve Basra merkezli gelişmiştir.",
            "• Önemli âlimler: Bâkıllânî, Cüveynî, İmam Gazâlî,",
            "  Fahreddin er-Râzî, Beyzâvî, Cürcânî.",
            "• Temel eser: el-İbâne an Usûli'd-Diyâne, el-Lüma'.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("Mâtürîdîlik Mektebi", "Kurucu: Ebu Mansûr el-Mâtürîdî (ö. 944)", [
            "• Semerkant (Mâverâünnehir) merkezli gelişmiştir.",
            "• Ebu Hanife'nin itikadi görüşlerini sistemleştirmiştir.",
            "• Önemli âlimler: Ebü'l-Muîn en-Nesefî, Nûreddin es-Sâbûnî.",
            "• Temel eser: Kitâbü't-Tevhîd, Tabsıratü'l-Edille.",
        ], RENK["yesil"], RENK["acik_yesil"]),
    ]
    for i, (b, alt, maddeler, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+60}" font-size="11.5" font-weight="700" fill="{rk}">{alt}</text>'
        for j, m in enumerate(maddeler):
            s += f'<text x="{x+16}" y="{y+90 + j*32}" font-size="11.5" fill="{RENK["lacivert"]}">{m}</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """Mütekaddimîn, Müteahhirîn ve Yeni İlm-i Kelam"""
    W, H = 720, 320
    s = _baslik(W, H, "DÖNEMLER", "Mütekaddimîn, Müteahhirîn ve Yeni İlm-i Kelam Ayrımı", RENK["mor"])
    cols = [
        ("Mütekaddimîn Dönemi", "Gazâlî Öncesi (VIII–XI. yy)", [
            "• Kelamın kuruluş ve sistemleşme dönemidir.",
            "• Bâkıllânî ve Cüveynî gibi âlimler öne çıkar.",
            "• Aristo mantığı henüz kelama dâhil edilmemiştir.",
            "• Bilginin delile bağımlı olduğu (in'ikâs-ı edille) savunulur.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("Müteahhirîn Dönemi", "Gazâlî Sonrası (XI–XIX. yy)", [
            "• İmam Gazâlî ile başlayan felsefe-mantık mezcidir.",
            "• Aristo mantığı kelamda yöntem olarak kullanılmıştır.",
            "• Râzî, Beyzâvî, Teftâzânî ve Cürcânî başlıca temsilcilerdir.",
            "• Felsefe ile kelam konuları aynı eserlerde tartışılmıştır.",
        ], RENK["mor"], RENK["acik_mor"]),
        ("Yeni İlm-i Kelam", "XIX. Yüzyıldan Günümüze", [
            "• Batı'da doğan pozitivizm, materyalizm, Darwinizm",
            "  ve Freudizm akımlarına karşı İslam inancını savunur.",
            "• İzmirli İsmail Hakkı, Abdüllatif Harpûtî, Filibeli",
            "  Ahmed Hilmi ve Muhammed İkbal öncü isimlerdir.",
        ], RENK["turuncu"], RENK["acik_turuncu"]),
    ]
    for i, (t, sub, items, rk, ark) in enumerate(cols):
        x = 20 + i * 230
        y = 64
        s += f'<rect x="{x}" y="{y}" width="218" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+109}" y="{y+22}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{t}</text>'
        s += f'<text x="{x+109}" y="{y+54}" text-anchor="middle" font-size="11" font-weight="700" fill="{rk}">{sub}</text>'
        for j, it in enumerate(items):
            s += f'<text x="{x+10}" y="{y+82 + j*34}" font-size="10.5" fill="{RENK["lacivert"]}">{it}</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """Kelam İlminin İslami İlimlerle İlişkisi (Küllî İlim - Cüz'î İlimler)"""
    W, H = 720, 320
    s = _baslik(W, H, "İSLAMİ İLİMLER", "Kelamın İslami İlimler İçindeki Konumu (Küllî İlim)", RENK["turuncu"])
    s += f'<rect x="230" y="64" width="260" height="60" rx="12" fill="{RENK["turuncu"]}"/>'
    s += f'<text x="360" y="90" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">KELAM İLMİ (Küllî İlim)</text>'
    s += f'<text x="360" y="110" text-anchor="middle" font-size="11" fill="#fff">Eşrefü\'l-Ulûm • İnanç esaslarını ispatlar</text>'

    ilimler = [
        ("TEFSİR", "Kur'an'ın anlaşılması", "Kelamın vahiy delillerini sağlar", RENK["mavi"], RENK["acik_mavi"]),
        ("HADİS", "Sünnetin tespiti", "Mütevatir ve sahih nakil kaynağı", RENK["yesil"], RENK["acik_yesil"]),
        ("FIKIH", "İbadet ve muamelat", "Fروع (amel) kelamın aslına dayanır", RENK["mor"], RENK["acik_mor"]),
        ("MEZHEPLER TARİHİ", "İtikadi fırkalar", "Görüşlerin tarihî seyrini inceler", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (ad, alt, bag, rk, ark) in enumerate(ilimler):
        x = 20 + i * 172
        y = 166
        s += f'<line x1="360" y1="124" x2="{x+80}" y2="{y}" stroke="{rk}" stroke-width="2"/>'
        s += f'<rect x="{x}" y="{y}" width="160" height="130" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="160" height="30" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+80}" y="{y+20}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="{x+80}" y="{y+56}" text-anchor="middle" font-size="11" font-weight="700" fill="{RENK["lacivert"]}">{alt}</text>'
        s += f'<text x="{x+80}" y="{y+88}" text-anchor="middle" font-size="10.5" fill="{RENK["gri"]}">{bag}</text>'
        s += f'<text x="{x+80}" y="{y+112}" text-anchor="middle" font-size="10" font-weight="600" fill="{rk}">Cüz\'î İlim (Gazâlî)</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """Kelam İlminin Felsefe ve Diğer Bilimlerle İlişkisi"""
    W, H = 720, 320
    s = _baslik(W, H, "DİĞER İLİMLER", "Kelam – Felsefe – Tabiat ve Sosyal Bilimler İlişkisi", RENK["lacivert"])
    s += f'<rect x="24" y="64" width="330" height="236" rx="10" fill="{RENK["acik_mavi"]}" stroke="{RENK["mavi"]}" stroke-width="1.8"/>'
    s += f'<text x="189" y="90" text-anchor="middle" font-size="13.5" font-weight="800" fill="{RENK["mavi"]}">Kelam ve Felsefe Karşılaştırması</text>'
    rows = [
        ("Ortak Yön:", "Varlık, bilgi, Tanrı, evren ve insanı inceler."),
        ("Kelamın Kaynağı:", "Haber-i sâdık (vahiy) + Aklıselim + Duyu"),
        ("Felsefenin Kaynağı:", "Yalnızca akıl ve beş duyu (vahye dayanmaz)"),
        ("Kelamın Amacı:", "Vahiyle gelen hakikati akılla temellendirmek"),
    ]
    for i, (k, v) in enumerate(rows):
        yy = 122 + i * 42
        s += f'<text x="38" y="{yy}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{k}</text>'
        s += f'<text x="38" y="{yy+17}" font-size="11" fill="{RENK["gri"]}">{v}</text>'

    s += f'<rect x="370" y="64" width="326" height="112" rx="10" fill="{RENK["acik_yesil"]}" stroke="{RENK["yesil"]}" stroke-width="1.8"/>'
    s += f'<text x="386" y="90" font-size="13" font-weight="800" fill="{RENK["yesil"]}">Tabiat Bilimleri (Fizik, Astronomi, Biyoloji)</text>'
    s += f'<text x="386" y="116" font-size="11" fill="{RENK["lacivert"]}">• Evrendeki hassas ölçü ve düzeni ortaya koyar.</text>'
    s += f'<text x="386" y="138" font-size="11" fill="{RENK["lacivert"]}">• Kelamdaki "Hudûs" ve "Nizam/Gaye" delillerini besler.</text>'
    s += f'<text x="386" y="160" font-size="11" fill="{RENK["lacivert"]}">• Kevnî ayetlerin anlaşılmasını kolaylaştırır.</text>'

    s += f'<rect x="370" y="188" width="326" height="112" rx="10" fill="{RENK["acik_turuncu"]}" stroke="{RENK["turuncu"]}" stroke-width="1.8"/>'
    s += f'<text x="386" y="214" font-size="13" font-weight="800" fill="{RENK["turuncu"]}">Sosyal Bilimler (Psikoloji, Sosyoloji, Tarih)</text>'
    s += f'<text x="386" y="240" font-size="11" fill="{RENK["lacivert"]}">• İnanma fıtratını ve dinin toplumsal etkisini inceler.</text>'
    s += f'<text x="386" y="262" font-size="11" fill="{RENK["lacivert"]}">• İnanç krizleri ve çağdaş akımların analizine katkı sunar.</text>'
    s += f'<text x="386" y="284" font-size="11" fill="{RENK["lacivert"]}">• Yeni İlm-i Kelam döneminde önemi daha da artmıştır.</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """Kelam İlminin Yöntemleri ve Başlıca Klasik Eserleri"""
    W, H = 720, 330
    s = _baslik(W, H, "YÖNTEM & ESER", "Kelam İlminin Yöntemi ve Temel Klasik Eserleri", RENK["kirmizi"])
    yontemler = [
        ("Tümevarım", "Tekil olgulardan genel ilkeye ulaşma", RENK["mavi"]),
        ("Temsil (Kıyas)", "Görünenden (şâhid) görünmeyene (gâib) استدلال", RENK["yesil"]),
        ("Normatif Yaklaşım", "İnanç ilkelerini kesin ölçüt olarak koruma", RENK["mor"]),
    ]
    for i, (ad, acik, rk) in enumerate(yontemler):
        x = 24 + i * 228
        s += f'<rect x="{x}" y="62" width="216" height="62" rx="8" fill="#fff" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="{x+108}" y="86" text-anchor="middle" font-size="12.5" font-weight="800" fill="{rk}">{ad}</text>'
        s += f'<text x="{x+108}" y="108" text-anchor="middle" font-size="10.5" fill="{RENK["lacivert"]}">{acik}</text>'

    s += f'<rect x="24" y="138" width="672" height="174" rx="10" fill="#fff" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
    s += f'<text x="42" y="162" font-size="13" font-weight="800" fill="{RENK["kirmizi"]}">Kelam Tarihinin Başlıca Temel Eserleri</text>'
    eserler = [
        ("İmam-ı Âzam Ebu Hanife (ö. 767)", "el-Fıkhu'l-Ekber (İtikadi esasları derleyen ilk risalelerden)"),
        ("İmam Mâtürîdî (ö. 944)", "Kitâbü't-Tevhîd (Mâtürîdî kelamının kurucu şaheseri)"),
        ("Ebü'l-Hasan el-Eş'arî (ö. 936)", "el-İbâne an Usûli'd-Diyâne ve Makâlâtü'l-İslâmiyyîn"),
        ("Nûreddin es-Sâbûnî (ö. 1184)", "el-Bidâye fî Usûli'd-Dîn (Mâtürîdiyye Akâidi)"),
        ("Bekir Topaloğlu (1932–2016)", "Kelam İlmine Giriş (Çağdaş dönem temel başvuru eseri)"),
    ]
    for i, (muellif, eser) in enumerate(eserler):
        yy = 188 + i * 24
        s += f'<text x="42" y="{yy}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">• {muellif}:</text>'
        s += f'<text x="270" y="{yy}" font-size="11.5" fill="{RENK["gri"]}">{eser}</text>'
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

