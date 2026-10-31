"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 4. hafta (Mustafa Kemal’in Askerlik Hayatı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def gorev_kartlari_semasi():
    """Şam, İstanbul, Fransa ve Trablusgarp görev yerleri bilgi kartları."""
    kartlar = [
        ('Şam (1907’ye dek)', '5. Ordu · Vatan ve Hürriyet', MAVI, MAVI_A),
        ('İstanbul (1909)', '31 Mart · Hareket Ordusu', TUR, TUR_A),
        ('Fransa (1910)', 'Picardie Manevraları', YES, YES_A),
        ('Trablusgarp (1911)', 'Bingazi · Tobruk · Derne', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 11, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört görev yeri kartı: Şam 5. Ordu, İstanbul 31 Mart Hareket Ordusu, Fransa Picardie Manevraları, Trablusgarp Bingazi Tobruk Derne.', 14)


def otuzbir_mart_semasi():
    """31 Mart Olayı sonrasında Hareket Ordusu ve ordu-siyaset ayrımı şeması."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, '13 Nisan 1909 · 31 Mart Olayı', 11, MAVI)
    ic += yazi(90, 38, 'Selânik’te Mahmut Şevket Paşa', 10.5, LAC, 'middle', True)
    ic += yazi(90, 53, 'komutasında Hareket Ordusu', 10.5, LAC, 'middle', True)
    ic += yazi(90, 68, 'kuruldu ve isyanı bastırdı.', 10.5, MAVI)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Mustafa Kemal’in Tutumu', 11, TUR)
    ic += yazi(270, 38, 'İttihatçıların yönetimdeki ağırlığı', 10.5, LAC, 'middle', True)
    ic += yazi(270, 53, 'artınca “Ordu ile siyaset ayrı', 10.5, LAC, 'middle', True)
    ic += yazi(270, 68, 'olmalıdır.” görüşünü savundu.', 10.5, TUR)
    return svg(360, 90, ic, '31 Mart Olayı ve Hareket Ordusu ile Mustafa Kemal in ordu ve siyasetin ayrılması gerektiğine dair tutumu.', 14)


def trablusgarp_panosu():
    """Trablusgarp Savaşı süreç ve Uşi Antlaşması panosu."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'TRABLUSGARP SAVAŞI (1911–1912) VE UŞİ ANTLAŞMASI', 10.5, '#fff')
    adimlar = [
        ('29 Eylül 1911', ['İtalya sömürge', 'için işgal etti'], MAVI, MAVI_A, 10),
        ('18–22 Aralık', ['Gönüllü subaylar', 'direnişi örgütledi'], TUR, TUR_A, 126),
        ('Uşi Antlaşması', ['Trablusgarp gitti,', '12 Ada geçici'], MOR, MOR_A, 242),
    ]
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 32, 108, 56, z, r, 7, 1.2)
        ic += yazi(x + 54, 46, bas, 10.5, r)
        ic += yazi(x + 54, 63, alt[0], 10.5, LAC, 'middle', True)
        ic += yazi(x + 54, 78, alt[1], 10.5, LAC, 'middle', True)
    return svg(360, 100, ic, 'Trablusgarp Savaşı panosu: 29 Eylül 1911 İtalya işgali, 18-22 Aralık gönüllü subaylar ve İtalyanların durdurulması, Uşi Antlaşması.', 14)


def kronoloji_seridi():
    """Şam'dan Sofya'ya 5 görev durağı şeridi."""
    duraklar = [
        ('Şam', '5. Ordu', MAVI, MAVI_A),
        ('Selânik', '3. Ordu', TUR, TUR_A),
        ('Picardie', 'Manevra', YES, YES_A),
        ('Trablusgarp', 'Binbaşı', MOR, MOR_A),
        ('Sofya', 'Ataşemiliter', CAM, CAM_A),
    ]
    ic = ''
    for i, (ust, alt, r, z) in enumerate(duraklar):
        x = 4 + i * 71
        ic += kutu(x, 8, 65, 58, z, r, 7, 1.3)
        ic += yazi(x + 32.5, 28, ust, 10.5, r)
        ic += yazi(x + 32.5, 48, alt, 10.5, LAC, 'middle', True)
    return svg(358, 74, ic, 'Beş görev durağı: Şam 5. Ordu, Selânik 3. Ordu, Picardie Manevra, Trablusgarp Binbaşı, Sofya Ataşemiliter.', 14)


def balkan_neden_sonuc():
    """I. Balkan Savaşı'nın 3 dış/fikrî etkeni ve yenilginin 2 iç nedeni şeması."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Savaşın 3 Temel Etkeni', 11, MAVI)
    ic += yazi(14, 38, '1) Milliyetçilik akımı', 10.5, LAC, 'start', True)
    ic += yazi(14, 54, '2) Panslavizm propagandası', 10.5, LAC, 'start', True)
    ic += yazi(14, 70, '3) Avrupa’nın kışkırtması', 10.5, LAC, 'start', True)

    ic += kutu(184, 4, 172, 82, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, 'Ağır Yenilginin 2 İç Nedeni', 11, KIR)
    ic += yazi(194, 42, '1) Siyasi çekişmeler', 10.5, LAC, 'start', True)
    ic += yazi(194, 62, '2) Ordunun hazırlıksızlığı', 10.5, LAC, 'start', True)
    return svg(360, 90, ic, 'I. Balkan Savaşı nın 3 etkeni ve Osmanlı nın ağır yenilgi almasının 2 iç nedeni.', 14)


def olgu_yorum_kartlari():
    """Olgu ile kişilik özelliği yorumunu bağlayan şema."""
    satirlar = [
        ('Olgu 1: Şam’da Vatan ve Hürriyet’i kurması', 'Vatanseverlik', MAVI, MAVI_A),
        ('Olgu 2: Trablusgarp’a gönüllü gitmesi', '? (Özellik)', TUR, TUR_A),
        ('Olgu 3: Picardie deneyimini uygulaması', '? (Özellik)', YES, YES_A),
    ]
    ic = ''
    for i, (sol, sag, r, z) in enumerate(satirlar):
        y = 4 + i * 29
        ic += kutu(4, y, 244, 25, z, r, 6, 1.2)
        ic += yazi(12, y + 16.5, sol, 10.5, LAC, 'start', True)
        ic += kutu(254, y, 102, 25, '#fff', r, 6, 1.3)
        ic += yazi(305, y + 16.5, sag, 10.5, r)
    return svg(360, 90, ic, 'Üç olgu ve kişilik özelliği eşleştirme şeması.', 14)


def antlasmalar_karsilastirma():
    """Londra, İstanbul ve Atina antlaşmaları karşılaştırma kartları."""
    kartlar = [
        ('Londra (1913)', ['I. Balkan sonu', 'Midye-Enez sınırı'], MAVI, MAVI_A, 4),
        ('İstanbul (1913)', ['Bulgaristan ile', 'Edirne geri alındı', 'Sınır: Meriç Nehri'], YES, YES_A, 122),
        ('Atina (1913)', ['Yunanistan ile', 'Yanya, Selânik ve', 'Girit kaybedildi'], TUR, TUR_A, 240),
    ]
    ic = ''
    for bas, sat, r, z, x in kartlar:
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        ic += yazi(x + 58, 19, bas, 10.5, r)
        for k, s_met in enumerate(sat):
            ic += yazi(x + 58, 37 + k * 16, s_met, 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Londra, İstanbul ve Atina antlaşmalarının sınır ve toprak sonuçları.', 14)


def ikinci_balkan_karti():
    """Londra Antlaşması sonrası II. Balkan Savaşı çıkış ve sonuç kartı."""
    ic = kutu(4, 4, 352, 78, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 20, 'Londra Antlaşması Sonrası II. Balkan Savaşı (29 Haziran 1913)', 11, MOR)
    ic += kutu(12, 28, 164, 46, '#fff', MOR, 6, 1.2)
    ic += yazi(94, 45, 'Neden: Bulgaristan’ın daha', 10.5, LAC, 'middle', True)
    ic += yazi(94, 62, 'çok toprak alması', 10.5, MOR)
    ic += kutu(184, 28, 164, 46, '#fff', YES, 6, 1.2)
    ic += yazi(266, 45, 'Osmanlı: Enver Paşa ile Edirne', 10.5, LAC, 'middle', True)
    ic += yazi(266, 62, 've Kırklareli’ni geri aldı', 10.5, YES)
    return svg(360, 86, ic, 'II. Balkan Savaşı nın çıkışı ve Osmanlı nın Edirne ile Kırklareli ni geri alması.', 14)


def ordu_siyaset_karsilastirma():
    """Mustafa Kemal'in 1909 uyarısı ile 1912 I. Balkan Savaşı sonucu karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, '1909 · Mustafa Kemal’in Görüşü', 10.5, MAVI)
    ic += yazi(90, 42, '“Ordu mensupları siyasetten', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, 'ayrı kalmalıdır.”', 10.5, LAC)

    ic += kutu(184, 4, 172, 74, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, '1912 · I. Balkan Savaşı Sonucu', 10.5, KIR)
    ic += yazi(270, 42, 'Subaylar arasındaki siyasi', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, 'çekişmeler ağır yenilgi getirdi.', 10.5, KIR)
    return svg(360, 82, ic, '1909 da Mustafa Kemal in ordu-siyaset ayrımı görüşü ve 1912 I. Balkan Savaşı ndaki siyasi çekişme yenilgisi.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = gorev_kartlari_semasi()
    s[1]['gorsel'] = otuzbir_mart_semasi()
    s[5]['gorsel'] = trablusgarp_panosu()
    s[6]['gorsel'] = kronoloji_seridi()
    s[7]['gorsel'] = balkan_neden_sonuc()
    s[8]['gorsel'] = olgu_yorum_kartlari()
    s[9]['gorsel'] = antlasmalar_karsilastirma()
    s[10]['gorsel'] = ikinci_balkan_karti()
    s[13]['gorsel'] = ordu_siyaset_karsilastirma()
