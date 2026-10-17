# -*- coding: utf-8 -*-
"""12. Sınıf Coğrafya - 3. Hafta Görselleri (Beşerî Sistemler: Türkiye'de Kentleşme, Göç ve Arazi Kullanımı)"""


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
    """Fonksiyonel Arazi Kullanımı ve Sürdürülebilir Planlama"""
    g, y = 740, 260
    s = _baslik(g, "FONKSİYONEL ARAZİ KULLANIMI VE MEKÂNSAL PLANLAMA İLKELERİ", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "DOĞRU (PLANLI) ARAZİ KULLANIMI", [
        "• Verimli alüvyal ovalar (I. ve II. sınıf topraklar)",
        "  yalnızca TARIM faaliyetlerine ayrılır.",
        "• Sanayi tesisleri ve konutlar tarıma elverişsiz,",
        "  deprem riski düşük sağlam zeminlere kurulur.",
        "• Sanayi bölgesi, hâkim rüzgâr yönünün tersine",
        "  ve yerleşim alanlarının dışına konumlandırılır."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#fef2f2", "#ef4444", "YANLIŞ ARAZİ KULLANIMI ÖRNEKLERİ VE SONUÇLARI", [
        "• Çukurova, Bursa, Adapazarı, Gediz ve Ergene",
        "  ovalarının sanayi ve konutlarla işgal edilmesi.",
        "• Dere yataklarının doldurulup yerleşime açılması",
        "  (Sel ve taşkın felaketlerine davetiye çıkarır).",
        "• Orman ve meraların tahrip edilerek erozyonun",
        "  ve kentsel ısı adası etkisinin artırılması."
    ], "#991b1b")
    return _svg(g, y, s)


def gorsel_2():
    """Türkiye'de Kentleşme Süreci, Göç ve Kentsel Sorunlar"""
    g, y = 740, 260
    s = _baslik(g, "TÜRKİYE'DE KENTLEŞME SÜRECİ (1950 SONRASI) VE KENTSEL SORUNLAR", "#1d4ed8")
    s += _kutu(20, 52, 340, 190, "#eff6ff", "#3b82f6", "TÜRKİYE'DE KENTLEŞMENİN TARİHSEL EVRELERİ", [
        "• 1927-1950 Dönemi: Kent nüfusu oranı %24-25",
        "  düzeyinde sabit kaldı (Kırsal nüfus ağırlıklı).",
        "• 1950-1985 Dönemi: Tarımda makineleşme ve",
        "  sanayileşme ile KIRDAN KENTE GÖÇ patlaması yaşandı.",
        "• 1985'te ilk kez kent nüfusu kır nüfusunu geçti!",
        "• Günümüzde nüfusun %93'ten fazlası il/ilçe merkezlerindedir."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 190, "#fff7ed", "#f97316", "AŞIRI VE PLANSIZ KENTLEŞMENİN SORUNLARI", [
        "1. Gecekondulaşma (çarpık kentleşme) ve altyapı yetersizliği,",
        "2. Sanayi tesislerinin şehir içinde kalması,",
        "3. Trafik yoğunluğu, hava, su, ses ve ışık kirliliği,",
        "4. Tarım ve orman alanlarının daralması,",
        "5. Kentsel dönüşüm ve uydu kent (toplu konut) projeleri",
        "   bu sorunları çözmek amacıyla geliştirilmiştir."
    ], "#9a3412")
    return _svg(g, y, s)


def gorsel_3():
    """Geçmişten Geleceğe Şehir Fonksiyonları ve Akıllı Şehirler (Smart Cities)"""
    g, y = 740, 255
    s = _baslik(g, "GELECEĞİN ŞEHİRLERİ: AKILLI ŞEHİR (SMART CITY) VE SAKİN ŞEHİR (CITTASLOW)", "#6d28d9")
    s += _kutu(20, 52, 340, 185, "#f5f3ff", "#8b5cf6", "AKILLI ŞEHİRLER (SMART CITIES) VE DİKEY TARIM", [
        "• Bilgi ve iletişim teknolojileri (IoT, yapay zekâ, büyük",
        "  veri) ile enerji, ulaşım, su ve atık yönetimini",
        "  optimize eden sıfır karbon hedefli şehirlerdir.",
        "• Örnekler: Singapur, Tokyo, Kopenhag, Amsterdam.",
        "• Dikey Tarım (Vertical Farming): Gökdelenlerin içinde",
        "  topraksız (hidroponik) yöntemle gıda üretimi."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 185, "#f0fdf4", "#16a34a", "SAKİN ŞEHİR (CITTASLOW) HAREKETİ", [
        "• 1999'da İtalya'da doğan; hızlı tüketim ve küreselleşmeye",
        "  karşı yerel kimliği, geleneksel mimariyi, organik tarımı",
        "  ve yaşam kalitesini koruyan şehirler ağıdır (Nüfus &lt; 50.000).",
        "• Türkiye'nin İlk Sakin Şehri: SEFERİHİSAR (İzmir - 2009).",
        "• Diğer Örnekler: Akyaka, Gökçeada, Vize, Perşembe,",
        "  Halfeti, Şavşat, Eğirdir, Uzundere, Ahlat, Foça, Safranbolu."
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_4():
    """Geleceğin Ekonomisi, Nüfus ve Yerleşme Eğilimleri"""
    g, y = 740, 245
    s = _baslik(g, "GELECEKTE NÜFUS, YERLEŞME VE EKONOMİK TRENDLER", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "GELECEĞİN YERLEŞME MODELLERİ", [
        "• Mega Kentler (Nüfusu 10 milyonu aşan şehirler) artmaktadır.",
        "• Deniz seviyesinin yükselmesi ve arazi darlığı nedeniyle",
        "  YÜZEN ŞEHİRLER (Floating Cities), su altı ve uzay",
        "  kolonisi projeleri geliştirilmektedir.",
        "• Ekokentler (Yeşil Çatılar, Yenilenebilir Enerji)."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#eff6ff", "#3b82f6", "ENDÜSTRİ 4.0 VE DİJİTAL EKONOMİ", [
        "• Robotik otomasyon, 3B yazıcılar, bulut bilişim ve",
        "  nesnelerin interneti (IoT) üretim süreçlerini dönüştürür.",
        "• E-ticaret ve uzaktan çalışma (home-office), iş gücü",
        "  coğrafyasını ve ulaşım talebini yeniden şekillendirir.",
        "• Yeşil ekonomi ve döngüsel ekonomi ön plana çıkar."
    ], "#1e3a8a")
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