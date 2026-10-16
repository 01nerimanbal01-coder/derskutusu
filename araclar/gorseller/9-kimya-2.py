from ozet_gorsel import svg


def g1():
    w, h = 620, 235
    ic = [
        '<rect x="16" y="16" width="588" height="203" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">LABORATUVAR GÜVENLİK KURALLARI (4 TEMEL ALAN)</text>',
        '<rect x="30" y="58" width="270" height="68" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="165" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">1. Genel ve Kişisel Güvenlik</text>',
        '<text x="165" y="102" text-anchor="middle" font-size="12" fill="#334155">Önlük, gözlük ve eldiven giyilir;</text>',
        '<text x="165" y="118" text-anchor="middle" font-size="12" fill="#334155">kimyasal koklanmaz, tadına bakılmaz.</text>',
        '<rect x="320" y="58" width="270" height="68" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="455" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">2. Kimyasallarla Çalışma</text>',
        '<text x="455" y="102" text-anchor="middle" font-size="12" fill="#334155">Etiket okunur, pipetle puar kullanılır,</text>',
        '<text x="455" y="118" text-anchor="middle" font-size="12" fill="#334155">asit yavaşça suyun içine eklenir.</text>',
        '<rect x="30" y="138" width="270" height="68" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="165" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">3. Cam ve Ölçüm Araçları</text>',
        '<text x="165" y="182" text-anchor="middle" font-size="12" fill="#334155">Çatlak cam kullanılmaz; sıvı hacmi</text>',
        '<text x="165" y="198" text-anchor="middle" font-size="12" fill="#334155">beherglasla değil mezürle ölçülür.</text>',
        '<rect x="320" y="138" width="270" height="68" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="455" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">4. Atık ve Acil Durum</text>',
        '<text x="455" y="182" text-anchor="middle" font-size="12" fill="#334155">Atıklar lavaboya dökülmez; temasta</text>',
        '<text x="455" y="198" text-anchor="middle" font-size="12" fill="#334155">en az 15 dk bol suyla yıkanır.</text>',
    ]
    return svg(w, h, "".join(ic), "Laboratuvar güvenlik kuralları dört temel alan şeması")


def g2():
    w, h = 620, 240
    ic = [
        '<rect x="16" y="16" width="588" height="208" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">TEMEL GÜVENLİK UYARI İŞARETLERİ (RİSK PİKTOGRAMLARI)</text>',
        '<rect x="28" y="58" width="134" height="68" rx="9" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>',
        '<text x="95" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#be123c">Yanıcı / Parlayıcı</text>',
        '<text x="95" y="102" text-anchor="middle" font-size="12" fill="#334155">Alev simgesi;</text>',
        '<text x="95" y="117" text-anchor="middle" font-size="12" fill="#334155">ısıdan uzak tutulur</text>',
        '<rect x="172" y="58" width="134" height="68" rx="9" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>',
        '<text x="239" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#a16207">Oksitleyici</text>',
        '<text x="239" y="102" text-anchor="middle" font-size="12" fill="#334155">Halkalı alev; havasız</text>',
        '<text x="239" y="117" text-anchor="middle" font-size="12" fill="#334155">ortamda bile yakar</text>',
        '<rect x="316" y="58" width="134" height="68" rx="9" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>',
        '<text x="383" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1d4ed8">Korozif (Aşındırıcı)</text>',
        '<text x="383" y="102" text-anchor="middle" font-size="12" fill="#334155">Dokuyu tahrip eder,</text>',
        '<text x="383" y="117" text-anchor="middle" font-size="12" fill="#334155">metali aşındırır</text>',
        '<rect x="460" y="58" width="132" height="68" rx="9" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.4"/>',
        '<text x="526" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7e22ce">Zehirli (Toksik)</text>',
        '<text x="526" y="102" text-anchor="middle" font-size="12" fill="#334155">Kuru kafa; ağız, deri</text>',
        '<text x="526" y="117" text-anchor="middle" font-size="12" fill="#334155">ve solunumla zehirler</text>',
        '<rect x="28" y="138" width="134" height="68" rx="9" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.4"/>',
        '<text x="95" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#92400e">Tahriş Edici (!)</text>',
        '<text x="95" y="182" text-anchor="middle" font-size="12" fill="#334155">Deriye ve göze</text>',
        '<text x="95" y="197" text-anchor="middle" font-size="12" fill="#334155">zarar verir</text>',
        '<rect x="172" y="138" width="134" height="68" rx="9" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>',
        '<text x="239" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#15803d">Çevreye Zararlı</text>',
        '<text x="239" y="182" text-anchor="middle" font-size="12" fill="#334155">Toprak ve su</text>',
        '<text x="239" y="197" text-anchor="middle" font-size="12" fill="#334155">ekosistemini bozar</text>',
        '<rect x="316" y="138" width="134" height="68" rx="9" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.4"/>',
        '<text x="383" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0e7490">Basınçlı Gaz</text>',
        '<text x="383" y="182" text-anchor="middle" font-size="12" fill="#334155">Isınınca patlayabilir,</text>',
        '<text x="383" y="197" text-anchor="middle" font-size="12" fill="#334155">soğuk yanığı yapar</text>',
        '<rect x="460" y="138" width="132" height="68" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.4"/>',
        '<text x="526" y="162" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">Radyoaktif &amp; Tıbbi</text>',
        '<text x="526" y="182" text-anchor="middle" font-size="12" fill="#334155">Radyasyon hasarı ve</text>',
        '<text x="526" y="197" text-anchor="middle" font-size="12" fill="#334155">enfeksiyon riski</text>',
    ]
    return svg(w, h, "".join(ic), "Temel güvenlik uyarı işaretleri ve anlamları")


def g3():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">KİMYASAL MADDELERİN YANLIŞ KULLANIM RİSKLERİ</text>',
        '<rect x="30" y="60" width="180" height="128" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="120" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">Tuz Ruhu + Çamaşır Suyu</text>',
        '<text x="120" y="106" text-anchor="middle" font-size="12" fill="#334155">HCl ile NaClO karışımı</text>',
        '<text x="120" y="124" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">zehirli Klor gazı (Cl₂)</text>',
        '<text x="120" y="142" text-anchor="middle" font-size="12" fill="#334155">çıkarır; solunum</text>',
        '<text x="120" y="160" text-anchor="middle" font-size="12" fill="#334155">zehirlenmesine yol açar.</text>',
        '<rect x="220" y="60" width="180" height="128" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="310" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">Sodyum (Na) + Su</text>',
        '<text x="310" y="106" text-anchor="middle" font-size="12" fill="#334155">Yüksek reaktif alkali</text>',
        '<text x="310" y="124" text-anchor="middle" font-size="12" fill="#334155">metal olan sodyum</text>',
        '<text x="310" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">su ile şiddetli tepkime</text>',
        '<text x="310" y="160" text-anchor="middle" font-size="12" fill="#334155">ve patlama oluşturur.</text>',
        '<rect x="410" y="60" width="180" height="128" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="500" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">Cıva (Hg) Atıkları</text>',
        '<text x="500" y="106" text-anchor="middle" font-size="12" fill="#334155">Sıvı ağır metal besin</text>',
        '<text x="500" y="124" text-anchor="middle" font-size="12" fill="#334155">zinciriyle vücuda girer;</text>',
        '<text x="500" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">Minamata hastalığı</text>',
        '<text x="500" y="160" text-anchor="middle" font-size="12" fill="#334155">ve organ hasarı yapar.</text>',
    ]
    return svg(w, h, "".join(ic), "Kimyasal maddelerin yanlış kullanımından doğan başlıca tehlikeler")


def g4():
    w, h = 620, 235
    ic = [
        '<rect x="16" y="16" width="588" height="203" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">TEMEL LABORATUVAR MALZEMELERİ VE GÖREVLERİ</text>',
        '<rect x="30" y="58" width="176" height="68" rx="9" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>',
        '<text x="118" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">Balon Joje</text>',
        '<text x="118" y="102" text-anchor="middle" font-size="12" fill="#334155">Belli derişimde</text>',
        '<text x="118" y="118" text-anchor="middle" font-size="12" fill="#334155">çözelti hazırlama</text>',
        '<rect x="222" y="58" width="176" height="68" rx="9" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>',
        '<text x="310" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">Büret &amp; Erlenmayer</text>',
        '<text x="310" y="102" text-anchor="middle" font-size="12" fill="#334155">Titrasyon ve derişim</text>',
        '<text x="310" y="118" text-anchor="middle" font-size="12" fill="#334155">belirleme işlemi</text>',
        '<rect x="414" y="58" width="176" height="68" rx="9" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>',
        '<text x="502" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">Mezür &amp; Pipet</text>',
        '<text x="502" y="102" text-anchor="middle" font-size="12" fill="#334155">Sıvıların hacmini</text>',
        '<text x="502" y="118" text-anchor="middle" font-size="12" fill="#334155">doğru ölçme/aktarma</text>',
        '<rect x="30" y="138" width="176" height="68" rx="9" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.4"/>',
        '<text x="118" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">Ayırma Hunisi</text>',
        '<text x="118" y="182" text-anchor="middle" font-size="12" fill="#334155">Heterojen sıvı-sıvı</text>',
        '<text x="118" y="198" text-anchor="middle" font-size="12" fill="#334155">karışımları ayırma</text>',
        '<rect x="222" y="138" width="176" height="68" rx="9" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>',
        '<text x="310" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">Soğutucu</text>',
        '<text x="310" y="182" text-anchor="middle" font-size="12" fill="#334155">Buharlaşan çözücüyü</text>',
        '<text x="310" y="198" text-anchor="middle" font-size="12" fill="#334155">yoğunlaştırma</text>',
        '<rect x="414" y="138" width="176" height="68" rx="9" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.4"/>',
        '<text x="502" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0e7490">Kroze &amp; Amyant Tel</text>',
        '<text x="502" y="182" text-anchor="middle" font-size="12" fill="#334155">Yüksek ısıda yakma</text>',
        '<text x="502" y="198" text-anchor="middle" font-size="12" fill="#334155">ve eşit ısı dağıtımı</text>',
    ]
    return svg(w, h, "".join(ic), "Kimya laboratuvarında kullanılan temel malzemeler ve görevleri")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[3]["gorsel"] = g3()
    b[4]["gorsel"] = g4()
