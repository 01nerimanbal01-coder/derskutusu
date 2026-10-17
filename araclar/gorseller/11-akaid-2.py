from ozet_gorsel import svg


def _gorsel_1():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">AKAİD İLMİNİN KONUSU (USULÜSELASE) VE LİTERATÜRÜ</text>

    <!-- Sol: Usulüselase -->
    <rect x="28" y="52" width="315" height="156" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="185" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1d4ed8">USULÜSELASE (ÜÇ ANA BÖLÜM)</text>

    <rect x="40" y="82" width="291" height="36" rx="6" fill="#ffffff" stroke="#60a5fa"/>
    <text x="52" y="98" font-size="10.5" font-weight="bold" fill="#1e40af">1. İlahiyyat:</text>
    <text x="128" y="98" font-size="9.8" fill="#334155">Allah'a (cc) iman ve Kadere iman</text>
    <text x="52" y="112" font-size="8.8" fill="#64748b">(Allah'ın ilim, irade ve kudret sıfatlarıyla bütünlük içinde)</text>

    <rect x="40" y="124" width="291" height="34" rx="6" fill="#ffffff" stroke="#60a5fa"/>
    <text x="52" y="145" font-size="10.5" font-weight="bold" fill="#1e40af">2. Nübüvvat:</text>
    <text x="132" y="145" font-size="9.8" fill="#334155">Peygamberlere ve İlahi kitaplara iman</text>

    <rect x="40" y="164" width="291" height="34" rx="6" fill="#ffffff" stroke="#60a5fa"/>
    <text x="52" y="185" font-size="10.5" font-weight="bold" fill="#1e40af">3. Semiyyat:</text>
    <text x="132" y="185" font-size="9.8" fill="#334155">Meleklere ve Ahiret gününe iman</text>

    <!-- Sağ: Klasik Eserler -->
    <rect x="357" y="52" width="295" height="156" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="1.8"/>
    <text x="504" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#a16207">KLASİK AKAİD LİTERATÜRÜ</text>
    <text x="371" y="93" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Ebu Hanife:&lt;/tspan> el-Fıkhü'l-Ekber</text>
    <text x="371" y="110" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Tahavi:&lt;/tspan> el-Akidetü't-Tahaviyye</text>
    <text x="371" y="127" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Hakim es-Semerkandi:&lt;/tspan> es-Sevadu'l-Azam</text>
    <text x="371" y="144" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Eşari:&lt;/tspan> el-İbane  • &lt;tspan font-weight="bold">Nesefi:&lt;/tspan> Akaid</text>
    <text x="371" y="161" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Uşi:&lt;/tspan> el-Emali  • &lt;tspan font-weight="bold">Birgivi:&lt;/tspan> el-Vasıyye</text>
    <text x="371" y="178" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Erzurumlu İbrahim Hakkı:&lt;/tspan> Akaid-i Din-i İslam</text>
    <text x="371" y="195" font-size="9.6" fill="#1e293b">• &lt;tspan font-weight="bold">Ömer Nasuhi Bilmen:&lt;/tspan> Mülahhas İlm-i Tevhit</text>
    """
    return svg(w, h, ic, "Usulüselase Sınıflandırması ve Klasik Akaid Eserleri")


def _gorsel_2():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#14532d">İSLAM AKAİDİNİN ON TEMEL ÖZELLİĞİ (BİLGİ GÖRSELİ 1.2)</text>

    <!-- 2 Sütun x 5 Satır -->
    <rect x="28" y="52" width="302" height="156" rx="10" fill="#ffffff" stroke="#22c55e" stroke-width="1.5"/>
    <text x="42" y="74" font-size="10" fill="#1e293b">1. &lt;tspan font-weight="bold" fill="#15803d">İman esaslarını konu edinir:&lt;/tspan> 6 temel esas.</text>
    <text x="42" y="99" font-size="10" fill="#1e293b">2. &lt;tspan font-weight="bold" fill="#15803d">Değişmez esaslara dayanır:&lt;/tspan> Zamana göre değişmez.</text>
    <text x="42" y="124" font-size="10" fill="#1e293b">3. &lt;tspan font-weight="bold" fill="#15803d">Tevhit ilkesini merkeze alır:&lt;/tspan> Allah'ın birliği.</text>
    <text x="42" y="149" font-size="10" fill="#1e293b">4. &lt;tspan font-weight="bold" fill="#15803d">Açık ve anlaşılırdır:&lt;/tspan> Sade ve net bir dil sunar.</text>
    <text x="42" y="174" font-size="10" fill="#1e293b">5. &lt;tspan font-weight="bold" fill="#15803d">Kaynağı Kur'an ve sünnettir:&lt;/tspan> Vahye dayanır.</text>

    <rect x="350" y="52" width="302" height="156" rx="10" fill="#ffffff" stroke="#22c55e" stroke-width="1.5"/>
    <text x="364" y="74" font-size="10" fill="#1e293b">6. &lt;tspan font-weight="bold" fill="#15803d">Bir bütündür:&lt;/tspan> Biri reddedilirse tamamı bozulur.</text>
    <text x="364" y="99" font-size="10" fill="#1e293b">7. &lt;tspan font-weight="bold" fill="#15803d">Kesinlik ifade eder:&lt;/tspan> Zan ve şüpheye yer yoktur.</text>
    <text x="364" y="124" font-size="10" fill="#1e293b">8. &lt;tspan font-weight="bold" fill="#15803d">Akıl ve fıtratla uyumludur:&lt;/tspan> Yaratılışa uygundur.</text>
    <text x="364" y="149" font-size="10" fill="#1e293b">9. &lt;tspan font-weight="bold" fill="#15803d">Delillendirilebilir:&lt;/tspan> Akli ve naklî kanıtları vardır.</text>
    <text x="364" y="174" font-size="10" fill="#1e293b">10. &lt;tspan font-weight="bold" fill="#15803d">Hayatı yönlendirir:&lt;/tspan> Ahlak ve davranışı biçimlendirir.</text>
    """
    return svg(w, h, ic, "İslam Akaidinin On Temel Özelliği")


def _gorsel_3():
    w, h = 680, 230
    ic = """
    <rect x="15" y="15" width="650" height="200" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#78350f">AMENTÜ, KELİMEİTEVHİT VE KELİMEİŞEHADET</text>

    <rect x="28" y="52" width="624" height="64" rx="9" fill="#ffffff" stroke="#d97706" stroke-width="1.6"/>
    <text x="340" y="71" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#92400e">AMENTÜ ("İnandım") — Müslümanların Ortak İnanç Paydası</text>
    <text x="340" y="89" text-anchor="middle" font-size="9.8" fill="#1e293b">Allah'a (cc) • Meleklerine • Kitaplarına • Peygamberlerine • Ahiret Gününe • Kadere (Hayır ve Şerrin</text>
    <text x="340" y="104" text-anchor="middle" font-size="9.8" fill="#1e293b">Allah'tan olduğuna) iman ve Ölümden sonra dirilişin (ba's ba'de'l-mevt) hak olduğuna şehadet.</text>

    <rect x="28" y="126" width="302" height="74" rx="9" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
    <text x="179" y="145" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">Kelimeitevhit</text>
    <text x="179" y="163" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e">Lâ ilâhe illallah Muhammedürrasulüllâh</text>
    <text x="179" y="180" text-anchor="middle" font-size="9" fill="#334155">"Allah'tan başka ilah yoktur, Muhammed O'nun elçisidir."</text>

    <rect x="350" y="126" width="302" height="74" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
    <text x="501" y="145" text-anchor="middle" font-size="11" font-weight="bold" fill="#075985">Kelimeişehadet</text>
    <text x="501" y="162" text-anchor="middle" font-size="9.2" font-weight="bold" fill="#0369a1">Eşhedü ellâ ilâhe illallah ve eşhedü enne...</text>
    <text x="501" y="180" text-anchor="middle" font-size="9" fill="#334155">"Allah'tan başka ilah olmadığına, Muhammed'in O'nun</text>
    <text x="501" y="192" text-anchor="middle" font-size="9" fill="#334155">kulu ve elçisi olduğuna şahitlik ederim."</text>
    """
    return svg(w, h, ic, "Amentü Esasları, Kelimeitevhit ve Kelimeişehadet")


def _gorsel_4():
    w, h = 680, 230
    ic = """
    <rect x="15" y="15" width="650" height="200" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">İMANIN MAHİYETİ: KALPLE TASDİK VE DİLLE İKRAR</text>

    <rect x="28" y="54" width="295" height="146" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
    <text x="175" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">KALPLE TASDİK (İmanın Özü / Rüknü)</text>
    <text x="42" y="98" font-size="10" fill="#1e293b">• Vahyin bildirdiği hakikatleri gönülden</text>
    <text x="52" y="113" font-size="10" fill="#1e293b">doğrulamak ve içtenlikle bağlanmaktır.</text>
    <text x="42" y="134" font-size="10" fill="#1e293b">• Allah (cc) katında mümin sayılmanın</text>
    <text x="52" y="149" font-size="10" font-weight="bold" fill="#1e40af">olmazsa olmaz (asli) şartıdır.</text>
    <text x="42" y="170" font-size="9.5" fill="#475569">• Kalpte tasdik yoksa yalnız dilin söylemesi</text>
    <text x="52" y="184" font-size="9.5" fill="#be123c">kişiyi mümin yapmaz (Nifak / Bakara, 8-10).</text>

    <rect x="357" y="54" width="295" height="146" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
    <text x="504" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">DİLLE İKRAR VE İKRAH DURUMU</text>
    <text x="371" y="98" font-size="10" fill="#1e293b">• İnanılan değerleri sözlü veya fiilî olarak</text>
    <text x="381" y="113" font-size="10" fill="#1e293b">dışa yansıtmaktır.</text>
    <text x="371" y="134" font-size="10" fill="#1e293b">• Dünyada &lt;tspan font-weight="bold" fill="#166534">Müslüman muamelesi görmek&lt;/tspan></text>
    <text x="381" y="149" font-size="10" fill="#1e293b">için gereklidir.</text>
    <text x="371" y="170" font-size="9.5" fill="#475569">• &lt;tspan font-weight="bold" fill="#15803d">Ammar bin Yasir (Nahl, 106):&lt;/tspan> Ölüm tehdidi</text>
    <text x="381" y="184" font-size="9.5" fill="#475569">altında kalbi imanla dolu olan mazurdur.</text>
    """
    return svg(w, h, ic, "Kalple Tasdik, Dille İkrar ve Ammar bin Yasir Örneği")


def _gorsel_5():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#4c1d95">İMAN ÇEŞİTLERİ, GEÇERLİLİK ŞARTLARI VE AMEL İLİŞKİSİ</text>

    <!-- Sol: İman Çeşitleri -->
    <rect x="28" y="52" width="300" height="156" rx="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.6"/>
    <text x="178" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#5b21b6">İMAN ÇEŞİTLERİ</text>
    <text x="42" y="94" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">Taklidî İman:&lt;/tspan> Araştırmadan, çevreden</text>
    <text x="52" y="108" font-size="9.5" fill="#475569">görüldüğü şekliyle yapılan iman.</text>
    <text x="42" y="128" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">Tahkikî İman:&lt;/tspan> Akıl yürütme, araştırma ve</text>
    <text x="52" y="142" font-size="9.5" fill="#475569">ilmi delillere dayalı bilinçli iman.</text>
    <text x="42" y="162" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">İcmalî İman:&lt;/tspan> Esaslara topluca inanmak.</text>
    <text x="42" y="182" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">Tafsilî İman:&lt;/tspan> Esaslara ayrıntılı inanmak.</text>

    <!-- Sağ: Geçerlilik Şartları ve Amel -->
    <rect x="352" y="52" width="300" height="156" rx="10" fill="#ffffff" stroke="#0d9488" stroke-width="1.6"/>
    <text x="502" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0f766e">GEÇERLİLİK ŞARTLARI VE İMAN-AMEL</text>
    <text x="366" y="94" font-size="9.8" fill="#1e293b">1. Baskı olmadan &lt;tspan font-weight="bold">özgür iradeyle&lt;/tspan> tercih edilmeli.</text>
    <text x="366" y="112" font-size="9.8" fill="#1e293b">2. Azap / ölüm (&lt;tspan font-weight="bold">yeis&lt;/tspan>) anına bırakılmamalı.</text>
    <text x="366" y="130" font-size="9.8" fill="#1e293b">3. Hiçbir dinî hüküm inkâr / alay konusu edilmemeli.</text>
    <rect x="366" y="142" width="272" height="54" rx="7" fill="#ccfbf1"/>
    <text x="502" y="159" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#115e59">İman-Amel: Amel imanın cüzü değildir; büyük</text>
    <text x="502" y="173" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#115e59">günah (kebire/mubikat) işleyen dinden çıkmaz.</text>
    <text x="502" y="187" text-anchor="middle" font-size="9" fill="#134e4a">İman nitelik (güçlülük) bakımından artıp eksilebilir.</text>
    """
    return svg(w, h, ic, "İman Çeşitleri, Geçerlilik Şartları ve İman-Amel İlişkisi")


def _gorsel_6():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">İNANÇ BAKIMINDAN İNSANLAR VE TEKFİRDEN SAKINMA</text>

    <!-- 4 Kutu -->
    <rect x="26" y="52" width="148" height="104" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
    <text x="100" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">MÜMİN (İman)</text>
    <text x="100" y="90" text-anchor="middle" font-size="9.2" fill="#1e293b">Vahyi şüphe duymadan</text>
    <text x="100" y="104" text-anchor="middle" font-size="9.2" fill="#1e293b">kalple tasdik ve dille</text>
    <text x="100" y="118" text-anchor="middle" font-size="9.2" fill="#1e293b">ikrar eden, güven</text>
    <text x="100" y="132" text-anchor="middle" font-size="9.2" fill="#1e293b">veren kimse.</text>

    <rect x="184" y="52" width="148" height="104" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
    <text x="258" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">MÜNAFIK (Nifak)</text>
    <text x="258" y="90" text-anchor="middle" font-size="9.2" fill="#1e293b">Kalben inanmadığı</text>
    <text x="258" y="104" text-anchor="middle" font-size="9.2" fill="#1e293b">hâlde aldatmak için</text>
    <text x="258" y="118" text-anchor="middle" font-size="9.2" fill="#1e293b">Müslüman görünen</text>
    <text x="258" y="132" text-anchor="middle" font-size="9.2" fill="#1e293b">ikiyüzlü kimse.</text>

    <rect x="342" y="52" width="148" height="104" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>
    <text x="416" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">MÜŞRİK (Şirk)</text>
    <text x="416" y="90" text-anchor="middle" font-size="9.2" fill="#1e293b">Allah'a inanmakla</text>
    <text x="416" y="104" text-anchor="middle" font-size="9.2" fill="#1e293b">birlikte zatında, sıfatında</text>
    <text x="416" y="118" text-anchor="middle" font-size="9.2" fill="#1e293b">veya ibadette O'na</text>
    <text x="416" y="132" text-anchor="middle" font-size="9.2" fill="#1e293b">ortak koşan kimse.</text>

    <rect x="500" y="52" width="154" height="104" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-width="1.6"/>
    <text x="577" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">KÂFİR (Küfür/İnkâr)</text>
    <text x="577" y="90" text-anchor="middle" font-size="9.2" fill="#1e293b">Allah'ın varlığını ve</text>
    <text x="577" y="104" text-anchor="middle" font-size="9.2" fill="#1e293b">İslam'ın hak din</text>
    <text x="577" y="118" text-anchor="middle" font-size="9.2" fill="#1e293b">olduğunu bütünüyle</text>
    <text x="577" y="132" text-anchor="middle" font-size="9.2" fill="#1e293b">reddeden kimse.</text>

    <!-- Alt Bant: Ehlikıble ve Tekfir -->
    <rect x="26" y="166" width="628" height="44" rx="8" fill="#e0f2fe" stroke="#0284c7"/>
    <text x="340" y="184" text-anchor="middle" font-size="10" font-weight="bold" fill="#075985">EHLİKIBLE TEKFİR EDİLEMEZ (Nisâ, 94: "Size selam verene 'Sen mümin değilsin' demeyin.")</text>
    <text x="340" y="199" text-anchor="middle" font-size="9.2" fill="#0c4a6e">Elfazıküfür: Küfre düşüren sözler  •  Efaliküfür: Küfre götüren fiiller  •  Ehlikıble: Kâbe'yi kıble edinen Müslümanlar</text>
    """
    return svg(w, h, ic, "İnanç Bakımından İnsan Sınıflandırması ve Ehlikıblenin Tekfir Edilmemesi")


def uygula(v):
    gorseller = [
        _gorsel_1(),
        _gorsel_2(),
        _gorsel_3(),
        _gorsel_4(),
        _gorsel_5(),
        _gorsel_6(),
    ]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g