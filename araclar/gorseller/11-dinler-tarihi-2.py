from ozet_gorsel import svg


def _kurumsal_din_ve_unsurlar_svg():
    ic = """
    <rect x="20" y="16" width="760" height="290" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="800" fill="#0f172a">KURUMSAL BİR YAPI OLARAK DİN VE DİNİN ÖZÜNÜ OLUŞTURAN 5 UNSUR</text>

    <!-- Sol: Kurumsallaşma Süreci -->
    <rect x="38" y="60" width="260" height="230" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <rect x="38" y="60" width="260" height="32" rx="12" fill="#2563eb"/>
    <text x="168" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">DİNİN KURUMSALLAŞMA SÜRECİ</text>

    <rect x="54" y="104" width="228" height="34" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="168" y="125" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#1e3a8a">1. Kurucu / Peygamber Dönemi</text>

    <text x="168" y="151" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#2563eb">↓ Vefat Sonrası İhtiyaçlar ↓</text>

    <rect x="54" y="160" width="228" height="54" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="168" y="178" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e40af">• İnananları bir arada tutmak</text>
    <text x="168" y="193" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e40af">• Kutsal metinleri derlemek</text>
    <text x="168" y="208" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e40af">• İbadet ve ritüelleri düzenlemek</text>

    <rect x="54" y="226" width="228" height="48" rx="7" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="168" y="245" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1e3a8a">Dinamik Kurumsal Yapı</text>
    <text x="168" y="262" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#1e40af">Mabedler • Eğitim • Hukuk • Geleneğin Korunması</text>

    <!-- Sağ: Dinin Özünü Oluşturan 5 Unsur -->
    <rect x="318" y="60" width="444" height="230" rx="12" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <rect x="318" y="60" width="444" height="32" rx="12" fill="#16a34a"/>
    <text x="540" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">DİNİN ÖZÜNÜ OLUŞTURAN 5 TEMEL UNSUR</text>

    <rect x="336" y="104" width="408" height="34" rx="8" fill="#dcfce7" stroke="#22c55e" stroke-width="1.5"/>
    <text x="540" y="125" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#14532d">1. ALLAH (CC) / YÜCE VARLIK İNANCI (Merkezî Kaynak)</text>

    <rect x="336" y="148" width="198" height="60" rx="8" fill="#ffffff" stroke="#86efac"/>
    <text x="435" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#166534">2. İnanç-İbadet-Ahlak-Muamelat</text>
    <text x="435" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">İman ile amelin ve sosyal</text>
    <text x="435" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">ilişkilerin ayrılmaz bütünlüğü</text>

    <rect x="546" y="148" width="198" height="60" rx="8" fill="#ffffff" stroke="#86efac"/>
    <text x="645" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#166534">3. Mutlak İtaat Duygusu</text>
    <text x="645" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">Yaratıcı'nın emirlerine saygı</text>
    <text x="645" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">ve gönülden teslimiyet</text>

    <rect x="336" y="218" width="198" height="58" rx="8" fill="#ffffff" stroke="#86efac"/>
    <text x="435" y="239" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#166534">4. Toplumsal Değerler Bilinci</text>
    <text x="435" y="256" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">Adalet, yardımlaşma ve</text>
    <text x="435" y="269" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">ortak cemaat dayanışması</text>

    <rect x="546" y="218" width="198" height="58" rx="8" fill="#ffffff" stroke="#86efac"/>
    <text x="645" y="239" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#166534">5. Akıl ve İrade</text>
    <text x="645" y="256" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">Mesajı kavrama ve özgürce</text>
    <text x="645" y="269" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#15803d">seçip sorumlu olma yetisi</text>
    """
    return svg(800, 322, ic, "Kurumsal Bir Yapı Olarak Din ve Dinin Özünü Oluşturan 5 Unsur")


def _dinler_tarihi_metot_ve_gelisim_svg():
    ic = """
    <rect x="20" y="16" width="760" height="295" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" fill="#0f172a">DİNLER TARİHİNİN METODU VE TARİHSEL GELİŞİM KOLLARI</text>

    <!-- Üst Bant: Metot Karşılaştırması -->
    <rect x="38" y="56" width="352" height="72" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="214" y="76" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#065f46">DİNLER TARİHİ METODU (TASVİRÎ &amp; OBJEKTİF)</text>
    <text x="214" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#047857">• Dinleri "olduğu gibi" ve kendi kaynaklarından betimler</text>
    <text x="214" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#047857">• Karşılaştırmalı (mukayeseli) ve tarafsızdır; yargılamaz</text>

    <rect x="410" y="56" width="352" height="72" rx="10" fill="#fff1f2" stroke="#f43f5e" stroke-width="2"/>
    <text x="586" y="76" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#9f1239">KELAM / TEOLOJİ METODU (NORMATİF)</text>
    <text x="586" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#be123c">• Belirli bir dinin inanç esaslarını savunur (apolojetik)</text>
    <text x="586" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#be123c">• Kural koyucu, doğrulayıcı ve reddiyeci niteliktedir</text>

    <!-- Alt Üç Sütun: İslam Dünyası, Osmanlı/Türkiye, Batı -->
    <rect x="38" y="142" width="232" height="154" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
    <rect x="38" y="142" width="232" height="28" rx="10" fill="#d97706"/>
    <text x="154" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">1. İSLAM DÜNYASI (Klasik Dönem)</text>
    <text x="50" y="186" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#78350f">• Kur'an-ı Kerim (Ehlikitap vb.)</text>
    <text x="50" y="205" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#78350f">• Bîrûnî — Tahkîku Mâ li'l-Hind</text>
    <text x="58" y="219" font-family="Inter,sans-serif" font-size="9" fill="#92400e">(Gözlem ve Sanskritçe ana kaynak)</text>
    <text x="50" y="238" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#78350f">• İbn Hazm — Kitâbu'l-Fasl</text>
    <text x="50" y="257" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#78350f">• Şehristanî — el-Milel ve'n-Nihal</text>
    <text x="58" y="271" font-family="Inter,sans-serif" font-size="9" fill="#92400e">(İlk mukayeseli dinler tarihi klasiği)</text>

    <rect x="284" y="142" width="232" height="154" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <rect x="284" y="142" width="232" height="28" rx="10" fill="#2563eb"/>
    <text x="400" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">2. BATI DÜNYASI (19. Yüzyıl)</text>
    <text x="296" y="186" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#1e3a8a">• Oryantalizm &amp; Sömürgecilik etkisi</text>
    <text x="296" y="205" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#1e3a8a">• İsviçre, Hollanda, Belçika kürsüleri</text>
    <text x="296" y="224" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#1e3a8a">• F. Max Müller (Din Bilimine Giriş)</text>
    <text x="296" y="243" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#1e3a8a">• Kilise: Önce muhalefet, sonra</text>
    <text x="304" y="257" font-family="Inter,sans-serif" font-size="9" fill="#1e40af">misyonerlik için destek</text>
    <text x="296" y="276" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#1e3a8a">• Din Fenomenolojisi yaklaşımı</text>

    <rect x="530" y="142" width="232" height="154" rx="10" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.8"/>
    <rect x="530" y="142" width="232" height="28" rx="10" fill="#7c3aed"/>
    <text x="646" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">3. OSMANLI VE TÜRKİYE</text>
    <text x="542" y="186" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#4c1d95">• 1874 Dârülfünun ilk ders</text>
    <text x="542" y="205" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#4c1d95">• Şemseddin Sami — Esâtir (1893)</text>
    <text x="542" y="224" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#4c1d95">• Ahmet Mithat &amp; M. Es'ad —</text>
    <text x="550" y="238" font-family="Inter,sans-serif" font-size="9" fill="#5b21b6">Tarih-i Edyan eserleri</text>
    <text x="542" y="257" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#4c1d95">• H. Ömer Budda &amp; Ö. Rıza Doğrul</text>
    <text x="542" y="276" font-family="Inter,sans-serif" font-size="9.8" font-weight="700" fill="#4c1d95">• 1949 Ankara İlahiyat &amp; Schimmel</text>
    """
    return svg(800, 325, ic, "Dinler Tarihinin Metodu ve Tarihsel Gelişimi")


def uygula(v):
    v["bolumler"][0]["gorsel"] = _kurumsal_din_ve_unsurlar_svg()
    v["bolumler"][3]["gorsel"] = _dinler_tarihi_metot_ve_gelisim_svg()
