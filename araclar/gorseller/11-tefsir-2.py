from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Şûrâ Suresi 51. Ayete Göre Vahyin Geliş Yolları ve Mushaf Tarihçesi</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">Vahyin 3 Geliş Şekli (Şûrâ, 51)</text>
    <text x="42" y="130" font-size="12" font-weight="bold" fill="#1e40af">1. Doğrudan Vahiy (İlham / Sadık Rüya)</text>
    <text x="42" y="148" font-size="12" fill="#1e3a8a">• Kalbe doğrudan mana ilkası</text>
    <text x="42" y="175" font-size="12" font-weight="bold" fill="#1e40af">2. Perde Arkasından Konuşma</text>
    <text x="42" y="193" font-size="12" fill="#1e3a8a">• Hz. Musa'ya Tûr Dağı'nda hitap</text>
    <text x="42" y="220" font-size="12" font-weight="bold" fill="#1e40af">3. Elçi (Melek Cebrail) Gönderme</text>
    <text x="42" y="238" font-size="12" fill="#1e3a8a">• Çıngırak/çan uğultusu veya insan sureti</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#15803d">Kur'an'ın Yazımı ve Korunması</text>
    <text x="392" y="130" font-size="12" font-weight="bold" fill="#166534">1. Cem' (Hz. Ebubekir Dönemi)</text>
    <text x="392" y="148" font-size="12" fill="#14532d">• Zeyd bin Sabit heyetiyle Mushaf'ta toplama</text>
    <text x="392" y="175" font-size="12" font-weight="bold" fill="#166534">2. İstinsah (Hz. Osman Dönemi)</text>
    <text x="392" y="193" font-size="12" fill="#14532d">• Çoğaltılarak İslam merkezlerine gönderilme</text>
    <text x="392" y="220" font-size="12" font-weight="bold" fill="#166534">3. Noktalama ve Harekeleme</text>
    <text x="392" y="238" font-size="12" fill="#14532d">• Ebü'l-Esved ed-Düelî &amp; Halil bin Ahmed</text>
    """
    return svg(720, 285, ic, "Vahyin Geliş Şekilleri ve Kur'an'ın Korunması")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">İmam Mâtürîdî'ye Göre Tefsir - Tevil Ayrımı ve Tercüme - Meal Farkı</text>

    <rect x="25" y="75" width="320" height="105" rx="10" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="185" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">TEFSİR (Açıklama ve Kesin Beyan)</text>
    <text x="185" y="122" text-anchor="middle" font-size="12" fill="#4c1d95">• Lafzın tek ve kesin muradını belirler.</text>
    <text x="185" y="142" text-anchor="middle" font-size="12" fill="#4c1d95">• Sahabe tanıklığına ve rivayete dayanır.</text>
    <text x="185" y="162" text-anchor="middle" font-size="12" font-weight="bold" fill="#6d28d9">Örn: Ayetin kim ve ne için indiğinin tespiti</text>

    <rect x="375" y="75" width="320" height="105" rx="10" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="535" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#9d174d">TEVİL (Derin Yorum ve Tercih)</text>
    <text x="535" y="122" text-anchor="middle" font-size="12" fill="#831843">• Muhtemel anlamlardan birini delille seçer.</text>
    <text x="535" y="142" text-anchor="middle" font-size="12" fill="#831843">• Dirayete dayanır, kesinlik iddiası taşımaz.</text>
    <text x="535" y="162" text-anchor="middle" font-size="12" font-weight="bold" fill="#be185d">Örn: "Elhamdülillah" ifadesinin 3 vecihle yorumu</text>

    <rect x="25" y="195" width="670" height="78" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="360" y="218" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">TERCÜME (Lafzî / Tefsirî) ve MEAL (Yaklaşık Çeviri)</text>
    <text x="360" y="240" text-anchor="middle" font-size="12" fill="#78350f">Kur'an'ın eşsiz belagati başka bir dile birebir aktarılamadığı için çevirilere "Meal" denir.</text>
    <text x="360" y="258" text-anchor="middle" font-size="12" fill="#92400e">Örn: Mü'minûn 1. ayetteki "أَفْلَحَ" fiili → "kurtuluşa erdi / felah buldu / başarıya ulaştı"</text>
    """
    return svg(720, 285, ic, "Tefsir, Tevil, Tercüme ve Meal Mukayesesi")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Kur'an İlimleri (Ulûmü'l-Kur'ân) Sınıflandırma Şeması</text>

    <rect x="25" y="75" width="320" height="198" rx="12" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="185" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">1. Kur'an'ın Lafzıyla İlgili İlimler</text>
    <text x="45" y="124" font-size="12" fill="#134e4a">• Garîbü'l-Kur'ân (Nadir/güç kelimeler)</text>
    <text x="45" y="144" font-size="12" fill="#134e4a">• Vücûh (Çok anlamlı) ve Nezâir (Eş anlamlı)</text>
    <text x="45" y="164" font-size="12" fill="#134e4a">• Münâsebâtü'l-Kur'ân (Ayet-sure irtibatı)</text>
    <text x="45" y="184" font-size="12" fill="#134e4a">• Emsâlü'l-Kur'ân (Temsil ve deyimler)</text>
    <text x="45" y="204" font-size="12" fill="#134e4a">• Aksâmü'l-Kur'ân (Kur'an yeminleri)</text>
    <text x="45" y="224" font-size="12" fill="#134e4a">• İ'câzü'l-Kur'ân &amp; Mecâzü'l-Kur'ân</text>
    <text x="45" y="244" font-size="12" fill="#134e4a">• Hurûf-ı Mukattaa &amp; Üslûbü'l-Kur'ân</text>

    <rect x="375" y="75" width="320" height="198" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="535" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">2. Kur'an'ın Manasıyla İlgili İlimler</text>
    <text x="395" y="124" font-size="12" fill="#1e3a8a">• Nâsih ve Mensûh (Hükümlerin neshi)</text>
    <text x="395" y="148" font-size="12" fill="#1e3a8a">• Kısasü'l-Kur'ân (Kur'an kıssaları)</text>
    <text x="395" y="172" font-size="12" fill="#1e3a8a">• Esbâb-ı Nüzûl (Ayetlerin iniş sebepleri)</text>
    <text x="395" y="196" font-size="12" fill="#1e3a8a">• Mekkîlik ve Medenîlik (İniş dönemi)</text>
    <text x="395" y="220" font-size="12" fill="#1e3a8a">• Müteşâbihü'l-Kur'ân (Kapalı ayetler)</text>
    <text x="395" y="244" font-size="12" fill="#1e3a8a">• Müşkilü'l-Kur'ân &amp; Fezâilü'l-Kur'ân</text>
    """
    return svg(720, 290, ic, "Kur'an İlimlerinin Lafız ve Mana Bakımından Tasnifi")


def gorsel_4():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#7c2d12"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Lafza Dair İlimlerden Örnekler: Aksâm, İ'câz ve Mecâz</text>

    <rect x="25" y="75" width="210" height="190" rx="12" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="130" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">Aksâmü'l-Kur'ân</text>
    <text x="130" y="125" text-anchor="middle" font-size="12" fill="#7c2d12">Şems 1-10 (Güneşe, aya,</text>
    <text x="130" y="145" text-anchor="middle" font-size="12" fill="#7c2d12">nefse yemin) ve Yâsîn 1-4</text>
    <text x="130" y="172" text-anchor="middle" font-size="11" fill="#9a3412">Fahreddin er-Râzî:</text>
    <text x="130" y="190" text-anchor="middle" font-size="11" fill="#7c2d12">Varlıkların hikmetine dikkat</text>
    <text x="130" y="208" text-anchor="middle" font-size="11" fill="#7c2d12">çekmek ve mesajı pekiştirmek</text>

    <rect x="255" y="75" width="210" height="190" rx="12" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="360" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">İ'câzü'l-Kur'ân</text>
    <text x="360" y="125" text-anchor="middle" font-size="12" fill="#7f1d1d">İsrâ Suresi 88. Ayet:</text>
    <text x="360" y="145" text-anchor="middle" font-size="12" fill="#7f1d1d">İnsan ve cinlere Kur'an'ın</text>
    <text x="360" y="165" text-anchor="middle" font-size="12" fill="#7f1d1d">benzerini getirme konusunda</text>
    <text x="360" y="185" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">Meydan Okuma (Tahaddî)</text>
    <text x="360" y="212" text-anchor="middle" font-size="11" fill="#7f1d1d">Eşsiz üslup ve belagat</text>

    <rect x="485" y="75" width="210" height="190" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="590" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">Mecâzü'l-Kur'ân</text>
    <text x="590" y="125" text-anchor="middle" font-size="12" fill="#064e3b">Bakara Suresi 187. Ayet:</text>
    <text x="590" y="145" text-anchor="middle" font-size="12" fill="#064e3b">"Beyaz iplik siyah iplikten</text>
    <text x="590" y="165" text-anchor="middle" font-size="12" fill="#064e3b">ayırt edilinceye kadar"</text>
    <text x="590" y="190" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">Adiy bin Hâtim Olayı:</text>
    <text x="590" y="208" text-anchor="middle" font-size="11" fill="#064e3b">Gündüz aydınlığı / Gece karanlığı</text>
    """
    return svg(720, 285, ic, "Aksâmü'l-Kur'ân, İ'câzü'l-Kur'ân ve Mecâzü'l-Kur'ân")


def gorsel_5():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#065f46"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Manaya Dair İlimlerden Örnekler: Kısasü'l-Kur'ân ve Esbâb-ı Nüzûl</text>

    <rect x="30" y="75" width="315" height="190" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="187" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">Kısasü'l-Kur'ân (Kur'an Kıssaları)</text>
    <text x="48" y="128" font-size="12" fill="#064e3b">• Tarih/hikâye gibi yer ve zaman ayrıntısına</text>
    <text x="48" y="148" font-size="12" fill="#064e3b">değil, ibret ve tevhit mesajına odaklanır.</text>
    <text x="48" y="176" font-size="12" font-weight="bold" fill="#047857">Örnek: Ashâb-ı Kehf (Kehf, 13-17)</text>
    <text x="48" y="198" font-size="12" fill="#064e3b">Putperest topluma karşı inançlarını</text>
    <text x="48" y="218" font-size="12" fill="#064e3b">korumak için mağaraya sığınan gençler.</text>

    <rect x="375" y="75" width="315" height="190" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="532" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">Esbâb-ı Nüzûl (İniş Sebepleri)</text>
    <text x="393" y="128" font-size="12" fill="#1e3a8a">• Ayetin indiği ortamı ve soruyu bildirerek</text>
    <text x="393" y="148" font-size="12" fill="#1e3a8a">yanlış hüküm çıkarılmasını engeller.</text>
    <text x="393" y="176" font-size="12" font-weight="bold" fill="#1d4ed8">Örnek: Bakara 158 (Safa-Merve Sa'yi)</text>
    <text x="393" y="198" font-size="12" fill="#1e3a8a">Hz. Aişe, nüzul sebebini açıklayarak</text>
    <text x="393" y="218" font-size="12" fill="#1e3a8a">Urve bin Zübeyr'in yanılgısını düzeltti.</text>
    """
    return svg(720, 285, ic, "Kısasü'l-Kur'ân ve Esbâb-ı Nüzûl Örnekleri")


def gorsel_6():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Mekkî ve Medenî Surelerin Ayırıcı Özellikleri (Ölçüt: Hicret)</text>

    <rect x="30" y="75" width="315" height="195" rx="12" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="187" y="102" text-anchor="middle" font-size="15" font-weight="bold" fill="#312e81">MEKKÎ SURELER (Hicret Öncesi - 13 Yıl)</text>
    <text x="48" y="128" font-size="12" fill="#3730a3">• Konu: Tevhit, peygamberlik, kıyamet, ahiret</text>
    <text x="48" y="150" font-size="12" fill="#3730a3">• Üslup: Kısa ayetler, vurucu ve sarsıcı belagat</text>
    <text x="48" y="172" font-size="12" fill="#3730a3">• Hitap: "Ey insanlar!" / "Ey Âdemoğulları!"</text>
    <text x="48" y="194" font-size="12" font-weight="bold" fill="#4338ca">• İşaret: Secde ayetleri ve "Kellâ" (Hayır!)</text>
    <text x="48" y="216" font-size="12" fill="#3730a3">• Kıssalar: Geçmiş peygamberler (Bakara hariç)</text>
    <text x="48" y="242" font-size="12" font-weight="bold" fill="#312e81">Örnek: Tekâsür ve Tîn Sureleri</text>

    <rect x="375" y="75" width="315" height="195" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="532" y="102" text-anchor="middle" font-size="15" font-weight="bold" fill="#92400e">MEDENÎ SURELER (Hicret Sonrası - 10 Yıl)</text>
    <text x="393" y="128" font-size="12" fill="#78350f">• Konu: İbadet, muamelat, aile-miras hukuku</text>
    <text x="393" y="150" font-size="12" fill="#78350f">• Üslup: Uzun ayetler, sade ve açıklayıcı dil</text>
    <text x="393" y="172" font-size="12" fill="#78350f">• Hitap: "Ey iman edenler!" / "Ey Ehlikitap!"</text>
    <text x="393" y="194" font-size="12" font-weight="bold" fill="#b45309">• İşaret: Cihat izni ve Münafıklar (Ankebût hariç)</text>
    <text x="393" y="216" font-size="12" fill="#78350f">• Tarih: Bedir, Uhud, Hendek, Tebük gazveleri</text>
    <text x="393" y="242" font-size="12" font-weight="bold" fill="#92400e">Örnek: Bakara, Âl-i İmrân, Nisâ Sureleri</text>
    """
    return svg(720, 285, ic, "Mekkî ve Medenî Surelerin Karşılaştırılması")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g