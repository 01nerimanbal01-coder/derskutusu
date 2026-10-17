# -*- coding: utf-8 -*-
"""12. Sınıf Kelam — 4. Hafta görsel modülü: Kelam İlminin Doğuşu ve Gelişmesi."""


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
        'text-anchor="middle">KELAM İLMİNİN DOĞUŞUNA ETKİ EDEN İÇ VE DIŞ SEBEPLER</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "İç Sebepler (Müslüman Toplum İçi Etkenler)", [
        "• Kur'an-ı Kerim'in akletmeyi ve tefekkürü emretmesi",
        "• Müteşâbih ayetlerin ve kader konusunun yorumlanması",
        "• Hz. Osman'ın şehadeti, Cemel ve Sıffîn savaşları",
        "• 'Büyük günah işleyenin durumu' ve 'Hilafet/İmamet'",
        "  tartışmalarıyla siyasi-itikadî fırkaların çıkması",
        "• Haricîlik, Şîa, Mürcie, Cebriyye ve Kaderiyye"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Dış Sebepler (Kültürel ve Felsefi Etkenler)", [
        "• Fetihlerle birlikte Yahudi, Hristiyan, Mecûsî, Sâbiî,",
        "  Maniheist ve Budist kültürlerle karşılaşılması",
        "• Yeni Müslüman olanların eski inanç alışkanlıkları",
        "• Tercüme faaliyetleriyle Yunan felsefesi ve mantığının",
        "  İslam dünyasına girmesi",
        "• İslam inancını akli delillerle savunma ihtiyacı"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">İLK İTİKADÎ FIRKALAR VE MU\'TEZİLE EKOLÜ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Erken Dönem Fırkaları ve Öncü Âlimler", [
        "• Cebriyye: İnsanın iradesini yok sayan aşırı kaderci görüş",
        "• Kaderiyye: İnsanın kendi fiilini yarattığını savunan görüş",
        "• Mürcie: Ameli imandan ayırıp hükmü Allah'a bırakanlar",
        "• Selefiye: Müteşâbihleri te'vil etmeden kabul edenler",
        "• Hasan-ı Basrî ve İmam-ı Âzam Ebû Hanîfe (el-Fıkhu'l-Ekber)",
        "  Ehl-i Sünnet kelamının temellerini atmıştır"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Mu'tezile Ekolü (Vâsıl b. Atâ)", [
        "• Kurucusu Vâsıl b. Atâ ve Amr b. Ubeyd'dir (8. yy)",
        "• Kelamda akli istidlâl yöntemini ilk kullanan ekoldür",
        "• Beş Temel İlkesi (Usûl-i Hamse): 1) Tevhid, 2) Adalet,",
        "  3) Va'd ve Vaîd, 4) el-Menzile beyne'l-Menzileteyn",
        "  (Büyük günah işleyen iman-küfür arasındadır),",
        "  5) Emr-i bi'l-Ma'rûf ve Nehy-i ani'l-Münker"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">EHL-İ SÜNNET KELAM MEKTEPLERİ: MÂTÜRÎDÎLİK VE EŞ\'ARÎLİK</text>'
    )
    ic += _kart(25, 50, 340, 175, "#6366f1", "Mâtürîdîlik (İmam Ebû Mansûr el-Mâtürîdî)", [
        "• Semerkant'ta İmam Mâtürîdî (ö. 944) tarafından kuruldu",
        "• Temel eseri: Kitâbü't-Tevhîd ve Te'vîlâtü'l-Kur'ân",
        "• Vahiy ile akıl arasında tam bir denge kurmuştur",
        "• İnsan aklıyla Allah'ın varlığını ve iyilik-kötülüğü",
        "  (hüsün-kubuh) kavrayabilir; cüz'î iradeye sahiptir",
        "• Önemli âlimleri: Pezdevî, Ebü'l-Muîn en-Nesefî, Sabûnî"
    ])
    ic += _kart(395, 50, 340, 175, "#14b8a6", "Eş'arîlik (İmam Ebü'l-Hasan el-Eş'arî)", [
        "• Basra ve Bağdat'ta İmam Eş'arî (ö. 936) kurmuştur",
        "• Temel eseri: el-İbâne, el-Lüma' ve Makâlâtü'l-İslâmiyyîn",
        "• 40 yaşına kadar Mu'tezile'de kalmış, sonra Ehl-i Sünnet",
        "  inancını akli delillerle savunmaya başlamıştır",
        "• İrade konusunda 'Kesb' teorisini geliştirmiştir",
        "• Önemli âlimleri: Bâkıllânî, Cüveynî, Gazzâlî, Fahreddin Râzî"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">KELAM TARİHİNİN DÖNEMLERİ VE YENİ İLM-İ KELAM</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Mütekaddimîn ve Müteahhirîn Dönemleri", [
        "• Mütekaddimîn (İlk Dönem - Gazzâlî'ye kadar): Ehl-i Sünnet",
        "  kelamının sistemleştiği, Mu'tezile ve batıl fırkalara",
        "  cevap verildiği dönemdir (Bâkıllânî, Cüveynî, Nesefî)",
        "• Müteahhirîn (Sonraki Dönem - Gazzâlî sonrası): İmam",
        "  Gazzâlî ile Aristo mantığı kelama dahil edilmiş, felsefe",
        "  ile kelam mezcedilmiştir (Râzî, Îcî, Teftâzânî, Cürcânî)"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Yeni İlm-i Kelam Dönemi (19-20. Yüzyıl)", [
        "• Batı'da ortaya çıkan materyalizm, pozitivizm, darvinizm",
        "  ve ateizm gibi akımlara karşı İslam inancını modern",
        "  bilim ve felsefe diliyle savunmak için doğmuştur",
        "• Osmanlı ve Türkiye'deki öncüleri: İzmirli İsmail Hakkı",
        "  (Yeni İlm-i Kelam), Abdüllatif Harpûtî, Filibeli Ahmed",
        "  Hilmi, Elmalılı Hamdi Yazır ve Ömer Nasuhi Bilmen"
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