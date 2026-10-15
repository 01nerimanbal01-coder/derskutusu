from ozet_gorsel import svg


def g1():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">RİSALET (İLAHİ ELÇİLİK) SÜRECİ</text>',
        '<rect x="34" y="64" width="160" height="118" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="114" y="92" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">YÜCE ALLAH (CC)</text>',
        '<text x="114" y="118" text-anchor="middle" font-size="12" fill="#334155">İlahi seçimle elçiyi</text>',
        '<text x="114" y="136" text-anchor="middle" font-size="12" fill="#334155">belirler ve vahiy</text>',
        '<text x="114" y="154" text-anchor="middle" font-size="12" fill="#334155">gönderir (En’âm 124)</text>',
        '<line x1="196" y1="123" x2="226" y2="123" stroke="#2563eb" stroke-width="2"/>',
        '<polygon points="228,123 220,118 220,128" fill="#2563eb"/>',
        '<rect x="230" y="64" width="160" height="118" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="92" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">PEYGAMBER</text>',
        '<text x="310" y="118" text-anchor="middle" font-size="12" fill="#334155">Nebi / Resul</text>',
        '<text x="310" y="136" text-anchor="middle" font-size="12" fill="#334155">Vahyi tebliğ eder ve</text>',
        '<text x="310" y="154" text-anchor="middle" font-size="12" fill="#334155">yaşayarak açıklar</text>',
        '<line x1="392" y1="123" x2="422" y2="123" stroke="#16a34a" stroke-width="2"/>',
        '<polygon points="424,123 416,118 416,128" fill="#16a34a"/>',
        '<rect x="426" y="64" width="160" height="118" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="506" y="92" text-anchor="middle" font-size="14" font-weight="700" fill="#a16207">İNSANLIK</text>',
        '<text x="506" y="118" text-anchor="middle" font-size="12" fill="#334155">Kendi içinden seçilen</text>',
        '<text x="506" y="136" text-anchor="middle" font-size="12" fill="#334155">elçiyi anlar ve</text>',
        '<text x="506" y="154" text-anchor="middle" font-size="12" fill="#334155">örnek alır</text>',
    ]
    return svg(w, h, "".join(ic), "Risalet ve ilahi elçilik süreci şeması")


def g2():
    w, h = 620, 240
    ic = [
        '<rect x="16" y="16" width="588" height="208" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">PEYGAMBERLERİN TEMEL ÖZELLİKLERİ</text>',
        '<rect x="32" y="58" width="174" height="68" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="119" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">1. İlahi Seçim</text>',
        '<text x="119" y="106" text-anchor="middle" font-size="12" fill="#334155">Allah tarafından seçilmek</text>',
        '<rect x="223" y="58" width="174" height="68" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">2. Vahiy ve Tebliğ</text>',
        '<text x="310" y="106" text-anchor="middle" font-size="12" fill="#334155">Vahiy alıp duyurmak</text>',
        '<rect x="414" y="58" width="174" height="68" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="501" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">3. Mucize Göstermek</text>',
        '<text x="501" y="106" text-anchor="middle" font-size="12" fill="#334155">Allah’ın izniyle kanıt</text>',
        '<rect x="32" y="140" width="174" height="68" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="119" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">4. Beşerî Nitelikler</text>',
        '<text x="119" y="188" text-anchor="middle" font-size="12" fill="#334155">İnsani özellikler taşımak</text>',
        '<rect x="223" y="140" width="174" height="68" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="310" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">5. Doğruluk ve Güven</text>',
        '<text x="310" y="188" text-anchor="middle" font-size="12" fill="#334155">Doğru sözlü ve emin olmak</text>',
        '<rect x="414" y="140" width="174" height="68" rx="10" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.5"/>',
        '<text x="501" y="166" text-anchor="middle" font-size="13" font-weight="700" fill="#0e7490">6. Günahlardan Korunma</text>',
        '<text x="501" y="188" text-anchor="middle" font-size="12" fill="#334155">Günahtan korunmuş olmak</text>',
    ]
    return svg(w, h, "".join(ic), "Peygamberlerin altı temel özelliği şeması")


def g3():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">NEBİ VE RESUL KAVRAMLARI</text>',
        '<rect x="34" y="60" width="265" height="92" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">NEBİ (Çoğulu: Enbiya)</text>',
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">Allah’ın vahyettiği hakikatleri</text>',
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">olduğu gibi insanlara aktaran ve</text>',
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">vahye itaate çağıran peygamberdir.</text>',
        '<rect x="321" y="60" width="265" height="92" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">RESUL</text>',
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">Kendisine yeni bir kitap verilen,</text>',
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">dinî ve toplumsal hayatı ilahi</text>',
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">emirlere göre düzenleyen elçidir.</text>',
        '<rect x="34" y="162" width="552" height="34" rx="8" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.2"/>',
        '<text x="310" y="184" text-anchor="middle" font-size="12.5" font-weight="700" fill="#92400e">Hz. Muhammed (sav): Hem nebi hem resuldür ve nebilerin sonuncusudur (Ahzâb 40).</text>',
    ]
    return svg(w, h, "".join(ic), "Nebi ve resul kavramları karşılaştırma tablosu")


def g4():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">DÖRT BÜYÜK İLAHİ KİTAP VE PEYGAMBERLERİ</text>',
        '<rect x="30" y="64" width="132" height="118" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="96" y="96" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">TEVRAT</text>',
        '<line x1="50" y1="112" x2="142" y2="112" stroke="#bfdbfe" stroke-width="1.5"/>',
        '<text x="96" y="142" text-anchor="middle" font-size="13" font-weight="600" fill="#334155">Hz. Musa (as)</text>',
        '<rect x="172" y="64" width="132" height="118" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="238" y="96" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">ZEBUR</text>',
        '<line x1="192" y1="112" x2="284" y2="112" stroke="#bbf7d0" stroke-width="1.5"/>',
        '<text x="238" y="142" text-anchor="middle" font-size="13" font-weight="600" fill="#334155">Hz. Davud (as)</text>',
        '<rect x="314" y="64" width="132" height="118" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="380" y="96" text-anchor="middle" font-size="14" font-weight="700" fill="#7e22ce">İNCİL</text>',
        '<line x1="334" y1="112" x2="426" y2="112" stroke="#e9d5ff" stroke-width="1.5"/>',
        '<text x="380" y="142" text-anchor="middle" font-size="13" font-weight="600" fill="#334155">Hz. İsa (as)</text>',
        '<rect x="456" y="64" width="134" height="118" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="523" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">KUR’AN-I KERİM</text>',
        '<line x1="476" y1="112" x2="570" y2="112" stroke="#fef08a" stroke-width="1.5"/>',
        '<text x="523" y="138" text-anchor="middle" font-size="12.5" font-weight="600" fill="#334155">Hz. Muhammed</text>',
        '<text x="523" y="156" text-anchor="middle" font-size="12.5" font-weight="600" fill="#334155">(sav)</text>',
    ]
    return svg(w, h, "".join(ic), "Dört büyük ilahi kitap ve gönderildiği peygamberler")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
