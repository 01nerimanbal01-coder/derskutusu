"""6. sınıf Sosyal Bilgiler 7. hafta (Ülkemizin, Kıtaların ve Okyanusların Konum Özellikleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def turkiye_koordinat_sema():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 21, 'Türkiye’nin Mutlak (Matematik) Konum Koordinat Çerçevesi', 11.2, LAC)
    ic += yazi(300, 36, '42° Kuzey Paraleli (Sinop - İnceburun)', 10.1, YESIL_K)
    ic += f'<rect x="130" y="42" width="340" height="46" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(300, 69, 'TÜRKİYE (Anadolu ve Trakya)', 11.2, MAVI)
    ic += yazi(300, 102, '36° Kuzey Paraleli (Hatay - Beysun)', 10.1, YESIL_K)
    ic += yazi(68, 62, '26° Doğu', 10.4, TUR)
    ic += yazi(68, 76, '(Çanakkale)', 10.0, LAC, ince=True)
    ic += yazi(532, 62, '45° Doğu', 10.4, TUR)
    ic += yazi(532, 76, '(Iğdır)', 10.0, LAC, ince=True)
    return svg(600, 116, ic, 'Türkiye’nin 36-42 Kuzey paralelleri ile 26-45 Doğu meridyenleri arasındaki mutlak konum çerçevesi.', 22)


def dort_ozellik_panosu():
    kartlar = [
        ('1. Özellik', 'Kuzey Yarım Küre Orta', 'Kuşak’ta yer alması', MAVI, MAVI_A),
        ('2. Özellik', 'Kuzeye gidildikçe güneş', 'açısının küçülmesi', TUR, TUR_A),
        ('3. Özellik', 'Doğuya gidildikçe yükseltinin', 'artması', YES, YES_A),
        ('4. Özellik', 'Doğu-batı arasında 76 dk', 'saat farkı olması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 56
        ic += f'<rect x="{x}" y="{y}" width="286" height="48" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="48" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, bas, 10.8, renk, 'start')
        ic += yazi(x + 18, y + 36, f'{s1} {s2}', 10.1, LAC, 'start', ince=True)
    return svg(600, 120, ic, 'Türkiye’ye ait dört coğrafi özellik kartı: 1, 2 ve 4 mutlak konum; 3 yükselti artışı göreceli konum.', 23)


def konum_durum_kartlari():
    kartlar = [
        ('1. Kart', 'Yıl içinde dört mevsimin', 'belirgin yaşanması', MAVI, MAVI_A),
        ('2. Kart', 'Aynı günde hem kayak', 'hem deniz yapılabilmesi', YES, YES_A),
        ('3. Kart', 'Akdeniz’in Karadeniz’den', 'daha tuzlu olması', TUR, TUR_A),
        ('4. Kart', 'TANAP ve TürkAkım', 'enerji boru hatları', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 11.0, renk)
        ic += f'<line x1="{x + 14}" y1="33" x2="{x + 122}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 52, s1, 10.2, LAC)
        ic += yazi(x + 68, 70, s2, 10.2, LAC, ince=True)
    return svg(600, 100, ic, 'Dört coğrafi durum kartı: yıl içinde dört mevsim, aynı günde kayak ve deniz, Akdeniz tuzluluğu, enerji hatları.', 22)


def meridyen_saat_cizelgesi():
    ic = f'<rect x="8" y="8" width="584" height="86" rx="10" fill="{KUM}" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Türkiye Meridyen ve Yerel Saat Farkı Çizelgesi (1 Meridyen = 4 Dakika)', 11.2, KAHVE)
    ic += f'<line x1="80" y1="60" x2="520" y2="60" stroke="{LAC}" stroke-width="2.2"/>'
    ic += f'<circle cx="130" cy="60" r="6" fill="{MAVI}"/>'
    ic += yazi(130, 46, 'Bursa (29° Doğu)', 10.6, MAVI)
    ic += yazi(130, 80, 'Batıda', 10.1, LAC, ince=True)

    ic += f'<circle cx="470" cy="60" r="6" fill="{TUR}"/>'
    ic += yazi(470, 46, 'Diyarbakır (41° Doğu)', 10.6, TUR)
    ic += yazi(470, 80, 'Doğuda', 10.1, LAC, ince=True)

    ic += yazi(300, 48, 'Fark: 41° − 29° = 12 meridyen', 10.4, YESIL_K)
    return svg(600, 102, ic, '29 Doğu Bursa ile 41 Doğu Diyarbakır arasındaki 12 meridyenlik yerel saat çizelgesi.', 22)


def kitalar_yuzolcumu_kartlari():
    kitalar = [
        ('Asya Kıtası', '44,5 milyon km²', '(En büyük kıta)', MAVI, MAVI_A),
        ('Afrika Kıtası', '30,3 milyon km²', '(2. büyük kıta)', TUR, TUR_A),
        ('Kuzey Amerika', '24,7 milyon km²', '(3. büyük kıta)', YES, YES_A),
        ('Avrupa Kıtası', '10,1 milyon km²', '(6. sırada yer alır)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, olcum, sira, renk, arka) in enumerate(kitalar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 10.9, renk)
        ic += yazi(x + 68, 50, olcum, 10.6, LAC)
        ic += yazi(x + 68, 72, sira, 10.1, LAC, ince=True)
    return svg(600, 100, ic, 'Asya, Afrika, Kuzey Amerika ve Avrupa kıtalarının yüz ölçümü büyüklükleri.', 22)


def ruzgar_tuzluluk_sema():
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, 'Türkiye’de Rüzgâr Yönleri ve Denizlerin Tuzluluk Sıralaması', 11.3, LAC)
    kutular = [
        ('Kuzeyden Esen Rüzgârlar', 'Karayel, Yıldız, Poyraz', 'Kutup yönünden gelir → Soğutur', MAVI, MAVI_A),
        ('Denizlerin Tuzluluk Oranı', 'Akdeniz > Ege > Marmara', '> Karadeniz (Kuzeye azalır)', YES, YES_A),
        ('Güneyden Esen Rüzgârlar', 'Kıble, Lodos, Samyeli', 'Ekvator yönünden gelir → Isıtır', KIR, '#fdeaea'),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 16 + i * 192
        ic += f'<rect x="{x}" y="32" width="180" height="60" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 48, bas, 10.6, renk)
        ic += yazi(x + 90, 65, s1, 10.1, LAC)
        ic += yazi(x + 90, 81, s2, 10.0, LAC, ince=True)
    return svg(600, 108, ic, 'Türkiye’de kuzeyden ve güneyden esen rüzgârların sıcaklığa etkisi ve deniz tuzluluğu sıralaması.', 22)


def kuresel_koordinat_duzlemi():
    ic = f'<rect x="8" y="6" width="584" height="94" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 22, 'Küresel Koordinat Düzlemi · Yarım Küre Bölgeleri', 11.2, LAC)
    ic += f'<rect x="90" y="30" width="205" height="30" rx="6" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(192, 49, '2. Bölge (Kuzey - Batı)', 10.4, TUR)
    ic += f'<rect x="305" y="30" width="205" height="30" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(407, 49, '1. Bölge (Kuzey - Doğu)', 10.6, YESIL_K)
    ic += f'<rect x="90" y="64" width="205" height="30" rx="6" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(192, 83, '3. Bölge (Güney - Batı)', 10.4, MOR)
    ic += f'<rect x="305" y="64" width="205" height="30" rx="6" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(407, 83, '4. Bölge (Güney - Doğu)', 10.4, MAVI)
    ic += f'<line x1="300" y1="26" x2="300" y2="98" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="80" y1="62" x2="520" y2="62" stroke="{KIR}" stroke-width="2"/>'
    ic += yazi(556, 65, '0° Ekvator', 10.0, KIR)
    return svg(600, 106, ic, 'Ekvator ve Başlangıç Meridyeni ile ayrılan dört yarım küre bölgesi.', 22)


def sicaklik_karsilastirma_kartlari():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Durum: Hatay ve Sinop', 11.2, MAVI)
    ic += yazi(149, 48, 'Güneydeki Hatay (36°K), kuzeydeki', 10.3, LAC, ince=True)
    ic += yazi(149, 65, 'Sinop’tan (42°K) daha sıcaktır.', 10.3, LAC, ince=True)
    ic += yazi(149, 82, '(Neden: Ekvator’a yakınlık ve enlem)', 10.2, MAVI)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Durum: İzmir ve Van', 11.2, TUR)
    ic += yazi(451, 48, 'Yaklaşık aynı enlemdeki İzmir, doğudaki', 10.3, LAC, ince=True)
    ic += yazi(451, 65, 'Van’dan çok daha sıcaktır.', 10.3, LAC, ince=True)
    ic += yazi(451, 82, '(Neden: Deniz kıyısı ve yükselti farkı)', 10.2, TUR)
    return svg(600, 102, ic, 'Hatay-Sinop enlem sıcaklık farkı ile İzmir-Van yükselti sıcaklık farkı karşılaştırma kartları.', 22)


def jeopolitik_konum_karti():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'Türkiye’nin Jeopolitik Konumu · Ulaşım ve Enerji Köprüsü', 11.3, KAHVE)
    unsurlar = [
        ('Boğazlar ve Denizler', 'İstanbul ve Çanakkale Boğazları', 'Karadeniz’i dünyaya bağlar.', MAVI, MAVI_A),
        ('Enerji Koridoru', 'TANAP, TürkAkım ve BTC', 'boru hatları Avrupa’ya uzanır.', TUR, TUR_A),
        ('Kıtalar Kavşağı', 'Asya ile Avrupa arasındaki', 'transit ticaret merkezidir.', YES, YES_A),
    ]
    for i, (bas, s1, s2, renk, arka) in enumerate(unsurlar):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 50, bas, 10.7, renk)
        ic += yazi(x + 90, 66, s1, 10.1, LAC)
        ic += yazi(x + 90, 80, s2, 10.0, LAC, ince=True)
    return svg(600, 104, ic, 'Türkiye’nin boğazları, enerji boru hatları ve kıtalar arası kavşak konumunu gösteren kart.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = turkiye_koordinat_sema()
    s[4]['gorsel'] = dort_ozellik_panosu()
    s[5]['gorsel'] = konum_durum_kartlari()
    s[6]['gorsel'] = meridyen_saat_cizelgesi()
    s[7]['gorsel'] = kitalar_yuzolcumu_kartlari()
    s[8]['gorsel'] = ruzgar_tuzluluk_sema()
    s[9]['gorsel'] = kuresel_koordinat_duzlemi()
    s[10]['gorsel'] = sicaklik_karsilastirma_kartlari()
    s[12]['gorsel'] = jeopolitik_konum_karti()
