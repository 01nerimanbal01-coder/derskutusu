from ozet_gorsel import svg


def _hadis_cesitleri():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">İçeriğine Göre Hadis Çeşitleri ve Şemail</text>'
        '<rect x="18" y="40" width="150" height="175" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="93" y="64" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">Kavlî Hadis</text>'
        '<text x="93" y="88" text-anchor="middle" font-size="10.5" font-weight="700" class="g-y">Sözlü Buyruklar</text>'
        '<text x="93" y="114" text-anchor="middle" font-size="10" class="g-y">"Resulullah şöyle</text>'
        '<text x="93" y="130" text-anchor="middle" font-size="10" class="g-y">buyurdu..."</text>'
        '<rect x="28" y="150" width="130" height="50" rx="6" fill="#fff"/>'
        '<text x="93" y="170" text-anchor="middle" font-size="9.5" class="g-y">Kişinin kendini</text>'
        '<text x="93" y="185" text-anchor="middle" font-size="9.5" class="g-y">ilgilendirmeyeni terk etmesi</text>'
        '<rect x="182" y="40" width="150" height="175" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="257" y="64" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">Fiilî Hadis</text>'
        '<text x="257" y="88" text-anchor="middle" font-size="10.5" font-weight="700" class="g-y">Uygulama ve Davranış</text>'
        '<text x="257" y="114" text-anchor="middle" font-size="10" class="g-y">"Resulullah şöyle</text>'
        '<text x="257" y="130" text-anchor="middle" font-size="10" class="g-y">yapardı..."</text>'
        '<rect x="192" y="150" width="130" height="50" rx="6" fill="#fff"/>'
        '<text x="257" y="170" text-anchor="middle" font-size="9.5" class="g-y">Günah olmadıkça iki işten</text>'
        '<text x="257" y="185" text-anchor="middle" font-size="9.5" class="g-y">kolay olanı seçmesi</text>'
        '<rect x="346" y="40" width="150" height="175" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="421" y="64" text-anchor="middle" font-size="12.5" font-weight="800" class="g-sf">Takrirî Hadis</text>'
        '<text x="421" y="88" text-anchor="middle" font-size="10.5" font-weight="700" class="g-y">Onay ve Uygun Bulma</text>'
        '<text x="421" y="114" text-anchor="middle" font-size="10" class="g-y">Açıkça övmesi veya</text>'
        '<text x="421" y="130" text-anchor="middle" font-size="10" class="g-y">itiraz etmemesi</text>'
        '<rect x="356" y="150" width="130" height="50" rx="6" fill="#fff"/>'
        '<text x="421" y="170" text-anchor="middle" font-size="9.5" class="g-y">Rükû sonrası dua eden</text>'
        '<text x="421" y="185" text-anchor="middle" font-size="9.5" class="g-y">sahabiyi onaylaması</text>'
        '<rect x="510" y="40" width="152" height="175" rx="10" class="g-moa" stroke="#7e22ce" stroke-width="1.5"/>'
        '<text x="586" y="64" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mof">Şemail ve Hilye</text>'
        '<text x="586" y="88" text-anchor="middle" font-size="10.5" font-weight="700" class="g-y">Fiziksel &amp; Ahlaki Yapı</text>'
        '<text x="586" y="114" text-anchor="middle" font-size="10" class="g-y">"Onun ahlakı Kur\'an\'dı"</text>'
        '<text x="586" y="130" text-anchor="middle" font-size="10" class="g-y">"Orta boyluydu"</text>'
        '<rect x="520" y="150" width="132" height="50" rx="6" fill="#fff"/>'
        '<text x="586" y="170" text-anchor="middle" font-size="9.5" class="g-y">Hat levhası hâline</text>'
        '<text x="586" y="185" text-anchor="middle" font-size="9.5" class="g-y">Hilye-i Şerif denir</text>'
    )
    return svg(680, 228, ic, "Kavlî, fiilî, takrirî hadisler ve şemail-hilye şeması")


def _sunnet_kapsami():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Sünnet Kavramının İlim Dallarına Göre Kullanımı</text>'
        '<rect x="24" y="42" width="300" height="156" rx="12" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="174" y="68" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">Hadis İlminde Sünnet</text>'
        '<text x="174" y="94" text-anchor="middle" font-size="11" class="g-y">Hz. Peygamber\'in söz, fiil ve</text>'
        '<text x="174" y="112" text-anchor="middle" font-size="11" class="g-y">takrirlerinin tamamını kapsar.</text>'
        '<rect x="44" y="128" width="260" height="52" rx="8" fill="#fff"/>'
        '<text x="174" y="149" text-anchor="middle" font-size="10.5" font-weight="700" class="g-mf">Hadis = Sünnet (Eş Anlamlı)</text>'
        '<text x="174" y="168" text-anchor="middle" font-size="10" class="g-y">Çoğulu: Sünen (Ebu Davud\'un eseri vb.)</text>'
        '<rect x="356" y="42" width="300" height="156" rx="12" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="506" y="68" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">Fıkıh İlminde Sünnet</text>'
        '<text x="506" y="94" text-anchor="middle" font-size="11" class="g-y">Farz ve vacip dışında dinen</text>'
        '<text x="506" y="112" text-anchor="middle" font-size="11" class="g-y">yapılması tavsiye edilen fiillerdir.</text>'
        '<rect x="376" y="128" width="260" height="52" rx="8" fill="#fff"/>'
        '<text x="506" y="149" text-anchor="middle" font-size="10.5" font-weight="700" class="g-yf">Daha Dar ve Özel Anlam</text>'
        '<text x="506" y="168" text-anchor="middle" font-size="10" class="g-y">Kesin bağlayıcı olmayan nebevi uygulamalar</text>'
    )
    return svg(680, 212, ic, "Hadis ve fıkıh ilimlerinde sünnet kavramı")


def _senet_zinciri():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Senet (İsnat) Zinciri Örneği: Hz. Peygamber\'den Tirmizî\'ye</text>'
        '<rect x="20" y="46" width="136" height="44" rx="8" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="88" y="66" text-anchor="middle" font-size="11" font-weight="800" class="g-yf">Resulullah (sav)</text>'
        '<text x="88" y="81" text-anchor="middle" font-size="9.5" class="g-y">Hadisin Kaynağı</text>'
        '<text x="168" y="72" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="180" y="46" width="136" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="248" y="66" text-anchor="middle" font-size="11" font-weight="800" class="g-mf">Ebu Zer (ra)</text>'
        '<text x="248" y="81" text-anchor="middle" font-size="9.5" class="g-y">1. Ravi (Sahabi)</text>'
        '<text x="328" y="72" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="340" y="46" width="150" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="415" y="66" text-anchor="middle" font-size="10.5" font-weight="800" class="g-mf">Meymun b. Ebu Şeybe</text>'
        '<text x="415" y="81" text-anchor="middle" font-size="9.5" class="g-y">2. Ravi</text>'
        '<text x="502" y="72" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="514" y="46" width="146" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="587" y="66" text-anchor="middle" font-size="10.5" font-weight="800" class="g-mf">Habib b. Ebu Sabit</text>'
        '<text x="587" y="81" text-anchor="middle" font-size="9.5" class="g-y">3. Ravi</text>'
        '<rect x="20" y="114" width="136" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="88" y="134" text-anchor="middle" font-size="11" font-weight="800" class="g-mf">Süfyan</text>'
        '<text x="88" y="149" text-anchor="middle" font-size="9.5" class="g-y">4. Ravi</text>'
        '<text x="168" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="180" y="114" width="156" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="258" y="134" text-anchor="middle" font-size="10.5" font-weight="800" class="g-mf">Abdurrahman b. Mehdi</text>'
        '<text x="258" y="149" text-anchor="middle" font-size="9.5" class="g-y">5. Ravi</text>'
        '<text x="348" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="360" y="114" width="150" height="44" rx="8" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="435" y="134" text-anchor="middle" font-size="10.5" font-weight="800" class="g-mf">Muhammed b. Beşşar</text>'
        '<text x="435" y="149" text-anchor="middle" font-size="9.5" class="g-y">6. Ravi</text>'
        '<text x="522" y="140" text-anchor="middle" font-size="14" font-weight="800" class="g-y">→</text>'
        '<rect x="534" y="114" width="126" height="44" rx="8" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="597" y="134" text-anchor="middle" font-size="11" font-weight="800" class="g-sf">Tirmizî</text>'
        '<text x="597" y="149" text-anchor="middle" font-size="9.5" class="g-y">Muhaddis (Müellif)</text>'
        '<rect x="20" y="172" width="640" height="32" rx="8" class="g-moa"/>'
        '<text x="340" y="192" text-anchor="middle" font-size="11" font-weight="700" class="g-mof">Metin: "Nerede olursan ol, Allah\'a karşı sorumluluğunun bilincinde ol... İnsanlara güzel ahlakla davran!"</text>'
    )
    return svg(680, 216, ic, "Hadiste senet zinciri ve metin ayrımı")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _hadis_cesitleri()
    if len(b) > 1:
        b[1]["gorsel"] = _sunnet_kapsami()
    if len(b) > 3:
        b[3]["gorsel"] = _senet_zinciri()
