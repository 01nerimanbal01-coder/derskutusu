from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 230
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">KLASİK FIKIH TANIMLARI VE FIKHIN 5 TEMEL KONU ALANI</text>')
    # Sol: 3 Tanım
    ic.append('<rect x="22" y="45" width="285" height="165" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>')
    ic.append('<text x="164" y="64" text-anchor="middle" font-size="10.5" font-weight="700" fill="#1e40af">KLASİK FIKIH TANIMLARI</text>')
    ic.append('<rect x="34" y="73" width="261" height="38" rx="6" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="42" y="88" font-size="9" font-weight="700" fill="#1d4ed8">1. Ebu Hanife (En Geniş Kapsam):</text>')
    ic.append('<text x="42" y="103" font-size="8.5" fill="#1e293b">Kişinin yararına ve zararına olan şeyleri bilmesidir.</text>')
    ic.append('<rect x="34" y="117" width="261" height="42" rx="6" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="42" y="132" font-size="9" font-weight="700" fill="#1d4ed8">2. İmam Şafii (Delil ve Amel Vurgusu):</text>')
    ic.append('<text x="42" y="146" font-size="8.5" fill="#1e293b">Amelî hükümleri özel delillere dayanarak bilmektir.</text>')
    ic.append('<rect x="34" y="165" width="261" height="36" rx="6" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="42" y="180" font-size="9" font-weight="700" fill="#1d4ed8">3. Mecelle (Özlü Hukuk Tanımı):</text>')
    ic.append('<text x="42" y="194" font-size="8.5" fill="#1e293b">Dinin şeri amelî meselelerini bilmektir.</text>')
    # Sağ: 5 Konu
    ic.append('<rect x="320" y="45" width="278" height="165" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="459" y="64" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">FIKHIN 5 TEMEL KONUSU</text>')
    topics = [
        ("İbadat:", "Namaz, oruç, zekât, hac (Bakara 43)"),
        ("Muamelat:", "Alışveriş, ticaret, kira, borç ilişkileri"),
        ("Münâkehat:", "Evlenme, boşanma, aile (Nisa 4)"),
        ("Ferâiz:", "Mirasın taksimi hükümleri (Nisa 8)"),
        ("Ukubat:", "Suçlar ve dünyevi cezalar (Bakara 66)"),
    ]
    for idx, (t, d) in enumerate(topics):
        y = 84 + idx * 25
        ic.append(f'<text x="332" y="{y}" font-size="9.5" font-weight="700" fill="#166534">• {t}</text>')
        ic.append(f'<text x="405" y="{y}" font-size="9" fill="#1e293b">{d}</text>')
    return svg(w, h, "".join(ic), "Klasik fıkıh tanımları ve fıkhın beş temel konusu")


def _gorsel_2():
    w, h = 620, 220
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#fffbeb" stroke="#fcd34d"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">FIKIH USULÜ VE FÜRU İLİŞKİSİ: DELİLDEN HÜKME ULAŞMA SÜRECİ</text>')
    steps = [
        (25, "1. ŞERİ DELİL (NAS)", "#eff6ff", "#3b82f6", "#1d4ed8", ["• Emir Ayeti: 'Namazı kılın...'", "  (Bakara suresi 43. ayet)", "• Yasaklama (Nehiy) Ayetleri:", "  İçki, kumar, faiz yasağı"]),
        (220, "2. FIKIH USULÜ KAİDESİ", "#faf5ff", "#a855f7", "#7e22ce", ["• 'Aksine delil olmadıkça emirler", "  gereklilik (vücup) ifade eder.'", "• 'Nehiy (yasaklama),", "  haramlık ifade eder.'"]),
        (415, "3. FÜRU (FIKHİ HÜKÜM)", "#f0fdf4", "#22c55e", "#15803d", ["• Sonuç 1: Namaz kılmak", "  FARZDIR.", "• Sonuç 2: İçki ve faiz", "  HARAMDIR."]),
    ]
    for x, title, bg, st, tc, lines in steps:
        ic.append(f'<rect x="{x}" y="48" width="180" height="148" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+90}" y="68" text-anchor="middle" font-size="10" font-weight="700" fill="{tc}">{title}</text>')
        for i, ln in enumerate(lines):
            ic.append(f'<text x="{x+10}" y="{92+i*22}" font-size="9" fill="#1e293b">{ln}</text>')
    ic.append('<path d="M206,122 L218,122" stroke="#92400e" stroke-width="2"/>')
    ic.append('<path d="M401,122 L413,122" stroke="#92400e" stroke-width="2"/>')
    return svg(w, h, "".join(ic), "Şeri delilden fıkıh usulü kaidesiyle füru hükmüne ulaşma şeması")


def _gorsel_3():
    w, h = 620, 235
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">FIKIH İLMİNİN 5 TEMEL İLKESİ (GRAFİK BİLGİ 1.4)</text>')
    items = [
        (22, 46, "1. GELİŞMEYE AÇIKLIK", "Değişmeyen ilahi emirler ile değişen", "hayat arasında köprü kurar", "#eff6ff", "#3b82f6", "#1d4ed8"),
        (220, 46, "2. TEKLİFLERDE KOLAYLIK", "Meşakkat, teysîri celbeder", "(Bakara 185, 286; kasr-ı salat)", "#f0fdf4", "#22c55e", "#15803d"),
        (418, 46, "3. KAMU YARARINI GÖZETMEK", "Zarar izale olunur; toplum yararı", "bireysel çıkarın önündedir", "#fffbeb", "#f59e0b", "#b45309"),
        (110, 134, "4. HELALLERDE GENİŞLİK", "Eşyada aslolan ibahadır (A'raf 157);", "yasaklanmayan temiz şeyler helaldir", "#ecfeff", "#06b6d4", "#0e7490"),
        (330, 134, "5. ADALETİ GÖZETMEK", "Emaneti ehline vermek (Nisa 58)", "ve tarafsız hükmetmek (Maide 8)", "#fdf2f8", "#ec4899", "#be185d"),
    ]
    for x, y, title, l1, l2, bg, st, tc in items:
        ic.append(f'<rect x="{x}" y="{y}" width="182" height="76" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+91}" y="{y+20}" text-anchor="middle" font-size="9.5" font-weight="700" fill="{tc}">{title}</text>')
        ic.append(f'<text x="{x+91}" y="{y+42}" text-anchor="middle" font-size="8.5" fill="#1e293b">{l1}</text>')
        ic.append(f'<text x="{x+91}" y="{y+58}" text-anchor="middle" font-size="8.5" font-weight="700" fill="#475569">{l2}</text>')
    return svg(w, h, "".join(ic), "Fıkıh ilminin beş temel ilkesi ve dayanak kaideleri")


def _gorsel_4():
    w, h = 620, 220
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">KAMU YARARI VE BİREYSEL HAK DENGESİ (MECELLE: "ZARAR İZALE OLUNUR")</text>')
    ic.append('<rect x="25" y="48" width="270" height="150" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>')
    ic.append('<text x="160" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b91c1c">TOPLUMA ZARAR VEREN DAVRANIŞLAR</text>')
    ic.append('<text x="36" y="90" font-size="9.5" fill="#1e293b">• Evin atık suyunu sokağa akıtmak</text>')
    ic.append('<text x="36" y="110" font-size="9.5" fill="#1e293b">• Ağaç dallarının yaya yolunu kapatması</text>')
    ic.append('<text x="36" y="130" font-size="9.5" fill="#1e293b">• İş yerinin kaldırımı işgal etmesi</text>')
    ic.append('<text x="36" y="150" font-size="9.5" fill="#1e293b">• Fabrikanın halk sağlığını tehdit etmesi</text>')
    ic.append('<rect x="36" y="162" width="248" height="26" rx="6" fill="#fee2e2"/>')
    ic.append('<text x="160" y="179" text-anchor="middle" font-size="9" font-weight="700" fill="#991b1b">Mülkiyet hakkı kamu yararıyla sınırlandırılır!</text>')

    ic.append('<rect x="320" y="48" width="275" height="150" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="457" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">FIKHİ ÇÖZÜM VE ADİL DENGE</text>')
    ic.append('<text x="332" y="92" font-size="9.5" fill="#1e293b">1. Kamu yararı ile bireysel menfaat</text>')
    ic.append('<text x="332" y="108" font-size="9.5" font-weight="700" fill="#166534">   çatıştığında KAMU YARARI tercih edilir.</text>')
    ic.append('<text x="332" y="132" font-size="9.5" fill="#1e293b">2. Ancak hak kaybına uğrayan ferdin</text>')
    ic.append('<text x="332" y="148" font-size="9.5" font-weight="700" fill="#166534">   zararı devletçe ADİL BEDELLE ödenir.</text>')
    ic.append('<rect x="332" y="162" width="250" height="26" rx="6" fill="#dcfce7"/>')
    ic.append('<text x="457" y="179" text-anchor="middle" font-size="9" font-weight="700" fill="#166534">Toplum + Birey Hakları Dengesi</text>')
    return svg(w, h, "".join(ic), "Kamu yararını gözetme ilkesi ve bireysel hak dengesi")


def uygula(v):
    gorseller = [_gorsel_1(), _gorsel_2(), _gorsel_3(), _gorsel_4(), None, None]
    for i, g in enumerate(gorseller):
        if g and i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
