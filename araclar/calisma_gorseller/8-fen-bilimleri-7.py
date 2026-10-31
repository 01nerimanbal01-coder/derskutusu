"""8. sınıf Fen Bilimleri 7. hafta (Kalıtım: İnsanda Cinsiyetin Belirlenmesi, Soy Ağaçları ve Akraba Evliliğinin Genetik Sonuçları) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK; eğik kesir yok K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="1.8"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def cinsiyet_caprazlama_sema():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'İnsanda Eşey Kromozomlarının Çaprazlanması (XX × XY)', 12, MAVI)
    # Anne ve Baba kutuları
    ic += f'<rect x="20" y="34" width="166" height="40" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.5"/>'
    ic += yazi(103, 51, 'Dişi Ebeveyn: 44+XX', 11, MOR)
    ic += yazi(103, 67, 'Yumurta: 22+X', 10.5, LAC, ince=True)

    ic += f'<rect x="20" y="80" width="166" height="40" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(103, 97, 'Erkek Ebeveyn: 44+XY', 11, MAVI)
    ic += yazi(103, 113, 'Sperm: 22+X veya 22+Y', 10.5, LAC, ince=True)

    # Sağ: Punnett tablosu ve sonuçlar
    ic += f'<rect x="206" y="34" width="372" height="86" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(392, 52, 'Oluşabilecek Eşey Kromozomu Eşleşmeleri', 11.2, TUR)
    kutular = [
        ('XX', 'Kız (%25)', MOR, MOR_A),
        ('XY', 'Erkek (%25)', MAVI, MAVI_A),
        ('XX', 'Kız (%25)', MOR, MOR_A),
        ('XY', 'Erkek (%25)', MAVI, MAVI_A),
    ]
    for i, (krm, ad, renk, arka) in enumerate(kutular):
        x = 218 + i * 88
        ic += f'<rect x="{x}" y="60" width="80" height="50" rx="7" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 40, 80, krm, 11.5, renk)
        ic += yazi(x + 40, 98, ad, 10.5, LAC, ince=True)
    return svg(600, 134, ic, 'İnsanda eşey kromozomları çaprazlama modeli: Dişi 44+XX ve Erkek 44+XY çaprazlamasıyla %50 XX kız ve %50 XY erkek olasılığı.', 14)


def soy_agaci_kulak_sema():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(190, 24, 'Soy Ağacı (Boyalı: Yapışık Kulak Memeli - aa)', 11.5, KAHVE)
    # 1. kuşak: Anne (1 - daire, boyasız) ve Baba (2 - kare, boyasız)
    ic += f'<circle cx="110" cy="52" r="16" fill="#fff" stroke="{MOR}" stroke-width="2.2"/>'
    ic += yazi(110, 56, '1', 11.5, MOR)
    ic += f'<line x1="126" y1="52" x2="214" y2="52" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="214" y="36" width="32" height="32" rx="4" fill="#fff" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += yazi(230, 56, '2', 11.5, MAVI)
    # Soy çizgileri
    ic += f'<line x1="170" y1="52" x2="170" y2="76" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="90" y1="76" x2="250" y2="76" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="90" y1="76" x2="90" y2="88" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="170" y1="76" x2="170" y2="88" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="250" y1="76" x2="250" y2="88" stroke="{LAC}" stroke-width="2"/>'
    # Çocuklar: Sol (daire, boyasız), Orta (3 - kare, boyalı), Sağ (kare, boyasız)
    ic += f'<circle cx="90" cy="102" r="14" fill="#fff" stroke="{MOR}" stroke-width="2"/>'
    ic += f'<rect x="156" y="88" width="28" height="28" rx="4" fill="{TUR}" stroke="{KAHVE}" stroke-width="2"/>'
    ic += yazi(170, 106, '3', 11.5, '#fff')
    ic += f'<rect x="236" y="88" width="28" height="28" rx="4" fill="#fff" stroke="{MAVI}" stroke-width="2"/>'

    # Sağ bilgi anahtarı
    ic += f'<rect x="348" y="22" width="232" height="96" rx="8" fill="#fff" stroke="{KAHVE}" stroke-width="1.4"/>'
    ic += yazi(464, 40, 'Sembol ve Gen Bilgisi', 11.5, KAHVE)
    ic += yazi(362, 60, 'Ayrık kulak memesi: Baskın (A)', 10.5, LAC, 'start', ince=True)
    ic += yazi(362, 78, 'Yapışık kulak memesi: Çekinik (a)', 10.5, LAC, 'start', ince=True)
    ic += yazi(362, 96, 'Daire: Dişi · Kare: Erkek', 10.5, MAVI, 'start')
    ic += yazi(362, 111, 'Boyalı (3): Özelliği gösteren (aa)', 10.5, TUR, 'start')
    return svg(600, 134, ic, 'Soy ağacı şeması: 1 numaralı dişi ve 2 numaralı erkek ebeveynden 3 numaralı boyalı (çekinik özellikli) çocuk oluşumu.', 14)


def kalitsal_hastalik_kartlari():
    kartlar = [
        ('1. Kart · Genotip: AA', 'İki baskın alel taşır.', 'Hastalık aleli (a) bulundurmaz.', YES, YES_A),
        ('2. Kart · Genotip: Aa', 'Biri baskın iki alel taşır.', 'Dış görünüşte sağlamdır.', TUR, TUR_A),
        ('3. Kart · Genotip: aa', 'İki çekinik hastalık aleli taşır.', 'Hastalık etkisini gösterir.', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="6" width="192" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 96, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 178}" y2="34" stroke="{renk}" stroke-width="1.2" stroke-dasharray="3 2"/>'
        ic += yazi(x + 96, 54, s1, 10.5, LAC, ince=True)
        ic += yazi(x + 96, 74, s2, 10.5, LAC, ince=True)
    return svg(600, 98, ic, 'Çekinik kalıtsal hastalıklar için AA, Aa ve aa genotip kartları.', 14)


def hucre_kromozom_sema():
    ic = f'<rect x="6" y="6" width="286" height="102" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'Sağlıklı Dişi Birey (2n = 46)', 11.5, MOR)
    ic += yazi(149, 46, 'Vücut Hücresi: 44+XX', 11, LAC)
    ic += f'<rect x="28" y="58" width="242" height="38" rx="7" fill="#fff" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(149, 81, 'Mayoz → Yumurta Hücresi (n = 23): ?', 10.8, MOR)

    ic += f'<rect x="308" y="6" width="286" height="102" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'Sağlıklı Erkek Birey (2n = 46)', 11.5, MAVI)
    ic += yazi(451, 46, 'Vücut Hücresi: 44+XY', 11, LAC)
    ic += f'<rect x="330" y="58" width="242" height="38" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(451, 81, 'Mayoz → Sperm Hücreleri (n = 23): ?', 10.8, MAVI)
    return svg(600, 114, ic, 'Dişi (44+XX) ve erkek (44+XY) bireylerin vücut ve üreme hücrelerindeki kromozom dağılımı şeması.', 14)


def soy_agaci_cozum_akis():
    adlar = [
        ('1. Adım', 'Sembolleri Tanı', MAVI, MAVI_A),
        ('2. Adım', 'Boyalılara aa Yaz', TUR, TUR_A),
        ('3. Adım', 'a’ları Dağıt', MOR, MOR_A),
        ('4. Adım', 'Taşıyıcı: Aa', YES, YES_A),
        ('5. Adım', 'Sağlam Çocuk', ALTIN, '#fffbe6'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += f'<rect x="{x}" y="10" width="104" height="68" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 52, 34, ust, 11, renk)
        ic += yazi(x + 52, 56, alt, 10.2, LAC, ince=True)
        if i < 4:
            ic += f'<line x1="{x + 105}" y1="44" x2="{x + 118}" y2="44" stroke="{LAC}" stroke-width="1.8"/>'
            ic += f'<path d="M{x + 114} 40 l4 4 l-4 4" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    return svg(600, 88, ic, 'Soy ağacı sorularını 5 adımda çözümleme akış şeması.', 14)


def akraba_evliligi_grafik():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'K ve L Bölgelerinde Akraba Evliliği ve Çekinik Hastalık Sıklığı', 11.8, LAC)
    # Sol grafik: K Bölgesi
    ic += f'<rect x="20" y="34" width="268" height="84" rx="8" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(154, 52, 'K Bölgesi (Akraba Evliliği Yüksek)', 11, KIR)
    ic += f'<rect x="36" y="64" width="210" height="16" rx="4" fill="{KIR}"/>'
    ic += yazi(141, 76, 'Çekinik Hastalık (aa) Oranı: Yüksek', 10.5, '#fff')
    ic += yazi(154, 102, 'Ortak atadan gelen a alelleri sık buluşur', 10.5, LAC, ince=True)

    # Sağ grafik: L Bölgesi
    ic += f'<rect x="312" y="34" width="268" height="84" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(446, 52, 'L Bölgesi (Akraba Evliliği Düşük)', 11, YESIL_K)
    ic += f'<rect x="328" y="64" width="68" height="16" rx="4" fill="{YES}"/>'
    ic += yazi(404, 76, 'Hastalık (aa) Oranı: Düşük', 10.5, YESIL_K, 'start')
    ic += yazi(446, 102, 'Aynı çekinik alelin buluşma olasılığı azdır', 10.5, LAC, ince=True)
    return svg(600, 134, ic, 'K ve L bölgelerinde akraba evliliği oranına bağlı çekinik kalıtsal hastalık sıklığı karşılaştırması.', 14)


def tasiyici_caprazlama_sema():
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'İki Taşıyıcı Ebeveynin Çaprazlanması: Aa (Anne) × Aa (Baba)', 11.8, MAVI)
    kutular = [
        ('AA (%25)', 'Sağlıklı', 'Hastalık aleli yok', YES, YES_A),
        ('Aa (%25)', 'Sağlıklı görünür', 'Taşıyıcı (Heterozigot)', TUR, TUR_A),
        ('Aa (%25)', 'Sağlıklı görünür', 'Taşıyıcı (Heterozigot)', TUR, TUR_A),
        ('aa (%25)', 'Hasta Birey', 'Homozigot çekinik', KIR, '#fdeaea'),
    ]
    for i, (ust, s1, s2, renk, arka) in enumerate(kutular):
        x = 14 + i * 144
        ic += f'<rect x="{x}" y="34" width="136" height="76" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 68, 52, ust, 11.5, renk)
        ic += yazi(x + 68, 72, s1, 10.5, LAC)
        ic += yazi(x + 68, 90, s2, 10.2, LAC, ince=True)
    return svg(600, 126, ic, 'Taşıyıcı anne (Aa) ve taşıyıcı babanın (Aa) çaprazlama tablosu: %25 AA, %50 Aa, %25 aa.', 14)


def iki_kusak_soy_agaci():
    ic = f'<rect x="6" y="6" width="588" height="112" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'İki Aileli Soy Ağacı Kesiti (Boyalı Bireyler: aa)', 11.8, KAHVE)
    # Sol aile: K bireyi ve eşi -> aa çocuk
    ic += f'<rect x="20" y="34" width="268" height="74" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(154, 52, '1. Aile: Sağlam Ebeveyn K → Boyalı Çocuk', 10.8, MAVI)
    ic += yazi(154, 72, 'K (Sağlam) × Eş (Sağlam) → Çocuk: aa (Boyalı)', 10.5, LAC, ince=True)
    ic += yazi(154, 92, 'Çocuktaki “a” alellerinden biri K’dendir.', 10.5, MAVI)

    # Sağ aile: Boyalı anne (aa) -> Sağlam çocuk L
    ic += f'<rect x="312" y="34" width="268" height="74" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(446, 52, '2. Aile: Boyalı Anne (aa) → Sağlam Çocuk L', 10.8, TUR)
    ic += yazi(446, 72, 'Anne (aa) × Baba → Çocuk L (Sağlam)', 10.5, LAC, ince=True)
    ic += yazi(446, 92, 'Anne (aa) çocuğuna mutlaka “a” aleli aktarır.', 10.5, TUR)
    return svg(600, 124, ic, 'K ve L bireylerinin heterozigot (Aa) olma nedenlerini gösteren iki aileli soy ağacı özeti.', 14)


def genetik_danismanlik_pano():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'Akraba Evliliğinde Risk Durumu', 11.5, TUR)
    ic += yazi(22, 48, 'Ortak atadan gelen çekinik alellerin (a)', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 65, '  bir araya gelme (aa) olasılığı yükselir.', 10.5, LAC, 'start', ince=True)
    ic += yazi(22, 84, 'Taşıyıcı çiftte (Aa × Aa) risk %25’tir.', 10.5, TUR, 'start')

    ic += f'<rect x="308" y="6" width="286" height="98" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'Akraba Olmayan Çiftler ve Tarama', 11.5, YESIL_K)
    ic += yazi(324, 48, 'Kan bağı olmayan iki kişi de tesadüfen', 10.5, LAC, 'start', ince=True)
    ic += yazi(324, 65, '  aynı hastalığın taşıyıcısı (Aa) olabilir.', 10.5, LAC, 'start', ince=True)
    ic += yazi(324, 84, 'Evlilik öncesi genetik tarama önerilir.', 10.5, YESIL_K, 'start')
    return svg(600, 110, ic, 'Akraba evliliğinde kalıtsal hastalık riski ve evlilik öncesi genetik tarama panosu.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cinsiyet_caprazlama_sema()
    s[4]['gorsel'] = soy_agaci_kulak_sema()
    s[5]['gorsel'] = kalitsal_hastalik_kartlari()
    s[6]['gorsel'] = hucre_kromozom_sema()
    s[7]['gorsel'] = soy_agaci_cozum_akis()
    s[8]['gorsel'] = akraba_evliligi_grafik()
    s[9]['gorsel'] = tasiyici_caprazlama_sema()
    s[10]['gorsel'] = iki_kusak_soy_agaci()
    s[12]['gorsel'] = genetik_danismanlik_pano()
