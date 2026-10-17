# -*- coding: utf-8 -*-
"""11. Sınıf Dinler Tarihi - 3. Hafta Görselleri (Dinler Tarihinin Tanımı, Konusu, Kaynakları ve Metodu)"""


def _svg(g, y, icerik):
    return (
        f'<svg viewBox="0 0 {g} {y}" width="100%" xmlns="http://www.w3.org/2000/svg" '
        f'style="max-width:{g}px;display:block;margin:14px auto;background:#fff;'
        f'border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _baslik(g, metin, renk="#1e293b"):
    return (
        f'<rect x="0" y="0" width="{g}" height="38" rx="10" fill="{renk}"/>'
        f'<rect x="0" y="20" width="{g}" height="18" fill="{renk}"/>'
        f'<text x="{g//2}" y="25" font-family="Arial,sans-serif" font-size="14" '
        f'font-weight="bold" fill="#ffffff" text-anchor="middle">{metin}</text>'
    )


def _kutu(x, y, g, yk, r_ark, r_ken, baslik, satirlar, r_bas="#0f172a"):
    ic = f'<rect x="{x}" y="{y}" width="{g}" height="{yk}" rx="8" fill="{r_ark}" stroke="{r_ken}" stroke-width="1.8"/>'
    ic += f'<text x="{x+g//2}" y="{y+22}" font-family="Arial,sans-serif" font-size="12.5" font-weight="bold" fill="{r_bas}" text-anchor="middle">{baslik}</text>'
    ic += f'<line x1="{x+10}" y1="{y+30}" x2="{x+g-10}" y2="{y+30}" stroke="{r_ken}" stroke-width="1"/>'
    for i, s in enumerate(satirlar):
        ic += f'<text x="{x+g//2}" y="{y+48+i*18}" font-family="Arial,sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s}</text>'
    return ic


def gorsel_1():
    """Dinler Tarihinin Tanımı, Konusu ve Kapsamı"""
    g, y = 740, 260
    s = _baslik(g, "DİNLER TARİHİ BİLİMİNİN TANIMI, KONUSU VE KAPSAMI", "#1d4ed8")
    s += _kutu(20, 52, 340, 190, "#eff6ff", "#3b82f6", "TANIMI VE KONUSU", [
        "• Konusu: Tarih sahnesinde ortaya çıkmış olan",
        "  TÜM DİNLERDİR (Yaşayan ve ölü/tarihî dinler).",
        "• Dinlerin doğuşunu, kurucularını, kutsal metinlerini,",
        "  inanç, ibadet, ahlak ve sembol sistemlerini",
        "  TARİHÎ, KARŞILAŞTIRMALI ve BETİMLEYİCİ",
        "  yöntemlerle inceleyen bilim dalıdır."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 190, "#f0fdf4", "#16a34a", "DİNLERİN İKİ ANA GRUBU (İnceleme Alanı)", [
        "1. YAŞAYAN DİNLER: Günümüzde mensubu bulunan",
        "   dinler (İslam, Hristiyanlık, Yahudilik, Hinduizm,",
        "   Budizm, Sihizm, Taoizm, Şintoizm vb.).",
        "2. ÖLÜ (TARİHÎ) DİNLER: Günümüzde inananı",
        "   kalmamış dinler (Eski Mısır, Mezopotamya,",
        "   Antik Yunan, Roma ve İskandinav dinleri)."
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_2():
    """Dinler Tarihinin Araştırma Metodu (Betimleyici/Deskriptif, Tarihî, Karşılaştırmalı, Fenomenolojik)"""
    g, y = 740, 265
    s = _baslik(g, "DİNLER TARİHİNİN TEMEL ARAŞTIRMA METODU VE İLKELERİ", "#0f766e")
    s += _kutu(16, 52, 168, 195, "#ecfdf5", "#10b981", "1. BETİMLEYİCİ", [
        "(Deskriptif / Tasvirî)",
        "• Normatif (kural koyucu)",
        "  veya yargılayıcı DEĞİLDİR.",
        "• Dinleri 'olması gerektiği'",
        "  gibi değil, 'OLDUĞU GİBİ'",
        "  tarafsızca tasvir eder."
    ], "#065f46")
    s += _kutu(196, 52, 168, 195, "#eff6ff", "#3b82f6", "2. TARİHÎ METOT", [
        "(Kronolojik İnceleme)",
        "• Bir dinin doğuşunu,",
        "  geçirdiği evreleri,",
        "  mezhepleşme sürecini",
        "  tarihsel bağlam ve",
        "  belgelerle inceler."
    ], "#1e40af")
    s += _kutu(376, 52, 168, 195, "#fefce8", "#eab308", "3. MUKAYESELİ", [
        "(Karşılaştırmalı Metot)",
        "• Farklı dinlerdeki",
        "  benzerlik ve farklılıkları",
        "  üstünlük yarışına",
        "  girmeden objektif",
        "  olarak karşılaştırır."
    ], "#854d0e")
    s += _kutu(556, 52, 168, 195, "#f5f3ff", "#8b5cf6", "4. FENOMENOLOJİK", [
        "(Görüngübilimsel)",
        "• Dua, kurban, oruç,",
        "  hac, kutsal mekân gibi",
        "  ortak dini olguların",
        "  özünü ve anlamını",
        "  empatiyle kavrar."
    ], "#5b21b6")
    return _svg(g, y, s)


def gorsel_3():
    """Dinler Tarihinin Kaynakları (Birincil ve İkincil Kaynaklar)"""
    g, y = 740, 250
    s = _baslik(g, "DİNLER TARİHİNİN TEMEL KAYNAKLARI", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "1. BİRİNCİL (ASLÎ) KAYNAKLAR", [
        "• Kutsal Metinler: Kur'an-ı Kerim, Tanah (Tevrat),",
        "  İnciller, Vedalar, Tripitaka, Avesta vb.",
        "• Arkeolojik Bulgular: Tapınaklar, kitabeler,",
        "  tabletler, heykeller ve dini semboller.",
        "• Yaşayan Gelenek: İbadet ve ayin gözlemleri."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#fff7ed", "#f97316", "2. İKİNCİL (YARDIMCI) KAYNAKLAR", [
        "• Din dışından gözlemcilerin, seyyahların ve",
        "  tarihçilerin kaleme aldığı eserler (Herodot,",
        "  Mes'ûdî, Bîrûnî, Şehristânî vb.).",
        "• Filoloji (Dilbilim), Arkeoloji, Antropoloji,",
        "  Din Sosyolojisi ve Din Psikolojisi verileri."
    ], "#9a3412")
    return _svg(g, y, s)


def gorsel_4():
    """İslam Dünyasında ve Batı'da Dinler Tarihinin Öncüleri"""
    g, y = 740, 255
    s = _baslik(g, "İSLAM DÜNYASINDA VE BATI'DA DİNLER TARİHİNİN ÖNCÜLERİ", "#6d28d9")
    s += _kutu(20, 52, 340, 185, "#f5f3ff", "#8b5cf6", "İSLAM DÜNYASINDA ÖNCÜ ÂLİMLER (Milel ve Nihal)", [
        "• EBU REYHAN EL-BÎRÛNÎ (ö. 1061): Sanskritçeyi öğrenip",
        "  Hindistan'da yerinde gözlem yaparak yazdığı",
        "  'Tahkîku mâ li'l-Hind' ile dünyanın ilk tarafsız",
        "  dinler tarihçisi kabul edilir.",
        "• ŞEHRİSTÂNÎ (ö. 1153): 'el-Milel ve'n-Nihal'",
        "• İBN HAZM (ö. 1064): 'el-Fasl fi'l-Milel ve'l-Ehvâi ve'n-Nihal'"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 185, "#fdf4ff", "#d946ef", "BATI'DA VE OSMANLI/TÜRKİYE'DE GELİŞİMİ", [
        "• F. MAX MÜLLER (1823-1900): 19. yüzyılda Batı'da",
        "  Karşılaştırmalı Dinler Tarihi'nin (Religionswissenschaft)",
        "  akademik kurucusu ('Bir dini bilen, hiçbirini bilmez').",
        "• MIRCEA ELIADE (1907-1986): Kutsal ve Profan kuramı.",
        "• OSMANLI'DA: Ahmed Midhat Efendi ('Târîh-i Edyân',",
        "  1911) ve Mahmud Esad Efendi ile Darülfünun'da başladı."
    ], "#86198f")
    return _svg(g, y, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for k, sv in GORSELLER.items():
        idx = int(k[1:]) - 1
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = sv
    return v
