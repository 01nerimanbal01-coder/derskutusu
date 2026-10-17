def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "MEKKE DÖNEMİNDE İSLAM'A DAVETİN İKİ AŞAMASI", 14, "#1e3a8a", "bold")
    ic += _kutu(28, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(183, 72, "1. Gizli (Bireysel) Davet (610-613 — 3 Yıl)", 11, "#1d4ed8", "bold")
    ic += _metin(183, 98, "• Müddessir suresi 1-5 ile başladı", 11, "#334155")
    ic += _metin(183, 120, "• İlk Müslümanlar: Hz. Hatice, Hz. Ali,", 11, "#334155")
    ic += _metin(183, 140, "  Hz. Zeyd b. Hârise, Hz. Ebû Bekir", 11, "#334155")
    ic += _metin(183, 166, "Merkez: Dârü'l-Erkam (Erkam'ın Evi)", 11, "#1e40af", "bold")

    ic += _kutu(362, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(517, 72, "2. Açık (Umumi) Davet (613-622 — 10 Yıl)", 11, "#1d4ed8", "bold")
    ic += _metin(517, 98, "• Şuarâ 214 (Yakın akrabaları uyar) ve", 11, "#334155")
    ic += _metin(517, 120, "  Hicr 94 (Emrolunduğun şeyi açıkça bildir!)", 11, "#334155")
    ic += _metin(517, 140, "• Safâ Tepesi konuşması ile tüm Mekke'ye", 11, "#334155")
    ic += _metin(517, 166, "  tevhit çağrısı ilan edildi.", 11, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "HÜZÜN YILI (SENETÜ'L-HÜZN) VE TAİF YOLCULUĞU (619-620)", 13, "#92400e", "bold")
    cols = [
        (25, "1. Boykot ve Hüzün Yılı", "3 yıllık boykotun ardından", "Ebû Tâlib ve Hz. Hatice'nin", "vefatı (Hüzün Yılı - 619)"),
        (248, "2. Taif'e Davet Yolculuğu", "Zeyd b. Hârise ile Taif'e gidiş;", "Taiflilerin taşlı saldırısına", "karşı sabır ve dua"),
        (471, "3. Rahmet Peygamberi", "'Belki Allah onların soyundan", "yalnız O'na ibadet eden bir", "nesil çıkarır!' duası ve Addâs")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+102, 72, b, 12, "#b45309", "bold")
        ic += _metin(x+102, 102, s1, 10, "#334155")
        ic += _metin(x+102, 124, s2, 10, "#334155")
        ic += _metin(x+102, 146, s3, 10, "#92400e", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "İLAHİ TESELLİ VE MUCİZE: İSRÂ VE MİRAÇ OLAYI (621)", 14, "#6b21a8", "bold")
    ic += _kutu(28, 48, 310, 138, "#ffffff", "#c084fc", 10, 1.8)
    ic += _metin(183, 72, "1. İsrâ (Gece Yürüyüşü)", 12, "#7e22ce", "bold")
    ic += _metin(183, 98, "Mekke'deki Mescid-i Haram'dan", 11, "#334155")
    ic += _metin(183, 120, "Kudüs'teki Mescid-i Aksâ'ya", 11, "#334155")
    ic += _metin(183, 142, "geceleyin götürülmesi", 11, "#334155")
    ic += _metin(183, 166, "(İsrâ Suresi, 17/1)", 11, "#581c87", "bold")

    ic += _kutu(362, 48, 310, 138, "#ffffff", "#c084fc", 10, 1.8)
    ic += _metin(517, 72, "2. Miraç (Göklere Yükseliş)", 12, "#7e22ce", "bold")
    ic += _metin(517, 98, "Mescid-i Aksâ'dan ilahi huzura yükseliş.", 11, "#334155")
    ic += _metin(517, 120, "Üç Büyük Hediye: • Beş Vakit Namaz", 11, "#1e293b", "bold")
    ic += _metin(517, 142, "• Bakara suresi son 2 ayeti (Âmener-resûlü)", 10, "#334155")
    ic += _metin(517, 164, "• Şirk koşmayanların bağışlanacağı müjdesi", 10, "#581c87", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "HİCRETE HAZIRLIK: AKABE BİATLARI (620-622)", 14, "#166534", "bold")
    ic += _kutu(30, 48, 640, 126, "#ffffff", "#22c55e", 10, 1.5)
    ic += _metin(350, 74, "Yesrib'den (Medine) Gelen Hacılarla Akabe Tepesi'nde Yapılan Sözleşmeler (Biatlar)", 12, "#15803d", "bold")
    ic += _metin(350, 100, "• I. Akabe Biatı (621 - 12 kişi): İman ve ahlak ilkelerine bağlılık sözü; Mus'ab b. Umeyr ilk öğretmen!", 11, "#334155")
    ic += _metin(350, 124, "• II. Akabe Biatı (622 - 75 kişi): Peygamberimizi ve muhacirleri kendi canları gibi koruma sözü.", 11, "#334155")
    ic += _metin(350, 150, "Sonuç: Medine İslam'a kucak açtı ve 622 yılında tarihi HİCRET gerçekleşti.", 11, "#166534", "bold")
    return _svg(700, 205, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
