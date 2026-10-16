from ozet_gorsel import svg


def _enerji_diyagrami_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'Endotermik ve Ekzotermik Tepkimelerde Enerji Değişimi</text>'
        # Sol: Endotermik
        '<rect x="16" y="32" width="216" height="172" rx="10" class="g-ma"/>'
        '<text x="124" y="50" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">'
        'Endotermik (Isı Alan)</text>'
        '<line x1="42" y1="175" x2="42" y2="62" class="g-c" stroke-width="1.8"/>'
        '<line x1="42" y1="175" x2="212" y2="175" class="g-c" stroke-width="1.8"/>'
        '<text x="34" y="70" text-anchor="end" font-size="10" class="g-y">E</text>'
        '<line x1="50" y1="148" x2="110" y2="148" class="g-ms" stroke-width="3"/>'
        '<text x="80" y="162" text-anchor="middle" font-size="10" font-weight="700" class="g-mf">Tepken + ısı</text>'
        '<path d="M 110 148 C 128 148, 128 86, 146 86" fill="none" class="g-ms" stroke-width="2" stroke-dasharray="4,3"/>'
        '<line x1="146" y1="86" x2="206" y2="86" class="g-ms" stroke-width="3"/>'
        '<text x="176" y="78" text-anchor="middle" font-size="10" font-weight="700" class="g-mf">Ürünler</text>'
        '<path d="M 128 144 L 128 92" fill="none" class="g-ts" stroke-width="2"/>'
        '<polygon points="128,87 124,95 132,95" class="g-tf"/>'
        '<text x="124" y="194" text-anchor="middle" font-size="10" font-weight="700" class="g-y">'
        'E_ürün &gt; E_tepken (Sistem ısı alır)</text>'
        # Sağ: Ekzotermik
        '<rect x="248" y="32" width="216" height="172" rx="10" class="g-ta"/>'
        '<text x="356" y="50" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">'
        'Ekzotermik (Isı Veren)</text>'
        '<line x1="274" y1="175" x2="274" y2="62" class="g-c" stroke-width="1.8"/>'
        '<line x1="274" y1="175" x2="444" y2="175" class="g-c" stroke-width="1.8"/>'
        '<text x="266" y="70" text-anchor="end" font-size="10" class="g-y">E</text>'
        '<line x1="282" y1="86" x2="342" y2="86" class="g-ts" stroke-width="3"/>'
        '<text x="312" y="78" text-anchor="middle" font-size="10" font-weight="700" class="g-tf">Tepkenler</text>'
        '<path d="M 342 86 C 360 86, 360 148, 378 148" fill="none" class="g-ts" stroke-width="2" stroke-dasharray="4,3"/>'
        '<line x1="378" y1="148" x2="438" y2="148" class="g-ts" stroke-width="3"/>'
        '<text x="408" y="162" text-anchor="middle" font-size="10" font-weight="700" class="g-tf">Ürün + ısı</text>'
        '<path d="M 360 90 L 360 142" fill="none" class="g-ms" stroke-width="2"/>'
        '<polygon points="360,147 356,139 364,139" class="g-mf"/>'
        '<text x="356" y="194" text-anchor="middle" font-size="10" font-weight="700" class="g-y">'
        'E_tepken &gt; E_ürün (Sistem ısı verir)</text>'
    )
    return svg(480, 214, ic, "Endotermik ve ekzotermik tepkimelerde enerji değişimi")


def _isil_deger_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        '1 Gram Maddenin Yanmasıyla Açığa Çıkan Isı (kJ/g)</text>'
        # Barlar
        '<text x="118" y="48" text-anchor="end" font-size="11" font-weight="600" class="g-y">Glikoz</text>'
        '<rect x="126" y="36" width="34" height="16" rx="4" class="g-sa"/>'
        '<text x="166" y="48" font-size="10" font-weight="700" class="g-sf">15,6 kJ/g</text>'

        '<text x="118" y="74" text-anchor="end" font-size="11" font-weight="600" class="g-y">Çam Odunu</text>'
        '<rect x="126" y="62" width="46" height="16" rx="4" class="g-sa"/>'
        '<text x="178" y="74" font-size="10" font-weight="700" class="g-sf">21,2 kJ/g</text>'

        '<text x="118" y="100" text-anchor="end" font-size="11" font-weight="600" class="g-y">Taş Kömürü</text>'
        '<rect x="126" y="88" width="62" height="16" rx="4" class="g-ta"/>'
        '<text x="194" y="100" font-size="10" font-weight="700" class="g-tf">28,3 kJ/g</text>'

        '<text x="118" y="126" text-anchor="end" font-size="11" font-weight="600" class="g-y">İzooktan</text>'
        '<rect x="126" y="114" width="104" height="16" rx="4" class="g-ta"/>'
        '<text x="236" y="126" font-size="10" font-weight="700" class="g-tf">47,8 kJ/g</text>'

        '<text x="118" y="152" text-anchor="end" font-size="11" font-weight="600" class="g-y">Doğal Gaz</text>'
        '<rect x="126" y="140" width="108" height="16" rx="4" class="g-ma"/>'
        '<text x="240" y="152" font-size="10" font-weight="700" class="g-mf">49,5 kJ/g</text>'

        '<text x="118" y="178" text-anchor="end" font-size="11" font-weight="700" class="g-yf">Hidrojen (H₂)</text>'
        '<rect x="126" y="166" width="286" height="18" rx="4" class="g-ya"/>'
        '<text x="418" y="179" font-size="10" font-weight="700" class="g-yf">142,9 kJ/g</text>'

        '<text x="240" y="202" text-anchor="middle" font-size="10" class="g-y">'
        'Besinlerin Fizyolojik Enerjisi: Karbonhidrat = 17 kJ/g · Protein = 17 kJ/g · Yağ = 38 kJ/g</text>'
    )
    return svg(480, 212, ic, "Bazı yakıtların ısıl değerlerinin karşılaştırılması")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _enerji_diyagrami_svg()
    if len(b) > 3:
        b[3]["gorsel"] = _isil_deger_svg()
