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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">BİLİMSEL ARAŞTIRMA SÜRECİNİN BASAMAKLARI</text>'
    ic += _kart(30, 56, 195, 160, "1. Gözlem &amp; Problem", ["Nitel (5 duyu) ve Nicel (ölçü)", "gözlemlerin yapılması", "Verilerin toplanması", "Araştırma probleminin tespiti"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "2. Hipotez &amp; Tahmin", ["Hipotez: Geçici çözüm önerisi", "(Deneylerle sınanabilir olmalı)", "Tahmin: ‘Eğer … ise … dır’", "mantıksal çıkarım cümlesi"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "3. Kontrollü Deney", ["Bağımsız değişken: Etkileyen", "Bağımlı değişken: Etkilenen", "Kontrol grubu &amp; Deney grubu", "Desteklenmezse hipotez değişir!"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">BİLİM ETİĞİ VE TEMEL ETİK İLKELER</text>'
    ic += _kart(30, 56, 195, 160, "Dürüstlük ve Açıklık", ["Verileri çarpıtmadan sunma", "Yöntem ve sonuçta şeffaflık", "Hataları gizlememe", "Tarafsız (nesnel) yaklaşım"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Emeğe Saygı", ["Önceki çalışmalara kaynak", "göstermek (atıf yapmak)", "Katkı sunanları belirtmek", "Fikri mülkiyet hakkını koruma"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Canlılara ve Doğaya Saygı", ["İnsan ve hayvan hakları", "3R İlkesi (Azaltma, İyileştirme,", "Yerine koyma) - Etik Kurul", "Çevreye zarar vermeme"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">BİLİM ETİĞİ İHLALLERİ (ETİK DIŞI DAVRANIŞLAR)</text>'
    ic += _kart(30, 56, 195, 160, "İntihal (Aşırma)", ["Başkasının fikir, metin veya", "verilerini kaynak göstermeden", "kendi eseri gibi sunmak", "(Bilimsel hırsızlık)"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Uydurma &amp; Çarpıtma", ["Uydurma (Fabrikasyon): Yoktan", "hayali deney verisi üretmek", "Çarpıtma (Falsifikasyon): Veriyi", "hipoteze uydurmak için değiştirmek"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Diğer İhlaller", ["Tekrar yayım (Duplikasyon)", "Dilimleme (Salamizasyon)", "Haksız yazarlık (katkısı olmayanı", "eklemek veya olanı çıkarmak)"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TEORİ, KANUN VE BİYOLOJİDE ETİK KURULLAR</text>'
    ic += _kart(30, 56, 300, 160, "Teori (Kuram) ve Kanun (Yasa)", ["• Kanun: Doğa olayının NASIL gerçekleştiğini betimler", "• Teori: Olayın NEDEN gerçekleştiğini kanıtlarla açıklar", "• Teoriler kanıtlandığında kanuna DÖNÜŞMEZ!", "• İkisi farklı bilimsel bilgi türleridir (Hiyerarşi yoktur)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(350, 56, 300, 160, "Biyolojide Etik Kurul Onayı", ["• Deney hayvanları üzerinde çalışmadan önce zorunludur", "• İnsan gönüllülerde ‘Aydınlatılmış Onam’ alınır", "• Gen teknolojisi, klonlama ve yapay zeka etiği", "• Bilimsel bilginin insanlık yararına kullanılması"], "#e0e7ff", "#6366f1", "#4338ca")
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
