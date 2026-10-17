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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TARİHSEL BİLGİNİN ÜRETİM SÜRECİ (5T YÖNTEMİ)</text>'
    ic += _kart(30, 56, 195, 160, "1. Tarama &amp; 2. Tasnif", ["1. Tarama (Heuristik):", "Kaynak ve belgeleri arama", "2. Tasnif (Sınıflandırma):", "Zaman, mekân ve konuya göre"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "3. Tahlil &amp; 4. Tenkit", ["3. Tahlil (Çözümleme):", "Bilgi yeterliliğini kontrol etme", "4. Tenkit (Eleştiri):", "Dış ve iç tenkitle doğruluk"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "5. Terkip (Sentez)", ["Doğrulanmış bilgileri birleştirme", "Neden-sonuç bağını kurma", "Nesnel bir dille eseri yazma", "Tarihsel bilginin inşası"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TARİHSEL KAYNAKLARIN SINIFLANDIRILMASI</text>'
    ic += _kart(30, 56, 300, 160, "Oluştuğu Döneme Göre Kaynaklar", ["• Birinci Elden (Ana) Kaynak: Olayın geçtiği döneme", "  ait özgün kanıt (Ferman, sikke, kitabe, antlaşma)", "• İkinci Elden Kaynak: Ana kaynaklara dayanılarak", "  sonradan yazılan eserler (Ders kitabı, makale)"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(350, 56, 300, 160, "Malzeme Türüne Göre Kaynaklar", ["• Sözlü Kaynaklar: Destan, efsane, mit, atasözü", "• Yazılı Kaynaklar: Tablet, kitabe, ferman, kronik", "• Sesli ve Görüntülü: Fotoğraf, film, ses kaydı", "• Gerçek Eşya/Nesne (Arkeolojik): Silah, kap, takı"], "#e0f2fe", "#0284c7", "#0369a1")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KAYNAKLARIN SORGULANMASI: DIŞ TENKİT VE İÇ TENKİT</text>'
    ic += _kart(30, 56, 300, 160, "Dış Tenkit (Biçimsel Eleştiri)", ["• Kaynağın gerçek (orijinal) olup olmadığı incelenir", "• Eserin adı, yazarı, basıldığı yer ve tarih saptanır", "• Kağıt, mürekkep ve yazı karakteri (paleografya)", "• ‘Bu belge sahte mi yoksa gerçek mi?’ sorusu"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(350, 56, 300, 160, "İç Tenkit (İçerik Eleştirisi)", ["• Yazarın verdiği bilgilerin doğruluğu sorgulanır", "• Yazar olayları çarpıtmış mı, tarafsız mı?", "• Farklı kaynaklarla (karşılaştırmalı) teyit edilir", "• ‘Yazar doğruyu mu söylüyor?’ sorusu"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TARİHSEL ARAŞTIRMADA NESNELLİK VE BAĞLAMSALLIK</text>'
    ic += _kart(30, 56, 195, 160, "Dönemin Şartları", ["Olayı yaşandığı çağın değer", "yargılarıyla değerlendirmek", "Bugünün gözüyle yargılamamak", "Anakronizmden kaçınmak!"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Çoklu Bakış Açısı", ["Tek kaynağa bağlı kalmamak", "Farklı devletlerin arşivlerini", "birlikte karşılaştırmak", "Kanıta dayalı nesnel çıkarım"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Değişen Tarihsel Bilgi", ["Tarihsel olay tekrarlanamaz", "Deney ve gözlem yapılamaz", "Yeni belge (ör. Göbeklitepe)", "eski bilgiyi değiştirebilir!"], "#f1f5f9", "#64748b", "#334155")
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
