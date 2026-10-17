# -*- coding: utf-8 -*-
"""12. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük - 3. Hafta Görselleri (I. Dünya Savaşı ve Osmanlı Cepheleri)"""


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
    """I. Dünya Savaşı'nın Genel ve Özel Nedenleri ile İki Blok"""
    g, y = 740, 265
    s = _baslik(g, "I. DÜNYA SAVAŞI (1914-1918): NEDENLERİ VE DEVLETLER ARASI BLOKLAŞMA", "#b91c1c")
    s += _kutu(20, 52, 340, 195, "#fef2f2", "#ef4444", "SAVAŞIN GENEL VE ÖZEL NEDENLERİ", [
        "• Genel: 1) Sanayi İnkılabı -> Hammadde ve pazar",
        "  rekabeti (Sömürgecilik), 2) Fransız İhtilali ->",
        "  Milliyetçilik akımı, 3) Silahlanma ve bloklaşma.",
        "• Özel: Alsace-Lorraine sorunu (Almanya-Fransa),",
        "  Panslavizm ve sıcak denizler rekabeti (Rusya-Avusturya).",
        "• Kıvılcım: 28 Haziran 1914 Saraybosna Suikastı."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 195, "#eff6ff", "#3b82f6", "SAVAŞ ÖNCESİ VE SIRASINDA İKİ BLOK", [
        "• İTTİFAK (BAĞDAŞMA) DEVLETLERİ:",
        "  Almanya, Avusturya-Macaristan, İtalya (1915'te karşıya",
        "  geçti) -> Sonradan katılanlar: OSMANLI ve BULGARİSTAN.",
        "• İTİLAF (ANLAŞMA) DEVLETLERİ:",
        "  İngiltere, Fransa, Çarlık Rusyası -> Sonradan:",
        "  İtalya (Londra Ant.), ABD, Japonya, Yunanistan, Sırbistan."
    ], "#1e3a8a")
    return _svg(g, y, s)


def gorsel_2():
    """Osmanlı Devleti'nin I. Dünya Savaşı'nda Savaştığı Cephelerin Sınıflandırılması"""
    g, y = 740, 265
    s = _baslik(g, "OSMANLI DEVLETİ'NİN I. DÜNYA SAVAŞI'NDA MÜCADELE ETTİĞİ CEPHELER", "#0f766e")
    s += _kutu(18, 52, 228, 195, "#fef2f2", "#ef4444", "1. TAARRUZ CEPHELERİ", [
        "(2K Şifresi: Kafkas - Kanal)",
        "• KAFKAS CEPHESİ",
        "  (Rusya'ya karşı açıldı)",
        "• KANAL (SÜVEYŞ) CEPHESİ",
        "  (İngiltere'ye karşı Mısır'ı",
        "  geri almak için açıldı)"
    ], "#991b1b")
    s += _kutu(256, 52, 228, 195, "#ecfdf5", "#10b981", "2. SAVUNMA CEPHELERİ", [
        "• ÇANAKKALE CEPHESİ (Zafer!)",
        "• IRAK (BASRA) CEPHESİ",
        "  (Kut'ül Amâre Zaferi - 1916)",
        "• HİCAZ - YEMEN CEPHESİ",
        "  (Fahreddin Paşa - Medine)",
        "• SURİYE - FİLİSTİN CEPHESİ"
    ], "#065f46")
    s += _kutu(494, 52, 228, 195, "#eff6ff", "#3b82f6", "3. YARDIM CEPHELERİ", [
        "(Sınırlarımız Dışında - 'YA' eki)",
        "• GALİÇYA CEPHESİ",
        "• ROMANYA CEPHESİ",
        "• MAKEDONYA CEPHESİ",
        "(Müttefiklerimize yardım",
        "amacıyla asker gönderildi)"
    ], "#1e3a8a")
    return _svg(g, y, s)


def gorsel_3():
    """Kafkas Cephesi, Sarıkamış, Tehcir Kanunu ve Brest-Litowsk"""
    g, y = 740, 255
    s = _baslik(g, "KAFKAS CEPHESİ VE ÇANAKKALE DESTANI", "#1d4ed8")
    s += _kutu(20, 52, 340, 185, "#eff6ff", "#3b82f6", "KAFKAS (DOĞU) CEPHESİ GELİŞMELERİ", [
        "• Amaç: Kars, Ardahan ve Batum'u (Elviye-i Selâse)",
        "  geri almak, Bakü petrollerine ve Turan'a ulaşmak.",
        "• Aralık 1914 Sarıkamış Harekâtı (Ağır kış şartları).",
        "• 27 Mayıs 1915: Sevk ve İskân (Tehcir) Kanunu.",
        "• 1916: Mustafa Kemal Paşa MUŞ ve BİTLİS'i kurtardı.",
        "• 3 Mart 1918 Brest-Litowsk: Elviye-i Selâse geri alındı!"
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 185, "#fefce8", "#eab308", "ÇANAKKALE CEPHESİ (1915) VE SONUÇLARI", [
        "• 18 Mart 1915 Deniz Zaferi (Nusret Mayın Gemisi,",
        "  Cevat Çobanlı Paşa, Seyit Onbaşı).",
        "• Kara Savaşları: Mustafa Kemal (19. Tümen Komutanı)",
        "  Arıburnu, Conkbayırı ve Anafartalar'da destan yazdı.",
        "• Sonuç: Savaş 2 yıl uzadı, Çarlık Rusyası yıkıldı,",
        "  Bulgaristan İttifak bloğuna katıldı!"
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_4():
    """Mustafa Kemal Paşa'nın I. Dünya Savaşı'nda Görev Yaptığı 3 Cephe (ÇKS)"""
    g, y = 740, 245
    s = _baslik(g, "MUSTAFA KEMAL PAŞA'NIN I. DÜNYA SAVAŞI'NDA GÖREV ALDIĞI 3 CEPHE", "#6d28d9")
    s += _kutu(18, 52, 228, 175, "#f5f3ff", "#8b5cf6", "1. ÇANAKKALE CEPHESİ (1915)", [
        "• Rütbe: Yarbay -> Albay",
        "• Görev: 19. Tümen ve",
        "  Anafartalar Grup Komutanı",
        "• Sözü: 'Ben size taarruzu değil,",
        "  ölmeyi emrediyorum!'",
        "• Millî Mücadele liderliği doğdu."
    ], "#5b21b6")
    s += _kutu(256, 52, 228, 175, "#fdf4ff", "#d946ef", "2. KAFKAS CEPHESİ (1916)", [
        "• Rütbe: Tuğgeneral (Paşa)",
        "• Görev: 16. Kolordu Komutanı",
        "• Başarısı: Ağustos 1916'da",
        "  MUŞ ve BİTLİS'i Rus",
        "  işgalinden kurtardı.",
        "• Altın Kılıç Madalyası aldı."
    ], "#86198f")
    s += _kutu(494, 52, 228, 175, "#ecfdf5", "#10b981", "3. SURİYE-FİLİSTİN (1917-18)", [
        "• Görev: 7. Ordu Komutanı ve",
        "  Yıldırım Orduları Grup Kom.",
        "• Başarısı: İngilizleri Halep'in",
        "  kuzeyinde (Katma'da) durdurarak",
        "  Anadolu'nun güney sınırını",
        "  korudu."
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
