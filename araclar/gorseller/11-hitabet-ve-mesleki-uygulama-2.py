from ozet_gorsel import svg


def _din_gorevlileri_ve_kurumlar_svg():
    ic = """
    <rect x="20" y="16" width="760" height="295" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" fill="#0f172a">ÜLKEMİZDE DİN HİZMETLERİ KADROLARI VE KURUMSAL YAPI (633 SAYILI KANUN)</text>

    <!-- Üst Merkez Kutu -->
    <rect x="190" y="54" width="420" height="44" rx="10" fill="#0f766e"/>
    <text x="400" y="74" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">DİYANET İŞLERİ BAŞKANLIĞI (3 Mart 1924)</text>
    <text x="400" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#ccfbf1">İmam Hatip Liseleri • İlahiyat Fakülteleri • Diyanet Akademisi</text>

    <!-- 5 Görev Kadrosu -->
    <rect x="34" y="114" width="138" height="114" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
    <rect x="34" y="114" width="138" height="26" rx="10" fill="#16a34a"/>
    <text x="103" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">İL / İLÇE MÜFTÜSÜ</text>
    <text x="103" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#14532d">• Din hizmetlerini yönetir</text>
    <text x="103" y="171" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#14532d">• Dinî soruları cevaplar</text>
    <text x="103" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#14532d">• Cami ve kursları</text>
    <text x="103" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#14532d">denetler (İlahiyat + İhtisas)</text>

    <rect x="180" y="114" width="138" height="114" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
    <rect x="180" y="114" width="138" height="26" rx="10" fill="#2563eb"/>
    <text x="249" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">VAİZ</text>
    <text x="249" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#1e3a8a">• Cami, cezaevi, yurt ve</text>
    <text x="249" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#1e3a8a">huzurevinde irşat yapar</text>
    <text x="249" y="185" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#1e3a8a">• Aile Dini Rehberlik</text>
    <text x="249" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#1e3a8a">(İlahiyat + Akademi)</text>

    <rect x="326" y="114" width="148" height="114" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.8"/>
    <rect x="326" y="114" width="148" height="26" rx="10" fill="#d97706"/>
    <text x="400" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">İMAM-HATİP</text>
    <text x="400" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#78350f">• Vakit, cuma, bayram ve</text>
    <text x="400" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#78350f">cenaze namazı kıldırır</text>
    <text x="400" y="185" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#78350f">• Hutbe okur, rehberlik eder</text>
    <text x="400" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#78350f">(İHL/İlahiyat + Akademi)</text>

    <rect x="482" y="114" width="138" height="114" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
    <rect x="482" y="114" width="138" height="26" rx="10" fill="#7c3aed"/>
    <text x="551" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">MÜEZZİN-KAYYIM</text>
    <text x="551" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#4c1d95">• Ezan ve kamet okur</text>
    <text x="551" y="171" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#4c1d95">• Caminin bakım, temizlik</text>
    <text x="551" y="185" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#4c1d95">ve düzenini sağlar</text>
    <text x="551" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#4c1d95">(Kayyımlık görevi)</text>

    <rect x="628" y="114" width="138" height="114" rx="10" fill="#fff1f2" stroke="#e11d48" stroke-width="1.8"/>
    <rect x="628" y="114" width="138" height="26" rx="10" fill="#e11d48"/>
    <text x="697" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#ffffff">KUR'AN KURSU ÖĞR.</text>
    <text x="697" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#881337">• Yüzünden okuma, tecvit</text>
    <text x="697" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#881337">ve hafızlık eğitimi verir</text>
    <text x="697" y="185" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#881337">• 4-6 Yaş ve yetişkin</text>
    <text x="697" y="201" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.2" font-weight="600" fill="#881337">kurslarında görev yapar</text>

    <!-- Alt Bant: Cami Dışı Hizmetler ve Nitelikler -->
    <rect x="34" y="242" width="732" height="54" rx="10" fill="#ecfeff" stroke="#0891b2" stroke-width="1.5"/>
    <text x="400" y="262" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#155e75">YAYGIN DİN HİZMETLERİ VE HADEME-İ HAYRATIN TEMEL NİTELİKLERİ</text>
    <text x="400" y="281" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.8" fill="#0e7490">Alo 190 Fetva Hattı • Aile ve Dinî Rehberlik Büroları • Manevi Danışmanlık | İhlas • Temsil Kabiliyeti • Sağlam Bilgi • Güzel Ahlak</text>
    """
    return svg(800, 325, ic, "Ülkemizde Din Hizmetleri Kadroları ve Kurumsal Yapı")


def _iletisim_ve_hitabet_asamalari_svg():
    ic = """
    <rect x="20" y="16" width="760" height="295" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="400" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="14.5" font-weight="800" fill="#0f172a">DİN HİZMETLERİNDE İLETİŞİM UNSURLARI VE HİTABET HAZIRLIK SÜRECİ</text>

    <!-- Üst: İletişimin 5 Unsuru -->
    <rect x="36" y="56" width="728" height="78" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="400" y="75" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="800" fill="#1e3a8a">İLETİŞİM SÜRECİNİN 5 TEMEL UNSURU</text>

    <rect x="52" y="85" width="120" height="36" rx="7" fill="#2563eb"/>
    <text x="112" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">1. KAYNAK</text>
    <text x="112" y="115" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#dbeafe">Hatip / Din Görevlisi</text>

    <text x="184" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="14" font-weight="800" fill="#2563eb">→</text>

    <rect x="196" y="85" width="120" height="36" rx="7" fill="#1d4ed8"/>
    <text x="256" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">2. MESAJ (İLETİ)</text>
    <text x="256" y="115" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#dbeafe">Davet • Tebliğ • İrşat</text>

    <text x="328" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="14" font-weight="800" fill="#2563eb">→</text>

    <rect x="340" y="85" width="120" height="36" rx="7" fill="#1e40af"/>
    <text x="400" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">3. KANAL</text>
    <text x="400" y="115" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#dbeafe">Söz, Ses, Beden Dili</text>

    <text x="472" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="14" font-weight="800" fill="#2563eb">→</text>

    <rect x="484" y="85" width="120" height="36" rx="7" fill="#1d4ed8"/>
    <text x="544" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">4. ALICI</text>
    <text x="544" y="115" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#dbeafe">Muhatap / Cemaat</text>

    <text x="616" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="14" font-weight="800" fill="#2563eb">→</text>

    <rect x="628" y="85" width="120" height="36" rx="7" fill="#0f766e"/>
    <text x="688" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">5. GERİ BİLDİRİM</text>
    <text x="688" y="115" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#ccfbf1">Dönüt / Tepki ve Soru</text>

    <!-- Alt: Hitabetin 4 Hazırlık Aşaması ve Sunum -->
    <rect x="36" y="148" width="460" height="148" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
    <rect x="36" y="148" width="460" height="28" rx="12" fill="#d97706"/>
    <text x="266" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">HİTABETİN 4 HAZIRLIK AŞAMASI</text>

    <text x="52" y="194" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#78350f">1. Hedef Kitleyi Tanıma: <tspan font-weight="500" fill="#92400e">Yaş, eğitim, meslek ve sosyal ihtiyaç analizi</tspan></text>
    <text x="52" y="216" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#78350f">2. Amaç ve Konu Seçimi: <tspan font-weight="500" fill="#92400e">Güncel, sınırları net ve faydalı konu belirleme</tspan></text>
    <text x="52" y="238" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#78350f">3. Planlama: <tspan font-weight="500" fill="#92400e">Giriş, gelişme ve sonuç bölümlerini taslaklaştırma</tspan></text>
    <text x="52" y="260" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#78350f">4. Bilgi Toplama (Sahih Kaynaklar):</text>
    <text x="66" y="278" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#b45309">• Kur'an ve Tefsirler • Kütübisitte • Din İşleri Yüksek Kurulu</text>

    <rect x="512" y="148" width="252" height="148" rx="12" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
    <rect x="512" y="148" width="252" height="28" rx="12" fill="#16a34a"/>
    <text x="638" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">SUNUM VE ÜSLUP İLKELERİ</text>

    <text x="526" y="194" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">• Giriş: Besmele, Hamdele, Salvele</text>
    <text x="526" y="216" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">• Üslup: Hikmet ve Kavl-i Leyyin</text>
    <text x="526" y="238" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">• Müjdeleyici, kolaylaştırıcı dil</text>
    <text x="526" y="260" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">• Göz teması, vurgu, süre uyumu</text>
    <text x="526" y="282" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">• Sonuç: Ana mesaj özeti ve Dua</text>
    """
    return svg(800, 325, ic, "Din Hizmetlerinde İletişim Unsurları ve Hitabet Hazırlık Süreci")


def uygula(v):
    v["bolumler"][1]["gorsel"] = _din_gorevlileri_ve_kurumlar_svg()
    v["bolumler"][4]["gorsel"] = _iletisim_ve_hitabet_asamalari_svg()
