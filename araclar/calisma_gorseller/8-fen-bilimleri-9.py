"""8. sınıf Fen Bilimleri 9. hafta (Biyoteknoloji ve Genetik Mühendisliği) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:14mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.6):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def insulin_uretim_asamasi():
    """Soru 2 (s[1]): Genetik mühendisliği (1. aşama) ve Biyoteknoloji (2. aşama) şeması."""
    ic = kutu(4, 4, 168, 86, MAVI_A, MAVI, 8)
    ic += yazi(88, 22, '1. Aşama (Moleküler Yöntem)', MAVI, boy=10.4)
    ic += yazi(88, 44, 'İnsülin geninin kesilerek', LAC, ince=True, boy=10.0)
    ic += yazi(88, 62, 'bakteri DNA’sına aktarılması', LAC, ince=True, boy=10.0)
    ic += yazi(88, 80, 'Bilim Dalı: ?', MAVI)

    ic += f'<path d="M174 47 L186 47" stroke="{LAC}" stroke-width="2"/>'
    ic += kutu(188, 4, 168, 86, YES_A, YES, 8)
    ic += yazi(272, 22, '2. Aşama (Endüstriyel Ürün)', YESIL_K, boy=10.4)
    ic += yazi(272, 44, 'Bakterilerin çoğaltılarak', LAC, ince=True, boy=10.0)
    ic += yazi(272, 62, 'insülin ilacının şişelenmesi', LAC, ince=True, boy=10.0)
    ic += yazi(272, 80, 'Teknoloji Alanı: ?', YESIL_K)
    return svg(360, 94, ic, 'Bakteride insülin geni aktarımı ve ilaç üretimi iki aşamalı şeması.', 15)


def dort_uygulama_yontem_karti():
    """Soru 3 (s[2]): Gen aktarımı, gen tedavisi, ıslah ve geleneksel biyoteknoloji kartları."""
    kartlar = [
        (4, 4, '1. Ateş Böceği Geni', 'Tütün bitkisinde parlama', MAVI, MAVI_A),
        (184, 4, '2. Kusurlu Gen Onarımı', 'Sağlıklı genin eklenmesi', YES, YES_A),
        (4, 52, '3. Verimli Buğday Seçimi', 'Üstün tohum çaprazlaması', TUR, TUR_A),
        (184, 52, '4. Sütten Yoğurt Yapımı', 'Maya bakterisi fermantasyonu', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.4)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.8)
    return svg(360, 100, ic, 'Dört biyoteknoloji ve genetik mühendisliği uygulama kartı.', 15)


def klonlama_prs_sema():
    """Soru 6 (s[5]): P (çekirdek), R (çekirdeksiz yumurta), S (taşıyıcı) -> T kuzusu klonlama şeması."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Klonlama Deneyi · P, R, S Koyunları ve T Kuzusu', KAHVE)
    kartlar = [
        (10, 'P Koyunu', 'Meme hücresi', 'ÇEKİRDEĞİ (DNA)', MAVI, MAVI_A),
        (100, 'R Koyunu', 'Çekirdeksiz', 'yumurta sitoplazması', TUR, TUR_A),
        (190, 'S Koyunu', 'Embriyoyu taşıyan', 'taşıyıcı anne', MOR, MOR_A),
        (280, 'T Kuzusu', 'Doğurulan', 'KLON YAVRU', YES, YES_A),
    ]
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 26, 70 if x == 280 else 84, 60, z, r, 6)
        w2 = 35 if x == 280 else 42
        ic += yazi(x + w2, 42, bas, r, boy=9.8)
        ic += yazi(x + w2, 59, s1, LAC, ince=True, boy=8.8)
        ic += yazi(x + w2, 75, s2, r if x in (10, 280) else LAC, boy=8.8)
    return svg(360, 96, ic, 'P koyunu çekirdeği, R koyunu yumurtası ve S taşıyıcı koyundan T klon kuzusunun oluşumu.', 15)


def geleneksel_modern_kartlar():
    """Soru 7 (s[6]): 4 biyoteknoloji kartı (I. kart geleneksel, diğerleri modern)."""
    kartlar = [
        (4, 4, 'I. Kart · Fermantasyon', 'Hamur mayalama · Sirke', YES, YES_A),
        (184, 4, 'II. Kart · Gen Aktarımı', 'Antifriz genli domates', MAVI, MAVI_A),
        (4, 52, 'III. Kart · 3B Biyoyazıcı', 'Kök hücreden yapay doku', MOR, MOR_A),
        (184, 52, 'IV. Kart · Klonlama', 'Vücut çekirdeğiyle kopya', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.3)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.8)
    return svg(360, 100, ic, 'Geleneksel ve modern biyoteknoloji örnek kartları.', 15)


def gdo_misir_ekosistem_karti():
    """Soru 8 (s[7]): Böcek dirençli GDO'lu mısırın arı ve kelebeklere etkisi."""
    ic = kutu(4, 4, 172, 82, TUR_A, TUR, 8)
    ic += yazi(90, 22, 'Uygulama: GDO’lu Mısır', TUR)
    ic += yazi(90, 44, 'Zararlı böceklere karşı', LAC, ince=True, boy=10.0)
    ic += yazi(90, 62, 'toksin üreten gen eklendi', LAC, ince=True, boy=10.0)

    ic += kutu(184, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(270, 22, 'Tarladaki Gözlem Sonucu', KIR)
    ic += yazi(270, 44, 'Yararlı bal arısı ve kelebek', LAC, ince=True, boy=10.0)
    ic += yazi(270, 62, 'popülasyonu hızla azaldı!', KIR, boy=10.0)
    return svg(360, 90, ic, 'GDOlu mısır tarlasında arı ve kelebek sayısının azalması gözlem kartı.', 15)


def plazmit_gen_aktarim_akis():
    """Soru 9 (s[8]): Bakteri plazmitine gen aktarımı 4 adımlı şema."""
    adimlar = [
        (4, '1. Kesme', 'İnsan genini', 'DNA’dan ayır', MAVI, MAVI_A),
        (93, '2. Bağlama', 'Geni bakteri', 'plazmitine ekle', TUR, TUR_A),
        (182, '3. Aktarma', 'Plazmiti', 'bakteriye ver', MOR, MOR_A),
        (271, '4. Üretim', 'Çoğaltıp ilaç', 'olarak saflaştır', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.3)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.6)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.6)
    return svg(360, 88, ic, 'Bakteri plazmitine gen aktarımıyla hormon üretimi 4 aşamalı şeması.', 14)


def gelecek_ve_risk_panosu():
    """Soru 10 (s[9]): Gelecekteki hedefler ve günümüzdeki riskler panosu."""
    ic = kutu(4, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(90, 21, 'Gelecekteki Olumlu Hedefler', YESIL_K, boy=10.2)
    ic += yazi(90, 43, '• Kök hücreden yapay organ', LAC, ince=True, boy=9.6)
    ic += yazi(90, 61, '• DNA’ya uygun kişisel ilaç', LAC, ince=True, boy=9.6)
    ic += yazi(90, 79, '• Genetik hastalık onarımı', YESIL_K, boy=9.6)

    ic += kutu(184, 4, 172, 86, KIR_A, KIR, 8)
    ic += yazi(270, 21, 'Ekolojik ve Sağlık Riskleri', KIR, boy=10.2)
    ic += yazi(270, 43, '• GDO kaynaklı alerji riski', LAC, ince=True, boy=9.6)
    ic += yazi(270, 61, '• Doğal türlere gen kaçışı', LAC, ince=True, boy=9.6)
    ic += yazi(270, 79, '• Biyoçeşitliliğin azalması', KIR, boy=9.6)
    return svg(360, 94, ic, 'Biyoteknolojinin gelecekteki hedefleri ve ekolojik riskleri panosu.', 15)


def sigir_islah_gozlem_karti():
    """Soru 12 (s[11]): İki sığır ırkının eşleştirilmesiyle verimli döl elde edilmesi (ıslah)."""
    ic = kutu(4, 4, 352, 84, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Hayvancılıkta Üstün Irk Elde Etme Çalışması', MAVI)
    ic += kutu(10, 28, 104, 52, '#fff', TUR, 6)
    ic += yazi(62, 46, '1. Sığır Irkı', TUR, boy=10.0)
    ic += yazi(62, 66, 'Az süt · Dirençli', LAC, ince=True, boy=9.4)

    ic += yazi(122, 56, 'x', LAC)
    ic += kutu(130, 28, 104, 52, '#fff', MOR, 6)
    ic += yazi(182, 46, '2. Sığır Irkı', MOR, boy=10.0)
    ic += yazi(182, 66, 'Bol süt · Duyarlı', LAC, ince=True, boy=9.4)

    ic += yazi(242, 56, '->', YESIL_K)
    ic += kutu(252, 28, 98, 52, YES_A, YES, 6)
    ic += yazi(301, 46, 'Yeni Yavru Döl', YESIL_K, boy=10.0)
    ic += yazi(301, 66, 'Bol süt · Dirençli', YESIL_K, boy=9.4)
    return svg(360, 92, ic, 'İki farklı sığır ırkının çaprazlanmasıyla hem bol süt veren hem dirençli döl elde edilmesi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = insulin_uretim_asamasi()
    s[2]['gorsel'] = dort_uygulama_yontem_karti()
    s[5]['gorsel'] = klonlama_prs_sema()
    s[6]['gorsel'] = geleneksel_modern_kartlar()
    s[7]['gorsel'] = gdo_misir_ekosistem_karti()
    s[8]['gorsel'] = plazmit_gen_aktarim_akis()
    s[9]['gorsel'] = gelecek_ve_risk_panosu()
    s[11]['gorsel'] = sigir_islah_gozlem_karti()
