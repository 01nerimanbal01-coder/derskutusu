# -*- coding: utf-8 -*-
"""12. Sınıf İslam Kültür ve Medeniyeti — 4. Hafta görsel modülü: İslam Kültür ve Medeniyetinin Kaynakları."""


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
        'text-anchor="middle">İLAHİ (VAHYÎ) KAYNAKLAR: KUR\'AN-I KERİM VE SÜNNET</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Kur'an-ı Kerim (Kurucu Ana Kaynak)", [
        "• İslam kültür ve medeniyetinin ruhu ve merkezidir",
        "• Tevhid, adalet, ilim, merhamet ve emanet ilkeleriyle",
        "  yeni bir dünya görüşü ve insan modeli inşa etmiştir",
        "• Tefsir, fıkıh, kelam, Arap dili ve hat-tezhip gibi",
        "  tüm İslami ilim ve sanatların doğuş kaynağıdır",
        "• Evreni incelemeyi emrederek bilimi başlatmıştır"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Sünnet-i Seniyye (Kur'an'ın Pratiğe Aktarımı)", [
        "• Hz. Peygamber'in (s.a.v.) söz, fiil ve takrirleridir",
        "• Kur'an'daki ilkelerin birey, aile, toplum, hukuk",
        "  ve devlet hayatında nasıl yaşanacağını göstermiştir",
        "• Medine Vesikası, Mescid-i Nebevî, Suffe ve vakıf",
        "  geleneğiyle İslam şehircilik ve kurumlarını kurmuştur",
        "• Nezafet (temizlik), nezaket ve estetik bilinci vermiştir"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">BEŞERÎ VE İLMÎ KAYNAKLAR: AKL-I SELİM VE HAVÂSS-I SELÎME</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Akl-ı Selim (Salim Akıl)", [
        "• Önyargı ve taassuptan arınmış sağlıklı düşünme gücüdür",
        "• Vahyin ilkelerini yeni karşılaşılan toplumsal ve",
        "  hukuki sorunlara uygular (İçtihat, Kıyas, İstihsan)",
        "• Matematik, mantık, felsefe, siyasetname ve şehir",
        "  planlaması gibi alanlarda medeniyet üretmiştir",
        "• Vahiy ile akıl birbirini tamamlayan iki kanattır"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Havâss-ı Selîme (Sağlam Beş Duyu / Deney-Gözlem)", [
        "• Görme, işitme, dokunma, tatma ve koklama duyularıdır",
        "• Dış dünyayı ve tabiat olaylarını inceleyen 'deney ve",
        "  gözlem (tümevarım) metodunun' temel aracıdır",
        "• Müslüman âlimler (İbnü'l-Heysem, Bîrûnî, İbn Sînâ,",
        "  Câbir b. Hayyân) sağlam duyulara dayalı deneylerle",
        "  tıp, optik, kimya ve astronomiyi kurmuşlardır"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">SOSYAL VE KÜLTÜREL KAYNAKLAR: ÖRF-ÂDET VE ETKİLEŞİM</text>'
    )
    ic += _kart(25, 50, 340, 175, "#6366f1", "Örf ve Âdetler (Gelenekler)", [
        "• Bir toplumda eskiden beri uygulanan ve sağduyu",
        "  sahiplerince güzel kabul edilen sosyal kurallardır",
        "• İslam, tevhid ve ahlak ilkelerine aykırı olmayan",
        "  sahih örfleri ('Örf-i Sahih') korumuş ve kaynak saymıştır",
        "• Mecelle kaidesi: 'Âdet muhakkemdir' (Örf hakem kılınır)",
        "• Türk, Arap, İran, Berberi örfleri medeniyeti zenginleştirmiştir"
    ])
    ic += _kart(395, 50, 340, 175, "#14b8a6", "Diğer Kültür ve Medeniyetlerle Etkileşim", [
        "• 'Hikmet müminin yitiğidir; nerede bulursa alır' ilkesi",
        "• Mezopotamya, Mısır, İran (Sâsânî), Hint, Yunan/Helenistik",
        "  ve Çin medeniyetlerinin birikimlerinden yararlanılmıştır",
        "• Ancak körü körüne taklit edilmemiş; Tevhid potasında",
        "  eritilip ayıklanarak özgün İslam kimliği kazandırılmıştır",
        "• Tercüme faaliyetleri ve ticaret yolları köprü olmuştur"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">KAYNAKLARIN MEDENİYET UNSURLARINA DÖNÜŞÜMÜ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#059669", "Kur'an ve Sünnetten", [
        "• Tevhid inancı ve ibadetler",
        "• Cami merkezli şehir planı",
        "• Vakıf ve infak kurumları",
        "• Hüsn-i hat, tezhip ve",
        "  Kur'an tilaveti sanatları",
        "• Evrensel insan hakları"
    ])
    ic += _kart(268, 50, 225, 175, "#0ea5e9", "Akıl ve Beş Duyudan", [
        "• Deneysel tıp ve şifahaneler",
        "• Rasathaneler ve usturlap",
        "• Cebir, algoritma ve optik",
        "• Su kemerleri, köprüler,",
        "  hamamlar ve kervansaraylar",
        "• Fıkıh ve kelam sistematiği"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Örf ve Etkileşimden", [
        "• Selçuklu-Osmanlı kubbe ve",
        "  kümbet mimarisi, çinicilik",
        "• Divan teşkilatı ve vakfiyeler",
        "• Ebru, minyatür ve musiki",
        "• Misafirperverlik, ahilik",
        "  ve fütüvvet gelenekleri"
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