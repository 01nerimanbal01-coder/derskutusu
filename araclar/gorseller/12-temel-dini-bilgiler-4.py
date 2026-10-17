# -*- coding: utf-8 -*-
"""12. Sınıf Temel Dini Bilgiler — 4. Hafta görsel modülü: İslam İnancının Temel Kaynakları (Kitap, Sünnet ve Salim Akıl)."""


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
        'text-anchor="middle">İSLAM İNANCININ BİRİNCİ KAYNAĞI: KİTAP (KUR\'AN-I KERİM)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Kur'an-ı Kerim'in Temel Özellikleri", [
        "• Allah Teâlâ tarafından Cebrâil (a.s.) aracılığıyla",
        "  Hz. Muhammed'e (s.a.v.) indirilen son ilahi kitaptır",
        "• Lafzı ve manası mucizedir; tevatürle nakledilmiştir",
        "• Tek bir harfi bile değişmeden korunmuştur (Hicr 9)",
        "• İnanç (akaid) esaslarının en kesin ve birincil delilidir",
        "• Kendisinden önceki ilahi kitapları tasdik ve tashih eder"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Kur'an'da İnanç Esaslarının Sunumu", [
        "• Tevhid, Nübüvvet ve Ahiret (Usûl-i Selâse) merkezdedir",
        "• İnanç konularını fıtrata ve akla hitap ederek açıklar",
        "• Evrendeki düzenden (kozmolojik deliller) örnekler verir",
        "• Gayb âlemi (melekler, cennet, cehennem, kader)",
        "  hakkındaki tek kesin bilgi kaynağımız vahiydir",
        "• Şirk, hurafe ve taklidi reddederek tahkiki emreder"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">İKİNCİ TEMEL KAYNAK: SÜNNET-İ SENİYYE</text>'
    )
    ic += _kart(25, 50, 225, 175, "#d97706", "Kavlî (Sözlü) Sünnet", [
        "• Hz. Peygamber'in (s.a.v.)",
        "  mübarek sözleri ve hadisleridir",
        "• Örn: Cibrîl Hadisi'nde altı",
        "  iman esasını açıklaması",
        "• Kur'an ayetlerini tefsir",
        "  ve beyan eden sözleridir"
    ])
    ic += _kart(268, 50, 225, 175, "#8b5cf6", "Fiilî (Uygulamalı) Sünnet", [
        "• Hz. Peygamber'in ibadetleri",
        "  ve ahlaki ilkeleri bizzat",
        "  yaşayarak göstermesidir",
        "• Namazın kılınışı, haccın",
        "  yapılışı ve zekât uygulaması",
        "• Yaşayan Kur'an oluşudur"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Takrîrî (Onaylayıcı) Sünnet", [
        "• Sahabilerin yaptığı bir işi",
        "  Hz. Peygamber'in görüp",
        "  yasaklamaması ve onaylamasıdır",
        "• Mütevatir ve sahih hadisler",
        "  inanç ve amelde delildir",
        "• Kur'an ile Sünnet etle tırnaktır"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">VAHYİ ANLAYAN KAYNAK: SALİM AKIL VE DUYULAR</text>'
    )
    ic += _kart(25, 50, 340, 175, "#6366f1", "Salim Akıl (Akl-ı Selim)", [
        "• Önyargı, kibir, taassup ve nefsani arzulardan",
        "  arınmış, yaratılış (fıtrat) temizliğini koruyan akıldır",
        "• Dini sorumluluğun (mükellefiyetin) ilk şartıdır",
        "• Kâinattaki düzenden Yaratıcı'nın varlığını ve birliğini",
        "  kavrar; vahyin hakikatini anlayıp tasdik eder",
        "• Gayb konularında tek başına hüküm koyamaz, vahye uyar"
    ])
    ic += _kart(395, 50, 340, 175, "#14b8a6", "Vahiy ile Akıl Arasındaki Uyum", [
        "• Vahiy 'güneş ışığı', akıl ise 'gören göz' gibidir",
        "• Işık olmadan göz karanlıkta göremez; göz olmadan",
        "  da ışıktan yararlanılamaz",
        "• İslam'da sahih nakil (vahiy) ile salim akıl",
        "  asla birbiriyle çelişmez, birbirini tamamlar",
        "• İlham ve rüya gibi öznel haller genel delil olamaz"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">SAHİH DİNİ BİLGİYİ KORUMA VE HURAFELERDEN SAKINMA</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "İnanç Esaslarında Delil Şartı", [
        "• İman esasları zan ve tahmine değil, 'kesin bilgiye'",
        "  (yakîn) dayanmak zorundadır",
        "• Kur'an-ı Kerim ayetleri ve mütevatir sünnet",
        "  iman esaslarını belirleyen kesin delillerdir",
        "• Uydurma (mevzû) rivayetlerle inanç inşa edilemez",
        "• Dini bilgi mutlaka ana kaynaklardan öğrenilmelidir"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Doğru İnanç Kaynaklarına Bağlılığın Sonucu", [
        "• Mümini şirkten, batıl inançlardan ve falcılık,",
        "  büyücülük, uğursuzluk gibi hurafelerden korur",
        "• Dini istismar eden sahte kurtarıcılara karşı",
        "  güçlü bir bilinç ve uyanıklık kazandırır",
        "• İslam toplumunda tevhid ve inanç birliği sağlar",
        "• Bilinçli (tahkikî) ve sarsılmaz bir iman inşa eder"
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