from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">أَرْكَانُ الْإِيمَانِ وَأَسْمَاءُ اللّٰهِ الْحُسْنَى (İman Esasları ve Esmaülhüsna)</text>

    <rect x="30" y="75" width="315" height="210" rx="12" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="187" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">أَرْكَانُ الْإِيمَانِ السِّتَّةُ (6 İman Esası)</text>
    <text x="50" y="130" font-size="13" fill="#134e4a">1. الْإِيمَانُ بِاللّٰهِ (Allah'a İman - Merkez)</text>
    <text x="50" y="155" font-size="13" fill="#134e4a">2. الْمَلَائِكَةُ (Melekler)</text>
    <text x="50" y="180" font-size="13" fill="#134e4a">3. الْكُتُبُ السَّمَاوِيَّةُ (İlahi Kitaplar)</text>
    <text x="50" y="205" font-size="13" fill="#134e4a">4. الرُّسُلُ (Peygamberler)</text>
    <text x="50" y="230" font-size="13" fill="#134e4a">5. الْآخِرَةُ (Ahiret Günü)</text>
    <text x="50" y="255" font-size="13" fill="#134e4a">6. الْقَضَاءُ وَالْقَدَرُ (Kaza ve Kader)</text>

    <rect x="375" y="75" width="315" height="210" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="532" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">أَسْمَاءُ اللّٰهِ الْحُسْنَى (Terkip Analizi)</text>
    <rect x="395" y="118" width="275" height="45" rx="8" fill="#fef3c7"/>
    <text x="532" y="138" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">أَسْمَاءُ اللّٰهِ (İsim Tamlaması)</text>
    <text x="532" y="155" text-anchor="middle" font-size="12" fill="#78350f">اِسْمٌ (Tekil) → أَسْمَاءٌ (Çoğul: İsimler)</text>
    <rect x="395" y="175" width="275" height="45" rx="8" fill="#fef3c7"/>
    <text x="532" y="195" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">الْحُسْنَى (Sıfat: En Güzel)</text>
    <text x="532" y="212" text-anchor="middle" font-size="12" fill="#78350f">لَهُ الْأَسْمَاءُ الْحُسْنَى (Haşr, 24)</text>
    <text x="532" y="255" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309">"En güzel isimler O'nundur"</text>
    """
    return svg(720, 300, ic, "İman Esasları ve Esmaülhüsna Terkibi")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">سُورَةُ الْحَشْرِ (22): هُوَ اللّٰهُ الَّذِي لَا إِلٰهَ إِلَّا هُوَ عَالِمُ الْغَيْبِ وَالشَّهَادَةِ</text>

    <rect x="35" y="80" width="310" height="190" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="190" y="112" text-anchor="middle" font-size="22" font-weight="bold" fill="#1d4ed8">اَلرَّحْمٰنُ (Er-Rahmân)</text>
    <text x="190" y="142" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">Kök: ر - ح - م (Rahmet)</text>
    <text x="190" y="172" text-anchor="middle" font-size="13" fill="#1e3a8a">• Dünya hayatında mümin-kâfir</text>
    <text x="190" y="194" text-anchor="middle" font-size="13" fill="#1e3a8a">ayrımı yapmadan bütün varlıklara</text>
    <text x="190" y="216" text-anchor="middle" font-size="13" fill="#1e3a8a">rızık ve merhamet edendir.</text>
    <text x="190" y="246" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">Yalnızca Allah için kullanılır.</text>

    <rect x="375" y="80" width="310" height="190" rx="12" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="530" y="112" text-anchor="middle" font-size="22" font-weight="bold" fill="#15803d">اَلرَّحِيمُ (Er-Rahîm)</text>
    <text x="530" y="142" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">Kök: ر - ح - م (Rahmet)</text>
    <text x="530" y="172" text-anchor="middle" font-size="13" fill="#14532d">• Ahiret yurdunda yalnızca</text>
    <text x="530" y="194" text-anchor="middle" font-size="13" fill="#14532d">mümin kullarına özel şefkat,</text>
    <text x="530" y="216" text-anchor="middle" font-size="13" fill="#14532d">bağışlama ve ikramda bulunandır.</text>
    <text x="530" y="246" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">هُوَ الرَّحْمٰنُ الرَّحِيمُ</text>
    """
    return svg(720, 290, ic, "Haşr Suresi 22. Ayet: Er-Rahmân ve Er-Rahîm")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Haşr Suresi 23. Ayet (1. Bölüm): Hükümranlık, Kutsiyet ve Esenlik</text>

    <rect x="25" y="80" width="210" height="190" rx="12" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="130" y="115" text-anchor="middle" font-size="20" font-weight="bold" fill="#5b21b6">اَلْمَلِكُ</text>
    <text x="130" y="140" text-anchor="middle" font-size="14" font-weight="bold" fill="#6d28d9">El-Melik</text>
    <text x="130" y="170" text-anchor="middle" font-size="12" fill="#4c1d95">Bütün mülkün ve</text>
    <text x="130" y="190" text-anchor="middle" font-size="12" fill="#4c1d95">kâinatın gerçek sahibi,</text>
    <text x="130" y="210" text-anchor="middle" font-size="12" fill="#4c1d95">mutlak hükümdarı</text>
    <text x="130" y="245" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">Kök: م - ل - ك</text>

    <rect x="255" y="80" width="210" height="190" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="360" y="115" text-anchor="middle" font-size="20" font-weight="bold" fill="#9d174d">اَلْقُدُّوسُ</text>
    <text x="360" y="140" text-anchor="middle" font-size="14" font-weight="bold" fill="#be185d">El-Kuddûs</text>
    <text x="360" y="170" text-anchor="middle" font-size="12" fill="#831843">Her türlü eksiklik,</text>
    <text x="360" y="190" text-anchor="middle" font-size="12" fill="#831843">kusur ve noksandan</text>
    <text x="360" y="210" text-anchor="middle" font-size="12" fill="#831843">münezzeh (tertemiz)</text>
    <text x="360" y="245" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">Kök: ق - د - س</text>

    <rect x="485" y="80" width="210" height="190" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="590" y="115" text-anchor="middle" font-size="20" font-weight="bold" fill="#065f46">اَلسَّلَامُ</text>
    <text x="590" y="140" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">Es-Selâm</text>
    <text x="590" y="170" text-anchor="middle" font-size="12" fill="#064e3b">Esenlik ve barış</text>
    <text x="590" y="190" text-anchor="middle" font-size="12" fill="#064e3b">kaynağı, kullarını</text>
    <text x="590" y="210" text-anchor="middle" font-size="12" fill="#064e3b">selamete çıkaran</text>
    <text x="590" y="245" text-anchor="middle" font-size="12" font-weight="bold" fill="#065f46">Kök: س - ل - م</text>
    """
    return svg(720, 290, ic, "El-Melik, El-Kuddûs ve Es-Selâm İsimleri")


def gorsel_4():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#7c2d12"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Haşr Suresi 23. Ayet (2. Bölüm): الْمُؤْمِنُ الْمُهَيْمِنُ الْعَزِيزُ الْجَبَّارُ الْمُتَكَبِّرُ</text>

    <rect x="25" y="75" width="320" height="92" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="16" font-weight="bold" fill="#9a3412">اَلْمُؤْمِنُ (El-Mü'min)</text>
    <text x="185" y="126" text-anchor="middle" font-size="12" fill="#7c2d12">Gönüllere iman bahşeden, kendine</text>
    <text x="185" y="146" text-anchor="middle" font-size="12" fill="#7c2d12">sığınanlara güven ve emniyet veren</text>

    <rect x="375" y="75" width="320" height="92" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="16" font-weight="bold" fill="#9a3412">اَلْمُهَيْمِنُ (El-Müheymin)</text>
    <text x="535" y="126" text-anchor="middle" font-size="12" fill="#7c2d12">Bütün varlıkları her an görüp</text>
    <text x="535" y="146" text-anchor="middle" font-size="12" fill="#7c2d12">gözeten, koruyan ve denetleyen</text>

    <rect x="25" y="182" width="210" height="100" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="130" y="208" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">اَلْعَزِيزُ (El-Azîz)</text>
    <text x="130" y="232" text-anchor="middle" font-size="12" fill="#7f1d1d">Mutlak güç ve üstünlük</text>
    <text x="130" y="252" text-anchor="middle" font-size="12" fill="#7f1d1d">sahibi, yenilmeyen</text>

    <rect x="255" y="182" width="210" height="100" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="360" y="208" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">اَلْجَبَّارُ (El-Cebbâr)</text>
    <text x="360" y="232" text-anchor="middle" font-size="12" fill="#7f1d1d">İradesini yürüten,</text>
    <text x="360" y="252" text-anchor="middle" font-size="12" fill="#7f1d1d">kırılanları onaran</text>

    <rect x="485" y="182" width="210" height="100" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="590" y="208" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">اَلْمُتَكَبِّرُ (El-Mütekebbir)</text>
    <text x="590" y="232" text-anchor="middle" font-size="12" fill="#7f1d1d">Ululuk ve büyüklükte</text>
    <text x="590" y="252" text-anchor="middle" font-size="12" fill="#7f1d1d">eşi benzeri olmayan</text>
    """
    return svg(720, 300, ic, "Güven, Koruma ve Mutlak Kudret İsimleri")


def gorsel_5():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#065f46"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Haşr Suresi 24. Ayet: Yaratılışın Üç Aşaması ve İlahi Hikmet</text>

    <rect x="25" y="80" width="155" height="185" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="102" y="110" text-anchor="middle" font-size="18" font-weight="bold" fill="#047857">1. اَلْخَالِقُ</text>
    <text x="102" y="132" text-anchor="middle" font-size="13" font-weight="bold" fill="#065f46">El-Hâlık</text>
    <text x="102" y="160" text-anchor="middle" font-size="12" fill="#064e3b">Yoktan takdir</text>
    <text x="102" y="180" text-anchor="middle" font-size="12" fill="#064e3b">edip ölçüsünü</text>
    <text x="102" y="200" text-anchor="middle" font-size="12" fill="#064e3b">planlayan</text>
    <text x="102" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">Takdir ve Plan</text>

    <rect x="200" y="80" width="155" height="185" rx="10" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="277" y="110" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f766e">2. اَلْبَارِئُ</text>
    <text x="277" y="132" text-anchor="middle" font-size="13" font-weight="bold" fill="#115e59">El-Bâri'</text>
    <text x="277" y="160" text-anchor="middle" font-size="12" fill="#134e4a">Uyumlu ve</text>
    <text x="277" y="180" text-anchor="middle" font-size="12" fill="#134e4a">kusursuz düzenle</text>
    <text x="277" y="200" text-anchor="middle" font-size="12" fill="#134e4a">varlığa çıkaran</text>
    <text x="277" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f766e">İcat ve Var Etme</text>

    <rect x="375" y="80" width="155" height="185" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="452" y="110" text-anchor="middle" font-size="18" font-weight="bold" fill="#1d4ed8">3. اَلْمُصَوِّرُ</text>
    <text x="452" y="132" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">El-Musavvir</text>
    <text x="452" y="160" text-anchor="middle" font-size="12" fill="#1e3a8a">Her varlığa</text>
    <text x="452" y="180" text-anchor="middle" font-size="12" fill="#1e3a8a">kendine özgü</text>
    <text x="452" y="200" text-anchor="middle" font-size="12" fill="#1e3a8a">şekil/suret veren</text>
    <text x="452" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">Tasvir ve Şekil</text>

    <rect x="550" y="80" width="145" height="185" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="622" y="110" text-anchor="middle" font-size="18" font-weight="bold" fill="#b45309">اَلْحَكِيمُ</text>
    <text x="622" y="132" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">El-Hakîm</text>
    <text x="622" y="160" text-anchor="middle" font-size="12" fill="#78350f">Her işi, emri</text>
    <text x="622" y="180" text-anchor="middle" font-size="12" fill="#78350f">ve yaratması</text>
    <text x="622" y="200" text-anchor="middle" font-size="12" fill="#78350f">hikmetli olan</text>
    <text x="622" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">İlahi Hikmet</text>
    """
    return svg(720, 285, ic, "El-Hâlık, El-Bâri', El-Musavvir ve El-Hakîm")


def gorsel_6():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Esmaülhüsna Cümle Kalıpları (الْجُمْلَةُ الِاسْمِيَّةُ وَالْفِعْلِيَّةُ)</text>

    <rect x="35" y="75" width="650" height="60" rx="10" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="360" y="100" text-anchor="middle" font-size="15" font-weight="bold" fill="#312e81">هُوَ اللّٰهُ الَّذِي لَا إِلٰهَ إِلَّا هُوَ (Tevhit Kalıbı)</text>
    <text x="360" y="122" text-anchor="middle" font-size="12" fill="#4338ca">"O, kendisinden başka ilah olmayan Allah'tır." (هُوَ: Müpteda | اللّٰهُ: Haber | الَّذِي: İsm-i Mevsul)</text>

    <rect x="35" y="148" width="650" height="60" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="360" y="173" text-anchor="middle" font-size="15" font-weight="bold" fill="#14532d">لِلّٰهِ الْأَسْمَاءُ الْحُسْنَى فَادْعُوهُ بِهَا (Dua Kalıbı - A'râf, 180)</text>
    <text x="360" y="195" text-anchor="middle" font-size="12" fill="#166534">"En güzel isimler Allah'ındır; öyleyse O'na bunlarla dua edin." (يَا رَحْمٰنُ ، يَا سَلَامُ ، يَا حَكِيمُ)</text>

    <rect x="35" y="221" width="650" height="60" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="360" y="246" text-anchor="middle" font-size="15" font-weight="bold" fill="#78350f">يُسَبِّحُ لَهُ مَا فِي السَّمَاوَاتِ وَالْأَرْضِ وَهُوَ الْعَزِيزُ الْحَكِيمُ</text>
    <text x="360" y="268" text-anchor="middle" font-size="12" fill="#92400e">"Göklerde ve yerde ne varsa O'nu tesbih eder. O, mutlak güç ve hikmet sahibidir." (Haşr, 24)</text>
    """
    return svg(720, 295, ic, "Esmaülhüsna İle İlgili Cümle Kalıpları")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
