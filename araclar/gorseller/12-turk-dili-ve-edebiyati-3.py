def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 210, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "1923-1960 CUMHURİYET DÖNEMİ HİKÂYE ANLAYIŞLARI", 14, "#92400e", "bold")
    cols = [
        (25, "#fef2f2", "#ef4444", "#991b1b", "Millî-Dinî Duyarlılık", "Anadolu, Kurtuluş Savaşı", "Doğu-Batı çatışması, halk", "Yakup Kadri, Reşat Nuri,", "Refik Halit, Aka Gündüz"),
        (248, "#eff6ff", "#3b82f6", "#1e40af", "Toplumcu Gerçekçilik", "Köylü-işçi, ağa-köylü", "Göç, geçim sıkıntısı, tezli", "Sabahattin Ali, Sadri Ertem,", "Orhan Kemal, Kemal Tahir"),
        (471, "#f0fdf4", "#22c55e", "#166534", "Bireyin İç Dünyası", "Psikoloji, yalnızlık, bunalım", "İç konuşma, bilinç akışı", "Peyami Safa, A. H. Tanpınar,", "Tarık Buğra, Samiha Ayverdi")
    ]
    for x, bg, st, tc, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 156, bg, st, 10, 1.8)
        ic += _metin(x+102, 72, b, 12, tc, "bold")
        ic += _metin(x+102, 100, s1, 11, "#334155")
        ic += _metin(x+102, 122, s2, 11, "#334155")
        ic += _kutu(x+12, 138, 180, 52, "#ffffff", st, 6, 1)
        ic += _metin(x+102, 158, s3, 10, tc, "bold")
        ic += _metin(x+102, 176, s4, 10, "#475569")
    return _svg(700, 230, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#f8fafc", "#64748b", 12, 2)
    ic += _metin(350, 34, "OLAY HİKÂYESİ (MAUPASSANT) VE DURUM HİKÂYESİ (ÇEHOV) KARŞILAŞTIRMASI", 13, "#1e293b", "bold")
    ic += _kutu(28, 48, 310, 142, "#eff6ff", "#2563eb", 10, 1.8)
    ic += _metin(183, 70, "Olay Hikâyesi (Klasik Vaka)", 12, "#1d4ed8", "bold")
    ic += _metin(183, 94, "• Serim - Düğüm - Çözüm planına sıkı bağlıdır", 11, "#334155")
    ic += _metin(183, 116, "• Merak ve heyecan unsuru ön plandadır", 11, "#334155")
    ic += _metin(183, 138, "• Beklenmedik çarpıcı bir sonla biter", 11, "#334155")
    ic += _metin(183, 164, "Temsilciler: Ömer Seyfettin, Refik Halit, Sabahattin Ali", 10, "#1e40af", "bold")

    ic += _kutu(362, 48, 310, 142, "#fdf4ff", "#a855f7", 10, 1.8)
    ic += _metin(517, 70, "Durum (Kesit) Hikâyesi", 12, "#7e22ce", "bold")
    ic += _metin(517, 94, "• Hayatın sıradan bir kesiti ve atmosfer anlatılır", 11, "#334155")
    ic += _metin(517, 116, "• Merak unsuru geri planda; duygu ve izlenim öndedir", 11, "#334155")
    ic += _metin(517, 138, "• Bitmemişlik hissi verir; yorumu okura bırakır", 11, "#334155")
    ic += _metin(517, 164, "Temsilciler: Memduh Şevket Esendal, Sait Faik Abasıyanık", 10, "#6b21a8", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "HİKÂYEDE MODERN ANLATIM TEKNİKLERİ", 14, "#166534", "bold")
    items = [
        (25, "İç Konuşma", "Kahramanın kendi", "kendisiyle konuşur gibi", "mantıklı iç diyaloğu"),
        (192, "Bilinç Akışı", "Düşüncelerin mantık", "sırası olmadan, çağrışımlarla", "kesik akması"),
        (359, "İç Çözümleme", "Anlatıcının kahramanın", "psikolojisini dışarıdan", "açıklaması"),
        (526, "Geriye Dönüş", "Zaman akışını kırıp", "geçmişteki olayları", "hatırlama (Flashback)")
    ]
    for x, b, s1, s2, s3 in items:
        ic += _kutu(x, 48, 150, 135, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#15803d", "bold")
        ic += _metin(x+75, 102, s1, 11, "#334155")
        ic += _metin(x+75, 124, s2, 11, "#334155")
        ic += _metin(x+75, 146, s3, 11, "#166534", "bold")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "CÜMLENİN ÖGELERİ: TEMEL VE YARDIMCI ÖGELER (YÖNTEM: YÖN)", 13, "#1e3a8a", "bold")
    ic += _kutu(25, 48, 200, 138, "#dbeafe", "#1d4ed8", 9, 1.8)
    ic += _metin(125, 72, "1. TEMEL ÖGELER", 12, "#1e40af", "bold")
    ic += _metin(125, 98, "Yüklem: Yargıyı bildirir", 11, "#1e293b", "bold")
    ic += _metin(125, 122, "Özne: Yükleme sorulan", 11, "#334155")
    ic += _metin(125, 142, "'Kim? / Ne?' sorusu", 11, "#1d4ed8", "bold")
    ic += _metin(125, 166, "(Gerçek, Gizli, Sözde)", 10, "#475569")

    ic += _kutu(245, 48, 430, 138, "#ffffff", "#3b82f6", 9, 1.8)
    ic += _metin(460, 70, "2. YARDIMCI ÖGELER", 12, "#1e40af", "bold")
    ic += _metin(460, 94, "• Belirtili Nesne: Neyi, Kimi? | Belirtisiz Nesne: Ne? (Özneden sonra)", 11, "#334155")
    ic += _metin(460, 118, "• Yer Tamlayıcısı (Dolaylı Tümleç): Kime, Kimde, Kimden / Nereye, Nerede, Nereden?", 11, "#334155")
    ic += _metin(460, 142, "• Zarf Tümleci: Nasıl, Ne zaman, Niçin, Ne kadar, Kim ile, Ne ile?", 11, "#334155")
    ic += _metin(460, 166, "Altın Kural: Önce Yüklem -> Sonra Özne -> Sonra Nesne ve Tümleçler (Y-Ö-N)", 11, "#b91c1c", "bold")
    return _svg(700, 215, ic)

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
