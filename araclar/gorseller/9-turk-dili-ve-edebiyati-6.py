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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MÜLAKAT (GÖRÜŞME) TÜRÜNÜN TEMEL ÖZELLİKLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Mülakat Nedir?", ["Alanında uzman/ünlü kişilerle", "Soru-cevap tekniğine dayalı", "Planlı ve amaçlı görüşme", "Öğretici (bilgilendirici) metin"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Yapı ve Bölümler", ["1. Giriş: Konunun ve kişinin", "kısaca tanıtılması", "2. Gelişme: Sorular ve yanıtlar", "3. Sonuç: Teşekkür ve kapanış"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Dil ve Anlatım", ["Açık, duru ve anlaşılır üslup", "Nesnel ve saygılı tutum", "Cevapları değiştirmeden aktarma", "Göndergesel dil işlevi"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MÜLAKAT İLE RÖPORTAJ ARASINDAKİ FARKLAR</text>'
    ic += _kart(30, 56, 300, 160, "Mülakat (Görüşme)", ["• Tek eksenlidir: Soru ve cevaba dayanır", "• Görüşülen kişinin sözleri aynen aktarılır", "• Yazar kendi kişisel yorum ve izlenimini katmaz", "• Amaç uzman görüşünü doğrudan okuyucuya sunmaktır"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(350, 56, 300, 160, "Röportaj", ["• Çok boyutludur: Gezi, gözlem ve araştırma içerir", "• Fotoğraf, belge ve mekan betimlemeleriyle desteklenir", "• Yazar kendi izlenimlerini ve edebi üslubunu katar", "• Bir yeri, olayı veya kurumu derinlemesine inceler"], "#e0f2fe", "#0284c7", "#0369a1")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">ÇOK MODLU METİNLERDE DİNLEME / İZLEME SÜRECİ</text>'
    ic += _kart(30, 56, 195, 160, "Çok Modlu Metin", ["Yazılı, sözlü, işitsel, görsel", "unsurların bir arada kullanımı", "Ses tonu, vurgu ve tonlama", "Jest, mimik ve beden dili"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Dinleme Öncesi &amp; Sırası", ["Ön bilgileri harekete geçirme", "Dinleme amacını belirleme", "Anahtar kavramları not alma", "Örtük iletileri yakalama"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Dinleme Sonrası", ["İçeriği özetleme ve çözümleme", "Tutarlılık ve geçerlilik analizi", "Sözün inceliğini değerlendirme", "Öz değerlendirme yapma"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TÜRK EDEBİYATINDA ÖNEMLİ MÜLAKAT ESERLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Ruşen Eşref Ünaydın", ["‘Diyorlar ki’ (1918)", "Edebiyatımızda ilk kapsamlı", "mülakat eseri kabul edilir", "‘Anafartalar Kumandanı M. Kemal’"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Cumhuriyet Dönemi", ["Hikmet Feridun Es: ‘Bugün de", "Diyorlar ki’", "Mustafa Baydar: ‘Edebiyatçılarımız", "Ne Diyorlar’"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Gاب (Gavsi Ozansoy) &amp; Diğer", ["Gavsi Ozansoy: ‘40 Yıl Sonra", "Diyorlar ki’", "Abdi İpekçi, Yaşar Nabi Nayır", "Sözlü kültür ve basın arşivi"], "#f1f5f9", "#64748b", "#334155")
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
