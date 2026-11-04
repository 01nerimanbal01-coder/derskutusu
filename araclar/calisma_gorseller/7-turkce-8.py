"""7. sınıf Türkçe 8. hafta (Mustafa 1881-1920 Tarihe Atılan İmza: Biyografi, Örtülü Anlam, Geçiş İfadeleri ve Anlam Kayması) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
CAM, CAM_A = '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def biyografi_yapragi_svg():
    ic = f'<rect x="8" y="6" width="584" height="90" rx="10" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'METİN YAPRAĞI : MUSTAFA 1881-1920 TARİHE ATILAN İMZA', 12, KIR)
    ic += yazi(300, 50, '«Mustafa Kemal, Çanakkale’de düşman donanmasının çıkarma yapacağı', 12, LAC, ince=True)
    ic += yazi(300, 70, 'noktayı haftalar öncesinden doğru sezerek birliklerini oraya konuşlandırdı.»', 12, LAC, ince=True)
    ic += yazi(300, 88, 'Anlatıcı : 3. Kişi Ağzı · Belgelere Dayalı Yaşam Öyküsü', 12, MAVI)
    return svg(600, 102, ic, 'Mustafa 1881-1920 Tarihe Atılan İmza biyografi metin yaprağı.', 20)


def kip_kaymasi_fisleri():
    fisler = [
        ('1. Fiş', '1919’da Samsun’a çıkar.', KIR, KIR_A),
        ('2. Fiş', 'Haftaya Ankara’ya gidiyorum.', MAVI, MAVI_A),
        ('3. Fiş', 'Her sabah erken uyanıyor.', YES, YES_A),
        ('4. Fiş', 'Yarın görevli olacaksın.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cumle, renk, arka) in enumerate(fisler):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 48
        ic += f'<rect x="{x}" y="{y}" width="286" height="42" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 42, y + 26, bas, 12, renk)
        ic += f'<line x1="{x + 80}" y1="{y + 6}" x2="{x + 80}" y2="{y + 36}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 182, y + 26, cumle, 12, LAC, ince=True)
    return svg(600, 102, ic, 'Fiillerde anlam kayması dört cümle fişi.', 20)


def dort_cumle_kip_karti():
    kartlar = [
        ('1. Kart', 'Şu an kitap okuyorlar.', MAVI, MAVI_A),
        ('2. Kart', 'Geçen ay müzeyi gezdik.', YES, YES_A),
        ('3. Kart', '1920’de Meclisi açar.', KIR, KIR_A),
        ('4. Kart', 'Yarın sunumu bitireceğiz.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, met, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, met, 12, LAC, ince=True)
    return svg(600, 84, ic, 'Kip ve zaman uyumu dört cümle kartı.', 19)


def ortulu_anlam_levhasi():
    ic = f'<rect x="8" y="6" width="584" height="84" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'ÖRTÜLÜ ANLAM ÇÖZÜMLEME LEVHASI', 12, YES)
    ic += yazi(300, 52, '«Genç Mustafa, Manastır Askerî İdadisinde tarih ve hitabet', 12, LAC)
    ic += yazi(300, 74, 'alanlarıyla DA yakından ilgilenmiştir.»  (İpucu Sözcük : da bağlacı)', 12, MAVI)
    return svg(600, 96, ic, 'Örtülü anlam çözümleme cümle levhası.', 20)


def biyografi_otobiyografi_karti():
    ic = f'<rect x="8" y="6" width="282" height="86" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 28, '1. Kart · Üçüncü Kişi Ağzı', 12, MAVI)
    ic += yazi(149, 52, 'Tanınmış bir kişinin hayatını', 12, LAC, ince=True)
    ic += yazi(149, 72, 'başka bir yazar belgelere dayalı yazar', 12, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="86" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 28, '2. Kart · Birinci Kişi Ağzı', 12, TUR)
    ic += yazi(451, 52, 'Kişi kendi yaşam öyküsünü', 12, LAC, ince=True)
    ic += yazi(451, 72, 'bizzat kendisi kaleme alır', 12, LAC, ince=True)
    return svg(600, 98, ic, 'Biyografi ve otobiyografi karşılaştırma kartları.', 20)


def tarihe_imza_seridi():
    adimlar = [
        ('1881', 'Selanik Doğumu', MAVI, MAVI_A),
        ('Eğitim', 'Askerî Okullar', YES, YES_A),
        ('1915', 'Çanakkale Zaferi', TUR, TUR_A),
        ('1919 - 1920', 'Samsun ve TBMM', KIR, KIR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, '1881-1920 kronolojik yaşam şeridi.', 19)


def gecis_ifadeleri_panosu():
    ic = f'<rect x="8" y="6" width="584" height="88" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'GEÇİŞ VE BAĞLANTI İFADELERİ TABLOSU', 12, MOR)
    ic += yazi(155, 52, 'Buna rağmen : Yön değiştirme', 12, LAC, ince=True)
    ic += yazi(445, 52, 'Başka bir deyişle : Açıklama', 12, LAC, ince=True)
    ic += yazi(155, 76, 'Kısacası : Özetleme ve sonuç', 12, LAC, ince=True)
    ic += yazi(445, 76, 'Üstelik : Zaman önceliği (?)', 12, KIR)
    return svg(600, 100, ic, 'Geçiş ve bağlantı ifadeleri panosu.', 20)


def canlilik_kip_karti():
    ic = f'<rect x="8" y="6" width="584" height="84" rx="10" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'TARİHSEL METİNLERDE ANLAM (ZAMAN) KAYMASI', 12, CAM)
    ic += yazi(300, 52, 'Örnek : «19 Mayıs 1919 sabahı Bandırma Vapuru Samsun’a ulaşır.»', 12, LAC)
    ic += yazi(300, 74, 'Biçim : Geniş zaman (-ır)  ·  Anlam : Geçmiş zaman (ulaştı)  ·  Amaç : ?', 12, KIR)
    return svg(600, 96, ic, 'Tarihsel metinlerde anlam kaymasının anlatıma etkisi kartı.', 20)


def dort_cumle_ortulu_svg():
    kartlar = [
        ('1. Cümle', '...tarih romanını da bitirdim.', YES, YES_A),
        ('2. Cümle', '...1881’de Selanik’te doğdu.', MAVI, MAVI_A),
        ('3. Cümle', '...dedem yine duygulandı.', TUR, TUR_A),
        ('4. Cümle', '...taşımak bile kahramanlıktı.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 48
        ic += f'<rect x="{x}" y="{y}" width="286" height="42" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 48, y + 26, bas, 12, renk)
        ic += f'<line x1="{x + 92}" y1="{y + 6}" x2="{x + 92}" y2="{y + 36}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 188, y + 26, met, 12, LAC, ince=True)
    return svg(600, 102, ic, 'Örtülü anlam incelemesi dört cümle kartı.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = biyografi_yapragi_svg()
    s[1]['gorsel'] = kip_kaymasi_fisleri()
    s[3]['gorsel'] = dort_cumle_kip_karti()
    s[4]['gorsel'] = ortulu_anlam_levhasi()
    s[6]['gorsel'] = biyografi_otobiyografi_karti()
    s[7]['gorsel'] = tarihe_imza_seridi()
    s[8]['gorsel'] = gecis_ifadeleri_panosu()
    s[11]['gorsel'] = canlilik_kip_karti()
    s[12]['gorsel'] = dort_cumle_ortulu_svg()
