# -*- coding: utf-8 -*-
"""12. Sınıf Biyoloji — 4. Hafta görsel modülü: Biyoteknoloji ve Genetik Mühendisliği."""


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
        'text-anchor="middle">GENETİK MÜHENDİSLİĞİ VE BİYOTEKNOLOJİ KAVRAMLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Genetik Mühendisliği", [
        "• Canlıların kalıtsal materyalini (DNA/RNA)",
        "  moleküler düzeyde inceleyen ve değiştiren alandır",
        "• Genlerin izolasyonu, çoğaltılması, kesilmesi",
        "  ve bir canlıdan diğerine aktarılmasını kapsar",
        "• Rekombinant DNA teknolojisini geliştirir",
        "• Bilimsel yöntem ve teknik tasarım boyutudur"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Geleneksel ve Modern Biyoteknoloji", [
        "• Biyoteknoloji: Canlı organizmaları kullanarak",
        "  endüstriyel ve tıbbi ürün üretme teknolojisidir",
        "• Geleneksel: Yoğurt, peynir, sirke, hamur mayalama",
        "  ve ıslah çalışmaları (gen aktarımı yoktur)",
        "• Modern: Genetik mühendisliği yöntemleriyle",
        "  insülin, aşı, antikor ve GDO üretimi"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">GEN KLONLAMASI VE REKOMBİNANT DNA BASAMAKLARI</text>'
    )
    ic += _kart(25, 50, 170, 175, "#d97706", "1. İzolasyon", [
        "• İstenilen geni taşıyan",
        "  hücreden DNA ve",
        "  bakteriden plazmit",
        "  (vektör) saf olarak",
        "  ayrıştırılır (izole edilir)"
    ])
    ic += _kart(210, 50, 170, 175, "#8b5cf6", "2. Kesim (Restriksiyon)", [
        "• Hedef gen ve plazmit",
        "  AYNI restriksiyon",
        "  endonükleaz enzimi",
        "  ile kesilerek uyumlu",
        "  yapışkan uçlar oluşturulur"
    ])
    ic += _kart(395, 50, 170, 175, "#ec4899", "3. Birleştirme (Ligaz)", [
        "• Kesilen gen ile plazmit,",
        "  DNA LİGAZ enzimiyle",
        "  fosfodiester bağı",
        "  kurularak birleştirilir:",
        "  Rekombinant DNA (rDNA)"
    ])
    ic += _kart(580, 50, 155, 175, "#14b8a6", "4. Aktarım &amp; Üretim", [
        "• rDNA tekrar bakteri",
        "  hücresine aktarılır",
        "• Bakteri bölündükçe",
        "  gen klonlanır ve ürün",
        "  (insülin vb.) üretilir"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">MODEL ORGANİZMALAR, GDO VE TRANSGENİK CANLILAR</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Model Organizmalar", [
        "• Kısa yaşam döngüsü olan,",
        "  laboratuvarda kolay yetişen",
        "• Genom haritası bilinen ve",
        "  genomu küçük canlılardır",
        "• Örnek: E. coli (bakteri),",
        "  meyve sineği (Drosophila), fare"
    ])
    ic += _kart(268, 50, 225, 175, "#0ea5e9", "GDO ve Transgenik Canlı", [
        "• GDO: Genetiği Değiştirilmiş",
        "  Organizma (kendi geni veya",
        "  başka tür geni değiştirilmiş)",
        "• Transgenik: Başka bir türe ait",
        "  gen aktarılmış canlıdır",
        "• Örnek: Altın pirinç (A vitamini)"
    ])
    ic += _kart(510, 50, 225, 175, "#10b981", "Canlı Klonlama (Dolly)", [
        "• Vücut hücresinin (2n) çekirdeği",
        "  çıkarılır; çekirdeği çıkarılmış",
        "  yumurta hücresine kaynaştırılır",
        "• Oluşan kuzu, ÇEKİRDEK",
        "  VERİCİSİ koyunun genetik",
        "  ikizidir (Mitokondri yumurtadan)"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">SAĞLIK UYGULAMALARI, DNA PARMAK İZİ VE BİYOETİK</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Kök Hücre, Gen Terapisi ve PCR", [
        "• Kök Hücre: Farklılaşmamış, bölünme yeteneği",
        "  yüksek hücredir (Embriyonik, Kordon kanı, Yetişkin)",
        "• Gen Terapisi: Bozuk genlerin sağlam genlerle",
        "  değiştirilerek kalıtsal hastalıkların tedavisidir",
        "• PCR ve Jel Elektroforezi: Tekrarlayan DNA dizileriyle",
        "  DNA Parmak İzi (Adli tıp ve babalık testi) çıkarılır"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "Biyogüvenlik ve Biyoetik İlkeleri", [
        "• İnsan Genom Projesi genetik hastalıkların",
        "  tanısını kolaylaştırmıştır, ancak kişisel genetik",
        "  verilerin gizliliği biyoetik açıdan korunmalıdır",
        "• İnsan klonlama tüm dünyada etik dışı ve yasaktır",
        "• GDO'lu ürünlerin ekolojik dengeye ve biyoçeşitliliğe",
        "  etkileri Biyogüvenlik Kurullarınca denetlenir"
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
