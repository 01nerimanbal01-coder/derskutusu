"""5. sınıf Türkçe 3. hafta (Topsuz Basketbol Oyunu: Tahmin, Anlam, Noktalama ve Ses Kullanımı) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def tahmin_duraklari_sema():
    kutular = [
        ('Okumadan Önce', 'Başlıktan ilk tahmin', 've gerekçe kaydı', MAVI, MAVI_A, False),
        ('K Durağı (1. Yer)', 'Moni fikir bulunca', 'Tahmin + gerekçe : ?', TUR, '#fff', True),
        ('2. Numaralı Durak', 'İnci yardım çağırınca', 'yeni tahmin + gerekçe', MOR, MOR_A, False),
        ('L Adımı (Okuma Sonu)', 'Okuma tamamlanınca', 'Değerlendirme : ?', YES, '#fff', True),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka, kesik) in enumerate(kutular):
        x = 8 + i * 148
        ek = ' stroke-dasharray="5 3"' if kesik else ''
        ic += f'<rect x="{x}" y="8" width="134" height="88" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"{ek}/>'
        ic += f'<rect x="{x}" y="8" width="134" height="24" rx="10" fill="{renk}"/><rect x="{x}" y="22" width="134" height="10" fill="{renk}"/>'
        ic += yazi(x + 67, 24, bas, 10.6, '#fff')
        ic += yazi(x + 67, 54, s1, 10.8, LAC, ince=not kesik)
        ic += yazi(x + 67, 74, s2, 10.8, renk if kesik else LAC, ince=not kesik)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="52" x2="{x + 146}" y2="52" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 142} 47 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 104, ic, 'Tahmin çalışma kâğıdı akışı: Okumadan önce, K durağı (1. yer), 2. numaralı durak ve L adımı (okuma sonu).', 22)


def nokta_gorev_kartlari():
    kartlar = [
        ('1. Kart', '08.10.2026 günü okul turnuvası', 'Görev: Gün, ay ve yılı ayırma', MAVI, MAVI_A),
        ('2. Kart', 'Takımımız 2. kademeye yükseldi.', 'Görev: Sıra bildiren sayı sonu', YES, YES_A),
        ('3. Kart', 'Çınar Cad. spor salonunda maç', 'Görev: Cümlenin bittiğini gösterme', KIR, '#fdeaea'),
        ('4. Kart', 'Antrenman tam 45 dk. sürdü.', 'Görev: Kısaltmanın sonuna konma', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ornek, gorev, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, f'{bas}: {ornek}', 10.8, LAC, 'start')
        ic += yazi(x + 18, y + 38, gorev, 10.5, renk, 'start', ince=True)
    return svg(600, 124, ic, 'Dört nokta görevi kartı: 1. tarih, 2. sıra sayısı, 3. Cad. kısaltması için yanlış yazılmış görev, 4. dk. kısaltması.', 23)


def gercek_hayal_sahne_panosu():
    kartlar = [
        ('1. Kart', 'Moni’nin kendi ağzıyla', 'siren sesi çıkarması', MAVI, MAVI_A),
        ('2. Kart', 'Mete’nin Satürn’deki bir', 'hastanede iyileşmesi', TUR, TUR_A),
        ('3. Kart', 'Çocukların saha içinde', 'neşeyle koşuşturması', YES, YES_A),
        ('4. Kart', 'Çantadan sedye, buz ve', 'sargı bezi çıkarılması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.4, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.4, LAC, ince=True)
    return svg(600, 104, ic, 'Topsuz Basketbol Oyunu dört sahne kartı: siren sesi, Satürn hastanesi, neşeli koşuşturma, sedye ve sargı bezi.', 22)


def acik_bilgi_yorum_panosu():
    ic = f'<rect x="8" y="8" width="282" height="92" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Not 1 (Okuma Kaydı)', 11.2, MAVI)
    ic += yazi(149, 52, '“İnci, yerde kıvranan Mete’yi', 10.8, LAC, ince=True)
    ic += yazi(149, 70, 'görünce sağlık görevlilerini', 10.8, LAC, ince=True)
    ic += yazi(149, 88, 'yardıma çağırdı.”', 10.8, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Not 2 (Okuma Kaydı)', 11.2, TUR)
    ic += yazi(451, 52, '“Mete gezegenlere ilgi duyduğu', 10.8, LAC, ince=True)
    ic += yazi(451, 70, 'için tedavi yeri olarak Satürn’ü', 10.8, LAC, ince=True)
    ic += yazi(451, 88, 'seçmiş olabilir.”', 10.8, LAC, ince=True)
    return svg(600, 108, ic, 'İki okuma notu: Not 1 İnci’nin sağlık görevlilerini çağırması, Not 2 Mete’nin Satürn’ü seçme nedeni tahmini.', 22)


def arac_secim_dongusu_sema():
    adimlar = [
        ('Amaç ve İhtiyaç', 'Okuma öncesi düşünme', MAVI, MAVI_A),
        ('Araç Seçimi', 'Sözlük / çalışma kâğıdı', MOR, MOR_A),
        ('Esnek Değişim', 'Yetmezse yeni araç ekle', TUR, TUR_A),
        ('Değerlendirme', 'Katkısını gözden geçir', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11.2, renk)
        ic += yazi(x + 68, 62, alt, 10.4, LAC, ince=True)
    return svg(600, 96, ic, 'Okuma araçlarını seçme ve değerlendirme adımları: amaç belirleme, araç seçimi, esnek değişim ve değerlendirme.', 22)


def ses_ok_yonu_karti():
    satirlar = [
        ('1. Cümle: “Turnuva şimdi başlıyor!”', '↑ (Yukarı ok)', 'Uygulama: Ses yükseltildi', YES, YES_A),
        ('2. Cümle: “Yedek formalar nerede?”', '↑ (Yukarı ok)', 'Uygulama: Ses yükseltildi', MAVI, MAVI_A),
        ('3. Cümle: “Antrenman saat beşte bitti.”', '↓ (Aşağı ok)', 'Uygulama: Ses alçaltıldı', MOR, MOR_A),
        ('4. Cümle: “Yarın sahada buluşuruz.”', '↓ (Aşağı ok)', 'Uygulama: Ses yükseltildi', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (cumle, ok_y, uyg, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 20, cumle, 10.6, LAC, 'start')
        ic += yazi(x + 14, y + 39, f'{ok_y} — {uyg}', 10.4, renk, 'start', ince=True)
    return svg(600, 124, ic, 'Dört cümlede ok yönü ve ses tonu uygulaması: 1, 2 ve 3 doğru; 4. cümlede aşağı oka rağmen ses yükseltilmiş.', 23)


def soz_varligi_kavram_agi():
    ic = f'<rect x="8" y="8" width="280" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(148, 26, '1. Bölüm: “Üzülmek” Sözcüğü', 11.2, MAVI)
    ic += f'<rect x="20" y="38" width="116" height="52" rx="7" fill="#fff" stroke="{MAVI}" stroke-width="1.3"/>'
    ic += yazi(78, 56, 'Yakın Anlamlısı', 10.4, MAVI)
    ic += yazi(78, 76, 'Kederlenmek', 11, LAC)
    ic += f'<rect x="156" y="38" width="116" height="52" rx="7" fill="#fff" stroke="{TUR}" stroke-width="1.3"/>'
    ic += yazi(214, 56, 'Zıt Anlamlısı', 10.4, TUR)
    ic += yazi(214, 76, 'Sevinmek', 11, LAC)

    ic += f'<rect x="304" y="8" width="288" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(448, 26, '2. Bölüm: “Kaz” Sözcüğü', 11.2, YESIL_K)
    ic += yazi(318, 52, '1. Cümle: Gölde beyaz bir kaz yüzüyordu.', 10.5, LAC, 'start', ince=True)
    ic += yazi(318, 74, '2. Cümle: Fidan dikmek için toprağı kaz.', 10.5, LAC, 'start', ince=True)
    ic += yazi(318, 92, '(Aynı yazılış, iki farklı anlam)', 10.3, YESIL_K, 'start')
    return svg(600, 112, ic, 'Söz varlığı kartı: Üzülmek kelimesinin yakın anlamlısı kederlenmek, zıt anlamlısı sevinmek; kaz kelimesinin iki farklı anlamda cümlesi.', 22)


def diyafram_nefes_deneyi():
    ic = f'<rect x="8" y="8" width="282" height="96" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Kerem’in Nefes Ölçümü (Mum Üfleme)', 11, KIR)
    ic += yazi(24, 50, 'Göğüsteki el hareketi:', 10.5, LAC, 'start', ince=True)
    ic += f'<rect x="156" y="40" width="110" height="12" rx="4" fill="{KIR}"/>'
    ic += yazi(24, 74, 'Karındaki el hareketi:', 10.5, LAC, 'start', ince=True)
    ic += f'<rect x="156" y="64" width="36" height="12" rx="4" fill="{GRI}"/>'
    ic += yazi(149, 94, 'Göğüs çok, karın az hareket etti.', 10.4, KIR)

    ic += f'<rect x="310" y="8" width="282" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Aslı’nın Nefes Ölçümü (Mum Üfleme)', 11, YESIL_K)
    ic += yazi(326, 50, 'Göğüsteki el hareketi:', 10.5, LAC, 'start', ince=True)
    ic += f'<rect x="458" y="40" width="32" height="12" rx="4" fill="{GRI}"/>'
    ic += yazi(326, 74, 'Karındaki el hareketi:', 10.5, LAC, 'start', ince=True)
    ic += f'<rect x="458" y="64" width="114" height="12" rx="4" fill="{YES}"/>'
    ic += yazi(451, 94, 'Göğüs az, karın çok hareket etti.', 10.4, YESIL_K)
    return svg(600, 112, ic, 'Kerem ve Aslı’nın diyafram nefesi ölçüm kartı: Kerem’de göğüs çok karın az, Aslı’da göğüs az karın çok hareket eder.', 22)


def kavram_davranis_karti():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Kart A (Oyun Davranışı)', 11.2, MAVI)
    ic += yazi(149, 50, 'Toplar patlayınca maçı bırakmayıp', 10.8, LAC, ince=True)
    ic += yazi(149, 70, 'oyunun sürmesi için çözüm aramak', 10.8, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Kart B (Oyun Davranışı)', 11.2, TUR)
    ic += yazi(451, 50, 'Yerde kıvranan arkadaşının yanına', 10.8, LAC, ince=True)
    ic += yazi(451, 70, 'koşup incinen bileğini sarmak', 10.8, LAC, ince=True)
    return svg(600, 102, ic, 'A kartında toplar patlayınca çözüm aramak, B kartında incinen arkadaşının bileğini sarmak davranışları.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tahmin_duraklari_sema()
    s[4]['gorsel'] = nokta_gorev_kartlari()
    s[5]['gorsel'] = gercek_hayal_sahne_panosu()
    s[6]['gorsel'] = acik_bilgi_yorum_panosu()
    s[7]['gorsel'] = arac_secim_dongusu_sema()
    s[8]['gorsel'] = ses_ok_yonu_karti()
    s[9]['gorsel'] = soz_varligi_kavram_agi()
    s[10]['gorsel'] = diyafram_nefes_deneyi()
    s[12]['gorsel'] = kavram_davranis_karti()
