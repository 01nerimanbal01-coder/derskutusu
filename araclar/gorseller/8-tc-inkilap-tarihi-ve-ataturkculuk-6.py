def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'


def _kart(x, y, w, h, baslik, satirlar, bg, border, text_c):
    rx = 12
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}" stroke="{border}" stroke-width="2"/>'
    s += f'<text x="{x + w/2}" y="{y + 26}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{text_c}" text-anchor="middle">{baslik}</text>'
    s += f'<line x1="{x+12}" y1="{y+36}" x2="{x+w-12}" y2="{y+36}" stroke="{border}" stroke-width="1" stroke-dasharray="3,3"/>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x + w/2}" y="{y + 58 + i*22}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="middle">{st}</text>'
    return s


def gorsel_1():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">OSMANLI DEVLETİ’NİN I. DÜNYA SAVAŞI’NA GİRİŞ SÜRECİ</text>'
    ic += _kart(30, 56, 195, 160, "Savaş Başında Tutum", ["Tarafsızlığını ilan etti", "Boğazları ulaşıma kapattı", "Kapitülasyonları kaldırdı", "Genel seferberlik başlattı"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Osmanlı’nın Amaçları", ["Kaybedilen yerleri geri almak", "Siyasi yalnızlıktan kurtulmak", "Kapitülasyon ve dış borçtan", "tamamen kurtulmak"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Almanya’nın Amaçları", ["Yeni cepheler açıp yükü azaltmak", "Jeopolitik konumdan yararlanmak", "Halifelik nüfuzunu kullanmak", "İngiliz sömürge yolunu kesmek"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">OSMANLI DEVLETİ’NİN SAVAŞTIĞI CEPHLER TABLOSU</text>'
    ic += _kart(30, 56, 195, 160, "1. Taarruz Cepheleri", ["(2K Şifresi)", "• Kafkas Cephesi", "• Kanal Cephesi", "Bizim açtığımız cepheler"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "2. Savunma Cepheleri", ["• Çanakkale Cephesi (Zafer!)", "• Irak Cephesi (Kut’ül Amare)", "• Hicaz - Yemen Cephesi", "• Suriye - Filistin Cephesi"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "3. Yardım Cepheleri", ["(Sınır Dışı - ‘ya’ ile biter)", "• Galiçya Cephesi", "• Makedonya Cephesi", "• Romanya Cephesi"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KAFKAS VE ÇANAKKALE CEPHELERİNİN ÖNEMİ</text>'
    ic += _kart(30, 56, 300, 160, "Kafkas Cephesi", ["• Sarıkamış Harekâtı ve ağır kış şartları", "• 1915 Sevk ve İskân (Tehcir) Kanunu", "• Mustafa Kemal Muş ve Bitlis’i geri aldı", "• 1918 Brest-Litovsk: Kars, Ardahan, Batum alındı"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(350, 56, 300, 160, "Çanakkale Cephesi (1915)", ["• 18 Mart Deniz Zaferi ve Nusret Mayın Gemisi", "• Mustafa Kemal: Arıburnu, Conkbayırı, Anafartalar", "• Savaş 2 yıl uzadı, Çarlık Rusyası yıkıldı", "• Mustafa Kemal Milli Mücadele lideri olarak tanındı"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MUSTAFA KEMAL’İN SAVAŞTIĞI CEPHLER VE SAVAŞIN SONU</text>'
    ic += _kart(30, 56, 195, 160, "Mustafa Kemal (ÇıKıS)", ["1. Çanakkale Cephesi", "2. Kafkas Cephesi", "3. Suriye-Filistin Cephesi", "(Sırasıyla görev yaptığı yerler)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "ABD ve Wilson İlkeleri", ["ABD 1917’de savaşa girdi", "Savaşın süresini kısaltmıştır", "Wilson İlkeleri yayımlandı", "Yenilenlerden toprak alınmayacak"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Savaşın Sonuçları", ["İmparatorluklar parçalandı", "Yeni ulus devletler kuruldu", "Milletler Cemiyeti kuruldu", "Mondros Ateşkesi imzalandı"], "#f1f5f9", "#64748b", "#334155")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    bolumler = v.get("bolumler", [])
    eslesme = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    for idx, key in eslesme:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[key]
