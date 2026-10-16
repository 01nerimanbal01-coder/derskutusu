from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 225
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">İSLAM’DA BİLGİ, İNANÇ VE DAVRANIŞ BÜTÜNLÜĞÜ</text>')
    boxes = [
        (25, "1. DOĞRU BİLGİ", "#eff6ff", "#3b82f6", "#1d4ed8", ["• Kaynak: Sadık haber, selim akıl,", "  salim duyular", "• Bakara 31-32: İsimlerin öğretilmesi", "• Zümer 9: Bilenle bilmeyen bir olmaz", "• En'am 116: Zandan sakınma"]),
        (220, "2. DOĞRU İNANÇ", "#f0fdf4", "#22c55e", "#15803d", ["• Yaratıcıyı delillerle tanıma", "• İnanılması gereken ilkeleri bilme", "• Kör taklitten (Bakara 170) uzaklaşma", "• Gayb ve şehadet âlemini kavrama"]),
        (415, "3. DOĞRU DAVRANIŞ", "#fffbeb", "#f59e0b", "#b45309", ["• Sorumluluk (mükellefiyet) bilinci", "• İlmi insanlık yararına kullanma", "• Salih amel ve güzel ahlak", "• Âlimler: Peygamberlerin varisleri"]),
    ]
    for x, title, bg, st, tc, lines in boxes:
        ic.append(f'<rect x="{x}" y="48" width="180" height="152" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+90}" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="{tc}">{title}</text>')
        for i, ln in enumerate(lines):
            ic.append(f'<text x="{x+10}" y="{90+i*22}" font-size="9" fill="#1e293b">{ln}</text>')
    ic.append('<path d="M206,124 L218,124" stroke="#475569" stroke-width="2"/>')
    ic.append('<path d="M401,124 L413,124" stroke="#475569" stroke-width="2"/>')
    return svg(w, h, "".join(ic), "Doğru bilgi, doğru inanç ve doğru davranış zinciri")


def _gorsel_2():
    w, h = 620, 225
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">MUAZ BİN CEBEL (RA) HADİSİ VE GAŞİYE SURESİ 17-20 ANALİZİ</text>')
    # Sol: Muaz bin Cebel
    ic.append('<rect x="25" y="46" width="275" height="156" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>')
    ic.append('<text x="162" y="66" text-anchor="middle" font-size="10.5" font-weight="700" fill="#1e40af">MUAZ BİN CEBEL HADİSİNDE HÜKÜM SIRASI</text>')
    ic.append('<rect x="40" y="76" width="245" height="32" rx="6" fill="#dbeafe"/>')
    ic.append('<text x="162" y="96" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1e3a8a">1. Adım: Allah’ın Kitabı (Kur’an / Vahiy)</text>')
    ic.append('<rect x="40" y="116" width="245" height="32" rx="6" fill="#dbeafe"/>')
    ic.append('<text x="162" y="136" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1e3a8a">2. Adım: Resulullah’ın Sünneti</text>')
    ic.append('<rect x="40" y="156" width="245" height="32" rx="6" fill="#dbeafe"/>')
    ic.append('<text x="162" y="176" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1e3a8a">3. Adım: Kendi Görüşüyle İçtihat (Selim Akıl)</text>')
    # Sağ: Gaşiye 17-20
    ic.append('<rect x="315" y="46" width="280" height="156" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="455" y="66" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">GAŞİYE 17-20: GÖZLEM VE TEFEKKÜR</text>')
    ic.append('<text x="328" y="90" font-size="9.5" fill="#1e293b">• Devenin nasıl yaratıldığına,</text>')
    ic.append('<text x="328" y="110" font-size="9.5" fill="#1e293b">• Göğün nasıl yükseltildiğine,</text>')
    ic.append('<text x="328" y="130" font-size="9.5" fill="#1e293b">• Dağların nasıl dikildiğine,</text>')
    ic.append('<text x="328" y="150" font-size="9.5" fill="#1e293b">• Yeryüzünün nasıl yayıldığına bakmak:</text>')
    ic.append('<rect x="328" y="162" width="254" height="28" rx="6" fill="#dcfce7"/>')
    ic.append('<text x="455" y="180" text-anchor="middle" font-size="9.5" font-weight="700" fill="#166534">Salim Duyular (Gözlem) + Selim Akıl (Tefekkür)</text>')
    return svg(w, h, "".join(ic), "Muaz bin Cebel hadisi ve Gaşiye suresi 17-20. ayetlerde bilgi kaynakları")


def _gorsel_3():
    w, h = 620, 230
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">İSLAM DÜŞÜNCESİNDE BİLGİ KAYNAKLARININ SINIFLANDIRILMASI</text>')
    # Nesnel
    ic.append('<rect x="22" y="45" width="380" height="165" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>')
    ic.append('<text x="212" y="65" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">NESNEL BİLGİ KAYNAKLARI (Genelgeçer / Bağlayıcı)</text>')
    ic.append('<rect x="34" y="76" width="172" height="122" rx="8" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="120" y="94" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">1. SADIK HABER</text>')
    ic.append('<text x="42" y="114" font-size="9" font-weight="700" fill="#1d4ed8">a) Haberiresul (Vahiy):</text>')
    ic.append('<text x="42" y="128" font-size="8.5" fill="#334155">Peygamberlerin getirdiği ilahi bilgi</text>')
    ic.append('<text x="42" y="148" font-size="9" font-weight="700" fill="#1d4ed8">b) Mütevatir Haber:</text>')
    ic.append('<text x="42" y="162" font-size="8.5" fill="#334155">Yalan üzere birleşemeyecek</text>')
    ic.append('<text x="42" y="175" font-size="8.5" fill="#334155">topluluğun kesintisiz aktarımı</text>')
    ic.append('<rect x="216" y="76" width="174" height="56" rx="8" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="303" y="94" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">2. SELİM AKIL</text>')
    ic.append('<text x="224" y="110" font-size="8.5" fill="#334155">Temizliğini koruyan, doğru hüküm</text>')
    ic.append('<text x="224" y="123" font-size="8.5" fill="#334155">veren akıl (Sorumluluk şartı)</text>')
    ic.append('<rect x="216" y="142" width="174" height="56" rx="8" fill="#ffffff" stroke="#93c5fd"/>')
    ic.append('<text x="303" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">3. SALİM DUYULAR</text>')
    ic.append('<text x="224" y="176" font-size="8.5" fill="#334155">Özelliğini yitirmemiş 5 duyu</text>')
    ic.append('<text x="224" y="189" font-size="8.5" fill="#334155">(Nahl 78: Kulaklar ve gözler)</text>')
    # Öznel
    ic.append('<rect x="414" y="45" width="184" height="165" rx="10" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>')
    ic.append('<text x="506" y="65" text-anchor="middle" font-size="10.5" font-weight="700" fill="#be123c">ÖZNEL KAYNAKLAR</text>')
    ic.append('<text x="426" y="88" font-size="9.5" fill="#1e293b">• Sezgi ve İlham</text>')
    ic.append('<text x="426" y="108" font-size="9.5" fill="#1e293b">• Rüya ve Keşif</text>')
    ic.append('<text x="426" y="128" font-size="9.5" fill="#1e293b">• Bireysel / Çevresel Tecrübe</text>')
    ic.append('<rect x="424" y="144" width="164" height="54" rx="6" fill="#ffe4e6"/>')
    ic.append('<text x="506" y="162" text-anchor="middle" font-size="8.5" font-weight="700" fill="#9f1239">Kesin bilgi kaynağı değildir;</text>')
    ic.append('<text x="506" y="176" text-anchor="middle" font-size="8.5" font-weight="700" fill="#9f1239">herkesi bağlamaz, teyit gerekir.</text>')
    return svg(w, h, "".join(ic), "Nesnel ve öznel bilgi kaynaklarının sınıflandırılması")


def _gorsel_4():
    w, h = 620, 235
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">ALTI TEMEL BİLGİ TÜRÜ VE ELDE EDİLİŞ YOLLARI</text>')
    items = [
        (25, 46, "1. GÜNDELİK BİLGİ", "Günlük tecrübe yoluyla", "Sistematik değildir, hayatı kolaylaştırır", "#eff6ff", "#3b82f6", "#1d4ed8"),
        (220, 46, "2. DİNÎ BİLGİ", "Vahiy (Kur'an ve Sünnet)", "İnananlar için kesin ve değişmezdir", "#f0fdf4", "#22c55e", "#15803d"),
        (415, 46, "3. TEKNİK BİLGİ", "Doğadan yararlanma / Uygulama", "Teknolojik ürün üretir, iş gücünü azaltır", "#fffbeb", "#f59e0b", "#b45309"),
        (25, 134, "4. SANATSAL BİLGİ", "Duygu, yetenek ve gözlem", "Özneldir, estetik duyarlılığa hitap eder", "#fdf2f8", "#ec4899", "#be185d"),
        (220, 134, "5. BİLİMSEL BİLGİ", "Sistemli deney ve gözlem", "Evrenseldir; yeni keşiflerle değişebilir", "#ecfeff", "#06b6d4", "#0e7490"),
        (415, 134, "6. FELSEFİ BİLGİ", "Akıl ve mantıkla sorgulama", "Varlığı ve insanı eleştirel temellendirir", "#faf5ff", "#a855f7", "#7e22ce"),
    ]
    for x, y, title, via, prop, bg, st, tc in items:
        ic.append(f'<rect x="{x}" y="{y}" width="180" height="76" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+90}" y="{y+20}" text-anchor="middle" font-size="10" font-weight="700" fill="{tc}">{title}</text>')
        ic.append(f'<text x="{x+90}" y="{y+40}" text-anchor="middle" font-size="9" font-weight="700" fill="#1e293b">{via}</text>')
        ic.append(f'<text x="{x+90}" y="{y+58}" text-anchor="middle" font-size="8.5" fill="#475569">{prop}</text>')
    return svg(w, h, "".join(ic), "Altı temel bilgi türü ve özellikleri şeması")


def uygula(v):
    gorseller = [_gorsel_1(), _gorsel_2(), _gorsel_3(), None, None, _gorsel_4()]
    for i, g in enumerate(gorseller):
        if g and i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
