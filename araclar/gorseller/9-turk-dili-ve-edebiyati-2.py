from ozet_gorsel import svg


def g1():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">EDEBÎ METİN İLE ÖĞRETİCİ METİN KARŞILAŞTIRMASI</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">EDEBÎ METİN (Kurmaca)</text>',
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">• Örnek: Çanakkale Şehitlerine (Şiir)</text>',
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">• Gerçekliği kurgulayarak dönüştürür.</text>',
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">• Özneldir, imge ve söz sanatı içerir.</text>',
        '<text x="166" y="160" text-anchor="middle" font-size="12" fill="#334155">• Her okurda farklı çağrışım uyandırır.</text>',
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">ÖĞRETİCİ METİN (Bilgi Verici)</text>',
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">• Örnek: Çanakkale Savaşları (Madde)</text>',
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">• Dış gerçekliği değiştirmeden aktarır.</text>',
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">• Nesneldir, kanıtlanabilir bilgi sunar.</text>',
        '<text x="453" y="160" text-anchor="middle" font-size="12" fill="#334155">• Bütün okurlar aynı anlamı çıkarır.</text>',
    ]
    return svg(w, h, "".join(ic), "Edebî metin ile öğretici metin karşılaştırma şeması")


def g2():
    w, h = 620, 240
    ic = [
        '<rect x="16" y="16" width="588" height="208" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">ŞİİRDE BAŞLICA EDEBÎ SANATLAR (SÖZ SANATLARI)</text>',
        '<rect x="30" y="58" width="176" height="68" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="118" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">Teşbih &amp; İstiare</text>',
        '<text x="118" y="102" text-anchor="middle" font-size="12" fill="#334155">Ana sütü gibi türkü</text>',
        '<text x="118" y="118" text-anchor="middle" font-size="12" fill="#334155">Damla damla eriyen gün</text>',
        '<rect x="222" y="58" width="176" height="68" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">Teşhis &amp; İntak</text>',
        '<text x="310" y="102" text-anchor="middle" font-size="12" fill="#334155">Kişileştirme ve</text>',
        '<text x="310" y="118" text-anchor="middle" font-size="12" fill="#334155">“Allah deyü” konuşturma</text>',
        '<rect x="414" y="58" width="176" height="68" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="502" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">Mecazımürsel &amp; Tezat</text>',
        '<text x="502" y="102" text-anchor="middle" font-size="12" fill="#334155">Hilâl → Türk bayrağı</text>',
        '<text x="502" y="118" text-anchor="middle" font-size="12" fill="#334155">Hürriyet ↔ Esaret</text>',
        '<rect x="30" y="138" width="176" height="68" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="118" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">Tenasüp &amp; Telmih</text>',
        '<text x="118" y="182" text-anchor="middle" font-size="12" fill="#334155">Su, bahçıvan, gül</text>',
        '<text x="118" y="198" text-anchor="middle" font-size="12" fill="#334155">Leyla ile Mecnun</text>',
        '<rect x="222" y="138" width="176" height="68" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="310" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">Hüsnütalil</text>',
        '<text x="310" y="182" text-anchor="middle" font-size="12" fill="#334155">Bulutlara hayretinden</text>',
        '<text x="310" y="198" text-anchor="middle" font-size="12" fill="#334155">yeşeren ağaçlar</text>',
        '<rect x="414" y="138" width="176" height="68" rx="10" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.5"/>',
        '<text x="502" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0e7490">Tecahülüarif</text>',
        '<text x="502" y="182" text-anchor="middle" font-size="12" fill="#334155">Taşın sert olduğunu</text>',
        '<text x="502" y="198" text-anchor="middle" font-size="12" fill="#334155">bilmezlikten gelme</text>',
    ]
    return svg(w, h, "".join(ic), "Şiirde başlıca edebî sanatlar ve dize örnekleri")


def g3():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">SAKARYA TÜRKÜSÜ’NDE AÇIK VE ÖRTÜK İLETİ</text>',
        '<rect x="34" y="58" width="552" height="36" rx="8" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.2"/>',
        '<text x="310" y="81" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">Dize: “İnsan bu, su misali, kıvrım kıvrım akar ya; / Bir yanda akan benim, öbür yanda Sakarya.”</text>',
        '<rect x="34" y="106" width="264" height="82" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="130" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">AÇIK İLETİ (Doğrudan Anlam)</text>',
        '<text x="166" y="152" text-anchor="middle" font-size="12" fill="#334155">Dış dünyadaki gerçeklik:</text>',
        '<text x="166" y="170" text-anchor="middle" font-size="12" fill="#334155">Sakarya Nehri’nin akıp gitmesi</text>',
        '<rect x="322" y="106" width="264" height="82" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="454" y="130" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">ÖRTÜK İLETİ (Sezdirilen Anlam)</text>',
        '<text x="454" y="152" text-anchor="middle" font-size="12" fill="#334155">İmge ve çıkarım yoluyla:</text>',
        '<text x="454" y="170" text-anchor="middle" font-size="12" fill="#334155">İnsan ömrünün ve tarihin hızla akması</text>',
    ]
    return svg(w, h, "".join(ic), "Sakarya Türküsü dizesinde açık ve örtük ileti")


def g4():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">DENEME METİNLERİNDE ANLAM OLUŞTURMA</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">Picasso’nun Hatları (R. Özdenören)</text>',
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">• Konu: Gelenekten yararlanma</text>',
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">• Yardımcı fikir: Picasso hatları</text>',
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">yalnız malzeme olarak kullanmıştır.</text>',
        '<text x="166" y="160" text-anchor="middle" font-size="12" fill="#334155">• Ana fikir: Geleneğin ruhu kavranmalı.</text>',
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">Canım Kitap (S. Kemal Yetkin)</text>',
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">• Konu: Kitap ve okuma sevgisi</text>',
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">• Karşılaştırma: Fikir ve sanat eseri</text>',
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">• Tanık gösterme: Nurullah Ataç</text>',
        '<text x="453" y="160" text-anchor="middle" font-size="12" fill="#334155">• Ana fikir: Kitap en yakın dosttur.</text>',
    ]
    return svg(w, h, "".join(ic), "Picasso'nun Hatları ve Canım Kitap denemelerinde anlam yapısı")


def uygula(v):
    b = v["bolumler"]
    b[1]["gorsel"] = g1()
    b[3]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
