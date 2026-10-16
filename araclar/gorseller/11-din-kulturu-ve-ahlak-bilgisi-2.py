from ozet_gorsel import svg


def _gorsel_1():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">EVRENSEL YASALAR (SÜNNETULLAH / ÂDETULLAH)</text>

    <!-- 3 Yasa Kutusu -->
    <rect x="28" y="54" width="198" height="154" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
    <text x="127" y="76" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. Fiziksel Yasalar</text>
    <line x1="45" y1="85" x2="209" y2="85" stroke="#93c5fd"/>
    <text x="127" y="105" text-anchor="middle" font-size="10" fill="#1e293b">Madde ve enerjinin oluşumu,</text>
    <text x="127" y="121" text-anchor="middle" font-size="10" fill="#1e293b">yer çekimi, suyun kaldırma</text>
    <text x="127" y="137" text-anchor="middle" font-size="10" fill="#1e293b">kuvveti, gece-gündüz ve</text>
    <text x="127" y="153" text-anchor="middle" font-size="10" fill="#1e293b">mevsimlerin düzeni.</text>
    <text x="127" y="182" text-anchor="middle" font-size="9" font-weight="bold" fill="#1e40af">(Deney ve gözleme dayanır)</text>

    <rect x="241" y="54" width="198" height="154" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
    <text x="340" y="76" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">2. Biyolojik Yasalar</text>
    <line x1="258" y1="85" x2="422" y2="85" stroke="#86efac"/>
    <text x="340" y="105" text-anchor="middle" font-size="10" fill="#1e293b">Canlıların doğması, büyümesi,</text>
    <text x="340" y="121" text-anchor="middle" font-size="10" fill="#1e293b">beslenmesi, fotosentez,</text>
    <text x="340" y="137" text-anchor="middle" font-size="10" fill="#1e293b">anatomik yapı ve çevreye</text>
    <text x="340" y="153" text-anchor="middle" font-size="10" fill="#1e293b">uyum (adaptasyon) ilkeleri.</text>
    <text x="340" y="182" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">(Canlılar dünyasını kapsar)</text>

    <rect x="454" y="54" width="198" height="154" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="1.8"/>
    <text x="553" y="76" text-anchor="middle" font-size="12" font-weight="bold" fill="#a16207">3. Toplumsal Yasalar</text>
    <line x1="471" y1="85" x2="635" y2="85" stroke="#fde047"/>
    <text x="553" y="105" text-anchor="middle" font-size="10" fill="#1e293b">Adalet, eşitlik, güven,</text>
    <text x="553" y="121" text-anchor="middle" font-size="10" fill="#1e293b">yardımlaşma, göç olgusu</text>
    <text x="553" y="137" text-anchor="middle" font-size="10" fill="#1e293b">ve toplumların yükseliş-çöküş</text>
    <text x="553" y="153" text-anchor="middle" font-size="10" fill="#1e293b">neden-sonuç ilişkileri.</text>
    <text x="553" y="182" text-anchor="middle" font-size="9" font-weight="bold" fill="#854d0e">(Toplumsal huzuru korur)</text>
    """
    return svg(w, h, ic, "Sünnetullah Kapsamındaki Fiziksel, Biyolojik ve Toplumsal Yasalar")


def _gorsel_2():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#78350f">KADERLE İLİŞKİLİ KAVRAMLAR VE İLAHİ İSİMLER</text>

    <rect x="28" y="54" width="300" height="154" rx="10" fill="#ffffff" stroke="#d97706" stroke-width="1.8"/>
    <text x="178" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">RIZIK VE ER-REZZAK</text>
    <text x="44" y="98" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#92400e">er-Rezzak:</tspan> Tüm canlıların rızkını yaratan Allah (cc).</text>
    <text x="44" y="118" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#92400e">Maddi Rızık:</tspan> Yiyecek, içecek, giyecek, hava, su.</text>
    <text x="44" y="138" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#92400e">Manevi Rızık:</tspan> Akıl, iman, ilim, sevgi, huzur.</text>
    <rect x="44" y="154" width="268" height="38" rx="6" fill="#fef3c7"/>
    <text x="178" y="171" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#78350f">Ölçü: Rızkı helal yoldan ve emekle aramak,</text>
    <text x="178" y="185" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#78350f">başarı için hileden kaçınıp gayret göstermek.</text>

    <rect x="352" y="54" width="300" height="154" rx="10" fill="#ffffff" stroke="#0d9488" stroke-width="1.8"/>
    <text x="502" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f766e">SABIR (ES-SABÛR), ÖMÜR VE ECEL</text>
    <text x="368" y="98" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#115e59">es-Sabûr:</tspan> Sabredenlere güç veren Yüce Allah.</text>
    <text x="368" y="118" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#115e59">Ömür:</tspan> Doğumdan ölüme kadar yaşanan süre.</text>
    <text x="368" y="138" font-size="10" fill="#1e293b">• <tspan font-weight="bold" fill="#115e59">Ecel:</tspan> Ömrün sona erdiği takdir edilmiş an.</text>
    <rect x="368" y="154" width="268" height="38" rx="6" fill="#ccfbf1"/>
    <text x="502" y="171" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#134e4a">Ölçü: Sağlığı korumak, hastalıkta tedavi olmak</text>
    <text x="502" y="185" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#134e4a">ve ömrü salih amellerle değerlendirmek.</text>
    """
    return svg(w, h, ic, "Rızık (er-Rezzak), Sabır (es-Sabûr), Ömür ve Ecel Kavramları")


def _gorsel_3():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">TEVEKKÜL VE TESLİMİYET ARASINDAKİ FARK (BİLGİ GÖRSELİ)</text>

    <!-- Sol: Tevekkül -->
    <rect x="28" y="54" width="285" height="154" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
    <text x="170" y="76" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">TEVEKKÜL (Süreç Aşaması)</text>
    <text x="44" y="100" font-size="10" fill="#1e293b">1. Yapılacak işte tüm bilimsel ve maddi</text>
    <text x="56" y="115" font-size="10" font-weight="bold" fill="#1e40af">tedbirler eksiksiz alınır.</text>
    <text x="44" y="136" font-size="10" fill="#1e293b">2. Çalışma ve gayret aşamasını kapsar.</text>
    <text x="44" y="157" font-size="10" fill="#1e293b">3. Gerekli çabadan sonra sonuç Allah'a (cc)</text>
    <text x="56" y="172" font-size="10" fill="#1e293b">bırakılır: <tspan font-weight="bold">"Önce deveni bağla, sonra</tspan></text>
    <text x="56" y="186" font-size="10" font-weight="bold" fill="#1d4ed8">Allah'a tevekkül et!"</tspan></text>

    <!-- Ok -->
    <line x1="320" y1="130" x2="355" y2="130" stroke="#475569" stroke-width="2.5"/>
    <polygon points="355,125 365,130 355,135" fill="#475569"/>

    <!-- Sağ: Teslimiyet ve Rıza -->
    <rect x="372" y="54" width="280" height="154" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <text x="512" y="76" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803d">TESLİMİYET VE RIZA (Sonuç Aşaması)</text>
    <text x="388" y="100" font-size="10" fill="#1e293b">1. Süreç, çalışma tamamlanıp <tspan font-weight="bold" fill="#166534">sonuç ortaya</tspan></text>
    <text x="400" y="115" font-size="10" font-weight="bold" fill="#166534">çıktıktan sonra başlar.</text>
    <text x="388" y="136" font-size="10" fill="#1e293b">2. Kişi sonucun Allah'tan (cc) geldiğine inanır</text>
    <text x="400" y="151" font-size="10" fill="#1e293b">ve isyan etmeden gönülden razı olur.</text>
    <text x="388" y="172" font-size="10" fill="#1e293b">3. <tspan font-weight="bold" fill="#15803d">Hz. Eyyüb (as):</tspan> Dua, sabır ve teslimiyetle</text>
    <text x="400" y="186" font-size="10" fill="#1e293b">ağır imtihanı gönül huzuruyla aşmıştır.</text>
    """
    return svg(w, h, ic, "Tevekkül ve Teslimiyet Arasındaki Temel Farklar")


def _gorsel_4():
    w, h = 680, 235
    ic = """
    <rect x="15" y="15" width="650" height="205" rx="14" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#881337">TOPLUMDAKİ YANLIŞ KADER ANLAYIŞI VE DOĞRU BAKIŞ</text>

    <!-- Sol: Yanlış Kader Algısının Sebepleri -->
    <rect x="28" y="52" width="295" height="152" rx="10" fill="#ffffff" stroke="#e11d48" stroke-width="1.8"/>
    <text x="175" y="73" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#be123c">YANLIŞ KADER ANLAYIŞININ BELİRTİLERİ</text>
    <text x="42" y="95" font-size="10" fill="#1e293b">✗ Kendi ihmal ve kusurlarını kadere yüklemek</text>
    <text x="42" y="115" font-size="10" fill="#1e293b">✗ Emek harcamadan rızık ve başarı beklemek</text>
    <text x="42" y="135" font-size="10" fill="#1e293b">✗ Tercihlerde cüzi iradenin rolünü yok saymak</text>
    <text x="42" y="155" font-size="10" fill="#1e293b">✗ "Alın yazım böyleymiş, hiçbir şeyi değiştiremem"</text>
    <text x="54" y="170" font-size="9.5" fill="#64748b">diyerek tembelliğe ve karamsarlığa sığınmak</text>

    <!-- Sağ: Kur'an'da Sahih Kader Bilinci -->
    <rect x="357" y="52" width="295" height="152" rx="10" fill="#ffffff" stroke="#059669" stroke-width="1.8"/>
    <text x="504" y="73" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#047857">KUR'AN'A GÖRE SAHİH KADER BİLİNCİ</text>
    <text x="371" y="95" font-size="10" fill="#1e293b">✓ <tspan font-weight="bold" fill="#065f46">İnsan, 3:</tspan> "Şüphesiz biz ona doğru yolu</text>
    <text x="383" y="110" font-size="9.5" fill="#334155">gösterdik; ister şükredici olur ister nankör."</text>
    <text x="371" y="130" font-size="10" fill="#1e293b">✓ <tspan font-weight="bold" fill="#065f46">Hidayet ve Hayır:</tspan> Doğru yolu ve iyiliği seçmek.</text>
    <text x="371" y="150" font-size="10" fill="#1e293b">✓ <tspan font-weight="bold" fill="#065f46">Dalalet ve Şer:</tspan> Kötülüğe sapmaktan kaçınmak.</text>
    <text x="371" y="170" font-size="10" fill="#1e293b">✓ Seçimlerinin sorumluluğunu üstlenmek.</text>
    """
    return svg(w, h, ic, "Yanlış Kader Anlayışı ile Kur'an'daki Sahih Kader Bilincinin Karşılaştırılması")


def _gorsel_5():
    w, h = 680, 235
    ic = """
    <rect x="15" y="15" width="650" height="205" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">AKIL, İRADE, HÜRRİYET VE SORUMLULUK (MÜKELLEF)</text>

    <!-- 4 Aşama Kutusu -->
    <rect x="25" y="56" width="148" height="146" rx="9" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.6"/>
    <text x="99" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">1. Akıl (Temyiz &amp; Tefrik)</text>
    <text x="99" y="98" text-anchor="middle" font-size="9.5" fill="#334155">Sebep-sonuç ilişkisini</text>
    <text x="99" y="113" text-anchor="middle" font-size="9.5" fill="#334155">kavrama (temyiz) ve</text>
    <text x="99" y="128" text-anchor="middle" font-size="9.5" fill="#334155">iyi-kötü ayrımını yapma</text>
    <text x="99" y="143" text-anchor="middle" font-size="9.5" fill="#334155">(tefrik) yeteneğidir.</text>
    <text x="99" y="175" text-anchor="middle" font-size="9" font-weight="bold" fill="#1e40af">(Beled, 8-10)</text>

    <rect x="184" y="56" width="148" height="146" rx="9" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.6"/>
    <text x="258" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">2. İrade ve Hürriyet</text>
    <text x="258" y="98" text-anchor="middle" font-size="9.5" fill="#334155">Yalnızca Allah'a kulluk</text>
    <text x="258" y="113" text-anchor="middle" font-size="9.5" fill="#334155">ederek nefsin ve dış</text>
    <text x="258" y="128" text-anchor="middle" font-size="9.5" fill="#334155">baskıların esaretinden</text>
    <text x="258" y="143" text-anchor="middle" font-size="9.5" fill="#334155">kurtulup seçim yapma.</text>
    <text x="258" y="175" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">(Özgür Tercih)</text>

    <rect x="343" y="56" width="148" height="146" rx="9" fill="#fefce8" stroke="#ca8a04" stroke-width="1.6"/>
    <text x="417" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#a16207">3. Mükellef Olma</text>
    <text x="417" y="98" text-anchor="middle" font-size="9.5" fill="#334155">Akli dengesi yerinde</text>
    <text x="417" y="113" text-anchor="middle" font-size="9.5" fill="#334155">ve ergenlik çağına</text>
    <text x="417" y="128" text-anchor="middle" font-size="9.5" fill="#334155">ulaşmış bireyin emir ve</text>
    <text x="417" y="143" text-anchor="middle" font-size="9.5" fill="#334155">yasaklara muhataplığı.</text>
    <text x="417" y="175" text-anchor="middle" font-size="9" font-weight="bold" fill="#854d0e">(Dini Yükümlülük)</text>

    <rect x="502" y="56" width="153" height="146" rx="9" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.6"/>
    <text x="578" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#6d28d9">4. Tedbir ve Güvenlik</text>
    <text x="578" y="98" text-anchor="middle" font-size="9.5" fill="#334155">4-10 Mayıs İş Sağlığı</text>
    <text x="578" y="113" text-anchor="middle" font-size="9.5" fill="#334155">ve Güvenliği Haftası:</text>
    <text x="578" y="128" text-anchor="middle" font-size="9.5" fill="#334155">Koruyucu ekipman ve</text>
    <text x="578" y="143" text-anchor="middle" font-size="9.5" fill="#334155">toplumsal sorumluluk.</text>
    <text x="578" y="175" text-anchor="middle" font-size="9" font-weight="bold" fill="#5b21b6">(Bireysel/Toplumsal Hak)</text>
    """
    return svg(w, h, ic, "Akıl, İrade, Hürriyet ve Mükellefiyet İlişkisi")


def _gorsel_6():
    w, h = 680, 235
    ic = """
    <rect x="15" y="15" width="650" height="205" rx="14" fill="#f0fdfa" stroke="#14b8a6" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#134e4a">ALLAH'IN (CC) KADERLE İLGİLİ SIFATLARI VE İNSAN SORUMLULUĞU</text>

    <!-- 3 Sıfat Kutusu -->
    <rect x="28" y="54" width="198" height="102" rx="9" fill="#ffffff" stroke="#0d9488" stroke-width="1.6"/>
    <text x="127" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f766e">İLİM (Her Şeyi Bilir)</text>
    <text x="127" y="93" text-anchor="middle" font-size="9.5" fill="#334155">Duyular âlemine ve duyu</text>
    <text x="127" y="108" text-anchor="middle" font-size="9.5" fill="#334155">ötesine ait geçmiş-gelecek</text>
    <text x="127" y="123" text-anchor="middle" font-size="9.5" fill="#334155">tüm olayları kuşatan bilgi.</text>

    <rect x="241" y="54" width="198" height="102" rx="9" fill="#ffffff" stroke="#0284c7" stroke-width="1.6"/>
    <text x="340" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">İRADE (Dilediğini Yapar)</text>
    <text x="340" y="93" text-anchor="middle" font-size="9.5" fill="#334155">Emir, hüküm ve fiillerinde</text>
    <text x="340" y="108" text-anchor="middle" font-size="9.5" fill="#334155">hiçbir zorunluluğa bağlı</text>
    <text x="340" y="123" text-anchor="middle" font-size="9.5" fill="#334155">olmadan dilemesi (Külli İrade).</text>

    <rect x="454" y="54" width="198" height="102" rx="9" fill="#ffffff" stroke="#7c3aed" stroke-width="1.6"/>
    <text x="553" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#6d28d9">KUDRET (Her Şeye Gücü Yeter)</text>
    <text x="553" y="93" text-anchor="middle" font-size="9.5" fill="#334155">Dilediğini eksiği ve fazlası</text>
    <text x="553" y="108" text-anchor="middle" font-size="9.5" fill="#334155">olmaksızın hikmet ve ölçü</text>
    <text x="553" y="123" text-anchor="middle" font-size="9.5" fill="#334155">çerçevesinde yaratması.</text>

    <!-- Alt Bant: Ayet İlkeleri -->
    <rect x="28" y="166" width="624" height="42" rx="8" fill="#ccfbf1" stroke="#0d9488"/>
    <text x="340" y="184" text-anchor="middle" font-size="10" font-weight="bold" fill="#115e59">"İnsan için ancak çalıştığı vardır." (Necm, 39)  •  "Allah her şahsı ancak gücünün yettiği ölçüde yükümlü kılar." (Bakara, 286)</text>
    <text x="340" y="199" text-anchor="middle" font-size="9.2" fill="#134e4a">Allah'ın (cc) ilim, irade ve kudreti insanın cüzi iradesiyle yaptığı seçimlerin sorumluluğunu ortadan kaldırmaz.</text>
    """
    return svg(w, h, ic, "Allah'ın Kaderle İlgili Sıfatları (İlim, İrade, Kudret) ve İnsan Sorumluluğu")


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
