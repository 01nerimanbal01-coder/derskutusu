from ozet_gorsel import svg


def _esbabinuzul_ve_ornekler_svg():
    ic = """
    <rect x="20" y="16" width="760" height="295" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" fill="#0f172a">ESBABINÜZUL (AYETLERİN İNDİRİLİŞ SEBEPLERİ) VE DOĞRU ANLAMA SÜRECİ</text>

    <!-- Sol: Esbabınüzul Tanım ve 4 Yararı -->
    <rect x="36" y="58" width="290" height="236" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <rect x="36" y="58" width="290" height="30" rx="12" fill="#2563eb"/>
    <text x="181" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#ffffff">ESBABINÜZULÜ BİLMENİN FAYDALARI</text>

    <rect x="50" y="100" width="262" height="36" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="181" y="122" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1e3a8a">1. Emir ve yasakların hikmetini kavratır</text>

    <rect x="50" y="144" width="262" height="36" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="181" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1e3a8a">2. Kapalı anlatılan olayları aydınlatır</text>

    <rect x="50" y="188" width="262" height="36" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="181" y="210" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1e3a8a">3. Ayet ve sureler arası ilişki kurdurur</text>

    <rect x="50" y="232" width="262" height="48" rx="7" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="181" y="252" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1e3a8a">4. Yanlış Yorumları Önler!</text>
    <text x="181" y="268" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#1e40af">Bağlamdan kopuk zahirî yanılgıları engeller</text>

    <!-- Sağ: Somut Ayet Örnekleri -->
    <rect x="344" y="58" width="420" height="236" rx="12" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <rect x="344" y="58" width="420" height="30" rx="12" fill="#16a34a"/>
    <text x="554" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#ffffff">NÜZUL SEBEBİYLE ANLAŞILAN AYET ÖRNEKLERİ</text>

    <rect x="360" y="98" width="388" height="42" rx="7" fill="#ffffff" stroke="#86efac"/>
    <text x="372" y="115" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#14532d">• Bakara, 115 (Kıble Tayini):</text>
    <text x="372" y="131" font-family="Inter,sans-serif" font-size="9.3" fill="#166534">Gece karanlıkta yön bulamayıp içtihatla namaz kılan sahabiler</text>

    <rect x="360" y="146" width="388" height="42" rx="7" fill="#ffffff" stroke="#86efac"/>
    <text x="372" y="163" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#14532d">• Tevbe, 79 (Sadaka ve İnfak):</text>
    <text x="372" y="179" font-family="Inter,sans-serif" font-size="9.3" fill="#166534">Abdurrahman b. Avf ve bir avuç hurma getiren sahabiyle alay edilmesi</text>

    <rect x="360" y="194" width="388" height="42" rx="7" fill="#ffffff" stroke="#86efac"/>
    <text x="372" y="211" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#14532d">• Maide, 93 (İçki Yasağı Öncesi):</text>
    <text x="372" y="227" font-family="Inter,sans-serif" font-size="9.3" fill="#166534">Yasaktan önce vefat eden sahabilerin sorumlu olmadığının bildirilmesi</text>

    <rect x="360" y="242" width="388" height="42" rx="7" fill="#ffffff" stroke="#86efac"/>
    <text x="372" y="259" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#14532d">• Bakara, 195 (Ebu Eyyüb el-Ensari):</text>
    <text x="372" y="275" font-family="Inter,sans-serif" font-size="9.3" fill="#166534">"Tehlikeye atmayın" = Allah yolunda infakı terk edip dünyevileşmeyin</text>
    """
    return svg(800, 325, ic, "Esbabınüzul ve Ayetleri Doğru Anlama Süreci")


def _adalet_ve_cehalet_kavramlari_svg():
    ic = """
    <rect x="20" y="16" width="760" height="290" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" fill="#0f172a">KUR'AN-I KERİM'DE ADALET VE CEHALET KAVRAMLARININ KARŞILAŞTIRMASI</text>

    <!-- Sol: Adalet -->
    <rect x="36" y="58" width="352" height="232" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <rect x="36" y="58" width="352" height="32" rx="12" fill="#059669"/>
    <text x="212" y="79" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">ADALET (Doğruluk, Denklik ve Hakkaniyet)</text>

    <text x="52" y="112" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#064e3b">• Kanun Önünde Eşitlik &amp; Hakkaniyet:</text>
    <text x="62" y="128" font-family="Inter,sans-serif" font-size="9.5" fill="#047857">Herkese hakkını vermek, emaneti ehline teslim etmek (Nisa, 58)</text>

    <text x="52" y="152" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#064e3b">• Yakınlara Karşı Tarafsızlık (Nisa, 135):</text>
    <text x="62" y="168" font-family="Inter,sans-serif" font-size="9.5" fill="#047857">Anne baba, akraba veya kendi aleyhine bile olsa adil şahitlik</text>

    <text x="52" y="192" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#064e3b">• Düşmana Karşı Adalet (Maide, 8):</text>
    <text x="62" y="208" font-family="Inter,sans-serif" font-size="9.5" fill="#047857">Bir topluluğa duyulan kinin adaletsizliğe sevk etmemesi</text>

    <rect x="52" y="224" width="320" height="52" rx="8" fill="#d1fae5" stroke="#10b981"/>
    <text x="212" y="243" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#065f46">Hz. Peygamber'in (sav) Ölçüsü:</text>
    <text x="212" y="261" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.3" font-style="italic" fill="#047857">"... Kızım Fatıma bile hırsızlık yapsa onu da cezalandırırdım."</text>

    <!-- Sağ: Cehalet / Cahiliye -->
    <rect x="412" y="58" width="352" height="232" rx="12" fill="#fff1f2" stroke="#f43f5e" stroke-width="2"/>
    <rect x="412" y="58" width="352" height="32" rx="12" fill="#e11d48"/>
    <text x="588" y="79" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">CEHALET VE CAHİLİYE ZİHNİYETİ</text>

    <text x="428" y="112" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#881337">• Bilgisizlik ve Yanlış İnanç:</text>
    <text x="438" y="128" font-family="Inter,sans-serif" font-size="9.5" fill="#9f1239">Okuma ve ilim emriyle (Alak, 1-5) cehaletin ortadan kaldırılması</text>

    <text x="428" y="152" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#881337">• Araştırmadan Hüküm Verme (Hucurât, 6):</text>
    <text x="438" y="168" font-family="Inter,sans-serif" font-size="9.5" fill="#9f1239">Fasığın haberini doğrulamadan (dezenformasyon) zarar verme</text>

    <text x="428" y="192" font-family="Inter,sans-serif" font-size="10.2" font-weight="700" fill="#881337">• Cahiliye Âdetleri ve Taşkınlık:</text>
    <text x="438" y="208" font-family="Inter,sans-serif" font-size="9.5" fill="#9f1239">Soyla övünme, nesebe dil uzatma, kibir ve öfkeli saldırganlık</text>

    <rect x="428" y="224" width="320" height="52" rx="8" fill="#ffe4e6" stroke="#f43f5e"/>
    <text x="588" y="243" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#881337">Müminin Duruşu (Furkân, 63; A'râf, 199):</text>
    <text x="588" y="261" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.3" font-style="italic" fill="#9f1239">Vakarla yürümek, cahiller laf attığında "Selam" deyip geçmek</text>
    """
    return svg(800, 320, ic, "Kur'an-ı Kerim'de Adalet ve Cehalet Kavramları")


def uygula(v):
    v["bolumler"][1]["gorsel"] = _esbabinuzul_ve_ornekler_svg()
    v["bolumler"][3]["gorsel"] = _adalet_ve_cehalet_kavramlari_svg()