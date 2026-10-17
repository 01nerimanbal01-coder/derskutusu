# -*- coding: utf-8 -*-
"""11. Sınıf Dinler Tarihi — 4. Hafta görsel modülü: Dinler Tarihinin Temel Kaynakları."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">DİNLER TARİHİNİN TEMEL KAYNAKLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Birincil (Asli ve Kutsal) Kaynaklar", [
        "• Dinlerin kendi kutsal metinleri ve külliyatları",
        "• Kur'an-ı Kerim, Tanah, Kitab-ı Mukaddes",
        "• Vedalar, Upanişadlar, Tripitaka ve Avesta",
        "• İbadet ve ayin kitapları, konsil kararları",
        "• Tapınak yazıtları ve arkeolojik kalıntılar",
        "• Yaşayan dindarların ritüel ve uygulamaları"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "İkincil (Yardımcı ve Tarihî) Kaynaklar", [
        "• Kutsal metinler üzerine yazılan şerh ve tefsirler",
        "• Tarihçilerin, seyyahların ve coğrafyacıların eserleri",
        "• Mezhepler ve dinler tarihi (Milel ve Nihal) kitapları",
        "• Antropolojik, sosyolojik ve filolojik araştırmalar",
        "• Karşılaştırmalı mitoloji ve epigrafi incelemeleri",
        "• Dış gözlemcilerin kaydettiği tarihsel belgeler"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">ARKELOJİK, EPİGRAFİK VE YAŞAYAN KAYNAKLAR</text>'
    )
    ic += _kart(25, 50, 225, 175, "#d97706", "Arkeolojik Bulgular", [
        "• Antik tapınaklar, sunaklar",
        "  ve mezar mimarileri",
        "• Göbeklitepe, Mısır piramitleri",
        "  ve Mezopotamya zigguratları",
        "• Kutsal semboller, heykeller",
        "  ve ritüel eşyaları"
    ])
    ic += _kart(268, 50, 225, 175, "#8b5cf6", "Epigrafik Belgeler", [
        "• Taş, kil tablet, papirüs ve",
        "  metallere kazınmış yazıtlar",
        "• Çivi yazılı Sümer-Babil",
        "  tabletleri ve Ölü Deniz",
        "  (Kumran) yazmaları",
        "• Orhun Abideleri ve kitabeler"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Sözlü &amp; Yaşayan Gelenek", [
        "• Yazılı metni olmayan geleneksel",
        "  dinlerdeki mitler ve destanlar",
        "• Kuşaktan kuşağa aktarılan",
        "  dualar ve ilahiler",
        "• Günümüzde devam eden",
        "  hac, bayram ve ayinler"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">İSLAM ÂLİMLERİNİN DİNLER TARİHİNE ÖNCÜ KATKILARI</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Ebû Reyhân el-Bîrûnî", [
        "• Eseri: Tahkîku mâ li'l-Hind",
        "  ve el-Âsâru'l-Bâkıye",
        "• Sanskritçe öğrenerek Hint",
        "  dinlerini yerinde inceledi",
        "• Tarafsız ve betimleyici",
        "  yöntemin dünyadaki öncüsüdür"
    ])
    ic += _kart(268, 50, 225, 175, "#14b8a6", "İbn Hazm el-Endelüsî", [
        "• Eseri: el-Fasl fi'l-Milel",
        "  ve'l-Ehvâi ve'n-Nihal",
        "• Tevrat ve İncil metinlerini",
        "  eleştirel metin tenkidine",
        "  tabi tutan ilk âlimdir",
        "• Karşılaştırmalı analiz yaptı"
    ])
    ic += _kart(510, 50, 225, 175, "#0ea5e9", "Ebu'l-Feth eş-Şehristânî", [
        "• Eseri: el-Milel ve'n-Nihal",
        "• Dinleri ve felsefi ekolleri",
        "  sistematik olarak sınıflandırdı",
        "• Vahye dayalı dinler ile beşerî",
        "  inançları objektif tanıttı",
        "• Klasik dönemin zirve eseridir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">KUR\'AN-I KERİM\'İN DİĞER DİNLERE BAKIŞI VE KAYNAK DEĞERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Kur'an'da Zikredilen İnanç Grupları", [
        "• Yahudiler (Hûd / Benî İsrâil) ve Hristiyanlar (Nasârâ)",
        "• Ehl-i Kitap kavramı ve ortak tevhid çağrısı",
        "• Sâbiîler ve Mecûsîler (ateşperestlik geleneği)",
        "• Müşrikler (putperestler) ve Dehrîler (materyalistler)",
        "• Hanîfler (Hz. İbrahim'in tevhid geleneği)",
        "• Müslüman âlimlere araştırma ufku açmıştır"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "Kaynak Kullanımında Bilimsel İlkeler", [
        "• Her dini önce kendi kutsal kaynaklarından tanımak",
        "• Kaynağın tarihsel otantikliğini ve dilini denetlemek",
        "• Önyargıdan uzak, tarafsız (epokhe) tutum takınmak",
        "• Metin ile yaşayan pratik arasındaki farkı görmek",
        "• Çoklu kaynak doğrulaması (metin + arkeoloji) yapmak",
        "• Empati ve akademik dürüstlükle betimlemek"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]