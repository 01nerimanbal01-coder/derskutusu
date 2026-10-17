# -*- coding: utf-8 -*-
"""11. Sınıf Kur'an-ı Kerim - 3. Hafta Görselleri (Kur'an-ı Kerim'den Kavramlar: Adalet ve Cehalet)"""


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
    """Kur'an'da Adalet (Adl / Kıst) ve Zıddı Zulüm Kavramları"""
    g, y = 740, 260
    s = _baslik(g, "KUR'AN-I KERİM'DE ADALET (ADL / KIST) VE ZULÜM KARŞITLIĞI", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "ADALET (Adl ve Kıst)", [
        "• Sözlük: Doğruluk, eşitlik, denge ve her şeyi",
        "  yerli yerine koymak, hak sahibine hakkını vermek.",
        "• Allah'ın İsmi: EL-ADL (Mutlak adalet sahibi).",
        "• Yakın Kavram: KIST (Ölçü ve tartıda, paylaştırmada",
        "  tam hakkaniyet; 'Allah muksitleri sever' - Mâide, 42)."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#fef2f2", "#ef4444", "ADALETİN ZIDDI: ZULÜM (Cevr / Bağy)", [
        "• Sözlük: Bir şeyi kendisine ait olmayan yere koymak,",
        "  haddi aşmak, haksızlık etmek ve karanlık.",
        "• En büyük zulüm ŞİRKTİR ('Şüphesiz şirk çok büyük",
        "  bir zulümdür' - Lokmân, 13).",
        "• Kul hakkı yemek ve ayrımcılık yapmak zulümdür."
    ], "#991b1b")
    return _svg(g, y, s)


def gorsel_2():
    """Adaletin Kur'an'daki Boyutları ve Temel Ayetler"""
    g, y = 740, 260
    s = _baslik(g, "KUR'AN'DA ADALET EMİRLERİ VE UYGULAMA ALANLARI", "#1d4ed8")
    s += _kutu(18, 52, 228, 190, "#eff6ff", "#3b82f6", "HÜKÜM VE ŞAHİTLİKTE", [
        "• 'İnsanlar arasında hükmettiğiniz",
        "  zaman adaletle hükmedin!'",
        "  (Nisâ, 58)",
        "• 'Kendinizin, anne-babanızın",
        "  aleyhine bile olsa adaleti",
        "  ayakta tutan şahitler olun!'",
        "  (Nisâ, 135)"
    ], "#1e3a8a")
    s += _kutu(256, 52, 228, 190, "#fefce8", "#eab308", "DÜŞMANA KARŞI BİLE", [
        "• 'Bir topluluğa olan kininiz",
        "  (öfkeniz), sakın sizi",
        "  adaletsizliğe sevk etmesin!",
        "  Adil olun; bu takvaya",
        "  daha yakındır.'",
        "  (Mâide, 8)"
    ], "#854d0e")
    s += _kutu(494, 52, 228, 190, "#f0fdf4", "#10b981", "SÖZDE VE ÖLÇÜ-TARTIDA", [
        "• 'Söylediğiniz zaman yakınınız",
        "  bile olsa adil konuşun!'",
        "  (En'âm, 152)",
        "• 'Şüphesiz Allah adaleti,",
        "  ihsanı ve akrabaya yardımı",
        "  emreder.' (Nahl, 90)"
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_3():
    """Kur'an'da Cehalet (Cehl) ve Cahiliye Kavramlarının Analizi"""
    g, y = 740, 260
    s = _baslik(g, "KUR'AN'DA CEHALET (CEHL) KAVRAMI: İLİM VE HİLM KARŞITLIĞI", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "CEHALETİN İKİ TEMEL BOYUTU", [
        "1. İLMİN (BİLGİNİN) ZIDDI OLARAK CEHL:",
        "   Vahiy bilgisinden, hakikatten ve tevhitten habersiz",
        "   olmak; zan ve körü körüne taklide uymak.",
        "2. HİLMİN (OLGUNLUK VE SAĞDUYUNUN) ZIDDI OLARAK CEHL:",
        "   Öfkesine yenilmek, zorbalık, kibir, taşkınlık ve",
        "   nefsin arzularına (hevâya) kapılıp haddi aşmak."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "CAHİLİYE ZİHNİYETİNİN 4 ÖZELLİĞİ", [
        "1. Zanü'l-Câhiliyye: Allah hakkında batıl zan (Âl-i İmrân, 154)",
        "2. Hükmu'l-Câhiliyye: Hevâya ve güce dayalı adaletsiz",
        "   hüküm (Mâide, 50)",
        "3. Teberrücü'l-Câhiliyye: Gösteriş ve iffetsizlik (Ahzâb, 33)",
        "4. Hamiyyetü'l-Câhiliyye: Kabilecilik, ırkçılık ve",
        "   baskıcı kibir / fanatizm (Fetih, 26)"
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Adalet ve Cehalet Karşılaştırması ve Rahmân'ın Kullarının Tutumu"""
    g, y = 740, 245
    s = _baslik(g, "ADALET - CEHALET KARŞILAŞTIRMASI VE MÜMİNİN TUTUMU", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "Cehaletin Toplumsal Sonucu: Zulüm ve Fesat", [
        "• Cehalet yalnızca okuma-yazma bilmemek değil;",
        "  hakikate karşı kibirlenmek ve öfkeyle hareket etmektir.",
        "• Cehaletin egemen olduğu yerde güçlü zayıfı ezer,",
        "  adalet yok olur ve yeryüzünde bozgunculuk (fesat) yayılır.",
        "• Hz. Yusuf: 'Cahillerden olmaktan Allah'a sığınırım' (Bakara, 67)."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#ecfdf5", "#10b981", "Rahmân'ın Kullarının (İbâdü'r-Rahmân) Duruşu", [
        "• 'Rahmân'ın has kulları yeryüzünde tevazu ve vakarla",
        "  yürürler; CAHİLLER kendilerine (sataşıp) laf attıkları",
        "  zaman, (tartışmaya girmeden) SELAM der geçerler.'",
        "  (Furkân Suresi, 63. ayet).",
        "• Mümin cehalete cehaletle değil, hilm ve adaletle karşılık verir."
    ], "#065f46")
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
