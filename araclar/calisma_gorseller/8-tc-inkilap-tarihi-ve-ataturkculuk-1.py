"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 1. hafta (Avrupa’daki Gelişmeler ve Osmanlı Devleti) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 9.5–11 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def avrupa_gelismeler_semasi():
    """Rönesans, Reform, Aydınlanma ve Sanayi İnkılabı şeması."""
    kartlar = [
        ('Rönesans', 'Hümanizm ve', 'sanat-düşünce', MAVI, MAVI_A, 4),
        ('Reform', 'Kilise dogması', 'yıkıldı', TUR, TUR_A, 92),
        ('Aydınlanma', 'Akıl, deney', 've gözlem', YES, YES_A, 180),
        ('Sanayi İnk.', 'Buhar gücü ve', 'makineleşme', MOR, MOR_A, 268),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 43
        ic += kutu(x, 4, 86, 76, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 9.8, r)
        ic += f'<line x1="{x + 10}" y1="27" x2="{x + 76}" y2="27" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 45, s1, 9.4, LAC, 'middle', True)
        ic += yazi(cx, 61, s2, 9.4, LAC, 'middle', True)
    return svg(358, 84, ic, 'Avrupa daki dört gelişme: Rönesans, Reform, Aydınlanma Çağı ve Sanayi İnkılabı.', 22)


def ihtilal_sanayi_karsilastirma():
    """Fransız İhtilali ve Sanayi İnkılabı'nın Osmanlı'ya etkileri."""
    ic = kutu(4, 4, 172, 84, KIR_A, KIR, 8, 1.4)
    ic += f'<rect x="4" y="4" width="172" height="20" rx="8" fill="{KIR}"/><rect x="4" y="14" width="172" height="10" fill="{KIR}"/>'
    ic += yazi(90, 18, 'Fransız İhtilali (1789)', 10, '#fff')
    ic += yazi(90, 38, 'Milliyetçilik ve eşitlik', 9.4, LAC, 'middle', True)
    ic += yazi(90, 54, 'Çok uluslu yapı sarsıldı', 9.4, LAC, 'middle', True)
    ic += yazi(90, 70, 'Balkanlarda ayaklanmalar', 9.4, KIR, 'middle')

    ic += kutu(184, 4, 172, 84, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="184" y="4" width="172" height="20" rx="8" fill="{MAVI}"/><rect x="184" y="14" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(270, 18, 'Sanayi İnkılabı', 10, '#fff')
    ic += yazi(270, 38, 'Ham madde ve pazar arayışı', 9.4, LAC, 'middle', True)
    ic += yazi(270, 54, 'El tezgâhları zorlandı', 9.4, LAC, 'middle', True)
    ic += yazi(270, 70, 'Ekonomik çöküş ve borçlar', 9.4, MAVI, 'middle')
    return svg(360, 92, ic, 'Fransız İhtilali siyasi etkileri ve Sanayi İnkılabı ekonomik etkileri karşılaştırma kartları.', 22)


def kronoloji_panosu():
    """1839-1909 arası yönetim ve maliye gelişmeleri panosu."""
    adimlar = [
        ('1839', 'Tanzimat', 'Kanun gücü', MAVI, MAVI_A, 4),
        ('1856', 'Islahat', 'Eşit haklar', YES, YES_A, 75),
        ('1876', 'Meşrutiyet', 'Anayasa', TUR, TUR_A, 146),
        ('1881', 'Düyun-u Um.', 'Dış borçlar', KIR, KIR_A, 217),
        ('1909', '31 Mart', 'Bastırıldı', MOR, MOR_A, 288),
    ]
    ic = ''
    for yil, bas, alt, r, z, x in adimlar:
        ic += kutu(x, 4, 68, 68, z, r, 7, 1.3)
        ic += yazi(x + 34, 21, yil, 9.6, r)
        ic += yazi(x + 34, 38, bas, 9.2, r)
        ic += yazi(x + 34, 56, alt, 9.0, LAC, 'middle', True)
    return svg(360, 76, ic, '1839 Tanzimat, 1856 Islahat, 1876 I. Meşrutiyet, 1881 Düyun-u Umumiye ve 1909 31 Mart Olayı kronoloji panosu.', 21)


def demokratiklesme_kartlari():
    """Dört demokratikleşme adımı kartı (3. kartta cumhuriyet hatası)."""
    kartlar = [
        ('1. Kart · 1839 Tanzimat', 'Azınlık hakları güvencede', MAVI, MAVI_A),
        ('2. Kart · 1856 Islahat', 'Yönetime katılım arttı', YES, YES_A),
        ('3. Kart · 1876 I. Meşrutiyet', 'Cumhuriyete geçildi (!)', KIR, KIR_A),
        ('4. Kart · 1908 II. Meşrutiyet', 'Çok partili hayat gelişti', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 9.5, r, 'middle')
        ic += yazi(x + 86, y + 30, cum, 9.2, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört demokratikleşme kartı: 1. Tanzimat, 2. Islahat, 3. I. Meşrutiyet, 4. II. Meşrutiyet.', 22)


def dis_borc_zinciri():
    """Kırım Savaşı dış borç ve 1881 Düyun-u Umumiye süreç zinciri."""
    ic = kutu(4, 4, 352, 78, KUM, GRI, 8, 1.2)
    ic += yazi(180, 19, 'Osmanlı Dış Borçlanma ve Egemenlik Süreci', 10.2, LAC)
    kutular = [
        ('Kırım Savaşı', 'İlk dış borç', MAVI, MAVI_A, 10),
        ('Borç Artışı', 'Ödenemez oldu', TUR, TUR_A, 128),
        ('1881 · Kurum: ?', 'Mali denetim', KIR, KIR_A, 246),
    ]
    for i, (b1, b2, r, z, x) in enumerate(kutular):
        ic += kutu(x, 28, 104, 44, z, r, 6, 1.3)
        ic += yazi(x + 52, 44, b1, 9.6, r)
        ic += yazi(x + 52, 61, b2, 9.4, LAC, 'middle', True)
        if i < 2:
            ax = x + 107
            ic += f'<line x1="{ax}" y1="50" x2="{ax + 14}" y2="50" stroke="{LAC}" stroke-width="1.6"/>'
            ic += f'<polygon points="{ax + 18},50 {ax + 12},46 {ax + 12},54" fill="{LAC}"/>'
    return svg(360, 86, ic, 'Kırım Savaşı ilk dış borç, borçların ödenememesi ve 1881 Düyun-u Umumiye İdaresi zinciri.', 22)


def fikir_akimlari_semasi():
    """Dört fikir akımı ve ortak amaç şeması."""
    ic = kutu(4, 4, 352, 90, '#fff', GRI, 8, 1.3)
    ic += kutu(60, 10, 240, 24, LAC, LAC, 12, 1)
    ic += yazi(180, 26, 'ORTAK AMAÇ: ?', 10.5, '#fff')
    akimlar = [
        ('Osmanlıcılık', 'Eşit yurttaş', MAVI, MAVI_A, 8),
        ('İslamcılık', 'Halife birliği', YES, YES_A, 95),
        ('Türkçülük', 'Dil ve kültür', TUR, TUR_A, 182),
        ('Batıcılık', 'Bilim-teknik', MOR, MOR_A, 269),
    ]
    for bas, alt, r, z, x in akimlar:
        ic += kutu(x, 42, 83, 44, z, r, 6, 1.3)
        ic += yazi(x + 41.5, 58, bas, 9.6, r)
        ic += yazi(x + 41.5, 75, alt, 9.2, LAC, 'middle', True)
    return svg(360, 98, ic, 'Osmanlıcılık, İslamcılık, Türkçülük ve Batıcılık fikir akımlarının ortak amacı şeması.', 22)


def balkan_kayiplar_karti():
    """Balkanlardaki siyasi kayıplar ve toplumsal sonuçlar kartı."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Siyasi (Toprak Kayıpları)', 9.8, MAVI)
    ic += yazi(90, 38, '1829 Edirne: Yunanistan', 9.2, LAC, 'middle', True)
    ic += yazi(90, 54, '1878 Berlin: Sırp, Karadağ', 9.2, LAC, 'middle', True)
    ic += yazi(90, 70, '1908: Girit, Bulgar., Bosna', 9.2, LAC, 'middle', True)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Toplumsal (Sosyal) Sonuç', 9.8, TUR)
    ic += yazi(270, 38, 'Anadolu’ya yoğun göçler', 9.2, LAC, 'middle', True)
    ic += yazi(270, 54, 'Barınma ve gıda sıkıntısı', 9.2, LAC, 'middle', True)
    ic += yazi(270, 70, 'Salgın ve sağlık sorunları', 9.2, TUR, 'middle')
    return svg(360, 90, ic, 'Balkanlardaki siyasi toprak kayıpları ve Anadolu ya göç gibi toplumsal sonuçlar kartı.', 22)


def amac_sonuc_karti():
    """Tanzimat ve Islahat fermanlarında amaç ve gerçekleşen sonuç kartı."""
    ic = kutu(4, 4, 172, 74, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, 'Hedeflenen Amaç', 9.8, YES)
    ic += yazi(90, 41, 'Azınlık haklarını korumak', 9.2, LAC, 'middle', True)
    ic += yazi(90, 59, 'Dış müdahaleyi önlemek', 9.2, LAC, 'middle', True)

    ic += kutu(184, 4, 172, 74, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, 'Gerçekleşen Sonuç', 9.8, KIR)
    ic += yazi(270, 41, 'Avrupa sözünü tutmadı', 9.2, LAC, 'middle', True)
    ic += yazi(270, 59, 'İç işlere müdahale sürdü', 9.2, KIR, 'middle')
    return svg(360, 82, ic, 'Tanzimat ve Islahat fermanlarının amacı ile gerçekleşen sonucu karşılaştırma kartı.', 22)


def osmanlicilik_ipucu_karti():
    """Açık uçlu soru için Osmanlıcılık ipucu kartı."""
    ic = kutu(4, 4, 352, 72, CAM_A, CAM, 8, 1.3)
    ic += yazi(180, 20, 'Osmanlıcılık Fikir Akımı Değerlendirme Kartı', 10.2, CAM)
    ic += yazi(180, 41, '1) Temel ilke: Dil, din ve ırk ayrımı olmadan eşitlik', 9.5, LAC, 'middle', True)
    ic += yazi(180, 60, '2) Sonuç: Balkanlardaki milliyetçi kopuşlarla sona erdi', 9.5, LAC, 'middle', True)
    return svg(360, 80, ic, 'Osmanlıcılık fikir akımının temel ilkesi ve geçerliliğini yitirme nedeni ipucu kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = avrupa_gelismeler_semasi()
    s[1]['gorsel'] = ihtilal_sanayi_karsilastirma()
    s[3]['gorsel'] = kronoloji_panosu()
    s[5]['gorsel'] = demokratiklesme_kartlari()
    s[7]['gorsel'] = dis_borc_zinciri()
    s[8]['gorsel'] = fikir_akimlari_semasi()
    s[9]['gorsel'] = balkan_kayiplar_karti()
    s[10]['gorsel'] = amac_sonuc_karti()
    s[13]['gorsel'] = osmanlicilik_ipucu_karti()
