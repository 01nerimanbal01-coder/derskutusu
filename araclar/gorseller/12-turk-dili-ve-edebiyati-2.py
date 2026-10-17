from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Giriş Ünitesi Metinlerinde Edebiyat - Felsefe ve Psikoloji İlişkisi</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">Edebiyat ve Felsefe İlişkisi</text>
    <text x="42" y="128" font-size="12" font-weight="bold" fill="#1e40af">• Âşık Veysel - "Yıllarca Aradım Kendi Kendimi"</text>
    <text x="42" y="148" font-size="12" fill="#1e3a8a">  Varlık, insan ve benlik sorgulaması</text>
    <text x="42" y="172" font-size="12" font-weight="bold" fill="#1e40af">• Oruç Aruoba - "Baharda" Şiiri</text>
    <text x="42" y="192" font-size="12" fill="#1e3a8a">  Oluş, varoluş ve zaman bilinci</text>
    <text x="42" y="218" font-size="12" font-weight="bold" fill="#1d4ed8">• İsmail Çetişli Ayrımı:</text>
    <text x="42" y="238" font-size="12" fill="#1e3a8a">  Felsefi dil: Araç (İçerik odaklı)</text>
    <text x="42" y="256" font-size="12" fill="#1e3a8a">  Edebî dil: Amaç ("Dil içinde üst dil")</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9d174d">Edebiyat, Psikoloji ve Psikiyatri</text>
    <text x="392" y="128" font-size="12" font-weight="bold" fill="#be185d">• Peyami Safa - "Dokuzuncu Hariciye Koğuşu"</text>
    <text x="392" y="148" font-size="12" fill="#831843">  Hasta gencin ruh hâli, "iki dikkatle</text>
    <text x="392" y="166" font-size="12" fill="#831843">  çalışan zihin", iç konuşma ve dalgınlık</text>
    <text x="392" y="192" font-size="12" font-weight="bold" fill="#be185d">• Sabahattin Ali - "Kürk Mantolu Madonna"</text>
    <text x="392" y="212" font-size="12" fill="#831843">  Portre karşısındaki ruhsal sarsıntı</text>
    <text x="392" y="238" font-size="12" font-weight="bold" fill="#9d174d">• Ortak Yön:</text>
    <text x="392" y="256" font-size="12" fill="#831843">  İnsanı çevresiyle bir "bütün" olarak ele alma</text>
    """
    return svg(720, 285, ic, "Edebiyatın Felsefe ve Psikoloji İle İlişkisi")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#065f46"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Dilin Tarihî Değişimini Etkileyen Sebepler (Tuncer Gülensoy - Dil-Millet Bağlantısı)</text>

    <rect x="30" y="75" width="315" height="195" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="187" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">1. İç Etkenler (Dilin Yapı ve İşleyişi)</text>
    <text x="48" y="130" font-size="12" fill="#064e3b">• Türkçe sondan eklemeli (iltisaklı) dildir.</text>
    <text x="48" y="152" font-size="12" fill="#064e3b">• Kökler değişmez, eklerle kelime türetilir.</text>
    <text x="48" y="178" font-size="12" font-weight="bold" fill="#047857">Tarihî Ses Değişimi Örnekleri:</text>
    <text x="48" y="200" font-size="12" fill="#064e3b">  • til → dil       • tag → dağ</text>
    <text x="48" y="222" font-size="12" fill="#064e3b">  • kül- → gül-     • imdi → şimdi</text>
    <text x="48" y="244" font-size="12" fill="#064e3b">  • çaruk → çarık</text>

    <rect x="375" y="75" width="315" height="195" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="532" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">2. Dış Etkenler (Tarihî ve Sosyal Şartlar)</text>
    <text x="393" y="128" font-size="12" fill="#78350f">• Din Değiştirmeler:</text>
    <text x="393" y="146" font-size="11" fill="#92400e">  VIII-IX. yy. Uygurlar (Budizm ve Manihaizm)</text>
    <text x="393" y="164" font-size="11" fill="#92400e">  X. yy. İslamiyet'in kabulü (Arapça ve Farsça)</text>
    <text x="393" y="188" font-size="12" fill="#78350f">• Göçler ve coğrafya değişiklikleri</text>
    <text x="393" y="210" font-size="12" fill="#78350f">• Ticari ve kültürel alışverişler, çeviriler</text>
    <text x="393" y="232" font-size="12" fill="#78350f">• Bilimsel ve teknolojik gelişmeler</text>
    <text x="532" y="256" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">"Dil toplumsal, söz bireyseldir." (Kemal Ateş)</text>
    """
    return svg(720, 285, ic, "Dilin Değişimini Etkileyen İç ve Dış Sebepler")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">11. Yüzyıldan 1900'e Türkçenin Tarihî Sözlükleri Zaman Çizelgesi</text>

    <rect x="20" y="75" width="160" height="90" rx="10" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="100" y="98" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">11. Yüzyıl</text>
    <text x="100" y="116" text-anchor="middle" font-size="11" font-weight="bold" fill="#6d28d9">Divanü Lugati't-Türk</text>
    <text x="100" y="134" text-anchor="middle" font-size="11" fill="#4c1d95">Kâşgarlı Mahmud</text>
    <text x="100" y="150" text-anchor="middle" font-size="10" fill="#4c1d95">(İlk sözlük + Harita)</text>

    <rect x="193" y="75" width="160" height="90" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="273" y="98" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">12. Yüzyıl</text>
    <text x="273" y="116" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">Mukaddimetü'l-Edeb</text>
    <text x="273" y="134" text-anchor="middle" font-size="11" fill="#1e3a8a">Zemahşerî</text>
    <text x="273" y="150" text-anchor="middle" font-size="10" fill="#1e3a8a">(Harezm / 4 dilli)</text>

    <rect x="366" y="75" width="160" height="90" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="446" y="98" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">14. Yüzyıl Sonu</text>
    <text x="446" y="116" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Codex Cumanicus</text>
    <text x="446" y="134" text-anchor="middle" font-size="11" fill="#14532d">Kuman-Kıpçak</text>
    <text x="446" y="150" text-anchor="middle" font-size="10" fill="#14532d">(Latin alfabesiyle)</text>

    <rect x="540" y="75" width="160" height="90" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="620" y="98" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">15. Yüzyıl</text>
    <text x="620" y="116" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">Muhâkemetü'l-Lugateyn</text>
    <text x="620" y="134" text-anchor="middle" font-size="11" fill="#78350f">Ali Şir Nevaî</text>
    <text x="620" y="150" text-anchor="middle" font-size="10" fill="#78350f">(Türkçe - Farsça)</text>

    <rect x="20" y="180" width="680" height="90" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="360" y="204" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b">Osmanlı Dönemi Sözlükçülüğü (18. - 19. Yüzyıl: Türkçeden Türkçeye)</text>
    <text x="360" y="226" text-anchor="middle" font-size="12" fill="#7f1d1d">• Mehmed Esad Efendi: Lehcetü'l-Lügat   |   • James W. Redhouse: Müntahabât-ı Türkiyye</text>
    <text x="360" y="248" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">• Ahmed Vefik Paşa: Lehce-i Osmânî (1876)   |   • Şemseddin Sami: Kâmûs-ı Türkî (1900)</text>
    """
    return svg(720, 285, ic, "İlk Örneklerden Osmanlı'ya Türkçenin Sözlükleri")


def gorsel_4():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Cumhuriyet Dönemi Sözlükçülüğü ve TDK Dijital Sözlük Ağı</text>

    <rect x="30" y="75" width="660" height="62" rx="10" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="360" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">1932: Türk Dili Tetkik Cemiyeti (TDK)  →  1945: Türkçe Sözlük (1. Baskı)</text>
    <text x="360" y="122" text-anchor="middle" font-size="12" fill="#134e4a">2002: Dijital Sözlük Uygulaması  →  2008: Büyük Türkçe Sözlük Veri Tabanı</text>

    <rect x="30" y="150" width="210" height="120" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="135" y="176" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">Güncel ve Sesli</text>
    <text x="135" y="198" text-anchor="middle" font-size="11" fill="#1e3a8a">• Güncel Türkçe Sözlük</text>
    <text x="135" y="218" text-anchor="middle" font-size="11" fill="#1e3a8a">• Sesli Türkçe Sözlük</text>
    <text x="135" y="238" text-anchor="middle" font-size="11" fill="#1e3a8a">• Parmak Alfabesi</text>
    <text x="135" y="256" text-anchor="middle" font-size="11" fill="#1e3a8a">• Atasözleri ve Deyimler</text>

    <rect x="255" y="150" width="210" height="120" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="360" y="176" text-anchor="middle" font-size="13" font-weight="bold" fill="#065f46">Tarihî ve Yöresel</text>
    <text x="360" y="198" text-anchor="middle" font-size="11" fill="#064e3b">• Tarama Sözlüğü</text>
    <text x="360" y="216" text-anchor="middle" font-size="10" fill="#064e3b">(13. yy.'dan beri yazılı metinler)</text>
    <text x="360" y="238" text-anchor="middle" font-size="11" fill="#064e3b">• Türkiye Türkçesi Ağızları</text>
    <text x="360" y="256" text-anchor="middle" font-size="11" fill="#064e3b">• Türk Lehçeleri Sözlüğü</text>

    <rect x="480" y="150" width="210" height="120" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="585" y="176" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309">Özel Alan Sözlükleri</text>
    <text x="585" y="198" text-anchor="middle" font-size="11" fill="#78350f">• Bilim ve Sanat Terimleri</text>
    <text x="585" y="218" text-anchor="middle" font-size="11" fill="#78350f">• Batı Kökenli Kelimeler</text>
    <text x="585" y="238" text-anchor="middle" font-size="11" fill="#78350f">• Eş ve Yakın Anlamlılar</text>
    <text x="585" y="256" text-anchor="middle" font-size="11" fill="#78350f">• Kişi Adları Sözlüğü</text>
    """
    return svg(720, 285, ic, "Cumhuriyet Dönemi ve TDK Dijital Sözlükleri")


def gorsel_5():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#7c2d12"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Dil Bilgisi: Çok Anlamlılık ("Ağır" ve "Çarık") ile Güncel Yazım Kuralları</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">Kelimede Anlam Genişlemesi</text>
    <text x="42" y="128" font-size="12" font-weight="bold" fill="#7c2d12">1. "Ağır" Sözcüğü (Emin Özdemir):</text>
    <text x="42" y="146" font-size="11" fill="#7c2d12">• Temel Anlam: Tartıda çok çeken</text>
    <text x="42" y="164" font-size="11" fill="#7c2d12">• Yan/Mecaz: Değerli, çetin, kırıcı, yavaş</text>
    <text x="42" y="192" font-size="12" font-weight="bold" fill="#7c2d12">2. "Çarık" Sözcüğü (DLT → TDK):</text>
    <text x="42" y="210" font-size="11" fill="#7c2d12">• 1. İşlenmemiş sığır derisinden ayakkabı</text>
    <text x="42" y="228" font-size="11" fill="#7c2d12">• 2. Tekerleği frenleyen demir levha (Yan)</text>
    <text x="42" y="246" font-size="11" fill="#7c2d12">• 4. Para cüzdanı (Argo)</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Dönem İmlası ve Güncel Yazım</text>
    <text x="392" y="130" font-size="12" fill="#475569">• birşeyler (Eski)  →  bir şeyler (Güncel)</text>
    <text x="392" y="152" font-size="12" fill="#475569">• yaştanberi (Eski) →  yaştan beri (Güncel)</text>
    <text x="392" y="174" font-size="12" fill="#475569">• öğe / lâmba (Eski) →  öge / lamba (Güncel)</text>
    <text x="392" y="196" font-size="12" fill="#475569">• M. S. (Eski)       →  MS (Güncel)</text>
    <rect x="392" y="212" width="286" height="44" rx="8" fill="#fee2e2"/>
    <text x="535" y="232" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">Önemli Noktalama Kuralı:</text>
    <text x="535" y="248" text-anchor="middle" font-size="11" fill="#7f1d1d">Tekrarlı bağlaçlardan (hem...hem) önce/sonra virgül konmaz!</text>
    """
    return svg(720, 285, ic, "Kelimede Çok Anlamlılık ve Yazım-Noktalama")


def gorsel_6():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Yazma Sürecinin 5 Aşaması ve Sözlü İletişimde Sunum İlkeleri</text>

    <rect x="20" y="75" width="128" height="75" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="84" y="102" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">1. Hazırlık</text>
    <text x="84" y="122" text-anchor="middle" font-size="10" fill="#3730a3">Okuma, gözlem</text>
    <text x="84" y="136" text-anchor="middle" font-size="10" fill="#3730a3">ve araştırma</text>

    <rect x="158" y="75" width="128" height="75" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="222" y="102" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">2. Planlama</text>
    <text x="222" y="122" text-anchor="middle" font-size="10" fill="#3730a3">Ana ve yardımcı</text>
    <text x="222" y="136" text-anchor="middle" font-size="10" fill="#3730a3">düşünce planı</text>

    <rect x="296" y="75" width="128" height="75" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="360" y="102" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">3. Taslak</text>
    <text x="360" y="122" text-anchor="middle" font-size="10" fill="#3730a3">Metni plana</text>
    <text x="360" y="136" text-anchor="middle" font-size="10" fill="#3730a3">göre yazma</text>

    <rect x="434" y="75" width="128" height="75" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="498" y="102" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">4. Düzeltme</text>
    <text x="498" y="122" text-anchor="middle" font-size="10" fill="#3730a3">Dil bilgisi ve</text>
    <text x="498" y="136" text-anchor="middle" font-size="10" fill="#3730a3">imla kontrolü</text>

    <rect x="572" y="75" width="128" height="75" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="636" y="102" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">5. Paylaşım</text>
    <text x="636" y="122" text-anchor="middle" font-size="10" fill="#3730a3">Pano veya</text>
    <text x="636" y="136" text-anchor="middle" font-size="10" fill="#3730a3">ağda yayım</text>

    <rect x="20" y="165" width="680" height="105" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="360" y="190" text-anchor="middle" font-size="14" font-weight="bold" fill="#15803d">Sözlü İletişim (Sunum) ve Yabancı Sözcüklere Türkçe Karşılıklar</text>
    <text x="360" y="214" text-anchor="middle" font-size="12" fill="#14532d">• Sunum Öncesi: Araştırma ve prova  |  • Sunum Sırası: Kısa cümle, doğru telaffuz, jest-mimik</text>
    <text x="360" y="236" text-anchor="middle" font-size="12" fill="#14532d">• Sunum Sonrası: Dinleyici sorularına tartışmaya girmeden kısa, açık ve net cevaplar verme</text>
    <text x="360" y="256" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Örnek: online → çevrim içi | trend → eğilim | start almak → başlamak | revize etmek → düzeltmek</text>
    """
    return svg(720, 285, ic, "Yazma Aşamaları ve Sözlü İletişim İlkeleri")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g