# -*- coding: utf-8 -*-
"""11. Sınıf Peygamberimizin Hayatı - 3. Hafta Görselleri (Hicret Öncesi Yesrib ve Hicaz Şehirleri)"""


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
    """Hicaz Bölgesinin Üç Önemli Şehrinin Mukayesesi: Mekke, Yesrib (Medine) ve Tâif"""
    g, y = 740, 265
    s = _baslik(g, "İSLAM ÖNCESİ HİCAZ'IN ÜÇ ÖNEMLİ ŞEHRİ: MEKKE, YESRİB VE TÂİF", "#0f766e")
    s += _kutu(18, 52, 228, 195, "#fef2f2", "#ef4444", "1. MEKKE (Ümmü'l-Kurâ)", [
        "• Coğrafya: Kurak vadi, tarıma",
        "  elverişsizdir.",
        "• Ekonomi: Kervan TİCARETİ",
        "  ve hac panayırları.",
        "• Nüfus: Tek hâkim kabile",
        "  KUREYŞ (homojen yapı).",
        "• İnanç: Kâbe merkezli putperestlik."
    ], "#991b1b")
    s += _kutu(256, 52, 228, 195, "#ecfdf5", "#10b981", "2. YESRİB (Medine)", [
        "• Coğrafya: Su kaynakları bol,",
        "  volkanik (Harre) verimli vaha.",
        "• Ekonomi: Hurma ve tahıl",
        "  TARIMI, zanaat ve çarşılar.",
        "• Nüfus: EVS ve HAZREC (Arap) +",
        "  3 YAHUDİ kabilesi (Kozmopolit).",
        "• İnanç: Putperestlik + Yahudilik."
    ], "#065f46")
    s += _kutu(494, 52, 228, 195, "#eff6ff", "#3b82f6", "3. TÂİF", [
        "• Coğrafya: Yüksek, serin,",
        "  yağışlı ve bağlık-bahçelik.",
        "• Ekonomi: Üzüm bağları, meyve",
        "  tarımı ve dericilik.",
        "• Nüfus: SAKÎF kabilesi.",
        "• İnanç: 'Lât' putunun merkezi;",
        "  Mekke elitleriyle sıkı bağ."
    ], "#1e40af")
    return _svg(g, y, s)


def gorsel_2():
    """Hicret Öncesi Yesrib'in Demografik ve Sosyal Yapısı (Evs, Hazrec ve Yahudi Kabileleri)"""
    g, y = 740, 260
    s = _baslik(g, "HİCRET ÖNCESİ YESRİB'İN DEMOGRAFİK VE SOSYAL YAPISI", "#1d4ed8")
    s += _kutu(20, 52, 340, 190, "#eff6ff", "#3b82f6", "MÜŞRİK ARAP KABİLELERİ (Benu Kayle)", [
        "• Yemen'deki Arim Seli'nden sonra Yesrib'e göç eden",
        "  Ezd kolundan iki kardeş kabile: EVS ve HAZREC.",
        "• Menât putuna tapıyorlardı.",
        "• Aralarında 120 yıl süren kanlı kabile savaşları yaşandı.",
        "• Son savaş olan BUÂS SAVAŞI (617) her iki kabileyi de",
        "  tüketmiş ve barış sağlayacak bir lider arayışı doğurmuştu."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 190, "#fefce8", "#eab308", "YAHUDİ KABİLELERİ (Ehl-i Kitap)", [
        "1. BENÎ KAYNUKA: Çarşı ticaretine ve kuyumculuğa hâkimdi.",
        "2. BENÎ NADÎR: Verimli hurma bahçelerine ve tarıma sahipti.",
        "3. BENÎ KUREYZA: Tarım ve kaleleriyle (utum) güçlüydü.",
        "• Evs ve Hazrec'i birbirine düşürerek ekonomik üstünlük",
        "  kurmuşlar; ancak Araplara sürekli 'Ahir zaman peygamberi",
        "  gelecek!' diyerek onları vahiy ve nübüvvet fikrine hazırlamışlardı."
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_3():
    """Yesrib'i İslam'a ve Hicrete Hazırlayan Stratejik Sebepler"""
    g, y = 740, 255
    s = _baslik(g, "YESRİB'İ İSLAM DAVETİNE VE HİCRETE HAZIRLAYAN 4 TEMEL ETKEN", "#6d28d9")
    s += _kutu(20, 52, 340, 185, "#f5f3ff", "#8b5cf6", "SİYASİ VE SOSYAL ETKENLER", [
        "1. BUÂS SAVAŞI YORGUNLUĞU: Evs ve Hazrec liderlerinin",
        "   çoğu ölmüş; iki kabileyi birleştirecek adil ve",
        "   tarafsız bir hakem/lider ihtiyacı zirveye çıkmıştı.",
        "2. MEKKE GİBİ EKONOMİK ÇIKAR ENGELİ OLMAMASI:",
        "   Mekke'de Kureyş Kâbe putlarından gelir sağlıyordu;",
        "   Yesrib ekonomisi ise tarıma dayalıydı."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 185, "#fdf4ff", "#d946ef", "DİNİ, KÜLTÜREL VE AKRABALIK ETKENLERİ", [
        "3. İLAHİ KİTAP VE PEYGAMBER AŞİNALIĞI: Yesribli",
        "   Araplar, komşuları olan Yahudilerden tevhid, vahiy,",
        "   ahiret ve beklenen son peygamber kavramlarını duymuştu.",
        "4. HZ. PEYGAMBER'İN YESRİB İLE AKRABALIK BAĞI:",
        "   Dedesi Abdülmuttalib'in annesi Selma bint Amr",
        "   Hazrec kabilesinin Neccâroğulları kolundandı (Dayıları)."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Birinci ve İkinci Akabe Biatları ve Mus'ab b. Umeyr'in Rolü"""
    g, y = 740, 245
    s = _baslik(g, "YESRİB'İN MEDİNE'YE DÖNÜŞÜMÜ: AKABE GÖRÜŞMELERİ (620-622)", "#15803d")
    s += _kutu(20, 52, 340, 175, "#f0fdf4", "#22c55e", "AKABE GÖRÜŞMELERİ VE İLK ÖĞRETMEN", [
        "• 620 (Akabe): 6 Hazrecli hacı Müslüman oldu.",
        "• 621 (I. Akabe Biatı): 12 kişi İslam ahlakı üzere söz verdi.",
        "• İslam'ın İlk Öğretmeni: MUS'AB B. UMEYR (r.a.) Yesrib'e",
        "  gönderildi; Es'ad b. Zürâre'nin evinde (Dârü'l-Kurrâ)",
        "  1 yılda neredeyse her eve İslam'ın girmesini sağladı."
    ], "#166534")
    s += _kutu(380, 52, 340, 175, "#ecfeff", "#06b6d4", "II. AKABE BİATI (622) VE MEDİNETÜ'N-NEBÎ", [
        "• 622 (II. Akabe Biatı): 73 erkek ve 2 kadın sahabi,",
        "  Hz. Peygamber'i (s.a.v.) canları ve malları pahasına",
        "  koruyacaklarına söz vererek Yesrib'e davet ettiler.",
        "• Hicretle birlikte 'Yesrib' adı bırakılarak şehre",
        "  'Medînetü'n-Nebî (Peygamber Şehri) / el-Medînetü'l-Münevvere' dendi."
    ], "#0e7490")
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